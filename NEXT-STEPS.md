# Next Steps — Program Backlog

Program-level backlog for the design system: cross-cutting work and priorities. The phased plan below (agreed 2026-07-28) is the organizing layer; the detailed queues that follow it are the backlog the phases draw from. Component-level roadmaps live in [public/README.md](design-patterns/public/README.md) (public patterns) and [internal/DESIGN-PROGRESS.md](design-patterns/internal/DESIGN-PROGRESS.md) (internal). When an item here is really about one of those, this file points at it rather than duplicating it.

## Done

- [x] **Brand statement + voice + design implications** — [BRAND.md](BRAND.md) (2026-06-16). Wired into the reading order in CLAUDE.md and CONTEXT.md.
- [x] **Docs-chrome callout decision** (2026-07-28) — the older reference pages' bespoke `.callout` boxes stay as quiet page-local chrome for *neutral* usage/rationale notes (docs chrome is page-specific by policy; no `.ds-callout` promoted — production has no need for one, and most of the ~80 notes aren't advisories). Only genuine hard rules use the real `.ds-alert`: converted the destructive-confirmation rule (internal `button-styles`) and the three underline mandates (public `link-styles`, internal `color-tokens` + `link-styles`) to `.ds-alert-error`, matching the flagship-page convention (advisory = `.ds-alert-info`, prohibition = `.ds-alert-error`).
- [x] **Docs pages locked to light** (2026-07-28) — the 13 light-only docs pages carry `<html data-theme="light">`; the 7 deliberate dark-preview pages stay unlocked. Recorded in [dark-mode-decision.md](design-patterns/dark-mode-decision.md).

## The plan — three phases (2026-07-28)

Sequencing rationale: (1) measure token burn *before* reorganizing files, so the reorg has a before/after report card; (2) land the dark-mode surface-token layer *before* the component build-out, so new components are born dark-aware instead of retrofitted.

### Phase 1 — Measure, then move

- [ ] **Token-burn test harness.** A fixed battery of 4–6 realistic agent tasks (build a small pattern page from a spec, apply existing components to a mock request, catch a planted policy violation, "which token/color for X" Q&A), run headlessly. **Build-task outputs are real, self-contained HTML pages** written to a per-run directory, plus a generated review index that shows each output beside its prompt and metrics — so scoring is both quantitative (tokens consumed, files read, wrong-file detours, policy violations) and a designer's visual pass/flag on each page. Compare variants: current repo structure vs. a compact single-file digest (llms.txt-style) vs. a reordered reading order.
- [ ] **Baseline run** against today's structure, before anything moves.
- [ ] **File reorganization** — after a dedicated context-gathering session with Shamsi. Capture the *decisions* from that session durably (docs + memory), not just the resulting file moves.
- [ ] **Re-run the battery** — the delta is the reorg's report card. Keep the harness afterward as a regression check whenever the repo grows.

### Phase 2 — Foundations that pay forward

- [ ] **Dark mode, split in two.** Execute [DARK-MODE-AUDIT.md](design-patterns/DARK-MODE-AUDIT.md) Phase 0/1 now: agree the toggle mechanism (Decision A), add the semantic surface-token layer (§3), tokenize the hardcoded components. This is plumbing — no design decisions on a moving target. The audit's Phase 2 (public button dark redesign, toggle UI + persistence) **stays gated** on the resume criteria in [dark-mode-decision.md](design-patterns/dark-mode-decision.md) (user-testing round incorporated + mockups ~80% stable).
- [ ] **Dark-mode presentation page** — flagship-style HTML page with the implementation instructions and light↔dark color-transition swatches; ships alongside Phase 0/1.
- [ ] **Brand & vision page** — HTML page combining [BRAND.md](BRAND.md) and [audits/audit-brand-color.md](audits/audit-brand-color.md): origin story, brand statement + voice, the competitor color landscape and where arXiv sits in it. The page Shamsi points team members at to pick up the historical background and evaluate the brand statement on the merits.

### Phase 3 — Expansion under real demand

