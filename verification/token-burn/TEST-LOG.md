# Test log

One entry per round of agent build tests: what was built, what happened, and what changed in the docs as a result. The changes themselves are in the docs; the commit is the state of the docs the agents built from.

The full runs (screenshots, built pages, measurements, review notes) are not kept in the repository. Shamsi keeps a copy outside it.

## July 2026: the first battery

Five tasks, two builds each, with Claude Sonnet 4.6. Baseline, 28 July: 4 of 10 passed. The grades followed what the docs covered, not what the model could do: builds failed where a pattern was missing or hard to find. After the reorganisation and the routing table in `AGENTS.md` (29 July), every build opened `AGENTS.md` first and went straight to the pages it needed; the policy violations (Google Fonts, an icon font from a CDN) went from 3 to 0.

## Search

**Round 1, simple search** (2 October, commit fa85b0b). All four builds followed the rules; Shamsi rejected the design. The docs had no compact search form, and nothing placed the form and results on white with the tips on the tint. The review page was confusing, which led to the one-build-at-a-time review.

**Round 2, search results** (2 October, 7b45c2c). All four accepted with changes. Left open: where the sort order goes, how results are separated from each other and from the pager. `AGENTS.md` and the Pager page disagreed about results per page; fixed.

**Round 3, search results** (6 October, 2b7aee0). All four accepted with changes, and all reached the agreed search design from the docs alone. The skip link had no focus ring (a design-system bug, fixed). Docs changes: which page numbers to show; pager bars space themselves from the list.

## Moderation reports (internal tools)

**Round 4** (6 October, f4a4faa). All four rejected. The builds organised the data instead of deciding what is primary, invented two-level navigation, and copied the docs' light header. Docs changes: the main content comes first, cards that link, two levels of navigation with a compact filter bar, the standard header for internal tools.

**Round 5** (8 October, 70c39ab). All four accepted with changes. Secondary content still pushed the main content down; two builds used the public logo. Docs changes: the internal logo rule; a placeholder and a sort control were planned.

**Round 6, the review pass** (13 October, 94945ef). Each agent built the pages, then revised them using a draft review step. Shamsi preferred the revised pages for three of four agents, and the main content moved up in seven of eight pages. Opus 5.5 outperformed Sonnet 5.5. Docs change: *Before you finish* in `AGENTS.md`.

**Round 7** (13 October, b1fe700). One accepted with changes, three rejected. The rules from round 6 held in every build. Three builds put content in a sidebar, which narrows the charts. Docs changes: what a sidebar costs, *Where secondary content goes*, the sort bar as a GET form.

**Round 8** (13 October, 79bb9c7). All four rejected; Shamsi's standard had risen, so verdicts stopped measuring progress. No sidebars, but no sort bar either: the docs had two sort patterns and no rule for choosing. Docs changes: when to use a sort bar, Refresh on the updated line, a popover or a modal for a list the reader opens. From here Shamsi picks the best and the worst build.

**Round 9** (13 October, f16574a). The best builds yet. Best D, worst B. Three of four used the sort bar; three put the category list in a popover or a modal. Docs changes: the toolbar row above a list, a labelled information button, a status tag in the card's corner. Build D, with parts of C, is the starting point for a reference example of these pages.
