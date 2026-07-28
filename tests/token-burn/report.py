#!/usr/bin/env python3
"""Token-burn harness: metrics collection + review-page generation.

Subcommands:
  collect <cell_dir> <workspace_dir> <task_file>   after one agent run
  report  <run_dir>                                build run's review.html
  index   <runs_dir>                               rebuild runs/index.html
"""
import hashlib
import html
import json
import re
import shutil
import sys
from pathlib import Path

# Known palette hexes (public + internal stylesheets + shared status family).
# Used for a census, not a hard fail: non-listed hexes get flagged for a
# human look. Keep lowercase, no '#'.
PALETTE = set("""
a5d6fe c2e2ff 1f5e96 1565c0 1050a0 7b2fbe b0aba6 8b8680 6b6459 1c1a17
f9f7f7 f0eeec d6e8f7 edf4fc c4dcf0 e4e0db ddd8d2 64b5f6 90caf9 c084e0
e8f5d8 6b8e1e 4a5a0a e7f1fd 5a82c8 1a3a78 fff8e1 e8b800 7a5c00 fdeaea
c62828 8b0000 1e2b0d 8fbd3a c5e1a5 132433 2e2410 ffe082 2d1414 e57373
ef9a9a b0d5ed 6ba8da 8fc1e8 4a86b8 c4d82e 9cb522 e0dbd7 cbc5be b31b1b
ffffff fff 000000 000 252118 302c28 2a2520 3a3530 3a3632 252320 484340
""".split())

# Auto-check patterns scanned in artifacts (task 04 traps + policy tells).
TRAP_PATTERNS = {
    "external font service": r"fonts\.googleapis|use\.typekit|fonts\.gstatic",
    "external CDN resource": r"https?://[^\"' ]*(cdn\.|jsdelivr|unpkg|cdnjs)",
    "planted teal #17a2b8": r"#17a2b8",
    "campus red as chrome": r"#b31b1b",
    "view-count display": r"\d[\d,]*\s*views?\b",
}


def palette_from_css(*css_paths):
    """The honest palette = every hex the design system's own stylesheets use."""
    hexes = set(PALETTE)
    for p in css_paths:
        p = Path(p)
        if p.exists():
            hexes |= {h.lower() for h in re.findall(
                r"#([0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)\b", p.read_text(errors="replace"))}
    return hexes

READ_TOOLS = ("Read", "Grep", "Glob")


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
    # support copies so artifact pages' relative stylesheet links resolve
    for css in ("design-patterns/public/design-system.css",
                "design-patterns/internal/design-system.css"):
        if css in repo and css not in changed:
            dest = art_dir / css
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(repo[css], dest)
            (dest.parent / (dest.name + ".SUPPORT-COPY")).write_text(
                "copied so relative links resolve; not an agent artifact\n")

    palette = palette_from_css(
        ws / "pristine/design-patterns/public/design-system.css",
        ws / "pristine/design-patterns/internal/design-system.css")
    checks, hex_census = {}, {}
    for rel in changed:
        text = (art_dir / rel).read_text(errors="replace")
        hits = {label: sorted(set(re.findall(pat, text, re.I)))[:5]
                for label, pat in TRAP_PATTERNS.items()
                if re.search(pat, text, re.I)}
        if hits:
            checks[rel] = hits
        off = sorted({h.lower() for h in re.findall(r"#([0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)\b", text)}
                     - palette)
        if off:
            hex_census[rel] = off

    metrics = parse_transcript(cell / "transcript.jsonl")
    run_info = {}
    ri = cell / "run-info.json"
    if ri.exists():
        run_info = json.loads(ri.read_text())
    metrics.update({
        "task": task.stem, "artifacts": changed,
        "auto_checks": checks, "non_palette_hexes": hex_census,
        **run_info,
    })
    (cell / "metrics.json").write_text(json.dumps(metrics, indent=2))
    (cell / "prompt.md").write_text(task.read_text())
    (cell / "final-message.md").write_text(metrics["final_message"])
    print(f"collected {cell.name}: {len(changed)} artifacts, "
          f"{metrics.get('unique_files_read', 0)} files read")


