# Scoring notes: moderation reports

The builder never sees this file. Written 2026-10-06, before any build, from the five screenshots in `whiteboard/mockups/internal/membership-dashboard/member-dashboard-new-screenshots/`. The test workspace leaves out `whiteboard/`, so the builder cannot see the screenshots or the DS-built mockup beside them.

## What the screenshots do that a correct build should not

1. Public Open Blue for the title, the headings and the "Reports for Staff" button. This is an internal tool: Access Lime, from `.ds-internal`.
2. Title Case headings and uppercase tab labels.
3. Breadcrumbs above a page that also has tabs.
4. Two levels of tabs. The docs allow one level (`.ds-tabs`); the second level is secondary navigation or a choice of view.
5. Floating labels inside the selects and fields. Labels go above.
6. Two separate Apply buttons in one view (date range, thresholds).
7. Sort arrows on every column; numbers left-aligned (`.ds-num` exists).
8. Pale "View activity" links below contrast.
9. An icon-only refresh control.
10. The public footer on an internal tool.

## What a build should use

| Need | Documented answer |
|---|---|
| Surface | `internal-tools.css`, `.ds-internal` |
| Totals | `.ds-card--stat` in a stat grid |
| Subject groups | cards, the whole card one link target |
| Report parts | `.ds-tabs` (one level), with the views as secondary navigation |
| Group, archive, category; dates; thresholds | `.ds-filter-bar`, one Apply |
| Table | `.ds-table`, `.ds-num`, sortable headers only where useful |
| Codes | mono (`cs`, `q-fin`) |

## Gaps we predict

- **No meter or bar.** The design system has no data-visualisation pattern (deferred). How each build shows "above or below average" and "needs attention" is the main finding.
- **Highlighting table columns** by threshold, and a legend for it: no documented pattern.
- **"Last updated" with refresh:** no pattern.
- **Nested navigation** (report parts, then views): builds will split between tabs inside tabs and tabs plus secondary navigation.

## Not in the brief, scored anyway

Dark mode, phone width, keyboard use, accessible names, and needs-attention shown by more than colour.

## Predictions

1. All four use `.ds-internal` and Access Lime.
2. At least three use `.ds-card--stat` for the totals.
3. Every build writes its own meter; this is where most of their CSS goes.
