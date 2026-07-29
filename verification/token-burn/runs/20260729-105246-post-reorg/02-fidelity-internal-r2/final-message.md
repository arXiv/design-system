Done. Here's what was built and every design-system rule applied:

---

## What was built

`docs/internal/bulk-action-styles.html` — a static demo page rendering the bulk-action bar in all four required states:

1. **Idle (nothing selected)** — bar present, all three buttons `disabled`, idle background matches the table header tone (`#f0eeec`), count says "No submissions selected"
2. **Selection active** — bar background shifts to `--sec-bg` (`#f0f9e8`, lime tint) to signal live selection, count shows "3 submissions selected", "Clear selection" affordance appears, checked rows get a lime-tint row highlight (`#f5fae8`), all buttons enabled
3. **Success** — action buttons replaced by a `.ds-alert-success` spanning the full bar, "3 submissions approved", `role="status"` for polite announcement
4. **Failure** — bar shows `.ds-alert-error` with recovery link, `role="alert"` for assertive announcement, selection preserved in table so moderator can retry

All four states sit inside a `.queue-wrapper` that provides the shared border and `border-radius: 6px` for both the bar and the table, with the bar's bottom edge connecting to the table's top border at the seam.

---

## Design-system rules applied

| Rule | How it's applied |
|---|---|
| **Internal surface — Access Lime primary** | `Approve selected` uses `.btn-primary` (lime). `btn-secondary` and `btn-destructive` carry the other two actions. Open Blue never appears. |
| **Actions disable, never disappear** | All three buttons always render in the DOM; they receive `disabled` in the idle state. |
| **Destructive action requires confirmation** | `Remove selected` uses `.btn-destructive` and carries `aria-haspopup="dialog"`. A callout documents that the production button must open a `<dialog>` before acting. |
| **Reuse before rebuilding** | Zero new chrome for alerts or buttons — `.ds-alert-success`, `.ds-alert-error`, `.ds-alert-dismiss`, `.btn-primary`, `.btn-secondary`, `.btn-destructive`, `.btn-link`, `.ds-table`, `.type-badge` are all consumed directly from `design-system.css`. |
| **Page-specific glue in the page `<style>` block** | `.bulk-bar`, `.queue-wrapper`, `.bulk-bar-alert`, `.col-check`, `.is-selected` are all page-local. Nothing was added to `design-system.css`. |
| **Light-only page** | `<html lang="en" data-theme="light">` per the AGENTS.md requirement for new demo pages. |
| **Self-hosted only — no external URLs** | Icons are inline SVG paths (Lucide geometry). No CDN links, no `@import`, no Google Fonts. |
| **Spacing scale** | `--space-3` (12 px) and `--space-4` (16 px) used for bar padding and gaps. No off-scale values. |
| **Color alone never the sole signal (WCAG 1.4.1)** | Each alert state pairs a distinct SVG icon shape (checkmark-circle vs. x-circle) with a leading word ("3 submissions approved" vs. "Action failed"). |
| **No sticky chrome, no ad-hoc z-index** | Bar is static flow. Neither is present. |
| **ARIA** | `role="status"` on success (polite), `role="alert"` on failure (assertive), `aria-hidden="true"` on all icon SVGs, `aria-label` on every checkbox, `aria-haspopup="dialog"` on the destructive button. |