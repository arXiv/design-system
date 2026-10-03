I built the page at `build/search/results.html` with `build/search/search.css`. It renders cleanly at 1000px wide. I did not get a reliable narrow-screen check, because headless Chrome would not render below about 500px.

**1. Design system used**
- Page frame: `.ds-container` on `<main>`, skip link, the public header and footer, and a `.ds-zone-secondary` band for the search form.
- Search form: `.ds-form--compact` with `.ds-input-group` and `.ds-check`.
- Filter bar: `.ds-filter-bar` holds order and results per page.
- Results: `.ds-card` per result, `.ds-tag` for identifiers and categories, `.ds-tooltip` for category full names, `.ds-acc` for the full abstract, `.ds-date-row`, `.ds-link-list`, `<mark>`, and `.ds-alert` for the 10,000-result limit.
- Paging: `.ds-pagination` numbered pages, shown above and below the list, with the last reachable page 200.

**2. Where the design system had no answer**
- **Result list and rows:** I added list, row and metadata layout in `search.css`.
- **Category tooltip placement:** it opens under the whole tag row so it stays inside the card on narrow screens (also in `search.css`).
- **Results per page:** the design system gives two homes (the filter bar in the routing table, a small form in the pager example). I used the filter bar.
- **Date row:** the pattern assumes Submitted is the v1 date and has no month-only announcement. I showed this version's submit date, then "Version 1 submitted", then "Announced Oct 2026".
- **Abstract open and close:** the excerpt does not continue into the full text, so the show-more button does not fit. I used a native `<details>` accordion instead.

**3. Not done as briefed**
- Result 5's DOI was malformed (`…101198}{10.1016/…`), so I used the single DOI and linked it to doi.org.
- The footer's "major funders" and "all contributors" links point to `#`, because the design system gives no URL. I left out the institution name because none is known.
- The page also uses URLs I assumed: pdf, ps and other-format links, author-search query parameters, and the `order` values.