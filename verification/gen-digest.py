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

The shape it reads is buttons.html's (whiteboard/planning/DIGEST-PLAN.md has the table):
  page header            -> the page summary
  h2/h3 opening a plain <section> -> a component; its .ds-section-desc paragraphs are the summary
  "Relevant code" .ds-acc -> <pre><code> is the markup, <dt>/<dd> the class key; each key stays
                             with the markup of its own accordion
  <pre> in the section itself -> markup too (the page skeleton on using.html)
  <table> in the section itself, or a .token-table anywhere -> a table
  .ds-marginalia          -> a note on the component it sits in
  .ds-note in the section -> guidance, under the note's label
  .ds-note--internal      -> the component's internal variant
  .ds-note--essential     -> rules, under the note's label
  sections under a plain "Rules" h2 -> rules, each under its own heading, with its paragraphs,
                             lists and tables; under "Spec" -> the spec, the same way, code included
An alert is never a rule: on these pages every alert is a demo, and a requirement is a note.
A demo is not the contract. What sits in a demo (a .ds-card, a .page-demo or a <dialog>) is left
out: a sample alert, a sample note, a sample table. So is everything else on the page.
A section inside a section has its own entry and is not repeated in its parent's.
--check also fails when a page's code blocks and its digest's do not match in number, so a
code block the generator cannot place is never dropped without a word.

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
def md_inline(node, skip=()):
    """Inline HTML to Markdown: code, emphasis, links; everything else is text."""
    out = []
    for c in node.children:
        if not isinstance(c, Node):
            out.append(c)
        elif c.tag in skip:
            continue
        elif c.tag == "br":
            out.append(" ")
        elif c.tag == "code":
            out.append("`" + c.text() + "`")
        elif c.tag in ("strong", "b"):
            out.append("**" + md_inline(c) + "**")
        elif c.tag in ("em", "i"):
            out.append("*" + md_inline(c) + "*")
        elif c.tag == "a":
            href = c.attrs.get("href", "")
            out.append(f"[{md_inline(c)}]({digest_href(href)})" if href else md_inline(c))
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
def digest_href(href):
    # The pages link relative to docs/; a digest lives in docs/spec/. A link to a
    # page that has a digest goes to the digest, any other link inside docs/ goes
    # up a level, and links off the site or within the page are left alone.
    if re.match(r"^(?:[a-z]+:|#|/)", href):
        return href
    m = re.match(r"^([a-z0-9-]+)\.html(#.*)?$", href)
    if m and f"{m.group(1)}.html" in reviewed():
        return f"{m.group(1)}.md{m.group(2) or ''}"
    return "../" + href


def section_title(node):
    # A section heading is the h2 or h3 that opens a plain <section>; component
    # sections (a data card) always have a class, so they never match.
    parent = node.parent
    if node.tag not in ("h2", "h3") or parent is None or parent.tag != "section" or parent.attrs.get("class"):
        return False
    # a section inside a demo (a demo card or a whole-page demo) is part of the demo, not a component
    if parent.ancestor(lambda n: n.has("ds-card") or n.has("page-demo")) is not None:
        return False
    first = next((c for c in parent.children if isinstance(c, Node)), None)
    return first is node


def titled(n):
    """A plain <section> opened by its own h2 or h3: it has an entry of its own."""
    return (isinstance(n, Node) and n.tag == "section" and not n.attrs.get("class")
            and any(section_title(c) for c in n.children if isinstance(c, Node)))


def own(section, pred):
    """The section's own nodes that match, in page order. A titled section inside it is not
    entered: on papers.html three sections sit inside another, and each was digested twice."""
    out = []

    def visit(node):
        for c in node.children:
            if not isinstance(c, Node) or titled(c):
                continue
            if pred(c):
                out.append(c)
            visit(c)
    visit(section)
    return out


def within(n, section, pred):
    """The nearest ancestor of n, below its section, that matches."""
    p = n.parent
    while p is not None and p is not section:
        if pred(p):
            return p
        p = p.parent
    return None


def in_demo(n, section):
    """In a demo: a card, a whole-page demo or a dialog. What a demo shows is sample content."""
    return within(n, section, lambda p: p.has("ds-card") or p.has("page-demo") or p.tag == "dialog") is not None


