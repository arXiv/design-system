# Next Steps — Program Backlog

Program-level backlog for the design system: cross-cutting work and priorities. Component-level roadmaps live in [public/README.md](design-patterns/public/README.md) (public patterns) and [internal/DESIGN-PROGRESS.md](design-patterns/internal/DESIGN-PROGRESS.md) (internal). When an item here is really about one of those, this file points at it rather than duplicating it.

## Done

- [x] **Brand statement + voice + design implications** — [BRAND.md](BRAND.md) (2026-06-16). Wired into the reading order in CLAUDE.md and CONTEXT.md.

## Next — gating user testing of the two mockups

- [ ] **User-testing plan** for `abstract-redesign.html` and `html-redesign.html` — moderated-test script, tasks, recruitment criteria (working researchers first), what to measure.
- [ ] **Create `accessibility-research-questions.md`** (currently referenced by G9 and the audit evaluation but missing). Seed it with the already-parked questions: G9 silent ambient indicators, the "Journal article vs Related DOI" label tension, newcomer signposting after the announcement banner retires, justify/hyphenation reconsideration (issues #6533, #5028).
- [ ] **Lightweight decision log** for open product questions so test findings have a home: co-equal vs HTML-first (G2), DOI-replaces-arXiv-ID in citations, the citation label question, newcomer signposting.

## Foundations

- [ ] **Refine font choices** — *Family settled (2026-06-17): re-evaluated against Atkinson Hyperlegible Next / Source Sans 3 / Inter / Public Sans → stay with IBM Plex; CJK falls back to system; tabular figures + a subsetted variable build are the agreed direction. See the "Typeface re-evaluation" section in [typography.md](design-patterns/typography.md).* Still open: finalize the weight set; settle whether headings use a distinct display treatment or just Plex Sans; lock italic / 700-bold decisions; build and measure the subsetted variable woff2. Ties into the Rival Sans / Freight → self-hosted IBM Plex migration tracked in DESIGN-PROGRESS.md.
- [ ] **Common tints in the color guidelines** — building on the recent tint-families / three-tier-rule / contrast-matrix work, document: (a) the named common tints and what each is for (section backgrounds, card fills, active/hover washes, alert surfaces); (b) usage scenarios for each; (c) accessible color combinations — which text/icon colors clear WCAG AA on each tint, as a ready-to-use pairing table. Update [color-mapping.md](design-patterns/color-mapping.md) and `colors.html`.

## Components — promotion order (from the 2026-06-11 component audit)

Footer and both header variants are already promoted. Next, by frequency × drift:

- [ ] **Search input** — multiple variants in use today; standardize a shared base.
- [ ] **Form atoms** (label + input + fieldset + validation) — bridges legacy and modern; used on login, advanced search, submission.
- [ ] **Citation export panel** (BibTeX / APA / Chicago / MLA with source toggle)
- [ ] **Version display** (pills + warning banner)
- [ ] **Author list with truncation** (including the 100+ author case)
- [ ] **Labs toggle section**
- [ ] **Announcement / banner component**

## Audit follow-ups

- [ ] **Interaction-state audit pass** — the 2026-06-11 audit was single-viewport/static; do a second pass triggering hover / focus / loading / disabled / error states.
- [ ] **Stale inventory cleanup** — figure lightbox, section-heading permalinks, and Expand chips are missing from the net-new component inventory.
- [ ] Reader TOC mobile fade mask → add the **half-item peek** as its primary continuation signal (small follow-up noted in PROPOSED-GUIDELINES G10).
