# Scoring notes: search results, round 3

The builder never sees this file. Written 2026-10-06, before any build. The brief is round 2's, unchanged; the sample content now lists the formats as PDF, HTML, TeX Source, as the Papers page says.

## The answer key: search version D (search.html, "After a search")

| Need | Documented answer |
|---|---|
| Page ground | the search form and the results both on white; no tinted band behind the form |
| Heading | an h2 "Results for “lensing”", with no count |
| Order and results per page | under the compact search row, as results settings |
| Page numbers | `.ds-pagination--top` and `--bottom` tinted bars above and below the list |
| The 10,000 limit | a notice above the top pager |
| Advanced search | at the end of the options line |
| Each result | `.ds-paper` in `.ds-paper-list`: title; dates and formats on one line (`.ds-paper-when`); authors; abstract; metadata (`.ds-data-list`); categories (`.ds-tag-list`, primary first) (papers.html) |
| Formats | PDF, HTML, TeX Source, PDF first |
| Categories | links with the full name in a tooltip (`tooltip.js`) |
| Matched words | `<mark>` |

## What to watch

- Does each build arrive at D from the docs alone?
- Does any build still put the form in a tinted band, or put results in cards?
- Where does a build differ from D? Each difference is a gap or an unclear spot in the docs.

## Predictions

1. All four put the form and the results on white, with the "Results for" heading.
2. At least three use `.ds-paper` and `.ds-paper-when` for each result.
3. At least one puts order or results per page in a filter bar, because pager.html's numbered-pages demo shows results per page in a filter bar's settings (right for a filtered list, not for search).
