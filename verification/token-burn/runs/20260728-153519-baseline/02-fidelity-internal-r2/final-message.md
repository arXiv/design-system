Done. Here's a summary of what was built and every design-system rule applied.

---

## What was built

**`design-patterns/internal/bulk-action-styles.html`** — a five-state demo page for the moderation queue bulk-action bar.

**States rendered:**
1. **Idle** — bar occupies its slot with a muted hint; "select all" checkbox is disabled; table is unaffected
2. **Selection active (3 of 5)** — lime-tinted bar, count + Clear link + three action buttons, selected rows share the same lime tint, lime bottom border connects bar to table
3. **Confirm destructive** — "Remove selected" click replaces action buttons with inline "Remove 3 submissions permanently? [Confirm remove] [Cancel]" prompt; checkboxes disabled during confirmation; danger bottom border
4. **Success** — bar content replaced with success message; approved rows are gone from the table; dismiss returns to idle
5. **Failure** — error message; selection preserved (all 3 rows remain checked) so moderator can retry without re-selecting; dismiss returns to active state

**Visual connection to table:** a `.queue-block` wrapper holds both elements with a shared outer border (`1px solid #ddd8d2`, `border-radius: 6px`, `overflow: hidden`). The table surrenders its own border and radius inside the block, creating one seamless unit with no seam at the bar/table join.

---

## Design-system rules applied

| Rule | Source | How applied |
|---|---|---|
| Internal tools use **Access Lime** as primary action color | `DESIGN-POLICIES.md` — Internal vs Public | `btn-primary` (lime fill) for Approve; never Open Blue |
| **Danger Red** for destructive actions only | `DESIGN-POLICIES.md` — Colors | `btn-destructive` for Remove; `--danger` border for confirm state |
| **No off-palette hex values** | `DESIGN-POLICIES.md` — Colors | All bar state colors draw from existing `--sec-bg`, `--lime`, `--danger`, `--success-*`, `--error-*` tokens; zero new hex values |
| **4.5:1 text / 3:1 UI contrast** floors (WCAG AA) | `DESIGN-POLICIES.md` — Accessibility | Count text: `--text` on `--sec-bg` ≫ AAA. Success: `--success-fg` 6.7:1. Error: `--error-fg` 8.6:1. Confirm text: `--danger` 5.17:1 on white ✓ |
| `:focus-visible` not `:focus` | `DESIGN-POLICIES.md` — Accessibility | Dismiss button and all reused `.btn` classes use `:focus-visible` |
| **Color is never the sole signal** (WCAG 1.4.1) | `DESIGN-POLICIES.md` — Accessibility | Message states pair icon shape + text with the color change |
| **Destructive actions require a confirmation step** | `design-system.css` button usage rules | Inline confirm/cancel prompt replaces actions on first click of Remove; never fires on single click |
| **Spacing scale** (4px base / 8-pt grid) | `DESIGN-POLICIES.md` — Spacing | Bar uses `--space-2` (8px) for gap; `10px 14px` padding matches `ds-table td` |
| `prefers-reduced-motion` covers all transitions | `DESIGN-POLICIES.md` — Chrome and interaction | `@media (prefers-reduced-motion: reduce)` disables bar and dismiss transitions |
| **IBM Plex Mono** for identifiers; **IBM Plex Sans Condensed** for table headers | `typography.md` | `col-id` uses `IBM Plex Mono`; `ds-table th` already sets Condensed |
| **`font-variant-numeric: tabular-nums`** for aligned numeric columns | `typography.md` | Applied to `.col-id` and `.col-date` |
| `role="status"` (polite) for success, `role="alert"` (assertive) for error | `design-system.css` `.ds-alert` usage comment | Applied to bar in success and failure states |
| `aria-live="polite"` on dynamic selection count | WCAG 4.1.3 + `ds-alert` pattern | `<span aria-live="polite" aria-atomic="true">` on count text |
| Page-specific styles stay in the page's `<style>` block; `.ds-` prefix reserved for shared components | `DESIGN-POLICIES.md` — Components | Bulk-bar classes (`.bulk-bar`, `.queue-block`, etc.) are unprefixed page-local; all reused components (`btn`, `btn-primary`, `btn-secondary`, `btn-destructive`, `btn-link`, `btn-tertiary`, `ds-table`, `ds-table-footer`, `type-badge`, `ds-alert`) come from `design-system.css` unchanged |
| `max-width: 1080px` for data-dense internal tools | `DESIGN-POLICIES.md` — Layout and content width | Applied to `.page` container |