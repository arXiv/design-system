I built `build/search/results.html` and `build/search/search.css`, and changed no existing files. I checked the page in headless Chrome: the HTML is balanced, there is no sideways scrolling at 320px, and the script collapses all six abstracts to their excerpts.

**1. Design system parts used**
- Site header and footer from the templates' static version, with asset paths pointed at this repo. Fonts, `design-system.css` and `theme.js`; the secondary tinted band for the search.
- The search is a compact form (query and field joined, Show abstracts, Advanced search). Pages use numbered pages, repeated below the list; the first and last links are disabled, not removed.
- Results per page is the pager's small form after Next, with its own Apply button. The 10,000-result notice is an info alert.
- Category tags, the author link list, `<mark>` for matched words, show-more for abstracts, date rows, and dark mode through tokens.

**2. Where the design system had no answer**
- **Order:** I added it to the results-per-page form, so one Apply sets both. Order is not a filter, so a filter bar did not fit.
- **The result itself:** grouped by spacing tokens alone (no cards), IDs and DOIs in mono, labels muted. That CSS is in `search.css`, on tokens only.
- **Category full names:** a tooltip on each tag, which links to its listing page. This follows the tooltip rule that its text must also exist somewhere else.
- **Abstracts:** without JavaScript each abstract shows in full; the script collapses it to the excerpt. This follows the version list pattern, so the script never holds content.

**3. Not done, or changed**
- Only the 6 sample results, not 50.
- Result 5's DOI is malformed in the record. I show the one DOI it names.
- The AGENTS.md routing table puts results per page in a filter bar above the list, but `pager.html` puts it after Next. I followed `pager.html`.