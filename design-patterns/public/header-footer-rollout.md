# Spinout header/footer — cross-repo rollout process

How the codified spinout chrome — `.ds-announcement` (banner), `.ds-site-header`,
`.ds-site-footer` (codified 2026-06-11; see `header-styles.html`, `footer-styles.html`,
`design-system.css`) — is propagated from the design system into the production
repositories. **arxiv-base is the single source of truth** for the shipped markup + the asset
package; every other surface consumes, vendors, or regenerates from it.

**Method (process):** bring every affected repo onto the same stabilized, uniform asset package
in working-tree feature branches (`ARXIVCE-4426-spinout-header-footer`) and QA them together —
**then, and only then, open PRs.** Stabilize the single source of truth first; a single uniform
reusable asset package across all repos is the goal.

**Stabilization status (working trees, no PRs yet):**
- Vendored + build-verified: **arxiv-search** (Flask preview renders the chrome), **arxiv-status**
  (static page; asset package byte-identical to the SSOT), **arxiv-docs** (`mkdocs build` renders
  the chrome; legacy Cornell chrome removed).
- Per the tactics below: **arxiv-base** (authors the SSOT), **arxiv-browse** / **arxiv-auth**
  (consume), **arxiv-submit** (hand-port — all four layouts carry the banner).

## Decision
**arxiv-base is the single source of truth.** browse / auth **consume** the chrome from
arxiv-base at runtime; arxiv-search **vendors** (its pin is too old to bump safely);
arxiv-submit (Perl/Catalyst, no arxiv-base) **vendors** a hand-port; **info.arxiv.org /
arxiv-docs** (mkdocs-material) ultimately **regenerates** its static theme from arxiv-base (today
it **vendors** for stabilization, see its section); **status.arxiv.org** vendors a static copy.
browse keeps its own `base.html` and other deviations — it only swaps its chrome includes/links
to arxiv-base and deletes its vendored copies. Go-live: dev-soak all week → coordinated cutover.

**Scope** (JIRA ARXIVCE-4425): arxiv-base, arxiv-auth, arxiv-browse, arxiv-search, arxiv-submit,
**arxiv-docs (info.arxiv.org)**, and **status.arxiv.org** (linked as "Operational status" in the
new footer, so one click from arxiv.org). Same feature branch on every repo:
`ARXIVCE-4426-spinout-header-footer`.

## What lands in arxiv-base (the SSOT)
Replace the legacy Cornell chrome in place so apps that extend `base/base.html` get it for free:
- `base/templates/base/header.html` ← spinout header + search overlay
- `base/templates/base/footer.html` ← spinout footer
- `base/templates/base/announcement_banner.html` ← reusable banner macro
- `base/static/css/arxiv-header-footer.css`, `js/arxiv-header.js`, `fonts/IBMPlexSans-*.woff2`,
  `images/arxiv-logo-primary-light.svg`, `images/funders/*.png`, `images/icons/smileybones-small.svg`
- `base/head.html`: link the CSS + add the `html.js` setter; `base/base.html`: load
  `arxiv-header.js` in place of `member_acknowledgement.js`; strip Cornell identity.
- Bump the package version → rotates `/static/base/<version>/…` (auto cache-bust); release.

The **vendored copies must stay byte-identical to this SSOT** — verified for arxiv-search and
arxiv-status (`diff` clean against `base/static/css/arxiv-header-footer.css`); re-verify on every
asset change so the package stays uniform.

## Don't drop the banner (it's a separate block, not part of the header)
The announcement banner is **not** in `header.html`. arxiv-base renders it in
`base/base.html` via its own `{% block announcement %}`, **above** `{% block header %}`,
by calling the `announcement_banner(text, link_text, link, name)` macro from
`base/announcement_banner.html`. The dismissal JS (`arxiv-header.js`, keyed by
`data-banner-name`), the `.ds-announcement*` CSS, and `smileybones-small.svg` are
already part of the shared chrome — **only the markup has to be present** for the banner
to show.

⟹ An app that **inherits** base.html's default rendering gets the banner for free. An app
that **vendors** base.html, **overrides** `block header` / `block announcement`, or extends
an **older** base.html with no announcement block will **silently drop the banner** — the
header and footer look correct, but the band is just gone. Such apps must render
`.ds-announcement` themselves: import + invoke the macro, or inline its markup at the top of
the header override.

**This bit arxiv-search** (vendored chrome on a 3-yr-old base that has no `announcement`
block): its header/footer override shipped without the banner until the `.ds-announcement`
markup was added at the top of `block header` (asset via `url_for('static', …)`, since search
serves its own vendored copy, not `base.static`).

