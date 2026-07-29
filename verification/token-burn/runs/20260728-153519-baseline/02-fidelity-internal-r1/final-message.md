`design-patterns/internal/bulk-action-styles.html` is written. Here's a full accounting of what was built and every design-system rule applied:

---

## What was built

A single demo page at `design-patterns/internal/bulk-action-styles.html` rendering the bulk action bar in five labeled states:

| Section | What it shows |
|---|---|
| Nothing selected | Bar absent; table renders alone inside the shared wrapper |
| Selection active | Bar visible with 3 selected rows, then 1 selected row |
| Destructive confirm | Bar shifts to danger tint with inline "Remove 3 submissions? / Confirm / Cancel" |
| Success | `.ds-alert-success` above a reset table; bar gone |
| Failure | `.ds-alert-error` above the bar, which remains visible with the intact selection |

### Architecture

- **`.bulk-action-wrap`** — a single border container (`border: 1px solid #ddd8d2; border-radius: 6px; overflow: hidden`) that wraps both bar and table so they read as one connected unit. The table inside strips its own border via `.bulk-action-wrap .ds-table { border: none; border-radius: 0 }`.
- **`.bulk-action-bar`** — the bar itself; shown/hidden at the DOM level (no JS in this static demo). Uses `var(--sec-bg)` lime tint with `var(--sec-border)` bottom border when in default selection state, and `var(--error-bg)` / `var(--error-border)` in the confirming state.
- **`.is-selected`** rows get `background: var(--sec-bg)` — same lime tint as the bar, creating the visual link between bar and selection.

---

## Design-system rules applied

**Internal vs public surface (DESIGN-POLICIES.md)**
- `Approve selected` → `.btn-primary` (Access Lime `#c4d82e`). Internal tool surface; Open Blue never appears.
- `Put on hold` → `.btn-secondary` (lime tint).
- `Remove selected` → `.btn-destructive` (Danger Red `#c62828`, white text 5.17:1 AA ✓).

**Destructive action confirmation (design-system.css)**
- Per the button docs: *"Always pair with a confirmation step (dialog or inline confirm)."* The confirming state replaces the action group with an inline prompt rather than a modal (appropriate since the affected rows are visible in the same view).

**Status / alert component (design-system.css `.ds-alert`)**
- Reused verbatim. Success → `.ds-alert-success` with `role="status"` (polite). Failure → `.ds-alert-error` with `role="alert"` (assertive). Each pairs the color with a distinct icon shape and leading word, satisfying WCAG 1.4.1.

**Color palette (color-mapping.md)**
- All values are palette tokens: `var(--sec-bg)`, `var(--sec-border)`, `var(--error-bg)`, `var(--error-border)`, `var(--error-fg)`, `var(--text)`, `var(--grey)`. The wrapper border uses `#ddd8d2` (Border Light), which is how `.ds-table` itself declares its border. Zero one-off hex values introduced.

**Accessibility (DESIGN-POLICIES.md)**
- `:focus-visible` (never `:focus`) — inherited from `.btn`, `.btn-link`, `.ds-alert-dismiss`.
- `aria-live="polite"` + `aria-atomic="true"` on `.bulk-count` for count updates.
- `role="toolbar"` on active bar; `role="group"` on the action cluster; `role="alert"` on the confirmation message.
- Every checkbox has an `aria-label`; the select column header has `.sr-only` text.
- Button height in the bar: `6px + 13px + 6px = 25px`, clearing the WCAG 2.5.8 24px minimum.
- Color is never the sole signal for selected rows (checkbox + background tint).
- `@media (forced-colors: active)` block degrades bar backgrounds to `Canvas` and selected rows to `Highlight`/`HighlightText`.

**Typography (typography.md)**
- IBM Plex Sans body, IBM Plex Mono for badge text (inherited from `.type-badge`), IBM Plex Sans Condensed for table headers (inherited from `.ds-table`). Loaded via Google Fonts, consistent with every other pattern page in the repo while self-hosting migration is pending.

**Spacing (DESIGN-POLICIES.md)**
- Bar padding: `10px 14px` — matches `.ds-table td` exactly, so bar and table rows feel rhythmically linked. Button gap: `var(--space-2)` (8px). Bar gap: `var(--space-3)` (12px). Status margin: `var(--space-2)`.

**Page structure**
- Follows the pattern established by `table-styles.html` and `alert-styles.html`: `docs-nav` strip, `.page-header` with lime rule, `.section` + `.demo` + `.callout` layout, page-specific CSS in the `<style>` block.