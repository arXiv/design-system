#!/usr/bin/env python3
"""Agent build tests for the design system. One round = one spec, built several times.

  round.py build    tests/<name> [--models a,b] [--reps 2] [--budget 10]
  round.py evaluate runs/<run>          computed checks + screenshots (needs playwright)
  round.py review   runs/<run>          serves the blind visual review; saves review.json
  round.py summary  runs/<run>          writes summary.html (the detailed record) and rebuilds runs/index.html
  round.py report   runs/<run>          writes report.html, the one-page report for the team

The protocol is in README.md. Builds are labelled A, B, C... in shuffled order;
key.json maps labels to models and is only shown in the summary.
"""
import argparse
import hashlib
import html
import json
import os
import random
import re
import shutil
import string
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
MODELS = ["claude-sonnet-5-5", "claude-opus-5-5"]
# What a builder never sees: the tests and their scoring, and Shamsi's working files.
EXCLUDE = [".git", "verification", "whiteboard", "node_modules", ".claude", "__pycache__", ".DS_Store"]
SCRUB = re.compile(r"^(CLAUDE|ANTHROPIC|USE_(STAGING|LOCAL)_OAUTH|AI_AGENT|BAGGAGE)", re.I)
AXE = HERE.parent / "node_modules/axe-core/axe.min.js"
VERDICTS = {"accept": "Accept", "changes": "Accept with changes", "reject": "Reject"}


def esc(s):
    return html.escape(str(s))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tree(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): sha(p) for p in root.rglob("*") if p.is_file()}


def cells_of(run: Path):
    return sorted(p.parent for p in run.glob("*/metrics.json"))


