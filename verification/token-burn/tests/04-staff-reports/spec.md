You are a frontend developer at arXiv. This repository is the arXiv design system. Follow its guidance for AI assistants.

# Redesign the moderation reports

arXiv staff use moderation reports to see how submissions and holds are moving in each subject, and where moderators need help. The reports are being redesigned on the design system. Build two static HTML pages that show the new design. They are internal tools for arXiv staff.

Work only from this repository and this brief. Do not fetch anything from the network.

## Page 1: all sections

`build/reports/sections.html`. The starting page of the reports.

- The page says what it is for: choose a subject to explore its archives and categories.
- It says which period the figures cover and when they were last updated, and the reader can refresh them.
- Each subject group (Computer Science, Economics, and the rest) shows: its name; its short code; how many archives and categories it has; and three figures for the period: new submissions in the last 7 days, open holds, and unresolved primaries. Each figure has a ratio beside it. For new submissions, the ratio compares the last 7 days with the 3-week weekly average; the reader needs to see at a glance whether it is above or below average, by how much, within a range of 50% either side. For open holds and unresolved primaries, a ratio above 1.0 needs attention, and the reader must be able to tell which groups need it.
- Each subject group links to its own report.
- A link goes to the other reports for staff.

## Page 2: one section's submission statistics

`build/reports/cs-submissions.html`. The report for Computer Science, open at its submission statistics.

- The reader can see where they are: the reports, then Computer Science.
- The reader can choose which part of arXiv the report covers: a group, an archive within it, and a category within that, or all of them.
- The report has three parts: Submissions and holds, Moderators, and Recruitment. Submissions and holds is open. It has four views: Activity charts, Category submission stats, Recent releases, and Recent submissions. Category submission stats is open. Build only that view; the others are links.
- The reader can set the date range (a start date and an inclusive end date) and apply it. The page says which period is showing and when it was last updated, and the reader can refresh it.
- A short note explains how the figures are counted (in the sample content).
- The reader can set two thresholds, in days, and apply them. A held submission older than the first threshold, or older than the second, counts toward the two threshold columns.
- Four totals: submissions, holds, held longer than the first threshold, held longer than the second.
- A table with one row per category: group, archive, subject, new submissions, new accepted, new rejected, holds, held longer than the first threshold, held longer than the second. The reader can sort it. The two threshold columns stand out, and differently from each other, and the reader can tell what each means.

Both pages work as ordinary forms sent with GET, with the chosen values in the address.

## Sample content

The sample content is below the line at the end of this brief. It is real data from arXiv.

## How to build

Use the design system for everything it covers. Where it has no answer, do what its guidance says to do in that case.

If you need CSS that the design system does not provide, put all of it in `build/reports/reports.css` and nowhere else. Do not change any existing file.

Do not run git commands and do not start a server.

## Your final message

At most 15 short lines, in three parts:

1. The parts of the design system you used.
2. Each place the design system had no answer: what you did, and why.
3. Anything in this brief you did not do, and why.