def is_alert(n):
    return n.has("ds-alert") and not (n.has("ds-alert-icon") or n.has("ds-alert-content") or n.has("ds-alert-title"))


def is_guidance(n):
    return n.has("ds-note") and not (n.has("ds-note--essential") or n.has("ds-note--internal"))


def alert_text(alert):
    t = alert.find(lambda n: n.has("ds-alert-title"))
    body = [q for q in alert.find_all(lambda n: n.tag == "p") if not q.has("ds-alert-title")]
    return ((squash(t.text()) + ": ") if t else "") + " ".join(md_inline(q) for q in body)


def md_item(li):
    """A list item, and the items of a list inside it, each once."""
    kids = [md_inline(k) for sub in li.children if isinstance(sub, Node) and sub.tag in ("ul", "ol")
            for k in sub.children if isinstance(k, Node) and k.tag == "li"]
    return {"text": md_inline(li, skip=("ul", "ol")), "kids": kids}


def reference_table(table, section):
    """A table a builder reads: one that stands in the section, or a docs token table. A table in
    a demo is a sample, and a table with no rows is filled in by the page's script."""
    if within(table, section, lambda p: p.tag == "details") is not None:
        return False
    if len(table.find_all(lambda n: n.tag == "tr")) < 2:
        return False
    return table.has("token-table") or not in_demo(table, section)


def md_table(table):
    rows = []
    for tr in table.find_all(lambda n: n.tag == "tr"):
        cells = [c for c in tr.children if isinstance(c, Node) and c.tag in ("th", "td")]
        if cells:
            rows.append([md_inline(c).replace("|", "\\|") for c in cells])
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
    return "\n".join(out)


def blocks(node, section):
    """The paragraphs, list items and tables of a rules section or a note, in page order."""
    out = []
    for n in own(node, lambda n: n.tag in ("p", "li", "table", "pre")):
        if n.has("ds-marginalia-body"):
            out.append(("p", md_inline(n)))   # a margin note says something about the rule, wherever it sits
            continue
        if n.tag == "pre":
            acc = within(n, node, lambda p: p.tag == "details")
            relevant = acc is not None and acc.find(lambda m: m.tag == "summary") is not None and \
                squash(acc.find(lambda m: m.tag == "summary").text()).lower().startswith("relevant")
            if relevant or (acc is None and not in_demo(n, section)):
                raw = re.sub(r"</?span[^>]*>", "", n.inner_html())
                out.append(("pre", html.unescape(re.sub(r"^\s*<code[^>]*>|</code>\s*$", "", raw)).strip("\n")))
            continue
        if in_demo(n, section) and not (n.tag == "table" and n.has("token-table")):
            continue
        if within(n, node, lambda p: p.tag in ("li", "table", "details") or p.has("ds-marginalia")) is not None:
            continue
        if n.tag == "p" and not n.has("ds-note-label"):
            out.append(("p", md_inline(n)))
        elif n.tag == "li":
            out.append(("li", md_item(n)))
        elif n.tag == "table" and reference_table(n, section):
            out.append(("table", md_table(n)))
    return out


def flat(bl):
    """Blocks as plain strings, for the header's list of rules."""
    out = []
    for kind, v in bl:
        if kind == "p":
            out.append(v)
        elif kind == "li":
            out.append(v["text"])
            out.extend(v["kids"])
    return out