def load(path: Path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


# ── build ────────────────────────────────────────────────────────────────────

def parse_transcript(path: Path) -> dict:
    m = {"file_reads": [], "files_written": [], "bash": [], "web": [], "final_message": "",
         "usage": {}, "cost_usd": None, "num_turns": None, "is_error": None}
    if not path.exists():
        return m
    for line in path.read_text(errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for block in (ev.get("message") or {}).get("content") or []:
                if block.get("type") != "tool_use":
                    continue
                name, inp = block.get("name", "?"), block.get("input") or {}
                if name == "Read" and inp.get("file_path"):
                    m["file_reads"].append(inp["file_path"])
                elif name in ("Write", "Edit") and inp.get("file_path"):
                    m["files_written"].append(inp["file_path"])
                elif name == "Bash":
                    m["bash"].append(inp.get("command", "")[:200])
                elif name in ("WebFetch", "WebSearch"):
                    m["web"].append(inp.get("url") or inp.get("query") or "")
        elif ev.get("type") == "result":
            m.update(is_error=bool(ev.get("is_error")), usage=ev.get("usage") or {},
                     cost_usd=ev.get("total_cost_usd"), num_turns=ev.get("num_turns"),
                     final_message=ev.get("result") or "")
    m["unique_files_read"] = len(set(m["file_reads"]))
    return m


STOP = threading.Event()   # set when a build reports usage beyond the plan


def plan_only():
    """Builds run on the Claude subscription. Refuse to start if an API key would be billed."""
    env = {k: v for k, v in os.environ.items() if not SCRUB.match(k)}
    out = subprocess.run(["claude", "auth", "status"], env=env, capture_output=True, text=True).stdout
    try:
        st = json.loads(out)
    except json.JSONDecodeError:
        sys.exit("could not read `claude auth status`; not starting any build")
    if st.get("authMethod") != "claude.ai" or not st.get("subscriptionType"):
        sys.exit(f"not signed in with a Claude subscription (authMethod={st.get('authMethod')}); not starting any build")
    for f in (Path.home() / ".claude/settings.json", Path.home() / ".claude/settings.local.json"):
        cfg = load(f, {})
        if cfg.get("apiKeyHelper") or any(k in (cfg.get("env") or {}) for k in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")):
            sys.exit(f"{f} configures an API key; not starting any build")


def build_cell(cell: Path, model: str, prompt: str, budget: float):
    if STOP.is_set():
        print(f"  {cell.name}: not started", flush=True)
        return
    ws = Path(tempfile.mkdtemp(prefix="dsround-"))
    repo = ws / "repo"
    subprocess.run(["rsync", "-a", *[f"--exclude={e}" for e in EXCLUDE], f"{REPO}/", f"{repo}/"], check=True)
    before = tree(repo)
    env = {k: v for k, v in os.environ.items() if not SCRUB.match(k)}
    start = time.time()
    with open(cell / "transcript.jsonl", "w") as out, open(cell / "stderr.log", "w") as err:
        try:
            status = subprocess.run(
                ["claude", "-p", prompt, "--model", model, "--permission-mode", "bypassPermissions",
                 "--setting-sources", "project", "--max-budget-usd", str(budget),
                 "--output-format", "stream-json", "--verbose"],
                cwd=repo, env=env, stdout=out, stderr=err, timeout=60 * 60).returncode
        except subprocess.TimeoutExpired:
            status = "timeout"
    after = tree(repo)
    new = sorted(r for r in after if r not in before)
    modified = sorted(r for r in after if r in before and after[r] != before[r])
    for rel in new + modified:
        dest = cell / "build" / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(repo / rel, dest)
    m = parse_transcript(cell / "transcript.jsonl")
    if re.search(r'"isUsingOverage"\s*:\s*true', (cell / "transcript.jsonl").read_text(errors="replace")):
        m["used_overage"] = True
        STOP.set()
        print(f"  {cell.name}: this build went beyond the plan's included usage; no further builds will start", flush=True)
    for prefix in (str(repo.resolve()) + "/", str(repo) + "/"):
        m["file_reads"] = [f.replace(prefix, "") for f in m["file_reads"]]
    m.update(exit=status, wall_seconds=int(time.time() - start), new_files=new,
             modified_existing=modified, deleted=sorted(r for r in before if r not in after))
    (cell / "metrics.json").write_text(json.dumps(m, indent=2))
    (cell / "final-message.md").write_text(m["final_message"])
    shutil.rmtree(ws, ignore_errors=True)
    print(f"  {cell.name}: {len(new)} new files, {len(modified)} existing files modified, "
          f"${m['cost_usd']}, {m['wall_seconds']}s, exit {status}", flush=True)


def snapshot(run: Path):
    """Keep the stylesheets and scripts as they were for this run, so later changes to the
    design system do not change how these builds look."""
    (run / "snapshot/docs").mkdir(parents=True, exist_ok=True)
    for f in (REPO / "docs").iterdir():
        if f.suffix in (".css", ".js"):
            shutil.copy2(f, run / "snapshot/docs" / f.name)


def build(args):
    plan_only()
    test = Path(args.test).resolve()
    prompt = (test / "spec.md").read_text()
    if (test / "content.md").exists():
        prompt += "\n\n---\n\n" + (test / "content.md").read_text()
    run = HERE / "runs" / f"{time.strftime('%Y%m%d-%H%M%S')}-{test.name}"
    run.mkdir(parents=True)
    jobs = [(m, r) for m in args.models.split(",") for r in range(1, args.reps + 1)]
    random.shuffle(jobs)
    key = {string.ascii_uppercase[i]: {"model": m, "rep": r} for i, (m, r) in enumerate(jobs)}
    (run / "key.json").write_text(json.dumps(key, indent=2))
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPO, capture_output=True, text=True).stdout.strip()
    dirty = bool(subprocess.run(["git", "status", "--porcelain", "docs", "AGENTS.md"], cwd=REPO,
                                capture_output=True, text=True).stdout.strip())
    (run / "run.json").write_text(json.dumps({
        "test": test.name, "date": time.strftime("%Y-%m-%d"), "commit": commit,
        "uncommitted_docs_changes": dirty, **load(test / "test.json", {})}, indent=2))
    shutil.copy2(test / "spec.md", run / "spec.md")
    snapshot(run)
    print(f"run {run.name}: {len(jobs)} builds (labels hide the model)", flush=True)
    with ThreadPoolExecutor(max_workers=args.parallel) as pool:
        for label in key:
            (run / label).mkdir()
            pool.submit(build_cell, run / label, key[label]["model"], prompt, args.budget)
    print(f"next: python3 {Path(__file__).name} evaluate {run.relative_to(HERE)}")


# ── serving a build: its own files first, the repo for everything else ───────

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, run=None, **kw):
        self.run = run
        super().__init__(*a, **kw)

    def log_message(self, *a):
        pass

    def translate_path(self, path):
        parts = unquote(urlparse(path).path).lstrip("/").split("/")
        if parts[0] == "b" and len(parts) > 2:
            rel = Path(*parts[2:])
            if ".." in rel.parts:
                return str(self.run / "missing")
            for root in (self.run / parts[1] / "build", self.run / "snapshot", REPO):
                if (root / rel).exists():
                    return str(root / rel)
            return str(REPO / rel)
        if parts[0] == "shots" and len(parts) == 3:
            return str(self.run / parts[1] / "shots" / parts[2])
        return str(self.run / "missing")

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if urlparse(self.path).path == "/":
            body = review_page(self.run).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            super().do_GET()

    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        (self.run / "review.json").write_text(json.dumps(data, indent=2))
        self.send_response(204)
        self.end_headers()


def serve(run: Path, port: int):
    srv = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, run=run))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


