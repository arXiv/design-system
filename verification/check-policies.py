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
ROOTS = [REPO / "docs", REPO / "whiteboard" / "mockups"]

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
# No fonts, icons, scripts or stylesheets from a third party. Data URIs and
# protocol-relative paths to our own assets are not what this is about; an
# absolute http(s) URL in a resource slot is, unless it is arXiv's own static
# assets (arxiv.org), which is where DESIGN-POLICIES says they are served from.
EXTERNAL = re.compile(
    r"""(?:<script\b[^>]*?\bsrc\s*=|@import\s+(?:url\()?|src:\s*url\()"""
    r"""\s*["'(]?\s*(?!https?://(?:[\w-]+\.)?arxiv\.org/)(https?://[^"')\s>]+)""",
    re.I,
)
# A <link> loads something only with these rels; a canonical or alternate link
# to another origin loads nothing.
LINK = re.compile(r"<link\b[^>]*>", re.I)
LOADS = re.compile(r"""\brel\s*=\s*["']?[^"'>]*\b(?:stylesheet|preload|modulepreload|icon)\b""", re.I)
LINK_HREF = re.compile(r"""\bhref\s*=\s*["']?(?!https?://(?:[\w-]+\.)?arxiv\.org/)(https?://[^"'\s>]+)""", re.I)


def check_self_hosted():
    rule = "no external fonts, scripts or stylesheets"
    n = 0
    for path, text in pages():
        for m in EXTERNAL.finditer(text):
            line = text[: m.start()].count("\n") + 1
            fail(rule, f"{path.relative_to(REPO)}:{line}", f"loads {m.group(1)}")
        for m in LINK.finditer(text):
            href = LINK_HREF.search(m.group(0))
            if href and LOADS.search(m.group(0)):
                line = text[: m.start()].count("\n") + 1
                fail(rule, f"{path.relative_to(REPO)}:{line}", f"loads {href.group(1)}")
        n += 1
    if rule not in FAILS:
        ok(rule, f"{n} pages")


# ── Arrows are icons, never text characters ──
# A dropdown arrow drawn as a character ("▾" at a small font size) is a glyph
# from memory: it rendered at 10px on every header dropdown. Arrows come from
# docs/icons, as --ds-chevron does.
TEXT_ARROW = re.compile(r'content:\s*"[^"]*(?:\\25B[A-F]|\\25C[0-4]|[▴▸▾◂▲▶▼◀])')


def check_no_text_arrows():
    rule = "arrows are icons, never text characters"
    for f in [REPO / "docs" / "design-system.css", REPO / "docs" / "internal-tools.css"]:
        text = f.read_text()
        for m in TEXT_ARROW.finditer(text):
            line = text[: m.start()].count("\n") + 1
            fail(rule, f"{f.relative_to(REPO)}:{line}", "draw the arrow from docs/icons (see --ds-chevron)")
    if rule not in FAILS:
        ok(rule, "stylesheets")


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


# ── Colours come from tokens ──
# DESIGN-POLICIES: "Do not introduce one-off hex values." A colour written
# straight into a rule, instead of into a token, is one. White and black are
# allowed, at any opacity, and so are the component-internal constants listed
# on docs/colors.html, in the Tier 2 rule. The list is read from there so the
# exceptions are written down once.
COLOUR = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?)\([^)]*\)")
CONSTANTS_DOC = REPO / "docs" / "colors.html"


def rgb(colour):
    """The red, green and blue of a colour, ignoring opacity; None for hsl()."""
    if colour.startswith("#"):
        h = colour[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h[:3])
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))
    if colour.startswith("rgb"):
        return tuple(int(n) for n in re.findall(r"\d+", colour)[:3])
    return None


