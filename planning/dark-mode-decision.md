# Dark / Light Theme — Decision: Deferral

**Status:** Active decision — 2026-06-11.
**Scope:** Both stylesheets (`docs/design-system.css`, `docs/internal/internal-tools.css`) and the public-facing mockups (`mockups/public/html-phase1.html`, `mockups/public/abstract-phase2.html`).
**Companion document:** [`DARK-MODE-AUDIT.md`](./DARK-MODE-AUDIT.md) — the substrate plan this decision sits against.

---

## The decision

arXiv will support **both light and dark modes** as a values-level commitment. That part is not in question.

Within the current redesign phase, dark-mode *execution* is **explicitly deferred**. The mockups remain light-only for stakeholder review; the design system's existing dark-aware tokens (alerts, links) stay in place as foundation work but are not extended.

---

## Reasoning

Light-mode design is still actively iterating: citation styles, hover states, mobile breakpoints, marginalia treatments, hover-borders on equations and figures, the TOC dropdown. Decisions in these areas are still moving week to week.

Doing dark mode in parallel means doing every decision twice — once for light, once for dark — on a moving target. The discipline is: **settle light first, then add dark as a parallel treatment against stable decisions.**

The companion audit (`DARK-MODE-AUDIT.md`) demonstrates that the work is feasible whenever we decide to start. The blocker isn't capability; it's sequencing.

---

## What stays in place

- **The audit document** (`DARK-MODE-AUDIT.md`) — keeps the plan ready to execute, with the surface-token layer proposal, toggle-mechanism recommendation (`@media` + `[data-theme]`), and the public-button design-decision flag.
- **Dark-mode tokens already added to `docs/design-system.css`** for the alert family (`--ds-success-bg/border/fg`, `--arxiv-info-*`, `--arxiv-warning-*`, `--arxiv-error-*`) and the link family (`--ds-link/-hover/-visited`). These are foundation work; they don't get rolled back.
- **`color-scheme: light !important`** stays in the mockup HTML files (`mockups/public/html-phase1.html`, `mockups/public/abstract-phase2.html`). This is the explicit signal that light-only is *intentional* during this phase — not an oversight. A user with `prefers-color-scheme: dark` still sees light when reviewing the mockups.
- **Internal stylesheet dark-mode coverage** is unaffected by this decision; internal tools work in dark mode where they already do.
- **Docs pages locked to light** (added 2026-07-28): the 13 documentation pages with light-only chrome carry `<html data-theme="light">` — the stylesheets' documented lock — so the dark-aware alert/link tokens no longer flip against their light backgrounds under OS dark mode. This is the docs-page parallel of the mockups' `color-scheme: light !important`. The seven pages with *deliberate* dark previews stay unlocked: `alerts.html` (invites OS-switching to preview dark tokens), `alerts.html`, `links.html`, `alerts.html`, `internal/color-tokens.html` (dark-aware chrome / document dark values), and `internal/buttons.html` + `internal/cards.html` (own theme toggles). When dark-mode work resumes, unlocking is one attribute per page.

## What gets deferred

- Adding the surface-token layer (§3 of the audit)
- Extending dark-mode tokens to the rest of the public `:root` palette (the ~14 brand/surface tokens currently light-only)
- Designing the public button's dark treatment (Decision B in the audit)
- Implementing a user-facing toggle UI
- Adding dark-mode treatments to mockup-specific styles (header chrome, marginalia, popovers, hover states, equation/figure chrome, citation breadcrumbs, TOC dropdown, etc.)
- Removing the `color-scheme: light !important` overrides

---

## Criteria for picking it back up

Dark mode work resumes when **all three** of the following are true:

1. **Stakeholder feedback on the light-mode design has been received and incorporated** (i.e., the GitHub Pages mockups have gone through at least one feedback round).
2. **The mockups feel ~80% stable** — fewer day-to-day visual changes; the major design decisions in the mockups are settled.
3. **The work fits in scope** alongside other priorities at that time (production handoff prep, design-system adoption planning, etc.).

A conservative estimate: 2–3 months out, possibly aligned with whatever next major redesign milestone exists at that point.

---

## What happens when work resumes

Pick up the audit document and execute against it. No re-planning needed — the Phase 0 / 1 / 2 sequence is already drafted:

- **Phase 0:** agree the mechanism (Decision A in the audit), the surface-token layer (§3 of the audit), and the public-button approach (Decision B in the audit).
- **Phase 1:** add the surface-token layer + chosen opt-in mechanism; convert tokenizable components.
- **Phase 2:** public button dark redesign; toggle UI + persistence; final audit pass.

---

## Why this isn't tech debt

Deferring an unstarted feature is not tech debt — it's sequencing. Tech debt would be shipping a partial dark mode that breaks in some states and not others, or building dark mode into mockups while the light-mode design is still changing weekly. Both of those would cost more to undo later than the current cost of deferring.

The audit document and the dark-aware tokens already in `design-system.css` are foundation work that pays off whenever execution resumes. None of the deferred work is irreversibly off the table.
