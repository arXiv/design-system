I built the results page at `build/search/results.html`, with the extra CSS in `build/search/search.css`. Headless Chrome screenshots of the local file show it lays out correctly at 1280px and reflows at 360px, and the HTML checks clean. I did not change any existing file, run git or start a server.

**1. What I used from the design system**
- **Page and form:** the page base and container, the public site header and footer markup, the skip link, and the compact search form with Show abstracts, Sort by, Results per page and Advanced search under the row. The form is an ordinary GET form.
- **Results:** the "Results for" heading, an info alert for the 10,000 limit, and numbered pager bars above and below the list. The pager runs 1–5 … 200, with Previous disabled on page 1.
- **Each result:** the paper list pattern (dates, formats, authors, data list), matched words marked with `<mark>`, and category tags with the primary one first. Each category's full name is in a tooltip.
- **Show more:** for author lists over 8 names and for abstracts. Without JavaScript the full lists and full abstracts show.

**2. Where the design system had no answer**
- **More than 25 authors:** for SN Helios, the button reads "show 17 more of 67 authors". When opened, the list ends "and 42 more not shown here: all 67 are on the abstract page", with a link. The show-more pattern supplies the button; the extra wording is my choice, so the list never looks complete.
- **Report number, MSC class and ACM class:** the data list only orders Comments, journal reference, DOI and arXiv ID. I put these three after journal reference, noted in a code comment. None of the six records has them.
- **Space between the pager bars and the list:** the pager guidance says it should equal the gap between papers, and no named spacing step matches. `search.css` uses that same value, `--ds-space-8`; this is its only rule.
- **Chrome assets:** the shared header and footer load the logo and scripts from static.arxiv.org. I pointed them at the copies in this repo and left out the announcement banner, so the page loads nothing from another host.

**3. What I did not do**
- I built the 6 sample results, not 50, and the links are arxiv.org paths that will not work from the local file.
- Changes to the checkbox and selects take effect only when the searcher presses Search; nothing auto-submits.