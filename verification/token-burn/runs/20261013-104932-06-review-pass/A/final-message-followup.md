I revised both pages after reviewing them as a reader would. I did not open them in a browser. I only checked the HTML structure and re-read the generated markup.

**Primary content**
- **All sections:** the eight subject-group cards. A moderator or staff member uses them to pick where to go.
- **Computer Science, activity charts:** the category rows, each with its holds, weekly touches and daily touches. This is what the reader is there to scan.

**What I changed**
1. **Accordion on All sections.** "About these figures" sat between the status line and the cards, so it pushed them down. It now sits below the cards. The figures are secondary, and the layout guidance allows an accordion or a place below the main content.
2. **Staff reports on All sections.** It had its own "More reports" heading and section for one link. It is now one line under the cards, in the same section. A heading for one link was more than it needed.
3. **Back link on the activity page.** The "All sections" line above the heading duplicated the header and pushed the title down. I removed it. The header's link to sections.html is now labelled "All sections", so the way back stays in the header. This keeps the guidance of no breadcrumbs, and the title now starts higher.

**What I checked and kept**
- **Sections page cards:** the cards that link are the right component. A table, tabs or a sidebar would suit records, views or supporting content, and this page only sends the reader on. The "Needs attention" tag is the right way to mark the card that needs attention, since an alert would make the reader find the item.
- **Refresh:** it stays a text button on the status line, as the layout guidance says. Only the page's main action is primary, and neither page has one.
- **Status lines:** each stays as one short line after its heading. They are the one line the guidance allows before the content.
- **Activity page navigation:** the report parts, subject filter and views stay as the two-level navigation with the compact filter bar, as the header documentation shows. Tabs are for views that share one address, and these views are separate pages.
- **Explanation of the charts:** it stays in a closed accordion above the rows, so it costs one line. A tooltip is too short for four paragraphs, and a sidebar would take width the charts need.
- **Sort:** it stays a small compact form above the list. It is a setting for the list, not a filter, so it does not become a second filter bar.

I changed no other files, and I ran no git commands or server.