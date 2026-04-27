# Design Policies

Hard constraints for all arXiv frontend work. These are non-negotiable rules, not suggestions. Verify compliance before submitting changes.

---

## Accessibility (WCAG 2.0 AA)

- **Text contrast:** 4.5:1 minimum for normal text, 3:1 for large text (18px+ regular or 14px+ bold)
- **UI component contrast:** 3:1 minimum for interactive boundaries (borders, outlines, tracks) against their background
- **Focus indicators:** All interactive elements must have a visible focus ring on keyboard navigation. Use `:focus-visible` (not `:focus`) to avoid showing rings on mouse click
- **Labels:** Every form input must have an associated `<label>` (visible or `sr-only`). Use `aria-label` when a visible label is impractical
- **Required fields:** Mark with a visible indicator (red asterisk via `.field-required`) AND `required` + `aria-required="true"` attributes
- **Validation errors:** Link error messages to their field with `aria-describedby`
- **Color alone:** Never use color as the sole means of conveying information (WCAG 1.4.1). Always provide a secondary cue (text, icon, position change)
- **Link underlines:** Inline links in body text must be underlined. Standalone navigation links may omit underlines

## Design tokens

- **Use the palette.** All colors must come from `design-system.css` `:root` tokens. Do not introduce one-off hex values
- **Warm grey ladder:** The palette provides specific stops for specific contrast needs:
  - `--grey-dis` (`#b0aba6`) — disabled/exempt states only (2.24:1, below AA thresholds)
  - `--grey-ui` (`#8b8680`) — interactive UI boundaries: borders, tracks, arrows (3.61:1 on white, passes 3:1)
  - `--grey` (`#6b6459`) — body-weight text, muted labels (5.83:1 on white, passes 4.5:1)
- **Semantic colors:** Use danger tokens (`--danger`) only for destructive actions. Use lime/secondary tokens for positive/constructive states

## Components

- **New patterns:** If a UI element appears in two or more mockups, extract it into `design-system.css` and create or update a pattern page in `design-patterns/`
- **Platform independence:** Components use plain CSS custom properties — no Sass, no CSS-in-JS, no framework-specific syntax. This allows consumption from React, Jinja, PHP, or static HTML
- **Naming:** Use `.ds-` prefix for shared design system classes (e.g., `.ds-table`, `.ds-filter`). Mockup-specific styles stay in the mockup's own `<style>` block or stylesheet

## Content and interaction

- **Submission type badges:** Use the established palette: `.type-new` (blue), `.type-rep` (yellow), `.type-wdr` (dark), `.type-cross` (light grey)
- **Segmented controls:** Use semantic variants — `.seg-positive` (green/accept), `.seg-neutral` (blue/informational), `.seg-negative` (red/reject)
- **Filter dropdowns:** Use `.ds-filter` with a visible `<label>`. Always include an "All" option as the inclusive default

---

*These policies will expand as UX research and production requirements are incorporated. When a policy conflicts with a mockup's current implementation, the policy wins — update the mockup.*