def extract(path):
    root = parse(path)
    warn = []
    page = {"page": path.name, "components": [], "rules": [], "rule_groups": [], "spec_groups": []}

    title = root.find(lambda n: n.tag == "h1")
    page["title"] = squash(title.text()) if title else path.stem
    header = root.find(lambda n: n.tag == "header" and n.has("ds-page-header"))
    if header:
        paras = [c for c in header.children if isinstance(c, Node) and c.tag == "p"]
        page["summary"] = " ".join(md_inline(p) for p in paras)
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
                if isinstance(sib, Node) and sib.tag == "h2" and not section_title(sib):
                    prev = squash(sib.text())
            group = prev or group
        else:
            group = None
        if group and re.search(r"rule|spec", group, re.I):
            bl = blocks(section, section)
            if bl:
                key = "spec_groups" if re.search(r"spec", group, re.I) or re.search(r"token|spec", h.text(), re.I) else "rule_groups"
                page[key].append({"title": squash(h.text()), "blocks": bl})
            continue
        comp = {"id": h.attrs.get("id", ""), "title": squash(h.text()), "group": group,
                "summary": "", "more": [], "classes": [], "markup": [], "examples": [], "tables": [],
                "guidance": [], "notes": [], "rules": [], "internal": None}
        descs = own(section, lambda n: n.has("ds-section-desc"))
        if descs:
            comp["summary"] = md_inline(descs[0])
            # the further paragraphs that stand in the section itself say more about the same component
            comp["more"] = [md_inline(d) for d in descs[1:] if d.parent is section]
        else:
            warn.append(f"{comp['title']}: no .ds-section-desc")

        def relevant(d):
            # only the reference accordions: a page that documents the accordion itself has demo ones too
            summary = d.find(lambda n: n.tag == "summary")
            return (d.tag == "details" and d.has("ds-acc") and summary is not None
                    and squash(summary.text()).lower().startswith("relevant"))

        def loose_pre(n):
            # markup that stands in the section itself, outside any accordion or demo
            return (n.tag == "pre" and within(n, section, lambda p: p.tag == "details") is None
                    and not in_demo(n, section))

        def code_of(pre):
            # The block's text as a reader sees it: the <code> wrapper and any
            # highlighting spans go, and what the page escapes stays escaped.
            raw = re.sub(r"</?span[^>]*>", "", pre.inner_html())
            return html.unescape(re.sub(r"^\s*<code[^>]*>|</code>\s*$", "", raw)).strip("\n")

        sources = own(section, lambda n: relevant(n) or loose_pre(n))
        if not sources:
            warn.append(f"{comp['title']}: no Relevant code accordion")
        for acc in sources:
            if acc.tag == "pre":
                comp["markup"].append({"label": None, "code": code_of(acc)})
                comp["examples"].append({"label": None, "codes": [code_of(acc)], "classes": [], "internal": False})
                continue
            in_internal = acc.ancestor(lambda n: n.has("ds-note--internal")) is not None
            target = comp
            if in_internal:
                comp["internal"] = comp["internal"] or {"summary": "", "classes": [], "markup": []}
                target = comp["internal"]
            example = {"label": None, "codes": [], "classes": [], "internal": in_internal}
            comp["examples"].append(example)
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
            example["label"] = label
            for pre in acc.find_all(lambda n: n.tag == "pre"):
                code = code_of(pre)
                if "\n" not in code.strip() and len(code) > 90:
                    warn.append(f"{comp['title']}: a code block is a single line")
                target["markup"].append({"label": label, "code": code})
                example["codes"].append(code)
            # a class table: first column the class, last column what it is for
            for table in acc.find_all(lambda n: n.tag == "table"):
                for tr in table.find_all(lambda n: n.tag == "tr"):
                    cells = [c for c in tr.children if isinstance(c, Node) and c.tag == "td"]
                    if len(cells) >= 2:
                        key = {"name": squash(cells[0].text()), "does": md_inline(cells[-1])}
                        target["classes"].append(key)
                        example["classes"].append(key)
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
                key = {"name": name, "does": md_inline(dd)}
                target["classes"].append(key)
                example["classes"].append(key)
            if not dts and not acc.find_all(lambda n: n.tag == "pre"):
                warn.append(f"{comp['title']}: an accordion with neither markup nor a class key")

        internal = next((n for n in own(section, lambda n: n.has("ds-note--internal")) if not in_demo(n, section)), None)
        if internal:
            comp["internal"] = comp["internal"] or {"summary": "", "classes": [], "markup": []}
            ps = [c for c in internal.children if isinstance(c, Node) and c.tag == "p"]
            comp["internal"]["summary"] = " ".join(md_inline(p) for p in ps)
        # a table that stands in the section, outside a note, is part of the contract
        for table in own(section, lambda n: n.tag == "table"):
            if reference_table(table, section) and within(table, section, is_guidance) is None:
                comp["tables"].append(md_table(table))
        # a grey note in the section is guidance: how to word something, when to choose one thing over another
        for note in own(section, is_guidance):
            if in_demo(note, section):
                continue
            label = note.find(lambda n: n.has("ds-note-label"))
            bl = blocks(note, section)
            if bl:
                comp["guidance"].append({"label": squash(label.text()) if label else "", "blocks": bl})
        for note in own(section, lambda n: n.has("ds-marginalia")):
            body = note.find(lambda n: n.has("ds-marginalia-body"))
            if body:
                comp["notes"].append(md_inline(body))
        # a list straight under the section, outside any demo, card or note, is its guidance:
        # a .notes list holds the section's rules (the arrangement rules on organize-content.html),
        # any other list is a note (where a pattern is used, the parts it is made of)
        for lst in [c for c in section.children if isinstance(c, Node) and c.tag in ("ul", "ol")]:
            items = [md_inline(li) for li in lst.children if isinstance(li, Node) and li.tag == "li"]
            if lst.has("notes"):
                comp["rules"].extend(items)
            elif items:
                comp["notes"].append("; ".join(items))
        # a titled card holding a list (the questions on organize-content.html) is guidance for this section
        for card in own(section, lambda n: n.has("ds-card")):
            ct = next((c for c in card.children if isinstance(c, Node) and c.tag == "h3"), None)
            ul = next((c for c in card.children if isinstance(c, Node) and c.tag == "ul"), None)
            if ct is None or ul is None:
                continue
            first = next((c for c in card.children if isinstance(c, Node) and c.tag == "p"), None)
            items = "; ".join(md_inline(li) for li in ul.find_all(lambda n: n.tag == "li"))
            comp["notes"].append(squash(ct.text()) + (" (" + md_inline(first).rstrip(".") + ")" if first else "") + ": " + items)
        page["components"].append(comp)

    # a section with no heading under a plain "Rules" h2 still holds rules
    for sec in root.find_all(lambda n: n.tag == "section" and not n.classes):
        if any(section_title(c) for c in sec.children if isinstance(c, Node)):
            continue
        prev = None
        for sib in sec.parent.children:
            if sib is sec:
                break
            if isinstance(sib, Node) and sib.tag == "h2" and not section_title(sib):
                prev = squash(sib.text())
        if prev and re.search(r"rule", prev, re.I):
            bl = blocks(sec, sec)
            if bl:
                page["rule_groups"].append({"title": "", "blocks": bl})

    for ess in root.find_all(lambda n: n.has("ds-note--essential")):
        label = ess.find(lambda n: n.has("ds-note-label"))
        bl = [("li", md_item(li)) for li in ess.find_all(lambda n: n.tag == "li")
              if li.ancestor(lambda n: n.tag == "li") is None]
        for g in ess.find_all(lambda n: n.has("ds-note-gotcha")):
            bl.append(("li", {"text": "Easy to get wrong: " + md_inline(g).replace("**Easy to get wrong** ", ""), "kids": []}))
        if bl:
            page["rule_groups"].append({"title": squash(label.text()) if label else "Essentials", "blocks": bl})
    if not page["components"]:
        warn.append("no section titles")
    return page, warn


