I built `build/search/results.html` and `build/search/search.css`. I checked the page in headless Chrome from the local file: it renders, has no sideways scrolling at 320px, its HTML tags balance, and the show-more script runs.

**1. What I used from the design system:** the brand header and footer markup from `templates/adapters/vendored/`, with paths pointed at this repo. The search pattern from `search.html`: compact form, `.ds-filter`, a heading of "Results for" and the query, and the 10,000-result alert in its existing wording. Numbered pages in `--top`/`--bottom` bars, with Previous disabled and the last link at page 200. Papers in a list from `papers.html`: date row, data list, tags with tooltips, primary tag first. Also `.ds-show-more`, `<mark>`, `tooltip.js` and `theme.js`.

**2. Where the design system had no answer:**
- **25-author cap:** the system shows 8 names and puts the rest behind show more. Result 6 adds "(42 more authors are not shown here; see all 67 on the abstract page)", because the brief says to give the count.
- **No-JavaScript reading:** the server sends the whole abstract and every listed author, and the script switches to the short version. This follows the policy that scripts never hold content.
- **IDs in mono:** the data list has no identifier style, so `search.css` puts the arXiv ID and DOI in the mono face, as the policy says.
- **Spacing in the results:** the results section spaces its own parts with a gap, as the spacing policy says. That and the muted author note are everything in `search.css`.
- **Data-list order:** journal reference, report number, MSC and ACM have no set position. I placed them between Comments and DOI; none of the six sample records has them.

**3. Not done:**
- The announcement banner is left out, because its script fetches its data over the network.
- Hiding abstracts needs the server to read a missing `abstracts=show` as "hide". I noted that in a comment in the form.