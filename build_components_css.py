"""Derive design-system-components.css from docs/design-system.css.

docs/design-system.css is a whole-page stylesheet: besides the components, it switches the
page to dark on a dark OS (`@media (prefers-color-scheme: dark)`) and styles the page itself
(the print block's `body`). Dropped into a host page that keeps its own styling
(arxiv-browse's arXiv.css), those rules bleed into the host's unstyled elements (dark UA
defaults, washed-out links). The component stylesheet is the same file without them; dark
stays available through the host-controlled [data-theme] blocks (docs/dark-mode.html).
verification/check-components.py enforces the result.

    python3 build_components_css.py [docs/design-system.css [out.css]]
"""
import sys

BANNER = (
    "/* GENERATED from design-system.css by build_components_css.py — do not edit.\n"
    "   Components + tokens; OS-auto dark (@media prefers-color-scheme) and page-level rules\n"
    "   removed. Dark is host-controlled via [data-theme] (design system's theme.js /\n"
    "   .ds-theme-toggle). Safe to drop into a host page; regenerate, never hand-maintain. */\n"
)
# The at-rules whose rules are filtered like top-level ones.
GROUPS = ("@media", "@supports", "@container")


def top_level_blocks(css: str):
    """Yield (start, end, prelude) for each top-level rule or at-rule block, skipping
    comments. `css[start:end]` is the whole block."""
    i, n, depth, start = 0, len(css), 0, None
    while i < n:
        if css.startswith("/*", i):
            j = css.find("*/", i + 2)
            i = n if j == -1 else j + 2
            continue
        c = css[i]
        if depth == 0 and start is None:
            if not c.isspace():
                start = i
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                yield start, i + 1, css[start:css.index("{", start)].strip()
                start = None
        i += 1


def split_selectors(prelude: str) -> list[str]:
    """A selector list's selectors, split on top-level commas only (not inside :is())."""
    parts, depth, cur = [], 0, ""
    for ch in prelude:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    return [p.strip() for p in parts + [cur] if p.strip()]


def bare(selector: str) -> bool:
    """Whether a selector matches a host's own elements (`a`, `body`, `*`): no class, id or
    attribute anchor, and not a :root/html scope."""
    return not any(tok in selector for tok in (".", "#", "[", ":root", "html"))


def generate(css: str) -> str:
    """The component stylesheet: `css` without its OS-auto dark block(s) and page-level rules."""
    return BANNER + _components(css)


def _components(css: str) -> str:
    out, pos = [], 0
    for start, end, prelude in top_level_blocks(css):
        if (prelude.startswith("@media") and "prefers-color-scheme" in prelude) or (
                not prelude.startswith("@") and all(bare(s) for s in split_selectors(prelude))):
            keep = ""
        elif prelude.startswith(GROUPS):
            body = css.index("{", start) + 1
            keep = css[start:body] + _components(css[body:end - 1]) + "}"
        else:
            continue
        out.append(css[pos:start] + keep)
        pos = end
    return "".join(out) + css[pos:]


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "docs/design-system.css"
    with open(src, encoding="utf-8") as f:
        result = generate(f.read())
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(result)
    else:
        sys.stdout.write(result)
