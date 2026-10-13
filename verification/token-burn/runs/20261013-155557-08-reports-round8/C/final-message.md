I built both pages, but I have not opened either in a browser, so I have not checked how they look. I only checked that the HTML tags balance. The files are `build/reports/sections.html`, `build/reports/cs-activity.html` and `build/reports/reports.css`.

**1. Design system parts used**
- Internal-tools setup, the internal header, the standard footer, and the second-level navigation under the header. Page 2 follows the "Two levels of navigation" pattern: report parts, the subject filter bar and the views.
- Cards that link with a "Needs attention" warning tag, plus the data list, plain cards, text buttons and a closed accordion.
- Compact forms for refresh and sorting. Every form is GET and carries the other choices as hidden fields.

**2. Where the design system had no answer**
- **Placeholders:** they are plain paragraphs in `.ds-card`, which the system already colours `--ds-text-muted`, so they need no CSS.
- **Category list:** `reports.css` has one rule, columns for the list of 40 category links.
- **Refresh:** the system has no page-refresh pattern, so I used a text button beside the period line, as the layout guidance says for secondary actions.
- **Sorting:** I used a "Sort by" select plus an "Order" select instead of click-to-reverse, because that needs JavaScript.
- **Logo:** the only internal logo in the repository says "Admin Console".
- **Footer:** it has no funders row, because the footer page says funders were removed in September 2026.

**3. Not done**
- Only cs.DB and cs.SY are built, as the brief said.
- The pages that other links point to are not built: `staff.html`, the other groups' report pages, `physics-archives.html`, and the Moderators, Recruitment and other view pages.
- Page 1 has two short lines under the heading (purpose, then period with Refresh). The guidance allows one, but the brief needs both.