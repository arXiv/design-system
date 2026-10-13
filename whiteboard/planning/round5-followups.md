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
