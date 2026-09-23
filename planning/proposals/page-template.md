# Pattern-page template — proposal (2026-08-06)

Answers the open question from the reorg planning: what documentation shape serves
agent-assisted frontend work AND stays pleasant for humans. Status: **proposed** —
first pages built to this template: `docs/internal/metadata-panel.html` and the
bulk-actions section of `docs/internal/tables.html`. React to those, not to this file.

## The three consumers

1. **A human skimming** — wants the visual gist without scrolling.
2. **A human deciding** — wants the rule and the why, findable, not buried.
3. **An agent building** (often in another repo, over a URL) — wants exact values,
   markup, and hard rules; never wants to infer.

They want the same thing at different depths, so every page is an inverted pyramid:

## The template (top to bottom)

1. **Title + one-sentence purpose.** What this is, when to reach for it.
2. **The rendered thing.** Live demos of the real classes, states visible, before any prose.
3. **Spec table.** Classes, tokens, values — compact, exact.
4. **Usage code.** Canonical markup, copy-paste ready, correct usage only.
5. **Rules.** Hard rules use `.ds-alert--error`; each rationale ≤ 3 sentences.
6. **Accessibility notes.** What the pattern must keep to stay compliant.

Nothing else. No status boxes, no backlog pointers, no history — planning/ holds those.

## Budgets and rules

- One fact, one home: state a rule once, link to it everywhere else.
- Prose is added only against evidence (a failed agent test, a real misunderstanding).
- Page-local CSS is demo staging only; everything demonstrable comes from the stylesheet.
- Every page carries the shared docs nav and locks light (`data-theme="light"`) unless it
  deliberately previews dark.
