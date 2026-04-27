# arXiv Design System

## What this is

A proto-design-system for arXiv's frontend. It contains design tokens, component specifications, accessibility requirements, and interactive HTML/CSS pattern references. These are not production code — they define the visual language and interaction patterns that production code should follow.

The design system is being built incrementally, starting with arXiv's internal tools (arXiv Check and the Admin Console) and expanding to public-facing pages (arxiv.org, abstract pages) in a future phase.

## Who this is for

- **Designers / product owners** — open any `.html` file in a browser to see the component reference
- **Developers** — reference `design-patterns/internal/` for component specs, tokens, and accessibility requirements
- **AI agents** — read this file, then `DESIGN-POLICIES.md`, then `design-patterns/internal/DESIGN-PROGRESS.md` before making changes

## Directory structure

```
CONTEXT.md                        ← this file: project overview
DESIGN-POLICIES.md                ← hard constraints (a11y, tokens, conventions)
CLAUDE.md                         ← AI agent entry point (pointer to context files)

visual-audit/                     ← platform-wide visual audit (the "why")
  audit-report.md                 ←   11-silo audit with screenshots
  images/

design-patterns/
  internal/                       ← arXiv Check + Admin Console (active)
    design-system.css             ←   all component CSS + design tokens (:root)
    button-styles.html            ←   button component reference
    card-styles.html              ←   info card component reference
    color-tokens.html             ←   full color palette with contrast ratios
    link-styles.html              ←   link color states reference
    table-styles.html             ←   data table, sortable headers, filter toolbar
    form-styles.html              ←   segmented control, toggle switch, validation
    DESIGN-PROGRESS.md            ←   decisions made, what's pending

  public/                         ← arxiv.org + abstract pages (planned)
    README.md                     ←   scope and status
```

## Tech context

arXiv's production frontend spans multiple stacks accumulated over 30+ years:
- **Cloud-native:** Python (Flask/Jinja) + React
- **Legacy:** PHP, Perl/CGI, static HTML
- Components must work across stacks — the design system uses plain CSS custom properties (no build step, no framework dependency)

## Scope

**Internal tools (active):** The `internal/` patterns cover arXiv Check (moderation tool) and the Admin Console. These are staff-facing tools with a utilitarian, information-dense design language.

**Public-facing pages (planned):** The `public/` patterns will cover arxiv.org, abstract pages, search, and other researcher-facing interfaces. Some foundations (color tokens, typography, accessibility rules) will be shared with the internal patterns; the component layer will likely differ to suit a different audience and context.

## How to modify

- Check `DESIGN-POLICIES.md` for hard constraints before making changes
- Use tokens from `design-system.css` `:root` — don't introduce one-off color values
- After adding or changing a component pattern, update the relevant pattern page in `design-patterns/internal/`
