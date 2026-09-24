#!/usr/bin/env python3
"""Generate every target of the brand templates from their one source, the Python
package's arxiv_brand/{head,header,footer}.html and schema.json (README.md, Template
rules): the TemplateToolkit, React (+ .d.ts) and vendored HTML adapters and the root
package.json. verification/check-generated.py checks they are current, and
tests/integration/test_targets.py that each renders what Jinja renders. Stdlib only:

    python3 templates/generate.py
"""
import html
import json
import re
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent
PACKAGE = TEMPLATES / "arxiv_brand"
REPO = TEMPLATES.parent
SECTIONS = ("head", "header", "footer")   # every template; checks and tests read this list
VARS = json.loads((PACKAGE / "schema.json").read_text(encoding="utf-8"))["vars"]

VAR_RE = re.compile(r"\{\{\s*(\w+)\s*\}\}")
# Jinja's: `{#-` and `-#}` also remove the whitespace before and after the comment.
COMMENT_RE = re.compile(r"(\s*)\{#(-?).*?(-?)#\}(\s*)", re.S)
# A section's start or end, or a tag (its attributes double-quoted).
TOKEN_RE = re.compile(r"""
    \{%\s*if\s+(?P<neg>not\s+)?(?P<flag>\w+)\s*%\} | (?P<endif>\{%\s*endif\s*%\})
  | <(?P<close>/)?(?P<name>[A-Za-z][A-Za-z0-9-]*)
    (?P<attrs>(?:\s+[^\s"'=<>/{}]+(?:="[^"]*")?)*)\s*(?P<self>/)?>""", re.X)
ATTR_RE = re.compile(r'(\s+)([^\s"\'=<>/{}]+)(?:="([^"]*)")?')
VOID = frozenset("area base br col embed hr img input link meta source track wbr".split())
RULES = ("outside the template rules (README.md): only {{ variable }} and {% if [not] flag %} "
         "sections around whole elements, attributes double-quoted, no HTML comments")


def uncomment(text: str) -> str:
    return COMMENT_RE.sub(lambda m: ("" if m[2] else m[1]) + ("" if m[3] else m[4]), text)


def parse(src: str, label: str) -> list[tuple]:
    """The source as tokens: ("text", s), ("start", name, attrs, closed, s), ("end", name, s),
    ("if", flag, negated) and ("endif",), where s is the source text and attrs
    [(whitespace, name, value or None)]. Markup JSX cannot mirror fails, with its line."""
    def fail(at: int, rule: str):
        raise ValueError(f"{label}.html line {src.count(chr(10), 0, at) + 1}: {rule}")

    def check(text: str, at: int, attr: bool = False) -> str:
        rest = VAR_RE.sub("", text)
        if re.search(r"\{[{%#]|[}%#]\}|\[%|%\]", rest) or ("<" in rest and not attr):
            fail(at, RULES)
        return text

    tokens, stack, pos = [], [], 0   # stack: the open elements and sections ("{%"), with offsets
    for m in TOKEN_RE.finditer(src):
        if m.start() > pos:
            tokens.append(("text", check(src[pos:m.start()], pos)))
        pos, at = m.end(), m.start()
        if m["flag"]:
            stack.append(("{%", at))
            tokens.append(("if", m["flag"], bool(m["neg"])))
            continue
        if m["endif"]:
            if not stack or stack.pop()[0] != "{%":
                fail(at, "{% endif %} closes an element: a section wraps whole elements")
            tokens.append(("endif",))
            continue
        name = m["name"].lower() if m["name"].lower() in VOID else m["name"]
        if name in ("pre", "textarea"):
            fail(at, f"<{name}> keeps whitespace, which JSX drops")
        if m["close"]:
            if not stack or stack.pop()[0] != name:
                fail(at, f"</{name}> must close the element opened last, in the same section")
            tokens.append(("end", name, m[0]))
            continue
        attrs = [(a[1], a[2], a[3]) for a in ATTR_RE.finditer(m["attrs"])]
        for _, _, value in attrs:
            check(value or "", at, attr=True)
        names = {a for _, a, _ in attrs}
        if m["self"] and name not in VOID and not any(s[0] == "svg" for s in stack):
            fail(at, f"<{name}/> does not close itself in HTML")
        if name == "script" and (names - {"src", "defer", "async"} or "src" not in names
                                 or not src.startswith("</script>", pos)):
            fail(at, 'a script is a static loader: <script src="…" [defer|async]></script>')
        closed = name in VOID or bool(m["self"])
        if not closed:
            stack.append((name, at))
        tokens.append(("start", name, attrs, closed, m[0]))
    if pos < len(src):
        tokens.append(("text", check(src[pos:], pos)))
    if stack:
        fail(stack[-1][1], "never closed")
    return tokens


