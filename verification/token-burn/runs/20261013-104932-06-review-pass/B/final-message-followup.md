I reviewed both pages against the layout guidance and changed one thing, on page 2. I could not open the pages in a browser, so I judged the layout from the markup, not a rendered view.

**Page 1 (all sections)**
- **Primary content:** the subject group cards, where the reader picks a subject.
- **What sits above it:** the header, the heading, the purpose line and the "Subject groups" heading. Each earns its place, and the cards start right after.
- **What sits below it:** the period, last updated and Refresh sit below the cards, as `layout-patterns.html` says for secondary content. I kept the link to the staff reports there too, as the brief asked.
- **Components:** cards that link fit a page that sends the reader on. A table is for reading and comparing records, which this page does not do.
- **Changes:** none.

**Page 2 (Computer Science activity charts)**
- **Primary content:** the category rows with their holds and chart placeholders, which the reader scans and sorts.
- **What sits above it:** the header, the two-level navigation, the subject filter, the heading, one line for the period and Refresh, and the sort controls. All of these are navigation or controls for the list, and the navigation components fit that job.
- **Alternatives I rejected:**
  - Tabs: the views are separate pages.
  - Breadcrumbs: the page already has secondary navigation.
  - A table: each row holds two charts.
  - A sidebar or accordion for the explanation: the guidance allows putting it below the main content, so I did.

**What I changed:** I merged the Sort form and the Refresh form into one form, so the period line, sort, reverse and Refresh sit in one compact row. That puts the first category row higher on the page. Sort is the first submit button, so Enter sorts, and Refresh keeps the same choices.