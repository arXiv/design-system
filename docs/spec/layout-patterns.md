---
page: layout-patterns.html
title: "Layout patterns"
summary: "This section covers our primary patterns for differentiating and organizing content based on user needs. The organizing principle to follow throughout: Choose typographic and proximity-based organization patterns first, reach for visible containers only when called for."
stylesheet: design-system.css
components:
  - id: evaluating-user-needs
    title: "Evaluating user needs"
    summary: "What a user needs to learn determines the right organizational pattern to employ for any group of content. Use the four questions below as a starting point. Each question has a test and a set of patterns that answer it. Most content will fit under one of these questions. Have an edge case? Discuss it with the design team."
    notes:
      - "Where am I? (The address or the item changes): [Header](header.md) and [secondary navigation](navigation.md#secondary-navigation): sections of a site or tool; [Steps](navigation.md#steps): an ordered process; [Pager](pager.md): a queue, one item at a time; [Numbered pages](pager.md#numbered-pages): a long list split across pages; [TOC bar](progressive-disclosure.md#toc-bar): sections of one long page"
      - "What matters here? (Directing user attention): [Spacing](spacing.md) and [dividers](#dividers): separate content; [Page container](#the-page-container), [page zones](#page-zones) and [wide page](#wide-page): the page frame; [Sidebar](#sidebar) and [marginalia](#marginalia): supporting content; [Cards](cards.md) and [tables](tables.md): records; [Cards that link](cards.md#cards-that-link): a page that sends the reader on"
      - "Which part do I need? (The content swaps in place): [Tabs](progressive-disclosure.md#tabs): one view at a time; [Filters](filters.md): narrowed data; [Sections of one page](typography.md#the-heading-scale): views to compare"
      - "Can I learn more? (Richer details are revealed upon request): [Tooltip](forms.md#tooltip) and [popover](progressive-disclosure.md#popover): detail on request; [Show more](progressive-disclosure.md#show-more) and [accordion](progressive-disclosure.md#accordion): more in the flow; [Modal](modals.md): a decision first; [Actions attached to content](buttons.md#small-actions-attached-to-content): act on one item"
  - id: the-main-content-comes-first
    title: "The main content comes first"
    summary: "Before choosing components, decide what the page is for and which content is primary. Everything else is arranged so it does not push the primary content down."
    rules:
      - "**A page either sends the reader on or is where they work.** A page that sends the reader on, such as a list of sections or reports, shows each destination as a [card that links](cards.md#cards-that-link), with only what helps the reader choose. A page where the reader reads, compares or acts on records uses [tables](tables.md) and [filters](filters.md)."
      - "**Leave detailed figures for the page they belong to.** A card shows a name and, at most, a count or a mark that something needs attention; the figures are on the page it opens."
      - "**The page heading is followed by the main content.** At most one short line comes between them. A line that sets the data in context, such as the period it covers and when it was last updated, goes there, just above the main content. The refresh control ends that line: a text button with the refresh icon (`refresh-cw`). An explanation of the figures is secondary: see [Where secondary content goes](#where-secondary-content-goes)."
      - "**Controls for a list sit on one line in its header bar.** See [Where controls go](#where-controls-go)."
      - "**A page with little on it needs no section headings.** The page heading names it; a heading such as “Subject groups” under “All sections” adds nothing."
      - "**A link in the header navigation is not repeated on the page**, and no link on the page repeats the page heading."
      - "**One name for one thing.** Choose one word for each kind of thing, such as “section”, and use it in every heading, link and sentence."
      - "**Mark what needs attention where it is.** A status tag on the card or row, not an alert that lists the items, which the reader then has to find."
      - "**Only the page's main action is a primary button.** Refresh, export and other secondary actions are text buttons."
      - "**Show readers what they can use, without labelling their access.** A page shows each reader only what their permissions allow. It does not label parts of the page with who is allowed to see them."
      - "**Dense pages do not organise content with [page zones](#page-zones)**, and neither do the lighter pages of the same tool, so every page of the tool looks the same. The one band a dense page uses is an opening band that holds a filter for the whole page."
      - "**A state that changes how the whole page reads is met first.** The page's `<title>` starts with it, and its notice comes straight after the page heading, before anything else; on a paper the heading starts with it too. A reader, and a screen reader, meets it before reading on. See [a withdrawn paper](../versions.html#withdrawn-papers) and [a form with errors](forms.md#alerts-in-forms)."
      - "**When a record's main content is gone, what acts on it goes too.** Its name, identity and details stay. No column is left empty: what remains takes the row."
  - id: where-secondary-content-goes
    title: "Where secondary content goes"
    summary: "Each kind of secondary content has a home that keeps the main content high and wide. Compare at least two homes for each piece, and keep the one that leaves the main content highest and widest."
    rules:
      - "**A line or two: a line below the main content.** A short note, such as what the figures count, reads as a footnote. It needs no heading and no accordion."
      - "**A labelled section the reader may want: an [accordion](progressive-disclosure.md#accordion)** below the main content. An accordion holds more than a line or two."
      - "**The rest of a list whose first items matter most: [show more](progressive-disclosure.md#show-more)**, such as authors after the first eight. A list of equal items, such as the categories a report covers, is shown or hidden whole."
      - "**A list or explanation the reader opens when needed: a [popover](progressive-disclosure.md#popover) or a [modal](modals.md)**, opened from a button with a visible label, such as “Categories (40)” or “About these charts” beside the heading; an icon on its own is easy to miss. A popover opens beside its button and leaves the page usable; a modal takes over the page while the reader looks through it."
      - "**A sentence about one label or control: a [tooltip](forms.md#tooltip).**"
      - "**Supporting content beside short main content: a [sidebar](#sidebar).**"
      - "**Never a band across the main content.** Supporting material goes beside the opening, in a sidebar, or after all of the main content, in a closing band. A band between two parts of the main content interrupts the reading."
      - "**A sidebar starts level with the block it supports.** Above it, the page heading and any long one-line content, such as a paper's title and authors, use the full width: titles can be very long, and an author list reads better on one wide line."
      - "**Reveal on request rather than add a setting.** Something a reader needs now and then opens when they ask for it, as a popover or a tooltip does. A setting that keeps it on screen adds noise for everyone else."
  - id: where-controls-go
    title: "Where controls go"
    summary: "A control sits with what it changes. The more of the site it changes, the higher it sits on the page."
    rules:
      - "**A tool or filter for the whole site: the header's centred space**, on the header's background. Use it sparingly. See [Header](header.md#design-rules)."
      - "**A choice between the sections of a tool: the section menu**, at the start of the second row, on the accent tint. It is navigation. See [Two levels of navigation](navigation.md#two-levels-of-navigation)."
      - "**A filter for the whole page: the page's opening band**, a `.ds-full.ds-zone-secondary` band under the page heading. See [Page zones](#page-zones)."
      - "**Filters, sort and group actions for one set of data: the set's header bar**, on one line. See [Filters](filters.md) and [Cards with a header bar](cards.md#cards-with-a-header-bar). A table sorts from its [column headers](tables.md#sortable-column-headers)."
      - "**A set with no controls is not in a card.** It sits on the page ground under its heading."
      - "**A control for the whole page sits at least as far above the first set of data as the sets sit from each other**, so it reads as the page's and not the first set's."
      - "**A control is filed under what it does.** A Permalink switch is a reading feature, not an accessibility one, and a way to add alt text sits beside the figures. Filed under another topic, a control is both hidden and mislabelled."
      - "**A group of blocks, such as a sidebar, is ordered by value**, the most used first, and shown in the same order as the markup, so a screen reader meets the main action first too."
      - "**When chrome has to shrink, keep the control readers use often** and let one they use rarely go, as a paper's TOC bar keeps its contents list before a mode switch."
      - "**Width decides where a control sits; the pointer decides its size.** A narrow window on a laptop still has a mouse. Give larger targets and tap-to-reveal where the pointer is coarse, never because the window is narrow."
  - id: the-page-container
    title: "The page container"
    summary: "Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Page zones](#page-zones)."
    rules:
      - "**One width per page.** Prose, tables, demos, code and callouts share the reading column, so everything on a page has the same left and right edge. A page that needs a different width changes the width token; it does not add a second width."
      - "**Long-form reading is narrower.** An abstract, a paper body or an explanation read from start to finish targets a line of about 65 characters, set on the page, not on the paragraph."
      - "**Reference pages accept a longer line.** At 850px a line is about 109 characters. That suits short reference paragraphs and two-column layouts; it is not a reason to set long text that wide."
      - "**Few breakpoints, each for a change in structure.** Prefer a layout that needs no query, then a container query, then a media query. Breakpoints about text are in rem; breakpoints about fixed widths are in px. A threshold that CSS and JavaScript share is a custom property, read by the script with `getComputedStyle`."
  - id: sidebar
    title: "Sidebar"
    summary: "A sidebar sits to the right of the main column and contains supplementary content. If the content is secondary, distinct from the main content, and it is important that it not be pushed far down the page, then a sidebar is appropriate."
    classes:
      - name: ".ds-sidebar"
        does: "On an `<aside>` with an `aria-label` that names what it holds: a complementary landmark. Its parent becomes the two-column layout, with the main content taking the spare width, the sidebar 17rem wide, and `--ds-space-section` between them. A border frames it, with 8px inside (`--ds-space-2`), and a line separates its blocks, 16px apart (`--ds-space-4`). Its text is 13px. Nothing in it is sticky."
      - name: "<aside>"
        does: "The sidebar comes after the main content in the markup. When the two no longer fit side by side, the sidebar wraps below the content at full width, 24px below it (`--ds-space-6`), and a screen reader meets the article first."
      - name: ".ds-acc"
        does: "An accordion inside the sidebar is the same ruled accordion as anywhere else, a step smaller to match the sidebar's text, and single-column for the narrow measure. Several in a row go in a `.ds-acc-stack`. No extra class."
    rules:
      - "**A sidebar is for a page whose main content is about as long as the sidebar**, such as an abstract page beside its versions and citation. The main content gives up the sidebar's width and the gap, about 22rem."
      - "**When the main content needs its width or runs long, choose another home.** Charts, tables and wide pages need the width, and beside a long main column a sidebar leaves an empty column for most of the page. See [Where secondary content goes](#where-secondary-content-goes)."
  - id: dividers
    title: "Dividers"
    summary: "A rule between things. It belongs in the same conversation as the card, because both answer the same question and the answer is usually neither: this system groups with space first, and a line drawn where space would have done adds noise without adding meaning."
    classes:
      - name: "<hr>"
        does: "The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role=\"separator\"` for free."
      - name: ".ds-divider--tight"
        does: "Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning."
      - name: ".ds-divider--flush"
        does: "No margin at all; the caller owns the spacing."
      - name: ".ds-divider"
        does: "The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`."
      - name: ".ds-divider--vertical"
        does: "For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context."
  - id: marginalia
    title: "Marginalia and gutter space"
    summary: "At wide screen widths, our max content width leaves enough gutter space on the sides for marginalia. A short note beside the block it belongs to is appropriate for annotation-style content. At narrower widths, it is hidden in an info icon in the block’s top-right corner. Try it by widening and narrowing your screen."
    classes:
      - name: ".ds-marginalia"
        does: "The note, a `<details>`. Its first child in the block, so it is read before the thing it annotates. The block supplies `position: relative`; `.ds-card` already does."
      - name: ".ds-marginalia-body"
        does: "The text, with `.ds-annotation` for the voice. In the margin it has no chrome; folded, it opens as a small panel under the mark."
      - name: ".is-sr-only"
        does: "Required on the mark. The icon is `aria-hidden`, so without it the control announces as nothing."
    notes:
      - "A margin note is one or two sentences. Anything longer belongs in the main content."
    rules:
      - "**No JavaScript required.** Even the info links use a native disclosure."
      - "**The marginalia appear at 1314px width.** The page width plus a note and its gaps on each side. Below that width, marginal notes are hidden behind an info icon."
      - "**A note should never contain required information.** A reader on a narrow screen may never open or see it, so annotations must contain only optional content."
  - id: page-zones
    title: "Page zones"
    group: "Modifiers"
    summary: "The default page background is white, and that is the color that primary page content sits on. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material. The zone is named for its role, because the ground changes in dark mode."
    classes:
      - name: ".ds-zone-secondary"
        does: "Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode."
      - name: ".ds-full"
        does: "On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own."
    rules:
      - "**Dense pages do not use page zones.** On an admin tool or a data view, where the reader needs to find and act on content quickly, a tinted band pushes the main content too far down the page. Separate content with spacing and headings instead. The one exception is an opening band that holds a filter for the whole page, as in [Where controls go](#where-controls-go)."
      - "**Only a direct child can run full width.** `.ds-full` works on children of `.ds-container`; nested deeper it does nothing."
      - "**Do not build a full-width band with negative margins and `100vw`.** `100vw` includes the scrollbar, so a band built that way is wider than the page, and the page scrolls sideways on Windows and Linux. `.ds-full` measures the container instead, so it fits exactly."
  - id: wide-page
    title: "Wide page"
    group: "Modifiers"
    summary: "A dense internal tool can use a wider page: 1080px instead of 850px. Use it for tables and filters that do not fit the standard width, not for prose."
