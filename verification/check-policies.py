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
             REPO / "docs" / "internal-tools.css"]
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
    REPO / "docs" / "internal-tools.css",
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


# ── The theme control is on every page, and lands before first paint ──
# theme.js writes the attribute synchronously in the head. Deferring it, or
# leaving it off a page, brings back the flash of the wrong theme — worst for
# exactly the reader who chose dark because light hurts.
THEME_SCRIPT = re.compile(r"<script[^>]*src=\"[^\"]*theme\.js\"([^>]*)>")


def check_theme_control():
    rule = "every page carries the theme control, unblocked"
    n = 0
    for path in sorted((REPO / "docs").rglob("*.html")):
        if path.name == "doc.html":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = str(path.relative_to(REPO))
        n += 1
        # A page documenting the control shows its markup in a code block.
        # Same rule as the naming check: a term quoted as a term is not a use.
        text = re.sub(r"<pre\b.*?</pre>", "", text, flags=re.S)
        m = THEME_SCRIPT.search(text)
        if not m:
            fail(rule, rel, "does not load theme.js")
            continue
        if "defer" in m.group(1) or "async" in m.group(1):
            fail(rule, rel, "loads theme.js deferred — the attribute must land before first paint")
        if text.count('class="ds-theme-toggle"') != 1:
            fail(rule, rel, f'{text.count(chr(34)+"ds-theme-toggle"+chr(34))} theme toggles; expected exactly 1')
        if 'id="ds-theme-status"' not in text:
            fail(rule, rel, "no #ds-theme-status live region for the toggle to announce into")
    if rule not in FAILS:
        ok(rule, f"{n} pages")


# ── A contents bar needs its script ──
# The bar is markup, but its behaviour (menu closes on a choice, the current
# section is named, the bar compacts once it sticks) is toc.js. A page that
# has the one without the other looks right until it is scrolled.
TOC_SCRIPT = re.compile(r"<script[^>]*src=\"[^\"]*toc\.js\"")


def check_toc_script():
    rule = "every page with a contents bar loads toc.js"
    n = 0
    for path in sorted((REPO / "docs").rglob("*.html")):
        text = path.read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"<pre\b.*?</pre>", "", text, flags=re.S)
        if 'class="ds-full ds-toc-bar' not in text and 'class="ds-toc-bar' not in text:
            continue
        n += 1
        if not TOC_SCRIPT.search(text):
            fail(rule, str(path.relative_to(REPO)), "has a .ds-toc-bar but does not load toc.js")
    if rule not in FAILS:
        ok(rule, f"{n} pages")


# ── The docs do not narrate their own history ──
# The system is new and in use nowhere, so a reader needs to know what a thing
# IS. "Previously", "we dropped", a decision date in the prose — all of it is
# a changelog in the wrong place. Decisions live in planning/; git is the log.
HISTORY = re.compile(
    r"\b(decided 20\d\d|settled 20\d\d|reviewed 20\d\d|renamed 20\d\d"
    r"|we (?:rejected|dropped|removed|replaced)|the earlier version"
    r"|until today|before this existed|retired from|has been renamed)\b",
    re.I,
)


def check_no_changelog_prose():
    rule = "the docs describe what things are, not how they changed"
    n = 0
    for path in sorted((REPO / "docs").rglob("*.html")):
        if path.name == "doc.html":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if "<body" not in text:
            continue
        body = text[text.index("<body") :]
        body = re.sub(r"<style.*?</style>|<script.*?</script>", "", body, flags=re.S)
        n += 1
        for m in HISTORY.finditer(re.sub(r"<[^>]+>", " ", body)):
            fail(rule, str(path.relative_to(REPO)),
                 f'"{m.group(0)}" — the system is new; say what it is, not what it was')
    if rule not in FAILS:
        ok(rule, f"{n} pages")


# ── Every class a builder can write is findable in the docs ──
# A class that exists and is documented nowhere is a class nobody uses, or
# worse, one somebody re-invents. The exemptions are classes the SCRIPTS own:
# a page author never writes them, so there is nothing for the docs to say.
CLASS_RE = re.compile(r"\.((?:ds-|btn-|type-|info-|seg-)[\w-]+)")
SCRIPT_OWNED = {
    "ds-code-copy-idle", "ds-code-copy-done",      # copy-code.js swaps these
    "ds-theme-icon-system", "ds-theme-icon-light", "ds-theme-icon-dark",  # theme.js
}


def check_classes_documented():
    rule = "every class a builder can write appears in the docs"
    classes = set()
    for f in CSS_FILES:
        classes |= set(CLASS_RE.findall(re.sub(r"/\*.*?\*/", "", f.read_text(), flags=re.S)))
    prose = []
    for path in (REPO / "docs").rglob("*.html"):
        if path.name == "doc.html":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        prose.append(text[text.index("<body") :] if "<body" in text else text)
    prose = "\n".join(prose)
    missing = sorted(c for c in classes - SCRIPT_OWNED if c not in prose)
    for c in missing:
        fail(rule, "docs/", f".{c} is in a stylesheet and on no page")
    if rule not in FAILS:
        ok(rule, f"{len(classes)} classes, {len(SCRIPT_OWNED)} script-owned")


# ── Section anchors are generated and current ──
# Delegates to gen-anchors.py so the rule lives in one place: the script that
# writes the ids is the script that knows what they should be.
def check_section_anchors():
    rule = "every section heading has a generated anchor"
    import subprocess
    r = subprocess.run(
        [sys.executable, str(REPO / "verification" / "gen-anchors.py"), "--check"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        for line in r.stdout.splitlines():
            if line.startswith("FAIL"):
                fail(rule, line.split("—")[0].replace("FAIL", "").strip(),
                     "run: python3 verification/gen-anchors.py")
        return
    ok(rule, "checked by gen-anchors.py")


def main():
    check_wordmark_not_typed()
    check_self_hosted()
    check_tokens_defined()
    check_one_name_per_surface()
    check_relative_type_sizes()
    check_page_shape()
    check_theme_control()
    check_toc_script()
    check_no_changelog_prose()
    check_classes_documented()
    check_section_anchors()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAIL")
        sys.exit(1)
    print("clean")


if __name__ == "__main__":
    main()
