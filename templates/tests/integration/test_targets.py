"""Every target renders what Jinja renders, for each template and fixture.html (every
construct the rules allow), under every combination of its flags, with the defaults, empty
values and values that need escaping: the stdlib renderer (vendored) exactly, TemplateToolkit
and server-rendered React as a browser reads them (whitespace collapsed), React without a
warning and loading the same scripts. A template is covered once it is in SECTIONS.

    npm ci && pip install flask pytest && pytest -q      # TemplateToolkit: libtemplate-perl
"""
import itertools
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest
from jinja2 import DictLoader, Environment, StrictUndefined

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
import arxiv_brand  # noqa: E402
import generate as g  # noqa: E402

SLOT = '<b class="brand-slot">x &amp; y</b>'   # every html slot's value
TT = r"""use strict; use Template; use JSON::PP;
my $tt = Template->new({ INCLUDE_PATH => $ARGV[0], ENCODING => 'utf8' }) or die Template->error;
my @out = map { my ($c, $out) = ($_, '');
  my %v = map { $_ => (JSON::PP::is_bool($c->{vars}{$_}) ? 0 + $c->{vars}{$_} : $c->{vars}{$_}) } keys %{ $c->{vars} };
  $tt->process($c->{file}, \%v, \$out) or die $tt->error; $out } @{ decode_json(join '', <STDIN>) };
print JSON::PP->new->utf8->encode(\@out);"""

FIXTURE = (HERE / "fixture.html").read_text(encoding="utf-8")
TEMPLATES = {s: g.template(s) for s in g.SECTIONS} | {"fixture": g.template("fixture", g.uncomment(FIXTURE))}


def cases(vars_: dict) -> list[tuple[str, dict]]:
    flags = [n for n, m in vars_.items() if m["type"] == "bool"]
    values = [n for n, m in vars_.items() if m["type"] != "bool"]
    special = {n: SLOT if vars_[n]["type"] == "html" else f"{n} & \"q\" <x> 's" for n in values}
    out = [("omitted", {})]
    for combo in itertools.product([False, True], repeat=len(flags)):
        on = dict(zip(flags, combo))
        label = ",".join(f for f in flags if on[f]) or "off"
        out += [(label, on), (label + "+empty", {**on, **dict.fromkeys(values, "")}),
                (label + "+escaped", {**on, **special})]
    return out


CASES = [(name, label, values) for name, (_, vars_) in TEMPLATES.items() for label, values in cases(vars_)]


@pytest.fixture(scope="module")
def rendered(tmp_path_factory):
    """Each case's output in every target, in CASES order."""
    tmp = tmp_path_factory.mktemp("targets")
    jinja = arxiv_brand.init_env(Environment(autoescape=True, undefined=StrictUndefined,
                                             loader=DictLoader({"fixture.html": FIXTURE})))
    components = {}
    for name, (tokens, vars_) in TEMPLATES.items():
        (tmp / f"{name}.tt").write_text(g.to_templatetoolkit(tokens, vars_), encoding="utf-8")
        (tmp / f"{name}.jsx").write_text(g.to_react(tokens, vars_, g.component(name)), encoding="utf-8")
        components[g.component(name)] = str(tmp / f"{name}.jsx")
    tt = json.loads(subprocess.run(
        ["perl", "-e", TT, str(tmp)], capture_output=True, text=True, check=True,
        input=json.dumps([{"file": f"{name}.tt", "vars": values} for name, _, values in CASES])).stdout)
    react = json.loads(subprocess.run(
        ["node", str(HERE / "render_react.cjs")], capture_output=True, text=True, check=True,
        input=json.dumps({"components": components, "cases": [
            {"component": g.component(name), "props": values} for name, _, values in CASES]})).stdout)
    out = []
    for (name, _, values), t, r in zip(CASES, tt, react):
        page = jinja.get_template("fixture.html" if name == "fixture" else f"arxiv_brand/{name}.html")
        out.append({"jinja": page.render(**arxiv_brand.context(**values)), "tt": t, "react": r,
                    "stdlib": g.render(*TEMPLATES[name], values)})
    return out


class Read(HTMLParser):
    """Elements with sorted attributes, and text with whitespace collapsed, dropped where it
    is only whitespace between top-level elements or in a table (as generate.py leaves it)."""
    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.out, self.scripts, self.open = [], [], []
        self.feed(html.strip())
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = tuple(sorted((k, v or "") for k, v in attrs))
        if tag == "script":
            self.scripts.append(dict(attrs)["src"])
        elif not (tag == "link" and ("rel", "preload") in attrs):   # React's own image preloads
            self.out.append((tag, attrs))
        if tag not in g.VOID:
            self.open.append(tag)

    def handle_endtag(self, tag):
        if tag not in g.VOID:
            self.open.pop()
            if tag != "script":
                self.out.append(("/" + tag,))

    def handle_data(self, data):
        if data.strip() or (self.open and self.open[-1] not in g.NO_TEXT):
            self.out.append(("#text", data))


def read(html: str, react: bool = False) -> tuple[list, list]:
    r = Read(html)
    ev = r.out
    if react:   # the <span> React puts an html slot in
        for i in reversed(range(len(ev) - 1)):
            if ev[i] == ("span", ()) and ev[i + 1] in (("/span",), ("b", (("class", "brand-slot"),))):
                del ev[next(j for j in range(i + 1, len(ev)) if ev[j] == ("/span",))], ev[i]
    out = []
    for e in ev:   # adjacent text reads as one
        if e[0] == "#text" and out and out[-1][0] == "#text":
            out[-1] = ("#text", out[-1][1] + e[1])
        else:
            out.append(e)
    return [("#text", re.sub(r"\s+", " ", e[1])) if e[0] == "#text" else e for e in out], r.scripts


@pytest.mark.parametrize("i", range(len(CASES)), ids=[f"{n}:{c}" for n, c, _ in CASES])
def test_every_target_renders_what_jinja_renders(rendered, i):
    out = rendered[i]
    assert out["stdlib"].strip() == out["jinja"].strip(), "stdlib renderer (vendored)"
    want = read(out["jinja"])
    assert read(out["tt"]) == want, "TemplateToolkit"
    assert out["react"]["errors"] == [], "React logged"
    assert (read(out["react"]["html"], react=True)[0], out["react"]["scripts"]) == want, "React"
