I built `build/reports/sections.html`, `cs-activity.html` and `reports.css`. Both pages render at a laptop width and nothing scrolls sideways at 320px. I did not test the categories popover by clicking it.

**1. Design system parts used**
- **Frame:** `.ds-internal` on the page, the tier 1 and tier 2 stylesheets, the internal header with an Account menu, and the wide page on both pages.
- **Page 1:** cards that link in `.ds-card-grid`, a `--keep-case` tag for each short code, and a `--warning` "Needs attention" tag on Quantitative Finance.
- **Page 2:** the "Two levels of navigation" pattern. The report parts and a compact Group/Archive/Category filter bar sit under the header, and the four views are a second row inside the page.
- **Page 2 controls and text:** the sort bar is a GET form whose pressed button sends the reverse order. The 40 category links are in a popover behind "Categories (40)", and the explanation is in an accordion below the charts.
- **Both pages:** the period line ends with a Refresh text button and the `refresh-cw` icon, and works as a GET form.

**2. Where the design system had no answer**
- **Logo:** the reports have no wordmark of their own, so I used the only internal logo there is (arXiv admin) rather than the public one.
- **Placeholder text:** there is no class for it, so I added one muted-text rule in `reports.css`.
- **Chart rows:** the standard card grid left an empty third column beside the two charts, so `reports.css` makes them share the row in halves.
- **Popover script:** the popover needs page code to place it, so I wrote a short inline script. Without JavaScript its button stays hidden, and every category still has its own row on the page.

**3. Not done from the brief**
- **Figure placeholders on the All sections cards:** I left these out. The layout guidance says a card shows a name and at most a count or an attention mark, and the figures belong on the page the card opens. Say if you want them back.
- **Purpose line:** "Choose a section…" shares one line with the period, because the guidance allows at most one line between the heading and the cards.
- **Rows and links:** only the cs.DB and cs.SY rows are built, so 38 of the popover links have no row to jump to. "Staff reports" and the other report pages it links to are not built.