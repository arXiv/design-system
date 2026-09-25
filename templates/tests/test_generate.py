"""The brand-template build: the source's rules and the templates' content (every target is
compared with Jinja in integration/test_targets.py). Stdlib only:

    python3 -m unittest discover -s templates/tests
"""
import re
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate as g  # noqa: E402

HEADER_LINKS = ("{b}/", "{b}/search", "{b}/search/advanced", "{b}/submit", "{b}/IgnoreMe",
                "{a}/login", "{h}/about/donate.html")


def render(section: str, context: dict) -> str:
    return g.render(*g.template(section), context)


class TestSource(unittest.TestCase):
    def test_every_declared_variable_is_used(self):
        used = set().union(*(g.template(s)[1] for s in g.SECTIONS))
        self.assertEqual(set(g.VARS) - used, set())

    def test_the_rules_are_enforced(self):
        """A source outside the rules (README.md, Template rules) fails, with its line."""
        for bad in ("<details{% if hide_nav %} open{% endif %}>x</details>",
                    '<a class="t{% if signed_in %} on{% endif %}">x</a>',
                    "{% if hide_nav %}<div>{% endif %}</div>", "<div><!-- note --></div>",
                    "{% for x in y %}{% endfor %}", "{% if hide_nav %}a{% else %}b{% endif %}",
                    "{% if header_variant %}x{% endif %}", "{% if on %}x{% endif %}",
                    "<a title='{{ base_url }}'>x</a>", '<a href="{{ base_url|e }}">x</a>',
                    "<p>{{ signed_in }}</p>", "<p>[% x %]</p>", "<div/>", "<p>open", "<pre>x</pre>",
                    "<script>go()</script>"):
            with mock.patch.dict(g.VARS, {"on": {"type": "bool", "default": True, "doc": ""}}), \
                    self.assertRaises((KeyError, ValueError), msg=bad):
                g.template("t", bad)


class TestTemplates(unittest.TestCase):
    """The content, through the stdlib renderer."""

    def test_links_are_paths_on_three_base_urls(self):
        header = render("header", {"base_url": "B", "auth_url": "A", "help_url": "H"})
        for link in HEADER_LINKS:
            self.assertIn(f'href="{link.format(b="B", a="A", h="H")}"', header)
        footer = render("footer", {"help_url": "H"})
        self.assertIn('href="H/help"', footer)
        self.assertNotIn("info.arxiv.org", footer)

    def test_the_flags(self):
        # Signed in, Account replaces Log in (five items with the logo, DESIGN-POLICIES); logout
        # is on the account page.
        header = render("header", {"signed_in": True})
        self.assertIn('href="https://arxiv.org/user" class="ds-site-header-login">Account</a>', header)
        for gone in (">Log in<", "/logout"):
            self.assertNotIn(gone, header)
        portal = render("header", {"signed_in": True, "auth_url": "", "account_path": "/user-account/"})
        self.assertIn('href="/user-account/" class="ds-site-header-login">Account</a>', portal)
        header = render("header", {"hide_nav": True})
        for gone in ('id="ds-site-header-nav"', 'id="ds-search-overlay"'):
            self.assertNotIn(gone, header)
        self.assertIn('class="ds-site-header-logo"', header)
        self.assertNotIn('id="ds-announcement"', render("header", {"hide_announcement": True}))

    def test_every_new_tab_link_says_so(self):
        for section in g.SECTIONS:
            for link in re.findall(r'<a [^>]*target="_blank".*?</a>', render(section, {}), re.S):
                self.assertIn('<span class="is-sr-only"> (opens in new tab)</span>', link, section)


if __name__ == "__main__":
    unittest.main()
