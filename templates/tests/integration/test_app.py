"""The Python package under real Jinja: the setup API and the Flask host (test_targets.py
compares every target with Jinja).

    pip install flask pytest && pytest -q
"""
import sys
from pathlib import Path

import pytest
from flask import Flask, render_template_string
from jinja2 import DictLoader, Environment, StrictUndefined

sys.path.insert(0, str(Path(__file__).resolve().parent))
import app as host  # noqa: E402  (also puts templates/ on sys.path)

import arxiv_brand  # noqa: E402


def env(**pages):
    return arxiv_brand.init_env(Environment(autoescape=True, undefined=StrictUndefined,
                                            loader=DictLoader(pages)))


def test_context_checks_names_and_keeps_the_html_slot_raw():
    with pytest.raises(TypeError):
        arxiv_brand.context(base_ulr="https://x")
    footer = env(p='{% include "arxiv_brand/footer.html" %}').get_template("p")
    out = footer.render(**arxiv_brand.context(member_institution="<strong>X</strong>"))
    assert "<strong>X</strong>" in out
    assert arxiv_brand.context(member_institution=None, static_base=None) == {}  # left out
    none = footer.render(**arxiv_brand.context(member_institution=None))
    assert "None" not in none and "member institutions</strong></a>," in none
    head = arxiv_brand.init_env(Environment(autoescape=True), static_base="SITE/")
    assert 'href="SITE/fonts.css"' in head.get_template("arxiv_brand/head.html").render(
        **arxiv_brand.context(static_base=None))  # the site-wide value still applies


def test_host_templates_and_globals_win_and_setup_is_idempotent():
    e = Environment(autoescape=True, loader=DictLoader({"arxiv_brand/footer.html": "HOST FOOTER"}))
    e.globals["static_base"] = "HOST/"
    arxiv_brand.init_env(e)
    arxiv_brand.init_env(e, base_url="https://b.dev")  # later values still apply
    assert len(e.loader.loaders) == 2  # the host's and the package's, once
    assert e.get_template("arxiv_brand/footer.html").render() == "HOST FOOTER"
    assert 'href="HOST/fonts.css"' in e.get_template("arxiv_brand/head.html").render()
    assert 'href="https://b.dev/search"' in e.get_template("arxiv_brand/header.html").render()


def test_config_values_follow_arxiv_conventions():
    assert arxiv_brand.config_values({"BASE_SERVER": "browse.dev.arxiv.org", "HELP_SERVER": "info.dev.arxiv.org",
                                      "EXTERNAL_URL_SCHEME": "http", "BRAND_STATIC_BASE": "S/"}) == {
        "base_url": "http://browse.dev.arxiv.org", "auth_url": "http://browse.dev.arxiv.org",
        "help_url": "http://info.dev.arxiv.org", "static_base": "S/"}
    assert arxiv_brand.config_values({"BASE_SERVER": "b", "AUTH_SERVER": "a"})["auth_url"] == "https://a"
    assert arxiv_brand.config_values({"BRAND_STATIC_BASE": "http://127.0.0.1:8093"})["static_base"] == \
        "http://127.0.0.1:8093/"
    assert arxiv_brand.config_values({}) == {}


def test_flask_links_follow_the_app_config_and_session():
    app = Flask("dev_host")
    app.config.update(BASE_SERVER="browse.dev.arxiv.org", HELP_SERVER="info.dev.arxiv.org")
    arxiv_brand.init_app(app)

    @app.context_processor
    def brand():
        return arxiv_brand.context(signed_in=True)

    with app.test_request_context("/"):
        html = render_template_string(host.PAGE, title="dev")
    assert 'href="https://browse.dev.arxiv.org/user" class="ds-site-header-login">Account</a>' in html
    assert 'href="https://info.dev.arxiv.org/help"' in html
