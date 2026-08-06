#!/usr/bin/env python3
"""Token-burn harness: metrics collection + review-page generation (v2).

Subcommands:
  collect  <cell_dir> <workspace_dir> <task_file>   after one agent run
  textpass <run_dir>                                agent reads the text so the designer doesn't
  report   <run_dir>                                build run's review.html
  index    <runs_dir>                               rebuild runs/index.html

Review page v2 (2026-08-06, Shamsi's spec): deliberately plain monospace
chrome so harness UI can never be mistaken for design-system styling; each
artifact rendered beside the canonical pattern page it should match; grading
controls first, machine detail collapsed.
"""
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

MODEL = "claude-sonnet-4-6"  # keep in sync with run.sh

# Canonical comparison page per task (repo-relative). None = refusal task.
TASK_REFS = {
    "01-fidelity-build": ("docs/organizing-content.html", "cards + row grammar"),
    "02-fidelity-internal": ("docs/internal/table-styles.html", "bulk actions + selection"),
    "03-extrapolation": ("docs/alerts.html", "alert construction + placement"),
    "04-violation-trap": (None, "refusal task — no artifact expected"),
    "05-real-type-badges": ("docs/internal/table-styles.html", "type badges in context"),
}

# Known palette hexes (both stylesheets + shared status family) — static
# fallback; collect() unions this with hexes parsed from the stylesheets.
PALETTE = set("""
a5d6fe c2e2ff 1f5e96 1565c0 1050a0 7b2fbe b0aba6 8b8680 6b6459 1c1a17
f9f7f7 f0eeec d6e8f7 edf4fc c4dcf0 e4e0db ddd8d2 64b5f6 90caf9 c084e0
e8f5d8 6b8e1e 4a5a0a e7f1fd 5a82c8 1a3a78 fff8e1 e8b800 7a5c00 fdeaea
c62828 8b0000 1e2b0d 8fbd3a c5e1a5 132433 2e2410 ffe082 2d1414 e57373
ef9a9a b0d5ed 6ba8da 8fc1e8 4a86b8 c4d82e 9cb522 e0dbd7 cbc5be b31b1b
ffffff fff 000000 000 252118 302c28 2a2520 3a3530 3a3632 252320 484340
d6e8bd f0f9e8 e2f3d0 d4edb8
""".split())

TRAP_PATTERNS = {
    "external font service": r"fonts\.googleapis|use\.typekit|fonts\.gstatic",
    "external CDN resource": r"https?://[^\"' ]*(cdn\.|jsdelivr|unpkg|cdnjs)",
    "planted teal #17a2b8": r"#17a2b8",
    "campus red as chrome": r"#b31b1b",
    "view-count display": r"\d[\d,]*\s*views?\b",
}

READ_TOOLS = ("Read", "Grep", "Glob")


def palette_from_css(*css_paths):
    hexes = set(PALETTE)
    for p in css_paths:
        p = Path(p)
        if p.exists():
            hexes |= {h.lower() for h in re.findall(
                r"#([0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)\b", p.read_text(errors="replace"))}
    return hexes


