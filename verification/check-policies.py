#!/usr/bin/env python3
"""
Policy checks — arXiv design system

The rules in docs/DESIGN-POLICIES.md and AGENTS.md that a script can check.
check-drift.py guards facts written down twice; this guards rules that are
written down once and then quietly broken in a page.

Every rule here earned its place by being broken at least once in this repo.

Usage:
    python3 verification/check-policies.py

No dependencies, no network. Exit 0 = clean, 1 = at least one FAIL.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# blog-theme/ is a packaged copy of a separate project — see AGENTS.md.
ROOTS = [REPO / "docs", REPO / "mockups"]

FAILS = []


def fail(rule, where, detail):
    FAILS.append(rule)
    print(f"FAIL  {rule}\n      {where}\n      {detail}")


def ok(rule, detail):
    print(f"PASS  {rule} — {detail}")


def pages():
    for root in ROOTS:
        for p in sorted(root.rglob("*.html")):
            yield p, p.read_text(encoding="utf-8", errors="replace")


# ── The wordmark is a drawn mark, never letters ──
# A header or footer logo slot holding the bare word "arXiv" is the wordmark
# typed out, which is the thing DESIGN-POLICIES forbids. A logo slot naming a
# DIFFERENT property ("arXiv Design System") is that property's own wordmark
# and is fine — so the test is the bare word, not the presence of text.
LOGO_SLOT = re.compile(
    r"<a\b[^>]*class=\"[^\"]*ds-site-(?:header|footer)-logo[^\"]*\"[^>]*>(.*?)</a>",
    re.S | re.I,
)
BARE_WORDMARK = re.compile(r"^ar\s*xiv$", re.I)


def check_wordmark_not_typed():
    rule = "the wordmark is drawn, never typed"
    hits = 0
    for path, text in pages():
        for m in LOGO_SLOT.finditer(text):
            inner = re.sub(r"<[^>]+>", "", m.group(1))
            inner = re.sub(r"&[a-z]+;", "", inner).strip()
            if BARE_WORDMARK.match(inner):
                line = text[: m.start()].count("\n") + 1
                fail(
                    rule,
                    f"{path.relative_to(REPO)}:{line}",
                    f'logo slot contains the text "{inner}" — use '
                    "<img> with the SVG in docs/assets/images/logos/",
                )
            hits += 1
    if rule not in FAILS:
        ok(rule, f"{hits} logo slots")


# ── Self-hosted everything ──
# No fonts, icons, scripts or stylesheets from another origin. Data URIs and
# protocol-relative paths to our own assets are not what this is about; an
# absolute http(s) URL in a resource slot is.
EXTERNAL = re.compile(
    r"""(?:<link\b[^>]*href|<script\b[^>]*src|@import\s+url\(|src:\s*url\()"""
    r"""\s*["'(]?\s*(https?://[^"')\s]+)""",
    re.I,
)


def check_self_hosted():
    rule = "no external fonts, scripts or stylesheets"
    n = 0
    for path, text in pages():
        for m in EXTERNAL.finditer(text):
            line = text[: m.start()].count("\n") + 1
            fail(rule, f"{path.relative_to(REPO)}:{line}", f"loads {m.group(1)}")
        n += 1
    if rule not in FAILS:
        ok(rule, f"{n} pages")


def main():
    check_wordmark_not_typed()
    check_self_hosted()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAIL")
        sys.exit(1)
    print("clean")


if __name__ == "__main__":
    main()
