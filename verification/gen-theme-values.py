#!/usr/bin/env python3
"""
Light and dark values, written into the pages that show both.

The theme belongs to the whole page, so a page cannot show a light sample
beside a dark one from the live stylesheet. colors.html and dark-mode.html
show both anyway: this script reads each token's value in each theme from
the stylesheets, with check-contrast.py's parser, and writes it into the page.
The pages then need no script, and check-policies.py fails when a token
changes and the pages have not been regenerated.

    python3 verification/gen-theme-values.py           # write the values
    python3 verification/gen-theme-values.py --check   # fail if a page is stale

What it fills, in any docs page:
  - an element with data-mode="light" or "dark" and data-token="--ds-…": a
    .swatch gets the colour as its background, anything else as its text
    colour (a .contrast-ring as its outline), and a <code class="tint-hex">
    right after it gets the hex. data-surface="internal" reads the internal
    tools palette;
  - a .contrast-sample with data-mode: its ground (data-ground, or
    --ds-canvas) and its text (data-text, or --ds-text), and its
    .contrast-ratio: the hex of the token inside it and its contrast with
    the ground;
  - dark-mode.html's token table, from TOKENS below.
"""

import importlib.util
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"

_spec = importlib.util.spec_from_file_location("check_contrast", REPO / "verification" / "check-contrast.py")
cc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cc)

TOKENS = [
    "--ds-text", "--ds-text-muted", "--ds-text-disabled", "--ds-text-on-accent",
    "--ds-canvas", "--ds-surface", "--ds-surface-hover", "--ds-tint-warm", "--ds-zone-secondary-bg", "--ds-chrome",
    "--ds-border", "--ds-border-strong",
    "--ds-accent", "--ds-accent-strong", "--ds-accent-wash", "--ds-accent-surface", "--ds-accent-border",
    "--ds-link", "--ds-link-hover", "--ds-link-visited", "--ds-danger-fg",
    "--ds-success-bg", "--ds-success-border", "--ds-success-fg",
    "--ds-info-bg", "--ds-info-border", "--ds-info-fg",
    "--ds-warning-bg", "--ds-warning-border", "--ds-warning-fg",
    "--ds-error-bg", "--ds-error-border", "--ds-error-fg",
]


def palettes():
    (pub_l, pub_d), (int_l, int_d) = cc.palettes()
    return {("public", "light"): pub_l, ("public", "dark"): pub_d,
            ("internal", "light"): int_l, ("internal", "dark"): int_d}


def attr(tag, name):
    m = re.search(rf'\s{name}="([^"]*)"', tag)
    return m.group(1) if m else None


def with_style(tag, style):
    """The opening tag with its style attribute set to `style`."""
    if attr(tag, "style") is not None:
        return re.sub(r'\sstyle="[^"]*"', f' style="{style}"', tag)
    return tag[:-1] + f' style="{style}">'


def value(pal, tag):
    surface = attr(tag, "data-surface") or "public"
    token = attr(tag, "data-token")
    hexv = pal[(surface, attr(tag, "data-mode"))].get(token)
    if hexv is None:
        raise SystemExit(f"FAIL  {token} has no {attr(tag, 'data-mode')} value in the stylesheets")
    return hexv.lower()


def fill(text, pal):
    # A contrast sample: its ground and text, the colour inside it, and the ratio.
    def sample(m):
        tag, inner = m.group(1), m.group(2)
        mode, surface = attr(tag, "data-mode"), attr(tag, "data-surface") or "public"
        p = pal[(surface, mode)]
        ground = p[attr(tag, "data-ground") or "--ds-canvas"].lower()
        ink = p[attr(tag, "data-text") or "--ds-text"].lower()
        tok = re.search(r'<span class="(contrast-(?:link|ring))[^"]*" data-token="([^"]+)"[^>]*>', inner)
        fg = p[tok.group(2)].lower()
        prop = "outline-color" if tok.group(1) == "contrast-ring" else "color"
        inner = inner.replace(tok.group(0), with_style(tok.group(0), f"{prop}:{fg}"), 1)
        inner = re.sub(r'(<span class="contrast-ratio">)[^<]*(</span>)',
                       lambda r: f"{r.group(1)}{fg} · {cc.ratio(fg, ground):.2f}:1{r.group(2)}", inner)
        return with_style(tag, f"background:{ground};color:{ink}") + inner + "</div>"

    text = re.sub(r'(<div class="contrast-sample[^"]*"[^>]*\sdata-mode="[^"]+"[^>]*>)(.*?)</div>', sample, text)

    # A swatch and the hex after it.
    def swatch(m):
        tag, code = m.group(1), m.group(2)
        hexv = value(pal, tag)
        out = with_style(tag, f"background:{hexv}") + "</span>"
        if code is not None:
            out += f'<code class="tint-hex">{hexv}</code>'
        return out

    text = re.sub(r'(<span class="swatch"[^>]*\sdata-mode="[^"]+"[^>]*>)</span>(<code class="tint-hex">[^<]*</code>)?',
                  swatch, text)

    # The token table on dark-mode.html.
    def table(m):
        rows = []
        for t in TOKENS:
            light, dark = pal[("public", "light")][t].lower(), pal[("public", "dark")][t].lower()
            cell = lambda h: f'<span class="swatch" style="background:{h}"></span><code>{h}</code>'
            rows.append(f'          <tr><th scope="row"><code>{t}</code></th><td>{cell(light)}</td>'
                        f'<td>{cell(dark)}</td><td>{"holds" if light == dark else "flips"}</td></tr>')
        return m.group(1) + "\n" + "\n".join(rows) + "\n        " + m.group(2)

    text = re.sub(r'(<tbody id="theme-token-rows">).*?(</tbody>)', table, text, flags=re.S)
    return text


def main():
    check = "--check" in sys.argv
    pal = palettes()
    stale = []
    for path in sorted(DOCS.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        if "data-mode=" not in text and 'id="theme-token-rows"' not in text:
            continue
        new = fill(text, pal)
        if new != text:
            stale.append(path)
            if not check:
                path.write_text(new, encoding="utf-8")
    if check:
        for p in stale:
            print(f"FAIL  {p.relative_to(REPO)} — light and dark values do not match the stylesheets")
        if stale:
            print("run: python3 verification/gen-theme-values.py")
            return 1
        print("PASS  the light and dark values in the docs match the stylesheets")
        return 0
    print(f"{len(stale)} page(s) written" if stale else "nothing to do — every value is current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
