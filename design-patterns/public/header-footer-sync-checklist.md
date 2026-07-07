# Spinout chrome — cross-repo sync checklist & pre-PR audit

Companion to `header-footer-rollout.md`. The header/footer/banner triple is hand-mirrored
across repos (no generator on the launch timeline), so **before opening each repo's PR, walk
this checklist against that repo**: every *uniform* item (Parts A–G) must match the
arxiv-base SSOT, and the only allowed differences are the *documented deviations* in Part H.

SSOT = `arxiv-base/arxiv/base/templates/base/{header,footer,announcement_banner}.html` +
`arxiv-base/arxiv/base/static/{css,js,fonts,images}/…`.
Consumers (browse, auth) inherit it via `{% include %}` + `base.static` — for them, Parts A–F
are automatic; audit only Part G + H. Vendorers (search, submit, status, docs) carry copies —
audit everything.

---

## A. Assets — byte-identical to SSOT
Run `design-system/scripts/chrome-assets.sh check` → every cell `ok`. Covers:
- [ ] `css/arxiv-header-footer.css`
- [ ] `js/arxiv-header.js`
- [ ] `fonts/IBMPlexSans-{Regular,Medium,SemiBold}.woff2` + `IBMPlexSans-LICENSE.txt`
- [ ] `images/arxiv-logo-primary-light.svg`
- [ ] `images/funders/{simons-foundation,schmidt-sciences}.png`
- [ ] `images/icons/smileybones-small.svg`

## B. Announcement banner (`.ds-announcement`)
- [ ] wrapper: `id="announcement-banner"`, `role="region"`, `aria-label="Announcement"`, `data-banner-name="spinout-nonprofit"`
- [ ] glyph `.ds-announcement-glyph` → `smileybones-small.svg`, `alt=""`, `aria-hidden="true"`
- [ ] text `.ds-announcement-text` = **"arXiv is now an independent nonprofit!"**
- [ ] link `.ds-announcement-link` = **"Learn more"** → `https://info.arxiv.org/about`
- [ ] dismiss `.ds-announcement-close` `<button type="button" aria-label="Dismiss announcement">×`
- [ ] rendered **above** `.ds-site-header` (sibling immediately before it)

## C. Header (`.ds-site-header`)
- [ ] (base/browse/auth only) `ignore_me` honeypot `<a class="is-sr-only" aria-hidden tabindex="-1">`
- [ ] logo `.ds-site-header-logo` → home, `aria-label="archive home"`, `<img alt="archive" src=arxiv-logo-primary-light.svg>`
- [ ] hamburger `#ds-nav-toggle.ds-site-header-nav-toggle` (3-line svg), `aria-controls="ds-site-header-nav"`, `aria-expanded="false"`
- [ ] nav `#ds-site-header-nav.ds-site-header-nav` items **in order**:
  - [ ] **Search** `#arxiv-search-toggle` → search page, `aria-controls="arxiv-search-overlay"` (magnifier svg + "Search")
  - [ ] **Submit** → submit/create
  - [ ] **Donate** → `https://info.arxiv.org/about/donate.html`
  - [ ] `.ds-site-header-divider`
  - [ ] auth-conditional: **My Account** + **Logout**, else **Log in** (`.ds-site-header-login`)
- [ ] search overlay `#arxiv-search-overlay.arxiv-search-overlay[hidden]`: `role="search"` form (GET → search), `input[name=query]`, hint + **Advanced search** link
- [ ] skip-link `.ds-skip-link` → the page's main-content id (see Part H for the id per repo)

## D. Footer (`.ds-site-footer`)
- [ ] ack `.ds-site-footer-ack`: "We gratefully acknowledge support from our **major funders**, **member institutions** … and all contributors." + `.ack-member-inline[hidden]`
- [ ] nav `.ds-site-footer-links` **in order**, `&middot;`-separated (`.ds-site-footer-sep`):
      About · Help · Contact · Subscribe · Copyright · Privacy · Accessibility · **Operational Status**
- [ ] Operational Status → `https://status.arxiv.org`, `target="_blank" rel="noopener noreferrer"` + `<span class="is-sr-only"> (opens in new tab)</span>`
- [ ] funders `.ds-site-footer-funders`: label **"Major funding support from"** + `.ds-funder-logo` × 2 (Simons Foundation, Schmidt Sciences, with `alt`)