- [ ] **Blog theme (WordPress).** The live blog runs an out-of-the-box Automattic theme; replace it by customizing a minimal vanilla starter theme built for that purpose (block theme; map design-system tokens into `theme.json` + a small CSS layer; fonts self-hosted in the theme per policy). This is **system expansion, not a system test** — it will add creative styles and may change existing rules, so changes go through the mockup → decision → policy-update path. Known tension to design deliberately: the director-requested **Open Blue header** conflicts with the current public header policy (black → Repository Brown) and with Open Blue's primary-action role — explore it in a blog mockup, decide explicitly, document the variant if adopted. Imagery + iconography exploration rides with this work.
- [ ] **Brand-assets page** — arXiv's special marks: logos, the X mark, smileybones, and friends; each in the needed sizes and colors, SVG + PNG, with usage notes. Static and cheap; no library machinery.
- [ ] **Icon decision** — no bespoke icon library (ongoing maintenance burden a very small team shouldn't carry). Choose one existing open icon set, self-host it, document the choice and usage rules. Resolves the outstanding violation in `internal/button-styles.html` (icon font loaded from a CDN).
- [ ] **Components + form styles, as needed** — a continuous demand-driven track, not a phase. The promotion-order and pattern-pages queues below are the backlog; blog and dark-mode work pull items forward. **Forms & validation** remains the highest-leverage unbuilt flagship page and should land *after* the surface-token layer so it's dark-aware from day one.

## User testing — gates the mockups and dark-mode completion

- [ ] **User-testing plan** for `abstract-redesign.html` and `html-redesign.html` — moderated-test script, tasks, recruitment criteria (working researchers first), what to measure. (This round is also resume-criterion #1 for finishing dark mode.)
- [x] **Created `accessibility-research-questions.md`** (2026-07-24) at `design-patterns/public/accessibility-research-questions.md`, seeded with the parked questions (G9 silent ambient indicators, the "Journal article vs Related DOI" label tension, newcomer signposting after the announcement banner retires, justify/hyphenation reconsideration — issues #6533, #5028). Add findings as testing rounds complete.
- [ ] **Lightweight decision log** for open product questions so test findings have a home: co-equal vs HTML-first (G2), DOI-replaces-arXiv-ID in citations, the citation label question, newcomer signposting.

## Foundations

- [ ] **Refine font choices** — *Family settled (2026-06-17): re-evaluated against Atkinson Hyperlegible Next / Source Sans 3 / Inter / Public Sans → stay with IBM Plex; CJK falls back to system; tabular figures + a subsetted variable build are the agreed direction. See the "Typeface re-evaluation" section in [typography.md](design-patterns/typography.md).* Still open: finalize the weight set; settle whether headings use a distinct display treatment or just Plex Sans; lock italic / 700-bold decisions; build and measure the subsetted variable woff2. Ties into the Rival Sans / Freight → self-hosted IBM Plex migration tracked in DESIGN-PROGRESS.md.
- [ ] **Common tints in the color guidelines** — building on the recent tint-families / three-tier-rule / contrast-matrix work, document: (a) the named common tints and what each is for (section backgrounds, card fills, active/hover washes, alert surfaces); (b) usage scenarios for each; (c) accessible color combinations — which text/icon colors clear WCAG AA on each tint, as a ready-to-use pairing table. Update [color-mapping.md](design-patterns/color-mapping.md) and `colors.html`.
- [ ] **Build out the internal-tools color reference** — `colors.html` documents the internal palette only lightly (Access Lime + the secondary lime tint). Document the full internal palette (primary/secondary lime, lime tints, internal surfaces, internal status usage) the way the public palette is documented, on `colors.html` and in [color-mapping.md](design-patterns/color-mapping.md).
- [ ] **Modernize the internal components** — the internal styles were built first and predate the public refinements; e.g. internal buttons are still plain/flat while public buttons gained gradient/press construction and the `.on-tint` modifier. Audit `internal/design-system.css` against the public patterns and bring the internal components up to parity (buttons first). *Pairs naturally with the dark-mode tokenization pass (Phase 2 above) — both touch the same hardcoded surfaces.*

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
- [ ] **Forms & validation (flagship page)** — highest-leverage unbuilt flagship page; build after the surface-token layer lands (Phase 2) so it's dark-aware from day one.
- [ ] **Search input** — standardize the multiple variants in use (promotion order above).
- [ ] **Modal / dialog** — native `<dialog>` backdrop, container, footer button grouping (pending).

## Audit follow-ups

- [ ] **Interaction-state audit pass** — the 2026-06-11 audit was single-viewport/static; do a second pass triggering hover / focus / loading / disabled / error states.
- [ ] **Stale inventory cleanup** — figure lightbox, section-heading permalinks, and Expand chips are missing from the net-new component inventory.
- [ ] Reader TOC mobile fade mask → add the **half-item peek** as its primary continuation signal (small follow-up noted in PROPOSED-GUIDELINES G10).
