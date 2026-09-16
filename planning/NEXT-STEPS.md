# Next Steps — Program Backlog

Program-level backlog for the design system. **The active list is the v1 plan immediately below (agreed 2026-09-09).** Everything after the horizontal rule is the older backlog, last groomed 2026-07-28 — read it as history until it is groomed again. The 2026-07-28 phased plan was the organizing layer for that era; the detailed queues that follow it are the backlog the phases draw from. Component-level roadmaps live in [public/README.md](../docs/public/README.md) (public patterns) and [internal/DESIGN-PROGRESS.md](../docs/internal/DESIGN-PROGRESS.md) (internal). When an item here is really about one of those, this file points at it rather than duplicating it.

## The v1 plan (agreed 2026-09-09) — ACTIVE

This is the working list. Everything below the horizontal rule further down is
the older backlog, which has not been groomed since July and should be read as
history until it is.

**The exit test defines v1.** Shamsi prompts an agent to build pages from a
written spec, using the design system and **no custom CSS**. When the pages are
acceptable to both of us, the system is reviewable and v1 is done. Everything
here is either something that test will need, or something we already know it
would fail without.

**Why the order is what it is.** The sequence is forced by which files each item
touches, not by importance. Nearly every component touches
`docs/design-system.css`, so component work is serial. Every docs sweep touches
all the pattern pages, so those are serial too. The two tracks barely overlap,
and a third pile of one-off cleanups collides with nothing — which is what makes
any parallelism possible.

### Phase 0 — Decisions (Shamsi; each unblocks work downstream)

- [x] **18. A written browser-support floor.** DONE 2026-09-09 — Baseline
      "Widely available", in DESIGN-POLICIES *Browser support*, with a labelled
      exception for progressive enhancement. Audit found two features below the
      floor (`scrollbar-gutter`, `text-wrap`), both cosmetic, both now labelled
      at the point of use.
- [x] **32. The rule for serif.** DONE 2026-09-09 — it turned out to be a
      writing task, not a decision: `typography.md` and `typography.html`
      already agreed, and the code implements it. Serif italic is the annotation
      voice (arXiv speaking beside the author); upright serif is outreach only.
      DESIGN-POLICIES *Typography* now states what every face is for, as a
      positive rule rather than a prohibition, which also fixed a real
      contradiction — the policy had listed only four families and left serif
      out entirely. **Carried into #20:** test serif for figure captions.
- [x] **16. One file each, the HTML.** DONE 2026-09-09. They were not
      duplicates: `BRAND.md` held Voice and the eight design principles that
      `brand.html` lacked, and `typography.md` held the tokens, `@font-face`
      rules, hosting and fallbacks. Voice and the principles went into
      `brand.html`'s body (they are the "why" the repo routes to, not an
      appendix); the typography spec went to the bottom of `typography.html`
      under *Implementation spec*. The June 2026 typeface comparison moved to
      `planning/proposals/typeface-re-evaluation-2026-06.md` as a decision
      record. Both `.md` files deleted.

      **Found while merging:** `typography.md` documented the token names as
      `--font-body` / `--font-serif` — the pre-rename names, and `--font-math`,
      which never existed in either stylesheet. It had already drifted, which is
      the argument for the merge in one line.
- [x] **28. Ruled is the default; card and panel are gone.** DONE 2026-09-09.
      Shamsi went further than swapping: the white card is not needed at all,
      and neither is the filled panel. The evidence was that **all four
      dressings were doing one job** — of 15 card uses, 11 were "Relevant
      classes" reference blocks, as were both panel uses and two flush uses.
      Three styles, one purpose, across the docs. Now two: `.ds-acc` (ruled)
      and `.ds-acc-rail` (rules dropped, for a container that already frames
      it). 124 lines lighter, 19 markup sites migrated. New variants get added
      when a use case actually breaks the default, not before.

### Phase 1 — Parallel cleanup (subagents; disjoint files, no decisions)

- [x] **5.** DONE 2026-09-09. Four files deleted, `design-review-2026-06-11.md`
      moved to `verification/design-reviews/`. No page linked the deleted
      mockups — a prior rename had already orphaned them — so no nav sweep was
      needed. One stale comment fixed in `verification/verify-mockups.py`.
- [x] **19.** DONE 2026-09-09 — `.github/workflows/checks.yml`, on push and
      pull request. Both scripts are stdlib-only. Confirmed by reading and by
      running that `check-drift.py` exits 0 on NOTE lines and only fails on a
      real FAIL, so the expected blog-theme divergence will not redden the
      build.
- [x] **24.** DONE 2026-09-09 — three admin-console mockups now link the
      repo's own `docs/fonts.css`; verified in a browser that every `@font-face`
      resolves to `docs/fonts/*.woff2` and no request reaches Google. A stale
      comment claiming the opposite was corrected. **Left alone:**
      `mockups/public/submission-metadata/arxivstyle.css` imports Open Sans from
      Google — that file is a vendored snapshot of the legacy Submission 2.0
      CSS, not ours, and Open Sans is a family we do not host at all, so it is a
      separate decision rather than a path fix.
- [x] **26.** DONE 2026-09-09 — **all eight were legitimate; nothing was
      deleted.** The names had suggested otherwise, which is why they were
      looked at rather than judged. Now documented: field widths on
      `forms.html`, `.ds-full` with
      `.ds-container` on `organizing-content.html`, `.ds-inline-active` on
      `progressive-disclosure.html`, `.is-disabled` on `buttons.html`, and
      `.type-cross` via a four-badge legend on `internal/tables.html` —
      the whole badge family had only ever been demonstrated, never explained.
      **Undocumented classes: 8 → 0.**

      **Found, not fixed:** public and staff have two different field-width
      systems — `.ds-field--short` / `--full` against `--sm` / `--md` / `--lg`.
      One concept, two vocabularies; belongs with the tier-1 reconciliation.

      **Also found:** `.ds-container` itself is undocumented, which is a bigger
      gap than any of the eight. It belongs to #34, the consume page.

### Phase 2 — The stylesheet pass (one churn, not two)

- [x] **33.** DONE 2026-09-09. Tier 1 went from **3,154 lines (49% comments) to
      2,221 (29%)**; the staff sheet from 28% to 25%. 26 rationale essays became
      short headers naming the component, pointing at its pattern page, and
      keeping only what stops someone breaking the rule. Usage examples deleted
      — the live demo is better. **278 selectors before, 278 after**: nothing
      was lost.
- [x] **27.** DONE 2026-09-09 — 14 primitives naming the brand palette
      (Repository Brown, Library Grey, Open Blue, Link Blue, Visited Purple and
      the rest), with every semantic token pointing at one. Deliberately scoped
      to the *named* palette rather than inventing numeric names for all ~60
      incidental shades: those are not colours anyone would retune.
      **Proved a pure refactor** — 39 tokens checked in a browser across both
      themes, zero mismatches, and all 67 root tokens resolve.
      `check-contrast.py` needed teaching to follow `var()` chains, which is a
      real consequence of the layer and now handled.

### Phase 3 — Components (serial; each wants Shamsi's eye)

Simplest first, so the pattern-page rhythm is set before the harder ones.

- [x] **8f.** Rules / dividers — DONE 2026-09-09. `.ds-divider` with `--tight`,
      `--flush` and `--vertical`, documented on `organizing-content.html` beside
      the card, since both answer the same question. **The finding:** `<hr>` was
      already styled by the foundation and used nowhere, while nine docs pages
      hand-rolled table row separators out of `--ds-surface-muted` — a *surface*
      token used as a border, at 1.08:1 against the canvas. Those nine are table
      styling rather than dividers, so they belong to #15.
      `.ds-site-header-divider` is the same component on the header's own colour
      token; consolidating it is part of #20, because two mockups declare it
      locally.