# ── Rendering ────────────────────────────────────────────────────────────
def render_blocks(bl):
    """Paragraphs, bullets and tables, in the order the page has them."""
    out = []
    for i, (kind, v) in enumerate(bl):
        if kind == "li":
            out.append(f"- {v['text']}")
            out += [f"  - {k}" for k in v["kids"]]
            if i + 1 == len(bl) or bl[i + 1][0] != "li":
                out.append("")
        elif kind == "pre":
            out += ["```", v, "```", ""]
        else:
            out += [v, ""]
    return out


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
    rules = page["rules"] + [r for g in page["rule_groups"] for r in flat(g["blocks"])]
    if rules:
        y.append("rules:")
        for r in rules:
            y.append(f"  - {yaml_str(r)}")
    y.append("---")

    b = ["", f"# {page['title']}", "", page["summary"], ""]
    b += ["Load `design-system.css`; internal tools also load `internal-tools.css` and put",
          "`class=\"ds-internal\"` on `<html>`. Every class below is in tier 1 unless it says otherwise.", ""]
    for c in page["components"]:
        b.append(f"## {c['title']}" + (f"  ({c['group']})" if c["group"] else ""))
        b += ["", c["summary"], ""]
        for more in c["more"]:
            b += [more, ""]

        def example(e):
            # each example keeps its own key: the same class can mean something else in the next one
            out = []
            if e["label"]:
                out += [f"**{e['label']}**", ""]
            for code in e["codes"]:
                out += ["```html", code, "```", ""]
            if e["classes"]:
                out += [f"- `{k['name']}` — {k['does']}" for k in e["classes"]] + [""]
            return out

        for e in c["examples"]:
            if not e["internal"]:
                b += example(e)
        for t in c["tables"]:
            b += [t, ""]
        if c["internal"]:
            b.append("**Internal variant.** " + c["internal"]["summary"])
            b.append("")
            for e in c["examples"]:
                if e["internal"]:
                    b += example(e)
        for g in c["guidance"]:
            if g["label"]:
                b += [f"**{g['label']}**", ""]
            b += render_blocks(g["blocks"])
        for n in c["notes"]:
            b += [f"> {n}", ""]
        for r in c["rules"]:
            b += [f"**Rule.** {r}", ""]
    if page["rules"] or page["rule_groups"]:
        b += ["## Rules", ""]
        if page["rules"]:
            b += [f"- {r}" for r in page["rules"]] + [""]
        for g in page["rule_groups"]:
            if g["title"]:
                b += [f"### {g['title']}", ""]
            b += render_blocks(g["blocks"])
    if page["spec_groups"]:
        b += ["## Spec", ""]
        for g in page["spec_groups"]:
            b += [f"### {g['title']}", ""]
            b += render_blocks(g["blocks"])
    while b and b[-1] == "":
        b.pop()
    return "\n".join(y) + "\n" + "\n".join(b) + "\n"


