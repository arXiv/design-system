---
page: organize-content.html
title: "Organize complex page content"
summary: "How to arrange a page around what its users need and what patterns and components to reach for. This page does not show the patterns themselves. It provides guidelines to content organization and links to the pages where the examples are shown. Learn about the page container and page areas on [Layouts](layouts.md)."
stylesheet: design-system.css
components:
  - id: evaluating-user-needs
    title: "Evaluating user needs"
    summary: "What a user needs to learn determines the right organizational pattern to employ for any group of content. Use the four questions below as a starting point. Each question has a test and a set of patterns that answer it. Most content will fit under one of these questions. Have an edge case? Discuss it with the design team."
    notes:
      - "Where am I? (The address or the item changes): [Header](header.md) and [secondary navigation](navigation.md#secondary-navigation): sections of a site or tool; [Steps](navigation.md#steps): an ordered process; [Pager](pager.md): a queue, one item at a time; [Numbered pages](pager.md#numbered-pages): a long list split across pages; [TOC bar](navigation.md#toc-bar): sections of one page"
      - "What matters here? (Directing user attention): [Spacing](spacing.md) and [dividers](dividers.md): separate content; [Page container](layouts.md#the-page-container), [secondary zones](layouts.md#secondary-zones) and [wide page](layouts.md#wide-page): the page frame; [Sidebar](layouts.md#sidebar) and [marginalia](layouts.md#marginalia): supporting content; [Cards](cards.md) and [tables](tables.md): records; [Cards that link](cards.md#cards-that-link): a page that sends the reader on"
      - "Which part do I need? (The content swaps in place): [Tabs](progressive-disclosure.md#tabs): one view at a time; [Filters](filters.md): narrowed data; [Sections of one page](typography.md#the-heading-scale): views to compare"
      - "Can I learn more? (Richer details are revealed upon request): [Tooltip](forms.md#tooltip) and [popover](progressive-disclosure.md#popover): detail on request; [Show more](progressive-disclosure.md#show-more) and [accordion](progressive-disclosure.md#accordion): more in the flow; [Modal](modals.md): a decision first; [Actions attached to content](buttons.md#small-actions-attached-to-content): act on one item"
  - id: the-main-content-comes-first
    title: "The main content comes first"
    summary: "Before choosing components, decide what the page is for and which content is primary. Everything else is arranged so it does not push the primary content down."
    rules:
      - "**The page heading is followed by the main content.** At most one short line comes between them: a line that sets the data in context, such as the period it covers. An explanation of the figures is secondary: see [Where secondary content goes](#where-secondary-content-goes)."
      - "**What the reader must know before acting comes before the steps it governs**, even when the steps are what they came for. On a withdrawal page, what makes a withdrawal reason acceptable comes before how to submit one."
      - "**A state that changes how the whole page reads is met first.** The page's `<title>` starts with it, and its notice comes straight after the page heading, before anything else; on a paper the heading starts with it too. A reader, and a screen reader, meets it before reading on. See [a withdrawn paper](papers.md#withdrawn-papers) and [a form with errors](forms.md#alerts-in-forms)."
  - id: where-secondary-content-goes
    title: "Where secondary content goes"
    summary: "Each kind of secondary content has a home that keeps the main content high and wide. Compare at least two homes for each piece, and keep the one that leaves the main content highest and widest."
    rules:
      - "**A line or two: a line below the main content.** A short note, such as what the figures count, reads as a footnote. It needs no heading and no accordion."
      - "**A labelled section the reader may want: an [accordion](progressive-disclosure.md#accordion)** below the main content. An accordion holds more than a line or two."
      - "**The rest of a list whose first items matter most: [show more](progressive-disclosure.md#show-more)**, such as authors after the first eight. A list of equal items, such as the categories a report covers, is shown or hidden whole."
      - "**A list or explanation the reader opens when needed: a [popover](progressive-disclosure.md#popover) or a [modal](modals.md)**, opened from a button with a visible label, such as “Categories (40)” or “About these charts” beside the heading; an icon on its own is easy to miss. A popover opens beside its button and leaves the page usable; a modal takes over the page while the reader looks through it."
      - "**A sentence about one label or control: a [tooltip](forms.md#tooltip).**"
      - "**Supporting content beside short main content: a [sidebar](layouts.md#sidebar).**"
  - id: where-controls-go
    title: "Where controls go"
    summary: "A control sits with what it changes. The more of the site it changes, the higher it sits on the page."
    rules:
      - "**A tool or filter for every page under the header, whether a whole site or a whole tool: the header's centred space**, on the header's background. Nothing sits higher. Use it sparingly. See [Header](header.md#design-rules)."
      - "**A choice between the sections of a tool: the section menu**, at the start of the second row, on the accent tint. It is navigation. See [Two levels of navigation](navigation.md#two-levels-of-navigation)."
      - "**A filter for the whole page: the page's opening band**, a `.ds-full.ds-zone-secondary` band under the page heading. See [Secondary zones](layouts.md#secondary-zones)."
      - "**Filters, sort and group actions for one set of data: the set's header bar**, on one line, even when the set's only control is one action, such as Copy emails. See [Filters](filters.md) and [Cards with a header bar](cards.md#cards-with-a-header-bar). A table sorts from its [column headers](tables.md#sortable-column-headers)."
      - "**Selecting items in a list: the checkbox at the start of each item, and the actions on the selection in the set's header bar.** A control for one item only goes at the end of that item, on the right. See [Selecting items in a list](tables.md#selecting-items-in-a-list)."
      - "**A control for the whole page sits at least as far above the first set of data as the sets sit from each other**, so it reads as the page's and not the first set's."
  - id: long-pages
    title: "Long pages"
    summary: "Long pages need special consideration of their organization. The longer the page, the more we need to think about [navigation](navigation.md), defining [page zones](layouts.md#secondary-zones), and [not losing your place](../references.html#getting-back-after-a-jump)."
    rules:
      - "**The contents bar hangs from the opening band.** A page with a contents bar has an opening band with its title and an introduction of one to five sentences. See [Secondary zones](layouts.md#secondary-zones). A paper is the exception: its contents bar holds the paper's tools and sits under the site header ([The TOC bar on a paper](papers.md#paper-toc-bar))."
      - "**On a page with a contents bar, all content sits under headings**, so the bar lists every part of the page. An introduction longer than five sentences keeps its first sentences in the band; the rest goes under a heading of its own."
