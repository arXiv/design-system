I've built both pages: `build/reports/sections.html` and `build/reports/cs-activity.html`. All extra CSS is in `build/reports/reports.css`, and I changed no existing file. I checked both in a headless browser at laptop width and at 360px: nothing overlaps and the page never scrolls sideways. The HTML tags are balanced.

**1. Design system parts used**
- **Page setup:** the internal-tools setup (`.ds-internal`, both stylesheets, `theme.js`), the internal header with its theme toggle, Account menu and `header.js`, the skip link and the standard footer.
- **Page 1:** linking cards in a card grid, with a "Needs attention" warning tag on Quantitative Finance.
- **Page 2:** the docs' two-level navigation. The three parts and a one-row Group/Archive/Category filter sit under the header, and the four views sit inside the page. It uses the wide page and an accordion for the explanation. Show more handles the category list, and the sort select sits in a toolbar. Placeholders are plain `.ds-card`s, whose text is already in the muted colour.

**2. Where the design system had no answer**
- **No logo for the reports:** I used the internal Admin logo, because internal tools must not use the public logo.
- **Refresh:** a text button at the end of the period line. It submits a GET form through its `form` attribute, so it stays on the same line.
- **Sorting rows that are not a table:** a "Sort by" select plus a "Reverse order" checkbox in a GET form. This matches the sample's "click the chosen option again to reverse it" without needing JavaScript.
- **Show more without JavaScript:** I copied the docs' show-more script but reversed its starting state. The list is complete until the script folds it, because content must never depend on a script.
- **Card titles as `<h2>`:** the heading order needs `<h2>` under the `<h1>`, but the system only sizes `<h3>` card titles. I copied that size into `reports.css`.
- **Spacing:** I added `reports.css` rules for the gaps between category rows, and to let the two chart placeholders share a row equally.

**3. Not done, or worth knowing**
- **Missing pages:** links to other subjects, Physics's archives, Staff reports and the other parts and views go to pages that do not exist.
- **Category links:** 38 of the 40 category links point to rows that are not built, since the brief asked for cs.DB and cs.SY only.