- [x] **8d.** Tags, labels, flags — DONE 2026-09-09. The reconciliation is a
      table on `tags.html`: four components that are all "a bit of text in a
      small box", and what distinguishes them is what the text *is*.
      `.ds-tag` (what a thing IS), `.type-badge` (a submission's TYPE, staff
      only), `.ds-panel-label` (the label half of a pair, not a box at all),
      and the paper's inline chips (a reference marker inside a sentence, still
      page-local). Both shape questions now have written answers rather than
      being accidents.
      **The defect found:** `.type-badge` carried **24 one-off hex values**
      across four variants and two modes, none of them in `color-mapping.md`.
      Now `--ds-badge-*` tokens, with the dark mode handled by re-pointing the
      tokens rather than by a second set of class overrides — which deleted the
      four `html:not([data-theme="light"]) .type-*` rules entirely.

      **Raised by Shamsi and answered on the page:** the paper's permalink and
      figure "chips" are not tags — a tag says what something *is*, those do
      something, and anything with a verb on it is a button. They now have their
      own section on `buttons.html`, *Small actions attached to content*, with
      `tags.html` linking to it.

      **Decision waiting on Shamsi:** promote that treatment to a real class?
      It is shown on the buttons page but reproduced from the mockup, not linked
      from the stylesheet — the repo's rule is to promote when a *second* surface
      needs a pattern, and today only the HTML paper does. Suggested name
      `.ds-btn-quiet`, because "chip" means a filter or a selection in most
      systems and importing that confusion is how this started.

      **Latent bug found in the mockup:** `.fig-chip` and `.eqn-chip` have no
      `white-space: nowrap`, so a two-word label wraps and makes the pill
      lopsided. Visible with "Alt text". Fixed in the docs demo; the mockup
      still has it — carry into #20.

      **Found, not fixed — a real asymmetry:** the staff stylesheet has **no
      `[data-theme="dark"]` mirror**. Tier 1 supports both the OS preference and
      an explicit toggle; tier 2 supports only the OS preference, so a staff tool
      cannot offer its own dark toggle. Worth deciding deliberately rather than
      inheriting.
- [x] **25.** The switch — DONE 2026-09-09, in tier 1 as `.ds-switch`, and
      **tier 2 spends exactly one line on it** (`--ds-switch-on`), which is what
      Shamsi predicted and what the accent-as-token work was for.
      Renamed from "toggle": that word already means the show/hide control here,
      and `role="switch"` is what makes a screen reader say on/off rather than
      checked. The handoff's "two behaviours" turned out to be one — the
      checkbox-versus-immediate distinction is about whether there is a Save
      step, not about markup, so it is `<input type="checkbox" role="switch">`
      either way and works with no JavaScript.
      **Two real accessibility defects found and fixed:** the staff on-track was
      `#9cb522`, giving 2.3:1 against the white thumb and 2.2:1 against the page
      — both under the 3:1 a UI component needs. It is now the darker end of the
      same accent, 4.8:1 and 4.5:1. The public default is `--ds-accent-strong`
      at 6.8:1 and 6.4:1; neither accent could be used directly, since both are
      light fills built to carry dark text.
      Also removed: three one-off hexes (`#9cb522`, `#7c7670`, `#fff`), and
      79 lines of tier 2 CSS.

      **Shamsi caught a layout bug in review:** the label went 500 → 700 on
      toggle, and a bolder face is a wider face — measured at **1.71px**, which
      shifted every control after it along the row. The label is now 600 in both
      states, matching `.ds-panel-label`, with colour carrying the state change.
      Verified at zero width delta and zero sibling shift. **General rule now in
      the stylesheet and on both pages: never signal state with anything that
      changes text metrics** — weight, size, family, letter-spacing. Colour is
      free, position is free.
- [x] **8g.** Menu and dropdown — DONE 2026-09-09. Examined, and the
      examination found more than expected.
      **Two implementations of one nav.** 15 pages carried a page-local
      `.nav-dd` / `.docs-nav` duplicate — about 15 rules each, with hardcoded
      `#1565c0`, a literal font stack and its own anchoring. All 30 pages now
      use `.ds-site-header` + `.ds-site-header-dropdown`.
      **A keyboard bug on every page:** Escape closed the menu but left focus on
      a link that was no longer visible. Fixed, and the fix returns focus only
      when it was inside the menu being closed, so Escape elsewhere does not
      steal it. Two pages (`brand.html`, `outreach/html-papers.html`) had no
      Escape handler at all.
      **Checked and correct already:** targets clear the 24px floor (32px
      trigger, 33px item), the menu does not overflow the viewport, the nav
      landmark is named, and a second trigger closes the first.
      **Documented** on `public/header.html`: why it is a disclosure and
      not `role="menu"` — an ARIA menu promises roving arrow-key focus that a
      list of links does not have.
- [x] **8b.** DONE 2026-09-09 as `.ds-pagination` — a **record stepper**, which
      is what the internal styles actually had: the ownership-requests mockup's
      Previous / Next with "Request 3 of 15". Not numbered pages; nothing at
      arXiv needs those, and a stepper answers "what is next" while page numbers
      answer "take me to item 40".
      The position is an `aria-live` region — without it a reader who cannot see
      the counter has no way to know that Next did anything. Ends disable rather
      than disappear. And the counter takes the flex slack and centres, so
      stepping 9 → 10 grows the text inward instead of shoving the buttons;
      verified stable even with a much longer label, where a `min-width` could
      not have been (the caller chooses the wording).
- [x] **10.** DONE 2026-09-09. The bar's last item is an **emphasis slot**, not
      a login link: "Log in" signed out, "Account" signed in, with
      `.ds-site-header-greeting` beside it.
      **The name truncates at 18 characters.** A name is user data of unbounded
      length in any script, and a bar that reflows on a long one breaks for
      exactly the people whose names get tested least. Both a short and a long
      name are demonstrated on the page.
      The greeting is deliberately not a link — making the name the link would
      give it the accessible name "Ada Lovelace", which says nothing about where
      it goes. Below 600px the greeting hides and Account stays.
      **Log out is deliberately not in the bar** — it belongs on the account
      page, not one mis-tap from Search. Flagging in case you disagree; it is
      the one piece I decided rather than inherited.
      Also removed the two `!important` declarations on the login link, by
      scoping through `.ds-site-header-nav` so it out-specifies the nav's own
      colour rather than shouting at it.