rules:
  - "**Choose typographic and proximity-based organization patterns first**, and reach for visible containers only when called for. This is the organizing principle to follow throughout."
  - "**Use only the questions the content raises.** When a page uses more than one layer, they stack in this order: navigation, then tabs, then filters."
  - "**A page in a set follows the set.** Pages in one section of a site, such as arXiv's help pages, share one template: the opening band and the contents bar are on every page of the set or on none. Before choosing, find out whether the page belongs to a set and what the set already uses. If no one has said, ask; if you cannot ask, say what you assumed."
  - "**In a set that uses the opening band, every page has an introduction**: one to five sentences that say what the whole page is for. Use the page's own text only if it introduces the whole page; a sentence that opens a section introduces that section, not the page. Otherwise write a sentence or two."
  - "**A page outside a set, or in a set without the band, decides for itself.** Without the band it has no contents bar and no introduction."
  - "**When a filter sets what the whole page is about, the page heading names the choice**, as in “Charts for cs”, and so does the page's `<title>`, so tabs, history and bookmarks tell the choices apart. With nothing chosen, the heading is the view alone. A filter that narrows one set on the page never changes the heading."
  - "**A page with little on it needs no section headings.** The page heading names it; a heading such as “Subject groups” under “All sections” adds nothing."
  - "**A link in the header navigation is not repeated on the page**, and no link on the page repeats the page heading."
  - "**One name for one thing.** Choose one word for each kind of thing, such as “section”, and use it in every heading, link and sentence."
  - "**Show readers what they can use.** A page shows each reader only what their permissions allow; inside an internal tool it does not label parts of the page with who may see them. A privileged control on a public page is the exception: it says it is privileged, as [DESIGN-POLICIES.md](../doc.html?src=docs/DESIGN-POLICIES.md) requires."
  - "**Reveal on request rather than add a setting.** Something a reader needs now and then opens when they ask for it, as a popover or a tooltip does. A setting that keeps it on screen adds noise for everyone else."
  - "**A count says what the reader cannot see for themselves.** Search results always have one, even for a few results: the range at the top of the results, “1–3 of 3 results”. See [Search](search.md#results); no results is a message. A set the reader has filtered ends its header bar with how much is left, “3 of 120 holds”. See [Filters](filters.md#rules). A list longer than one page states its range in its [pager](pager.md), “1–50 of 18,659”. A set shown whole that the reader did not search or filter, such as a short table, a paper's versions or a group's categories, has no count."
  - "**A control is filed under what it does.** A Permalink switch is a reading feature, not an accessibility one, and a way to add alt text sits beside the figures. Filed under another topic, a control is both hidden and mislabelled."
  - "**A group of blocks, such as a sidebar, is ordered by value**, the most used first, and shown in the same order as the markup, so a screen reader meets the main action first too."
  - "**When chrome has to shrink, keep the control readers use often** and let one they use rarely go, as a paper's TOC bar keeps its contents list before a mode switch."
  - "**Prefer disabling to removing.** When one page of a group cannot use a control the other pages have, show it disabled there, so every page of the group keeps one layout and the reader learns where the control lives. This is a default, not a rule: leave the control out where a disabled one would mislead."
