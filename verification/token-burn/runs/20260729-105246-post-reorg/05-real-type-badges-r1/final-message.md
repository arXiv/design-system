HTML is balanced. Here's what was built and every design-system rule applied:

---

## What was built

**`docs/internal/type-badge-styles.html`** — a dedicated reference page for the submission type badge pattern, organized into six sections:

1. **All Badge Types** — isolated demo of all four badges + spec table mapping each class, label text, submission type meaning, and WCAG contrast ratio
2. **In Context: Moderation Queue** — a full `.ds-table` with sortable-ready columns, all four badge types across realistic rows, plus a `.ds-filter` type selector; also a detail-panel metadata grid showing a badge alongside other fields
3. **Color Values** — token table with swatch + hex for bg/text/border of all four types, with contrast ratios
4. **Base Class Anatomy** — property-by-property breakdown of `.type-badge` with rationale
5. **Accessibility** — WCAG 1.4.1 compliance, screen reader behavior, forced-colors, abbreviation legibility, dark-mode status
6. **Usage Rules** — internal-only surface, dual-class requirement, no new types, one per row, no custom colors

**`AGENTS.md`** — routing table row for "Type badges" updated from `table-styles.html` to `type-badge-styles.html`.

---

## Design-system rules applied

- **Light-only page** — `<html lang="en" data-theme="light">` per AGENTS.md rule ("New demo pages lock light")
- **No external resources** — no Google Fonts, no CDN icons; page chrome uses `system-ui` stack; badge font falls back through system monospace (IBM Plex Mono → SF Mono → Fira Code → monospace)
- **Internal surface** — page uses Access Lime (`#c4d82e`) for the header border, matching other internal reference pages
- **Example-first** — isolated badge demo + minimal spec table appear before tokens and rationale, per AGENTS.md pattern page rule
- **Palette only** — all colors are either from `design-system.css` tokens (swatches, borders, text) or the established badge hex values; no one-off values introduced
- **WCAG 2.1 AA floor** — all four badge contrast ratios documented; `.type-rep` (lowest at 5.6:1 AA) is explicitly called out with a rationale note
- **Color not sole signal** — accessibility section explicitly addresses WCAG 1.4.1; badge text labels are the primary signal
- **Reuse before rebuilding** — uses `.ds-table`, `.ds-filter`, `.ds-table-footer` from `design-system.css` exactly as specified; no re-implementation of existing components
- **Rationale ≤ 3 sentences** — each callout and spec table rationale cell stays within this limit
- **No dark-mode values invented** — the page notes they're not yet defined and routes future work to the correct location in `design-system.css`
- **Spacing scale** — gaps use `24px` (≈`--space-6`), `12px` (≈`--space-3`), `16px` (≈`--space-4`) throughout; no off-scale values