rules:
  - "**Use only the questions the content raises.** When a page uses more than one layer, they stack in this order: navigation, then tabs, then filters."
  - "**One control of each kind per view.** Never two rows of tabs, and never two filter bars."
  - "**No tabs inside a tab panel.**"
  - "**Filters apply to everything below them.**"
  - "**One Apply button per filter bar.**"
  - "**A number that changes a calculation is a setting, not a filter.**"
  - "**No breadcrumbs.** See [Header](header.md), *Rules*."
  - "**One main landmark.** Put the page's content in a single `<main>`. A page with two, or with none, gives a screen-reader user nothing to jump to."
  - "**Label every aside.** A sidebar is an `<aside>` with an `aria-label` that says what it holds, so it announces as a complementary landmark with a name, not as part of the article."
  - "**Headings continue the outline inside a card.** A heading inside a container takes the next level down from the section it sits in. Do not skip a level because the content is in a card."
  - "**Use native disclosure.** Build accordions, margin notes and the TOC bar on `<details>` and `<summary>`: the summary is focusable and toggles with Enter and Space for free. Do not rebuild them from `<div>` elements and click handlers."
  - "**Nothing required lives only in a collapsed panel.** Anything legally or practically required, such as a warning or a licence, must also exist in always-visible flow. A closed accordion, a folded margin note and a popover are all places a reader may never open."
