#!/usr/bin/env python3
"""
Surface-drift checks — arXiv design system

Three surfaces (internal, public, outreach) share one palette and one set
of components. Drift is what happens when a copy of a value gets edited on
one side only. Every check here guards a place where the same fact is
written down twice and nothing but discipline keeps the copies equal.

Usage:
    python3 verification/check-drift.py

No dependencies, no network. Exit 0 = clean. FAIL means the copies
disagree and one of them is now wrong. NOTE is for review, not a failure.

The WordPress blog theme is a SEPARATE PROJECT, not a copy kept in lockstep.
It extends the design system rather than mirroring it, and it is brought up to
date by a deliberate translation pass, not opportunistically. So divergence
there is reported as a NOTE, never a FAIL — the list of differences IS the
worklist for that pass, not a defect to fix in passing. Consumers are checked
when present on this machine; when they are not, the check reports SKIP rather
than passing silently. Point at a different checkout with:

    python3 verification/check-drift.py --consumer /path/to/arxiv-blog-theme
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PUBLIC_CSS = REPO / "docs" / "design-system.css"
INTERNAL_CSS = REPO / "docs" / "internal" / "internal-tools.css"
DEFAULT_CONSUMER = REPO.parent / "arxiv-blog-theme"

FAILS = []
NOTES = []


def fail(name, detail):
    FAILS.append(name)
    print(f"FAIL  {name}\n      {detail}")


def ok(name):
    print(f"PASS  {name}")


def note(name, detail):
    NOTES.append(name)
    print(f"NOTE  {name}\n      {detail}")


def skip(name, detail):
    print(f"SKIP  {name}\n      {detail}")


def matching_block(text, start):
    """Return the {...} block whose opening brace follows index `start`."""
    i = text.index("{", start)
    depth = 0
    while True:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[text.index("{", start) + 1 : i]
        i += 1


def declarations(css):
    """Every `prop: value;` in a chunk of CSS, comments stripped, in order."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    return [
        (m.group(1).strip(), " ".join(m.group(2).split()))
        for m in re.finditer(r"([-\w]+)\s*:\s*([^;{}]+);", css)
    ]


