I built the four pages in `build/reports/`: `sections.html`, `cs-activity.html`, `cs-submissions.html` and `staff.html`, plus `reports.css`. I changed no existing file. The markup is balanced, every class exists in a stylesheet, and I checked the pages in headless Chrome straight from the files, without a server.

**1. Design system parts used:** the internal surface (`.ds-internal`, tier 1 then tier 2), the light site header, secondary navigation for the three parts, page zones and the wide page, the filter bar (the choosers, dates, sort order and rows per page), sortable headers, numeric columns, numbered pages with tinted bars, stat cards, a grey note, a warning alert, tags, data lists, link lists, link buttons with Lucide icons, the theme toggle and the skip link.

**2. Where the design system had no answer:**
- **Views inside a part:** only one bar may sit under the header, and tabs only swap panels within one page. So the four views are a plain row of links, with the open one in bold and marked as current. This is in `reports.css`.
- **Sorting by GET:** the sort headers submit a small separate form that carries the current filters. The filter bar carries the current sort, so `sort` is never sent twice.
- **Staff only:** each staff-only part has an info tag reading "Staff only" and a sentence saying so, which is what the policy says for privileges. The staff page groups its reports under "For staff only" and "For staff and moderators".
- **Needs attention and trends:** these use a warning tag in words ("Needs attention", "Growing"). A fall of more than 15% would get an info tag; the sample has no such fall. A summary alert names the group that needs attention.
- **Charts:** each chart is a plain card holding its "Chart: …" text. There is no header wordmark image for the reports, so the header uses the text wordmark "arXiv Reports". Identifiers are set in mono with one rule in `reports.css`.

**3. Not done:**
- **Darker colour for a change of 50% or more:** tags have no darker shade. cs.DB's +185% has the same "Growing" tag as a smaller rise, even though the explanation text says otherwise.
- **Real link targets:** the arXiv Check address (`check.arxiv.org/submission/…`) is my guess, and the other report pages linked from these four do not exist.
- **Rows:** only the 2 category rows and 10 table rows from the sample are built.