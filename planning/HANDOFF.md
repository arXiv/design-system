# Handoff — design-system foundations

## State

18 commits on `master`, **none pushed**. Working tree clean. A local server
serves the repo at `http://localhost:8080` (restart with
`python3 -m http.server 8080` from the repo root).

The two most recent commits close what were open decisions 1 and 2, and settle
3 by finding it stale. What still needs Shamsi is under **Still open**.

## What was built

**A foundation.** The system had 91 components and no `body`, headings,
container, code or table styling, so every docs page invented its own.
`.ds-page` / `.ds-container` now provide it, scoped so a legacy page can link
the stylesheet safely.

**Spacing as a system.** Named rhythm — `--ds-space-tight` / `--ds-space-block` /
`--ds-space-section` — where a page names the *kind of break*, never a pixel.
Containers own the space between regions; elements own prose flow. Scale in
rem so it moves with the reader's text size.

**Gap.** No separate scale: gap uses the rhythm on either axis. One addition,
`--ds-gap-glyph` (0.5em), for the space between a glyph and its label inside a
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

## Settled since

1. **The close button — done.** One `.ds-close`, on both stylesheets. Text tier
   (Shamsi's call), Lucide `x` rather than `×`, `color: inherit` so one rule
   serves four alert palettes and dark chrome, 32×32 where two of the four
   predecessors were under the target-size floor, and a required `.is-sr-only`
   name. Hosts supply position only. `.is-sr-only` had to be added to the staff
   stylesheet, which documented it in an example and never defined it.
   Documented on `buttons.html`.
2. **Progressive disclosure — done.** New flagship page
   `docs/progressive-disclosure.html`: the chooser (accordion / show more /
   popover / a link, by what relationship the hidden thing has to what the
   reader is looking at), then all four accordion dressings side by side, show
   more, and the popover. `.ds-acc-flush` now takes a rule above as well as
   below, and stacks butt together into one ruled list. `.ds-show-more` promoted
   from the author-list toggle in both mockups. `organizing-content.html` keeps
   only the rail-placement rule and links out. Nav swept across 29 pages;
   AGENTS.md routing updated.
3. **The 4px header navs — nothing to fix.** `.ds-reader-header-nav` was deleted
   in `d2d2c43` with the rest of the retired reader chrome, and
   `.ds-site-header-nav` already uses `--ds-space-tight` (8px), the default. The
   only remaining 4px in that area is `.ds-site-header-divider`'s margin, which
   is a divider's breathing room and not a between-siblings gap. The item was
   stale, not a decision.

## Found, not fixed

- **The figure viewer does not return focus to the chip that opened it.**
  Pre-existing — verified against the pre-change file, identical behaviour
  before and after the modal work. The chip is `visibility: hidden` at rest and
  a hidden element cannot take focus; the mockup's `close` handler tries to
  reveal the region first and does not appear to succeed. Worth a session of
  its own, in the mockup rather than the system.

## Still open

4. **Two questions inside the close work.** `.ds-close` repeats about eight
   declarations that `.ds-btn` already has, to stay usable on the staff surface.
   And `color-mix()` is now used for its hover wash, with an `rgba` fallback
   declared first — the first use of `color-mix` in the repo, and there is no
   written browser-support floor to check it against. Worth setting one.
4b. **Settled 2026-09-08 — token naming direction.** ar5iv's styles become a
   tier 2 stylesheet inside the design system, loaded only on HTML papers pages
   and rewritten not to fight tier 1. In that world `--ds-` is the right prefix:
   `--arxiv-` would be true of every token on an all-arXiv page and so say
   nothing, while `--ds-` keeps separating the system from what is built on it.
   ar5iv defines zero `--ds-` properties, so the naming decision does not depend
   on the ar5iv conversation. Tier-1 consolidation happens **after** the rename.
   See `planning/proposals/token-naming.md`.

5. **Naming the icon-only control family** — proposal written against Primer,
   shadcn and Carbon: `planning/proposals/icon-only-controls.md`. Recommends
   `.ds-btn-icon` as a shape modifier, not a fourth tier, and recommends *not*
   renaming `.ds-btn-text` to ghost/invisible. Needs Shamsi's yes.
6. **Token unification** — the question "what are the two stylesheets" is
   answered in `planning/proposals/token-unification.md`. Headline: they share 7
   token names, but **25 more are the same value under a different name**, and
   that duplication is invisible to every check we have. It has already drifted
   once — `--ds-text-disabled` and `--ds-text-disabled` have different dark values and
   nobody decided that. The only step needing Shamsi is step 1, agreeing one
   name per concept. **Settled: `--ds-`, role-based** — see 4b below.

## Open decisions

7. **The three-tier model**, agreed but only partly built:
   - Tier 1 `design-system.css` — anything a second surface could use. **A
     modal and a toggle belong here and do not exist.** Build the modal from
     requirements (focus trap, restore focus, scroll lock, Escape) using native
     `<dialog>`; the lightbox is a poor template. The toggle needs reconciling
     with the internal one: same visual, two legitimate behaviours (a checkbox
     when it is a form setting, `aria-pressed` when it is an immediate action).
   - Tier 2 `docs/public/reader.css` — **not yet created.** Marginalia, the
     equation and figure regions, the contents bar.
   - Tier 3 — the mockup, for anything still moving.
8. **Internal is two axes, not one.** 57 internal-only classes are genuinely
   tier 2. But 22 (`.ds-alert*`, `.ds-tag*`, `.ds-field`, `.ds-input`,
   `.ds-label`, `.ds-check`) are the same component in a different palette and
   want token re-pointing, like `.ds-site-header--light`. Access Lime as
   primary is a **token** decision, not a stylesheet one.
   Deeper: the two stylesheets share **7 of ~60 token names** — internal says
   `--ds-canvas`, `--ds-text-muted`, `--ds-danger`; public says `--ds-canvas`,
   `--ds-text-muted`, `--ds-error-border`. One name per thing, broken
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
