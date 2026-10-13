I built both pages in `build/reports/`, with `sections.html` and `cs-activity.html` sharing one small `reports.css`. All assets load from the repo, and the pages reflow at 1366px and 375px.

**1. What I used from the design system**
- Internal-tools setup (`.ds-internal`, both stylesheets, `theme.js`, `header.js`) on the wide page, with the standard header and footer from `templates/`.
- All sections: cards that link, each with a data list (code, archives, categories) and a "Needs attention" warning tag on Quantitative Finance.
- CS report: the "two levels of navigation" pattern (report parts and the Group / Archive / Category filter bar, then the views), a "How to read these charts" accordion, and show more after eight categories.
- Both pages: Refresh is a text button that sends the form again with GET.

**2. Where the design system had no answer**
- No reports wordmark: I used the only internal one, the admin logo, so readers still see they are in an internal tool.
- No placeholder style: one muted-text rule in `reports.css`. The other rules there only arrange existing components (two charts per row, gaps between rows).
- No shared show-more script: I put the docs' version inline. Without JavaScript the full list shows.
- Sort: a compact form with Sort by and Order selects. "Click again to reverse" needs a script, and the system allows only one filter bar per view.

**3. What I did not do, or changed**
- I built only cs.DB and cs.SY, as the brief says. The links to the other 38 categories have nothing to jump to.
- Moderators, Recruitment, the other three views, Staff reports, Physics' archives and the account links point to pages that do not exist.
- All sections has two lines under the heading (purpose, then period); the guidance allows one. I moved the "last 7 days" explanation to a footnote under the cards.
- The design system says cards on a page like All sections show no detailed figures. The brief asks for one, so each card has its placeholder.
- After reviewing screenshots, I moved the category list above the sort form and fixed spacing and the two-column chart layout.