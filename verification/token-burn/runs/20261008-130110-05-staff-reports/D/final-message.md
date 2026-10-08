The four pages and `reports.css` are in `build/reports/`. Markup balances and every linked design-system file exists. I did not open them in a browser, so the layout is unchecked.

1. **Design system used:** internal-tools setup (`.ds-internal`, both stylesheets, `theme.js`), the internal header, the standard footer, and `.ds-container` (wide on pages 2 and 3). Two-level report navigation with the compact subject filter bar. Cards that link, with a warning tag for "Needs attention". Filter bar with settings, sortable table headers, numbered pagers above and below, accordions, `.ds-note`, text buttons for Refresh and the CSV download, and icons copied from `docs/icons/`.
2. **No answer in the design system:**
   - **Figures and charts:** I used a plain dashed-border placeholder, `.reports-placeholder` in `reports.css`, built from tokens only. It is the only custom CSS besides three layout rules (status line, category grid, chart pair).
   - **Page 2 sort:** it is a select plus an Order select in a filter bar, not the segmented control, which is for approve/reject. The explanation says "click the chosen option again", which is now inaccurate. I kept that text as written.
   - **Header logo:** the Admin Console wordmark is the only internal one.
   - **"Go back to all sections":** it is the header link "All sections", because breadcrumbs are not allowed where there is a secondary navigation.
3. **Not done or assumed:**
   - **Links to pages I did not build:** these include the other groups, Moderators, Recruitment, the staff reports, and the CSV file.
   - **arXiv Check URL:** I invented `check.arxiv.org/submissions/<ID>`. Please correct it.
   - **Sample rows:** only the 10 given rows are shown, with the position text "1–100 of 16,590".
   - **Held column:** it shows "No" where the sample was blank.
   - **Page 4:** it has no form, because it has no controls.
   - **Greeting:** I left it out because I do not know the reader's name.
   - **Git:** I ran no git commands and started no server.