def check_colours_from_tokens():
    rule = "colours come from tokens (white, black and listed constants allowed)"
    m = re.search(r"Tier 2 — component-internal constants</strong>(.*?)<strong>Tier 3",
                  CONSTANTS_DOC.read_text(), flags=re.S)
    if m is None:
        return fail(rule, str(CONSTANTS_DOC.relative_to(REPO)),
                    "no Tier 2 rule to read the exceptions from")
    allowed = {(255, 255, 255), (0, 0, 0)}
    allowed |= {rgb(c) for c in COLOUR.findall(" ".join(re.findall(r"<code>([^<]+)</code>", m.group(1))))}
    n = 0
    for f in CSS_FILES:
        # Blank comments rather than drop them, so line numbers stay true.
        text = re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group(0)),
                      f.read_text(), flags=re.S)
        for d in re.finditer(r"([-\w]+)\s*:\s*([^;{}]+);", text):
            if d.group(1).startswith("--"):
                continue
            for c in COLOUR.finditer(d.group(2)):
                n += 1
                if rgb(c.group(0)) not in allowed:
                    at = text[: d.start(2) + c.start()].count("\n") + 1
                    fail(rule, f"{f.relative_to(REPO)}:{at}",
                         f"{d.group(1)}: {c.group(0)} — use a token, or list it as a "
                         "component-internal constant on docs/colors.html")
    if rule not in FAILS:
        ok(rule, f"{n} raw colours, all allowed")


# ── One name per surface ──
# The two surfaces are "public pages" and "internal tools" (DESIGN-POLICIES).
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
    REPO / "whiteboard" / "mockups" / "public" / "html-phase1.html",
    REPO / "whiteboard" / "mockups" / "public" / "abstract-phase2.html",
]
TYPE_DEFERRED = [
    REPO / "whiteboard" / "mockups" / "internal" / "admin-console" / "user-page" / "index.html",
    REPO / "whiteboard" / "mockups" / "internal" / "admin-console" / "paper-details" / "index.html",
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
              "mockups,\n      deferred with the internal tools work (whiteboard/planning/NEXT-STEPS.md, Mockups)")
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
        if text.count('class="ds-theme-toggle"') < 1:
            fail(rule, rel, "no theme toggle")
        if 'id="ds-theme-status"' not in text:
            fail(rule, rel, "no #ds-theme-status live region for the toggle to announce into")
    if rule not in FAILS:
        ok(rule, f"{n} pages")


# ── A TOC bar needs its script ──
# The bar is markup, but its behaviour (menu closes on a choice, the current
# section is named, the bar compacts once it sticks) is toc.js. A page that
# has the one without the other looks right until it is scrolled.
TOC_SCRIPT = re.compile(r"<script[^>]*src=\"[^\"]*toc\.js\"")


def check_toc_script():
    rule = "every page with a TOC bar loads toc.js"
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



# ── A Permalink needs copy.js ──
# anchors.js adds the Permalink control; copy.js does the copying, the tick and
# the spoken message. A page that loads the one without the other shows a
# Permalink that does nothing when pressed. index.html is checked too: it sits
# outside docs/ but carries section Permalinks.
ANCHORS_SCRIPT = re.compile(r"<script[^>]*src=\"[^\"]*anchors\.js\"")
COPY_SCRIPT = re.compile(r"<script[^>]*src=\"[^\"]*copy\.js\"")


def check_permalink_script():
    rule = "every page that loads anchors.js loads copy.js"
    n = 0
    paths = [REPO / "index.html"] + [p for p, _ in pages()]
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"<pre\b.*?</pre>", "", text, flags=re.S)
        if not ANCHORS_SCRIPT.search(text):
            continue
        n += 1
        if not COPY_SCRIPT.search(text):
            fail(rule, str(path.relative_to(REPO)), "loads anchors.js but not copy.js")
    if rule not in FAILS:
        ok(rule, f"{n} pages")

# ── The docs do not narrate their own history ──
# The system is new and in use nowhere, so a reader needs to know what a thing
# IS. "Previously", "we dropped", a decision date in the prose — all of it is
# a changelog in the wrong place. Decisions live in whiteboard/planning/; git is the log.
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
    # The rule documents in docs/ too: the policies and the style guide. (AGENTS.md
    # quotes the phrases in the rule that bans them.)
    for path in sorted((REPO / "docs").glob("*.md")):
        n += 1
        for m in HISTORY.finditer(path.read_text(encoding="utf-8", errors="replace")):
            fail(rule, str(path.relative_to(REPO)),
                 f'"{m.group(0)}" — the system is new; say what it is, not what it was')
    if rule not in FAILS:
        ok(rule, f"{n} pages and rule documents")


