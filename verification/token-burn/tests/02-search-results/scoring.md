# Scoring notes: search results (rebuild of test 1)

The builder never sees this file. Written 2026-10-02, before any build.

## What changed in the design system since test 1

The page ground is white with a tinted band for supporting content; the compact form; numbered pages with the position on the left, results per page in the pager row, and repeated below a long list; the filter bar on a grid; `<mark>` for matched words; styles for the Versions date row; heavier select and sort arrows.

## What a build should use

| Need | Documented answer |
|---|---|
| Search form | `.ds-form--compact`, `.ds-input-group` joining the query and the field select, hidden labels, Show abstracts and Advanced search under the row (forms.html) |
| Page ground | white; the form and results on it; anything supporting in a `.ds-full.ds-zone-secondary` band (layout-patterns.html) |
| Result count and pages | `.ds-pagination` with `.ds-pagination-position` and `.ds-pagination-pages`, above and below the list (pager.html) |
| Results per page | the small form in the pager row (pager.html) |
| Order | not settled in the docs: the pager row or a filter bar |
| Matched words | `<mark>` with no class (typography.html) |
| Dates | `.ds-date-row` (version-display.html) |
| The 10,000 limit | the brief says the searcher is told; nearest pattern is a note or an info alert |

## Still undocumented (the new-problem part)

The search result itself. Shamsi preferred cards in test 1 (Build C). Watch whether builders reach for cards, and how the abstract opens (Show more, not an accordion).

## Predictions

1. All four use the compact form and numbered pages with the position on the left.
2. At least three put results per page in the pager row.
3. The builds split on where order goes.
4. All four mark matched words with `<mark>` and add no CSS for it.
5. At least two still wrap results in cards.
6. The Sonnet builds write more CSS of their own than the Opus builds, again.
