# Mockup: the moderation reports

2026-10-14. Pages in `whiteboard/mockups/internal/membership-dashboard/` (they replaced the older mockup there, which is in git history), hand-finished from round 9's best build (D), with build C's code pills and categories popover, and Shamsi's notes from rounds 7 to 9. The docs' Mockups menu links to `index.html`, the Submissions overview.

## What changed from build D

- All sections: the needs-attention tag sits in the card's top corner; each group's code is a pill (from C); the placeholder is a line in the card, not a card inside a card; the lede, the data line and the cards sit closer together; the footnote is a plain line, not the annotation voice; card titles are `<h2>`, so headings do not skip a level.
- Activity charts: the heading and its views sit together; "About these charts" is a labelled button that opens a modal (D); the data line with Refresh sits under the heading; the sort bar is at the left and "Categories (40)" at the right of one row, close to the rows; the category list is a popover (C), not a modal.

## Design-system changes made for these pages

- A card's own `<h2>` title is sized like its `<h3>` title, so a page can keep its heading order.
- A status tag first in a card has no bottom margin, so it no longer pushes the next line in.
- The sort bar's group role moved from the `<form>` to the `.ds-btn-group` inside it: `role="group"` is not allowed on a form (axe, `aria-allowed-role`).

## Page-only CSS: candidates for the design system (Shamsi decides)

`reports.css` beside the pages holds what the design system does not provide yet:

1. **The page heading with "Last updated" and Refresh at its right end**, the same on every page of the tool. The time uses `.ds-date-row`, the style of a paper's submitted date.
2. **A text button at the end of a sentence**, such as "About these charts": no box of its own, on the text's line.
3. **The heading group**: a heading and what introduces it, close together, with the main content a block below.
4. **A footnote** under the main content: smaller muted text.
5. **The filter at the right end of the second row**, after the views.

## Still open

- **The header does not yet mark the report the reader is in.** The pages set `aria-current="true"` on it, so a screen reader announces it, but there is no visual marking. Shamsi wants a better style than the first try; it is being worked on in its own branch, `header-current-section`.

## Checks

All repo checks pass. axe finds nothing on either page in light or dark mode, and neither page scrolls sideways at 1440 or 360px.

## Navigation and sitemap (Shamsi, 2026-10-14)

The live tool put three reports under an All sections page, with a fourth, staff-only area beside them. The reports are now the tool's sections, in the header:

| Header (right-aligned) | Second row: views, then the shared filter | Example page |
|---|---|---|
| Staff reports (menu, staff only): User activity, Section health, Admin effort, Suspicious activity | none: each report has its own controls inside the page | — |
| Submissions | Overview, Charts, Category stats, Workload stats, Releases, Submissions; Group, Archive, Category (not on Overview) | `index.html`, `charts.html` |
| Moderators | Moderator contacts, Moderator touches; the same filter | `moderators.html` |
| Recruitment | Frequent authors, Endorsers; the same filter | — |

- Staff reports comes first: the navigation is right-aligned, so the three shared reports keep their place for readers who do not see it.
- Overview replaces All sections and is the Submissions landing page. It shows every section, so it has no filter.
- Every view stays visible: no "More" menu. When the views and the filter do not fit on one line, the filter moves to a line of its own.
- The filter narrows the page the reader is on; it never moves them to another page.
- Headings: the view and the reader's choice, such as "Charts for cs" and "Moderator contacts for cs".
- How each level displays (for example Physics and its archives) is for the lead developer.