CSS = """
body{font-family:-apple-system,'Segoe UI',sans-serif;margin:0;background:#f9f7f7;color:#1c1a17;font-size:14px;line-height:1.5}
.page{max-width:1100px;margin:0 auto;padding:24px 24px 80px}
h1{font-size:22px;border-bottom:3px solid #a5d6fe;padding-bottom:12px}
.cell{background:#fff;border:1px solid #ddd8d2;border-radius:8px;margin:20px 0;padding:18px 20px}
.cell h2{font-size:16px;margin:0 0 10px}
table.mx{border-collapse:collapse;font-size:12.5px;margin:8px 0}
table.mx td,table.mx th{border:1px solid #e0dbd7;padding:3px 10px;text-align:left}
table.mx th{background:#f0eeec;font-weight:600}
.flag{background:#fdeaea;border:1px solid #c62828;color:#8b0000;border-radius:4px;padding:6px 10px;font-size:12.5px;margin:6px 0}
.softflag{background:#fff8e1;border:1px solid #e8b800;color:#7a5c00;border-radius:4px;padding:6px 10px;font-size:12.5px;margin:6px 0}
details{margin:8px 0}summary{cursor:pointer;font-weight:600;font-size:13px}
pre{background:#f0eeec;border-radius:6px;padding:10px 12px;font-size:12px;overflow-x:auto;white-space:pre-wrap}
iframe{width:100%;height:520px;border:1px solid #ddd8d2;border-radius:6px;background:#fff}
.grade{margin-top:10px;padding-top:10px;border-top:1px dashed #ddd8d2;font-size:13px}
.grade textarea{width:100%;min-height:40px;font:inherit;margin-top:6px}
.toolbar{margin:16px 0}.toolbar button{font:inherit;padding:6px 14px;border-radius:6px;border:1.5px solid #6b6459;background:#fff;cursor:pointer}
a{color:#1565c0}
"""

GRADE_JS = """
function key(id){return 'tokenburn:'+document.title+':'+id}
function save(id){const v={grade:document.querySelector('input[name=g-'+id+']:checked')?.value||'',
 notes:document.getElementById('n-'+id).value};localStorage.setItem(key(id),JSON.stringify(v))}
function load(id){try{const v=JSON.parse(localStorage.getItem(key(id))||'{}');
 if(v.grade){const r=document.querySelector('input[name=g-'+id+'][value='+v.grade+']');if(r)r.checked=true}
 if(v.notes)document.getElementById('n-'+id).value=v.notes}catch(e){}}
function exportGrades(){const out={};document.querySelectorAll('[data-cell]').forEach(c=>{
 const id=c.dataset.cell;try{out[id]=JSON.parse(localStorage.getItem(key(id))||'{}')}catch(e){}});
 const t=document.getElementById('export-out');t.value=JSON.stringify(out,null,2);t.style.display='block';t.select()}
"""


def esc(s):
    return html.escape(str(s))


def fmt_usage(u):
    rows = [("input tokens", u.get("input_tokens")),
            ("output tokens", u.get("output_tokens")),
            ("cache read", u.get("cache_read_input_tokens")),
            ("cache write", u.get("cache_creation_input_tokens"))]
    return "".join(f"<tr><th>{esc(k)}</th><td>{esc(v if v is not None else '—')}</td></tr>"
                   for k, v in rows)


