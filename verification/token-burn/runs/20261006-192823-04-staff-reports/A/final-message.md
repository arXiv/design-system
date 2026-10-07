I built the four pages in `build/reports/`: `sections.html`, `cs-activity.html`, `cs-submissions.html` and `staff.html`. I only checked that the HTML is balanced and ids are unique. I did not open the pages in a browser, so how they look is unchecked. I wrote no `reports.css` because nothing needed it, and I changed no existing file.

**1. Design system parts used**
- Internal tools setup (`ds-internal`, both stylesheets, `theme.js`) and the internal light header with the theme toggle and account menu.
- Page container, page zone and page header. Also the filter bar, table with sortable headers and numeric columns, numbered pager with top and bottom bars, stat cards, data list, tags (`Staff only`, trends), warning alert, notes, sidebar with accordions, and buttons.
- Icons copied from `docs/icons`.

**2. Where the design system had no answer**
- **Parts and views inside a report:** I used a sidebar of accordions, with Submissions and holds open and the current view marked, because the design system allows only one bar under the header.
- **Back to all sections:** a plain link with an arrow above the heading, because breadcrumbs are not allowed.
- **Trend strength:** growth is a warning tag and a fall is an info tag, each with an arrow and a sign. A change of 50% or more is not made darker, because there is no darker tier and red is reserved for errors.
- **Category sort:** one setting in the filter bar with eight combined options. The "click again to reverse" behaviour is not built.
- **Charts:** each is a one-line text placeholder, as the brief asked.

**3. Not done, or assumed**
- **Links:** the arXiv Check address, the other subject-group pages, Physics archives and the other report pages do not exist yet. I used placeholder paths such as `/check/submission/ID`.
- **Partial content:** page 2 shows two of the 40 category rows and page 3 shows the 10 sample rows, although the pager says 1–100 of 16,590.
- **Not added:** the Moderators and Recruitment parts, and the other three Computer Science views, have only links, since the brief gave no content for them.
- **Log out:** it posts rather than uses GET, because the design system requires that.