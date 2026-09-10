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


# ── Every token a rule uses is a token that exists ──
# A var() naming a property nothing defines makes the whole declaration
# invalid and it is silently dropped — .ds-note shipped with no padding
# that way. Fallbacks (var(--x, 1rem)) are legitimate and skipped.
CSS_FILES = [REPO / "docs" / "design-system.css",
             REPO / "docs" / "internal" / "design-system-staff.css"]
DEFINED = re.compile(r"^\s*(--[\w-]+)\s*:", re.M)
USED = re.compile(r"var\(\s*(--[\w-]+)\s*\)")


def check_tokens_defined():
    rule = "every var() names a token that exists"
    defined = set()
    for f in CSS_FILES:
        defined |= set(DEFINED.findall(f.read_text()))
    # a page may define its own; collect those too rather than false-alarm
    for path, text in pages():
        defined |= set(DEFINED.findall(text))
    n = 0
    for f in CSS_FILES:
        text = f.read_text()
        for m in USED.finditer(text):
            n += 1
            if m.group(1) not in defined:
                line = text[: m.start()].count("\n") + 1
                fail(rule, f"{f.relative_to(REPO)}:{line}",
                     f"var({m.group(1)}) is never defined — the whole declaration is dropped")
    if rule not in FAILS:
        ok(rule, f"{n} references")


# ── One name per surface ──
# The two surfaces are "the public site" and "internal tools" (DESIGN-POLICIES).
# "Staff" is for people, not for the surface, its stylesheet or its pages —
# a second name for one thing reads as a third thing.
SURFACE_SYNONYM = re.compile(
    r"staff[- ](tool|tools|surface|surfaces|stylesheet|page|pages|screen|screens|accent|form|forms|only)\b",
    re.I,
)
PROSE = ["docs", "AGENTS.md", "README.md"]


def check_one_name_per_surface():
    rule = 'the surface is called "internal tools", never "staff"'
    n = 0
    for base in PROSE:
        b = REPO / base
        paths = [b] if b.is_file() else [
            q for q in b.rglob("*") if q.suffix in {".html", ".md", ".css"}
        ]
        for q in paths:
            text = q.read_text(encoding="utf-8", errors="replace")
            n += 1
            # Naming a term AS a term is fine — `staff tools` in backticks or a
            # <code> span is the rule quoting what not to write. Blank those
            # out (same length, so line numbers survive) before scanning.
            text = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), text)
            text = re.sub(r"<code>.*?</code>", lambda m: " " * len(m.group(0)), text, flags=re.S)
            for m in SURFACE_SYNONYM.finditer(text):
                line = text[: m.start()].count("\n") + 1
                fail(rule, f"{q.relative_to(REPO)}:{line}",
                     f'"{m.group(0)}" — say "internal tools" / "the internal stylesheet"')
    if rule not in FAILS:
        ok(rule, f"{n} files")


def main():
    check_wordmark_not_typed()
    check_self_hosted()
    check_tokens_defined()
    check_one_name_per_surface()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAIL")
        sys.exit(1)
    print("clean")


if __name__ == "__main__":
    main()