# ── evaluate ─────────────────────────────────────────────────────────────────

PAGE_JS = """() => {
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 };
  return {
    lang: document.documentElement.lang, title: document.title,
    h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim().replace(/\\s+/g, ' ').slice(0, 120)),
    headings: [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(vis).map(h => h.tagName + ' ' + h.textContent.trim().replace(/\\s+/g, ' ').slice(0, 60)),
    landmarks: ['header', 'nav', 'main', 'footer', 'form', '[role=search]', '[role=status]', '[aria-live]'].filter(s => document.querySelector(s)),
    style_blocks: document.querySelectorAll('style').length,
    inline_styles: [...document.querySelectorAll('[style]')].map(e => e.tagName.toLowerCase() + ': ' + e.getAttribute('style')).slice(0, 20),
    classes: [...new Set([...document.querySelectorAll('[class]')].flatMap(e => [...e.classList]))].sort(),
    stylesheets: [...document.querySelectorAll('link[rel=stylesheet]')].map(l => l.getAttribute('href')),
    scripts: [...document.querySelectorAll('script')].map(s => s.getAttribute('src') || 'inline (' + s.textContent.length + ' chars)'),
    handlers: document.querySelectorAll('[onclick],[onchange],[onsubmit]').length,
    placeholders: [...document.querySelectorAll('[placeholder]')].map(e => e.getAttribute('placeholder')),
    text_length: document.body.innerText.length,
  }
}"""
OVERFLOW_JS = "() => document.documentElement.scrollWidth - document.documentElement.clientWidth"
FOCUS_JS = """() => { const e = document.activeElement; if (!e || e === document.body) return null;
  const s = getComputedStyle(e);
  return { what: e.tagName.toLowerCase() + ' "' + (e.getAttribute('aria-label') || e.textContent || e.value || e.name || '').trim().replace(/\\s+/g, ' ').slice(0, 40) + '"',
    indicator: (s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0) || s.boxShadow !== 'none' } }"""
AXE_JS = """opts => axe.run(document, opts).then(r => r.violations.map(v => ({ id: v.id, impact: v.impact, help: v.help,
  count: v.nodes.length, where: v.nodes.slice(0, 3).map(n => n.target.join(' ')) })))"""


def css_classes(path: Path) -> set:
    if not path.exists():
        return set()
    text = re.sub(r"/\*.*?\*/", "", path.read_text(errors="replace"), flags=re.S)
    return set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", re.sub(r"\{[^{}]*\}", "{}", text)))


def css_hexes(text: str) -> set:
    return {h.lower() for h in re.findall(r"#([0-9a-fA-F]{3,8})\b", text)}


def own_css_report(cell: Path, own_rel: str, palette: set) -> dict:
    own = cell / "build" / own_rel if own_rel else None
    if not own or not own.exists():
        return {"exists": False}
    text = re.sub(r"/\*.*?\*/", "", own.read_text(errors="replace"), flags=re.S)
    decls = re.findall(r"([\w-]+)\s*:\s*([^;{}]+)[;}]", text)
    return {"exists": True, "rules": text.count("{"), "declarations": len(decls),
            "uses_tokens": sum("var(--ds-" in v for _, v in decls),
            "new_custom_properties": sorted({p for p, _ in decls if p.startswith("--")}),
            "hexes_not_in_design_system": sorted(css_hexes(text) - palette),
            "classes": sorted(css_classes(own))}


