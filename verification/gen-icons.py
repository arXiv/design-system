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

The page's shell (head, nav, scripts) is copied from docs/tags.html so the
generated page carries the same hand-copied nav as every other page.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ICONS = REPO / "docs" / "icons"
PAGE = REPO / "docs" / "icons.html"
SHELL = REPO / "docs" / "tags.html"


def shell():
    text = SHELL.read_text(encoding="utf-8")
    head = text[: text.index('<div class="ds-container')]
    tail = text[text.rindex("<script>") :]
    head = head.replace("<title>Tags — arXiv Design System</title>", "<title>Icons — arXiv Design System</title>")
    head = head.replace('<a href="tags.html" aria-current="page">Tags</a>', '<a href="tags.html">Tags</a>')
    head = head.replace('<a href="icons.html">Icons</a>', '<a href="icons.html" aria-current="page">Icons</a>')
    if 'href="docs.css"' not in head:
        head = head.replace('<link rel="stylesheet" href="design-system.css">\n', '<link rel="stylesheet" href="design-system.css">\n  <link rel="stylesheet" href="docs.css">\n')
    return head, tail


def render():
    version = (ICONS / "VERSION").read_text().strip() if (ICONS / "VERSION").exists() else "unpinned"
    files = sorted(ICONS.glob("*.svg"))
    cells = []
    for f in files:
        svg = f.read_text(encoding="utf-8").strip()
        cells.append(
            f'      <li class="icon-cell">\n'
            f"        {svg}\n"
            f'        <span class="icon-name">{f.stem}</span>\n'
            f"      </li>"
        )
    head, tail = shell()
    body = f'''<div class="ds-container ds-zone-secondary">

  <header class="ds-page-header">
    <h1>Icons</h1>
    <p>Every icon the design system uses, and only those. One icon language: stroke drawings on a
    24-unit grid, from the {version.replace("lucide", "Lucide")} release, with any arXiv-specific
    icon drawn to the same rule. The source is <code>docs/icons/</code>, one file per icon; this page
    is generated from it.</p>
  </header>

  <div class="ds-full ds-zone-primary">

  <section class="section">
    <h2 class="section-title" id="the-set">The set</h2>
    <p class="ds-section-desc">{len(files)} icons. The name under each is the file name.</p>
    <ul class="icon-grid">
{chr(10).join(cells)}
    </ul>
  </section>

  <section class="section">
    <h2 class="section-title" id="using-an-icon">Using an icon</h2>
    <p class="ds-section-desc">Copy the file&rsquo;s contents into the page where the icon goes. The
    icon inherits the text colour around it, and it is hidden from assistive technology, so the
    control or text beside it carries the meaning.</p>
    <div class="ds-card">
      <button class="ds-btn ds-btn-secondary" type="button">{(ICONS / "download.svg").read_text().strip()} Download PDF</button>
      <details class="ds-acc"><summary>Relevant code</summary><div class="ds-acc-body">
<pre><code>&lt;button class="ds-btn ds-btn-secondary" type="button"&gt;
  &lt;svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
       stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"&gt;…&lt;/svg&gt;
  Download PDF
&lt;/button&gt;</code></pre>
        <dl>
          <dt>aria-hidden="true"</dt>
          <dd>On every icon. The icon never carries meaning on its own: a button gets its name from
          its label or an <code>.is-sr-only</code> span, and an icon beside text is decoration.</dd>
          <dt>stroke="currentColor"</dt>
          <dd>The icon takes the colour of the text around it, in every state and both themes.</dd>
          <dt>No width or height</dt>
          <dd>The component that holds the icon sizes it in <code>em</code>, so it follows the
          control&rsquo;s own type size. A bare icon in text takes the line&rsquo;s height.</dd>
        </dl>
      </div></details>
    </div>
  </section>

  </div>

  <section class="section">
    <h2 class="section-title" id="adding-an-icon">Adding an icon</h2>
    <ul class="notes">
      <li><strong>From the set.</strong> Take the file from the Lucide release named in
      <code>docs/icons/VERSION</code>, keep its name, and put it in <code>docs/icons/</code>.</li>
      <li><strong>Drawn for arXiv.</strong> A 24-unit grid, a 2-unit stroke, round caps and joins, no
      fills, no ids or styles. If it cannot be told apart from the set, it belongs.</li>
      <li><strong>Then run</strong> <code>python3 verification/gen-icons.py</code>. The page rewrites
      itself; nobody edits it.</li>
    </ul>
  </section>

</div>

'''
    return head + body + tail


def main():
    out = render()
    if "--check" in sys.argv:
        if PAGE.exists() and PAGE.read_text(encoding="utf-8") == out:
            print("PASS  icons.html matches docs/icons/")
            return 0
        print("FAIL  icons.html is stale — run: python3 verification/gen-icons.py")
        return 1
    PAGE.write_text(out, encoding="utf-8")
    print(f"icons.html written: {len(list(ICONS.glob('*.svg')))} icons")
    return 0


if __name__ == "__main__":
    sys.exit(main())
