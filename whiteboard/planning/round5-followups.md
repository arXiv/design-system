# Round 5 follow-ups

2026-10-13. Everything Shamsi raised in the round 5 review, grouped. For the next branch, after PR 9 merges.

## Rules to write or sharpen

- **A review pass before finishing** (Shamsi's "together" note): the agent names the primary content, checks it sits as high as it can, and checks each component it chose against the alternatives (a sidebar beside the main content, an accordion, the bottom of the page). Home: `AGENTS.md`, pointing at layout-patterns.html *The main content comes first*.
- **Internal tools use the internal logo.** Two builds used the public logo. Home: header.html *Internal header*, and `AGENTS.md`.
- **Page zones are not for dense pages**, including the lighter pages of an internal tool, so the look stays the same across the tool. One build still used them.
- **The heading follows the reader's choices:** the open section and the filters, in that order ("Submissions and holds, all of cs"; "Moderators, cs.DC").
- **Pages of a table at the top and bottom only for a long table** (above about 25 rows); below that, at the bottom only. Home: pager.html.
- **A link already in the header is not repeated on the page**, and a link does not repeat the heading's words.
- **Compact date fields** take the width a date needs, not the whole row. Home: forms.html field widths.

## Patterns to settle

- **Placeholder for content still to come**: three builds made three different ones. A documented placeholder with a set wording.
- **A sort bar**: buttons that sort at once, as on the live site, instead of a select with Apply. Shamsi has a screenshot of the live version to look at together.
- **A card variant for prominent cards**, for example a top border in the accent colour. Cards that link looked too plain.
- **Applying dates to every view** ("use these dates for all tabs"), as the live site does: decide where that option lives.

## Content notes for the next brief

- Activity charts: the heading is "Recent moderator activity"; four sort options (category, current holds, weekly holds trend, monthly holds trend); the category list and the explanation are secondary.
- Staff reports: "Choose a report" is not needed; one sentence saying the page is not available to moderators is optional.
- "About these figures": a single line needs no accordion, especially at the bottom of the page.

## From round 6 (2026-10-13)

- **No breadcrumbs.** One revision added a breadcrumb above the heading. The design system has none on purpose: arXiv's site map is broad and shallow, so a link back belongs in the header navigation. Check that the docs say this plainly where an agent would look.
- **Staff reports in the header navigation,** beside All sections: it is one of the tool's sections, and a small link at the bottom of a page is too hard to find.
- **One name for one thing:** a page called them "sections" in its heading and "groups" in the next. Pick one word and use it everywhere.
- **The date and last-updated line above the cards:** it is one line of important context, so it goes before the main content, not at the bottom.
- **Fewer headings on a light page:** "Subject groups" under "All sections" adds nothing when the page holds little else.
- **Question content the brief did not ask for,** such as an "About these figures" section; now in the review step in `AGENTS.md` ("Is it needed at all?").
- **A sidebar for context the reader may want while scrolling:** agents considered it and rejected it to keep the charts wide. Worth a docs example that shows when a sidebar beats putting context at the bottom.

## Status, 2026-10-13 (branch `dashboard-followups-2026-10`, PR 11)

Done: the review pass, internal logo, page zones, heading follows the reader's choices, pager placement, no repeated header links, compact date fields, the sort bar, no breadcrumbs (one home in Header *Rules*), one name for one thing, the data line above the main content, fewer headings, compact internal tools by default. Staff reports in the header and the placeholder wording are in the round 7 spec only.

Still open: applying dates to every view, a prominent card variant (Shamsi prefers fewer variants), a docs example of when a sidebar beats the bottom of the page.

## From round 7 (2026-10-13)

- **What a sidebar costs.** Three builds put the category list or the explanation in a sidebar; Shamsi rejected all three. The sidebar guidance says when one is appropriate but not that it narrows the main content, or that beside a long main column it leaves an empty column. Home: layout-patterns.html *Sidebar*.
- **More than one home for secondary content.** The main-content rule names only "below the main content or in an accordion", so no agent weighed a popover, a modal or a footnote. Give a short list of homes with a test for each.
- **A short note needs no accordion.** One or two lines read as a footnote below the main content. (A round 5 content note that never reached the docs.) Home: progressive-disclosure.html *Accordion*.
- **The sort bar in a GET form.** The demo uses `type="button"`; two agents fell back to a select with a Sort button. Show it as submit buttons with a name and value.
- **Try the alternatives.** Shamsi: as a human designer she would try each relevant component to see which works best. Idea: in the review step, build two arrangements of the hardest placement choice and compare them. Costs more tokens per build.
- **Placeholders in a card** (spec only, for the next round): a card border around each placeholder makes the page easier to read.
- **A condensed secondary navigation at phone width.** The secondary navigation wraps to two lines and is hard to read. Ideas to explore: a menu button, the current label with icons, letters or numbers for the others, a small carousel with back and next. Part of the larger conversation about compact elements.

### Status after round 7 (2026-10-13)

Done in the docs: what a sidebar costs (Layout patterns, *Sidebar*); *Where secondary content goes*, a home for each kind with a test; an accordion holds more than a line or two (*Which affordance*); the sort bar as a GET form with submit buttons. Placeholders in a card go in the round 8 spec only.

Future sessions, not today:
- **Compact elements**, its own session: the condensed secondary navigation at phone width, and wide elements (filter bars, tables, button groups) at phone width.
- **Agents try the alternatives**: build two arrangements of the hardest placement choice and compare them, as a designer would. Test it as a before-and-after pair, like round 6, and weigh the extra tokens.

## From rounds 8 and 9 (2026-10-14)

Done in the docs: the toolbar row above a list (sort bar left, other control right, `.ds-btn-group--split`); an information button with a visible label; a status tag first in a card floats to its top corner.

Still open:
- **No popover script.** The popover is styling only; agents write their own opening code or avoid popovers. A shared script, like `tooltip.js`, would settle it.
- **The joined sort bar wraps badly at phone width.** For the compact-elements session.
- **A footer check.** Build C left out the footer and nobody noticed in review; the evaluation could flag a page without the standard footer.
- **Shamsi liked the codes as pills** (`.ds-tag--keep-case`) in build C's cards.
