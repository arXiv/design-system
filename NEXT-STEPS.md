# Next Steps — Program Backlog

Program-level backlog for the design system: cross-cutting work and priorities. Component-level roadmaps live in [public/README.md](design-patterns/public/README.md) (public patterns) and [internal/DESIGN-PROGRESS.md](design-patterns/internal/DESIGN-PROGRESS.md) (internal). When an item here is really about one of those, this file points at it rather than duplicating it.

## Done

- [x] **Brand statement + voice + design implications** — [BRAND.md](BRAND.md) (2026-06-16). Wired into the reading order in CLAUDE.md and CONTEXT.md.

## Next — gating user testing of the two mockups

- [ ] **User-testing plan** for `abstract-redesign.html` and `html-redesign.html` — moderated-test script, tasks, recruitment criteria (working researchers first), what to measure.
- [x] **Created `accessibility-research-questions.md`** (2026-07-24) at `design-patterns/public/accessibility-research-questions.md`, seeded with the parked questions (G9 silent ambient indicators, the "Journal article vs Related DOI" label tension, newcomer signposting after the announcement banner retires, justify/hyphenation reconsideration — issues #6533, #5028). Add findings as testing rounds complete.
- [ ] **Lightweight decision log** for open product questions so test findings have a home: co-equal vs HTML-first (G2), DOI-replaces-arXiv-ID in citations, the citation label question, newcomer signposting.

## Foundations

- [ ] **Refine font choices** — *Family settled (2026-06-17): re-evaluated against Atkinson Hyperlegible Next / Source Sans 3 / Inter / Public Sans → stay with IBM Plex; CJK falls back to system; tabular figures + a subsetted variable build are the agreed direction. See the "Typeface re-evaluation" section in [typography.md](design-patterns/typography.md).* Still open: finalize the weight set; settle whether headings use a distinct display treatment or just Plex Sans; lock italic / 700-bold decisions; build and measure the subsetted variable woff2. Ties into the Rival Sans / Freight → self-hosted IBM Plex migration tracked in DESIGN-PROGRESS.md.
- [ ] **Common tints in the color guidelines** — building on the recent tint-families / three-tier-rule / contrast-matrix work, document: (a) the named common tints and what each is for (section backgrounds, card fills, active/hover washes, alert surfaces); (b) usage scenarios for each; (c) accessible color combinations — which text/icon colors clear WCAG AA on each tint, as a ready-to-use pairing table. Update [color-mapping.md](design-patterns/color-mapping.md) and `colors.html`.

- [ ] **Build out the internal-tools color reference** — `colors.html` documents the internal palette only lightly (Access Lime + the secondary lime tint). Document the full internal palette (primary/secondary lime, lime tints, internal surfaces, internal status usage) the way the public palette is documented, on `colors.html` and in [color-mapping.md](design-patterns/color-mapping.md).
- [ ] **Modernize the internal components** — the internal styles were built first and predate the public refinements; e.g. internal buttons are still plain/flat while public buttons gained gradient/press construction and the `.on-tint` modifier. Audit `internal/design-system.css` against the public patterns and bring the internal components up to parity (buttons first).

## Components — promotion order (from the 2026-06-11 component audit)

Footer and both header variants are already promoted. Next, by frequency × drift:

- [ ] **Search input** — multiple variants in use today; standardize a shared base.
- [ ] **Form atoms** (label + input + fieldset + validation) — bridges legacy and modern; used on login, advanced search, submission.
- [ ] **Citation export panel** (BibTeX / APA / Chicago / MLA with source toggle)
- [ ] **Version display** (inline version links + `.ds-alert` warning)
- [ ] **Author list with truncation** (including the 100+ author case)
- [ ] **Labs toggle section**
- [ ] **Announcement / banner component**

## Pattern pages to build

Demo / reference `.html` pages that don't exist yet — each renders the component with its tokens, states, and accessibility notes, like the existing `button-styles.html`. Ordered by leverage. (Building a page usually means extracting its CSS into the relevant `design-system.css` at the same time.)

**Internal (arXiv Check / Admin Console)**

- [ ] **Form layout + fields** — top-aligned labels, content-matched field widths (`.w-sm` / `.w-md` / `.w-lg`), the standardized action bar, and the editable "section card" container. From the admin-console session; today it lives only in the mockup + `form-styles.html`.
- [ ] **Category editor** — lozenge rows, combo-search, drag-to-reorder (primary = first, bold), inline remove. Admin-console session, pending.
- [x] **Version display** — built: `design-patterns/version-display.html` (inline-version-links + `.ds-alert` warning across the one-version → many-versions spectrum). *Next: extract the `.versions` / `.v-current` CSS into `design-system.css`.*
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

- [x] **Spacing** — built: `design-patterns/spacing.html` (visual reference for the `--space-1`…`--space-12` scale + the proximity rule).
- [x] **Buttons (flagship page)** — built 2026-07-27: `design-patterns/buttons.html` unifies the public + internal button references (two-context rule, states, `.on-tint`, internal hierarchy, shared mechanics). The internal-parity and public-tertiary gaps are flagged on the page; detailed per-surface pages remain the deep references.
- [x] **Alerts & messaging (flagship page)** — built 2026-07-27: `design-patterns/alerts.html` (four `.ds-alert` states, announcement band, inline form errors, live token table, writing guidance).
- [x] **Organizing content (flagship page)** — built 2026-07-27: `design-patterns/organizing-content.html` (main-column vs rail placement rule, card + rail accordion variants, cards vs whitespace, popover + element pill). Accordion promoted 2026-07-28: `.ds-acc` (+ `.ds-acc-stack` / `.ds-acc-body` / `.ds-acc-rail`) is now real in `public/design-system.css` and the page renders it directly. *Still open from the version-display extraction: the `.versions` / `.v-current` inline-version-links CSS.*
- [ ] **Search input** — standardize the multiple variants in use (promotion order above).
- [ ] **Modal / dialog** — native `<dialog>` backdrop, container, footer button grouping (pending).

## Audit follow-ups

- [ ] **Interaction-state audit pass** — the 2026-06-11 audit was single-viewport/static; do a second pass triggering hover / focus / loading / disabled / error states.
- [ ] **Stale inventory cleanup** — figure lightbox, section-heading permalinks, and Expand chips are missing from the net-new component inventory.
- [ ] Reader TOC mobile fade mask → add the **half-item peek** as its primary continuation signal (small follow-up noted in PROPOSED-GUIDELINES G10).