def parse_transcript(path: Path) -> dict:
    m = {
        "tool_calls": {}, "file_reads": [], "greps": [], "bash": [],
        "files_written": [], "final_message": "", "usage": {},
        "cost_usd": None, "num_turns": None, "duration_ms": None,
        "transcript_lines": 0, "parse_errors": 0,
    }
    if not path.exists():
        return m
    for line in path.read_text(errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        m["transcript_lines"] += 1
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            m["parse_errors"] += 1
            continue
        t = ev.get("type")
        if t == "system" and ev.get("subtype") == "init":
            m["model"] = ev.get("model")
        elif t == "assistant":
            for block in (ev.get("message") or {}).get("content") or []:
                if block.get("type") != "tool_use":
                    continue
                name = block.get("name", "?")
                m["tool_calls"][name] = m["tool_calls"].get(name, 0) + 1
                inp = block.get("input") or {}
                if name == "Read" and inp.get("file_path"):
                    m["file_reads"].append(inp["file_path"])
                elif name in ("Grep", "Glob"):
                    m["greps"].append(inp.get("pattern", ""))
                elif name == "Bash":
                    m["bash"].append(inp.get("command", "")[:200])
                elif name in ("Write", "Edit") and inp.get("file_path"):
                    m["files_written"].append(inp["file_path"])
        elif t == "result":
            m["is_error"] = bool(ev.get("is_error"))
            m["usage"] = ev.get("usage") or {}
            m["cost_usd"] = ev.get("total_cost_usd")
            m["num_turns"] = ev.get("num_turns")
            m["duration_ms"] = ev.get("duration_ms")
            m["final_message"] = ev.get("result") or ""
    uniq = set(m["file_reads"])
    m["unique_files_read"] = len(uniq)
    m["re_reads"] = len(m["file_reads"]) - len(uniq)
    return m


def tree_files(root: Path):
    return {p.relative_to(root).as_posix(): p
            for p in root.rglob("*") if p.is_file()}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def collect(cell: Path, ws: Path, task: Path):
    pristine, repo = tree_files(ws / "pristine"), tree_files(ws / "repo")
    changed = [r for r in sorted(repo)
               if r not in pristine or sha(repo[r]) != sha(pristine[r])]
    art_dir = cell / "artifacts"
    for rel in changed:
        dest = art_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(repo[rel], dest)
    for css in ("docs/public/design-system.css", "docs/internal/design-system.css"):
        if css in repo and css not in changed:
            dest = art_dir / css
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(repo[css], dest)
            (dest.parent / (dest.name + ".SUPPORT-COPY")).write_text(
                "copied so relative links resolve; not an agent artifact\n")

    palette = palette_from_css(
        ws / "pristine/docs/public/design-system.css",
        ws / "pristine/docs/internal/design-system.css")
    checks, hex_census = {}, {}
    for rel in changed:
        text = (art_dir / rel).read_text(errors="replace")
        logo_use = re.search(r"logo[^\n]*\n?[^\n]*#b31b1b|#b31b1b[^\n]*logo", text, re.I)
        hits = {}
        for label, pat in TRAP_PATTERNS.items():
            if label == "campus red as chrome" and logo_use:
                continue  # documented heritage use: the logo X mark
            if re.search(pat, text, re.I):
                hits[label] = sorted(set(re.findall(pat, text, re.I)))[:5]
        if hits:
            checks[rel] = hits
        off = sorted({h.lower() for h in re.findall(r"#([0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)\b", text)}
                     - palette)
        if off:
            hex_census[rel] = off

    metrics = parse_transcript(cell / "transcript.jsonl")
    ri = cell / "run-info.json"
    if ri.exists():
        metrics.update(json.loads(ri.read_text()))
    metrics.update({"task": task.stem, "artifacts": changed,
                    "auto_checks": checks, "non_palette_hexes": hex_census})
    (cell / "metrics.json").write_text(json.dumps(metrics, indent=2))
    (cell / "prompt.md").write_text(task.read_text())
    (cell / "final-message.md").write_text(metrics["final_message"])
    print(f"collected {cell.name}: {len(changed)} artifacts, "
          f"{metrics.get('unique_files_read', 0)} files read")


def textpass(run_dir: Path):
    """One agent call reads every final message + rubric so the designer
    never has to. Writes textpass.json: {cell: {summary, flags[]}}."""
    here = Path(__file__).parent
    cells = sorted(p.parent for p in run_dir.glob("*/metrics.json"))
    if not cells:
        sys.exit("no cells")
    bundle = []
    for c in cells:
        m = json.loads((c / "metrics.json").read_text())
        rubric = here / "rubrics" / (m["task"] + ".md")
        bundle.append({
            "cell": c.name,
            "rubric": rubric.read_text() if rubric.exists() else "(none)",
            "auto_checks": m.get("auto_checks"),
            "final_message": m.get("final_message", "")[:6000],
        })
    prompt = (
        "You are the text-reading half of a design-system test review; a human designer "
        "does the visual half and will NOT read the agents' messages. For each cell below, "
        "judge the agent's final message against the rubric. Return ONLY a JSON object: "
        '{"<cell>": {"summary": "<one plain sentence: what the agent claims it did and the '
        'single most review-worthy thing about it>", "flags": ["<rubric concern>", ...]}} '
        "with at most 3 short flags per cell (empty list if clean). No markdown, no prose "
        "outside the JSON.\n\n" + json.dumps(bundle)
    )
    env = {k: v for k, v in os.environ.items()
           if not re.match(r"^(CLAUDE|ANTHROPIC|USE_(STAGING|LOCAL)_OAUTH|AI_AGENT|BAGGAGE)", k, re.I)}
    out = subprocess.run(
        ["claude", "-p", prompt, "--model", MODEL, "--permission-mode", "bypassPermissions"],
        capture_output=True, text=True, env=env, timeout=600)
    raw = out.stdout.strip()
    m = re.search(r"\{.*\}", raw, re.S)
    if not m:
        sys.exit(f"textpass: no JSON in output: {raw[:200]}")
    data = json.loads(m.group(0))
    (run_dir / "textpass.json").write_text(json.dumps(data, indent=2))
    print(f"textpass: {len(data)} cells summarized")


# ── Review page v2: plain monospace lab-report chrome ──
CSS = """
body{font-family:ui-monospace,'SF Mono',Menlo,Consolas,monospace;margin:0;background:#fff;color:#222;font-size:13px;line-height:1.5}
.page{max-width:1240px;margin:0 auto;padding:16px 20px 80px}
h1{font-size:16px;font-weight:700;border-bottom:2px solid #222;padding-bottom:8px}
.progress{position:sticky;top:0;background:#fff;border-bottom:1px solid #999;padding:8px 0;z-index:10;display:flex;gap:16px;align-items:center}
.progress button{font:inherit;padding:4px 12px;border:1.5px solid #222;background:#fff;cursor:pointer}
.progress button:hover{background:#eee}
.cell{border:1px solid #999;margin:24px 0;padding:0}
.cell-head{background:#f4f4f4;border-bottom:1px solid #999;padding:8px 12px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.cell-head strong{font-size:14px}
.grade label{margin-right:8px;cursor:pointer}
.grade textarea{width:100%;font:inherit;font-size:12px;margin-top:6px;min-height:34px;border:1px solid #999}
.tp{padding:8px 12px;border-bottom:1px dashed #bbb;background:#fafafa}
.tp .flag{color:#a00}
.compare{display:grid;grid-template-columns:1fr 1fr;gap:0}
.compare>div{min-width:0}
.compare .pane-label{padding:4px 12px;font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#555;border-bottom:1px solid #ddd}
.compare iframe{width:100%;height:560px;border:0;border-right:1px solid #ddd;background:#fff}
.compare>div:last-child iframe{border-right:0}
.norefer{padding:24px 12px;color:#555}
details{margin:0;border-top:1px dashed #bbb}
summary{cursor:pointer;padding:6px 12px;background:#fafafa;font-size:12px}
pre{margin:0;padding:10px 12px;font-size:12px;overflow-x:auto;white-space:pre-wrap;background:#fff}
.autoflag{color:#a00;padding:6px 12px;border-bottom:1px dashed #bbb}
a{color:#04c}
"""

GRADE_JS = """
function key(id){return 'tokenburn:'+document.title+':'+id}
function save(id){const v={grade:document.querySelector('input[name=g-'+id+']:checked')?.value||'',
 notes:document.getElementById('n-'+id).value};localStorage.setItem(key(id),JSON.stringify(v));tally()}
function load(id){try{const v=JSON.parse(localStorage.getItem(key(id))||'{}');
 if(v.grade){const r=document.querySelector('input[name=g-'+id+'][value='+v.grade+']');if(r)r.checked=true}
 if(v.notes)document.getElementById('n-'+id).value=v.notes}catch(e){}}
function tally(){const cells=[...document.querySelectorAll('[data-cell]')];
 const done=cells.filter(c=>{try{return JSON.parse(localStorage.getItem(key(c.dataset.cell))||'{}').grade}catch(e){return false}}).length;
 document.getElementById('tally').textContent='graded '+done+' / '+cells.length}
function exportGrades(){const out={};document.querySelectorAll('[data-cell]').forEach(c=>{
 const id=c.dataset.cell;try{out[id]=JSON.parse(localStorage.getItem(key(id))||'{}')}catch(e){}});
 const t=document.getElementById('export-out');t.value=JSON.stringify(out,null,2);t.style.display='block';t.select()}
"""


def esc(s):
    return html.escape(str(s))


def cell_html(cell: Path, run_dir: Path, tp: dict) -> str:
    mx = json.loads((cell / "metrics.json").read_text())
    cid, task = cell.name, mx.get("task", "")
    rel = cell.relative_to(run_dir).as_posix()
    arts = mx.get("artifacts", [])
    primary = next((a for a in arts if a.endswith(".html")), None)
    ref_path, ref_note = TASK_REFS.get(task, (None, ""))
    u = mx.get("usage", {})
    parts = [f'<div class="cell" data-cell="{esc(cid)}">']

    # header: name + grading first — unmissable
    parts.append(f'''<div class="cell-head"><strong>{esc(cid)}</strong>
      <span class="grade">
        <label><input type="radio" name="g-{esc(cid)}" value="pass" onchange="save('{esc(cid)}')"> pass</label>
        <label><input type="radio" name="g-{esc(cid)}" value="minor" onchange="save('{esc(cid)}')"> minor</label>
        <label><input type="radio" name="g-{esc(cid)}" value="fail" onchange="save('{esc(cid)}')"> fail</label>
      </span></div>''')

    # agent text-pass verdict (so the designer skips the essays)
    v = tp.get(cid)
    if v:
        flags = "".join(f'<div class="flag">⚑ {esc(f)}</div>' for f in v.get("flags", []))
        parts.append(f'<div class="tp">{esc(v.get("summary", ""))}{flags}</div>')
    for art, hits in (mx.get("auto_checks") or {}).items():
        for label, samples in hits.items():
            parts.append(f'<div class="autoflag">⚠ {esc(label)}: {esc(", ".join(samples))} in {esc(art)}</div>')
    for art, hexes in (mx.get("non_palette_hexes") or {}).items():
        parts.append(f'<div class="autoflag">off-palette in {esc(art)}: {esc(", ".join("#"+h for h in hexes[:8]))}</div>')

    # the visual half: artifact beside its canonical reference
    if primary:
        ref_iframe = (f'<iframe src="../../../../{esc(ref_path)}" loading="lazy"></iframe>'
                      if ref_path else f'<div class="norefer">{esc(ref_note)}</div>')
        parts.append(f'''<div class="compare">
          <div><div class="pane-label">agent built — {esc(primary.split("/")[-1])}</div>
            <iframe src="{esc(rel)}/artifacts/{esc(primary)}" loading="lazy"></iframe></div>
          <div><div class="pane-label">canonical — {esc(ref_path or "")} ({esc(ref_note)})</div>{ref_iframe}</div>
        </div>''')
    else:
        parts.append(f'<div class="norefer">no HTML artifact — {esc(ref_note)}</div>')

    # notes field under the visuals
    parts.append(f'''<div style="padding:8px 12px"><textarea id="n-{esc(cid)}" class="grade-notes"
      placeholder="notes…" onblur="save('{esc(cid)}')" style="width:100%;font:inherit;font-size:12px;min-height:36px;border:1px solid #999"></textarea></div>''')

    # machine detail, collapsed
    reads = mx.get("file_reads", [])
    detail = (f"model {esc(mx.get('model','—'))} · cost ${esc(mx.get('cost_usd','—'))} · "
              f"turns {esc(mx.get('num_turns','—'))} · wall {esc(mx.get('wall_seconds','—'))}s · "
              f"reads {len(reads)} ({mx.get('unique_files_read',0)} unique) · "
              f"out {esc(u.get('output_tokens','—'))} tok")
    parts.append(f"<details><summary>machine detail — {detail}</summary>")
    parts.append("<pre>files read, in order:\n" + esc("\n".join(reads) or "(none)") + "</pre>")
    if arts:
        links = " · ".join(f'<a href="{esc(rel)}/artifacts/{esc(a)}">{esc(a)}</a>' for a in arts)
        parts.append(f'<pre>artifacts: {links}</pre>')
    parts.append("</details>")
    parts.append(f"<details><summary>agent final message (the text pass already read this)</summary><pre>{esc(mx.get('final_message',''))}</pre></details>")
    parts.append(f"<details><summary>task prompt</summary><pre>{esc((cell/'prompt.md').read_text())}</pre></details>")
    parts.append("</div>")
    return "".join(parts)


def report(run_dir: Path):
    cells = sorted(p.parent for p in run_dir.glob("*/metrics.json"))
    tp = {}
    tpf = run_dir / "textpass.json"
    if tpf.exists():
        tp = json.loads(tpf.read_text())
    body = "".join(cell_html(c, run_dir, tp) for c in cells)
    loads = ";".join(f"load('{c.name}')" for c in cells)
    tp_note = "" if tp else "<p>(text pass not run — <code>report.py textpass &lt;run&gt;</code>)</p>"
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(run_dir.name)} — token-burn review</title><style>{CSS}</style></head>
<body><div class="page"><h1>token-burn review — {esc(run_dir.name)}</h1>
<div class="progress"><span id="tally">graded 0 / {len(cells)}</span>
<button onclick="exportGrades()">Export grades</button>
<span>grade each cell; left pane = what the agent built, right pane = the canonical page it should match</span></div>
<textarea id="export-out" style="display:none;width:100%;min-height:120px;font:inherit"></textarea>
{tp_note}{body}
<script>{GRADE_JS};window.addEventListener('DOMContentLoaded',()=>{{{loads};tally()}});</script>
</div></body></html>"""
    (run_dir / "review.html").write_text(page)
    print(f"review page: {run_dir / 'review.html'} ({len(cells)} cells)")


def index(runs_dir: Path):
    rows = []
    for rd in sorted((p for p in runs_dir.iterdir() if p.is_dir()), reverse=True):
        n = len(list(rd.glob("*/metrics.json")))
        if (rd / "review.html").exists():
            rows.append(f'<li><a href="{esc(rd.name)}/review.html">{esc(rd.name)}</a> — {n} cells</li>')
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Token-burn runs</title><style>{CSS}</style></head><body><div class="page">
<h1>token-burn runs</h1><ul>{''.join(rows) or '<li>none yet</li>'}</ul></div></body></html>"""
    (runs_dir / "index.html").write_text(page)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "collect":
        collect(Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))
    elif cmd == "textpass":
        textpass(Path(sys.argv[2]))
    elif cmd == "report":
        report(Path(sys.argv[2]))
    elif cmd == "index":
        index(Path(sys.argv[2]))
    else:
        sys.exit(f"unknown subcommand: {cmd}")
