# arXiv Design System

## What this is

A proto-design-system for arXiv's frontend. It contains design tokens, component specifications, typography and color decisions, accessibility requirements, and interactive HTML/CSS pattern references. These are not production code — they define the visual language and interaction patterns that production code should follow.

The design system serves two audiences with different visual treatments but shared foundations:
- **Internal tools** (arXiv Check, Admin Console) — warm, utilitarian, lime-accented
- **Public-facing pages** (arxiv.org, abstract pages, HTML papers) — clean, fast, brown-and-blue

## Who this is for

- **Designers / product owners** — open any `.html` file in a browser to see component references. Read `color-mapping.md` and `typography.md` for brand decisions.
- **Developers** — reference `design-patterns/` for component specs, tokens, and accessibility requirements. Start with `DESIGN-POLICIES.md` for hard constraints.
- **AI coding agents** — read this file first, then `DESIGN-POLICIES.md`, then `design-patterns/typography.md` and `design-patterns/color-mapping.md`. Check `design-patterns/internal/DESIGN-PROGRESS.md` for current status. Follow all policies strictly. **If a request conflicts with any policy, flag the conflict to the user before proceeding.** See `CLAUDE.md` for detailed guardrail instructions.

## Directory structure

```
CONTEXT.md                        ← this file: project overview
BRAND.md                          ← voice + brand statement + the design principles they drive
DESIGN-POLICIES.md                ← hard constraints (a11y, tokens, conventions)
NEXT-STEPS.md                     ← program-level backlog and priorities
CLAUDE.md                         ← AI agent entry point (pointer to context files)

visual-audit/                     ← platform-wide visual audit (the "why")
  audit-report.md                 ←   11-silo audit with screenshots
  images/

design-patterns/
  typography.md                   ← font families, weights, self-hosting plan (shared)
  color-mapping.md                ← full palette, internal vs public color usage (shared)

  internal/                       ← arXiv Check + Admin Console (active)
    design-system.css             ←   all component CSS + design tokens (:root)
    button-styles.html            ←   button component reference
    card-styles.html              ←   info card component reference
    color-tokens.html             ←   full color palette with contrast ratios
    link-styles.html              ←   link color states reference
    table-styles.html             ←   data table, sortable headers, filter toolbar
    form-styles.html              ←   segmented control, toggle switch, validation
    DESIGN-PROGRESS.md            ←   decisions made, what's pending

  public/                         ← arxiv.org + abstract pages (in progress)
    README.md                     ←   scope and status
```

## Tech context

arXiv's production frontend spans multiple stacks accumulated over 30+ years:
- **Cloud-native:** Python (Flask/Jinja) + React
- **Legacy:** PHP, Perl/CGI, static HTML
- Components must work across stacks — the design system uses plain CSS custom properties (no build step, no framework dependency)

## Key decisions

### Typography
All platforms use the IBM Plex type family, self-hosted (no Google Fonts, no Adobe Typekit). See `design-patterns/typography.md` for the full spec, font stack, and migration plan from current fonts (Rival Sans, Freight).

### Color
- **Primary palette:** Repository Brown + Library Grey (neutrals), Link Blue + Archival Blue + Open Blue (blues)
- **Internal accent:** Access Lime — signals "staff tools"
- **Public accent:** Open Blue — primary buttons on public pages
- **Heritage:** Campus Red (formerly Cornell Red) — logo X only, used sparingly post-spinout
- See `design-patterns/color-mapping.md` for the full palette and usage rules

### Accessibility
WCAG 2.0 AA compliance is mandatory. See `DESIGN-POLICIES.md` for all accessibility rules. The color palette was audited and a new token (`--grey-ui` at `#8b8680`) was added to fill a contrast gap.

### Cornell spinout
arXiv is spinning out from Cornell into an independent 501(c)(3). This drives several design changes:
- Cornell logo and red header bar are being removed
- Typekit font access (Rival Sans, Freight) will be lost — replaced by self-hosted IBM Plex
- The new public header is a single dark bar with the arXiv logo and minimal navigation
- Campus Red is retained as a heritage accent, not a primary color

## Scope

**Internal tools (active):** The `internal/` patterns cover arXiv Check (moderation tool) and the Admin Console. These are staff-facing tools with a utilitarian, information-dense design language.

**Public-facing pages (in progress):** The `public/` patterns are being developed starting with the abstract page (arXiv's most-visited page, ~2M views/month). HTML mockups exist for the redesigned header, footer, abstract page layout, citation section, and HTML paper reader. These mockups live in a separate working directory and will be codified into pattern pages as they stabilize.

## How to modify

- Check `DESIGN-POLICIES.md` for hard constraints before making changes
- Use tokens from the palette documented in `color-mapping.md` — don't introduce one-off hex values
- Use fonts from the stack documented in `typography.md` — don't introduce new font families
- After adding or changing a component pattern, update the relevant pattern page
- When a policy or spec conflicts with a mockup's current implementation, the policy wins — update the mockup