def rules(css):
    """{selector: [declarations]} for a chunk of CSS, comments stripped."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out = {}
    for m in re.finditer(r"([^{}@]+)\{([^{}]*)\}", css):
        sel = " ".join(m.group(1).split())
        if not sel:
            continue
        out.setdefault(sel, []).extend(declarations(m.group(2)))
    return out


# ── 1. The dark mirror ──────────────────────────────────────────────
# docs/design-system.css states the dark palette twice: once under
# @media (prefers-color-scheme: dark) for the OS preference, once under
# [data-theme="dark"] so a surface with its own toggle can force it.
# The second is a mirror of the first. If they disagree, one of the two
# ways a reader can arrive at dark mode is now painting the wrong colors.
def check_dark_mirror():
    name = "dark mirror matches the @media block (public stylesheet)"
    css = PUBLIC_CSS.read_text()
    media = matching_block(css, css.index("@media (prefers-color-scheme: dark)"))
    expected = rules(
        # The mirror is scopable: it drops the :root / html prefix so a
        # data-theme island anywhere in the DOM picks up the same values.
        media.replace(':root:not([data-theme="light"])', '[data-theme="dark"]').replace(
            'html:not([data-theme="light"])', '[data-theme="dark"]'
        )
    )
    # The mirror is everything after the @media block that keys on
    # [data-theme="dark"] without a :not() guard.
    after = css[css.index("@media (prefers-color-scheme: dark)") :]
    after = after[len(matching_block(after, 0)) :]
    actual = {s: d for s, d in rules(after).items() if '[data-theme="dark"]' in s and ":not(" not in s}

    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    if missing or extra:
        return fail(
            name,
            f"selectors only in @media: {missing or 'none'}; only in mirror: {extra or 'none'}",
        )
    for sel in expected:
        if expected[sel] != actual[sel]:
            differing = [
                f"{p}: {v}" for p, v in expected[sel] if (p, v) not in actual[sel]
            ]
            return fail(name, f"{sel} differs — @media has {differing}")
    ok(name)


# ── 2. Consumers that bundle a copy of the stylesheet ───────────────
# The WordPress theme cannot link a stylesheet from another origin (and our
# policy forbids it anyway), so it ships its own copy. That copy is allowed to
# diverge: the blog is a separate project that extends the design system, more
# playful and more colorful than arxiv.org would ever be. What this check
# produces is the diff to consider at the next translation pass — deliberately
# a NOTE, so nobody "fixes" it by overwriting the theme's own decisions.
def check_bundled_copy(consumer):
    name = "blog theme's stylesheet vs canonical (separate project — informational)"
    bundled = consumer / "assets" / "css" / "design-system.css"
    if not bundled.exists():
        return skip(name, f"no consumer checkout at {consumer}")

    canon_decls = declarations(PUBLIC_CSS.read_text())
    bundled_decls = declarations(bundled.read_text())
    if canon_decls == bundled_decls:
        # Comments can still differ (the copy lags on prose edits); say so
        # without failing, since no rendered pixel depends on them.
        if bundled.read_text() != PUBLIC_CSS.read_text():
            note(name, "declarations identical; comments differ — refresh the copy when convenient")
        else:
            ok(name)
        return

    canon_map, bundled_map = dict(canon_decls), dict(bundled_decls)
    diffs = [
        f"{p}: canonical {v!r} vs bundled {bundled_map.get(p)!r}"
        for p, v in canon_map.items()
        if p.startswith("--") and bundled_map.get(p, v) != v
    ]
    note(
        name,
        ((f"{len(diffs)} token value(s) differ: " + "; ".join(diffs[:5]))
         if diffs
         else f"{abs(len(canon_decls) - len(bundled_decls))} declaration(s) differ")
        + " — expected. Blog is a separate project; translate deliberately, do not overwrite.",
    )


# ── 3. Shared .ds- names across surfaces ────────────────────────────
# Both stylesheets define some .ds- classes. Sharing a NAME is fine — the
# same component wearing each surface's tokens. Sharing a name while the
# constructions have drifted apart means an agent reading one page builds
# something that looks wrong on the other surface.
def check_shared_names():
    name = "shared .ds- class names agree across public and internal"
    pub, intl = rules(PUBLIC_CSS.read_text()), rules(INTERNAL_CSS.read_text())

    def classes(rs):
        out = {}
        for sel, decls in rs.items():
            for cls in re.findall(r"\.(ds-[\w-]+)", sel):
                if sel.strip() == "." + cls:  # base rule only
                    out[cls] = decls
        return out

    pub_c, intl_c = classes(pub), classes(intl)
    shared = sorted(set(pub_c) & set(intl_c))
    if not shared:
        return ok(name + " (none shared)")
    drifted = []
    for cls in shared:
        props_p = {p for p, _ in pub_c[cls]}
        props_i = {p for p, _ in intl_c[cls]}
        only = (props_p ^ props_i) - {"color", "background", "background-color", "border-color"}
        if only:
            drifted.append(f".{cls} ({', '.join(sorted(only))})")
    if drifted:
        note(
            name,
            "same name, different construction — intended variant, or drift? "
            + "; ".join(drifted),
        )
    else:
        ok(name + f" ({len(shared)} shared)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--consumer", type=Path, default=DEFAULT_CONSUMER)
    args = ap.parse_args()

    check_dark_mirror()
    check_bundled_copy(args.consumer)
    check_shared_names()

    print()
    if FAILS:
        print(f"{len(FAILS)} FAIL, {len(NOTES)} NOTE")
        sys.exit(1)
    print(f"clean — {len(NOTES)} NOTE" if NOTES else "clean")


if __name__ == "__main__":
    main()
