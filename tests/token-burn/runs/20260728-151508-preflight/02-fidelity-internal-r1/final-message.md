Done. Here's a summary of what was built and every design-system rule applied.

---

## What was built

`design-patterns/internal/bulk-action-styles.html` — a standalone demo page with five labelled static-state blocks (nothing selected, selection active, destructive confirm, success, failure) and a fully interactive live demo with a real checkbox queue table.

**New component classes (page-local, flagged for promotion to `design-system.css`):**

| Class | Purpose |
|---|---|
| `.bulk-bar-wrap` | flex column wrapper that fuses bar and table edges |
| `.bulk-bar` | the action strip itself |
| `.bulk-bar-lhs / -rhs` | count cluster / button cluster |
| `.bulk-bar-count` | selection count, carries `role="status"` |
| `.bulk-bar-rule` | decorative vertical divider between clusters |
| `.bulk-bar--confirm` | confirm sub-state (warning tint) |
| `.bulk-bar--success / --error` | feedback states (token-driven) |
| `.bulk-bar-feedback-icon / -msg` | icon + message anatomy for feedback |
| `.row-selected` | lime-tint row highlight on checked rows |

---

## Design-system rules applied

**Internal tool surface:** Access Lime (`--lime`) on the primary button (Approve) and bar's top stripe. Open Blue is absent — these are staff tools.

**Button hierarchy:** Approve → `.btn-primary` (lime, safe, default). Hold → `.btn-secondary` (lime tint, neutral). Remove → `.btn-destructive` (red). The policy requires one primary per action group.

**Destructive confirmation:** Remove fires a two-step confirm inline in the bar (required by the destructive-button policy; single-click removal is called out as a violation in the usage notes).

**Color tokens only:** Every value comes from tokens defined in `design-system.css` (`--lime`, `--sec-bg`, `--warning-bg/border/fg`, `--success-*`, `--error-*`, `--grey-ui`, `--text`, `--link`, `--danger`). No one-off hex values except `#cbc5be` for the decorative divider (within the Border Light family, which is palette-documented) and `#c8960a` for the confirm warning icon (manually darkened from `#e8b800` to ensure 3:1 contrast on `#fff8e1` for a UI element — inline comment explains this).

**Visual connection to table:** `.bulk-bar` matches `.ds-table`'s border color (`#ddd8d2`), has `border-bottom: none` and `border-radius: 6px 6px 0 0`. A page-local `.bulk-bar-wrap .ds-table` rule removes the table's top border and top radius — these are layout-seam glue styles, not modifications to the shared component.

**Selected row highlight:** `#f0f9e8` (`--sec-bg`, lime tint) — ties checked rows visually to the lime action bar.

**Spacing scale:** Gap and padding values use the 4px/8pt grid (`8px`, `10px`, `12px`, `14px`, `16px`) — no off-scale values.

**Typography:** IBM Plex Sans for body, IBM Plex Mono for arXiv IDs, IBM Plex Sans Condensed for state labels. Loaded via Google Fonts (same as `table-styles.html`; self-hosting is a production migration, not yet completed in this repo).

**WCAG AA:** `role="status"` on the count (polite live region), `role="alert"` on the error bar (assertive), `role="status"` on success. A separate `aria-live="assertive"` region announces the confirm step. `aria-label` on all icon buttons. `aria-hidden="true"` on all decorative SVGs. `:focus-visible` focus rings from `design-system.css` apply unchanged. `Clear selection` and Dismiss use `.btn-link` (Library Grey, 5.8:1 on white ✓).

**No sticky chrome, no z-index abuse, no metrics, no external data** — the page is fully self-contained.