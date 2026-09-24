#!/usr/bin/env python3
"""design-system-components.css (build_components_css.py) is design-system.css minus the
OS-auto dark switch, for hosts that keep their own page. It must stay that:
  1. no `@media (prefers-color-scheme ...)`: it bled into hosts' unstyled elements;
  2. `color-scheme` only under `[data-theme]` or `@media print`, never on a bare `:root`;
  3. no selector, top-level or inside @media/@supports/@container, that matches a host's
     raw elements (`a`, `body`, `*`, …): the build drops such rules, so this fails only on a
     list that mixes one with a component selector;
  4. every `.ds-*` class of the full stylesheet survives;
  5. component rules only: no `@font-face`, `@import`, `@page`, `@namespace` (fonts are
     published as their own fonts.css).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import build_components_css  # noqa: E402


def preludes(css):
    """Every rule's selector list, including those inside @media/@supports/@container."""
    for start, end, prelude in build_components_css.top_level_blocks(css):
        if prelude.startswith(build_components_css.GROUPS):
            yield from preludes(css[css.index("{", start) + 1:end - 1])
        elif not prelude.startswith("@"):
            yield prelude


def main():
    canonical = open(os.path.join(ROOT, "docs", "design-system.css"), encoding="utf-8").read()
    out = build_components_css.generate(canonical)
    fails = []

    if "@media (prefers-color-scheme" in out:
        fails.append("INV1: @media (prefers-color-scheme ...) leaked into the component CSS")

    for start, end, prelude in build_components_css.top_level_blocks(out):
        block = out[start:end]
        if "color-scheme" in block and not (
            "[data-theme" in prelude or (prelude.startswith("@media") and "print" in prelude)
        ):
            fails.append(f"INV2: color-scheme outside [data-theme]/@media print -> {prelude[:60]}")
    for prelude in preludes(out):
        for selector in build_components_css.split_selectors(prelude):
            if build_components_css.bare(selector):
                fails.append(f"INV3: unscoped selector would style host elements -> {selector!r}")

    canon_classes = set(re.findall(r"\.ds-[A-Za-z0-9_-]+", canonical))
    out_classes = set(re.findall(r"\.ds-[A-Za-z0-9_-]+", out))
    missing = canon_classes - out_classes
    if missing:
        fails.append(f"INV4: {len(missing)} .ds- class(es) dropped, e.g. {sorted(missing)[:5]}")

    for _, _, prelude in build_components_css.top_level_blocks(out):
        if re.match(r"@(font-face|import|page|namespace)\b", prelude.strip()):
            fails.append(f"INV5: page-level at-rule in the component CSS -> {prelude.strip()[:40]}")
    for rule in re.findall(r"@(?:import|namespace)\b[^;]*;", re.sub(r"/\*.*?\*/", "", out, flags=re.S)):
        fails.append(f"INV5: page-level at-rule in the component CSS -> {rule[:40]}")

    if fails:
        print("FAIL  design-system-components.css derivation contract:")
        for f in fails:
            print("  - " + f)
        return 1
    print(
        f"PASS  component CSS derivation contract "
        f"({len(out_classes)} .ds- classes, [data-theme] dark kept, no OS-auto bleed)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