def template(section: str, src: str | None = None) -> tuple[list, dict]:
    """A template's tokens and the schema entries it uses, checked; `src` (comment-free)
    stands in for the file."""
    if src is None:
        src = uncomment((PACKAGE / f"{section}.html").read_text(encoding="utf-8"))
    tokens = parse(src.strip(), section)
    flags, printed = {t[1] for t in tokens if t[0] == "if"}, set(VAR_RE.findall(src))
    unknown = sorted((flags | printed) - VARS.keys())
    if unknown:
        raise KeyError(f"{section}.html uses {unknown}, which schema.json does not declare")
    vars_ = {n: m for n, m in VARS.items() if n in flags | printed}
    for n, m in vars_.items():
        if m["type"] not in ("attr", "url", "html", "bool"):
            raise ValueError(f"schema.json {n!r}: the type is attr, url, html or bool")
        if (m["type"] == "bool") != (n in flags) or (n in flags and n in printed):
            raise ValueError(f"{section}.html '{n}': only a bool gates a section, and it is never printed")
        if m["type"] == "bool" and m["default"] is not False:
            raise ValueError(f"bool '{n}' must default to false (undefined = default everywhere)")
    return tokens, vars_


# ---- stdlib renderer (the vendored target) and TemplateToolkit -------------

