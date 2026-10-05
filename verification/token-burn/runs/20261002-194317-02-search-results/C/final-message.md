I built `build/search/results.html` and `build/search/search.css`. I checked the render in headless Chrome at desktop width only: not checked at 320px, in dark mode, or without JavaScript. I changed no existing file.

1. **Design system used:** public header and footer chrome, the compact search form, filter bar (settings group), numbered pager, `.ds-alert`, `.ds-card`, `.ds-tag--info`, tooltip, `.ds-show-more`, `<mark>`, `.ds-date-row`, spacing tokens, mono IDs, and dark-mode tokens.

2. **No answer in the design system:**
   - **Result layout:** it has no search-result component. I laid one out in `search.css` from tokens only.
   - **Category full names:** a tooltip on a tag button. Tags are never styled as links, so this does not replace a link.
   - **Abstract excerpt:** it is not a tail, so I adapted show-more to swap excerpt and full text. Without JavaScript the full abstract shows and the button stays hidden.
   - **Dates:** I used the design system's Submitted, Announced and Revised row. For a later version, Revised is this version's date and Submitted is version 1.

3. **Not done or changed:**
   - **DOI:** the sample for result 5 repeated it as `…101198}{10.1016/…101198`. I showed it once, clean, and linked it to doi.org.
   - **Authors:** the 42 authors of result 6 beyond the 25 shown get a text note only, because there are no names to disclose.
   - **Announcements:** the sample gave only a month, so "Announced" shows the month with no time.
   - **Order and per page:** both sit in one filter bar with one Apply. The query is carried as hidden inputs, and the page links point to `results.html?…`, not `/search/`.
   - **Footer:** it has no funders block, following `docs/footer.html`.