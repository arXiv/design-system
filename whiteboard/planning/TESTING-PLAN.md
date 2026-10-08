# Testing plan

Agreed with Shamsi 2026-10-02. How one test works is in `verification/token-burn/README.md`.

## What the testing is for

Shamsi takes the design system as far as she can before developers use it heavily. Developers will have their own input once they implement it in arXiv's repositories, and this testing does not try to stand in for that.

Version 1 is finished when:

- Shamsi has reviewed the visual output of each test and it follows the design guidelines.
- Claude has checked the same output programmatically and finds it conformant.
- An agent given a problem the design system does not address reaches a good result, keeps the rules that must not change, bends where bending makes sense, and reasons from arXiv's stated priorities.

Nothing in Shamsi's area should be obviously wrong: design and visual display, accessibility, usability, and how `docs/` is organized and presented.

## Decisions

- **Shamsi's part is two steps.** She reviews the spec before the build, and she reviews the rendered pages after it. She is never asked a technical question.
- **One review question:** "What is off?", with a verdict for each build (accept, accept with changes, reject). Claude sorts her notes into categories afterwards. The categories are settled after the first test, from what she wrote.
- **Blind review.** One build at a time, in shuffled order, with the model hidden. Then all together.
- **Two models, two builds each.** Sonnet shows whether the docs are clear without a strong model. Opus 5.5 is what most arXiv developers use. A problem in all four builds is a gap in the docs. A problem only in the Sonnet builds is a place the docs leave something unsaid. A problem in one build is probably chance.
- **Specs are written in product words.** A spec that names a component cannot show whether the builder would have found it.
- **Each spec includes something the design system does not cover.** This is the new-problem test, and it happens inside a realistic page.
- **Tests go from simple to complex.** Each test starts after the fixes from the one before it.

## The tests

| # | Page | Surface | Why this one | Source for the spec |
|---|---|---|---|---|
| 1 | Simple search and its results | Public | Forms, filter bar, pager, messages. The search result is undocumented. | `arxiv-search` repository and the live page |
| 2 | Advanced search | Public | A long form with validation, date ranges, and groups of options. | `arxiv-search` repository |
| 3 | A change to an existing page | Public | Developers asked for this shape of task: bring an existing page onto the design system. The request includes one thing that conflicts with a policy, to see whether the builder flags it. | An existing template from an arXiv repository |
| 4 | arXiv Check submission queue | Internal tools | The first internal page: tables, row selection, bulk actions, Access Lime. | Screenshots in `whiteboard/mockups/internal/arxiv-check/` |
| 5 | Membership dashboard | Internal tools | The most complex page, and the original exit test. | `whiteboard/planning/specs/membership-dashboard.md` |

**Out of date (2026-10-06):** the rounds actually run are 1 to 3 on search (done) and 4 on the moderation and staff reports (waiting for review); arXiv Check, in React, is under *To do later*. V1 is defined in `HANDOFF.md`. Tests 3 to 5 in this table were a proposal. Shamsi confirms each one when its spec is written, since what tests 1 and 2 find may change what is worth testing next.

## After each test

1. Claude writes the summary.
2. Shamsi and Claude decide what to change in the design system. A change to the docs needs evidence from more than one build, or a rule Shamsi confirms was missing.
3. After the changes, the same spec is built again with one build for each model. Shamsi looks only at what the changes were meant to fix.

## To do later

- **arXiv Check, in React (added 2026-10-06).** arXiv Check is built in React, so the brief asks for React components built on the design system's CSS and docs. That adds a translation step the HTML tests do not have. Shamsi takes screenshots first; not before she has time for it.

## Not decided yet

- How much of Shamsi's time a test should take. She decides after reviewing the first outputs.
- The categories for her notes.
- Whether to test with Gemini. Some developers use it.
- Whether to rename `verification/token-burn/`. The name describes the July goal, not this one.

## What changed from July

- The five July tasks are retired. Most asked for things the design system now documents.
- The test workspace now leaves out `whiteboard/`. Since the 2026-10-02 reorganization it would otherwise have included the mockups and the scoring notes.
- Each build has a limit, which developers asked for. Builds run only on Shamsi's Claude plan, never on an API key, and stop if a build goes beyond what the plan includes.
- The review page asks one question and saves the answers itself. There is no JSON to copy.
- Token and cost figures are recorded in the summary. They are not something Shamsi reviews.

## Status

