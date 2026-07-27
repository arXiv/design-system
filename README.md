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
design-patterns/   canonical tokens, components, and demo pages (internal/ + public/)
mockups/           in-progress whole-page mockups (preview, NOT canonical)
audits/            visual, labs, and component audit runs
```

See [`CONTEXT.md`](CONTEXT.md) for the full annotated directory guide.

## Mockups vs. canonical patterns

`design-patterns/` is the **canonical** library — tokens, components, and demo pages that have been validated and are intended for production adoption. Anything in there is fair game to reference from production code.

`mockups/` is the **preview surface** — whole-page work-in-progress for stakeholder review. Patterns that stabilize in the mockups get promoted to `design-patterns/public/` and *then* are considered canonical. Mockups themselves are not promised to remain stable.

When this repo is served via GitHub Pages, both surfaces are visible at the same URL — that's deliberate (stakeholders see component demos and page mockups in one place) — but the README in each folder makes the distinction clear.

## Key links

- `CONTEXT.md` — full project overview and directory guide
- `DESIGN-POLICIES.md` — hard constraints: accessibility, colors, typography, buttons, components
- `CLAUDE.md` — entry point for AI coding agents