def escape(value: str) -> str:
    """Jinja's escaping (MarkupSafe's), so render() matches Jinja exactly."""
    return (value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&#34;").replace("'", "&#39;"))


def render(tokens: list, vars_: dict, context: dict) -> str:
    """Render without a Jinja engine; escaping follows each variable's type."""
    def value(m: re.Match) -> str:
        v = context.get(m[1], vars_[m[1]]["default"])
        return v if vars_[m[1]]["type"] == "html" else escape(str(v))

    out, shown = [], []
    for t in tokens:
        if t[0] == "if":
            shown.append(bool(context.get(t[1], False)) != t[2])
        elif t[0] == "endif":
            shown.pop()
        elif all(shown):
            out.append(VAR_RE.sub(value, t[-1]))
    return "".join(out)


def to_templatetoolkit(tokens: list, vars_: dict) -> str:
    # The schema defaults, keeping a host's explicit value ("" included): TT's DEFAULT would
    # replace "", and the postfix `x = v UNLESS …` blanks a defined x. Undef is false for bools.
    def quote(v: str) -> str:
        return "'" + v.replace("\\", "\\\\").replace("'", "\\'") + "'"

    def value(m: re.Match) -> str:
        return f"[% {m[1]} %]" if vars_[m[1]]["type"] == "html" else f"[% {m[1]} | html %]"

    prelude = "".join(f"[% UNLESS {n}.defined; {n} = {quote(str(m['default']))}; END %]\n"
                      for n, m in vars_.items() if m["type"] != "bool" and m["default"])
    return prelude + "".join(
        f"[% {'UNLESS' if t[2] else 'IF'} {t[1]} %]" if t[0] == "if" else "[% END %]" if t[0] == "endif"
        else VAR_RE.sub(value, t[-1]) for t in tokens) + "\n"


# ---- React / JSX ----------------------------------------------------------

# HTML attributes React spells differently; beyond these, a hyphenated or namespaced name
# (stroke-width, xlink:href) is camelCased, except data-* and aria-*.
REACT_ATTRS = {a.lower(): a for a in (
    "accessKey allowFullScreen autoCapitalize autoComplete autoFocus autoPlay charSet colSpan "
    "contentEditable crossOrigin dateTime encType enterKeyHint fetchPriority formAction "
    "formNoValidate hrefLang inputMode maxLength minLength noModule noValidate playsInline "
    "readOnly referrerPolicy rowSpan spellCheck srcSet tabIndex useMap").split()}
REACT_ATTRS.update({"class": "className", "for": "htmlFor"})
# Written bare, these are true; any other bare attribute is "" (crossorigin), a string to React.
REACT_BOOLEAN = frozenset(
    "allowFullScreen async autoFocus autoPlay controls defaultChecked defer disabled "
    "formNoValidate hidden inert loop multiple muted noModule noValidate open playsInline "
    "readOnly required reversed selected".split())
FIXED_VALUE = ("hidden", "submit", "reset", "button", "image", "checkbox", "radio")  # input types
NO_TEXT = frozenset("table thead tbody tfoot tr colgroup".split())   # React warns on text here


def _expr(value: str) -> str:
    """An attribute value as a JavaScript expression: `x`, or a template literal (with the
    entities HTML would have decoded)."""
    exact = VAR_RE.fullmatch(value)
    if exact:
        return exact[1]
    parts = VAR_RE.split(value)
    for i in range(0, len(parts), 2):
        parts[i] = html.unescape(parts[i]).replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
    for i in range(1, len(parts), 2):
        parts[i] = "${" + parts[i] + "}"
    return "`" + "".join(parts) + "`"


def _jsx_attr(tag: str, attrs: list, name: str, value) -> str:
    jsx = name if name.startswith(("data-", "aria-")) else \
        REACT_ATTRS.get(name.lower()) or re.sub(r"[-:](.)", lambda m: m[1].upper(), name)
    if tag == "input" and name == "checked":
        jsx = "defaultChecked"
    if tag == "input" and name == "value" and {a: v for _, a, v in attrs}.get("type") not in FIXED_VALUE:
        jsx = "defaultValue"   # a value alone makes React treat the field as controlled
    if value is None:
        return jsx if jsx in REACT_BOOLEAN else f'{jsx}=""'
    return f"{jsx}={{{_expr(value)}}}" if "{{" in value else f'{jsx}="{value}"'


def _jsx_text(text: str, vars_: dict, parent) -> str:
    """Text as JSX children that mean what the HTML means: JSX drops a whitespace run holding
    a line break, which HTML shows as a space, so each becomes {" "} (the break stays, for
    layout). An html slot goes in a <span> (README.md, Template rules)."""
    if (parent is None or parent in NO_TEXT) and not text.strip():   # between top-level elements
        return text if "\n" in text else ""
    parts = VAR_RE.split(text)
    for i in range(0, len(parts), 2):
        s = parts[i].replace("{", "&#123;").replace("}", "&#125;").replace(">", "&gt;")
        parts[i] = re.sub(r"\s*\n\s*", lambda w: '{" "}' + w[0], s)
    for i in range(1, len(parts), 2):
        n = parts[i]
        parts[i] = f"<span dangerouslySetInnerHTML={{{{ __html: {n} }}}} />" \
            if vars_[n]["type"] == "html" else f"{{{n}}}"
    return "".join(parts)


def to_react(tokens: list, vars_: dict, component: str) -> str:
    scripts, out, stack = [], [], []
    for t in tokens:
        if t[0] == "text":
            out.append(_jsx_text(t[1], vars_, stack[-1] if stack else None))
        elif t[0] == "if":
            out.append(f"{{{'!' if t[2] else ''}{t[1]} && (<>")
        elif t[0] == "endif":
            out.append("</>)}")
        elif t[1] == "script":   # a <script> does not run in JSX: a useEffect loads it
            if t[0] == "start":
                scripts.append(next(v for _, a, v in t[2] if a == "src"))
        elif t[0] == "start":
            attrs = "".join(sep + _jsx_attr(t[1], t[2], a, v) for sep, a, v in t[2])
            out.append(f"<{t[1]}{attrs}{' />' if t[3] else '>'}")
            if not t[3]:
                stack.append(t[1])
        else:
            stack.pop()
            out.append(f"</{t[1]}>")

    props = ", ".join(f"{n} = {json.dumps(m['default'])}" for n, m in vars_.items())
    body = "\n".join("      " + ln for ln in "".join(out).splitlines() if ln.strip())
    imports, effect = "", ""
    if scripts:
        imports = "import { useEffect } from 'react';\n\n"
        deps = sorted({v for s in scripts for v in VAR_RE.findall(s)})
        effect = (
            "  useEffect(() => {\n"
            f"    const tags = [{', '.join(map(_expr, scripts))}].map((src) => {{\n"
            "      const s = document.createElement('script');\n"
            "      s.src = src;\n"
            "      document.body.appendChild(s);\n"
            "      return s;\n"
            "    });\n"
            "    return () => { tags.forEach((s) => s.remove()); };\n"
            f"  }}, [{', '.join(deps)}]);\n\n"
        )
    return (f"{imports}export default function {component}({{ {props} }}) {{\n{effect}"
            f"  return (\n    <>\n{body}\n    </>\n  );\n}}\n")


def to_dts(vars_: dict, component: str) -> str:
    """The component's props, typed from schema.json."""
    lines = []
    for name, meta in vars_.items():
        doc = meta["doc"].replace("*/", "* /")
        lines.append(f"  /** {doc} Default: {json.dumps(meta['default'])}. */")
        lines.append(f"  {name}?: {'boolean' if meta['type'] == 'bool' else 'string'};")
    return (
        "import type { ReactElement } from 'react';\n\n"
        f"export interface {component}Props {{\n" + "\n".join(lines) + "\n}\n\n"
        f"export default function {component}(props: {component}Props): ReactElement;\n"
    )


# ---- the npm manifest ------------------------------------------------------

def to_package_json(version: str) -> str:
    """The repository-root package.json: `npm install github:arXiv/design-system#<sha>`
    installs the React components at the same SHA Python consumers pin."""
    manifest = {
        "name": "@arxiv/brand-templates",
        "version": version,
        "description": "arXiv brand head/header/footer as React components, generated from the "
                       "design system's portable-Jinja templates. Install by git SHA: the same "
                       "SHA Python consumers pin. GENERATED by templates/generate.py.",
        "private": True,
        "license": "SEE LICENSE IN LICENSE",
        "type": "module",
        "sideEffects": False,
        "files": ["templates/adapters/react/*.jsx", "templates/adapters/react/*.d.ts"],
        "exports": {
            f"./{component(s)}": {"types": f"./templates/adapters/react/{component(s)}.d.ts",
                                  "default": f"./templates/adapters/react/{component(s)}.jsx"}
            for s in SECTIONS
        },
        "peerDependencies": {"react": ">=18"},
    }
    return json.dumps(manifest, indent=2) + "\n"


def version() -> str:
    """The package version, from pyproject.toml (it stays put: the SHA is what moves)."""
    text = (TEMPLATES / "pyproject.toml").read_text(encoding="utf-8")
    return re.search(r'^version = "([^"]+)"', text, re.M).group(1)


# ---- every generated file --------------------------------------------------

def component(section: str) -> str:
    """The React component's name: labs_accordion -> LabsAccordion."""
    return "".join(part.capitalize() for part in section.split("_"))


def generated() -> dict[str, str]:
    """Every generated file, keyed by path relative to the repository root. None is edited
    by hand; verification/check-generated.py fails if the repository differs from this."""
    out: dict[str, str] = {}
    for section in SECTIONS:
        comp, (tokens, vars_) = component(section), template(section)
        origin = f"GENERATED from templates/arxiv_brand/{section}.html by templates/generate.py — do not edit"
        out[f"templates/adapters/templatetoolkit/{section}.tt"] = (
            f"[%# {origin} %]\n" + to_templatetoolkit(tokens, vars_))
        out[f"templates/adapters/react/{comp}.jsx"] = f"// {origin}\n" + to_react(tokens, vars_, comp)
        out[f"templates/adapters/react/{comp}.d.ts"] = f"// {origin}\n" + to_dts(vars_, comp)
        out[f"templates/adapters/vendored/{section}.html"] = (
            f"<!-- {origin} -->\n" + render(tokens, vars_, {}).strip() + "\n")
    out["package.json"] = to_package_json(version())
    return out


def main() -> None:
    for rel, text in generated().items():
        path = REPO / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {rel}")


if __name__ == "__main__":
    main()