- [x] **12.** DONE 2026-09-09. Of the five promotion candidates recorded from
      the submission-form work, three had already landed (disabled filled
      buttons, the warning tier for fields, inline code). The two remaining are
      now in:
      **`.ds-tooltip`**, promoted from the submission mockup where it was
      already `.ds-`-named. WCAG 1.4.13 is its whole design — hoverable (the gap
      is the tooltip's own padding, not a margin), persistent (no timer),
      dismissible (Escape, without moving focus).
      **`.ds-btn-group--split`**, which is what the mockup's `.form-actions-split`
      was; `.form-rule` turned out to be `.ds-divider`, built earlier today.
      **Two bugs found while building the demo.** The tooltip showed at rest and
      Escape lost to `:hover` — both specificity, since `:hover` and
      `:focus-within` each count as a class. And my first demo nested the
      trigger inside a `<label>`, which forwards clicks to the control it names,
      so the button's clicks would have landed on the input. That rule is now
      written on the page.
- [x] **11.** DONE 2026-09-09 — the mechanical half. Two real inconsistencies
      fixed across the docs:
      **`.callout` had five different definitions on ten pages** — same intent,
      drifting values (line-height 1.6 / 1.65 / unset, margin 16 / 18, colour
      set or not). Now one definition, copied verbatim, with a marker comment
      saying so. Still page-local by policy: DESIGN-POLICIES keeps docs
      furniture out of the design system.
      **Two names for one thing** — `.section-desc` on 14 pages and
      `.ds-section-desc` on 27, where the second is real and in the stylesheet.
      Unified on the system's name and the local copies deleted.

      **Left for Shamsi, deliberately.** The `.a11y` and `.tone` guidance blocks
      exist only on `forms.html`, where their construction was carefully
      reasoned (shared tint, mono heading, Link Blue edge for requirements
      against warm grey for guidance). Extending that pair to other pages is a
      content decision about which pages *have* those two things to say — not a
      styling one, and not mine. It belongs with #13 and #14.

**Deliberately not built: 8a, member cards.** The #17 test page is the
membership dashboard, and building its component first would make the exit test
unable to fail. Left out so the test can tell us whether the system covers it.

### Phase 4 — The mockups

- [x] **20.** DONE 2026-09-11 — audit in
      `verification/audits/2026-09-10/AUDIT-PAPER-MOCKUP.md`, six findings, all
      six acted on. Five of them changed tier 1 rather than the mockup, which
      is what "read it both ways" was for. The paper mockup still rebuilds **seven** DS components under
      other names — card, popover, accordion, tag, alert, panel label, and
      `.ds-annotation` (the footnote and figure-alt marginalia re-declare it by
      hand, right treatment, wrong route) — plus 54 raw pixel gaps and 41 pixel
      font sizes across nine sizes.

      **Read this audit both ways** (Shamsi, 2026-09-09): where the page does
      not use the design system as intended, and equally where the design system
      does not support what the page needs. The second half is the more valuable
      finding and is easy to miss when the task is framed as compliance.

      **Experiment to run while here:** serif for figure captions. Serif for
      marginalia is settled and liked; captions are the plausible extension and
      want testing rather than deciding in the abstract.
- [x] **20a. DONE 2026-09-11.** Point the type-size check at the stylesheets. Found while
      auditing 20. The rule *"sizes are rem, never px"* has existed since
      2026-07-29 and has never been checked anywhere it matters. The one
      automated guard runs on `abstract-phase2.html` and reads the stylesheets
      that page loads — and that page loads none, because it carries an
      1,828-line inlined fork (item 21). So the check has never seen
      `design-system.css`, and reports green while **217 pixel font sizes** sit
      across the files that matter: 17 in tier 1, 13 in internal tools, 40 in
      the paper mockup, 92 and 55 in the two admin console mockups.

      The count in tier 1 has gone 6 → 12 → 13 → 15 → 17 since July, about two
      a day while we have been working fast. The other three typography rules on
      the same page hold perfectly — zero violations each — because they forbid
      things that feel wrong to write. Writing `font-size: 13px` is simply how
      everyone writes CSS, and a rule that asks someone to resist an ordinary
      habit does not survive on good intentions.

      Do the check **before** converting: it produces the violation list, so it
      replaces the audit rather than adding one, and it keeps the conversion
      converted. Static, in `check-policies.py`, so CI runs it without a browser.
      The two admin mockups are deferred deliberately and by name, the way
      `check-drift.py` defers the blog theme.

      **Fourth instance of one pattern** — the typed wordmark, the undefined
      token, the two names for the internal surface, and now this. A rule in
      prose with no check has a half-life of about a month here, and we are
      writing rules faster than checks.

- [x] **22.** DONE 2026-09-11. Both fixed, and both had the same shape: a
      rule that was right for a screen following the reader onto paper.
      `@media print` in tier 1 now re-points the colour tokens rather than
      overriding components, so every component prints correctly without
      knowing that it is printing — and its selector list matches the dark
      block's `:root:not([data-theme="light"])`, because otherwise it lost on
      specificity rather than on order. The paper mockup's own dark block is
      now `@media screen and (prefers-color-scheme: dark)`: that query answers
      what suits a display, and paper is not one.
      The reference band's `calc(50vw - 50%)` padding measures the sheet in
      print, so it became a wide empty margin with the tint running off both
      edges. Zeroed, in the block that had to be beaten rather than an earlier
      one. **Four harness checks added**, light and dark.
- [x] **23.** DONE 2026-09-11 — already fixed in the page, never verified.
      The `close` handler restores focus for every exit path and reveals the
      chip region first, since a `visibility: hidden` element cannot take
      focus. Tested end to end: Expand &rarr; dialog opens on Close &rarr;
      Escape &rarr; focus lands back on the Expand chip. **Now a harness
      check**, so the next refactor cannot quietly lose it.
- [x] **21.** DONE 2026-09-11. It was worse than "vendors a copy": the page
      linked **no stylesheet at all** and carried an 1,828-line inlined fork,
      including a `:root` block declaring 22 tokens that were every one a copy
      of the canonical value. That fork is also why the type-size check
      reported green for six weeks (see 20a) — it ran on this page and read
      the stylesheets this page loads, which were none.
      Now links `fonts.css` and `design-system.css`, with the token copy, six
      exactly-duplicated component rules and the vendored `.ds-panel-label`
      deleted, and four hardcoded values pointed back at the tokens that
      already held them. Verified pixel-identical before and after.
- [x] **7.** DONE 2026-09-11, and it turned into a measurement rather than a
      piece of writing. Two criteria, and they fail differently: **text-only
      zoom** (1.4.4) breaks controls with fixed boxes, **page zoom** (1.4.10)
      breaks full-bleed bands measured in `vw`. Passing one says nothing about
      the other, which is why the rule now says to test both. Both are in
      DESIGN-POLICIES, together with the rule never to size a full-bleed band
      in viewport units.

      Measured, at 1280px:

      | | 200% text | 400% page zoom |
      |---|---|---|
      | abstract | 0px overflow | 0px overflow |
      | reader   | **466px overflow** | 0px overflow |

      The abstract is asserted in the harness. **The reader fails text-only
      zoom and the cause is structural**: ar5iv makes `<body>` a five-column
      grid whose columns are sized by content, so at double text the grid is
      1746px wide inside a 1280px viewport and every full-width row goes with
      it. The same grid gives an 18px overhang at ordinary text size, because
      `100vw` includes the scrollbar. Neither is fixable without restructuring
      `article.ltx_document` onto `.ds-container` — **item 30, parked, Deyan's
      to start**. Not asserted in the harness, because a check that is red by
      design stops being read.

### Phase 5 — The docs sweep (serial)

- [ ] **14.** Apply the forms.html page organisation to every docs page; rename
      "Form demo" to "Demo" as the generic pattern.
- [ ] **15.** Consistent use of the design system across all docs pages.
- [x] **34.** DONE 2026-09-16 — `docs/using.html`. Whole-page template first,
      then the internal-tools variant, then the two foundations nothing had
      explained: `.ds-page` (the body class the type stack and canvas are
      scoped to) and `.ds-container` (three grid tracks, and why that is not a
      max-width). Then the optional files, then five things that go wrong —
      each one drawn from something that actually happened here, and each now
      caught by `check-policies.py`. Linked first in the Docs menu on all 25
      pages, and a new **Start here** group at the top of `index.html` pairs it
      with DESIGN-POLICIES. `AGENTS.md` routes to it as step 0.
- [~] **13. IN PROGRESS.** Shamsi's framing, 2026-09-16: she will wordsmith
      every page herself later, so this item is **structure and deletion, not
      writing**. Two jobs.

      **Consistent sections.** Every component page takes the same spine —
      page header, Demo, Spec, Usage, Rules, Accessibility — and no page may
      use a different name for one of them. 14 headings renamed
      ("Behavior contract" → Rules, "Color tokens" → Spec, "Accessibility
      notes" → Accessibility, "Semantics & markup" → Usage). The spine is now
      in AGENTS.md. **Still to do:** reorder the spine sections to that order
      where a page has them out of sequence, and fill the gaps — 9 of 15
      component pages have no Spec section, and `internal/tables.html` has
      none of the four.

      **Delete the changelog prose.** The system is new and in use nowhere, so
      a reader needs to know what a thing *is*, not what it was. Eleven
      passages removed or rewritten across ten pages — dated decisions, "we
      rejected", "retired from body-text use", "the earlier version of this
      table". `check-policies.py` now fails on the phrasing, so it cannot come
      back.
- [x] **3.** DONE 2026-09-16. 130 anchors across 24 pages, written into the
      HTML by `verification/gen-anchors.py` rather than added at runtime — a
      real id works with JavaScript off, works for a link arriving from another
      page, and exists when the browser resolves the fragment on first load,
      none of which a `DOMContentLoaded` script can promise. Verified with JS
      disabled: `tags.html#usage` lands on the heading.
      `.ds-anchor` is the control beside each heading, and it is a **button,
      not a link**: an `<a href="#here">` inside a heading is a tab stop that
      goes nowhere the reader wanted to go, since they are already looking at
      the section. What they want is the address, so it copies it and says so.
      Its accessible name carries the section, because twelve buttons all
      called "Copy link to section" are useless in a list of controls.
      Hand-written ids are kept rather than regenerated — something already
      links to those. An id follows its heading, so `--check` (wired into
      `check-policies.py`) is what says to re-run the generator after a
      rewording. **Shamsi's wordsmithing pass will change headings; re-run it
      afterwards.**

### A decision for Shamsi, found in Phase 5

- [ ] **37. Is the spacing scale too sparse in the middle, or are the docs
      careless?** Measured 2026-09-16 across all 23 docs pages. Of the pixel
      values on spacing properties, **115 are on the scale and 265 are not**.
      The 41 on-scale *layout* values have been converted; the rest is this
      question.

      The off-scale values are not scattered — they cluster:

      | value | uses | sits between |
      |---|---|---|
      | 10px | 39 | `--ds-space-2` (8) and `--ds-space-3` (12) |
      | 6px  | 38 | `--ds-space-1` (4) and `--ds-space-2` (8) |
      | 20px | 31 | `--ds-space-4` (16) and `--ds-space-6` (24) |
      | 14px | 24 | `--ds-space-3` (12) and `--ds-space-4` (16) |
      | 28px | 18 | `--ds-space-6` (24) and `--ds-space-8` (32) |
      | 18px | 17 | `--ds-space-4` (16) and `--ds-space-6` (24) |
      | 80, 60, 52, 44, 40 | 28 | above `--ds-space-12` (48) |

      **Two readings, and they need different answers.** The small values —
      6, 10, 14 — are almost all *component-internal padding*, which
      `spacing.html` does not claim the scale is for; the scale's stated job is
      the rhythm between elements. The mid values — 18, 20, 28 — are layout
      gaps in the range the scale is meant to cover, and there are 66 of them.

      **The options.** Add the half-steps the docs keep reaching for, which
      makes the scale describe what people actually build but doubles its size
      and weakens the proximity rule that depends on steps being visibly
      different. Or keep seven steps and say plainly that component-internal
      padding is not on the scale, which is honest and leaves 66 layout values
      to round. **My reading: the second, plus one step at 20px** — it is the
      single most-used off-scale layout value and the 16→24 jump is the
      scale's widest proportional gap below 48.

### Phase 6 — Exit

- [ ] **9.** The build and audit skills. Thin routers into the docs, **not** a
      second copy of the system — if the skill explains how buttons work, the
      exit test measures the skill instead of the documentation. Tool-agnostic.
- [ ] **17.** The exit test. Build the membership-dashboard pages from
      [the written spec](specs/membership-dashboard.md) (drafted 2026-09-13
      from the two screenshots, **awaiting Shamsi's corrections**), with no
      custom CSS. Includes re-running the token-burn battery
      (**31**), which has not run since July: the harness measures regression
      against a known baseline, the new pages measure coverage of things never
      tried. **Run one page before the skills exist**, so we see what the docs
      alone produce.

### Phase 6b — Dark mode everywhere, with one toggle (added 2026-09-13, Shamsi)

- [x] **36. DONE 2026-09-16.** Dark mode on every page, public and internal,
      with the same affordance for switching. Shamsi's decision. Three pieces:

      1. **Tier 2 gets the `[data-theme="dark"]` mirror.** Tier 1 keys dark to
         both the OS query and the attribute; `internal-tools.css` has **zero**
         attribute rules, so an internal tool follows the OS and cannot be
         switched at all. That asymmetry was inherited, not decided.
      2. **A toggle component**, one affordance used identically on both
         surfaces. It belongs in tier 1 beside the switch.
      3. **The plumbing**: read the stored choice before first paint, fall back
         to the OS, write the attribute. `dark-mode.html` currently ends with
         "the system still ships no toggle UI" — that sentence is what changes.

      **One tension, recorded rather than argued.** The standing preference is
      courageous defaults and OS-level signals rather than in-product
      preference controls. A dark toggle is a preference control. It is
      defensible as the exception because the OS setting is one choice for a
      whole machine while reading is per-context — the same laptop at night in
      a bright room — and because arXiv does not control the OS of a reader on
      a shared library machine. It stays **one** control, not the first item of
      a settings page.

      **Before the exit test**, because the spec requires dark on both pages.

### Phase 7 — Rebuild the reader's structure (added 2026-09-11, Shamsi)

- [ ] **35. Restructure the paper mockup so the layout is ours.** Not a
      cleanup — a rebuild of `mockups/public/html-phase1.html`'s page
      structure, for the most usable and accessible reading page we can make,
      rather than the most we can retrofit onto what ar5iv emits.

      **The evidence.** ar5iv makes `<body>` a five-column grid whose columns
      are sized by their content. Every full-width row inherits that width, so
      at 200% text the grid is 1746px inside a 1280px viewport — 466px of
      horizontal scroll, a WCAG 1.4.4 failure — and even at ordinary text size
      it overhangs by 18px wherever `100vw` meets a scrollbar. The paper mockup
      also carries 62 `.mg-*` classes inventing the shape of a reading page,
      because the design system has no primitive for a main column with a rail
      beside it, which is the defining shape of what arXiv publishes.

      **What it should become.** `.ds-container`'s three tracks, which measure
      the element rather than the viewport, so a full-bleed band cannot
      overhang and the grid cannot be widened by its contents. The marginalia
      rail becomes a real track rather than absolute positioning against a
      containing block that has to be reasoned about. What survives the rebuild
      is the candidate for the **reader chrome** primitive the system is
      missing.

      **This does NOT wait on #30.** A mockup demonstrates what is possible,
      not what is currently practical — that is what mockups are for here. The
      mockup leads and production follows: restructuring it is how we find out
      what a papers tier 2 stylesheet should say, and it makes #30 a
      conversation about a worked example rather than about an intention.

      **Not v1-blocking.** The exit test builds the membership-dashboard pages,
      which never touch paper layout. Sequenced after v1 deliberately, so it is
      done against a finished system rather than a moving one.

### Outside the sequence

- **1.** The paper title's `max-inline-size: none` and `text-wrap: pretty`
  override ar5iv's 52rem cap and `balance`. Delete once the papers tier 2
  stylesheet exists — so blocked on #30.
- **30.** Papers tier 2 and the `ltx_` class audit. **Parked** — Deyan's
  territory; do not start without asking.
- **Dropped:** a style-ignore file for directories needing no styles (#6, no
  clear problem); the blog-theme translation pass (#29, the theme is in a state
  people are happy with and will be translated deliberately later).

---

## Done

- [x] **Brand statement + voice + design implications** — [BRAND.md](../docs/brand.html) (2026-06-16). Wired into the reading order in CLAUDE.md and README.md.
- [x] **Docs-chrome callout decision** (2026-07-28) — the older reference pages' bespoke `.callout` boxes stay as quiet page-local chrome for *neutral* usage/rationale notes (docs chrome is page-specific by policy; no `.ds-callout` promoted — production has no need for one, and most of the ~80 notes aren't advisories). Only genuine hard rules use the real `.ds-alert`: converted the destructive-confirmation rule (internal `button-styles`) and the three underline mandates (public `link-styles`, internal `color-tokens` + `link-styles`) to `.ds-alert-error`, matching the flagship-page convention (advisory = `.ds-alert-info`, prohibition = `.ds-alert-error`).
- [x] **Outreach — the third context** (2026-08-11). The blog, event and celebration mini-sites, and campaign pages became a named surface that inherits the public system and takes an enumerated list of liberties: [docs/outreach/](../docs/outreach/). Defined in DESIGN-POLICIES *Surfaces*; routed in AGENTS.md. Anti-drift rests on three rules — borrowing goes one way, never repeat a rule that applies everywhere, and a script checks the copies we cannot avoid (`verification/check-drift.py`). Shamsi's correction 2026-08-11, now written into the wording: moving a style into the shared stylesheet is about where the CSS lives, not about where the style is allowed; extending anything to arxiv.org stays a separate, explicit decision. First style through the shared-code path: `.on-dark`, the secondary-button variant for committed color panels, lifted from the blog masthead's ghost button — shared CSS, still outreach-only in practice.
- [x] **Text button — the quiet tier** (2026-08-11). `.ds-btn-text`: Link Blue, no fill, no border, no shadow, never underlined, hover is a background wash. An outline-only tertiary was considered and **rejected** — the public secondary is already white-fill-plus-border, so on a white canvas the two would differ by a drop shadow alone. Written down as a general rule: each surface reaches its quiet tier by removing whatever its secondary uses to hold the page, which is why internal `.btn-tertiary` (drops the fill, keeps a border) and public `.ds-btn-text` (drops the border, keeps no fill) look nothing alike and both are correct.
- [x] **Docs pages locked to light** (2026-07-28) — the 13 light-only docs pages carry `<html data-theme="light">`; the 7 deliberate dark-preview pages stay unlocked. Recorded in [dark-mode-decision.md](dark-mode-decision.md).

## The plan — three phases (2026-07-28)

Sequencing rationale: (1) measure token burn *before* reorganizing files, so the reorg has a before/after report card; (2) land the dark-mode surface-token layer *before* the component build-out, so new components are born dark-aware instead of retrofitted.

### Phase 1 — Measure, then move

**Testing philosophy (2026-07-28):** the design system must be **agent-agnostic** — arXiv developers use Claude (various models), Gemini, and occasionally Copilot, so a top model must never be a requirement. The baseline therefore deliberately uses a mid-tier worker model: if the docs only work with a frontier model, the docs aren't carrying the load. Model-capability deltas (same task on Sonnet vs a stronger model, run only when grading suggests a capability question) are a *diagnostic instrument*: wherever a stronger model succeeds and a weaker one fails, the docs are leaning on model inference instead of explicit, findable guidance — fix the docs until the delta shrinks. Baseline worker: Sonnet only (decided 2026-07-28).

- [x] **Token-burn test harness** — built 2026-07-28 (`verification/token-burn/`). A fixed battery of 4–6 realistic agent tasks (build a small pattern page from a spec, apply existing components to a mock request, catch a planted policy violation, "which token/color for X" Q&A), run headlessly. **Build-task outputs are real, self-contained HTML pages** written to a per-run directory, plus a generated review index that shows each output beside its prompt and metrics — so scoring is both quantitative (tokens consumed, files read, wrong-file detours, policy violations) and a designer's visual pass/flag on each page. Compare variants: current repo structure vs. a compact single-file digest (llms.txt-style) vs. a reordered reading order.
- [x] **Baseline run** — done and graded 2026-07-28: 10/10 cells, $11.28, **4 pass / 6 fail**; full write-up in [verification/token-burn/BASELINE-RESULTS.md](../verification/token-burn/BASELINE-RESULTS.md). Headline: **grades track documentation coverage/findability, not model capability** — well-documented patterns (trap guardrails, type badges) passed both reps; everything requiring unrouted pages (organizing-content, alert-styles, header-styles, version-display) or unwritten conventions failed. Key evidence for the reorg: the CLAUDE.md reading order stops before the flagship pattern pages; no "building X → read Y" routing; reference pages are training data (an agent copied the button-styles CDN icon link verbatim); dark tokens get hand-mixed into light pages because usage guidance lives outside the reading path.
- [x] **File reorganization** — done 2026-07-29 (commit 6c9f9cb; plan of record in [REORG-PLAN.md](REORG-PLAN.md)). Page-template question now has a proposal: [proposals/page-template.md](proposals/page-template.md) (first pages built to it 2026-08-06 — react to those). Capture the *decisions* from that session durably (docs + memory), not just the resulting file moves. Must address **agent-agnostic entry points**: today the reading order and guardrails live only in `CLAUDE.md`, which non-Claude agents never read — move canonical onboarding to a neutral home (e.g. `AGENTS.md`, the emerging cross-tool convention) with thin per-agent pointer files (`CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`). Also address **routing**: the preflight run showed an agent using a component without ever finding its reference page — nothing maps "I need X" to the right deep reference.
- [x] **Re-run the battery** — done + graded 2026-07-29: 6/10 designer pass (was 4/10), 0 policy flags (was 3); see [../verification/token-burn/REORG-COMPARISON.md](../verification/token-burn/REORG-COMPARISON.md). Harness stays as the regression check.
- [x] **Harness v2** — built 2026-08-06 (validated on the post-reorg run with a live text pass): monospace lab-report review chrome (harness styling must be visually distinct from design-system styles); each artifact shown side-by-side with the canonical pattern page it should match; an agent does the text-reading pass before Shamsi's visual pass; unmissable grading affordance; neutral-shell scope framing in task specs; caps on agent final-message length.
**Dev feedback received (2026-08-07)** — into round 3 and harness v3: (a) **per-cell token quota** so an overenthusiastic run can't burn unbounded (dev ask; harness feature); (b) **model-variance probe** — same task across models to measure consumption spread (dev prediction: dramatic differences; fits the capability-delta diagnostic); (c) **task-size mix** — big (whole page) AND small (add a button to an existing page) tasks; (d) don't over-optimize for tokens yet; (e) Sonnet-only re-validated. Separately: justified-text/hyphenation concern recorded in accessibility-research-questions.md §4; **permalink permanence** question recorded as §4b.
**Shamsi's review-division directive (2026-08-07):** the human review step focuses on visual anomaly-spotting only; agents take everything text- and computation-shaped — reading agent output (done, text pass), code-diff against canonical patterns, computed color-contrast checks on artifacts, spec-conformance checks (padding/radius/tokens via computed styles). Harness v3 presents results visual-first: rendered pairs, minimal prose. Partly in place (v2 side-by-side + text pass); the computed-checks agent is the main v3 build.
- [ ] **Run the repo checks automatically in GitHub.** The repo has no CI: `verification/check-drift.py` and `verification/check-contrast.py` only run when someone remembers. A small GitHub Actions workflow running both on every push (seconds of runtime, no dependencies) would flag a broken promise within a minute of any push, from any contributor or agent, on any machine. Deliberately not built yet — parked 2026-08-25.
- [ ] **Brand-metrics deliberation — parked until late September 2026.** Proposal and reasoning are on record (promise/proxy table in [proposals/brand-metrics-brainstorm.md](proposals/brand-metrics-brainstorm.md)); revisit with leadership once the new CEO has had time to settle in. Not active until then.
- [ ] **Round 3 + the digest experiment** — wait until later this week: design work in other sessions is firming up and being written into the docs; then design the next testing round (includes the rules-only digest variant that tests whether the "why" prose earns its cost). Dev feedback on FOR-DEVELOPERS.md feeds this too (collection in progress, shared 2026-07-30). *From the dev Slack thread (2026-07-30): add a **migration-shaped task** — "update an existing page to match the current look and feel" — the task shape Carly's stats work actually is; all current battery tasks build fresh. The digest experiment gains a production purpose: a compact URL-reachable digest is what agents working in OTHER arXiv repos (who never clone this one) could consume.*

**From the dev Slack thread (2026-07-30, Carly + Deyan on template reuse) — proposals pending discussion with devs, not unilateral actions:**
- [ ] **Proposal: the design system as the dependency-free UI layer.** The devs need shared look-and-feel that works in services that can't take arxiv-base (vendored template copies drift; a footer change = ~9 PRs). Our CSS is already dependency-free by policy and published at a stable URL — draft a short proposal offering tokens + component CSS (possibly + reference Jinja partials) as the "reusable everywhere, nearly no dependencies" core Deyan described. Offers, never prescribes: packaging/Flask/arxiv-base governance is theirs (Brian C preferred keeping things in base as of January).
- [ ] **Proposal: agent pointer file for other arXiv repos.** Carly's workflow (point Claude at browse's templates for "the new look and feel") makes whatever repo an agent reads the de facto design system — drift propagates. A three-line AGENTS.md-style pointer other repos could carry ("canonical look-and-feel reference: the design-system docs, not sibling services") fixes this cheaply and agent-agnostically. Draft for dev feedback alongside the layer proposal.
- [x] **Write the week's design decisions into docs** (2026-07-30): card rows = spacing never dividers + tint-is-a-signal + card/table/metadata-panel distinction → `docs/organizing-content.html`; bulk-action bar layout + selected-row lime tint + disable-don't-disappear → `docs/internal/tables.html`; AGENTS.md routing rows added. Public tint rule written from the verified example (Card Grey citation block in the merged mockup); full public tint vocabulary still with the tint-families foundations item. Full metadata-panel pattern page remains with the Wombat promotion item.
- [x] **Local mockups → GitHub — DONE 2026-07-30** *(historical record; `category-management/` was removed 2026-08-11, superseded by the category editors inside `user-page/` and `paper-details/`)* (commit f05714c; scrub verified, Shamsi approved pre-push; single-home follow-throughs applied: local folder CLAUDE.md pointer, promote-pattern skill paths, machine-map memory). Original plan: Destinations: Wombat `user-page` → `mockups/internal/user-page/` (scrub: confirmed real names/emails/IPs); `user-ownership-requests` → `mockups/internal/ownership-requests/` (scrub: confirmed real email + Cornell-range IP); `user-category-management` → `mockups/internal/category-management/` (verify pass); `arXiv Check mockups` → `mockups/internal/arxiv-check/` (review the 3 images with Shamsi first — may show real submissions); `Optin modal` → `mockups/public/optin-modal/` (verify pass; saved-production-page base). Existing repo mockups join the structure: `admin-paper-detail.html` → `mockups/internal/paper-details/` (Shamsi 2026-07-29), abstract/html/merged-reader files → `mockups/public/`, all with redirect stubs + link updates. Not publishing: dated .zip snapshots (git is the version record), `server.js` (local tool, stale path), Paper Detail local folder (already in repo), internal screenshots (reference), research folder (never). Post-migration: local CLAUDE.md becomes a pointer; update promote-pattern skill + machine-map memory (single-home). Working-tree staging only — nothing commits/pushes until Shamsi reviews the scrub replacement list.
 All four decisions approved by Shamsi: `mockups/internal/` + `mockups/public/` substructure; **mandatory scrub pass** before anything publishes (findings held and shown to Shamsi before push); the research folder never enters the repo; single-home after migration (mockups live only in the repo; `~/arxiv/design` keeps source assets only — update the promote-pattern skill paths and machine-map notes when executed). Original survey: Shamsi's local mockup work at `~/arxiv/design/arXiv-mockups/` should publish to this repo for easy sharing. Surveyed 2026-07-29: `Wombat mockups/` (4.8M), `arXiv Check mockups/` (4.1M), `Optin modal mockup/` (208K), plus a local `server.js` and a **`User and other research/` folder (109M) that must NOT publish** — research materials, possible participant data; it belongs elsewhere in `~/arxiv/research`-land. Decisions needed: (a) which mockup sets publish and where they land (`mockups/` substructure — flat today; likely `mockups/internal/` vs `mockups/public/`); (b) a **scrub pass before anything publishes** — this repo is public: check admin mockups for real user names/emails, internal URLs, anything sensitive; (c) asset weight (screenshots/images may need the gitignore treatment the audits use); (d) the single-home question — after migration, do mockups live *only* in the repo (killing the local/repo split the promote-pattern skill describes, whose paths are already stale)? Aligns with one-fact-one-home.

### Phase 2 — Foundations that pay forward

- [ ] **Dark mode, split in two.** Execute [DARK-MODE-AUDIT.md](DARK-MODE-AUDIT.md) Phase 0/1 now: agree the toggle mechanism (Decision A), add the semantic surface-token layer (§3), tokenize the hardcoded components. This is plumbing — no design decisions on a moving target. *Include the cheap baseline-driven fix: a point-of-use status note at the dark block in both stylesheets + one line in DESIGN-POLICIES ("new pages are light-only until this program resumes; never hand-pick dark token values; lock demo pages with `data-theme=\"light\"`") — baseline agents hand-mixed dark values into light pages because the rule lives only in dark-mode-decision.md.* The audit's Phase 2 (public button dark redesign, toggle UI + persistence) **stays gated** on the resume criteria in [dark-mode-decision.md](dark-mode-decision.md) (user-testing round incorporated + mockups ~80% stable).
- [x] **Documentation pages made dark-aware** (2026-08-12). Shamsi reported BRAND.md rendering wrong in dark. Root cause: there is no brand.html — it renders through `docs/doc.html`, one of seven pages that never locked to light, whose code blocks and tables held a hardcoded `#fff` under flipped text. Fixed repo-wide across four passes, each driven by a mechanical contrast scan of every page in dark: 266 chrome declarations tokenized, then link colors and inline `style=` chrome, then a bare-`<a>` rule (no page had one — prose links were browser-default blue all along), then text moved off `--ds-text-disabled`, which fails AA at 2.24:1 in light and flips darker in dark. New `--ds-canvas` token on the internal side. 19 pages unlocked. Light mode provably unchanged except two deliberate accessibility fixes, both noted in the commits. The scan also caught a regression it introduced: on-lime button labels flipped light on a light fill — the `--ds-text-on-accent` trap, now pinned.
- [ ] **Dark-mode presentation page** — flagship-style HTML page with the implementation instructions and light↔dark color-transition swatches; ships alongside Phase 0/1.
- [x] **Clicks-to-content audit — DONE 2026-08-17.** [../verification/audits/audit-clicks-to-content.md](../verification/audits/audit-clicks-to-content.md). All nineteen rows measured, twice, in one sitting through a real browser: once before accepting any cookie banner and once after. The bot-blocking that limited the first attempt was solved by driving Shamsi's own Chrome rather than an automated client. Findings that replaced the early guesses: repeat loads of the same page return identical numbers, so the volatility that prompted a median re-measure was browser state, not ad auctions; consent is what moves the privacy columns, and it moves them a long way; and three recorded ad figures did not reproduce in any state, ACM's among them. arXiv's own row improved on re-measurement — 2 third-party domains and 1 cookie for a first-time visitor. Remaining human-only work is tracked in the audit itself under "Possible future usability tests" (citation round-trip, screen-reader experience, and four unexercised controls), not here.
- [ ] **Brand & vision page** — HTML page combining [BRAND.md](../docs/brand.html) and [verification/audits/audit-brand-color.md](../verification/audits/audit-brand-color.md): origin story, brand statement + voice, the competitor color landscape and where arXiv sits in it. The page Shamsi points team members at to pick up the historical background and evaluate the brand statement on the merits.

### Phase 3 — Expansion under real demand

**Blog-side follow-ups (2026-08-11 review of arxiv-blog-theme v0.8.4)** — changes that belong in *that* repo, not this one:
- The theme's `[data-theme="dark"]` block hand-copies ~20 dark token values. The public stylesheet now ships an explicit-dark guard, so that block can be deleted and the values inherited.
- `.arxiv-btn-ghost` is superseded by `.ds-btn-secondary.on-dark`; the `.ds-btn svg` icon rule is now canonical and can come out of blog.css too.
- The theme's bundled copy of `design-system.css` is behind canonical (the drift checker reports how far). Re-copy it verbatim when convenient; nothing renders wrong today, but the gap grows.
- Deliberately **not** promoted: `--arxiv-card-sheen` (the special card's lit top edge). One consumer, so it stays blog-local until a second one needs it.
- **Tags** (formerly "lozenges"): researched 2026-08-11 → [proposals/tag-component.html](proposals/tag-component.html). We have no such component; the same idea is currently built five ways, two of them in the same file. Proposal recommends `.ds-tag` based on the blog's construction, with three prominence levels (quiet / chrome / status) and no new colors. **Decided:** the name is Tags; no lime tier (crosses the internal/public line); no info tier (it collided with chrome — fills identical in dark mode); dark contrast verified, lowest is 6.20:1. **Also decided:** mono type register; uppercase by default with `.ds-tag--keep-case` for identifiers and long labels; category names are copied never restyled (now in DESIGN-POLICIES). **Audited the real design 2026-08-11** (user-page privileges accordion + paper-details edit-metadata modal): the category-management design conflicts with none of the rules — case, mono, contrast, and non-color cues all pass — but runs three parallel implementations, two shapes (999px vs 4px), three undocumented blues (`#eef2ff`, `#d0daf5`, `#deeeff` are in no stylesheet), one 23.4px chip under the 24px floor, and no dark-mode awareness. **Nothing blocking:** build `.ds-tag` against those mockups, repoint all three, and let the category-editor pattern page document the editing affordances (remove ✕, nested source badge, drag-to-reorder, primary marker, negative variant) on top. **Native `<dialog>`** popups: the blog's phone header is now the working reference implementation for the unbuilt Modal/dialog pattern page below.

- [ ] **Blog theme (WordPress).** The live blog runs an out-of-the-box Automattic theme; replace it by customizing a minimal vanilla starter theme built for that purpose (block theme; map design-system tokens into `theme.json` + a small CSS layer; fonts self-hosted in the theme per policy). This is **system expansion, not a system test** — it will add creative styles and may change existing rules, so changes go through the mockup → decision → policy-update path. Known tension to design deliberately: the director-requested **Open Blue header** conflicts with the current public header policy (black → Repository Brown) and with Open Blue's primary-action role — explore it in a blog mockup, decide explicitly, document the variant if adopted. Imagery + iconography exploration rides with this work.
- [ ] **Brand-assets page** — *Shamsi is gathering official logo files + assets during the blog work and will add them to the repo; documenting them becomes this item's job (2026-07-30).* arXiv's special marks: logos, the X mark, smileybones, and friends; each in the needed sizes and colors, SVG + PNG, with usage notes. Static and cheap; no library machinery.
- [ ] **Icon decision** — no bespoke icon library (ongoing maintenance burden a very small team shouldn't carry). Choose one existing open icon set, self-host it, document the choice and usage rules. Resolves the outstanding violation in `internal/buttons.html` (icon font loaded from a CDN).
- [ ] **Components + form styles, as needed** — a continuous demand-driven track, not a phase. The promotion-order and pattern-pages queues below are the backlog; blog and dark-mode work pull items forward. **Forms & validation** remains the highest-leverage unbuilt flagship page and should land *after* the surface-token layer so it's dark-aware from day one.

## User testing — gates the mockups and dark-mode completion

- [ ] **User-testing plan** for `abstract-phase2.html` and `html-phase1.html` — moderated-test script, tasks, recruitment criteria (working researchers first), what to measure. (This round is also resume-criterion #1 for finishing dark mode.)
- [x] **Created `accessibility-research-questions.md`** (2026-07-24) at `docs/public/accessibility-research-questions.md`, seeded with the parked questions (G9 silent ambient indicators, the "Journal article vs Related DOI" label tension, newcomer signposting after the announcement banner retires, justify/hyphenation reconsideration — issues #6533, #5028). Add findings as testing rounds complete.
- [ ] **Lightweight decision log** for open product questions so test findings have a home: co-equal vs HTML-first (G2), DOI-replaces-arXiv-ID in citations, the citation label question, newcomer signposting.

## Foundations

- [ ] **Type open questions** (moved out of `typography.md`, 2026-09-09): do we
  need italic variants of Plex Sans — abstracts sometimes carry italic terms,
  and they are not currently loaded? And does any context need true bold (700),
  given 600 semibold is the heaviest weight in use? **Evidence arrived
  2026-09-09:** yes, apparently — two staff mockups set `font-weight: 700` in
  16 places (12 in paper-details, 4 in user-page), and the repo does not
  self-host Plex Sans 700, so those now render synthetic bold. **Resolved
  2026-09-09 by hosting everything:** all 64 Plex faces are now self-hosted, and
  Sans 700 plus Condensed 700 are activated because the staff mockups
  demonstrably use them (4 and 10 elements respectively). What remains open is
  narrower and still Shamsi's: **does the type scale sanction 700, or should the
  staff mockups come back to 600?** Both faces are live either way; this decides
  what the scale says. Weight 300 was requested by those mockups and is used
  nowhere.

  **Deferred deliberately (Shamsi, 2026-09-09):** decide weights *in context*,
  while working on real pages like the HTML paper page — not in the abstract.
  Do not put this as a standalone question again; bring it up when a page makes
  it concrete. *(Settled and not carried
  over: Plex Serif upright 400/600 are real and outreach-only, 2026-08-11; CJK
  falls back to system fonts, 2026-06-17.)*
- [ ] **Refine font choices** — *Family settled (2026-06-17): re-evaluated against Atkinson Hyperlegible Next / Source Sans 3 / Inter / Public Sans → stay with IBM Plex; CJK falls back to system; tabular figures + a subsetted variable build are the agreed direction. See the "Typeface re-evaluation" section in [typography.html](../docs/typography.html).* Still open: finalize the weight set; settle whether headings use a distinct display treatment or just Plex Sans; lock italic / 700-bold decisions; build and measure the subsetted variable woff2. Ties into the Rival Sans / Freight → self-hosted IBM Plex migration tracked in DESIGN-PROGRESS.md.
- [ ] **Common tints in the color guidelines** — building on the recent tint-families / three-tier-rule / contrast-matrix work, document: (a) the named common tints and what each is for (section backgrounds, card fills, active/hover washes, alert surfaces); (b) usage scenarios for each; (c) accessible color combinations — which text/icon colors clear WCAG AA on each tint, as a ready-to-use pairing table. Update [color-mapping.md](../docs/color-mapping.md) and `colors.html`.
- [ ] **Build out the internal-tools color reference** — `colors.html` documents the internal palette only lightly (Access Lime + the secondary lime tint). Document the full internal palette (primary/secondary lime, lime tints, internal surfaces, internal status usage) the way the public palette is documented, on `colors.html` and in [color-mapping.md](../docs/color-mapping.md).
- [ ] **Modernize the internal components** — the internal styles were built first and predate the public refinements; e.g. internal buttons are still plain/flat while public buttons gained gradient/press construction and the `.on-tint` modifier. Audit `internal/internal-tools.css` against the public patterns and bring the internal components up to parity (buttons first). *Pairs naturally with the dark-mode tokenization pass (Phase 2 above) — both touch the same hardcoded surfaces.*

## Components — promotion order (from the 2026-06-11 component audit)

The footer and the site header are promoted. Next, by frequency × drift:

- [ ] **Reader chrome** (paper header, sticky contents bar, reading indicator). The earlier `.ds-reader-header` was a single sticky bar carrying both header and TOC; the design has since split into a non-sticky header plus a separate sticky contents bar, and the mockup uses none of the promoted classes. Those 52 rules were removed rather than left to mislead — a stylesheet that describes a superseded design is worse than one with a hole. Being worked out in `mockups/public/html-phase1.html`; promote when it settles.
- [ ] **Search input** — multiple variants in use today; standardize a shared base.
- [ ] **Form atoms** (label + input + fieldset + validation) — bridges legacy and modern; used on login, advanced search, submission.
- [ ] **Citation export panel** (BibTeX / APA / Chicago / MLA with source toggle)
- [ ] **Version display** (inline version links + `.ds-alert` warning)
- [ ] **Author list with truncation** (including the 100+ author case)
- [ ] **Labs toggle section**
- [ ] **Announcement / banner component**

## Pattern pages to build

Demo / reference `.html` pages that don't exist yet — each renders the component with its tokens, states, and accessibility notes, like the existing `buttons.html`. Ordered by leverage. (Building a page usually means extracting its CSS into the relevant `design-system.css` at the same time.)

**Internal (arXiv Check / Admin Console)**

- [ ] **Wombat user-page patterns** — promote the "owned references" table treatment and "owned papers" accordion from `~/arxiv/design/arXiv-mockups/Wombat mockups/user-page/index.html` into the internal design system, and differentiate universal table styles from internal-only ones. *Surfaced by baseline grading 2026-07-28: agents built selected-row/bulk layouts with nothing to reference because these styles never made it into the guidelines.*
  **Also includes (from post-reorg grading 2026-07-29):** the **action-bar layout** — buttons + descriptive text on the left, filter dropdown on the right (the "Owned Papers" toolbar in the user-page mockup is the reference; no tint behind action buttons), and the **selected-row green tint** — adopted from an agent's test output over the mockup's untinted rows (Shamsi: "the green tint aids usability").
  **Includes the metadata panel (classified 2026-07-29, Shamsi approved):** a grid of label+value pairs describing ONE record — neither card (peers in a set) nor table (many records, compare down columns). Build as a `<dl>`. Two variants, tint as signal: **editable** (lime wash `--ds-accent-wash`, the workbench — edit affordances live here) and **reference** (warm grey wash + lime top bar — read-only system facts, lower priority). Row separation: spacing by default; faint cell rules permitted only at high density (always lighter than table dividers). Related rules decided same day: cards separate rows with spacing, never hairlines — dividers are table furniture; if spacing can't hold rows apart, the content wants to be a table. Public-side transposition (warm brown tint family) to be verified against the merged mockup's brown-tint cards before writing down.
- [ ] **Form layout + fields** — top-aligned labels, content-matched field widths (`.w-sm` / `.w-md` / `.w-lg`), the standardized action bar, and the editable "section card" container. From the admin-console session. The widths and the action bar are now on `docs/forms.html`; the category editor (reorderable lozenges, primary first, inline remove, combo-search to add) is still only in the mockup.
- [ ] **Category editor** — lozenge rows, combo-search, drag-to-reorder (primary = first, bold), inline remove. Admin-console session, pending.
- [x] **Version display** — built: `docs/version-display.html` (inline-version-links + `.ds-alert` warning across the one-version → many-versions spectrum). *Next: extract the `.versions` / `.v-current` CSS into `design-system.css`.*
- [ ] **Type badges** — `.type-new` / `.type-rep` / `.type-wdr` / `.type-cross`, referenced in DESIGN-POLICIES but never demoed.
- [ ] **Icon buttons** — constructive / destructive, light + dark variants (documented in DESIGN-PROGRESS, no dedicated page).

**Public (arxiv.org / abstract / reader)**

- [ ] **Citation export panel** — BibTeX / APA / Chicago / MLA with a source toggle.
- [ ] **Author list with truncation** — "show all N authors" disclosure + half-item peek for the 100+ case (G10).
- [ ] **Labs toggle section** — opt-in toggles; third-party-login items deprioritized.
- [ ] **Announcement / banner** — `.ds-announcement` as a standalone dismissible pattern.
- [ ] **Reader chrome family** — popover, element-pill, inline-active, annotation on one page (the G4 tint vocabulary); today only in `design-system.css`.
- [ ] **Tertiary / text-only button** — the unchecked item on `public/README.md`.

**Shared / foundations**

- [x] **Spacing** — built: `docs/spacing.html` (visual reference for the `--ds-space-1`…`--ds-space-12` scale + the proximity rule).
- [x] **Buttons (flagship page)** — built 2026-07-27: `docs/buttons.html` unifies the public + internal button references (two-context rule, states, `.on-tint`, internal hierarchy, shared mechanics). The internal-parity and public-tertiary gaps are flagged on the page; detailed per-surface pages remain the deep references.
- [x] **Alerts & messaging (flagship page)** — built 2026-07-27: `docs/alerts.html` (four `.ds-alert` states, announcement band, inline form errors, live token table, writing guidance).
- [x] **Organizing content (flagship page)** — built 2026-07-27: `docs/organizing-content.html` (main-column vs rail placement rule, card + rail accordion variants, cards vs whitespace, popover + element pill). Accordion promoted 2026-07-28: `.ds-acc` (+ `.ds-acc-stack` / `.ds-acc-body` / `.ds-acc-rail`) is now real in `docs/design-system.css` and the page renders it directly. *Still open from the version-display extraction: the `.versions` / `.v-current` inline-version-links CSS.*
- [x] **Forms & validation (flagship page)** — built 2026-08-11: [docs/forms.html](../docs/forms.html). Dark-aware from day one, as planned. The find that shaped it: *neither* stylesheet had any base field styling — both contexts hand-rolled inputs, and the public stylesheet had no form CSS at all. `.ds-field`/`.ds-label`/`.ds-input`/`.ds-hint` + `.ds-check` now exist in both, grounded in the values already agreed in the admin mockups and the blog (grey-ui border, 6px radius, 9px/11px padding). Native `<select>` arrow and native checkboxes with `accent-color` — dark-correct with nothing to maintain. Page covers the three validation moments, error-message writing, and the four-part accessibility contract.
- [ ] **Search input** — standardize the multiple variants in use (promotion order above).
- [ ] **Modal / dialog** — native `<dialog>` backdrop, container, footer button grouping (pending).

## Audit follow-ups

- [ ] **Interaction-state audit pass** — the 2026-06-11 audit was single-viewport/static; do a second pass triggering hover / focus / loading / disabled / error states.
- [ ] **Stale inventory cleanup** — figure lightbox, section-heading permalinks, and Expand chips are missing from the net-new component inventory.
- [ ] Reader TOC mobile fade mask → add the **half-item peek** as its primary continuation signal (small follow-up noted in PROPOSED-GUIDELINES G10).