def evaluate(args):
    from playwright.sync_api import sync_playwright
    run = Path(args.run).resolve()
    info = load(run / "run.json")
    docs = run / "snapshot/docs" if (run / "snapshot/docs").exists() else REPO / "docs"
    ds_css = docs / "design-system.css"
    ds = css_classes(ds_css) | css_classes(docs / "internal-tools.css")
    docs_only = css_classes(docs / "docs.css") - ds
    palette = css_hexes(ds_css.read_text())
    srv = serve(run, 0)
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for cell in cells_of(run):
            mx = load(cell / "metrics.json")
            (cell / "shots").mkdir(exist_ok=True)
            own = own_css_report(cell, info.get("own_css"), palette)
            ev = {"own_css": own, "modified_existing": mx.get("modified_existing"),
                  "network_used_while_building": mx.get("web"), "pages": {}}
            for pg in info["pages"]:
                slug = Path(pg["path"]).stem
                url = f"{base}/b/{cell.name}/{pg['path']}"
                if not (cell / "build" / pg["path"]).exists():
                    ev["pages"][slug] = {"missing": True}
                    continue
                r = {}
                ctx = browser.new_context(viewport={"width": 1280, "height": 900})
                page = ctx.new_page()
                external, broken = [], []
                page.on("request", lambda q: external.append(q.url) if not q.url.startswith((base, "data:")) else None)
                page.on("response", lambda s: broken.append(s.url.replace(f"{base}/b/{cell.name}/", "")) if s.status >= 400 else None)
                page.goto(url, wait_until="load")
                page.wait_for_timeout(300)
                r.update(page.evaluate(PAGE_JS))
                classes = set(r.pop("classes"))
                own_classes = set(own.get("classes", []))
                r["classes_from_own_css"] = sorted(classes & own_classes - ds)
                r["classes_docs_only"] = sorted(classes & docs_only - own_classes)
                r["classes_defined_nowhere"] = sorted(classes - ds - own_classes - docs_only)
                r["external_requests"], r["broken_requests"] = sorted(set(external)), sorted(set(broken))
                page.add_script_tag(path=str(AXE))
                r["axe_light"] = page.evaluate(AXE_JS, {})
                page.screenshot(path=str(cell / "shots" / f"{slug}-desktop.jpg"), full_page=True, type="jpeg", quality=70)
                stops = []
                for _ in range(80):
                    page.keyboard.press("Tab")
                    f = page.evaluate(FOCUS_JS)
                    if not f or (stops and f["what"] == stops[0]["what"] and len(stops) > 3):
                        break
                    stops.append(f)
                r["tab_stops"] = [s["what"] for s in stops]
                r["tab_stops_without_focus_indicator"] = [s["what"] for s in stops if not s["indicator"]]
                r["overflow_px"] = {}
                for w in (768, 320):
                    page.set_viewport_size({"width": w, "height": 800})
                    page.wait_for_timeout(200)
                    r["overflow_px"][str(w)] = page.evaluate(OVERFLOW_JS)
                page.screenshot(path=str(cell / "shots" / f"{slug}-phone.jpg"), full_page=True, type="jpeg", quality=70)
                ctx.close()

                ctx = browser.new_context(viewport={"width": 1280, "height": 900}, color_scheme="dark")
                page = ctx.new_page()
                page.goto(url, wait_until="load")
                page.wait_for_timeout(300)
                page.add_script_tag(path=str(AXE))
                r["axe_dark_contrast"] = page.evaluate(AXE_JS, {"runOnly": ["color-contrast"]})
                page.screenshot(path=str(cell / "shots" / f"{slug}-dark.jpg"), full_page=True, type="jpeg", quality=70)
                ctx.close()

                ctx = browser.new_context(viewport={"width": 1280, "height": 900}, java_script_enabled=False)
                page = ctx.new_page()
                page.goto(url, wait_until="load")
                r["text_length_without_js"] = page.evaluate("() => document.body.innerText.length")
                page.screenshot(path=str(cell / "shots" / f"{slug}-nojs.jpg"), full_page=True, type="jpeg", quality=70)
                ctx.close()
                ev["pages"][slug] = r
            (cell / "evaluation.json").write_text(json.dumps(ev, indent=2))
            print(f"  {cell.name}: evaluated {len(ev['pages'])} pages")
        browser.close()
    srv.shutdown()
    print(f"next: python3 {Path(__file__).name} review {run.relative_to(HERE)}")


