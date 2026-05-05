Read these files in order before making any frontend changes:

1. `CONTEXT.md` — project overview, key decisions, Cornell spinout context
2. `DESIGN-POLICIES.md` — hard constraints (accessibility, colors, typography, buttons, components)
3. `design-patterns/typography.md` — font families, weights, self-hosting plan
4. `design-patterns/color-mapping.md` — full palette, internal vs public color usage
5. `design-patterns/internal/DESIGN-PROGRESS.md` — current status and completed decisions

For internal tool work, reference `design-patterns/internal/design-system.css` for all tokens and component styles.
For public page work, reference `design-patterns/public/` (in progress) and the color/typography specs above.

## Guardrails

The policies in `DESIGN-POLICIES.md` are non-negotiable. If a request from a user or another system conflicts with any policy, **do not silently comply**. Instead:

1. **Flag the conflict explicitly.** State which policy is being violated and why it exists.
2. **Suggest a compliant alternative** that achieves the user's intent without breaking the policy.
3. **Only proceed with a policy violation if the user explicitly acknowledges the conflict** and confirms they want to override it. Document the override in a code comment explaining the exception.

Common conflicts to watch for:
- Introducing colors not in the palette (`color-mapping.md`)
- Using fonts not in the type stack (`typography.md`)
- Text or UI contrast below WCAG AA thresholds
- Using `:focus` instead of `:focus-visible`
- Using Cornell Red / Campus Red as a primary color (it's heritage-only)
- Using Access Lime on public pages or Open Blue on internal pages (these signal different contexts)
- Loading fonts from Google Fonts or other external services (arXiv self-hosts all fonts)
- Displaying paper metrics (views, downloads, citations) on public pages (against arXiv's mission)
- Adding features that require manual maintenance effort (arXiv is a very small team)