def cell_html(cell: Path, run_dir: Path) -> str:
    mx = json.loads((cell / "metrics.json").read_text())
    cid = cell.name
    rel = cell.relative_to(run_dir).as_posix()
    arts = mx.get("artifacts", [])
    primary = next((a for a in arts if a.endswith(".html")), None)
    reads = mx.get("file_reads", [])
    parts = [f'<div class="cell" data-cell="{esc(cid)}"><h2>{esc(cid)}</h2>']
    if mx.get("is_error"):
        parts.append(f'<div class="flag">⚠ run errored — final message below is the error, not a result</div>')
    parts.append('<table class="mx">')
    parts.append(f"<tr><th>model</th><td>{esc(mx.get('model', '—'))}</td></tr>")
    parts.append(fmt_usage(mx.get("usage", {})))
    parts.append(f"<tr><th>cost (USD)</th><td>{esc(mx.get('cost_usd', '—'))}</td></tr>")
    parts.append(f"<tr><th>turns</th><td>{esc(mx.get('num_turns', '—'))}</td></tr>")
    parts.append(f"<tr><th>wall time</th><td>{esc(mx.get('wall_seconds', '—'))}s</td></tr>")
    parts.append(f"<tr><th>files read</th><td>{len(reads)} calls · "
                 f"{mx.get('unique_files_read', 0)} unique · {mx.get('re_reads', 0)} re-reads</td></tr>")
    tc = mx.get("tool_calls", {})
    parts.append(f"<tr><th>tool calls</th><td>{esc(', '.join(f'{k}×{v}' for k, v in sorted(tc.items())) or '—')}</td></tr>")
    parts.append(f"<tr><th>artifacts</th><td>{len(arts)}</td></tr></table>")

    for art, hits in (mx.get("auto_checks") or {}).items():
        for label, samples in hits.items():
            parts.append(f'<div class="flag">⚠ {esc(label)} in <code>{esc(art)}</code>: {esc(", ".join(samples))}</div>')
    for art, hexes in (mx.get("non_palette_hexes") or {}).items():
        parts.append(f'<div class="softflag">hexes not in the known palette list in <code>{esc(art)}</code> '
                     f'(check manually): {esc(", ".join("#" + h for h in hexes[:12]))}</div>')

    parts.append(f"<details><summary>Prompt</summary><pre>{esc((cell / 'prompt.md').read_text())}</pre></details>")
    parts.append(f"<details open><summary>Agent's final message</summary><pre>{esc(mx.get('final_message', ''))}</pre></details>")
    parts.append("<details><summary>Files read, in order</summary><pre>"
                 + esc("\n".join(reads) or "(none)") + "</pre></details>")
    if arts:
        links = " · ".join(f'<a href="{esc(rel)}/artifacts/{esc(a)}">{esc(a)}</a>' for a in arts)
        parts.append(f"<p>Artifacts: {links}</p>")
    if primary:
        parts.append(f'<iframe src="{esc(rel)}/artifacts/{esc(primary)}" loading="lazy"></iframe>')
    parts.append(f'''<div class="grade">Designer grade:
      <label><input type="radio" name="g-{esc(cid)}" value="pass" onchange="save('{esc(cid)}')"> pass</label>
      <label><input type="radio" name="g-{esc(cid)}" value="minor" onchange="save('{esc(cid)}')"> minor issues</label>
      <label><input type="radio" name="g-{esc(cid)}" value="fail" onchange="save('{esc(cid)}')"> fail</label>
      <textarea id="n-{esc(cid)}" placeholder="notes…" onblur="save('{esc(cid)}')"></textarea>
    </div></div>''')
    return "".join(parts)


def report(run_dir: Path):
    cells = sorted(p.parent for p in run_dir.glob("*/metrics.json"))
    body = "".join(cell_html(c, run_dir) for c in cells)
    loads = ";".join(f"load('{c.name}')" for c in cells)
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(run_dir.name)} — token-burn review</title><style>{CSS}</style></head>
<body><div class="page"><h1>Token-burn review — {esc(run_dir.name)}</h1>
<p>Grade each cell below (saved in your browser). Rubrics live in
<code>tests/token-burn/rubrics/</code>. When done, export your grades and
paste them back to Claude.</p>
<div class="toolbar"><button onclick="exportGrades()">Export grades</button>
<textarea id="export-out" style="display:none;width:100%;min-height:120px"></textarea></div>
{body}
<script>{GRADE_JS};window.addEventListener('DOMContentLoaded',()=>{{{loads}}});</script>
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
<h1>Token-burn runs</h1><ul>{''.join(rows) or '<li>none yet</li>'}</ul></div></body></html>"""
    (runs_dir / "index.html").write_text(page)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "collect":
        collect(Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))
    elif cmd == "report":
        report(Path(sys.argv[2]))
    elif cmd == "index":
        index(Path(sys.argv[2]))
    else:
        sys.exit(f"unknown subcommand: {cmd}")
