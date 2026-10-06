You are a frontend developer at arXiv. This repository is the arXiv design system. Follow its guidance for AI assistants.

# Redesign the moderation and staff reports

arXiv moderators and staff use these reports to see how submissions and holds are moving in each subject, and where moderators need help. The reports are being redesigned on the design system. Build four static HTML pages that show the new design. They are internal tools: only signed-in moderators and arXiv staff can see them.

Build the pages as an arXiv staff member with admin permissions sees them. Some parts are for staff only; moderators do not see them. Make clear which parts those are.

Work only from this repository and this brief. Do not fetch anything from the network.

## Charts

Some views hold charts. The design system has no guidance for charts yet, so do not design or draw any. Where a chart belongs, put a short placeholder that says which chart goes there, for example "Chart: cs.DB weekly moderator touches, 13 weeks". Where the current reports show a small meter or bar beside a figure, show the figure as text and leave the meter out.

## Page 1: all sections

`build/reports/sections.html`. The starting page of the moderation reports.

- The page says what it is for: choose a subject to explore its archives and categories.
- It says which period the figures cover and when they were last updated, and the reader can refresh them.
- Each subject group shows: its name; its short code; how many archives and categories it has; and three figures: new submissions in the last 7 days, open holds, and unresolved primaries. Each figure has a ratio beside it. A ratio above 1.0 on open holds or unresolved primaries needs attention, and the reader must be able to see which groups need it.
- Each subject group links to its report. Physics links to its archives instead.
- For staff only: a link to the staff reports.

## Page 2: a section report, activity charts

`build/reports/cs-activity.html`. The Computer Science report, open at its activity charts.

- The reader can see where they are, and go back to all sections.
- The reader can choose which part of arXiv the report covers: a group, an archive within it, and a category within that, or all of them.
- The report has three parts: Submissions and holds, Moderators, and Recruitment. Submissions and holds is open. It has four views: Activity charts, Category submission stats, Recent releases, and Recent submissions. Activity charts is open. The other parts and views are links.
- The page says which period is showing and when it was last updated, and the reader can refresh it.
- An explanation of the charts (in the sample content), and the list of categories shown, each a link.
- The reader can sort the categories by category, current holds, weekly holds trend, or monthly holds trend.
- For each category: its code, its open holds, and its monthly and weekly trends; then two charts, weekly touches over 13 weeks and daily touches over 21 days. A trend of more than 15% stands out; the reader can tell growth from a fall.

## Page 3: a section report, recent submissions

`build/reports/cs-submissions.html`. The same report, open at Recent submissions.

- The same place in the reports, choosers, parts and views as page 2, with Recent submissions open.
- The reader can set the date range (a start date and an inclusive end date) and apply it. The page says which period is showing and when it was last updated, and the reader can refresh it.
- A note on what the figures count (in the sample content).
- Five totals.
- A table of submissions: submitted primary category, current categories, submission ID, submit date, status, and whether it was held. Each submission ID opens that submission in arXiv Check. The reader can sort the table and move between its pages, and choose how many rows are on a page.
- The reader can download the table as CSV.

## Page 4: staff reports

`build/reports/staff.html`. The starting page of the staff reports. Staff only.

- The page says what it is for: choose a report.
- Five reports, each a link: User activity, Section health and Suspicious activity are for staff only; Sections and Moderators are also open to moderators. The reader can tell which is which.

All four pages work as ordinary forms sent with GET, with the chosen values in the address.

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
