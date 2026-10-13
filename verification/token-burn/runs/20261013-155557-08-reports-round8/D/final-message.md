I built both pages, plus `build/reports/reports.css`. I could not look at them in a browser because I was not to start a server, so the layout is unchecked on screen.

**1. Design system parts used**
- Internal tools setup: `ds-internal`, both stylesheets, `theme.js`, `header.js`, the admin header with the Refresh and theme tools, the Account menu, and the standard footer.
- Layout and navigation: the wide container, and the two-level navigation pattern for the report (parts, then a compact Group/Archive/Category filter bar, then views).
- Content components: link cards with the `Needs attention` warning tag, `.ds-data-list`, `.ds-card-grid` for the placeholder cards, a closed accordion for the chart explanation, and `.ds-form--compact` with `.ds-filter` for sorting.
- Layout rules applied: no page zones on either page, and the period and update time in one line under the heading.

**2. Where the design system had no answer**
- **Charts and figures:** I drew none. Each is a `.ds-card` with one muted "Content placeholder for…" line.
- **Sorting a list of cards:** The docs cover sortable table headers and a "Sort by" select, so I used a select, an Order select (largest or smallest first) and a Sort button. This replaces "click the chosen option again to reverse it".
- **Refresh:** The docs put whole-tool Refresh in the header tools. It is an icon button tied by the `form` attribute to a hidden GET form.
- **Spacing in `reports.css`:** Only token-based spacing for the card contents and the category list.

**3. Not done, or different from the brief**
- **Category list:** I built only cs.DB and cs.SY, as asked. An HTML comment notes that the real page shows eight and puts the other 32 behind "show 32 more". I did not add a show-more control with nothing behind it.
- **Linked pages:** Staff reports, the other group reports, the Physics archives page and the other parts and views are links only. I built no target pages.
- **Cards and figures:** The docs say cards should hold at most a count or a mark, with figures left for the report page. I followed the brief and put a placeholder in each card.
- **Account area:** There is no greeting, because I had no name.
- **Logo:** It is the only internal one in the repo, "Admin Console". It may be the wrong name for a reports tool.

**Layout review changes:**
- The period and update time share one line with the purpose.
- The explanation sits in a closed row above the list.
- Refresh moved to the header.
- The attention tag sits on the card heading row so the card contents stay aligned.