## E. Head / wiring
- [ ] `<html lang="en">`, `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">`
- [ ] `html.js` setter: `<script>document.documentElement.classList.add('js');</script>` in `<head>`
- [ ] chrome CSS `<link>` → `arxiv-header-footer.css` (vendorers append `?v=20260624c`)
- [ ] chrome JS `<script>` → `arxiv-header.js` (vendorers append `?v=…`)
- [ ] `@font-face` in the chrome CSS loads `url("../fonts/IBMPlexSans-*.woff2")` → **`fonts/` must sit as a sibling of the CSS's dir** in every repo (else IBM Plex 404s; see Part K)
- [ ] **favicon/meta set is SEPARATE from the chrome triple** (not in the asset package): each repo keeps its own favicons. ⚠ base `head.html` still hardcodes `theme-color` / `msapplication-TileColor` / `mask-icon` = `#b31b1b` (Cornell red) — spinout brand-consistency flag, decide whether to update.

## F. Behaviors (from arxiv-header.js — identical because the asset is byte-identical)
- [ ] search overlay opens (icon click / Cmd-Ctrl-K) + closes (Esc / backdrop)
- [ ] hamburger toggles nav (outside-click / Esc close); `.is-collapsible` only when JS ran
- [ ] banner dismissal persists via `localStorage` keyed by `data-banner-name`
- [ ] member-institution `fetch('/institutional_banner')` fills `.ack-member-inline`; **degrades silently** if the endpoint is absent

