I built the four pages in `build/reports/` (`sections.html`, `cs-activity.html`, `cs-submissions.html`, `staff.html`) and put the extra CSS in `reports.css`. No existing file changed. The HTML balances and all local links resolve. I looked at headless Chrome screenshots of the files: at 1280px wide all four pages lay out cleanly. I could not check a phone width: at 360px the screenshot was cut off, but a design system docs page was cut off the same way, so the narrow layout is unchecked.

1. **Design system parts used:** the internal tools surface (`.ds-internal`, tier 1 and tier 2 stylesheets); the standard header and footer from `templates/`, with local paths; cards that link, with the warning tag "Needs attention". From the header page's "Two levels of navigation": the report parts and subject choosers under the header, the views inside the page, and no breadcrumbs. Also the filter bar (with Rows per page under its settings), the table with sortable headers, numbered pages above and below the table, accordions, text buttons for Refresh and Download CSV, and the wide page for the two reports.
2. **Where the design system had no answer:**
   - **Placeholders:** there is no chart or figure pattern, so they are dashed boxes of muted text made from design system tokens.
   - **Categories shown:** a wrapping list of links, since tags must never stand in for links.
   - **Spacing:** a few stacking rules that use the named spacing steps (tight, block, section).
   - **Category order:** a "Sort categories by" select with an Apply button. Each option includes its direction, so there is no "click again to reverse", which needs JavaScript.
   - **Table sorting:** the header buttons submit a GET form, so the chosen order goes in the address.
   - **Inclusive end date:** the date field is labelled "Up to and including".
3. **Not done as written:**
   - **No figures on the subject group cards.** The layout guidance says a card that links shows a name and at most a count or a needs-attention mark, and the figures belong on the page it opens. Each card shows its name, code, and archive and category counts. The period and last-updated line, with Refresh, sits below the cards.
   - **Staff reports link:** it is in the header navigation, not repeated in the page.
   - **arXiv Check address:** the brief gives none, so the submission links use a guessed one (`check.arxiv.org/submission/<id>`).