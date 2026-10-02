The three pages are built in `build/search/` (`results.html`, `no-results.html`, `invalid-query.html`), with `search.css` and a small `search.js`. I checked them in headless Chrome in light mode at desktop and phone widths; dark mode, keyboard use and the abstract and tooltip toggles were not exercised.

**1. Design system parts used**
- Page foundation (`fonts.css`, `design-system.css`, `theme.js`, `.ds-page`, `.ds-container`), site header with skip link and `header.js`, and site footer.
- Forms (`.ds-form`, `.ds-field`, `.ds-input`, `.ds-check`, `.is-invalid`, `.field-error`), buttons, and the filter bar for page size and order.
- Alerts (info for no results, error for the invalid query), numbered pages, tags with tooltips for category names, show more for abstracts, `.ds-link-list`, tight dividers, `.ds-panel-label`, and the Versions date markup.

**2. Where the design system had no answer**
- **Result record:** there is no pattern, so I built an uncarded `<article>` grouped by spacing, following Layout patterns; optional fields copy the accordion's label and value list.
- **Matched terms:** there is no `<mark>` style, so I used the accent tint with the accent border; the outline means a match is not marked by colour alone.
- **Dates:** `.ds-date-row` is documented but not in the stylesheet, so `search.css` supplies the small muted type the Versions page describes.
- **Abstract excerpt:** show more assumes a hidden tail, but some excerpts start mid-abstract. The page is served with the full abstract, and the script swaps in the excerpt, so nothing is lost without JavaScript.
- **Order field:** the 9.5rem filter-bar field cut off the longest option, so that one field is widened.
- **Apply button:** it is secondary, not primary as in the filter bar example, because Buttons allows one primary cluster per view and that is Search.

**3. Not done, or done differently**
- **10,000-result limit:** this is only an HTML comment in `results.html`, because 8,291 results do not reach the limit.
- **More than 25 authors:** also only a comment, because no sample record has more than 22.
- **Dates:** they follow the Versions pattern ("Submitted · Announced · Revised (this version)", short months, UTC), not the sample wording; UTC is the design system's convention, not something in the sample data.
- **Format links:** they read PDF, PostScript and Other formats so that each link says where it goes.
- **Chrome omissions:** the announcement band and search overlay are left out because they need the network asset route; in the footer only "member institutions" is linked, because the docs give no address for the other two.
- **Invalid-query message:** it keeps the brief's sentence and adds an instruction, as the alert rules require.