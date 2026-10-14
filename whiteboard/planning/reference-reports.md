# Reference example: the moderation reports

2026-10-14. Two pages in `docs/examples/reports/`, hand-finished from round 9's best build (D), with build C's code pills and categories popover, and Shamsi's notes from rounds 7 to 9. Not linked from the docs menu until Shamsi approves them.

## What changed from build D

- All sections: the needs-attention tag sits in the card's top corner; each group's code is a pill (from C); the placeholder is a line in the card, not a card inside a card; the lede, the data line and the cards sit closer together; the footnote is a plain line, not the annotation voice; card titles are `<h2>`, so headings do not skip a level.
- Activity charts: the heading and its views sit together; "About these charts" is a labelled button that opens a modal (D); the data line with Refresh sits under the heading; the sort bar is at the left and "Categories (40)" at the right of one row, close to the rows; the category list is a popover (C), not a modal.

## Design-system changes made for these pages

- A card's own `<h2>` title is sized like its `<h3>` title, so a page can keep its heading order.
- A status tag first in a card has no bottom margin, so it no longer pushes the next line in.
- The sort bar's group role moved from the `<form>` to the `.ds-btn-group` inside it: `role="group"` is not allowed on a form (axe, `aria-allowed-role`).

## Page-only CSS: candidates for the design system (Shamsi decides)

`docs/examples/reports/reports.css` holds what the design system does not provide yet:

1. **The data line**: the period and last update, then Refresh, on one wrapping line.
2. **A heading with a button beside it**: the view heading and "About these charts".
3. **The heading group**: a heading and what introduces it (lede, data line, views), close together, with the main content a block below.
4. **A footnote** under the main content: smaller muted text.
5. **Equal items in columns**, for the list in the popover.
6. **The popover's opening script**: the docs style the popover but leave opening, placing and closing to each page. A shared `popover.js`, like `tooltip.js`, would settle it.

## Checks

All repo checks pass. axe finds nothing on either page in light or dark mode, and neither page scrolls sideways at 1440 or 360px.
