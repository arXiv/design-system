#!/usr/bin/env python3
"""
Digests for agents — generated from the pattern pages, never written.

    python3 verification/gen-digest.py            # write docs/spec/*.md
    python3 verification/gen-digest.py --check    # fail if any digest is stale
    python3 verification/gen-digest.py --diagnose docs/alerts.html
                                                  # what a page lacks in the shape

A digest holds only what an agent needs to build with a component: the
classes and what each does, the parts a class requires, the markup to copy,
and the rules. It is generated only for pages on verification/reviewed-pages.txt:
a digest copies its page's contract faithfully, so a digest of a page that
has not had its review pass is wrong with the same confidence.

The shape it reads is buttons.html's (planning/DIGEST-PLAN.md has the table):
  page header            -> the page summary
  h2/h3.section-title    -> a component; its .ds-section-desc is the summary
  "Relevant code" .ds-acc -> <pre><code> is the markup, <dt>/<dd> the class key
  .ds-marginalia          -> a note on the component it sits in
  .ds-note--internal      -> the component's internal variant
  .ds-note--essential     -> rules
  .ds-alert in a section  -> a rule for that component
Everything else on the page is scaffolding and is left out.

The output is Markdown with a YAML header: the header is the contract as
data, the body is the prose and markup. That is the format a renderer can
later read back to produce the human page, so it is written as if it were
already the source.
"""

import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
SPEC = DOCS / "spec"
REVIEWED = REPO / "verification" / "reviewed-pages.txt"
VOID = {"meta", "link", "br", "hr", "img", "input", "path", "circle", "line", "polyline",
        "rect", "polygon", "ellipse", "source", "col", "wbr", "use"}


