# Scoring notes: the review pass, before and after

The builder never sees this file. Written 2026-10-13, before any build.

## Design

Four agents build the two pages (all sections, activity charts) with the docs as they are. The pages are saved ("before"). Each agent then receives `followup.md`, the draft *Before you finish* section, in the same session, and revises its own pages ("after"). Shamsi sees each agent's two versions side by side, labelled 1 and 2 in random order, and says which is better, or that they are the same.

The docs do not change between the two versions, so the only difference is the review pass.

## Measures

- Shamsi's choice for each pair, and her reasons.
- How far down a 1440 by 900 screen the primary content starts: on all sections, the first subject-group card; on activity charts, the first chart placeholder.

## Predictions

1. Shamsi prefers the after version in at least three of four pairs.
2. The primary content moves up on activity charts in at least three of four pairs.
3. On all sections, little changes: the cards already come early.