# ── review (blind, one build at a time, then all together) ───────────────────

PLAIN = """body{font:16px/1.5 system-ui,sans-serif;margin:0;color:#111;background:#fff}
main{max-width:1100px;margin:0 auto;padding:16px 24px 64px}h1{font-size:22px}h2{font-size:18px;margin-top:32px}
button,.btn{font:inherit;padding:6px 14px;border:2px solid #111;background:#fff;color:#111;cursor:pointer;text-decoration:none;display:inline-block}
button[aria-pressed=true]{background:#111;color:#fff}button.go{background:#111;color:#fff}
textarea{font:inherit;width:100%;min-height:120px;box-sizing:border-box;border:2px solid #111;padding:8px}
label{margin-right:20px}fieldset{border:0;padding:0;margin:16px 0}legend,.q{font-weight:700;padding:0;margin-bottom:6px;display:block}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #999;padding:8px;text-align:left;vertical-align:top}
img.thumb{width:220px;height:300px;object-fit:cover;object-position:top;border:1px solid #999;display:block}
.muted{color:#555}.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}"""

REVIEW_JS = """
const R = JSON.parse(document.getElementById('data').textContent);
const state = R.saved || {builds: {}, together: ''};
let i = R.labels.findIndex(l => !(state.builds[l] && state.builds[l].verdict)); if (i < 0) i = R.labels.length;
let pg = 0, narrow = false, started = !!R.saved;
const $ = s => document.querySelector(s);
function save() { return fetch('/save', {method: 'POST', body: JSON.stringify(state)}) }
function src(l) { return '/b/' + l + '/' + R.pages[pg].path }
function intro() {
  $('#app').innerHTML = `<main><h1>${R.labels.length} builds to review</h1>
    <p>The same spec was built ${R.labels.length} separate times. Each build is a different attempt at the same ${R.pages.length === 1 ? 'page' : R.pages.length + ' pages: ' + R.pages.map(p => p.label).join(', ')}.</p>
    ${R.pages.length === 1 ? '' : '<p>Look at every page of a build before you write its notes.</p>'}
    <p>You will see one build at a time. For each build, write what is off and choose a verdict. Then the next build appears. Notes and verdicts are separate for each build.</p>
    <p>After the last build you will see all of them side by side.</p>
    <div class="row"><button class="go" id="start">Start with Build ${R.labels[0]}</button></div></main>`;
  $('#start').onclick = () => { started = true; show() };
}
function show() {
  window.scrollTo(0, 0);
  if (!started) return intro();
  if (i >= R.labels.length) return together();
  const l = R.labels[i], b = state.builds[l] || {notes: '', verdict: ''};
  $('#app').innerHTML = `<div class="bar"><div class="row"><strong>Build ${l}</strong><span class="muted">attempt ${i + 1} of ${R.labels.length} at the same pages</span>
    ${R.pages.map((p, n) => `<button data-pg="${n}" aria-pressed="${n === pg}">${p.label}</button>`).join('')}
    <button id="narrow" aria-pressed="${narrow}">Phone width</button>
    <a class="btn" href="${src(l)}" target="_blank">Open in a new tab</a></div></div>
    <iframe src="${src(l)}" style="width:${narrow ? '390px' : '100%'}" title="Build ${l}"></iframe>
    <main><label class="q" for="notes">What is off in Build ${l}?</label>
    <textarea id="notes">${b.notes.replace(/</g, '&lt;')}</textarea>
    <fieldset><legend>Verdict</legend>${Object.entries(R.verdicts).map(([v, t]) =>
      `<label><input type="radio" name="v" value="${v}" ${b.verdict === v ? 'checked' : ''}> ${t}</label>`).join('')}</fieldset>
    <div class="row">${i > 0 ? '<button id="back">Back</button>' : ''}<button class="go" id="next">${i + 1 < R.labels.length ? 'Save and go to Build ' + R.labels[i + 1] : 'Save and see all builds together'}</button><span id="msg" class="muted"></span></div></main>`;
  document.querySelectorAll('[data-pg]').forEach(b => b.onclick = () => { keep(l); pg = +b.dataset.pg; show() });
  $('#narrow').onclick = () => { keep(l); narrow = !narrow; show() };
  if ($('#back')) $('#back').onclick = () => { keep(l); save(); i--; pg = 0; show() };
  $('#next').onclick = () => { keep(l); if (!state.builds[l].verdict) { $('#msg').textContent = 'Choose a verdict first.'; return }
    save().then(() => { i++; pg = 0; show() }) };
}
function keep(l) { state.builds[l] = {notes: $('#notes').value, verdict: (document.querySelector('input[name=v]:checked') || {}).value || ''} }
function together() {
  $('#app').innerHTML = `<main><h1>All ${R.labels.length} builds together</h1>
    <p>Your answers are saved. Is there anything to add now that you can see them side by side?</p>
    <table><tr>${R.labels.map(l => `<th>Build ${l}<br><span class="muted">${R.verdicts[state.builds[l].verdict]}</span></th>`).join('')}</tr>
    ${R.pages.map(p => `<tr>${R.labels.map(l => { const s = p.path.split('/').pop().replace('.html', '');
      return `<td><a href="/b/${l}/${p.path}" target="_blank"><img class="thumb" alt="Build ${l}, ${p.label}" src="/shots/${l}/${s}-desktop.jpg"></a>${p.label}</td>` }).join('')}</tr>`).join('')}</table>
    <label class="q" for="tog" style="margin-top:24px">Notes after seeing them together</label>
    <textarea id="tog">${(state.together || '').replace(/</g, '&lt;')}</textarea>
    <div class="row"><button id="back">Back</button><button class="go" id="done">Save and finish</button><span id="msg" class="muted"></span></div></main>`;
  $('#back').onclick = () => { state.together = $('#tog').value; i = R.labels.length - 1; show() };
  $('#done').onclick = () => { state.together = $('#tog').value; state.finished = true;
    save().then(() => $('#msg').textContent = 'Saved. Tell Claude you are finished.') };
}
show();
"""


