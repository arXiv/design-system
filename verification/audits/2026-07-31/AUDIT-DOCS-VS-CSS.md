# Docs-vs-reality audit — 2026-07-31

**Trigger.** The paper-details mockup shipped an alert icon with an invisible exclamation mark because the alert docs' copyable snippet omitted the Lucide stroke attributes (fixed in `c92a444` / `a486307`). This audit swept all of `docs/` for the same class of defect: documentation that teaches a form differing from what actually works, so that faithfully copying it produces broken or wrong output.

**Method.** Three parallel audit agents (umbrella pages / internal deep pages / public deep pages), each comparing every copyable snippet against the same page's rendered demos and the authoritative stylesheets, verifying class/token existence, recomputing every stated WCAG ratio, and resolving every internal link. All findings independently re-verified before fixing. Clean pages: `colors.html`, `spacing.html`, `doc.html`, `public/header-styles.html`.

**Result.** 28 findings, all fixed across three commits: `1b49c6f` (breaks-when-copied), `44c4c93` (wrong values), plus `a0dae77` (personal-data scrub found in passing).

## Findings and fixes

| # | Location | Defect | Fix |
|---|----------|--------|-----|
| 1 | public/reader-header-styles.html demos | Nav links had labels but no `.ds-nav-icon` — compact/≤700px hides labels, leaving invisible empty nav | Icons added to both demos |
| 2 | public/reader-header-styles.html | Link to `../PROPOSED-GUIDELINES.md` (nonexistent) | → `../../planning/PROPOSED-GUIDELINES.md` |
| 3 | buttons.html shared-mechanics | `var(--focus-ring)` claimed universal; public token is `--arxiv-focus-ring` — copied to public = no focus ring | Row names both tokens |
| 4 | internal/card-styles.html | Section-card spec cited `--border-light` — no such internal token; border silently never renders | Cites the real value `#ddd8d2`, notes no internal token exists |
| 5 | typography.html | `--font-math` token doesn't exist in either stylesheet | Specs the stack directly |
| 6 | version-display.html | `--font-mono` token doesn't exist | → `--arxiv-font-mono` |
| 7 | version-display.html + color-mapping.md | Spec pointer "README.md (Versions)" — section doesn't exist | Pointers corrected |
| 8 | public/footer-styles.html | `.ack-member-inline` taught as a class; defined in no canonical CSS | Described as unstyled templater hook |
| 9 | internal/color-tokens.html | "All Tokens" omits 12 alert + 7 spacing tokens that exist in the same `:root` | Scope note + links added |
| 10 | public/link-styles.html | Only public page missing `data-theme="light"` — OS-dark viewers saw dark colors in the light demo | Lock added |
| 11 | version-display.html demo | Warning alert used `role="status"` against the ds-alert contract | → `role="alert"` |
| 12 | internal/button-styles.html | `--link` documented as retired `#1f5e96` with contrast math for the wrong color | → `#1565c0`, figures recomputed |
| 13 | internal/button-styles.html | "Production focus rule" hardcoded `#1f5e96`, losing the dark-mode override | → `var(--focus-ring)` |
| 14 | internal/form-styles.html | Toggle off-track documented as `#ddd8d2` (~1.4:1 — invisible) | → `--grey-ui` `#8b8680` (3.61:1) |
| 15 | internal/table-styles.html | Unsorted arrow documented as `#b0aba6` (fails 3:1 on header bg) | → `--grey-ui` (3.12:1) |
| 16 | internal/card-styles.html | Page framed the dark charcoal palette as THE card; light palette undocumented | Light values documented as primary, dark as override |
| 17 | internal/card-styles.html | Label ratio stated ~6.4:1 (actual 8.6:1) | Corrected |
| 18 | internal/card-styles.html | Taught a no-op inline mono override on `.info-value` (already Plex Mono 12px) | Guidance + demo corrected |
| 19 | internal/link-styles.html + color-tokens.html | Dark card surface given as `#252320` (not a system color); ratios anchored to it | → `#2e2b26`, ratios 6.37 / 5.11 (AA) |
| 20 | internal/color-tokens.html | `--sec-border` dark ratio stated 4.5:1 (actual 7.5:1) | Corrected |
| 21 | buttons.html | "Universal" rest shadow `0 1px 2px`; public uses `0 1px 3px` | Row split per surface |
| 22 | buttons.html | Tertiary claimed shadow-less; internal `.btn-tertiary` inherited the `.btn` shadow (policy violation in CSS) | **CSS fixed**: `box-shadow: none` added per DESIGN-POLICIES |
| 23 | buttons.html | Disabled treatment claimed universal; public `.ds-btn` has zero `:disabled` rules | Row scoped truthfully; see open items |
| 24 | buttons.html | "Border-gradient stops pass 3:1" — rest stops compute 2.2–2.6:1 | Claim corrected (hover stops pass; rest stops decorative) |
| 25 | public/button-styles.html | Buttons stated ~85px wide; `min-width: 120px` | Corrected |
| 26 | organizing-content.html | Claimed pill fade respects `prefers-reduced-motion`; no such rule existed | **CSS fixed**: reduce rule added (after `.is-revealed` so it wins both states) |
| 27 | typography.html | "Specimen honesty" note claimed Plex not yet self-hosted (it is, via `fonts.css`) | Note updated; STIX remains the exception |
| 28 | internal/design-system.css comments | Two stale comments (toggle track `#ddd8d2`; `--grey-ui` "5.91:1 on dark", actual 4.8:1) — seeded findings 14 and 20 | Comments corrected |

Also found in passing (fixed in `a0dae77`): real personal identities in demo content — a real researcher's name + Gmail address (card-styles), a real-looking Gmail + username (button-styles), a `cornell.edu` test address (user-page mockup). Replaced with fictional identities on example domains.

## Open items (design decisions, not doc bugs)

- **Public `.ds-btn` disabled styles** don't exist; DESIGN-POLICIES specifies a disabled treatment for all buttons. Needs a decision on the public disabled fills.
- **STIX Two Math** is not self-hosted in `docs/fonts/`; specimens fall back to Cambria Math.
- Public tertiary button remains intentionally absent (on hold, separate testing).

## Lesson

The archetype repeats: rendered demos evolve, copyable snippets and prose values don't. When editing a pattern, treat the snippet, the demo, and the stylesheet as one unit — AGENTS.md already requires verifying tokens/classes exist before committing doc pages; this audit suggests also re-verifying stated *values* (ratios, px, hexes) against the stylesheet, not against older prose.
