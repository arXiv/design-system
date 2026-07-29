Done. Here's what was built and every design-system rule applied:

---

**What was built**

`docs/internal/bulk-action-styles.html` — a single demo page showing the bulk-action bar in five states across five sections, each backed by a live table for visual context:

| State | Bar modifier | Key content |
|---|---|---|
| Idle | *(none)* | 0 selected, all buttons disabled |
| Active | `.is-active` | 3 selected, count + Clear + 3 actions |
| Confirm remove | `.is-confirm` | Inline destructive confirmation |
| Success | `.is-success` | "3 submissions approved" + Dismiss |
| Error | `.is-error` | Failure message + Retry + Dismiss |

The bar and table are wrapped in `.queue-panel` (`border: 1px solid #ddd8d2; border-radius: 6px; overflow: hidden`) so they share a border, satisfying the "visually connected" requirement. The table's own `border`/`border-radius` are reset inside the panel.

---

**Design-system rules applied**

- **Internal surface / Access Lime primary** — `.btn-primary` is lime; `.btn-secondary` uses `--sec-bg`; the active bar also uses `--sec-bg` so bar and button share the same palette family. No Open Blue anywhere.
- **`data-theme="light"`** on `<html>` — new internal demo pages lock light mode per AGENTS.md.
- **No CDN resources** — no Google Fonts, no Bootstrap Icons. Icons are inline SVG; fonts use the `system-ui` fallback stack.
- **Palette only** — every color is a `var(--*)` token from `design-system.css`. No one-off hex values in the bar CSS.
- **Spacing scale** — `var(--space-2)` (8 px, button gap) and `var(--space-3)` (12 px, bar internal gap); bar padding mirrors `.ds-table th`'s `9px 14px`.
- **Reuse before rebuilding** — `.btn-primary`, `.btn-secondary`, `.btn-tertiary`, `.btn-destructive`, `.btn-link` used as-is; `.ds-table`, `.type-badge .type-*` used as-is; success/error token families (`--success-bg/border/fg`, `--error-bg/border/fg`) reused directly (same source as `.ds-alert-success/error`).
- **Destructive action confirmation** — "Remove selected" shows an inline confirm step before executing, per the design-system.css comment: *"Always pair with a confirmation step (dialog or inline confirm)."*
- **Actions disable, they don't disappear** — idle state shows all three buttons with `:disabled`, not hidden.
- **WCAG 1.4.1 — color not the sole signal** — each state pairs a distinct icon shape (checkmark polyline / warning triangle / X-circle) with a leading word ("approved" / "Action failed") alongside the color.
- **`role` + `aria-live` pairing** — `role="status"` / `aria-live="polite"` for success; `role="alert"` / `aria-live="assertive"` for error and confirm, matching `.ds-alert` usage documented in `design-system.css`.
- **Focus indicators** — all button states get `:focus-visible` rings via the base `.btn` and `.btn-link` rules already in `design-system.css`.
- **Target size floor** — `min-height: 44px` on `.bulk-bar` satisfies WCAG 2.2 SC 2.5.8 (24 px hard floor, 44 px design target on touch surfaces).
- **`max-width: 1080px`** — correct for a data-dense internal tool per DESIGN-POLICIES.md.
- **Page-specific glue in `<style>` block** — bar layout, state modifiers, and the `.queue-panel` wrapper are all page-scoped per AGENTS.md convention.