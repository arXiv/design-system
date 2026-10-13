I reviewed both pages at laptop width and changed both. On a 1280px screen the main content now starts about 95px higher on page 1 and about 170px higher on page 2. Both pages still have balanced tags and do not scroll sideways at 320px.

**Page 1, all sections.** The main content is the grid of subject group cards; the reader comes to choose a subject.
- Above the cards were the heading and its one-line purpose, then a visible "Subject groups" heading and the period line with Refresh. The guidance allows at most one short line between the page heading and the main content.
- The "Subject groups" heading only repeated the purpose line. It is now hidden from view but kept for screen readers, so the heading structure stays correct.
- The period, last updated and Refresh moved below the cards into "About the figures". The guidance says this is secondary and may go after the main content.
- I checked the cards against tables: tables are for a page where the reader works on records, and this page sends the reader on, so cards that link stay.

**Page 2, Computer Science activity charts.** The main content is the category rows: each category's holds status and its two charts.
- **Header, report parts with the subject filter, the four views:** kept. These are navigation and come first, in the order the layout rules set.
- **Heading and views:** "Computer Science" and its views are now grouped together. Before, the page's 48px gap between sections separated the heading from its own views.
- **Status line with Refresh:** kept. The guidance names one short line after the heading as a correct place for it.
- **Explanation:** kept in a closed accordion. A tooltip is too short for four paragraphs, and placing it below 40 rows would hide it from the reader who needs it.
- **List of 40 category links:** replaced with the design system's contents menu, "40 categories shown", on the same row as the sort controls. The list took three lines; the menu takes one. I did not use the full contents bar because it is always sticky, and the policies allow only the header to be sticky in internal tools.
- **Sort:** kept as a small GET form. I considered the segmented control, but its docs say a choice inside a submitted form should be a radio group.

**Still open:** at 320px the open category menu starts 13px past the left edge of the screen. The link text stays visible, but the menu's left border is cut off. I left it rather than restyle a design system component from `reports.css`.

The earlier deviations still apply: no figures on page 1's cards, a "Reverse the order" checkbox instead of clicking an option twice, and the staff reports link only in the header.