def render_index(pages, unreviewed):
    out = ["# arXiv design system — digests for agents", "",
           "One file per pattern page, generated from the page by `verification/gen-digest.py`.",
           "Each holds the classes, what they do and require, the markup to copy, and the rules.",
           "Nothing else. A digest exists only for a page that has had its review pass.", "",
           "| Component | Digest |", "|---|---|"]
    for p in pages:
        out.append(f"| {p['title']} | [{p['page'].replace('.html', '.md')}]({p['page'].replace('.html', '.md')}) |")
    if unreviewed:
        out += ["", "## Not yet digested", "",
                "These pages have not had their review pass. Read the page itself, and expect the shape to differ.", ""]
        for u in unreviewed:
            out.append(f"- {u}")
    return "\n".join(out) + "\n"


def code_counts(path, text):
    """How many code blocks the page shows a builder, and how many the digest carries. A block
    in a demo is a sample, unless it is the demo's Relevant code."""
    root = parse(path)
    def counted(pre):
        if pre.ancestor(lambda n: n.tag == "details" and n.has("ds-acc")
                        and n.find(lambda m: m.tag == "summary") is not None
                        and squash(n.find(lambda m: m.tag == "summary").text()).lower().startswith("relevant")) is not None:
            return True
        return pre.ancestor(lambda n: n.has("ds-card") or n.has("page-demo") or n.tag == "dialog") is None
    titled_sections = [h.parent for h in root.find_all(section_title)]
    shown = sum(1 for pre in root.find_all(lambda n: n.tag == "pre")
                if counted(pre) and pre.ancestor(lambda n: any(n is t for t in titled_sections)) is not None)
    body = text.split("\n---\n", 1)[1] if "\n---\n" in text else text
    carried = len(re.findall(r"^```", body, flags=re.M)) // 2
    return shown, carried


# ── Main ────────────────────────────────────────────────────────────────
def reviewed():
    if not REVIEWED.exists():
        return []
    return [l.strip() for l in REVIEWED.read_text().splitlines() if l.strip() and not l.startswith("#")]


def all_pages():
    skip = {"doc.html", "icons.html", "using.html", "index.html"}   # the viewer, a generated page, and pages with a digest of their own or none to make
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
    short = []
    for rel in reviewed():
        shown, carried = code_counts(DOCS / rel, outputs[SPEC / Path(rel).with_suffix(".md").as_posix()])
        if shown != carried:
            short.append(f"{rel}: {shown} code blocks on the page, {carried} in the digest")
    for line in short:
        print("FAIL  " + line)
    if check:
        if short:
            return 1
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
    return 1 if short else 0


if __name__ == "__main__":
    sys.exit(main())
