# arXiv brand templates

The arXiv site chrome — `head` (stylesheet links), `header` (announcement band, header bar,
search overlay) and `footer` — written once as portable Jinja and generated for every
framework an arXiv app uses (one adapter per framework, never per app). It replaces chrome
hand-copied into each app, where every copy drifted and one footer edit took about ten PRs;
stats (ARXIVCE-4501) is the first consumer. Announcements:
[`BANNER_ANNOUNCEMENTS.md`](BANNER_ANNOUNCEMENTS.md).

```
arxiv_brand/{head,header,footer}.html   THE sources, with schema.json — the only files you edit
arxiv_brand/__init__.py                 the Python API: init_app, init_env, config_values, context
adapters/react/                         GENERATED {Head,Header,Footer}.jsx + typed .d.ts
adapters/templatetoolkit/               GENERATED {head,header,footer}.tt
adapters/vendored/                      GENERATED static HTML, every variable at its default
../package.json                         GENERATED npm manifest for the React components
generate.py                             writes every generated file (stdlib only)
assets/                                 chrome JS and json/announcements.json (asset route)
```

## Install and update

A consumer's manifest tracks `master` and its lock file pins the SHA, so an update is a lock
refresh: one SHA moves, reviewed and revertible (Renovate can open it).

**Python** (Flask, FastAPI, plain Jinja). Poetry takes the same `{ git, branch, subdirectory }`:

```toml
[tool.uv.sources]
arxiv-brand-templates = { git = "https://github.com/arXiv/design-system.git", branch = "master", subdirectory = "templates" }
```

```python
arxiv_brand.init_app(app)   # reads BASE_SERVER, AUTH_SERVER, HELP_SERVER, EXTERNAL_URL_SCHEME,
                            # BRAND_STATIC_BASE from app.config; init_env(env, ...) elsewhere,
                            # with autoescape on (Flask's default for .html)

@app.context_processor
def brand():                # only per-request values
    return arxiv_brand.context(signed_in=is_signed_in())
```

```jinja
<head> … {% include "arxiv_brand/head.html" %} </head>
<body> {% include "arxiv_brand/header.html" %} … {% include "arxiv_brand/footer.html" %}
```

Update with `uv lock --upgrade-package arxiv-brand-templates` or `poetry update
arxiv-brand-templates`. A site on arxiv-base gets the chrome through base.

**React.** `npm install "github:arXiv/design-system#master"`, then
`import Footer from "@arxiv/brand-templates/Footer"` (typed props, schema defaults). The
components are JSX for the automatic runtime (Vite's and Next.js's default), which the
bundler transpiles. Update with `npm update @arxiv/brand-templates`.

**TemplateToolkit or static HTML** (submit, tapir, status, lib). Copy
`adapters/templatetoolkit/` or `adapters/vendored/` at a `master` SHA, record the SHA, and copy
again to update.

`static_base`, the asset route, defaults to production. Dev deployments and local previews set
their own (`BRAND_STATIC_BASE`, or the React prop), so a production page never depends on the
dev bucket.

## Template rules

They keep every target a mechanical rewrite of the source: `generate.py` rejects what it
cannot read, with its line, and `tests/integration/test_targets.py` fails where a target
renders other than Jinja.

- **Syntax:** raw HTML, `{{ variable }}` and boolean sections only: no `else`, expressions,
  loops, filters, includes, macros or inheritance. Notes are Jinja comments, which no target
  outputs. Each variable has one `schema.json` entry with an arxiv.org default, for what the
  host resolves on the server.
- **Markup** that JSX can mirror: every element closed (void ones aside), attributes
  double-quoted, sections around whole elements (never inside a tag); no HTML comments,
  inline styles or handlers, `<pre>` or `<textarea>`.
- **Flags:** `{% if flag %}` or `{% if not flag %}` on a `bool`, nesting, removing markup
  rather than hiding it. A `bool` defaults to false, which every engine reads for an omitted
  value, and false is arxiv.org. `hide_nav` drops the nav and the search overlay (a sub-site
  with its own, like info.arxiv.org); `hide_announcement` drops the band; `signed_in` shows
  one Account link for Log in (the five items DESIGN-POLICIES allows; logout is on the
  account page).
- **Links** are fixed paths on `base_url` (home, `/search`, `/search/advanced`, `/submit`,
  `/IgnoreMe`), `auth_url` (`/login`, `account_path`) and `help_url` (donate, the footer
  links): no trailing slash, arxiv.org by default. The one per-link override is
  `account_path` (default `/user`): the keycloak account portal sets `/user-account/`, with
  `auth_url=""` for site-relative links.
- **The type decides escaping**, the same in every target:

  | Type | | Jinja | TemplateToolkit | React |
  |---|---|---|---|---|
  | `attr`, `url` | escaped | `{{ v }}` | `[% v \| html %]` | `{v}`, ``{`…${v}…`}`` |
  | `html` | trusted host markup | `{{ v }}` (marked safe) | `[% v %]` | `dangerouslySetInnerHTML`, on a `<span>` |
  | `bool` | gates a section | `{% if v %}` | `[% IF v %]` / `[% UNLESS v %]` | `{v && (…)}` / `{!v && (…)}` |

  The one `html` slot is `member_institution` (footer): `""` for an anonymous reader (the
  default); the resolved `<span class="ack-member-inline">, <strong>Name</strong></span>` for
  a recognised IP; or that span empty and `hidden`, which `chrome/header.js` fills from the
  same-origin `/institutional_banner`.
