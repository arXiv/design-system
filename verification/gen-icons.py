#!/usr/bin/env python3
"""
The icons page — generated from docs/icons/, never hand-maintained.

docs/icons/ is the single source for every icon the design system uses: one
SVG file per icon, copied from the Lucide release named in docs/icons/VERSION
(ISC licence beside them), plus any arXiv-specific icon drawn to the same
24-unit grid and 2-unit stroke. Adding an icon is dropping a file in that
folder and running this script.

    python3 verification/gen-icons.py            # write docs/icons.html
    python3 verification/gen-icons.py --check    # fail if the page is stale

Only the icon grid is generated. The rest of docs/icons.html is written by
hand like any other page; the script rewrites the <ul class="icon-grid"> in
place, and the count in the sentence above it, and leaves everything else.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ICONS = REPO / "docs" / "icons"
PAGE = REPO / "docs" / "icons.html"


GRID = re.compile(r'(<ul class="icon-grid">\n)(.*?)(\n\s*</ul>)', re.S)
COUNT = re.compile(r"\b\d+ icons\b")


def grid():
    files = sorted(ICONS.glob("*.svg"))
    cells = []
    for f in files:
        svg = f.read_text(encoding="utf-8").strip()
        cells.append(
            '        <li class="icon-cell">\n'
            f"          {svg}\n"
            f'          <span class="icon-name">{f.stem}</span>\n'
            "        </li>"
        )
    return "\n".join(cells), len(files)


def render():
    text = PAGE.read_text(encoding="utf-8")
    cells, n = grid()
    m = GRID.search(text)
    if not m:
        raise SystemExit("icons.html has no <ul class=\"icon-grid\"> to fill")
    out = text[: m.start(2)] + cells + text[m.end(2):]
    return COUNT.sub(f"{n} icons", out, count=1)


def main():
    out = render()
    if "--check" in sys.argv:
        if PAGE.read_text(encoding="utf-8") == out:
            print("PASS  icons.html matches docs/icons/")
            return 0
        print("FAIL  icons.html is stale — run: python3 verification/gen-icons.py")
        return 1
    PAGE.write_text(out, encoding="utf-8")
    print(f"icons.html grid written: {len(list(ICONS.glob('*.svg')))} icons")
    return 0


if __name__ == "__main__":
    sys.exit(main())
