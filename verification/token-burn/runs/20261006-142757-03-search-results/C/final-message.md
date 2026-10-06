The page is at `build/search/results.html`, with its CSS in `build/search/search.css`. I did not open it in a browser; I only checked that the HTML tags balance.

**1. Design system used**
- Chrome, form and results: public header and footer, skip link, and the compact search form with `.ds-input-group`, `.ds-check` and `.ds-filter`. Then an info `.ds-alert` and numbered `.ds-pagination--top/--bottom`.
- Each result: `.ds-paper-list` of `.ds-paper` with `.ds-paper-when`, `.ds-date-row`, `.ds-link-list`, `.ds-data-list` and `.ds-tag-list`. Category names use the tooltip, with `tooltip.js`.
- Show more: `.ds-show-more` for abstracts and authors.
- Matched words are `<mark>`. The page links `theme.js` and loads the fonts from `docs/`.

**2. No design-system answer**
- **Excerpt that is not the start of the abstract:** most excerpts begin mid-text, so I send the excerpt and the full abstract as two spans and "show more" swaps them (the pattern in `docs/papers.html`, copied inline; markup unchanged). Without JavaScript the reader gets the full abstract and no button, via `search.css`.
- **More than 25 authors:** the pattern collapses after eight names. Result 6 shows 25, a "show 17 more authors" button, and an italic "and 42 more not shown" (`.result-omitted` in `search.css`).
- **TeX in titles and abstracts:** shown as plain text, as written. The design system has no pattern for it, and rendering it would change the author's text.
- **Dates:** `docs/papers.html` defines Submitted as version 1. Result 3 therefore shows Submitted 29 Sep, Announced Sep 2026, Revised 1 Oct. The brief's "date this version was submitted" is the Revised date there.
- **Abstract page, format and author URLs:** these `arxiv.org` links are my guesses at the real addresses.

**3. Not done**
- Pages 201 and later are not linked. The pager runs 1, 2, 3, …, 200, and the alert says they cannot be reached.
- The page shows only the six sample results, and only the abstracts-shown state.
- No header search overlay or announcement banner. Both need production scripts loaded from `arxiv.org`, which the brief rules out.