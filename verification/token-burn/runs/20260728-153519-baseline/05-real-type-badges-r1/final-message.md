All references look correct. Here is a summary of what was built and every design-system rule applied:

---

## What was built

**`design-patterns/internal/type-badge-styles.html`** — a dedicated reference page for arXiv's submission type badges, following the exact structure and conventions of the existing internal pattern pages (`alert-styles.html`, `table-styles.html`).

### Content sections

1. **Variants (isolated)** — all four badges shown on a white demo surface and on the production Warm Wash (`#f9f7f7`) background, each labeled with its class name.
2. **In context — moderation queue** — two realistic `.ds-table` demos: a 6-row queue using all four badge types with a `.ds-filter` type-filter toolbar, and a second table showing a paper that has both a New and a Cross row (the common pattern for a cross-listed submission).
3. **Color tokens** — a table documenting every hex value (background, border, text) and verified WCAG contrast ratio for each badge, matching the values already in `design-system.css`.
4. **Typography and shape** — shows the badge sitting next to body text and a monospace identifier; explains the Plex Mono choice.
5. **HTML usage** — a dark code block with the markup pattern and a screen-reader expansion example.

### Badge CSS reused (not invented)

The CSS was already complete in `design-system.css` lines 626–674. The page only references those classes:
- `.type-new` — `#d4e9ff` bg / `#1a3d78` text / `#93c5fd` border — **8.5:1 AAA**
- `.type-rep` — `#fef3c7` bg / `#7a5c00` text / `#fde68a` border — **5.6:1 AA**
- `.type-wdr` — `#474340` bg / `#ffffff` text / `#474340` border — **9.8:1 AAA**
- `.type-cross` — `#e8e4df` bg / `#4a4540` text / `#cbc5be` border — **7.5:1 AAA**

### Design-system rules applied

| Rule | How applied |
|---|---|
| `data-theme="light"` lock | Set on `<html>` — badge dark-mode tokens don't exist yet; locking prevents broken states |
| Internal-tools surface | Page background is Warm Wash `#f9f7f7`; Access Lime `#c4d82e` used only for the page-header underline and callout accent (consistent with every other internal page) |
| WCAG 1.4.1 — color alone | Documented explicitly: text label is the primary signal, color is redundant |
| WCAG contrast floor 4.5:1 | All four badge text/bg pairings verified; lowest is Rep at 5.6:1 (AA) |
| `.ds-table` + `.ds-filter` | Used exactly as documented in `table-styles.html`; filter includes mandatory "All" option per DESIGN-POLICIES.md |
| Spacing scale | Demo padding uses 16px and 24px (on the 4px/8pt grid); section gaps 60px |
| No new badge types | Enforced by callout; directed future additions to `design-system.css` with contrast verification |
| No external fonts | No Google Fonts loaded; body uses `system-ui` stack; badge font falls through to system monospace (following `alert-styles.html` precedent) |
| Docs-nav | Exact same markup and links as every other page in `design-patterns/internal/` |