## F2. Responsive / print / motion (from the byte-identical CSS — uniform wherever vendored)
- [ ] nav collapses to the **hamburger at ≤599px** (`.is-collapsible` + `.is-open`); layout breakpoints 720 / 599 / 520px behave as upstream
- [ ] chrome is **hidden in `@media print`** (header + footer + banner don't print)
- [ ] `@media (prefers-reduced-motion: reduce)` honored (no transitions/animations)
- [ ] footer grid caps at `max-width: 1200px`; this is the chrome's own constraint, not a per-repo container width

## G. Link resolution (per app — no 500 / 404)
- [ ] every header + footer link resolves in *this* app (base/browse/auth via `config.URLS` registry; vendorers via absolute `arxiv.org`/`info.arxiv.org`)
- [ ] no template references a Flask endpoint the app doesn't register

---

## H. Per-repo INTENTIONAL deviations (do NOT "fix" these in the audit)

| Repo | Tactic | Documented deviations |
|---|---|---|
| **arxiv-base** | SSOT (author) | banner gated on `SPINOUT_BANNER_ENABLED`; `ignore_me` honeypot present; links via `url_for`/`base.static` |
| **arxiv-browse** | consume | keeps own `base.html`; `{% include "base/*"%}` + `base.static`; **no vendored copy**; skip-link target = its main container |
| **arxiv-auth** | consume (dep bump) | **zero template edits** (inherits `base/base.html`); the only change = arxiv-base pin → chrome commit + `uv.lock` refresh — **blocked until base lands on `master`** |
| **arxiv-search** | vendor (base 3yr behind) | banner **inlined at top of `block header`** (old base has no `announce` block); footer `body > footer { display: contents }` (drops legacy base wrapper); links absolute; **needs `URL_PREFIX=/search`** or `/search` 404s; static `Log in` |
| **arxiv-submit** | hand-port (Perl/TT) | member-ack omitted (no `/institutional_banner`); admin keeps `#menubar`, skip-link `#main`; abs breadcrumb removed; chrome lives in shared `layouts/_chrome_header.tt` + `_chrome_footer.tt`; login `[% IF c.user_exists %]` |
| **arxiv-status** | vendor (static HTML) | relative `./static/…` asset paths; `docs/.nojekyll`; static `Log in` (no session); skip-link `#content` |
| **arxiv-docs** | vendor (mkdocs) | **docs-ONLY carry-overs**: color-theme toggle + internal docs search kept via `md-header`-class interop; `html{font-size:100%}` reset; `--md-primary-fg-color` de-red; **paper-Search button omitted**; skip-link material's; ⚠ mobile docs-nav drawer gap (open TODO) |

## J. Design-system compliance (no hardcoding)
- [ ] chrome **markup** is class-only — no inline `style=`/hex/rgb (verified: base/browse/auth/search/status markup all clean)
- [ ] the shared chrome CSS uses `--arxiv-*` tokens (1:1 with `design-system.css`)
- [ ] per-repo **CSS additions** reference `--arxiv-*` tokens, not raw literals or a parallel `--color-*` alias namespace (docs additions fixed → `2c10aae5`)
- ⚠ **base `head.html`** `theme-color` / `msapplication-TileColor` / `mask-icon` = **`#b31b1b`** (Cornell red) vs spinout `--arxiv-ink #1c1a17` — static `<meta>` can't use `var()`; **decide whether to hand-update** for brand consistency
- ℹ **upstream gap (not chrome drift):** `#302c28` (dark-bar hover) and `#4a433d` (dark-bar hairline) are untokenized **in `design-system.css` itself**; the chrome faithfully mirrors them. Fix = tokenize upstream, then re-sync the subset.

## K. Asset reachability in the cloud deploy
Two delivery architectures — audit each repo against its own:

**(A) `base.static` consumers → `https://static.arxiv.org/static/base/<BASE_VERSION>/…`** (base, browse, auth; and **search when `FLASKS3_ACTIVE=1`**). Gated on shared devops:
- [ ] **CORS** — `gs://arxiv-web-static` has **no CORS block** → cross-origin `woff2` from `static.arxiv.org` is **blocked**. Add `cors{}` allowing `https://*.arxiv.org` GET. *(blocks all fonts in mode A)*
- [ ] **fonts uploaded** — chrome fonts land in the bucket **only** via arxiv-base's *unfiltered* `create_all` upload, run out-of-band for the **exact deployed `BASE_VERSION`**. browse's upload filter `r'(css|images\|js)'` and search's `r'(base|css|images|js|sass)'` **both EXCLUDE `fonts/`** → don't rely on consumer uploads for fonts.
- [ ] **version match** — the `<BASE_VERSION>` in the URL must be a version whose upload actually ran (browse pins `branch=master`, floating).
- [ ] **deploy mode** — `FLASKS3_ACTIVE=0` serves same-origin from the bundled arxiv-base package (fonts fine, no CORS); `=1` switches to the bucket (needs CORS + fonts uploaded). Confirm the intended mode per app.

**(B) same-origin vendorers — served from the app's own domain (no bucket, no CORS):**
- [ ] **status** (GitHub Pages, `status.arxiv.org`): `./static/…` relative; `docs/static/fonts/` present; `.nojekyll` present → **SAFE**
- [ ] **docs** (Cloud Build → GCS static bucket `gs://arxiv-docs`, `info.arxiv.org`): `/static/…` absolute; `source/static/fonts/` rsync'd into `site/` → **SAFE**
- [ ] **search** is a vendorer but flask-s3 rewrites `url_for('static',…)` too → it's only same-origin/safe in `FLASKS3_ACTIVE=0`; with `=1` its `/static/search/<v>/fonts/` are uploaded by **nobody** (filter excludes fonts) **and** cross-origin → fix the filter or pin `=0`

**Universal:** the chrome CSS `@font-face url("../fonts/…")` resolves relative to the served CSS, so **`fonts/` must sit beside the `css/` dir** in every served location (verified true everywhere).

**Two devops actions gating the mode-A repos (track outside the template repos):** (1) add bucket CORS for `*.arxiv.org`; (2) ensure chrome fonts are uploaded for the deployed `BASE_VERSION` (consumer filters exclude them).

## I. Per-repo PR-readiness (final gate)
- [ ] branch carries only chrome commits; build/test green where applicable
- [ ] cruft gitignored; `_chrome_preview.html` showcase left **uncommitted**
- [ ] PR description ready — see `arxiv-browse/docs/SPINOUT-PRS.md`
- [ ] coordination respected: base → `master` first; browse+auth re-lock in the same window (`uv lock` → commit lock → rebuild); search/submit/status/docs deploy independently
