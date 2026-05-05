# arXiv Design System

arXiv's DNA for product design and frontend development.

A proto-design-system defining design tokens, component specifications, and accessibility requirements for arXiv's frontend. Covers both internal tools (arXiv Check, Admin Console) and public-facing pages (arxiv.org, abstract pages).

## Quick start

Open any `.html` file in `design-patterns/internal/` in a browser — no build step needed.

For design decisions and guidelines, start with:
- `CONTEXT.md` — project overview, key decisions, directory guide
- `DESIGN-POLICIES.md` — hard constraints for all frontend work
- `design-patterns/typography.md` — font families, self-hosting plan
- `design-patterns/color-mapping.md` — full palette, internal vs public color usage

## Structure

```
design-patterns/
  typography.md                   shared font spec
  color-mapping.md                shared color palette + usage rules
  internal/                       arXiv Check + Admin Console patterns
    design-system.css               component CSS + design tokens
    button-styles.html              buttons (primary, secondary, tertiary, icon, destructive)
    card-styles.html                info cards
    color-tokens.html               color palette reference
    link-styles.html                link color states
    table-styles.html               data tables, sortable headers, filter toolbar
    form-styles.html                segmented controls, toggle switches, validation
    DESIGN-PROGRESS.md              decisions + status
  public/                         arxiv.org + abstract page patterns (in progress)
    README.md                       scope + status

visual-audit/                     platform-wide visual audit (11 silos documented)
```

## Key links

- `CONTEXT.md` — full project overview and directory guide
- `DESIGN-POLICIES.md` — hard constraints: accessibility, colors, typography, buttons, components
- `CLAUDE.md` — entry point for AI coding agents