# ── Every class a builder can write is findable in the docs ──
# A class that exists and is documented nowhere is a class nobody uses, or
# worse, one somebody re-invents. The exemptions are classes the SCRIPTS own:
# a page author never writes them, so there is nothing for the docs to say.
CLASS_RE = re.compile(r"\.((?:ds-|btn-|type-|info-|seg-)[\w-]+)")
SCRIPT_OWNED = {
    "ds-theme-icon-system", "ds-theme-icon-light", "ds-theme-icon-dark",  # theme.js
    "ds-toc-sentinel",                              # toc.js
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


# ── Every class the docs name exists ──
# The other direction: a class a page or a rule document tells builders to
# write must be in a stylesheet or a shared script. A documented class that
# exists nowhere is written by a builder and does nothing.
def check_documented_classes_exist():
    rule = "every .ds- or .is- class the docs name exists"
    known = set()
    for f in list((REPO / "docs").glob("*.css")) + list((REPO / "templates").rglob("*.css")):
        known |= set(re.findall(r"\.((?:ds|is)-[\w-]+)", f.read_text(encoding="utf-8", errors="replace")))
    for f in list((REPO / "docs").glob("*.js")) + list((REPO / "templates").rglob("*.js")):
        known |= set(re.findall(r"\b((?:ds|is)-[\w-]+)", f.read_text(encoding="utf-8", errors="replace")))
    docs = [p for p in (REPO / "docs").rglob("*.html") if p.name != "doc.html"]
    docs += [REPO / "AGENTS.md"] + list((REPO / "docs").glob("*.md"))
    n = 0
    for path in docs:
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"(?<![\w-])\.((?:ds|is)-[a-z0-9-]*[a-z0-9])", text):
            n += 1
            if m.group(1) not in known:
                line = text[: m.start()].count("\n") + 1
                fail(rule, f"{path.relative_to(REPO)}:{line}", f".{m.group(1)} is in no stylesheet or script")
    if rule not in FAILS:
        ok(rule, f"{n} mentions")


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


