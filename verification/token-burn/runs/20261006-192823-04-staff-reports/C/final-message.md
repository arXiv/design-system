The four pages are in `build/reports/`: `sections.html`, `cs-activity.html`, `cs-submissions.html` and `staff.html`. I checked all four in a headless-browser screenshot at 1280px wide. I did not check narrow screens or dark mode, and I did not run the design system's checks. I did not create `reports.css`, because no extra CSS was needed.

1. **Design system used:** internal tools setup (`.ds-internal`, both stylesheets, `theme.js`, header and `.ds-subnav`), page container and zone band, `.ds-sidebar` with accordions, the filter bar, `.ds-table` with sortable headers, numbered pager, stat cards, data cards, tags, `.ds-note`, `.ds-alert`, and the button and icon rules.
2. **No answer in the design system:**
   - **Chart placeholders:** I used the nearest pattern, a plain `.ds-card` with one line of text, and left a code comment.
   - **Parts and views menu:** no pattern for a menu of both. I used sidebar accordions. Moderators and Recruitment each hold one link, because the brief gives no views for them.
   - **Staff-only marking:** a "Staff only" tag next to the link and in the table.
   - **Needs attention:** an alert that names the groups, plus a "Needs attention" tag on the figure.
   - **Trends:** over 15% gets a "Growth" or "Fall" tag, or "Large growth" or "Large fall" at 50% or more. Both tags are the same colour at both strengths, so the "darker" step is shown in words only.
   - **GET sorting and refresh:** header sort buttons submit the filter form (`form="filters"`, `name="resort"`), and Refresh is its own small GET form.
3. **Not done or assumed:**
   - Only the data given: 2 of the 40 category rows and 10 of the 100 table rows, with a code comment on each.
   - Link targets such as `physics-archives.html`, the other group reports, the other views and the CSV are placeholders for pages not built. The arXiv Check link uses a placeholder path (`/check/submission/<id>`) because I had no real address.
   - I added "Staff reports" to the subnav of all four pages, not only page 1, and the Account menu has no real log-out target.
   - Sorting by moderator-touches or the chart legends is not built, since there are no charts.