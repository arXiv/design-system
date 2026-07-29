Everything is in place. Here is a summary of what was built and every design-system rule applied:

---

## What was built

**CSS** — `docs/public/design-system.css` (lines 762–977): A new component block, `.ds-artifact-links` and parts, inserted between the Accordion and Site Footer sections.

**Demo page** — `docs/public/artifact-links-styles.html`: A reference page following the exact structure of `alert-styles.html` and `link-styles.html` — docs nav, page header, rendered demos first, then token table, then usage code and callouts.

**README** — `docs/public/README.md`: Added the new pattern to the pattern-pages checklist.

---

## Design-system rules applied

**Tokens — no one-off hex values.** Every color comes from the `--arxiv-*` token set: `--arxiv-border-light` for card/row hairlines, `--arxiv-active-bg` for hover fills, `--arxiv-ink` for all primary text, `--arxiv-grey` for secondary text and the destination name, `--arxiv-grey-ui` for the decorative off-site icon stroke, `--arxiv-link-blue` / `--arxiv-link-hover` for the overflow summary, `--arxiv-focus-ring` for the focus outline. The sole `#fff` literal is an absolute (white page background), the same idiom used by `.ds-acc`.

**Public surface, Open Blue primary.** No Access Lime appears — the artifact links card is strictly a public-side component.

**`.ds-` prefix.** All shared classes follow the `ds-artifact-links*` naming convention per DESIGN-POLICIES.md Components.

**Card shape matches `.ds-acc`.** White background, `1px solid --arxiv-border-light`, `6px border-radius`, `overflow: hidden` — identical to the accordion card construction.

**Hover = Active Wash.** `--arxiv-active-bg` (#d6e8f7) on row hover is the same token used by `.ds-toc-dropdown-link:hover`, keeping all arXiv-layer interactive rows visually unified (color-mapping.md: "arXiv Chrome family").

**Focus ring.** `outline: 3px solid var(--arxiv-focus-ring); outline-offset: -2px` — inward ring matches `.ds-acc > summary:focus-visible`. Uses `:focus-visible` not `:focus` (DESIGN-POLICIES.md Accessibility).

**Visited suppressed.** Artifact rows are navigational links, not inline body text. `:visited { color: var(--arxiv-ink) }` prevents purple bleed into the structured layout.

**Off-site signal — aria-hidden icon + sr-only text.** The `↗` SVG carries `aria-hidden="true"`; each row includes `<span class="is-sr-only">(opens in new tab)</span>`. The `is-sr-only` utility is already in the public stylesheet. This matches the footer's pattern for external links documented in the Site Footer CSS comment.

**Overflow: explicit count via `<details>`, not scroll.** DESIGN-POLICIES.md "Truncation always signals continuation" lists disclosure with explicit count as the first preference. The `<details class="ds-artifact-links-more">` + summary "4 more artifacts" follows that preference, uses no JS, gets keyboard and screen-reader semantics for free, and mirrors the `.ds-acc` `+`/`−` glyph convention.

**Overflow threshold documented.** Eight rows before disclosure: documented in the CSS comment, the demo page, and the README. The threshold keeps the card comfortable in a sidebar column without internal scroll.

**Typography.** Card title at `0.92rem / 600` — identical to `.ds-acc > summary`. Destination name uses `--arxiv-font-condensed` at `0.75rem` with `letter-spacing: 0.02em`, consistent with how the accordion uses condensed for metadata labels.

**`prefers-reduced-motion`.** Transition on `.ds-artifact-links-row` and the overflow summary is disabled. The `<details>` open/close itself has no transition — nothing else to disable.

**`forced-colors`.** Explicit overrides pin the card border to `ButtonBorder`, the icon to `ButtonText`, and the hover row to `Highlight`/`HighlightText`, so the pattern survives Windows High Contrast without relying on custom colors.

**Light-only, `data-theme="light"`.** The demo page sets `<html lang="en" data-theme="light">` per AGENTS.md. No dark-mode token overrides are added to the component — consistent with the accordion, which also ships light-only.

**Demo page structure.** Rendered demos first (states, 1-row, 8-row, 12-row with closed and open overflow pre-rendered), then token table, then usage callouts — the "example-first" pattern required by AGENTS.md.