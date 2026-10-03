I built `build/search/results.html` and `build/search/search.css`. I checked that the HTML tags balance, every `ds-` class exists in `design-system.css`, every local file path resolves and every ARIA id reference points at an element. I have not looked at the page in a browser.

**1. Design system parts used:** the brand header and footer markup from `templates/adapters/vendored`, `.ds-container` with a `.ds-zone-secondary` band, the compact search form (`.ds-input-group`, `.ds-check`, `.ds-filter` for sort order), an info `.ds-alert`, numbered pages in `.ds-pagination` with the per-page form, `.ds-tag--info --keep-case` category tags with `.ds-tooltip`, `.ds-link-list`, `.ds-show-more`, `<mark>`, `.ds-date-row`, and the reference scripts for tooltips and show-more.

**2. Where the design system had no answer:**
- **The result itself:** there is no pattern for one, so I built it from the nearest patterns. Each result starts with a heading, and the gaps follow the spacing rule (small inside a result, large between results). All of this is in `search.css` and noted in comments.
- **Sort order:** I put it under the search row as a secondary option, because it is part of the query that produced the results. Sort is a setting, so it has no "All" option.
- **Results per page:** `AGENTS.md` says it goes in a filter bar above the list; `pager.html` puts it after Next. I followed `pager.html`, because it has the actual markup.
- **Abstract excerpt to full text:** the full abstract is in the HTML and a script collapses it to the excerpt, as the version list does. Without JavaScript, the full abstract shows.
- **Authors beyond 25:** the count of the other 42 is plain muted text, not a show-more, because the page does not have their names.
- **Dates:** I used the version-display words "Submitted", "Announced" and "Revised (this version)".

**3. Not done, or changed:**
- The page has the six sample results, not 50.
- I left out the announcement banner, because its script loads from arXiv's servers. Header and footer images point at copies in this repo instead of static.arxiv.org.
- Result 5's DOI was malformed in the record (`…101198}{10.1016/…`). I shortened it to `10.1016/j.ascom.2026.101198`, so check that this is right.
- Form and link addresses use arxiv.org paths (`/search/`, `/abs/…`), so they do not work when the file is opened locally.