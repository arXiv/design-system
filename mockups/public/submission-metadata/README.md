# Submission metadata — form validation mockup

Work in progress. **Not a build reference.** Per `AGENTS.md`, patterns get
promoted into `docs/` when they stabilise; nothing here is canonical yet.

For Carly: [FORM-VALIDATION-GUIDE.md](FORM-VALIDATION-GUIDE.md) is the
deliverable. It lists every validation component with its visual
characteristics, the flow, and the specific CSS / HTML / JS changes needed —
plus the bugs found in the current page along the way.

Open `index.html` and use the dark bar at the top to switch between five states.

## What is in here

| File | What it is |
|---|---|
| `FORM-VALIDATION-GUIDE.md` | **The written deliverable.** Component inventory, flow, port list, bugs |
| `index.html` | The mockup. Simplified to the form and the patterns under discussion |
| `mockup-validation.css` | Everything proposed. Eleven numbered sections, reasoning in comments |
| `mockup-validation.js` | Rendering, gating, tooltip, in-progress. Scenario data is scaffolding |
| `arxivstyle.css`, `submit.css`, `base_edit.css`, `submit_overrides.css` | **Snapshot of the live submission system, taken 2026-08-25. NOT design-system CSS.** Vendored unchanged so the mockup renders in context. Do not read these as the rule, and do not edit them here |

The mockup deliberately loads the submission system's own stylesheets rather
than the design system's: the submission app is staying on its own CSS for now,
so the proposal has to be legible against what Carly is actually editing. The
new work is confined to `mockup-validation.css`, written with design-system
class names and tokens so a later port is a stylesheet swap rather than a
rewrite.

## Promotion candidates

Flagged in the guide, none of them decided:

- **Disabled state for filled buttons.** The public stylesheet has none — only
  `.ds-btn-text` — and `docs/public/button-styles.html` never mentions disabled.
  `DESIGN-POLICIES.md:80` says "reduced opacity"; the internal implementation
  uses explicit `-dis-` tokens instead. The policy and the only implementation
  of it disagree.
- **Tooltip.** No tooltip exists. `.ds-popover` is a heavier click-triggered
  panel. This one borrows its material and meets WCAG 1.4.13.
- **Inline `<code>` treatment.** Used on every page in `docs/` but only ever as
  a local style, never promoted.
- **Warning tier for fields**, `.is-warning` / `.field-warning`, alongside the
  existing `.is-invalid` / `.field-error`.
- **Two form action areas** — the sidebar rail and the rule-anchored row.

## Not linked from the nav

Deliberately absent from the Mockups menu and `mockups/index.html`: this is an
in-progress whole-page exploration, not something to point people at yet.