- **Defaults travel with each target:** Jinja through `init_env`'s globals, React as prop
  defaults, TemplateToolkit through `[% UNLESS v.defined %]` (an explicit `""` wins); the
  vendored HTML is rendered with them.
- **Behaviour is a static `<script>`** loading design-system JS (`chrome/banner.js`,
  `chrome/header.js`); React loads it from a `useEffect`. The HTML is complete without it,
  except the band. A host that drives the phone menu itself marks `#ds-nav-toggle`
  `data-host-nav`.
- **The host keeps the skip link:** the templates start at the band, so `.ds-skip-link`
  (first in the body) and its target, the main content, are the host's.

## Adding a template

For example `labs_accordion`:

1. Style it in `docs/` (its rules in `design-system.css`, its reference page). Templates are
   markup only.
2. Write `arxiv_brand/labs_accordion.html` to the rules, any new variable in `schema.json`,
   any behaviour in a script under `assets/chrome/`.
3. Add it to `SECTIONS` in `generate.py` and run `python3 templates/generate.py`. It writes
   `LabsAccordion.jsx` and `.d.ts`, `labs_accordion.tt`, the vendored HTML and the
   `./LabsAccordion` export; `test_targets.py` and the checks pick it up, and CI
   (`verification/check-generated.py`) rejects a stale or hand-edited target.
4. For behaviour a browser must show, add a host page to `tests/integration/app.py` and a
   case to `chrome.spec.js`.
5. Merge to `master`. The dev route publishes its CSS and script at once; run the prod
   publish before any consumer ships it.
6. Each consumer relocks, or copies the TemplateToolkit or static adapter at the new SHA, and
   places it: `{% include "arxiv_brand/labs_accordion.html" %}`, `<LabsAccordion />` or
   `[% INCLUDE labs_accordion.tt %]`. Sites on arxiv-base get it when base includes it.

## Assets

The design system owns the brand, funder and chrome-JS assets. `upload_static_assets.py`
publishes them with the stylesheets to one rolling route, `static/design-system/latest/` on
the shared static buckets (base's script shape; CORS is set): dev on every `master` push,
prod by a manual run, the deliberate gate.

- **Compatible, not versioned.** `latest` serves every template version a lock may hold, so
  asset changes are additive: never remove or rename a published file, a `.ds-*` class, or an
  id or attribute an older template or script uses. `verification/check-template-compat.py`
  checks the files and classes of every template version in the history (ids and attributes
  are for review). Pages are cached for up to a year (browse's abs pages), so its `SINCE`
  never retires a younger version. Versioned snapshots would add a second version to move;
  revisit them only for a breaking change no consumer can take in place.
- **Component rules only.** A host with its own page styling loads
  `design-system-components.css` and, separately, `fonts.css` (fonts are global state). Each
  publish derives the component stylesheet from `docs/design-system.css`
  (`build_components_css.py`; never edited or committed) with every rule except two kinds
  that bled into host pages: the OS-auto dark block (dark comes from its `[data-theme]`
  mirror, which `check-drift.py` keeps identical) and rules on raw elements only (`a`,
  `body`). `check-components.py` fails CI if a `.ds-*` class goes missing or either kind gets
  through.
- **Not used:** a git subtree (used nowhere else in the stack; it saves only the lock-refresh
  PR), category-wide routes or a versioned `static3.arxiv.org` (a later static-platform
  track), and a shared mkdocs adapter (info.arxiv.org is the one mkdocs site; arxiv-docs
  renders the package with plain Jinja).

## Tests

```bash
python3 -m unittest discover -s templates/tests          # the build and announcements (stdlib)

cd templates/tests/integration                           # every target, Flask and Chromium
npm ci && pip install flask pytest && pytest -q          # TemplateToolkit: libtemplate-perl
npx playwright install chromium && npm test
```

The integration host (`app.py`) serves a Jinja page, a React page built from the installed
package, and the asset route as `upload_static_assets.py` stages it. `templates-ci.yml` runs
all three.

## Open

- **Production route:** the CI service account (its identity provider limited to this
  repository's `master`) and the first publish; no consumer goes to production before. Every
  `/static/` path already reaches the bucket through Fastly. Then the publish can purge the
  route, and objects can take a longer CDN TTL.
- **Root font size:** base's fixed 14px root and mkdocs-material's 125% root scale the
  rem-sized chrome (a question for the designer).
- **ARXIVCE-4522:** replace the funder logos with a "major funders" link once that page exists.
- **HTML2X-230:** the banner must not cover the phone menu.
- **Clean-up:** drain the design-system assets and the retired banner macro from arxiv-base,
  and move status, lib, submit and tapir onto the TemplateToolkit and static targets.

Background: the dev Slack channel (the update-to-latest and banner-service threads) and
[`dev-workflow-comparison.html`](../planning/proposals/dev-workflow-comparison.html).
