I've built both pages and the stylesheet in `build/reports/`: `sections.html`, `cs-activity.html` and `reports.css`. I did not change any existing file. I checked that the HTML is well formed and that every design-system class I used exists. I have not opened the pages in a browser, so how they look on screen is unchecked.

**1. Design system parts used**
- Internal surface (`.ds-internal`, both stylesheets), the standard header with an Account menu and the theme toggle, and `.ds-skip-link`.
- The two-level navigation pattern: report parts, then a compact `.ds-filter-bar` for Group, Archive and Category, then the views. All forms use GET.
- Cards that link, with a warning tag for "Needs attention", plus `.ds-data-list`, `.ds-card-grid`, `.ds-page-header`, `.ds-section-desc`, a text-button Refresh, `.ds-acc`, `.ds-filter`, `.ds-link-list` and `.ds-panel-label`.

**2. Where the design system had no answer**
- **Placeholders:** there is no pattern for charts, so I made a dashed box with muted text, based on the card and using only tokens.
- **Category list and row layout:** these needed small grid and wrapping-list rules, all in `reports.css`.
- **Sorting:** a "Sort by" select with a Sort button, following the compact form's results settings, because a static GET page has no script to re-sort.
- **Back to all sections:** the design system does not allow breadcrumbs, so the header has "All sections" and "Staff reports". The second one is also the link the brief asked for.

**3. Brief items not done**
- **No figure placeholders on the Page 1 cards.** The layout guidance says a card shows a name and at most a count or an attention mark, and that figures stay on the page the card opens. This conflicts with the brief; tell me if you want the placeholders added anyway.
- **Sorting cannot be reversed.** The sample text says clicking the chosen option again reverses it, which a plain select cannot do. Each option states its direction instead ("largest first", "A to Z").
- **Links to unbuilt pages:** the other subject reports, Physics archives and Staff reports point to pages that don't exist. On Page 2, only the cs.DB and cs.SY links in the category list have a section to jump to; the other 38 are in the list with nothing behind them.