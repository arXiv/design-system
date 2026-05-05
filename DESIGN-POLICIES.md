# Design Policies

Hard constraints for all arXiv frontend work — internal tools and public-facing pages. These are non-negotiable rules, not suggestions. Verify compliance before submitting changes.

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
- **Responsive design:** All pages must be usable at any screen width. Layouts should be mobile-first and degrade gracefully. No horizontal scrolling on any device.

## Typography

- **Font families:** Use only IBM Plex Sans, IBM Plex Sans Condensed, IBM Plex Mono, and STIX Two Math. See `design-patterns/typography.md` for the full spec.
- **Self-hosted:** All fonts must be self-hosted from arXiv's static assets. No external font services (Google Fonts, Adobe Typekit, CDN-hosted fonts).
- **Font display:** Use `font-display: swap` for text fonts (prioritize readability). Use `font-display: auto` for STIX Two Math (math rendering needs the correct font).
- **System fallbacks:** Every `font-family` declaration must include system fallbacks. See `typography.md` for the standard stacks.

## Design tokens

- **Canonical names.** The design system defines tokens by their semantic name (e.g., `--lime`, `--grey`, `--link`). These are the authoritative reference names used in `design-system.css`.
- **Namespace in production.** Each codebase should add a prefix appropriate to its context to avoid collisions with framework variables (e.g., `--arxiv-lime` in a React/MUI app, `$arxiv-lime` in Sass). The prefixed names should map 1:1 to the canonical names.
- **Values are the source of truth.** When in doubt, the hex values and behavior defined in `design-system.css` are authoritative. If a framework's token differs from the design system value, the design system wins.

## Colors

- **Use the palette.** All colors must come from the documented palette in `design-patterns/color-mapping.md`. Do not introduce one-off hex values.
- **Warm grey ladder:** The palette provides specific stops for specific contrast needs:
  - `--grey-dis` (`#b0aba6`) — disabled/exempt states only (2.24:1, below AA thresholds)
  - `--grey-ui` (`#8b8680`) — interactive UI boundaries: borders, tracks, arrows (3.61:1 on white, passes 3:1)
  - `--grey` (`#6b6459`) — body-weight text, muted labels (5.83:1 on white, passes 4.5:1)
- **Semantic colors:** Use danger tokens (`--danger`) only for destructive actions and error states. Not for brand accents.
- **Campus Red (`#b31b1b`):** Heritage color only. Use for the logo X mark and rare accents. Never for headers, buttons, large color fields, or text.
- **Internal vs public:** Internal tools use Access Lime as the primary button color. Public pages use Open Blue. Do not cross these — the color difference signals which context the user is in.

## Components

- **New patterns:** If a UI element appears in two or more pages, extract it into a design system CSS file and create or update a pattern page in `design-patterns/`.
- **Platform independence:** Components use plain CSS custom properties — no Sass, no CSS-in-JS, no framework-specific syntax. This allows consumption from React, Jinja, PHP, or static HTML.
- **Naming:** Use `.ds-` prefix for shared design system classes (e.g., `.ds-table`, `.ds-filter`). Page-specific styles stay in the page's own `<style>` block or stylesheet.

## Buttons

- **Border radius:** 6px for all buttons, icon buttons, and segmented controls
- **Padding:** 10px 20px for standard buttons
- **Shadow:** Subtle shadow at rest: `0 1px 2px rgba(0,0,0,0.08)`. No shadow on tertiary or text-only buttons.
- **Press effect:** All buttons use `transform: translateY(1px)` with shadow removal on `:active`
- **Transition timing:** 0.12s for background, border, color, and shadow. 0.08s for transform.
- **Disabled state:** `cursor: not-allowed`, reduced opacity. WCAG exempts disabled controls from contrast requirements.

## Content and interaction

- **Submission type badges:** Use the established palette: `.type-new` (blue), `.type-rep` (yellow), `.type-wdr` (dark), `.type-cross` (light grey)
- **Segmented controls:** Use semantic variants — `.seg-positive` (green/accept), `.seg-neutral` (blue/informational), `.seg-negative` (red/reject)
- **Filter dropdowns:** Use `.ds-filter` with a visible `<label>`. Always include an "All" option as the inclusive default.
- **Toggle switches:** Off state uses `--grey-ui`. On state uses lime green (internal) or Link Blue (public). Label text uses `--grey` (off) shifting to a darker shade (on).

## Public pages — additional policies

- **No metrics display:** arXiv does not display view counts, download counts, or citation counts on public pages. This is a core operating value — arXiv does not promote or rank papers.
- **Citation export:** Provide BibTeX (default), APA, Chicago, and MLA formats. Generate from metadata — no manual work.
- **arXiv Labs:** Labs tools that collect user data must be behind an opt-in toggle (not on by default). Labs that require login should be deprioritized in placement.
- **Header:** Single bar. Black (phase 1, spinout) transitioning to Repository Brown (phase 2). Logo, Search, Submit, Donate, Log in. No Cornell branding.
- **Footer:** Acknowledgment text (Simons Foundation, member institutions), then links: About, Help, Contact, Subscribe, Copyright, Privacy, Accessibility, Status.

---

*These policies expand as UX research and production requirements are incorporated. When a policy conflicts with a mockup's current implementation, the policy wins — update the mockup.*
