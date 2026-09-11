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
             REPO / "docs" / "internal" / "internal-tools.css"]
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


# ── Type sizes are relative, so a reader's font-size setting reaches them ──
# typography.html, "Sizes are rem, never px". The rule existed for six weeks
# before anything checked it, and tier 1 went from 6 px font sizes to 17 in
# that time. The one guard that existed ran in a browser against the abstract
# mockup and read the stylesheets THAT page loads — and it loads none, so it
# never saw design-system.css and reported green throughout.
#
# Deferred by name, not by silence: the two admin console mockups are 100% px
# (92 and 55) and belong to the internal tools work, not to this. They report
# as a NOTE, the way check-drift.py defers the blog theme.
PX_FONT = re.compile(r"font-size:\s*([0-9.]+)px")
TYPE_REQUIRED = [
    REPO / "docs" / "design-system.css",
    REPO / "docs" / "internal" / "internal-tools.css",
    REPO / "mockups" / "public" / "html-phase1.html",
    REPO / "mockups" / "public" / "abstract-phase2.html",
]
TYPE_DEFERRED = [
    REPO / "mockups" / "internal" / "admin-console" / "user-page" / "index.html",
    REPO / "mockups" / "internal" / "admin-console" / "paper-details" / "index.html",
]


def check_relative_type_sizes():
    rule = "type sizes are rem, never px"
    total = 0
    for f in TYPE_REQUIRED:
        if not f.exists():
            continue
        text = re.sub(r"/\*.*?\*/", "", f.read_text(), flags=re.S)
        hits = list(PX_FONT.finditer(text))
        total += 1
        for m in hits[:6]:
            line = text[: m.start()].count("\n") + 1
            px = float(m.group(1))
            fail(rule, f"{f.relative_to(REPO)}:{line}",
                 f"font-size: {m.group(1)}px — write {px / 16:g}rem so a reader's "
                 "font-size setting reaches it")
        if len(hits) > 6:
            print(f"      ...and {len(hits) - 6} more in {f.relative_to(REPO)}")
    deferred = 0
    for f in TYPE_DEFERRED:
        if f.exists():
            deferred += len(PX_FONT.findall(f.read_text()))
    if deferred:
        print(f"NOTE  {rule} — {deferred} px font sizes in the two admin console "
              "mockups,\n      deferred with the internal tools work (planning/NEXT-STEPS.md 20a)")
    if rule not in FAILS:
        ok(rule, f"{total} files")


# ── One page shape ──
# <title> is "<Name> — arXiv Design System" and no page name carries "Styles"
# or "Component Reference". Seven pages still did after their files were
# renamed, which is how a reader ends up with two names for one component.
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
BANNED_IN_NAME = re.compile(r"\b(Component Reference|Styles)\b")


def check_page_shape():
    rule = "every docs page is named the same way"
    n = 0
    for path in sorted((REPO / "docs").rglob("*.html")):
        if path.name == "doc.html":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        m = TITLE_RE.search(text)
        rel = path.relative_to(REPO)
        n += 1
        if not m:
            fail(rule, str(rel), "no <title>")
            continue
        title = re.sub(r"\s+", " ", m.group(1)).strip()
        if not title.endswith("— arXiv Design System"):
            fail(rule, str(rel), f'title "{title}" should end "— arXiv Design System"')
        if BANNED_IN_NAME.search(title):
            fail(rule, str(rel), f'title "{title}" still says Styles / Component Reference')
        h = H1_RE.search(text)
        if h and BANNED_IN_NAME.search(re.sub(r"<[^>]+>", "", h.group(1))):
            fail(rule, str(rel), "the <h1> still says Styles / Component Reference")
    if rule not in FAILS:
        ok(rule, f"{n} pages")


def main():
    check_wordmark_not_typed()
    check_self_hosted()
    check_tokens_defined()
    check_one_name_per_surface()
    check_relative_type_sizes()
    check_page_shape()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAIL")
        sys.exit(1)
    print("clean")


if __name__ == "__main__":
    main()
