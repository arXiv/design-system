HTML is balanced. Here's a summary of what was built and every design-system rule applied:

---

## What was built

**`docs/internal/type-badge-styles.html`** — a reference page for the four submission type badges defined in `docs/internal/design-system.css`.

**Three sections:**

1. **Badge Palette** — all four variants in isolation, each annotated with its CSS class and a description of what the submission type means.

2. **Moderation Queue Context** — a realistic `.ds-table` with all four badge types across six rows, wired to a `.ds-filter` select that filters the visible rows by type and updates the footer count.

3. **Token Reference** — a table showing the background, text color, border, contrast ratio, and WCAG level for each badge variant. All values drawn from the CSS comment block in `design-system.css` (lines 629–674), not invented.

---

## Design-system rules applied

| Rule | Application |
|---|---|
| **Self-hosted everything** | No Google Fonts CDN link. Font stacks with system fallbacks only. (`table-styles.html` violates this; this page does not.) |
| **Light-only for now** | `<html lang="en" data-theme="light">` on the root element. |
| **Internal surface** | Access Lime `#c4d82e` used for the page-header border stripe, consistent with other internal docs pages. |
| **Palette and type stack only** | Page chrome uses only documented palette hex values (`#f9f7f7`, `#1c1a17`, `#6b6459`, `#c4d82e`, `#ddd8d2`, etc.). Badge colors are component-internal constants in `.type-*` rules — documented but not lifted for other uses. |
| **Reuse before rebuilding** | Uses `.type-badge`, `.type-new`, `.type-rep`, `.type-wdr`, `.type-cross`, `.ds-table`, `.ds-table-footer`, `.ds-table tbody tr.hidden`, `.ds-filter`, and `.info-link` — all from the existing stylesheet, no new classes added to the CSS. |
| **Color is not the sole signal (WCAG 1.4.1)** | Every badge carries a text label (New, Rep, Wdr, Cross). Documented in a callout with an explicit accessibility note. |
| **WCAG 2.1 AA floor** | All four variants exceed 4.5:1 for 11px non-bold text. Noted in the token reference with per-badge ratios and WCAG level. |
| **Pattern pages are example-first** | Rendered demo at top (Section 1), in-context demo second (Section 2), token/rationale reference below (Section 3). |
| **Rationale ≤ 3 sentences per rule** | All callouts are 2–3 sentences. |
| **`.ds-filter` always has All option** | The type filter select defaults to "All" as the inclusive option per DESIGN-POLICIES. |
| **No modifications to unrelated files** | Only `docs/internal/type-badge-styles.html` was created. |