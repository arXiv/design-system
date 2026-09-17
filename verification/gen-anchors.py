#!/usr/bin/env python3
"""
Section anchors — generated, never hand-maintained.

Every `.section-title` gets an `id` derived from its own text, written into
the HTML rather than added at runtime: a real id works with JavaScript off,
works for an incoming link from another page, and is there when the browser
resolves the fragment on first load — none of which a script running at
DOMContentLoaded can promise.

    python3 verification/gen-anchors.py            # write the ids
    python3 verification/gen-anchors.py --check    # fail if any are missing or stale

An id follows its heading, so rewording a heading changes its anchor. That is
the right trade while the system is new and nothing links in from outside;
--check is what tells you to re-run this after an edit.

A heading that already carries a hand-written id keeps it. Those are anchors
something already links to, and silently renaming them would break the link.

A page with a contents bar (.ds-toc-menu) gets its list from the same
headings, for the same reason: written into the HTML, so it works with
JavaScript off, and regenerated, so nobody keeps it in step by hand.
"""

import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
HEADING = re.compile(r"<h2([^>]*)\sclass=\"section-title\"([^>]*)>(.*?)</h2>", re.S)


def slug(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&[a-z]+;|&#\d+;", " ", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text)[:60].strip("-")


def process(path, write):
    text = path.read_text(encoding="utf-8")
    seen, problems, out, last = {}, [], [], 0
    for m in HEADING.finditer(text):
        before, after, inner = m.group(1), m.group(2), m.group(3)
        existing = re.search(r'\bid="([^"]+)"', before + after)
        want = slug(inner)
        if not want:
            continue
        seen[want] = seen.get(want, 0) + 1
        if seen[want] > 1:
            want = f"{want}-{seen[want]}"
        if existing:
            # Hand-written ids are kept: something links to them already.
            continue
        out.append(text[last:m.start()])
        out.append(f'<h2{before} class="section-title"{after} id="{want}">{inner}</h2>')
        last = m.end()
        problems.append(want)
    out.append(text[last:])
    if problems and write:
        path.write_text("".join(out), encoding="utf-8")
    return problems


TOC_LIST = re.compile(r'(<nav class="ds-toc-menu"[^>]*>\s*<ol>)(.*?)(</ol>)', re.S)


def contents(path, write):
    """Rewrite the contents list from the page's section headings. True if it was stale."""
    text = path.read_text(encoding="utf-8")
    m = TOC_LIST.search(text)
    if not m:
        return False
    indent = "            "
    items = []
    for h in re.finditer(r'<h2([^>]*\sclass="section-title"[^>]*)>(.*?)</h2>', text, re.S):
        hid = re.search(r'\bid="([^"]+)"', h.group(1))
        if hid:
            label = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h.group(2))).strip()
            items.append(f'{indent}<li><a href="#{hid.group(1)}">{label}</a></li>')
    want = "\n" + "\n".join(items) + "\n" + indent[:-2]
    if m.group(2) == want:
        return False
    if write:
        path.write_text(text[:m.start(2)] + want + text[m.end(2):], encoding="utf-8")
    return True


def main():
    check = "--check" in sys.argv
    total, files, stale_toc = 0, 0, []
    for path in sorted(DOCS.rglob("*.html")):
        if path.name == "doc.html":
            continue
        added = process(path, write=not check)
        if contents(path, write=not check):
            stale_toc.append(path)
            if check:
                print(f"FAIL  {path.relative_to(REPO)} — contents list does not match its section headings")
        if added:
            total += len(added)
            files += 1
            if check:
                print(f"FAIL  {path.relative_to(REPO)} — {len(added)} section(s) with no anchor: "
                      + ", ".join(added[:4]))
    if check:
        if total or stale_toc:
            print(f"\n{total} missing anchors in {files} files, {len(stale_toc)} stale contents lists"
                  " — run: python3 verification/gen-anchors.py")
            return 1
        print("PASS  every section heading has a generated anchor")
        return 0
    if stale_toc:
        print(f"{len(stale_toc)} contents list(s) rewritten")
    print(f"{total} anchors written across {files} files" if total else "nothing to do — all anchors present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