**Per-deployment banner checklist** — verify the band actually renders, not just the header/footer:
- [ ] **arxiv-base** — `{% block announcement %}` invokes `announcement_banner(...)` in `base.html`.
- [ ] **arxiv-browse** — imports the macro **and calls it** (importing alone renders nothing).
- [ ] **arxiv-auth** — inherits base.html; does **not** override `block announcement`.
- [x] **arxiv-search** — while vendoring on the old base, `.ds-announcement` is inlined at the top
      of `block header` (no `announcement` block to inherit); drop it once search consumes a
      chrome-bearing base.
- [ ] **arxiv-submit** — hand-port adds the `.ds-announcement` markup to the TT header partial
      (the macro is Jinja-only; copy the rendered markup, asset path → `public/`). Present in all
      four layouts (application/short/abs/admin).
- [x] **arxiv-docs (info.arxiv.org)** — `.ds-announcement` placed at the top of the
      `{% block header %}` override in `overrides/main.html` (a sibling before `.ds-site-header`,
      uniform with search/status; avoids mkdocs-material's `.md-banner` wrapper).
- [x] **status.arxiv.org** — `.ds-announcement` is a sibling div before `<header>` in
      `docs/index.html`.

## Per-repo tactic
| Repo | Tactic |
|---|---|
| **arxiv-base** | Author the chrome (above), bump version, **release on `master`**, tag. Critical path. |
| **arxiv-browse** | 4 edits in `base.html` (`{% include "base/header.html" %}`, footer, `base.static` CSS/JS) + banner-macro import; **delete** the vendored copies. |
| **arxiv-auth** | Re-pin arxiv-base to the release tag (today: `branch="master"`); verify login/register/profile/registry render. No template edits. |
| **arxiv-search** | Bump arxiv-base in `pyproject.toml` + `Pipfile` + `poetry.lock` + `Pipfile.lock`; verify search pages. `search.css` has no conflicts. While still on the old base it **vendors** the chrome instead — inline the `.ds-announcement` banner in the `block header` override (see banner checklist). |
| **arxiv-submit** | Hand-port `header.tt`/`footer.tt` from the browse partials, `INCLUDE` across `application/short/abs/admin.tt`, retire `cu_identity.tt`; copy assets to `public/`; drop member-ack (no `/institutional_banner`). Independent/parallel. |
| **arxiv-docs** (info.arxiv.org) | mkdocs-material site; chrome normally **baked at build time** by `make_arxiv_theme` (a throwaway Flask+arxiv-base render). **Stabilized now by vendoring** (see section); canonical path is to repoint `prep_for_mkdocs.sh` → chrome-bearing base and regenerate later. |
| **arxiv-status** (status.arxiv.org) | Single static `docs/index.html`; vendor the asset package into `docs/static/` and hand-place `.ds-announcement` + `.ds-site-header` + `.ds-site-footer`. Done. |

## arxiv-docs (info.arxiv.org) — vendored now, regenerate later
arxiv-docs is an **mkdocs-material static site**. It normally consumes arxiv-base chrome at
**build time**: `make_arxiv_theme/` runs a throwaway Flask app (`app.py`, `Base(app)`) that
renders `make_arxiv_theme/templates/main.html`, expanding `{% include "base/{head,header,footer}.html" %}`
into static HTML written to `overrides/main.html` (mkdocs `custom_dir`); mkdocs blocks survive
via `{% raw %}`. The pre-spinout `overrides/main.html` carried **Cornell chrome** only because the
generator was pinned to old base `@ARXIVNG-5185` (`prep_for_mkdocs.sh`).

**What was done for stabilization (vendored):** because the chrome-bearing arxiv-base is not yet
on a base the generator can target, the `.ds-*` chrome was vendored directly:
- Asset package copied from the SSOT into `source/static/{css,js,fonts,images}` (mkdocs serves
  `source/` at site root; CSS `@font-face` uses `../fonts/…`, so the `css/`+`fonts/` layout is
  preserved). CSS/JS verified byte-identical to the SSOT.
- `overrides/main.html` edited (the "do not hand-edit / regenerate" banner is replaced with a note
  that it is now a hand-vendored copy): `extrahead` links the chrome CSS + sets `html.js`; the
  `header` block gets the `.ds-announcement` banner + `.ds-site-header` + search overlay (then
  `{{ super() }}` keeps material's `.md-header` nav below); the `footer` block becomes
  `.ds-site-footer` + loads `arxiv-header.js`. Asset URLs are root-relative `/static/…`.
- Coexistence fix: material's own `.md-header` (its docs search/nav, kept via `{{ super() }}`)
  was recoloured from Cornell Red to Library Grey in `source/stylesheets/extra.css`
  (`--md-primary-fg-color`; blast radius is just `.md-header`/`.md-tabs`/`.md-skip`) so it reads
  as a subordinate toolbar under the black brand bar — no heritage red competing below. The shared
  chrome CSS is left byte-identical to the SSOT; this tweak lives in the site's own `extra.css`.
- Verified with `mkdocs build` + screenshot: black `.ds-site-header` brand bar over a muted grey
  docs toolbar, banner + funder footer render, no Cornell chrome remains.

**Canonical re-sync (later, once base master carries the chrome):**
1. Repoint `prep_for_mkdocs.sh` from `@ARXIVNG-5185` → the chrome-bearing master/tag.
2. Add the banner in `make_arxiv_theme/templates/main.html` `{% raw %}{% block announce %}{% endraw %}`
   (`{% import "base/announcement_banner.html" as ann %}` + `ann.announcement_banner(...)`), or keep
   the header-block placement for uniformity with search/status.
3. Regenerate `overrides/main.html`; bump `APP_VERSION` in `app.py` and confirm the chrome assets
   are published to `static.arxiv.org` (FlaskS3 bucket `arxiv-web-static1`) so baked URLs resolve;
   otherwise keep the local `source/static/` vendoring.
4. `mkdocs build` → static output → deploy via `deploy/`. arxiv-docs couples to arxiv-base only at
   regeneration time; the deployed artifact is fully static.

## Coordination (the sharp edges)
- **browse & auth consume arxiv-base via `branch="master"`** (browse forces it fresh via
  `exclude-newer-package = { arxiv-base = "1 minute" }`); **search pins rev `1.0.1`** and
  **vendors** instead; **arxiv-docs** regenerates from master at build time (vendored for now). ⟹
  the chrome must release on **master**; the arxiv-base work branch must sit on `master`.
- **Policy (decided): keep the `branch="master"` pin untouched — do _not_ switch to a tag — and
  drive updates with manual build triggers.** Both consumer images install **frozen**
  (`uv sync --frozen`), so what ships is the SHA in the committed `uv.lock`, not "latest master".
  Adopting the chrome therefore needs a `uv lock` refresh + commit, then a manual rebuild (see
  next section). Re-lock browse + auth in the **same window** so they converge on the same master
  SHA — that buys reproducibility without tag-pinning.

## Post-merge: build all arxiv-base dependents
Merging the chrome to arxiv-base `master` changes **nothing in production** on its own —
arxiv-base is a build-time dependency baked into each image (or static theme), not a runtime
service, and there is no cross-repo CI trigger. After the master merge, rebuild each dependent
**manually**:

**Runtime consumers — browse, auth** (images build with `uv sync --frozen`, so the committed
`uv.lock` SHA is what ships):
1. `uv lock` — re-resolves arxiv-base to the new master SHA (browse's `exclude-newer-package`
   grabs the freshest commit; all other deps stay put). **Skipping this makes a rebuild reinstall
   the old frozen SHA and show no chrome.**
2. Commit the updated lockfile (`uv.lock` at browse root; `arxiv-auth/uv.lock` for auth).
3. Manually trigger the Cloud Build → Cloud Run deploy.
4. Leave `pyproject.toml`'s `arxiv-base = { …, branch = "master" }` line unchanged.

**Generation-time consumer — arxiv-docs** (static site): if/when re-synced via the generator, run
`make_arxiv_theme/prep_for_mkdocs.sh`, commit the regenerated theme, `mkdocs build`, deploy via
`deploy/`. While vendored, it ships on its own branch merge like the static set below.

**Not arxiv-base dependents — search, submit, status.arxiv.org** (and arxiv-docs while vendored):
vendored / local; they ship the chrome on their own branch merge + redeploy, independent of the
base master merge.

Order the manual triggers per the cutover sequence below; re-lock browse + auth together.

## 7-day sequence
1. **D1–2** arxiv-base port + self-verify; submit port + arxiv-docs/status vendoring in parallel;
   confirm release branch.
2. **D2** land arxiv-base on master, bump+tag, deploy arxiv-base-dev.
3. **D2–3** browse consume-edits + re-lock; auth + search pin-bumps → dev/QA.
4. **D3–5** cross-app QA (visual parity, 720/<599 responsive, a11y, no-JS, member-ack, banner —
   run the per-deployment banner checklist above on **every** app, not just arxiv-base).
5. **D6** staging soak + sign-off; freeze.
6. **D7** coordinated prod cutover (manual triggers — see "Post-merge: build all arxiv-base
   dependents"): arxiv-base release → re-lock+rebuild **auth + browse** in the same window →
   regenerate/deploy **arxiv-docs** → **search + submit + status.arxiv.org** on their own.
