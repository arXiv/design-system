I built all four pages in `build/reports/`, plus `reports.css`. The HTML is balanced, and I checked each page in headless Chrome at 1280px; I checked the two report pages at 600px too.

**1. Design system parts used**
- Internal surface (`.ds-internal`, tier 1 + tier 2), standard header with the account menu, skip link, `.ds-container`, and `--wide` on the two report pages.
- "Two levels of navigation" (`.ds-subnav` with the subject filter bar, `.ds-subnav--in-page` for the views). There are no breadcrumbs: "Moderation reports" in the header goes back to all sections.
- Cards that link with a `.ds-tag--warning` "Needs attention" (pages 1 and 4). `.ds-filter-bar` with a Rows per page setting, `.ds-filter`, `.ds-table` with sortable headers, pagers above and below the table, text buttons for Refresh and Download CSV, and `.ds-link-list`.

**2. Where the design system had no answer**
- **Chart and figure placeholders:** a dashed box in muted text (`.reports-placeholder`), taken from the card. The words say what goes there; the dashed edge only marks it as unfinished.
- **The period and Refresh line:** a GET form in `.ds-btn-group`, placed as layout-patterns says (one short line after the heading, or below the cards).
- **Sorting the categories:** there is no pattern, so I used one "Sort by" select. "Click again to reverse" becomes a choice of order in that select, since the page works without JavaScript.
- **Sortable table headers:** the documented buttons became submit buttons, so sorting works as a GET form.
- **Submission IDs and group codes:** set in IBM Plex Mono as the policies require. That needed one class.

**3. Not done, or done against guidance**
- The layout guidance says a linking card shows a name and at most one count, with figures left for the page it opens. The brief asks for two counts and a figures placeholder on each group card. I followed the brief because that guidance is not one of the firm rules; dropping the placeholders would follow it.
- Log out is a POST form, as the design system requires; every other form is GET.
- Only cs.DB and cs.SY are built, so the other 38 category links point to sections that are not on the page. The links to other groups, report parts and staff reports go to pages that do not exist yet.
- The brief lists no descriptions for the staff reports, so their cards show only names.