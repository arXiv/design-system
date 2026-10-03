# Scoring notes: simple search

The builder never sees this file. Written 2026-10-02, before any build, so the predictions cannot be adjusted to fit the results.

## What the design system covers, and what a build should use

| Need in the spec | Documented answer |
|---|---|
| Site header and footer | `.ds-site-header`, `.ds-site-footer` (header.html, footer.html) |
| Query field, field select, labels | `.ds-field`, `.ds-label`, `.ds-input` (forms.html). The label is visible. |
| Search button | `.ds-btn-primary`, Open Blue. No Access Lime anywhere. |
| Show or hide abstracts | `.ds-seg` or `.ds-check` radios (forms.html) |
| Results per page and order | `.ds-filter-bar`, a GET form. layout-patterns.html says settings sit apart from filters, and results per page is a setting. |
| Moving between pages | `.ds-pagination` with `.ds-pagination-pages` (pager.html, added 2026-10-02 before the test) |
| Category codes | `.ds-tag`; category names are copied, never restyled (tags.html). Full name through the tooltip or visible text. |
| Opening the abstract | `.ds-show-more` (progressive-disclosure.html) |
| No results | `.ds-alert` or a message per alerts.html and messages.html |
| Invalid query | `.is-invalid` and `.field-error` on the field (forms.html), and the query stays in the field |
| Links | bare `<a>`, no class (links.html) |
| Wording | STYLE.md: no contractions, plain words |

## What the design system does not cover (the new-problem part)

Each of these needs the builder to reason. For each one I record what it did and what it argued from.

1. **The search result itself.** No component. A good answer builds it from documented type sizes and spacing tokens, uses a list (the results are ordered), and gives the title the most weight. A poor answer wraps each result in a card by habit, or invents a type scale.
2. **Marking the matched words.** The current site uses a green fill. The design system says fills use a tint or a status colour and that a new fill colour is never added without discussion. This is the clearest test of holding a rule: a good answer uses `<mark>` with an existing tint token, or weight alone, and says why. Inventing a highlight colour is a fail on this point. Using the success colour is a fail too, because a match is not a status.
3. **DOI, journal reference, report number, and the other optional lines.** No pattern for a record's secondary metadata in a list. Watch for label and value treatment borrowed sensibly from `.ds-card--data`, or invented.
4. **The 10,000 result limit.** No pattern. A note (`.ds-note`) is the nearest documented thing. An alert would be wrong, since nothing went wrong.
5. **The author limit of 25.** Plain text is enough. Watch for invention.
6. **TeX in titles.** The brief says to show it as written. Loading a math library from a CDN breaks the self-hosting rule.

## Requirements the spec leaves out on purpose

A developer would not restate these, because the design system states them. A build is checked for each.

- The result count is announced to assistive technology (the current page uses `role="status"` on the heading).
- The page has one `<h1>`, and each result title is a heading or the list is otherwise navigable.
- The full abstract can be read with JavaScript off.
- Every control has a visible label. The current page hides the query label and uses a placeholder.
- Nothing is loaded from another host.
- The page reflows at 320px with no horizontal scroll.
- Dark mode works from tokens, with no hand-picked dark values.
- An unavailable Previous or Next is disabled, not removed (AGENTS.md: actions disable, they do not disappear).
- The DOI link leaves arXiv. Whatever links.html says about external links applies.

## Predictions

Recorded so the summary can say which were right.

1. All four builds find the header, footer, form fields, button, and pager. These are well routed from AGENTS.md.
2. At least two builds miss `.ds-filter-bar` or put results per page inside it as if it were a filter.
3. At least one build invents a highlight colour for matched words.
4. The Sonnet builds write more custom CSS for the result than the Opus builds.
5. No build loads an external resource.
6. At least one build makes the abstract toggle depend on JavaScript with no fallback.

## How I judge reasoning

From the final message and the transcript, for each undocumented point: did the builder cite arXiv's stated priorities (DESIGN-POLICIES, brand.html, accessibility-priorities.md), or fall back on what search pages generally look like? I quote the sentence that shows it.
