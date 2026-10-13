Both pages are built in `build/reports/`: `sections.html`, `cs-activity.html` and `reports.css`. I checked them in a Chrome screenshot at 1280px wide. I did not re-check the last chart-column tweak, which stacks the two chart placeholders on one line each.

**1. Design system parts used**
- Internal tools setup: `ds-internal`, both stylesheets, `theme.js`, `header.js`, the admin logo and the skip link.
- Header navigation: All sections and Staff reports.
- Pages and navigation: `ds-container` (wide on page 2) and the "Two levels of navigation" pattern. That pattern gave the part links, the compact GET filter bar, and the view links. I used `ds-sidebar`, an accordion and `ds-subnav--in-page`.
- Page 1: `ds-card-grid` of `ds-card--link` cards, `ds-data-list`, and the warning tag "Needs attention".
- Sorting: the sort bar from the buttons page (`aria-pressed` group), and a `ds-btn-text` Refresh button.
- Layout rules from `layout-patterns.html`: no page zones on dense pages, and the explanation behind a disclosure.

**2. Where the design system had no answer**
- Figures and charts: one muted line, "Content placeholder for …", styled by `.report-placeholder` in `reports.css`. It has no box, border or fill.
- Category rows: the system has no pattern for them. I used a plain list with hairline rules (`.report-row`, `.report-row-charts` in `reports.css`) rather than a card per row.
- Sort bar: the docs show `type="button"`, which cannot send a GET. I made the buttons submit (`sort=monthly:desc` and so on), and the pressed one sends the reverse direction.

**3. Not done, or done differently**
- Page 1 has two short lines under the heading, purpose and period, where the layout rule allows one. I merged them into one paragraph. The period explanation is in an accordion below the cards.
- The cards show the code and counts you asked for. The layout guidance says a card should show only a name, a count and a mark.
- Page 2 has only cs.DB and cs.SY, as asked. The Archive menu lists only All and cs, and I did not invent the other archives.
- Links to pages that do not exist yet: Staff reports, Moderators, Recruitment, the other views, the other groups' reports and the Physics archives page. The Physics card links to `archives.html`; the other groups (not Computer Science) link to `section.html`.
- I left out the footer, since the design system only documents a public one. I did not run git or start a server.