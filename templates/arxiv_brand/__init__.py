"""arXiv brand templates: the shared head/header/footer for Jinja hosts, installed from git
(the lock file pins the SHA). Setup is plain Jinja:

    arxiv_brand.init_app(app)                   # Flask: values from app.config
    arxiv_brand.init_env(env, base_url=...)     # any jinja2.Environment

    @app.context_processor                      # per-request values only
    def brand():
        return arxiv_brand.context(signed_in=is_signed_in())

    {% include "arxiv_brand/head.html" %}  {% include "arxiv_brand/header.html" %}  …

Values resolve from the schema defaults, then the site-wide values given to init_env /
init_app (env.globals), then whatever the render context passes. The templates rely on the
environment's autoescape (Flask's is on for .html): a host that turns it off (arxiv-docs, to
write mkdocs expressions verbatim) must pass trusted values only.
"""
import json
from pathlib import Path
from typing import Any

from jinja2 import ChoiceLoader, Environment, FileSystemLoader, PrefixLoader
from markupsafe import Markup

__all__ = ["init_env", "init_app", "config_values", "context"]

_HERE = Path(__file__).parent
# The template variables (type, default, doc) by name; context() consults it on every request.
_SCHEMA: dict[str, Any] = json.loads((_HERE / "schema.json").read_text(encoding="utf-8"))["vars"]
_INITIALISED = "_arxiv_brand_initialised"


def init_env(env: Environment, **values: Any) -> Environment:
    """Make ``arxiv_brand/*.html`` includable on ``env``, behind its own loader (so a host can
    override a template), and set the schema defaults as globals unless the host defines
    them. ``values`` (checked like ``context``) are site-wide and set as globals too."""
    if not getattr(env, _INITIALISED, False):
        pkg = PrefixLoader({"arxiv_brand": FileSystemLoader(_HERE)})
        env.loader = pkg if env.loader is None else ChoiceLoader([env.loader, pkg])
        for name, meta in _SCHEMA.items():
            env.globals.setdefault(name, _value(meta, meta["default"]))
        setattr(env, _INITIALISED, True)
    env.globals.update(context(**values))
    return env


def config_values(config: Any) -> dict[str, Any]:
    """The values an arXiv app's config carries: BASE_SERVER -> base_url, AUTH_SERVER (else
    BASE_SERVER) -> auth_url, HELP_SERVER -> help_url, joined with EXTERNAL_URL_SCHEME
    (default https), and BRAND_STATIC_BASE -> static_base (its trailing slash added if
    missing). Missing keys are left out."""
    get = config.get
    scheme = get("EXTERNAL_URL_SCHEME") or "https"
    hosts = {"base_url": get("BASE_SERVER"), "auth_url": get("AUTH_SERVER") or get("BASE_SERVER"),
             "help_url": get("HELP_SERVER")}
    out: dict[str, Any] = {name: f"{scheme}://{host}" for name, host in hosts.items() if host}
    if get("BRAND_STATIC_BASE"):
        out["static_base"] = get("BRAND_STATIC_BASE").rstrip("/") + "/"
    return out


def init_app(app: Any, **values: Any) -> Any:
    """Flask: ``init_env(app.jinja_env)`` with ``config_values(app.config)``; explicit
    ``values`` win. Call it after the config is loaded."""
    init_env(app.jinja_env, **{**config_values(app.config), **values})
    return app


def context(**values: Any) -> dict[str, Any]:
    """The given values as a template context: an unknown name raises TypeError (a typo would
    otherwise fall back to the default), a None is left out (so the site-wide value or the
    default applies), bools are coerced, html values marked safe."""
    unknown = sorted(set(values) - set(_SCHEMA))
    if unknown:
        raise TypeError(f"arxiv_brand.context(): unknown variable(s) {unknown}; see schema.json")
    return {name: _value(_SCHEMA[name], value) for name, value in values.items() if value is not None}


def _value(meta: dict[str, Any], value: Any) -> Any:
    if meta["type"] == "bool":
        return bool(value)
    return Markup(value) if meta["type"] == "html" else value