# ── The generated files follow their pages ──
# The digests in docs/spec/ and the icons page are written by scripts. A page edited without
# running its script leaves the old file in place, and agents are told to read the digest first.
def check_generated_current():
    import subprocess
    for rule, script in (("the digests match their pages", "gen-digest.py"),
                         ("the icons page matches the icons", "gen-icons.py"),
                         ("the light and dark values in the docs match the stylesheets", "gen-theme-values.py")):
        r = subprocess.run([sys.executable, str(REPO / "verification" / script), "--check"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            said = next((l for l in r.stdout.splitlines() if l.startswith("FAIL")), "").replace("FAIL", "").strip()
            fail(rule, said.split("—")[0].strip() or "docs/", f"run: python3 verification/{script}")
        else:
            ok(rule, f"checked by {script}")


# ── One docs menu, on every page ──
# The shared nav is copied into each page by hand, so copies drift: pages
# went missing from it, a deleted page stayed in it, and one page carried an
# old order. Every copy must match buttons.html (ignoring which link is marked
# current), mark its own page current if it is listed, and every docs page
# must be listed except the ones kept out of the nav on purpose.
NAV_MENUS = re.compile(
    r'<header class="ds-site-header ds-site-header--light">.*?'
    r'<nav class="ds-site-header-nav" aria-label="Design system">'
    r'((?:\s*<details class="ds-site-header-dropdown">.*?</details>)+)',
    re.S,
)
OFF_NAV = {"doc.html", "outreach.html"}   # the doc viewer; the outreach rules page


def check_docs_menu():
    rule = "every docs page carries the same menu, and the menu lists every page"
    docs = REPO / "docs"
    ref = NAV_MENUS.search((docs / "buttons.html").read_text(encoding="utf-8"))
    canon = ref.group(1).replace(' aria-current="page"', "")
    listed = set(re.findall(r'href="([a-z0-9-]+\.html)"', canon))
    n = 0
    for path in sorted(docs.glob("*.html")):
        rel = str(path.relative_to(REPO))
        m = NAV_MENUS.search(path.read_text(encoding="utf-8", errors="replace"))
        if not m:
            fail(rule, rel, "no shared docs menu")
            continue
        n += 1
        if m.group(1).replace(' aria-current="page"', "") != canon:
            fail(rule, rel, "menu differs from the one on buttons.html")
        if path.name in listed and f'href="{path.name}" aria-current="page"' not in m.group(1):
            fail(rule, rel, "does not mark its own menu link aria-current")
        if path.name not in listed and path.name not in OFF_NAV:
            fail(rule, rel, "is not in the menu")
    if rule not in FAILS:
        ok(rule, f"{n} pages, {len(listed)} listed")


# ── Plain words ──
# STYLE.md lists words that agents keep reaching for and Shamsi keeps
# replacing. Checked in reader-facing prose only: code, class names, scripts
# and styles are stripped first. STYLE.md itself quotes them, so it is skipped.
PLAIN_WORDS = re.compile(r"\b(carr(?:y|ies|ied|ying)|rails?|walk(?:s|ed|ing)?|track(?:s|ed)?)\b", re.I)   # "tracking" allowed: surveillance, on brand.html


def check_plain_words():
    rule = "prose uses the plain word (STYLE.md: includes, sidebar, scan, type)"
    files = sorted((REPO / "docs").rglob("*.html")) + sorted((REPO / "docs").glob("*.md")) + [REPO / "AGENTS.md"]
    n = 0
    for path in files:
        if path.name == "STYLE.md" or "spec" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.suffix == ".html":
            text = re.sub(r"<(pre|script|style|code)\b.*?</\1>", " ", text, flags=re.S)
            text = re.sub(r"<[^>]+>", " ", text)
        else:
            text = re.sub(r"```.*?```", " ", text, flags=re.S)
            text = re.sub(r"`[^`]*`", " ", text)
        text = re.sub(r"[\w.-]*-track\b|track-[\w-]+", " ", text)
        n += 1
        for m in PLAIN_WORDS.finditer(text):
            start = max(0, m.start() - 40)
            context = " ".join(text[start:m.end() + 40].split())
            fail(rule, str(path.relative_to(REPO)), f"“{m.group(0)}” in: …{context}…")
    if rule not in FAILS:
        ok(rule, f"{n} files")


# ── American spelling ──
# STYLE.md, American spelling. Brand names keep theirs (Library Grey, so a
# capital G is allowed), and so does an author's text, such as the sample
# abstract on papers.html, which is copied as written.
BRITISH = re.compile(
    r"(?<![-\w./#])(colou?rs?\b(?<!colors\b)(?<!color\b)|colour\w*|centre\w*|centred|behaviour\w*|licence\w*"
    r"|labell(?:ed|ing)|neighbour\w*|recognis\w*|organis\w*|optimis\w*|analys(?:e|ed|ing)\b"
    r"|artefacts?|catalogue|programme|towards|grey\w*)(?![\w])")
AUTHOR_TEXT = ("We investigate the scalar sector",)


def check_american_spelling():
    rule = "American spelling (STYLE.md)"
    files = sorted((REPO / "docs").rglob("*.html")) + sorted((REPO / "docs").glob("*.md")) + [REPO / "AGENTS.md", REPO / "README.md"]
    n = 0
    for path in files:
        if "spec" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.suffix == ".html":
            text = re.sub(r"<(pre|script|style|code)\b.*?</\1>", " ", text, flags=re.S)
            text = re.sub(r"<p>(?:(?!</p>).)*?(?:" + "|".join(map(re.escape, AUTHOR_TEXT)) + r").*?</p>", " ", text, flags=re.S)
            text = re.sub(r"<[^>]+>", " ", text)
        else:
            text = re.sub(r"```.*?```", " ", text, flags=re.S)
            text = re.sub(r"`[^`]*`|\]\([^)]*\)", " ", text)
        n += 1
        for m in BRITISH.finditer(text):
            start = max(0, m.start() - 40)
            context = " ".join(text[start:m.end() + 30].split())
            fail(rule, str(path.relative_to(REPO)), f"“{m.group(0)}” in: …{context}…")
    if rule not in FAILS:
        ok(rule, f"{n} files")


def main():
    check_wordmark_not_typed()
    check_self_hosted()
    check_tokens_defined()
    check_no_text_arrows()
    check_colours_from_tokens()
    check_one_name_per_surface()
    check_relative_type_sizes()
    check_page_shape()
    check_theme_control()
    check_docs_menu()
    check_toc_script()
    check_permalink_script()
    check_no_changelog_prose()
    check_plain_words()
    check_american_spelling()
    check_classes_documented()
    check_documented_classes_exist()
    check_section_anchors()
    check_generated_current()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAIL")
        sys.exit(1)
    print("clean")


if __name__ == "__main__":
    main()
