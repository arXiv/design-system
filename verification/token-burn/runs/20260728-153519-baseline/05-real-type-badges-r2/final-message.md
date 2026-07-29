The page is solid. Here's a summary of what was built and every design-system rule applied:

---

## What was built

**`design-patterns/internal/type-badge-styles.html`** — a reference page for the four submission type badges. No new CSS was added to `design-system.css`; the badge styles already existed there (lines 626–674) and are consumed, not redefined, by this page.

**The page has five sections:**
1. **Variants** — all four badges isolated with class labels and a scaled-up example
2. **In a moderation queue** — a live `.ds-table` with all four types, plus a working `.ds-filter` that hides rows and updates the footer count
3. **Inline with metadata** — badges leading a metadata line in a detail view, with `aria-label` applied
4. **Colors and contrast** — a token table populated entirely at runtime via `getComputedStyle` + WCAG luminance math (same technique as `alert-styles.html`) so it cannot drift from the stylesheet
5. **Usage** — HTML snippets and callout guidance

---

## Design-system rules applied

| Rule | Applied as |
|---|---|
| `data-theme="light"` locks light-only docs pages | On `<html>` — badges have no dark-mode overrides; dark mode is explicitly deferred (per `dark-mode-decision.md`) |
| IBM Plex fonts from Google Fonts in reference pages only | Loaded with comment noting production must self-host per DESIGN-POLICIES.md |
| Warm Wash `#f9f7f7` for page background | `body { background: #f9f7f7 }` |
| Access Lime `#c4d82e` for internal-tools accent | `border-bottom: 3px solid #c4d82e` on `.page-header` |
| Repository Brown `#1c1a17` for body text | `color: #1c1a17` on body |
| Library Grey `#6b6459` for secondary text | Section descriptions, queue count, table header text |
| UI Boundary Grey `#8b8680` for demo-sublabels | `.demo-sub` and `.badge-showcase-label` |
| Link Blue `#1565c0` via `var(--link)` for links | `.queue-id` links in the table |
| `:focus-visible` (not `:focus`) for focus rings | Docs-nav focus rule |
| No new one-off hex values | All page-chrome colors are documented palette values; all badge colors come from `design-system.css` unchanged |
| `.ds-table`, `.ds-filter`, `.hidden` from the design system | Used in the queue demo with no local overrides |
| Color is never the sole signal (WCAG 1.4.1) | Documented in callout; each badge's text label carries the meaning independently |
| `aria-hidden="true"` on probe elements | Applied on both the token-table probes and swatches |
| `aria-label` on inline badges | Shown in the inline demo and documented in the `<abbr>` callout |
| Do not invent new badge types | Callout explicitly prohibits it and directs any addition to `design-system.css` |