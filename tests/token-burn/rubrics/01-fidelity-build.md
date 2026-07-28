# Rubric — 01 fidelity build (Dataset & code links card)

**What this task measures:** can the agent find and apply the documented public-side rules for a component the system fully covers in principle (card conventions, link rules, truncation policy).

Hard-constraint checks (fail = miss):
- [ ] All colors from the documented palette (no new hexes); Open Blue only in a primary-action role if used at all — this card must NOT read as a primary CTA
- [ ] Public context: no Access Lime anywhere
- [ ] Links underlined (inline-link rule) and off-site signal present (not color-only — WCAG 1.4.1)
- [ ] `:focus-visible` (not `:focus`) with the standard ring
- [ ] Fonts: IBM Plex stack only, no external font loads
- [ ] Overflow handling follows the truncation policy: disclosure-with-count preferred; if internal scroll, half-item peek; fade never the sole signal
- [ ] CSS added to `design-patterns/public/design-system.css` with `.ds-` naming and a comment block matching the file's style
- [ ] Demo page follows reference-page structure (states, tokens, usage, a11y notes) and valid HTML

Judgment (designer pass):
- Does the card read as browsable supplementary material (quiet) rather than a CTA?
- Does the 12-artifact case look right, and is the chosen show-N sensible?
- Would you accept the reference page into the repo with minor edits?

Reasoning quality (final message): did it cite the actual rules it applied (truncation policy, link policy, card conventions) or generic best practices?