- 2026-10-08: Shamsi: phone widths are not checked for the internal-tools tests. Guidance drafted for her review from test 4: the main content comes first and pages that send the reader on (layout-patterns.html), cards that link (cards.html), two levels of navigation (header.html), and directing agents to the standard header (AGENTS.md, a note on every docs page's header).
- 2026-10-08: test 4 (moderation and staff reports, internal tools) reviewed: all four rejected on page hierarchy; programmatic Pass for two, Pass with changes for two. Found: no guidance on doorway pages or keeping secondary content out of the way; no two-level navigation; agents copy the docs pages' light header. Design-system bug fixed: `.ds-table-scroll` is positioned. Report: `verification/token-burn/runs/20261006-192823-04-staff-reports/report.html`.
- 2026-10-06: test 3 (search results, answer key version D) built and reviewed. All four reached D from the docs; visual Pass with changes, programmatic Pass for all four. Found: no rule for how many page numbers, no wording for the 10,000-result notice, pager bars do not space themselves from the list; and a skip-link focus bug (fixed). Report: `verification/token-burn/runs/20261006-142757-03-search-results/report.html`.
- 2026-10-05: test 2 (search results, one page state) built and reviewed: all four builds accepted with changes. Changes since: search version D (`search.html`), the Papers page, tooltips that stay on screen. Team report: `verification/token-burn/reports/2026-10-search/`. Next: test 3 rebuilds search results with the same spec once Shamsi has settled Papers; after that, arXiv Check as the non-paper search. The numbering in the table above is now out of date: the order is search results again, then arXiv Check.
- 2026-10-02: numbered pages added to the pager (`.ds-pagination-pages`, pager.html), with a routing row in AGENTS.md. Search needs them, and the pager had no row in the routing table.
- 2026-10-02: test 1 built, evaluated, reviewed and summarized. See "Test 1" below.
- 2026-10-02: numbered pages changed to one compact group with the accent tint on the current page (proposal: `proposals/numbered-pages.html`). The current page has the accent tint with the accent border. Both pagers share one structure: the position or range at the start (`.ds-pagination-position`), the controls at the end. Results per page goes in a filter bar above. Open: whether the row repeats below the list; the filter bar looks jumbled with five filters.
- 2026-10-02: runner rebuilt and checked with a one-build smoke test. Spec for test 1 drafted at `verification/token-burn/tests/01-search-simple/spec.md`, waiting for Shamsi's review. Nothing built yet.

## Test 1: simple search (2026-10-02)

Summary: `verification/token-burn/runs/20261002-143816-01-search-simple/summary.html`.

All four builds conformed on the computed checks, and Shamsi rejected the design. The design system lacks a pattern for a compact search form, and no builder used the page zones.

### What went wrong with the review

Shamsi did not realize she was looking at four separate builds of three pages each. She wrote full notes for Build A only. Changes:

- The review page now opens with a screen that says how many builds there are and that each is a separate attempt. Each build's screen says which attempt it is.
- A first test of a new page should have one page state, not three. Other states come in a later round, on the build that was accepted.

### Proposed changes to the design system

Status on 2026-10-02, evening. Done, waiting for Shamsi's review: 1 (the compact form, forms.html), 2 (the page ground is white and the tint is a band), 3 (select arrow, and sort arrows and small icons), 4 (results per page goes in a filter bar above the numbered pages). Partly done: 6 (the compact form keeps messages and options under the row). Open: 5, 7, 8 and 9 to 14.

From Shamsi's review:

1. **A compact search form.** The query field, the field select and the Search button joined as one group on one row, with the label available to screen readers and not shown (DESIGN-POLICIES allows this). On a phone the two fields share a row and the button takes its own. Show abstracts and Advanced search sit together as secondary options. New component.
2. **Page ground.** The default page ground is the tinted canvas (`--ds-canvas`, grey). Shamsi expects white by default, with the tint coming from a band. Decide the default; then search uses a white primary band for the form and results, and the tint for the tips.
3. **Select arrow.** Heavier, and further from the right edge.
4. **Order and results per page** belong with the results, in a filter bar above the numbered pages, not in the search form.
5. **Numbered pages repeat below a long list.** Make it a rule.
6. **Space under a short form.** Too much, and an error message under a field pushes the related controls away.
7. **An alert about a form goes above the form.** Check that alerts.html and forms.html say so; Build C put it below.
8. **Results as cards**, with Show more for the abstract, not an accordion. A search result pattern.

From the technical evaluation:

9. **`.ds-date-row` has no styles.** It is documented on the Versions page and missing from the stylesheet.
10. **Matched words.** Document `<mark>` with the accent tint and heavier weight. All four builds arrived at it.
11. **Show more** assumes the excerpt is the start of the text. Search excerpts can start in the middle.
12. **Tooltip position** at narrow widths. Two builds overrode it.
13. **Filter bar.** A long option is cut off at the default field width, and five filters wrap badly.
14. **Result count** announced to assistive technology. Two builds left it out.

### The spec, for the rebuild

- Use a result count above 10,000, and include a record with more than 25 authors, so both cases are shown.
- One page state.