---

# Organize complex page content

How to arrange a page around what its users need and what patterns and components to reach for. This page does not show the patterns themselves. It provides guidelines to content organization and links to the pages where the examples are shown. Learn about the page container and page areas on [Layouts](layouts.md).

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Evaluating user needs

What a user needs to learn determines the right organizational pattern to employ for any group of content. Use the four questions below as a starting point. Each question has a test and a set of patterns that answer it. Most content will fit under one of these questions. Have an edge case? Discuss it with the design team.

> Where am I? (The address or the item changes): [Header](header.md) and [secondary navigation](navigation.md#secondary-navigation): sections of a site or tool; [Steps](navigation.md#steps): an ordered process; [Pager](pager.md): a queue, one item at a time; [Numbered pages](pager.md#numbered-pages): a long list split across pages; [TOC bar](navigation.md#toc-bar): sections of one page

> What matters here? (Directing user attention): [Spacing](spacing.md) and [dividers](dividers.md): separate content; [Page container](layouts.md#the-page-container), [secondary zones](layouts.md#secondary-zones) and [wide page](layouts.md#wide-page): the page frame; [Sidebar](layouts.md#sidebar) and [marginalia](layouts.md#marginalia): supporting content; [Cards](cards.md) and [tables](tables.md): records; [Cards that link](cards.md#cards-that-link): a page that sends the reader on

> Which part do I need? (The content swaps in place): [Tabs](progressive-disclosure.md#tabs): one view at a time; [Filters](filters.md): narrowed data; [Sections of one page](typography.md#the-heading-scale): views to compare

> Can I learn more? (Richer details are revealed upon request): [Tooltip](forms.md#tooltip) and [popover](progressive-disclosure.md#popover): detail on request; [Show more](progressive-disclosure.md#show-more) and [accordion](progressive-disclosure.md#accordion): more in the flow; [Modal](modals.md): a decision first; [Actions attached to content](buttons.md#small-actions-attached-to-content): act on one item

## The main content comes first

Before choosing components, decide what the page is for and which content is primary. Everything else is arranged so it does not push the primary content down.

**Rule.** **The page heading is followed by the main content.** At most one short line comes between them: a line that sets the data in context, such as the period it covers. An explanation of the figures is secondary: see [Where secondary content goes](#where-secondary-content-goes).

**Rule.** **What the reader must know before acting comes before the steps it governs**, even when the steps are what they came for. On a withdrawal page, what makes a withdrawal reason acceptable comes before how to submit one.

**Rule.** **A state that changes how the whole page reads is met first.** The page's `<title>` starts with it, and its notice comes straight after the page heading, before anything else; on a paper the heading starts with it too. A reader, and a screen reader, meets it before reading on. See [a withdrawn paper](papers.md#withdrawn-papers) and [a form with errors](forms.md#alerts-in-forms).

## Where secondary content goes

Each kind of secondary content has a home that keeps the main content high and wide. Compare at least two homes for each piece, and keep the one that leaves the main content highest and widest.

**Rule.** **A line or two: a line below the main content.** A short note, such as what the figures count, reads as a footnote. It needs no heading and no accordion.

**Rule.** **A labelled section the reader may want: an [accordion](progressive-disclosure.md#accordion)** below the main content. An accordion holds more than a line or two.

**Rule.** **The rest of a list whose first items matter most: [show more](progressive-disclosure.md#show-more)**, such as authors after the first eight. A list of equal items, such as the categories a report covers, is shown or hidden whole.

**Rule.** **A list or explanation the reader opens when needed: a [popover](progressive-disclosure.md#popover) or a [modal](modals.md)**, opened from a button with a visible label, such as “Categories (40)” or “About these charts” beside the heading; an icon on its own is easy to miss. A popover opens beside its button and leaves the page usable; a modal takes over the page while the reader looks through it.

**Rule.** **A sentence about one label or control: a [tooltip](forms.md#tooltip).**

**Rule.** **Supporting content beside short main content: a [sidebar](layouts.md#sidebar).**

## Where controls go

A control sits with what it changes. The more of the site it changes, the higher it sits on the page.

**Rule.** **A tool or filter for every page under the header, whether a whole site or a whole tool: the header's centred space**, on the header's background. Nothing sits higher. Use it sparingly. See [Header](header.md#design-rules).

**Rule.** **A choice between the sections of a tool: the section menu**, at the start of the second row, on the accent tint. It is navigation. See [Two levels of navigation](navigation.md#two-levels-of-navigation).

**Rule.** **A filter for the whole page: the page's opening band**, a `.ds-full.ds-zone-secondary` band under the page heading. See [Secondary zones](layouts.md#secondary-zones).

**Rule.** **Filters, sort and group actions for one set of data: the set's header bar**, on one line, even when the set's only control is one action, such as Copy emails. See [Filters](filters.md) and [Cards with a header bar](cards.md#cards-with-a-header-bar). A table sorts from its [column headers](tables.md#sortable-column-headers).

**Rule.** **Selecting items in a list: the checkbox at the start of each item, and the actions on the selection in the set's header bar.** A control for one item only goes at the end of that item, on the right. See [Selecting items in a list](tables.md#selecting-items-in-a-list).

**Rule.** **A control for the whole page sits at least as far above the first set of data as the sets sit from each other**, so it reads as the page's and not the first set's.

## Long pages

Long pages need special consideration of their organization. The longer the page, the more we need to think about [navigation](navigation.md), defining [page zones](layouts.md#secondary-zones), and [not losing your place](../references.html#getting-back-after-a-jump).

**Rule.** **The contents bar hangs from the opening band.** A page with a contents bar has an opening band with its title and an introduction of one to five sentences. See [Secondary zones](layouts.md#secondary-zones). A paper is the exception: its contents bar holds the paper's tools and sits under the site header ([The TOC bar on a paper](papers.md#paper-toc-bar)).

**Rule.** **On a page with a contents bar, all content sits under headings**, so the bar lists every part of the page. An introduction longer than five sentences keeps its first sentences in the band; the rest goes under a heading of its own.

## Rules

- **Choose typographic and proximity-based organization patterns first**, and reach for visible containers only when called for. This is the organizing principle to follow throughout.
- **Use only the questions the content raises.** When a page uses more than one layer, they stack in this order: navigation, then tabs, then filters.
- **A page in a set follows the set.** Pages in one section of a site, such as arXiv's help pages, share one template: the opening band and the contents bar are on every page of the set or on none. Before choosing, find out whether the page belongs to a set and what the set already uses. If no one has said, ask; if you cannot ask, say what you assumed.
- **In a set that uses the opening band, every page has an introduction**: one to five sentences that say what the whole page is for. Use the page's own text only if it introduces the whole page; a sentence that opens a section introduces that section, not the page. Otherwise write a sentence or two.
- **A page outside a set, or in a set without the band, decides for itself.** Without the band it has no contents bar and no introduction.
- **When a filter sets what the whole page is about, the page heading names the choice**, as in “Charts for cs”, and so does the page's `<title>`, so tabs, history and bookmarks tell the choices apart. With nothing chosen, the heading is the view alone. A filter that narrows one set on the page never changes the heading.
- **A page with little on it needs no section headings.** The page heading names it; a heading such as “Subject groups” under “All sections” adds nothing.
- **A link in the header navigation is not repeated on the page**, and no link on the page repeats the page heading.
- **One name for one thing.** Choose one word for each kind of thing, such as “section”, and use it in every heading, link and sentence.
- **Show readers what they can use.** A page shows each reader only what their permissions allow; inside an internal tool it does not label parts of the page with who may see them. A privileged control on a public page is the exception: it says it is privileged, as [DESIGN-POLICIES.md](../doc.html?src=docs/DESIGN-POLICIES.md) requires.
- **Reveal on request rather than add a setting.** Something a reader needs now and then opens when they ask for it, as a popover or a tooltip does. A setting that keeps it on screen adds noise for everyone else.
- **A count says what the reader cannot see for themselves.** Search results always have one, even for a few results: the range at the top of the results, “1–3 of 3 results”. See [Search](search.md#results); no results is a message. A set the reader has filtered ends its header bar with how much is left, “3 of 120 holds”. See [Filters](filters.md#rules). A list longer than one page states its range in its [pager](pager.md), “1–50 of 18,659”. A set shown whole that the reader did not search or filter, such as a short table, a paper's versions or a group's categories, has no count.
- **A control is filed under what it does.** A Permalink switch is a reading feature, not an accessibility one, and a way to add alt text sits beside the figures. Filed under another topic, a control is both hidden and mislabelled.
- **A group of blocks, such as a sidebar, is ordered by value**, the most used first, and shown in the same order as the markup, so a screen reader meets the main action first too.
- **When chrome has to shrink, keep the control readers use often** and let one they use rarely go, as a paper's TOC bar keeps its contents list before a mode switch.
- **Prefer disabling to removing.** When one page of a group cannot use a control the other pages have, show it disabled there, so every page of the group keeps one layout and the reader learns where the control lives. This is a default, not a rule: leave the control out where a disabled one would mislead.