---

# Layout patterns

This section covers our primary patterns for differentiating and organizing content based on user needs. The organizing principle to follow throughout: Choose typographic and proximity-based organization patterns first, reach for visible containers only when called for.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Evaluating user needs

What a user needs to learn determines the right organizational pattern to employ for any group of content. Use the four questions below as a starting point. Each question has a test and a set of patterns that answer it. Most content will fit under one of these questions. Have an edge case? Discuss it with the design team.

> Where am I? (The address or the item changes): [Header](header.md) and [secondary navigation](navigation.md#secondary-navigation): sections of a site or tool; [Steps](navigation.md#steps): an ordered process; [Pager](pager.md): a queue, one item at a time; [Numbered pages](pager.md#numbered-pages): a long list split across pages; [TOC bar](progressive-disclosure.md#toc-bar): sections of one long page

> What matters here? (Directing user attention): [Spacing](spacing.md) and [dividers](#dividers): separate content; [Page container](#the-page-container), [page zones](#page-zones) and [wide page](#wide-page): the page frame; [Sidebar](#sidebar) and [marginalia](#marginalia): supporting content; [Cards](cards.md) and [tables](tables.md): records; [Cards that link](cards.md#cards-that-link): a page that sends the reader on

> Which part do I need? (The content swaps in place): [Tabs](progressive-disclosure.md#tabs): one view at a time; [Filters](filters.md): narrowed data; [Sections of one page](typography.md#the-heading-scale): views to compare

> Can I learn more? (Richer details are revealed upon request): [Tooltip](forms.md#tooltip) and [popover](progressive-disclosure.md#popover): detail on request; [Show more](progressive-disclosure.md#show-more) and [accordion](progressive-disclosure.md#accordion): more in the flow; [Modal](modals.md): a decision first; [Actions attached to content](buttons.md#small-actions-attached-to-content): act on one item

## The main content comes first

Before choosing components, decide what the page is for and which content is primary. Everything else is arranged so it does not push the primary content down.

**Rule.** **A page either sends the reader on or is where they work.** A page that sends the reader on, such as a list of sections or reports, shows each destination as a [card that links](cards.md#cards-that-link), with only what helps the reader choose. A page where the reader reads, compares or acts on records uses [tables](tables.md) and [filters](filters.md).

**Rule.** **Leave detailed figures for the page they belong to.** A card shows a name and, at most, a count or a mark that something needs attention; the figures are on the page it opens.

**Rule.** **The page heading is followed by the main content.** At most one short line comes between them. A line that sets the data in context, such as the period it covers and when it was last updated, goes there, just above the main content. The refresh control ends that line: a text button with the refresh icon (`refresh-cw`). An explanation of the figures is secondary: see [Where secondary content goes](#where-secondary-content-goes).

**Rule.** **Controls for a list sit on one line in its header bar.** See [Where controls go](#where-controls-go).

**Rule.** **A page with little on it needs no section headings.** The page heading names it; a heading such as “Subject groups” under “All sections” adds nothing.

**Rule.** **A link in the header navigation is not repeated on the page**, and no link on the page repeats the page heading.

**Rule.** **One name for one thing.** Choose one word for each kind of thing, such as “section”, and use it in every heading, link and sentence.

**Rule.** **Mark what needs attention where it is.** A status tag on the card or row, not an alert that lists the items, which the reader then has to find.

**Rule.** **Only the page's main action is a primary button.** Refresh, export and other secondary actions are text buttons.

**Rule.** **Show readers what they can use, without labelling their access.** A page shows each reader only what their permissions allow. It does not label parts of the page with who is allowed to see them.

**Rule.** **Dense pages do not organise content with [page zones](#page-zones)**, and neither do the lighter pages of the same tool, so every page of the tool looks the same. The one band a dense page uses is an opening band that holds a filter for the whole page.

**Rule.** **A state that changes how the whole page reads is met first.** The page's `<title>` starts with it, and its notice comes straight after the page heading, before anything else; on a paper the heading starts with it too. A reader, and a screen reader, meets it before reading on. See [a withdrawn paper](../versions.html#withdrawn-papers) and [a form with errors](forms.md#alerts-in-forms).

**Rule.** **When a record's main content is gone, what acts on it goes too.** Its name, identity and details stay. No column is left empty: what remains takes the row.

## Where secondary content goes

Each kind of secondary content has a home that keeps the main content high and wide. Compare at least two homes for each piece, and keep the one that leaves the main content highest and widest.

**Rule.** **A line or two: a line below the main content.** A short note, such as what the figures count, reads as a footnote. It needs no heading and no accordion.

**Rule.** **A labelled section the reader may want: an [accordion](progressive-disclosure.md#accordion)** below the main content. An accordion holds more than a line or two.

**Rule.** **The rest of a list whose first items matter most: [show more](progressive-disclosure.md#show-more)**, such as authors after the first eight. A list of equal items, such as the categories a report covers, is shown or hidden whole.

**Rule.** **A list or explanation the reader opens when needed: a [popover](progressive-disclosure.md#popover) or a [modal](modals.md)**, opened from a button with a visible label, such as “Categories (40)” or “About these charts” beside the heading; an icon on its own is easy to miss. A popover opens beside its button and leaves the page usable; a modal takes over the page while the reader looks through it.

**Rule.** **A sentence about one label or control: a [tooltip](forms.md#tooltip).**

**Rule.** **Supporting content beside short main content: a [sidebar](#sidebar).**

**Rule.** **Never a band across the main content.** Supporting material goes beside the opening, in a sidebar, or after all of the main content, in a closing band. A band between two parts of the main content interrupts the reading.

**Rule.** **A sidebar starts level with the block it supports.** Above it, the page heading and any long one-line content, such as a paper's title and authors, use the full width: titles can be very long, and an author list reads better on one wide line.

**Rule.** **Reveal on request rather than add a setting.** Something a reader needs now and then opens when they ask for it, as a popover or a tooltip does. A setting that keeps it on screen adds noise for everyone else.

## Where controls go

A control sits with what it changes. The more of the site it changes, the higher it sits on the page.

**Rule.** **A tool or filter for the whole site: the header's centred space**, on the header's background. Use it sparingly. See [Header](header.md#design-rules).

**Rule.** **A choice between the sections of a tool: the section menu**, at the start of the second row, on the accent tint. It is navigation. See [Two levels of navigation](navigation.md#two-levels-of-navigation).

**Rule.** **A filter for the whole page: the page's opening band**, a `.ds-full.ds-zone-secondary` band under the page heading. See [Page zones](#page-zones).

**Rule.** **Filters, sort and group actions for one set of data: the set's header bar**, on one line. See [Filters](filters.md) and [Cards with a header bar](cards.md#cards-with-a-header-bar). A table sorts from its [column headers](tables.md#sortable-column-headers).

**Rule.** **A set with no controls is not in a card.** It sits on the page ground under its heading.

**Rule.** **A control for the whole page sits at least as far above the first set of data as the sets sit from each other**, so it reads as the page's and not the first set's.

**Rule.** **A control is filed under what it does.** A Permalink switch is a reading feature, not an accessibility one, and a way to add alt text sits beside the figures. Filed under another topic, a control is both hidden and mislabelled.

**Rule.** **A group of blocks, such as a sidebar, is ordered by value**, the most used first, and shown in the same order as the markup, so a screen reader meets the main action first too.

**Rule.** **When chrome has to shrink, keep the control readers use often** and let one they use rarely go, as a paper's TOC bar keeps its contents list before a mode switch.

**Rule.** **Width decides where a control sits; the pointer decides its size.** A narrow window on a laptop still has a mouse. Give larger targets and tap-to-reveal where the pointer is coarse, never because the window is narrow.

## The page container

Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Page zones](#page-zones).

**Rule.** **One width per page.** Prose, tables, demos, code and callouts share the reading column, so everything on a page has the same left and right edge. A page that needs a different width changes the width token; it does not add a second width.

**Rule.** **Long-form reading is narrower.** An abstract, a paper body or an explanation read from start to finish targets a line of about 65 characters, set on the page, not on the paragraph.

**Rule.** **Reference pages accept a longer line.** At 850px a line is about 109 characters. That suits short reference paragraphs and two-column layouts; it is not a reason to set long text that wide.

**Rule.** **Few breakpoints, each for a change in structure.** Prefer a layout that needs no query, then a container query, then a media query. Breakpoints about text are in rem; breakpoints about fixed widths are in px. A threshold that CSS and JavaScript share is a custom property, read by the script with `getComputedStyle`.

## Sidebar

A sidebar sits to the right of the main column and contains supplementary content. If the content is secondary, distinct from the main content, and it is important that it not be pushed far down the page, then a sidebar is appropriate.

```html
<div>
<article>…</article>
<aside class="ds-sidebar" aria-label="Paper details">
  <div class="ds-acc-stack">
    <details class="ds-acc" open>
      <summary>Versions</summary>
      <div class="ds-acc-body">
        <dl>
          <dt>v3 · current</dt><dd>24 Apr 2026</dd>
          <dt>v2</dt><dd><a href="#">2 Mar 2026</a></dd>
        </dl>
      </div>
    </details>
    <details class="ds-acc">
      <summary>Paper information</summary>
      <div class="ds-acc-body">…</div>
    </details>
  </div>
</aside>
</div>
```

- `.ds-sidebar` — On an `<aside>` with an `aria-label` that names what it holds: a complementary landmark. Its parent becomes the two-column layout, with the main content taking the spare width, the sidebar 17rem wide, and `--ds-space-section` between them. A border frames it, with 8px inside (`--ds-space-2`), and a line separates its blocks, 16px apart (`--ds-space-4`). Its text is 13px. Nothing in it is sticky.
- `<aside>` — The sidebar comes after the main content in the markup. When the two no longer fit side by side, the sidebar wraps below the content at full width, 24px below it (`--ds-space-6`), and a screen reader meets the article first.
- `.ds-acc` — An accordion inside the sidebar is the same ruled accordion as anywhere else, a step smaller to match the sidebar's text, and single-column for the narrow measure. Several in a row go in a `.ds-acc-stack`. No extra class.

**Rule.** **A sidebar is for a page whose main content is about as long as the sidebar**, such as an abstract page beside its versions and citation. The main content gives up the sidebar's width and the gap, about 22rem.

**Rule.** **When the main content needs its width or runs long, choose another home.** Charts, tables and wide pages need the width, and beside a long main column a sidebar leaves an empty column for most of the page. See [Where secondary content goes](#where-secondary-content-goes).

## Dividers

A rule between things. It belongs in the same conversation as the card, because both answer the same question and the answer is usually neither: this system groups with space first, and a line drawn where space would have done adds noise without adding meaning.

```html
<p>A section of content.</p>
<hr>
<p>The next section.</p>
<hr>
<p>And the one after it.</p>
```

```html
<p>An item in a group.</p>
<hr class="ds-divider ds-divider--tight">
<p>The next item in the same group.</p>
<hr class="ds-divider ds-divider--tight">
<p>And the one after it.</p>
```

```html
<div class="ds-btn-group">
<span>Search</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Submit</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Donate</span>
</div>
```

- `<hr>` — The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role="separator"` for free.
- `.ds-divider--tight` — Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning.
- `.ds-divider--flush` — No margin at all; the caller owns the spacing.
- `.ds-divider` — The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`.
- `.ds-divider--vertical` — For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context.

## Marginalia and gutter space

At wide screen widths, our max content width leaves enough gutter space on the sides for marginalia. A short note beside the block it belongs to is appropriate for annotation-style content. At narrower widths, it is hidden in an info icon in the block’s top-right corner. Try it by widening and narrowing your screen.

```html
<div class="ds-card">
<details class="ds-marginalia">
  <summary><svg aria-hidden="true">…</svg><span class="is-sr-only">Note</span></summary>
  <p class="ds-marginalia-body ds-annotation">The note.</p>
</details>
…
</div>
```

- `.ds-marginalia` — The note, a `<details>`. Its first child in the block, so it is read before the thing it annotates. The block supplies `position: relative`; `.ds-card` already does.
- `.ds-marginalia-body` — The text, with `.ds-annotation` for the voice. In the margin it has no chrome; folded, it opens as a small panel under the mark.
- `.is-sr-only` — Required on the mark. The icon is `aria-hidden`, so without it the control announces as nothing.

> A margin note is one or two sentences. Anything longer belongs in the main content.

**Rule.** **No JavaScript required.** Even the info links use a native disclosure.

**Rule.** **The marginalia appear at 1314px width.** The page width plus a note and its gaps on each side. Below that width, marginal notes are hidden behind an info icon.

**Rule.** **A note should never contain required information.** A reader on a narrow screen may never open or see it, so annotations must contain only optional content.

## Page zones  (Modifiers)

The default page background is white, and that is the color that primary page content sits on. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material. The zone is named for its role, because the ground changes in dark mode.

```html
<div class="ds-container">
  <div class="ds-full ds-zone-secondary">               <!-- tinted: introduces -->
    <header class="ds-page-header">…</header>
  </div>
  <section>…</section>                                  <!-- page ground: the thing itself -->
  <div class="ds-full ds-zone-secondary">               <!-- tinted: supports -->
    <section>…</section>
  </div>
</div>
```

- `.ds-zone-secondary` — Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode.
- `.ds-full` — On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own.

**Rule.** **Dense pages do not use page zones.** On an admin tool or a data view, where the reader needs to find and act on content quickly, a tinted band pushes the main content too far down the page. Separate content with spacing and headings instead. The one exception is an opening band that holds a filter for the whole page, as in [Where controls go](#where-controls-go).

**Rule.** **Only a direct child can run full width.** `.ds-full` works on children of `.ds-container`; nested deeper it does nothing.

**Rule.** **Do not build a full-width band with negative margins and `100vw`.** `100vw` includes the scrollbar, so a band built that way is wider than the page, and the page scrolls sideways on Windows and Linux. `.ds-full` measures the container instead, so it fits exactly.

## Wide page  (Modifiers)

A dense internal tool can use a wider page: 1080px instead of 850px. Use it for tables and filters that do not fit the standard width, not for prose.

## Rules

- **Use only the questions the content raises.** When a page uses more than one layer, they stack in this order: navigation, then tabs, then filters.
- **One control of each kind per view.** Never two rows of tabs, and never two filter bars.
- **No tabs inside a tab panel.**
- **Filters apply to everything below them.**
- **One Apply button per filter bar.**
- **A number that changes a calculation is a setting, not a filter.**
- **No breadcrumbs.** See [Header](header.md), *Rules*.
- **One main landmark.** Put the page's content in a single `<main>`. A page with two, or with none, gives a screen-reader user nothing to jump to.
- **Label every aside.** A sidebar is an `<aside>` with an `aria-label` that says what it holds, so it announces as a complementary landmark with a name, not as part of the article.
- **Headings continue the outline inside a card.** A heading inside a container takes the next level down from the section it sits in. Do not skip a level because the content is in a card.
- **Use native disclosure.** Build accordions, margin notes and the TOC bar on `<details>` and `<summary>`: the summary is focusable and toggles with Enter and Space for free. Do not rebuild them from `<div>` elements and click handlers.
- **Nothing required lives only in a collapsed panel.** Anything legally or practically required, such as a warning or a licence, must also exist in always-visible flow. A closed accordion, a folded margin note and a popover are all places a reader may never open.
