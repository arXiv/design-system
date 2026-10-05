The three pages are built in `build/search/` and render correctly at desktop width and at 320px, checked from screenshots; dark mode and the keyboard behaviour were not tested.

**1. Design system parts used**
- Page markup, `.ds-container`, site header with skip link, site footer, tokens for spacing, type and colour.
- `.ds-filter-bar` (with its settings group) as the GET search form, plus `.ds-field`, `.ds-input`, `.ds-check`, `.ds-btn-primary`.
- `.ds-alert` (info for no results, error for the invalid query), `.is-invalid` and `.field-error` linked to the field.
- `.ds-tag` for categories, `.ds-tooltip` for their full names, `.ds-show-more` for abstracts, `.ds-link-list` for authors and formats.
- `.ds-pagination` with numbered pages, and the Versions page wording for dates.

**2. Where the design system had no answer**
- **Search result record:** no component exists, so I grouped each result by spacing and separated results with a hairline, derived from the Dividers guidance.
- **Matched words:** no pattern, so `<mark>` uses the accent wash from `.ds-inline-active` plus bold weight, so that it does not depend on colour alone.
- **Abstract excerpts:** two excerpts start mid-abstract, so show-more controls a hidden part before and after the excerpt. Without JavaScript the full abstract shows, as the progressive enhancement policy requires.
- **Dates:** `.ds-date-row` is documented but not in the stylesheet yet, so `search.css` supplies the described treatment.
- **Tooltip position:** overridden to open from the start of the category list, so it cannot overflow at 320px.
- **Script:** show-more and tooltip Escape need JavaScript and the system ships no shared file, so I added `build/search/search.js`, adapted from the reference scripts in the docs.

**3. Not done, or done differently from the brief**
- **10,000-result limit:** 8,291 results is under the limit, so the message does not render; the markup and pager rule are in a comment in `results.html`.
- **More than 25 authors:** no sample record has that many, so the "N more authors not shown" text is described in a comment and never appears.
- **Date wording:** follows the design system ("Submitted · Announced · Revised (this version)") instead of "v1 submitted; originally announced". "UTC" is appended as the pattern requires, though the brief does not state a time zone.
- **Messages:** reworded to the STYLE.md rules (articles, one instruction per sentence); "query" became "search" to keep one name per thing.
- **Line length:** the page keeps the 850px width, so an expanded abstract runs longer than the 65-character reading measure.