# Handoff — design-system foundations

## State

16 commits on `master`, **none pushed**. Working tree clean. A local server
serves the repo at `http://localhost:8080` (restart with
`python3 -m http.server 8080` from the repo root).

## What was built

**A foundation.** The system had 91 components and no `body`, headings,
container, code or table styling, so every docs page invented its own.
`.ds-page` / `.ds-container` now provide it, scoped so a legacy page can link
the stylesheet safely.

**Spacing as a system.** Named rhythm — `--space-tight` / `--space-block` /
`--space-section` — where a page names the *kind of break*, never a pixel.
Containers own the space between regions; elements own prose flow. Scale in
rem so it moves with the reader's text size.

**Gap.** No separate scale: gap uses the rhythm on either axis. One addition,
`--gap-glyph` (0.5em), for the space between a glyph and its label inside a
control — the one thing the rhythm cannot supply.

**Content width.** One width, 850px, and the policy rewritten to state what it
costs rather than contradict itself.

**Components consolidated from duplicates:** one header with two surfaces
(`.ds-site-header` + `--light`), `.ds-panel-label` (was eight implementations
at six sizes), `.ds-btn-group` (was nine), `.ds-card` / `.ds-card-grid` /
`.ds-table-framed` (the docs had invented the card three times), one
`<pre><code>` shape (was four).

**Full bleed by grid track**, replacing `calc(-50vw + 50%)` — that trick
overhangs by the scrollbar, because `100vw` includes it and the document width
does not.

**Cascade layers instead of `!important`.** Unlayered author CSS already beats
layered vendored CSS. The paper went 188 → 26.

Duplicated selectors across the docs: **29 → 0**.

## Gotchas that cost real time

- **`!important` inverts layer order.** A layered `!important` beats an
  unlayered one whatever its specificity. ar5iv forces
  `.ltx_title_document { font-size: 1.7rem !important }`, so the paper title's
  `clamp()` was dead code until an `arxiv-override` layer was declared *before*
  the vendored stylesheets.
- **A rule can name only `.ds-` classes and still be page layout.** Deleting
  `footer.ds-site-footer { grid-area: footer }` as a "duplicate" put the footer
  at the top of the page.
- **Verify after every write**: HTML tag balance, CSS brace balance, *and CSS
  comment-delimiter balance*. A regex that drops a sentence can take its `/*`
  with it — valid-looking, silently fatal. Never collapse runs of spaces inside
  comments; it flattens hanging indents across hundreds of them.
- **ar5iv paints `background-color` on every `<img>`** so transparent figure
  PNGs survive a dark canvas. Chrome logos must opt out.
- **`docs/public/*.html` and `docs/internal/*.html` are outside
  `glob('docs/*.html')`** — two sweeps missed them.

## Conventions now in force

- No dates, names, or change history in comments. The system is not in
  production; breadcrumbs are clutter. Backlog items go in
  `planning/NEXT-STEPS.md`, which Shamsi owns.
- arXiv writing policy: **no contractions** in any docs or comment prose.
- Mockups are not a style reference. Patterns are promoted into `docs/` when
  they stabilise.

## Open decisions

1. **The four close buttons.** `.ds-announcement-close`, `.ds-popover-close`,
   `.ds-alert-dismiss`, and the lightbox's own — same job, four names. Agreed
   direction: one close control, hosts supply only position. Two sub-questions:
   should it be the text tier (no fill, no border), and is `×` the right glyph
   when the system mandates Lucide icons everywhere else? **Next step: survey
   the four and report what they actually differ on.**
2. **Icon-only controls on chrome.** Zoom in / out / reset / close are one
   family. Agreed they belong on `buttons.html`, framed as *icon-only controls
   on a chrome surface* — not "lightbox controls", which would name a component
   after the first place it appeared.
3. **The three-tier model**, agreed but only partly built:
   - Tier 1 `design-system.css` — anything a second surface could use. **A
     modal and a toggle belong here and do not exist.** Build the modal from
     requirements (focus trap, restore focus, scroll lock, Escape) using native
     `<dialog>`; the lightbox is a poor template. The toggle needs reconciling
     with the internal one: same visual, two legitimate behaviours (a checkbox
     when it is a form setting, `aria-pressed` when it is an immediate action).
   - Tier 2 `docs/public/reader.css` — **not yet created.** Marginalia, the
     equation and figure regions, the contents bar.
   - Tier 3 — the mockup, for anything still moving.
4. **Internal is two axes, not one.** 57 internal-only classes are genuinely
   tier 2. But 22 (`.ds-alert*`, `.ds-tag*`, `.ds-field`, `.ds-input`,
   `.ds-label`, `.ds-check`) are the same component in a different palette and
   want token re-pointing, like `.ds-site-header--light`. Access Lime as
   primary is a **token** decision, not a stylesheet one.
   Deeper: the two stylesheets share **7 of ~60 token names** — internal says
   `--canvas`, `--grey`, `--danger`; public says `--arxiv-warm-wash`,
   `--arxiv-library-grey`, `--arxiv-error-border`. One name per thing, broken
   at the token layer. Its own project.

## Immediate queue on `html-phase1.html`

Seven components are still rebuilt under other names, now that the page links
the stylesheet. In rough order of size:

| Mockup | Rules | Should be |
|---|---|---|
| `.mg-cite-block`, `.fig-region`, `.eqn-region`, `.mg-band` | 29 | `.ds-card` |
| `.cite-popover`, `.ftn-popover` | 25 | `.ds-popover` |
| `.mg-acc*` | 24 | `.ds-acc` |
| `.eqn-chip`, `.fig-chip`, `.cite-chip` | 24 | `.ds-tag` |
| `.mg-verwarn`, `.mg-a11y-line` | 12 | `.ds-alert` |
| `.mg-btn-quiet`, `.ibtn*` | 7 | `.ds-btn-text` |
| `.fig-alt-label`, `.ltx_title_abstract` | 5 | `.ds-panel-label` |

These are markup changes, not deletions. `.mg-verwarn` already uses the right
*tokens* and rebuilds only the geometry, which is why it reads as almost-right.

Also outstanding there: **no rhythm tokens are defined in the mockup**, so it
uses 54 raw pixel gaps and 41 pixel font-sizes across 9 sizes (including a
12.5px). Those come free now that the stylesheet is linked; the values need
converting.

## Also owed

- **`.ds-acc` has four summary variants at four sizes** with nothing explaining
  why. Shamsi has thoughts queued on accordions.
- **The 4px header navs.** In the between-siblings gap family 8px is the
  default, but `.ds-site-header-nav` and `.ds-reader-header-nav` sit at 4px.
  Deliberate density or drift — answerable by looking, not asserting.
- **`abstract-phase2.html` still vendors its own CSS.** Same treatment as the
  paper: link the stylesheet, delete the copies.
- **Two pre-existing print bugs in the paper**, found and left: printing under
  a dark OS preference gets a dark background, and the bibliography's viewport
  padding survives into print. Both need the print selectors' specificity
  raised.
