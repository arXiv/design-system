I've built all four pages in `build/reports/`: `sections.html`, `cs-activity.html`, `cs-submissions.html` and `staff.html`, plus `reports.css`. I checked them in headless screenshots opened from the files; no existing file was changed.

**1. Design system parts used:** the internal tools setup (`.ds-internal`, tier 1 and tier 2 stylesheets, `theme.js`, `header.js`), the light site header with the Account menu, secondary navigation, page zones, the wide page, the filter bar with its settings row, tables (sortable headers, numeric columns, row headers), numbered pages, stat cards, card grid, data list, accordion, link list, tags, the warning alert, buttons and links styled as buttons, and Lucide icons copied from `docs/icons/`.

**2. Where the design system had no answer:**
- **Report views:** there is no nav level below the secondary navigation bar. The parts use it under the header; the four views reuse the same component inside the page, because each view has its own address and tabs would need a script.
- **Charts:** dashed cards holding one sentence that names the chart, because the system has no chart guidance.
- **Staff only:** shown with a `.ds-tag--info` label and words, which is how DESIGN-POLICIES says to mark a privileged control.
- **Ratios over 1.0:** a "Needs attention" warning tag on the cell, plus an alert above the table. **Trends over 15%:** a warning tag with a + or − sign, and the screen-reader word "growth" on rises; no fall is in the sample.
- **No-JS sorting and refresh:** sort header buttons submit a hidden GET form, and Refresh resends the chosen values. The tables spec shows the buttons as `type="button"`.
- **Extra CSS:** monospace submission IDs, the status row, and a two-column sort field so its long options are not cut off.

**3. Not done:**
- The sample explanation is kept as written, but two parts of it are not true of this build. It says a change of 50% or more is darker, and the system has no darker tint. It says to click a sort option again to reverse it; here, each direction is its own option in a select.
- Linked pages (other groups, physics archives, the other views and parts, the CSV, arXiv Check) are not built. The arXiv Check path `/check/submissions/<id>` is a guess.