# ── A small DOM ─────────────────────────────────────────────────────────
class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs), parent, []

    @property
    def classes(self):
        return self.attrs.get("class", "").split()

    def has(self, cls):
        return cls in self.classes

    def walk(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.walk()

    def find_all(self, pred):
        return [n for n in self.walk() if pred(n)]

    def find(self, pred):
        for n in self.walk():
            if pred(n):
                return n
        return None

    def text(self):
        out = []
        for c in self.children:
            out.append(c.text() if isinstance(c, Node) else c)
        return "".join(out)

    def inner_html(self):
        return "".join(c.html() if isinstance(c, Node) else html.escape(c, quote=False) for c in self.children)

    def html(self):
        a = "".join(f' {k}="{html.escape(v, quote=True)}"' for k, v in self.attrs.items())
        if self.tag in VOID:
            return f"<{self.tag}{a}/>"
        return f"<{self.tag}{a}>{self.inner_html()}</{self.tag}>"

    def ancestor(self, pred):
        p = self.parent
        while p is not None:
            if pred(p):
                return p
            p = p.parent
        return None


class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse(path):
    b = Builder()
    b.feed(path.read_text(encoding="utf-8"))
    return b.root


# ── Text helpers ─────────────────────────────────────────────────────────
def md_inline(node):
    """Inline HTML to Markdown: code, emphasis, links; everything else is text."""
    out = []
    for c in node.children:
        if not isinstance(c, Node):
            out.append(c)
        elif c.tag == "code":
            out.append("`" + c.text() + "`")
        elif c.tag in ("strong", "b"):
            out.append("**" + md_inline(c) + "**")
        elif c.tag in ("em", "i"):
            out.append("*" + md_inline(c) + "*")
        elif c.tag == "a":
            href = c.attrs.get("href", "")
            out.append(f"[{md_inline(c)}]({href})" if href else md_inline(c))
        elif c.tag in ("svg", "button", "details", "summary"):
            continue
        else:
            out.append(md_inline(c))
    return squash("".join(out))


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def yaml_str(s):
    s = squash(s)
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


# ── Extraction ───────────────────────────────────────────────────────────
def section_title(node):
    return node.tag in ("h2", "h3") and node.has("section-title")


def extract(path):
    root = parse(path)
    warn = []
    page = {"page": path.name, "components": [], "rules": []}

    title = root.find(lambda n: n.tag == "h1")
    page["title"] = squash(title.text()) if title else path.stem
    header = root.find(lambda n: n.tag == "header" and n.has("ds-page-header"))
    if header:
        paras = [c for c in header.children if isinstance(c, Node) and c.tag == "p"]
        page["summary"] = " ".join(md_inline(p) for p in paras)
        for alert in header.find_all(lambda n: n.has("ds-alert")):
            t = alert.find(lambda n: n.has("ds-alert-title"))
            body = [p for p in alert.find_all(lambda n: n.tag == "p") if not p.has("ds-alert-title")]
            page["rules"].append((squash(t.text()) if t else "") + (": " if t else "") + " ".join(md_inline(p) for p in body))
    else:
        page["summary"] = ""
        warn.append("no .ds-page-header")
    if root.find(lambda n: n.tag == "style"):
        warn.append("page has a <style> block")

    group = None
    for h in root.find_all(section_title):
        section = h.ancestor(lambda n: n.tag == "section") or h.parent
        # a plain h2 before this h3 names its group
        if h.tag == "h3":
            prev = None
            for sib in section.parent.children:
                if sib is section:
                    break
                if isinstance(sib, Node) and sib.tag == "h2" and not sib.has("section-title"):
                    prev = squash(sib.text())
            group = prev or group
        else:
            group = None
        comp = {"id": h.attrs.get("id", ""), "title": squash(h.text()), "group": group,
                "summary": "", "classes": [], "markup": [], "notes": [], "rules": [], "internal": None}
        desc = section.find(lambda n: n.has("ds-section-desc"))
        if desc:
            comp["summary"] = md_inline(desc)
        else:
            warn.append(f"{comp['title']}: no .ds-section-desc")

        accs = [d for d in section.find_all(lambda n: n.tag == "details" and n.has("ds-acc"))]
        if not accs:
            warn.append(f"{comp['title']}: no Relevant code accordion")
        for acc in accs:
            in_internal = acc.ancestor(lambda n: n.has("ds-note--internal")) is not None
            target = comp
            if in_internal:
                comp["internal"] = comp["internal"] or {"summary": "", "classes": [], "markup": []}
                target = comp["internal"]
            label = None
            card = acc.parent
            # a panel label before the card names this example
            if card is not None and card.parent is not None:
                sibs = card.parent.children
                idx = sibs.index(card)
                for s in reversed(sibs[:idx]):
                    if isinstance(s, Node):
                        if s.has("ds-panel-label"):
                            label = squash(s.text())
                        break
            for pre in acc.find_all(lambda n: n.tag == "pre"):
                code = html.unescape(re.sub(r"</?span[^>]*>", "", pre.inner_html()))
                code = html.unescape(code) if "<code" not in code else html.unescape(re.sub(r"</?code[^>]*>", "", code))
                if "\n" not in code.strip() and len(code) > 90:
                    warn.append(f"{comp['title']}: a code block is a single line")
                target["markup"].append({"label": label, "code": code.strip("\n")})
            # a class table: first column the class, last column what it is for
            for table in acc.find_all(lambda n: n.tag == "table"):
                for tr in table.find_all(lambda n: n.tag == "tr"):
                    cells = [c for c in tr.children if isinstance(c, Node) and c.tag == "td"]
                    if len(cells) >= 2:
                        target["classes"].append({"name": squash(cells[0].text()), "does": md_inline(cells[-1])})
            dts = acc.find_all(lambda n: n.tag == "dt")
            for dt in dts:
                dd = None
                sibs = dt.parent.children
                for s in sibs[sibs.index(dt) + 1:]:
                    if isinstance(s, Node) and s.tag == "dd":
                        dd = s
                        break
                if dd is None:
                    continue
                if dd.find(lambda n: n.tag == "pre"):
                    continue
                name = squash(dt.text())
                if not re.match(r"^[.\[]|^[a-z-]+=|^--ds-|^<", name):
                    warn.append(f"{comp['title']}: key entry \"{name}\" is prose, not a class or attribute")
                target["classes"].append({"name": name, "does": md_inline(dd)})
            if not dts and not acc.find_all(lambda n: n.tag == "pre"):
                warn.append(f"{comp['title']}: an accordion with neither markup nor a class key")

        internal = section.find(lambda n: n.has("ds-note--internal"))
        if internal:
            comp["internal"] = comp["internal"] or {"summary": "", "classes": [], "markup": []}
            ps = [c for c in internal.children if isinstance(c, Node) and c.tag == "p"]
            comp["internal"]["summary"] = " ".join(md_inline(p) for p in ps)
        # an alert inside a section is a rule for that component
        for alert in section.find_all(lambda n: n.has("ds-alert") and not n.has("ds-alert-icon") and not n.has("ds-alert-content") and not n.has("ds-alert-title")):
            t = alert.find(lambda n: n.has("ds-alert-title"))
            body = [q for q in alert.find_all(lambda n: n.tag == "p") if not q.has("ds-alert-title")]
            comp["rules"].append(((squash(t.text()) + ": ") if t else "") + " ".join(md_inline(q) for q in body))
        for note in section.find_all(lambda n: n.has("ds-marginalia")):
            body = note.find(lambda n: n.has("ds-marginalia-body"))
            if body:
                comp["notes"].append(md_inline(body))
        page["components"].append(comp)

    for ess in root.find_all(lambda n: n.has("ds-note--essential")):
        for li in ess.find_all(lambda n: n.tag == "li"):
            page["rules"].append(md_inline(li))
        for g in ess.find_all(lambda n: n.has("ds-note-gotcha")):
            page["rules"].append("Easy to get wrong: " + md_inline(g).replace("**Easy to get wrong** ", ""))
    if not page["components"]:
        warn.append("no section titles")
    return page, warn


# ── Rendering ────────────────────────────────────────────────────────────
def render(page):
    y = ["---", f"page: {page['page']}", f"title: {yaml_str(page['title'])}", f"summary: {yaml_str(page['summary'])}",
         "stylesheet: design-system.css", "components:"]
    for c in page["components"]:
        y += [f"  - id: {c['id']}", f"    title: {yaml_str(c['title'])}"]
        if c["group"]:
            y.append(f"    group: {yaml_str(c['group'])}")
        y.append(f"    summary: {yaml_str(c['summary'])}")
        if c["classes"]:
            y.append("    classes:")
            for k in c["classes"]:
                y += [f"      - name: {yaml_str(k['name'])}", f"        does: {yaml_str(k['does'])}"]
        if c["internal"] and c["internal"]["classes"]:
            y.append("    internal:")
            for k in c["internal"]["classes"]:
                y += [f"      - name: {yaml_str(k['name'])}", f"        does: {yaml_str(k['does'])}"]
        if c["notes"]:
            y.append("    notes:")
            for n in c["notes"]:
                y.append(f"      - {yaml_str(n)}")
        if c["rules"]:
            y.append("    rules:")
            for r in c["rules"]:
                y.append(f"      - {yaml_str(r)}")
    if page["rules"]:
        y.append("rules:")
        for r in page["rules"]:
            y.append(f"  - {yaml_str(r)}")
    y.append("---")

    b = ["", f"# {page['title']}", "", page["summary"], ""]
    b += ["Load `design-system.css`; internal tools also load `internal/internal-tools.css` and put",
          "`class=\"ds-internal\"` on `<html>`. Every class below is in tier 1 unless it says otherwise.", ""]
    for c in page["components"]:
        b.append(f"## {c['title']}" + (f"  ({c['group']})" if c["group"] else ""))
        b += ["", c["summary"], ""]
        for m in c["markup"]:
            if m["label"]:
                b.append(f"**{m['label']}**")
                b.append("")
            b += ["```html", m["code"], "```", ""]
        if c["classes"]:
            for k in c["classes"]:
                b.append(f"- `{k['name']}` — {k['does']}")
            b.append("")
        if c["internal"]:
            b.append("**Internal variant.** " + c["internal"]["summary"])
            b.append("")
            for m in c["internal"]["markup"]:
                b += ["```html", m["code"], "```", ""]
            for k in c["internal"]["classes"]:
                b.append(f"- `{k['name']}` — {k['does']}")
            if c["internal"]["classes"]:
                b.append("")
        for n in c["notes"]:
            b += [f"> {n}", ""]
        for r in c["rules"]:
            b += [f"**Rule.** {r}", ""]
    if page["rules"]:
        b += ["## Rules", ""]
        for r in page["rules"]:
            b.append(f"- {r}")
        b.append("")
    return "\n".join(y) + "\n" + "\n".join(b)


def render_index(pages, unreviewed):
    out = ["# arXiv design system — digests for agents", "",
           "One file per pattern page, generated from the page by `verification/gen-digest.py`.",
           "Each holds the classes, what they do and require, the markup to copy, and the rules.",
           "Nothing else. A digest exists only for a page that has had its review pass.", "",
           "| Component | Digest | Summary |", "|---|---|---|"]
    for p in pages:
        out.append(f"| {p['title']} | [{p['page'].replace('.html', '.md')}]({p['page'].replace('.html', '.md')}) | {p['summary'][:160]} |")
    if unreviewed:
        out += ["", "## Not yet digested", "",
                "These pages have not had their review pass. Read the page itself, and expect the shape to differ.", ""]
        for u in unreviewed:
            out.append(f"- {u}")
    return "\n".join(out) + "\n"


# ── Main ────────────────────────────────────────────────────────────────
def reviewed():
    if not REVIEWED.exists():
        return []
    return [l.strip() for l in REVIEWED.read_text().splitlines() if l.strip() and not l.startswith("#")]


def all_pages():
    skip = {"doc.html", "icons.html", "using.html", "index.html"}
    return sorted(p.relative_to(DOCS).as_posix() for p in DOCS.rglob("*.html") if p.name not in skip and "sharing" not in p.parts)


def main():
    if "--diagnose" in sys.argv:
        for arg in sys.argv[sys.argv.index("--diagnose") + 1:]:
            page, warn = extract(REPO / arg)
            print(f"{arg}: {len(page['components'])} components, {sum(len(c['classes']) for c in page['components'])} classes, {len(page['rules'])} rules")
            for w in warn:
                print("  WARN", w)
        return 0
    check = "--check" in sys.argv
    outputs = {}
    pages = []
    for rel in reviewed():
        page, warn = extract(DOCS / rel)
        pages.append(page)
        outputs[SPEC / (Path(rel).with_suffix(".md").as_posix())] = render(page)
        for w in warn:
            print(f"WARN  {rel}: {w}")
    unreviewed = [p for p in all_pages() if p not in reviewed()]
    outputs[SPEC / "index.md"] = render_index(pages, unreviewed)
    stale = [p for p, text in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    if check:
        if stale:
            print("FAIL  digests stale: " + ", ".join(str(p.relative_to(REPO)) for p in stale) + " — run: python3 verification/gen-digest.py")
            return 1
        print(f"PASS  {len(pages)} digest(s) match their pages")
        return 0
    SPEC.mkdir(exist_ok=True)
    for p, text in outputs.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    print(f"{len(pages)} digest(s) written, {len(stale)} changed; {len(unreviewed)} pages not yet reviewed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
