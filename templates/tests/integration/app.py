"""The integration host: a Flask app that uses the brand templates the way consumers do.

  /jinja     arxiv_brand.init_app + a context processor; ?hide_announcement drops the
             band, for the banner tests
  /react     the React host, react.js bundled to dist/ by `npm run build`
  /assets/   the design-system asset route, staged by upload_static_assets.stage

    python3 app.py      # serves on 127.0.0.1:$PORT (default 5001)
"""
import atexit
import os
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE.parents[1]
sys.path[:0] = [str(TEMPLATES), str(TEMPLATES.parent)]

import arxiv_brand  # noqa: E402
import upload_static_assets  # noqa: E402
from flask import Flask, render_template_string, request, send_from_directory  # noqa: E402

STATIC = "/assets/"
ASSETS = tempfile.mkdtemp(prefix="ds-route-")
atexit.register(shutil.rmtree, ASSETS, True)
upload_static_assets.stage(ASSETS)

# The html slot, resolved by the host. Both pages carry the one page-level rule a host's own
# CSS provides (body margin), which the component stylesheet leaves to the host.
MEMBER = '<span class="ack-member-inline">, <strong>RWTH Aachen</strong></span>'

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{{ title }}</title>
  <link rel="icon" href="data:,">
  <style>body { margin: 0; }</style>
  {% include "arxiv_brand/head.html" %}
</head>
<body>
{% include "arxiv_brand/header.html" %}
<main class="ds-container"><p>{{ title }}</p></main>
{% include "arxiv_brand/footer.html" %}
</body>
</html>
"""
REACT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>React host</title><link rel="icon" href="data:,">
<style>body { margin: 0; }</style></head>
<body><div id="root"></div><script src="/react.js"></script></body>
</html>
"""

app = Flask(__name__)
app.config["BRAND_STATIC_BASE"] = STATIC
arxiv_brand.init_app(app)


@app.context_processor
def brand():
    hide = "hide_announcement" in request.args
    return arxiv_brand.context(member_institution=MEMBER, hide_announcement=hide)


@app.get("/jinja")
def jinja():
    return render_template_string(PAGE, title="Jinja host")


@app.get("/react")
def react():
    return REACT_PAGE


@app.get("/react.js")
def react_bundle():
    return send_from_directory(HERE / "dist", "react.js")


@app.get("/assets/<path:name>")
def assets(name):
    return send_from_directory(ASSETS, name)


if __name__ == "__main__":
    import logging

    logging.getLogger("werkzeug").setLevel(logging.WARNING)  # no per-request log lines
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5001")))