def review_page(run: Path) -> str:
    info = load(run / "run.json")
    data = {"labels": [c.name for c in cells_of(run)], "pages": info["pages"], "verdicts": VERDICTS,
            "saved": load(run / "review.json")}
    blob = json.dumps(data).replace("</", "<\\/")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Review: {esc(info.get('title', run.name))}</title>
<style>{PLAIN}
.bar{{border-bottom:2px solid #111;padding:4px 16px;background:#fff}}
iframe{{display:block;height:78vh;border:0;border-bottom:2px solid #111;margin:0 auto;background:#fff}}</style></head>
<body><div id="app"></div><script type="application/json" id="data">{blob}</script>
<script>{REVIEW_JS}</script></body></html>"""


def review(args):
    run = Path(args.run).resolve()
    serve(run, args.port)
    print(f"review page: http://127.0.0.1:{args.port}/   (Ctrl+C to stop)", flush=True)
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        pass


# ── summary ──────────────────────────────────────────────────────────────────

def summary(args):
    run = Path(args.run).resolve()
    info, key = load(run / "run.json"), load(run / "key.json")
    rev = load(run / "review.json", {"builds": {}})
    tech = load(run / "technical.json", {"builds": {}})
    cells = cells_of(run)
    first = Path(info["pages"][0]["path"]).stem

    def row(title, fn):
        return f"<tr><th>{title}</th>" + "".join(f"<td>{fn(c)}</td>" for c in cells) + "</tr>"

    def shots(c):
        out = []
        for pg in info["pages"]:
            s = Path(pg["path"]).stem
            if (c / "shots" / f"{s}-desktop.jpg").exists():
                out.append(f'<a href="{c.name}/shots/{s}-desktop.jpg">{esc(pg["label"])}</a> '
                           f'(<a href="{c.name}/shots/{s}-phone.jpg">phone</a>, <a href="{c.name}/shots/{s}-dark.jpg">dark</a>)')
        thumb = f'<img class="thumb" alt="Build {c.name}" src="{c.name}/shots/{first}-desktop.jpg">' \
            if (c / "shots" / f"{first}-desktop.jpg").exists() else "no page built"
        return thumb + "<br>".join(out)

    def cost(c):
        m = load(c / "metrics.json")
        return (f"${(m.get('cost_usd') or 0):.2f} · {m.get('wall_seconds', 0) // 60} min · "
                f"{m.get('unique_files_read', 0)} files read")

    def para(text):
        return "".join(f"<p>{esc(p)}</p>" for p in str(text or "").split("\n\n") if p.strip())

    def fold(text):
        return f"<details><summary>Read</summary>{para(text)}</details>" if str(text or "").strip() else ""

    def items(xs):
        return "<ul>" + "".join(f"<li>{esc(x)}</li>" for x in xs) + "</ul>" if xs else "<p class='muted'>Not written yet.</p>"

    table = "<table>" + "".join([
        "<tr><th></th>" + "".join(f"<th>Build {c.name}</th>" for c in cells) + "</tr>",
        row("Model", lambda c: esc(key[c.name]["model"])),
        row("Pages", shots),
        row("Shamsi: verdict", lambda c: esc(VERDICTS.get(rev["builds"].get(c.name, {}).get("verdict"), "not reviewed"))),
        row("Shamsi: what is off", lambda c: fold(rev["builds"].get(c.name, {}).get("notes"))),
        row("Claude: technical verdict", lambda c: esc(tech["builds"].get(c.name, {}).get("verdict", "not evaluated"))),
        row("Claude: technical notes", lambda c: fold(tech["builds"].get(c.name, {}).get("notes"))),
        row("Cost", cost)]) + "</table>"
    dirty = " (with uncommitted changes to docs/)" if info.get("uncommitted_docs_changes") else ""
    prev_html = ""
    prev = HERE / "runs" / info["previous"] if info.get("previous") else None
    if prev and prev.exists():
        pinfo, prev_rev = load(prev / "run.json"), load(prev / "review.json", {"builds": {}})
        pfirst = Path(pinfo["pages"][0]["path"]).stem
        cells_p = cells_of(prev)
        prev_html = (f'<h2>Last round: {esc(pinfo.get("title", prev.name))}</h2><table><tr>'
                     + "".join(f'<td><a href="../{prev.name}/summary.html"><img class="thumb" alt="Last round, build {c.name}" '
                               f'src="../{prev.name}/{c.name}/shots/{pfirst}-desktop.jpg"></a>Build {c.name}: '
                               f'{esc(VERDICTS.get(prev_rev["builds"].get(c.name, {}).get("verdict"), "not reviewed"))}</td>'
                               for c in cells_p) + "</tr></table>")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(info.get('title', run.name))}: test summary</title><style>{PLAIN}</style></head><body><main>
<h1>{esc(info.get('title', run.name))}</h1>
<p class="muted">{esc(info['date'])} · design system at commit {esc(info['commit'])}{dirty} · <a href="spec.md">the spec</a></p>
<h2>Result</h2>{para(tech.get("result")) or "<p class='muted'>Not written yet.</p>"}
<h2>Builds</h2>{table}
{prev_html}
{('<h2>Shamsi: notes after seeing them together</h2>' + para(rev.get('together'))) if rev.get('together') else ''}
<h2>What the builds had in common</h2>{items(tech.get("patterns"))}
<h2>What we changed in the design system</h2>{items(tech.get("changes"))}
</main></body></html>"""
    (run / "summary.html").write_text(page)
    rows = []
    for rd in sorted((p for p in (HERE / "runs").iterdir() if p.is_dir()), reverse=True):
        if (rd / "summary.html").exists():
            rows.append(f'<li><a href="{rd.name}/summary.html">{esc(rd.name)}</a></li>')
        elif (rd / "review.html").exists():
            rows.append(f'<li><a href="{rd.name}/review.html">{esc(rd.name)}</a> (July battery, retired)</li>')
    (HERE / "runs/index.html").write_text(
        f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Test runs</title>'
        f'<style>{PLAIN}</style></head><body><main><h1>Test runs</h1><ul>{"".join(rows)}</ul></main></body></html>')
    print(f"summary: {run / 'summary.html'}")


# ── report: the one-page version for the team ────────────────────────────────

GRADES = {"pass": "Pass", "changes": "Pass with changes", "fail": "Fail"}
VISUAL = {"accept": "pass", "changes": "changes", "reject": "fail"}
AGENTS = {"claude-sonnet-5-5": "Claude Sonnet 5.5", "claude-opus-5-5": "Claude Opus 5.5"}


def total_tokens(m: dict) -> int:
    u = m.get("usage") or {}
    return sum(u.get(k, 0) or 0 for k in
               ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))


def millions(n: int) -> str:
    return f"{n / 1e6:.1f} million" if n >= 1e6 else f"{n:,}"


def report(args):
    run = Path(args.run).resolve()
    info, key = load(run / "run.json"), load(run / "key.json")
    rev = load(run / "review.json", {"builds": {}})
    tech = load(run / "technical.json", {"builds": {}})
    first = Path(info["pages"][0]["path"]).stem
    cards = []
    for c in cells_of(run):
        shot = f"{c.name}/shots/{first}-desktop.jpg"
        img = (f'<a href="{shot}"><img src="{shot}" alt="Build {c.name}, full size"></a>'
               if (run / shot).exists() else "<p>No page built.</p>")
        vis = GRADES.get(VISUAL.get(rev["builds"].get(c.name, {}).get("verdict")), "Not reviewed")
        prog = GRADES.get(tech["builds"].get(c.name, {}).get("programmatic"), "Not graded")
        tok = millions(total_tokens(load(c / "metrics.json", {})))
        cards.append(f"""<figure>{img}<figcaption><strong>Build {c.name}</strong><dl>
<dt>Visual fidelity</dt><dd>{vis}</dd><dt>Programmatic fidelity</dt><dd>{prog}</dd>
<dt>Agent</dt><dd>{esc(AGENTS.get(key[c.name]["model"], key[c.name]["model"]))}</dd><dt>Tokens</dt><dd>{tok}</dd></dl></figcaption></figure>""")
    found = tech.get("findings") or []
    found_html = ("<h2>What the review found</h2><ul>" + "".join(f"<li>{esc(x)}</li>" for x in found[:3]) + "</ul>") if found else ""
    nxt = f"<h2>Next</h2><p>{esc(tech['next'])}</p>" if tech.get("next") else ""
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(info.get("subject", info.get("title", run.name)))}: test report</title><style>
body{{font:16px/1.5 system-ui,sans-serif;margin:0;color:#1c1a17;background:#fff}}
main{{max-width:960px;margin:0 auto;padding:16px 16px 48px}}h1{{font-size:24px;margin:16px 0 4px}}h2{{font-size:18px;margin:32px 0 8px}}
.meta{{margin:0;padding:0;list-style:none;color:#59534c}}a{{color:#1565c0}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:24px}}
@media (max-width:600px){{.grid{{grid-template-columns:1fr}}}}
figure{{margin:0}}figure img{{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;object-position:top;border:1px solid #dad8d6;border-radius:6px}}
figcaption{{margin-top:8px}}dl{{display:grid;grid-template-columns:auto 1fr;gap:2px 12px;margin:4px 0 0;font-size:14px}}dt{{color:#59534c}}dd{{margin:0;font-weight:600}}
</style></head><body><main>
<h1>{esc(info.get("subject", info.get("title", run.name)))}</h1>
<ul class="meta"><li>{esc(info["date"])}</li><li><a href="spec.md">The spec</a></li><li><a href="summary.html">The detailed report</a></li></ul>
<div class="grid">{"".join(cards)}</div>
{found_html}{nxt}
</main></body></html>"""
    (run / "report.html").write_text(page)
    print(f"report: {run / 'report.html'}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("test")
    b.add_argument("--models", default=",".join(MODELS))
    b.add_argument("--reps", type=int, default=2)
    b.add_argument("--budget", type=float, default=10, help="stop a build once its estimated cost passes this many dollars")
    b.add_argument("--parallel", type=int, default=1)
    for name in ("evaluate", "review", "summary", "report"):
        s = sub.add_parser(name)
        s.add_argument("run")
        if name == "review":
            s.add_argument("--port", type=int, default=8765)
    a = ap.parse_args()
    {"build": build, "evaluate": evaluate, "review": review, "summary": summary, "report": report}[a.cmd](a)
