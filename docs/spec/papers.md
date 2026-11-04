---
page: papers.html
title: "Papers"
summary: "Displaying paper-related content is arXiv's richest, most complex, and highest stakes design challenge. This page gathers together guidelines that help us display papers and paper-related content consistently and accessibly. It is applicable to both HTML papers pages and search results. More relevant documentation: [Indicating which version is being read](../versions.html) and [following references without losing your place](../references.html)."
stylesheet: design-system.css
components:
  - id: the-metadata-hierarchy
    title: "The metadata hierarchy"
    summary: "This order is based on what we hear from arXiv readers. They focus in on certain information first and want it easy to find, while other content is lower in their reading order. Look for guidance on visual display? This table is purely about hierarchy and content flow. You will find design and display notes elsewhere on this page and in mockups, ."
  - id: a-paper-in-a-list
    title: "A paper in a list"
    summary: "Search results and listings use the metadata hierarchy. We rely on proximity to define rows instead of relying on visual blocks or dividers. Information is close together within each result and with a comfortable gap between result rows."
    classes:
      - name: ".ds-paper-list"
        does: "An `<ol>` of papers. Papers are separated by space, four times the space inside one, with no lines or boxes."
      - name: ".ds-paper"
        does: "One paper, an `<li>`. Its first child is the title: a heading one level below the list's own heading, linked to the abstract page."
      - name: ".ds-paper-when"
        does: "The format links (a `.ds-link-list`) and the dates (`.ds-date-row`) on one line. The links come first in the markup, so a screen reader reaches them straight after the title; the dates are shown first. On a narrow screen the links wrap below the dates."
      - name: ".ds-link-list"
        does: "On a `<p>`: the authors. After eight names, Show more for the rest."
      - name: "<p>"
        does: "The abstract excerpt and its Show more. See [Show more](progressive-disclosure.md#show-more)."
      - name: ".ds-data-list"
        does: "Comments, journal reference, DOI and the arXiv ID, in that order, each label beside its value. A paper shows only the rows it has. See [Data list](cards.md#data-list)."
      - name: ".ds-tag-list"
        does: "The category tags, primary first. See [Displaying categories](#paper-categories). It sits close under the metadata."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 1.3.1](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) Info and Relationships (Level A) and [WCAG 2.2 SC 2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html) Link Purpose (In Context) (Level A)"
  - id: paper-categories
    title: "Displaying categories"
    summary: "A paper's subject categories show as tags, primary first. Each code links to its listing, and its full name appears in a tooltip."
    classes:
      - name: "<a class=\"ds-tag\">"
        does: "Each category is a link to its listing of recent papers, with `.ds-tag--keep-case` so the code keeps its case. See [Tags](tags.md)."
      - name: ".ds-tag--info"
        does: "On the primary category only. The others are the plain grey tag."
      - name: ".ds-tooltip"
        does: "The full name of the category, on hover and on focus, named by the link's `aria-describedby`. The primary one adds “(primary)”. Load `tooltip.js` once on the page. See [Tooltip](forms.md#tooltip)."
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html) Content on Hover or Focus (Level AA)"
  - id: full-papers
    title: "Displaying abstract and primary metadata"
    summary: "On a paper's own page the order is the identity line, the title, the dates and versions, a warning when an older version is open, the authors and the abstract. The version history and the paper's details sit in the sidebar."
    classes:
      - name: ".ds-paper-identity"
        does: "The identity line above the title: the identifier with its version, the primary category code with its full name, the arXiv DOI, and the licence as a link. It is centred, and as a child of `.ds-container` it spans the viewport to the gutters, so it wraps only on narrow screens. The identifier is read out digit by digit from an `.is-sr-only` span; the visible one is hidden from screen readers."
      - name: "<h1>"
        does: "The paper title. The demo here uses an `<h2>` at the size of an `<h1>`, because it sits inside this page."
      - name: ".ds-date-row"
        does: "The dates and the version links, as in [Indicate which version is being read](../versions.html#version-row). Each version link goes to that version's abstract page, never its HTML: an HTML version may not exist for every version."
      - name: ".ds-alert--warning"
        does: "Only when an older version is being viewed. See [Indicate which version is being read](../versions.html#version-row)."
      - name: ".ds-link-list"
        does: "On a `<p>`: the authors, with Show more after eight."
      - name: "<h2 class=\"is-sr-only\">"
        does: "The abstract's heading, “Abstract”, hidden from sight. Sighted readers know the paragraph after the authors is the abstract; screen-reader users can still jump to it by heading. The demo uses an `<h3>`, because its title is an `<h2>`."
      - name: "<p>"
        does: "The abstract, in full."
      - name: "<title>"
        does: "Starts with the status, “Withdrawn:”, so a reader sees it in the browser tab and a screen reader announces it first."
      - name: ".ds-paper-identity"
        does: "The identifier with the notice's version, and the category. With no text to read, the DOI and the licence leave the line; Metadata, in the sidebar, still has the DOI."
      - name: ".ds-paper-status"
        does: "“Withdrawn:” before the title, inside the heading, in the error color. It is its own element, so the author's title is not edited, and it has `lang=\"en\"` because the title may be in another language."
      - name: ".ds-alert--error"
        does: "On a `<section>`: the notice, straight after the title and before the dates. It says who withdrew the paper, gives the reason as they wrote it, in quotes, and links to the last version that can be read. A `<section>` named by its heading, so a screen reader reaches it second and lists it among the headings. No role, because it is in the page as it loads (see [Alerts](alerts.md))."
      - name: ".ds-alert-title"
        does: "On a heading, one level below the title: an `<h2>` on the page. The demo uses an `<h3>` because it sits inside this page."
      - name: ".ds-paper-status"
        does: "“Removed:”, built as “Withdrawn:” is."
      - name: ".ds-alert--error"
        does: "Says that arXiv removed the version, quotes arXiv's comment as written, and says that the full text and files are gone."
      - name: ".ds-date-row"
        does: "Ends with Removed and its date. A removal changes the version in place, so no version is added to the list."
      - name: ".ds-sidebar"
        does: "The column beside the abstract: Files, Cite and Paper information, in that order. See [Sidebar](layout-patterns.md#sidebar). Beside a long paper, its frame keeps the controls together. It grows with its content; it never scrolls inside itself."
      - name: ".ds-panel-label"
        does: "On an `<h2>`: the label of each block, one level below the paper title, so the outline skips no level. The demo uses `<h3>` because it sits inside this page."
      - name: ".ds-paper-files"
        does: "The downloads. PDF is the primary button and fills the sidebar's width; TeX Source, Other formats (when a paper has them) and Ancillary files are text links under it. Each shows its size; TeX Source also shows its file type. Up to two ancillary files are listed by name; with three or more, one line gives the total size and Download all, at the end of the line; the hidden text on the link gives the count."
      - name: "[aria-describedby]"
        does: "On each download, pointing to the paper title, so a screen reader names the paper with the link. The visible words stay the link's name, which meets [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A)."
      - name: ".ds-paper-cite"
        does: "The citation. `.ds-paper-cite-head` holds the Cite label and, on the same line, a compact select (`.ds-form--compact`) to choose the format. Each format is a standard code block, so `copy-code.js` gives it the copy button and its “Copied to clipboard” announcement, and the citation wraps rather than scrolling. `.ds-paper-cite-code` shows the first two lines until the `.ds-show-more` below it opens the rest. Every format is in the page, one `<figure>` each; without JavaScript all four are shown in full with their names, and the select and the button are hidden."
      - name: ".ds-paper-capabilities"
        does: "The accessibility panel: one line per capability the paper has, each a `shield-check` icon from `docs/icons/` and words. Only what is present is listed, and there is no score."
      - name: ".ds-acc"
        does: "Version history, Accessibility and Metadata are accordions, closed by default, grouped under the Paper information label. They share `name=\"paper-info\"`, so only one is open at a time."
    notes:
      - "Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2: the status goes “before the original main title”, and the notice is “a clearly signposted box” in its own color."
      - "Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.5: a removed article keeps “the article’s title, author list, and relevant metadata”, and only “the main text” goes."
    rules:
      - "**You are viewing version 1.** A newer version is available — [version 3, revised 28 Jun 2026](https://arxiv.org/abs/2604.22725v3)."
      - "This paper has been withdrawn by Adrian Palomares.: Reason given: “The main result in Section 3 relies on a gauge condition that does not hold in general. A corrected analysis will be submitted as a new paper.” The withdrawn paper can still be read in [version 3](#v3)."
      - "This version has been removed by arXiv.: “arXiv admin comment: This version has been removed by arXiv administrators as the submitter did not have the rights to agree to the license at the time of submission.” The full text and files are no longer available."
  - id: the-version-row
    title: "The version row"
    summary: "The row under the title gives the paper's dates and links to its other versions; the version being read is in a box. The row changes with the number of versions, with the version being read, and when a paper is withdrawn or removed: [Indicate which version is being read](../versions.html#version-row) shows each case."
  - id: withdrawn-papers
    title: "Withdrawn and removed papers"
    summary: "A withdrawn paper keeps its title, authors, abstract and metadata, and its earlier versions can still be read. A removed version keeps its title, authors, abstract and metadata, but its full text and files are gone. In both cases, a status before the title and a notice after it say what happened."
    classes:
      - name: "<title>"
        does: "Starts with the status, “Withdrawn:”, so a reader sees it in the browser tab and a screen reader announces it first."
      - name: ".ds-paper-identity"
        does: "The identifier with the notice's version, and the category. With no text to read, the DOI and the licence leave the line; Metadata, in the sidebar, still has the DOI."
      - name: ".ds-paper-status"
        does: "“Withdrawn:” before the title, inside the heading, in the error color. It is its own element, so the author's title is not edited, and it has `lang=\"en\"` because the title may be in another language."
      - name: ".ds-alert--error"
        does: "On a `<section>`: the notice, straight after the title and before the dates. It says who withdrew the paper, gives the reason as they wrote it, in quotes, and links to the last version that can be read. A `<section>` named by its heading, so a screen reader reaches it second and lists it among the headings. No role, because it is in the page as it loads (see [Alerts](alerts.md))."
      - name: ".ds-alert-title"
        does: "On a heading, one level below the title: an `<h2>` on the page. The demo uses an `<h3>` because it sits inside this page."
      - name: ".ds-paper-status"
        does: "“Removed:”, built as “Withdrawn:” is."
      - name: ".ds-alert--error"
        does: "Says that arXiv removed the version, quotes arXiv's comment as written, and says that the full text and files are gone."
      - name: ".ds-date-row"
        does: "Ends with Removed and its date. A removal changes the version in place, so no version is added to the list."
    notes:
      - "Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2: the status goes “before the original main title”, and the notice is “a clearly signposted box” in its own color."
      - "Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.5: a removed article keeps “the article’s title, author list, and relevant metadata”, and only “the main text” goes."
    rules:
      - "This paper has been withdrawn by Adrian Palomares.: Reason given: “The main result in Section 3 relies on a gauge condition that does not hold in general. A corrected analysis will be submitted as a new paper.” The withdrawn paper can still be read in [version 3](#v3)."
      - "This version has been removed by arXiv.: “arXiv admin comment: This version has been removed by arXiv administrators as the submitter did not have the rights to agree to the license at the time of submission.” The full text and files are no longer available."
  - id: the-sidebar
    title: "Displaying paper actions and full metadata"
    summary: "Beside the abstract, the sidebar holds downloadable files, a citation tool, and additional paper information, in that order."
    classes:
      - name: ".ds-sidebar"
        does: "The column beside the abstract: Files, Cite and Paper information, in that order. See [Sidebar](layout-patterns.md#sidebar). Beside a long paper, its frame keeps the controls together. It grows with its content; it never scrolls inside itself."
      - name: ".ds-panel-label"
        does: "On an `<h2>`: the label of each block, one level below the paper title, so the outline skips no level. The demo uses `<h3>` because it sits inside this page."
      - name: ".ds-paper-files"
        does: "The downloads. PDF is the primary button and fills the sidebar's width; TeX Source, Other formats (when a paper has them) and Ancillary files are text links under it. Each shows its size; TeX Source also shows its file type. Up to two ancillary files are listed by name; with three or more, one line gives the total size and Download all, at the end of the line; the hidden text on the link gives the count."
      - name: "[aria-describedby]"
        does: "On each download, pointing to the paper title, so a screen reader names the paper with the link. The visible words stay the link's name, which meets [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A)."
      - name: ".ds-paper-cite"
        does: "The citation. `.ds-paper-cite-head` holds the Cite label and, on the same line, a compact select (`.ds-form--compact`) to choose the format. Each format is a standard code block, so `copy-code.js` gives it the copy button and its “Copied to clipboard” announcement, and the citation wraps rather than scrolling. `.ds-paper-cite-code` shows the first two lines until the `.ds-show-more` below it opens the rest. Every format is in the page, one `<figure>` each; without JavaScript all four are shown in full with their names, and the select and the button are hidden."
      - name: ".ds-paper-capabilities"
        does: "The accessibility panel: one line per capability the paper has, each a `shield-check` icon from `docs/icons/` and words. Only what is present is listed, and there is no score."
      - name: ".ds-acc"
        does: "Version history, Accessibility and Metadata are accordions, closed by default, grouped under the Paper information label. They share `name=\"paper-info\"`, so only one is open at a time."
  - id: paper-toc-bar
    title: "The TOC bar on a paper"
    summary: "On a paper, the TOC bar also has the arXiv logo on the left and links to the paper's PDF and TeX source on the right."
    classes:
      - name: ".ds-toc-bar"
        does: "The bar, as on [Progressive disclosure](progressive-disclosure.md#toc-bar). On a paper it is `.ds-full`, the full width of the page."
      - name: ".ds-paper-bar-logo"
        does: "The one-colour Library Grey logo, inlined from `docs/assets/images/logos/logo_arxiv-library-grey.svg` with `fill=\"currentColor\"`, so it follows the theme. It links to the arXiv home page, and its name is “archive home”."
      - name: ".ds-toc-menu"
        does: "The paper's own headings, numbers in `.ds-toc-num`, written into the HTML from LaTeXML's contents list. Subsections are an `<ol>` inside their section's `<li>`, indented to the section's title in smaller type."
      - name: ".ds-paper-tools"
        does: "PDF and Source, each an icon and its name, in a `<nav>` named “Other formats”. The TeX glyph says TeX, so the visible name is “Source”; an `.is-sr-only` “TeX” makes the spoken name “TeX Source”. The icons are `file-text` and `tex` from `docs/icons/`."
  - id: paper-permalinks
    title: "Section permalinks"
    summary: "Each section heading in a paper has a Permalink control that copies the link to that section, including the version."
    classes:
      - name: ".ds-permalink"
        does: "The Permalink control from [Linking to a section](links.md#linking-to-a-section), the same as on every other page. The demo holds it open."
      - name: ".is-sr-only"
        does: "Completes the name: “Permalink to section 2, Setup”. The name starts with the visible word."
      - name: "[role=\"status\"]"
        does: "One region on the page. `anchors.js` writes “Link to section 2, Setup copied” into it, shows the green tick in place of the link icon, and clears both after 2 seconds."
      - name: ".is-active"
        does: "Set on the heading by a tap, on screens without hover."
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A)"
  - id: paper-elements
    title: "Equations, figures and references"
    summary: "A display equation, a figure and a bibliography entry each have a small row of actions on their bottom edge. The row shows on hover, on keyboard focus and after a tap."
    classes:
      - name: ".ds-paper-element"
        does: "The wrapper round one equation, figure or entry. Hovering it, focusing anything inside it, or tapping it shows a hairline border and the pill. The demo holds all three open."
      - name: ".ds-element-pill"
        does: "The actions, as on [Buttons](buttons.md#small-actions-attached-to-content): one tab stop per element, with the arrow keys moving between its actions. Focusing an action shows the pill."
      - name: ".is-sr-only"
        does: "Each action's name says which element it acts on: “Permalink to equation 2.14”, not “Permalink” a hundred times."
      - name: "[aria-pressed]"
        does: "On View TeX, which switches the equation to its TeX and back. Its label becomes “View math”."
      - name: ".ds-marginalia"
        does: "The figure's alt text, under the label “Alt text”, in the margin at wide widths and folded to its info mark when narrower. See [Marginalia](layout-patterns.md#marginalia)."
      - name: ".is-cta"
        does: "Expand, the one main action on a figure. It opens the figure viewer."
      - name: "[role=\"status\"]"
        does: "One region on the page, where the script confirms a copy in words: “Link to equation 2.14 copied”."
    notes:
      - "**Alt text**Line chart of the power spectrum against scale. The solid blue line rises steeply; the dashed red line rises gently."
rules:
  - "**Show the author's text as written.** A title or abstract is never shortened, reworded or corrected. When we display TeX, it is shown exactly as the author wrote it. We excerpt formulas, but never edit them."
  - "**Leave out what a paper does not have.** No empty labels and no placeholders."
  - "**Every date has its label.** Readers confuse submitted and announced dates when either stands alone."
  - "**The primary category comes first** and is told apart by more than colour: its tooltip names it as primary."
  - "**The identity line comes first.** Many readers arrive at a paper directly, without passing its abstract page. It is centred and spans the page to the gutters."
  - "**The abstract has a heading, hidden from sight.** An `<h2 class=\"is-sr-only\">Abstract</h2>` puts it in the heading outline without adding a line above it."
  - "**The paper follows its abstract on the same page.** A reader reaches the first section by scrolling, by the TOC bar or by the skip link, with no click to open the paper."
  - "**The page has one `<main>`**, from the area above the identity line to the end of the paper, the sidebar included. The site header, the TOC bar and the footer are outside it, and the first skip link goes to it. When LaTeXML's output has no `<main>`, the page around the paper supplies it."
  - "**An optional area above the identity line** holds a temporary message or link, such as Back to abstract while readers move to HTML papers. It is `.ds-btn-text` for a link, or an alert for a message."
  - "**The licence is a link, with no explanation.**"
  - "**Other formats, when a paper has them, are a link in the sidebar**, under TeX Source and above Ancillary Files."
  - "**The sidebar order is Files, Cite, Paper information.** Files and Cite are always open; Version history, Accessibility and Metadata, under Paper information, start closed, and only one is open at a time (see [One panel open at a time](progressive-disclosure.md#one-panel-open-at-a-time))."
  - "**Every download shows its size.**"
  - "**A citation names the arXiv identifier and the arXiv DOI**, never the HTML page, even when the paper has a journal reference."
  - "**BibTeX lists every author.** “and others” becomes “et al.” in a reference manager, and the other authors are lost."
  - "**APA, Chicago and MLA follow their own style rules** for long author lists."
  - "**Every citation format is in the page.** The script only chooses which one shows."
  - "**The accessibility panel lists only what the paper has.** A missing capability has no line, and there is no overall score."
  - "**The status goes before the title, never into it.** “Withdrawn:” or “Removed:” is its own element inside the heading, and the page's `<title>` starts with it. The author's title is not edited."
  - "**The notice comes straight after the title, before the dates.** It says who withdrew or removed the paper and gives the reason as written, in quotes."
  - "**Every version of a withdrawn paper shows the notice.** On an earlier version it takes the place of the older-version warning. A reader who arrives at an earlier version by a link must still learn that the paper was withdrawn."
  - "**The withdrawal notice links to the last version that can be read, except on that version.**"
  - "**Without a text, what acts on a text goes.** The paper body, the TOC bar, Files, Cite and the Accessibility panel are left out; the sidebar holds Paper information alone. An earlier version of a withdrawn paper keeps them all."
  - "**A removed version keeps its license, but not its cross-listed categories.** arXiv may remove the license, or any other metadata, when there is a legal reason to, as [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2 allows."
  - "**A citation of an earlier version says the paper was withdrawn.** Each format ends with a note, such as “This paper was withdrawn, 22 Oct 2026”, so the status travels with the citation."
  - "Display guidelines for withdrawn and removed papers follow [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf)."
  - "**The body markup is LaTeXML's, unchanged.** arXiv styles it from outside with CSS and never rewrites, reorders or wraps the author's elements."
  - "**ar5iv's stylesheet is in a cascade layer**, so an ordinary rule outranks it without `!important`. The `arxiv-override` layer is only for a property ar5iv itself marks `!important`."
  - "**Body text is set as on [Typography](typography.md).** ar5iv sets weight 300, so set 400."
  - "**Body text is left-aligned, never justified.** Inline math gives a justified line nowhere to break."
  - "**Body text is hyphenated** with `hyphens: auto`. It needs the page's `lang` attribute, which tells the browser which language to hyphenate."
  - "**A figure caption is Plex Sans at 0.875rem, left-aligned, the width of the figure.** Its label, text and punctuation are as the author wrote them."
  - "**Paper figures keep ar5iv's white background in dark mode; arXiv's own images do not.** Clear it on the header, TOC bar and footer images."
  - "**LaTeXML's beta badge and conversion logo are not shown.**"
  - "**The contents list repeats the author's headings exactly**, including subsections, appendices, acknowledgements and references. Math in a heading appears as it renders, never as its TeX: copy LaTeXML's contents entries with their MathML. A script that reads a heading's words leaves out the TeX annotation, as `toc.js` and `anchors.js` do."
  - "**LaTeXML's own sidebar is not shown.** The `.ds-toc` list replaces it."
  - "**Each link in the bar shows an icon and its name.**"
  - "**PDF opens in a new tab, in the bar and in the sidebar**, so the reader keeps their place in the HTML paper. It has the external-link icon and “(opens in a new tab)”, as on [Links](links.md)."
  - "**A second skip link goes to the paper's first section**, before the sidebar, so a keyboard user can pass it."
  - "**Every link to a place in the paper lands below the TOC bar.** The bar sets `scroll-padding-top`, which covers the TOC, a permalink, a citation and a cross-reference; a script that scrolls uses `scrollIntoView`, which respects it."
  - "**Every section, subsection and appendix heading has a Permalink control.** It copies the address with the section's LaTeXML id and the version: `…/2604.22725v1#S2`."
  - "**The accessible name starts with the visible word**, then names the section."
  - "**Copying is announced in words**, as in [Confirm an action that changes nothing on screen](../action-feedback.html)."
  - "**One action gets the Permalink control; several get the element pill.**"
  - "**Inline math gets nothing from arXiv**: no tabindex, role, ARIA or actions. Assistive technology reads its MathML directly."
  - "**View TeX swaps the equation for its TeX in place**, in plain monospace with no code box. The TeX view is hidden until asked for, and MathML annotations are never displayed."
  - "**View TeX and Copy use the TeX that LaTeXML keeps with the equation.** LaTeXML expands the author's own macros into standard TeX, so the copy works outside the paper. The author's own files are the TeX Source download."
  - "**Copy copies what is on screen**: the MathML in math view, the TeX in TeX view."
  - "**A wide equation scrolls inside its own box, never the page.** The box has `tabindex=\"0\"`, `role=\"region\"` and a name: “Equation 2.14, scrolls sideways”."
  - "**The equation number stays in view**, pinned to the right edge while the equation scrolls."
  - "**Only the author's alt text is shown**, whole and unchanged. The image's `alt` is never changed, and no reader-written or machine-written description is added. Write it in with `textContent`."
  - "**Long alt text is not shortened.** This is the one margin note longer than two sentences."
  - "**A figure without alt text says so.** Its margin note reads “No alt text provided”, in `--ds-text-muted`, with a link to how to add alt text."
  - "**Expand opens the figure viewer**, a `.ds-modal.ds-modal--wide` with `closedby=\"any\"`. Clicking the image opens it too; Expand is the keyboard path."
  - "**The viewer shows a copy.** The figure in the paper is never moved or changed."
  - "**The viewer shows the caption exactly as the author wrote it**, under the figure. The dialog is named by the caption's own label, such as “Figure 1:”, with `aria-labelledby`."
  - "**Zoom stays until the reader closes the viewer.** Zoom in, Zoom out and Fit buttons, the wheel, double-click, pinch and the +, - and 0 keys all work; drag or the arrow keys pan."
  - "**The zoom level is shown and announced**, with `aria-live=\"polite\"`."
  - "**Closing returns focus to what opened the viewer.**"
  - "**Zoom is animated only when reduced motion is not set.**"
  - "**Print hides the TOC bar, the permalinks, the element pills and every popover.** The identity line prints at 10pt."
  - "**No page break inside an equation, table or figure, and none straight after a heading.** Sections may break."
  - "**Paper titles are always a heading**, so a screen reader user can easily find it and move from paper to paper in a list."
  - "**Name each format link's paper.** In a list, “PDF” alone is the same link text fifty times; an `.is-sr-only` span adds the identifier."
  - "**Category names are in the tooltip, never only in a `title` attribute.** See [Tooltip](forms.md#tooltip)."
  - "**Paper title just before links.** For screen reader users, to maintain context, the title should appear before the format links, and just before them, so that the context is not forgotten. That means displaying the row with dates and links using the CSS `order` property (ie: the visual display will show the dates first, but the DOM order lists the links first)."
  - "**Say a withdrawal in words.** On a withdrawn or removed paper the status starts the title and the page's `<title>`, and the notice follows the title as a heading, so a screen reader meets both first. The red adds to the words and never replaces them."
---

# Papers

Displaying paper-related content is arXiv's richest, most complex, and highest stakes design challenge. This page gathers together guidelines that help us display papers and paper-related content consistently and accessibly. It is applicable to both HTML papers pages and search results. More relevant documentation: [Indicating which version is being read](../versions.html) and [following references without losing your place](../references.html).

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The metadata hierarchy

This order is based on what we hear from arXiv readers. They focus in on certain information first and want it easy to find, while other content is lower in their reading order. Look for guidance on visual display? This table is purely about hierarchy and content flow. You will find design and display notes elsewhere on this page and in mockups, .

## A paper in a list

Search results and listings use the metadata hierarchy. We rely on proximity to define rows instead of relying on visual blocks or dividers. Information is close together within each result and with a comfortable gap between result rows.

```html
<ol class="ds-paper-list">
  <li class="ds-paper">
    <h3><a href="#">LUMA: A CNN for Strong Gravitational Lens Searches in Astronomical Imaging</a></h3>
    <p class="ds-paper-when"><span class="ds-link-list"><a href="#">PDF<span class="is-sr-only"> of 2609.36857</span></a> <a href="#">HTML<span class="is-sr-only"> of 2609.36857</span></a> <a href="#">TeX Source<span class="is-sr-only"> of 2609.36857</span></a></span>
      <span class="ds-date-row">Submitted <time datetime="2026-09-29">29 Sep 2026</time> UTC <span aria-hidden="true">·</span><span class="is-sr-only">,</span> Announced <time datetime="2026-09">Sep 2026</time></span></p>
    <p class="ds-link-list"><a href="#">Giovanni Vincenzo Donatiello</a>, <a href="#">Achille A. Nucita</a>, <a href="#">Francesco De Paolis</a>, <a href="#">Antonio Franco</a>, <a href="#">Francesco Strafella</a></p>
    <p>We present LUMA, a convolutional neural network (CNN) pipeline for the automated detection of strong gravitational <mark>lenses</mark> in simulated astronomical imaging. The method combines a physically motivated preprocessing stage, which enhances faint arc and ring features, with a compact three-block CNN trained using class reweighting and modern learning-rate schedul… <button type="button" class="ds-show-more" aria-expanded="false">show more</button></p>
    <dl class="ds-data-list">
      <div><dt>Comments</dt><dd>Accepted for publication in Astronomy and Computing, 2027, Corresponding Author: G.V. Donatiello (see associated pdf for useful e-mail addresses). 14 Pages, 8 Figures, 3 Tables</dd></div>
      <div><dt>DOI</dt><dd><a href="https://doi.org/10.1016/j.ascom.2026.101198">10.1016/j.ascom.2026.101198</a></dd></div>
      <div><dt>arXiv ID</dt><dd><a href="#">2609.36857</a></dd></div>
    </dl>
    <ul class="ds-tag-list" aria-label="Subject categories, primary first">
      <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.IM/recent" class="ds-tag ds-tag--keep-case ds-tag--info" aria-describedby="cat-1-0">astro-ph.IM</a><span class="ds-tooltip" id="cat-1-0" role="tooltip"><span class="ds-tooltip-body">Instrumentation and Methods for Astrophysics (primary)</span></span></span></li>
      <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.GA/recent" class="ds-tag ds-tag--keep-case" aria-describedby="cat-1-1">astro-ph.GA</a><span class="ds-tooltip" id="cat-1-1" role="tooltip"><span class="ds-tooltip-body">Astrophysics of Galaxies</span></span></span></li>
    </ul>
  </li>
  <li class="ds-paper">
    <h3><a href="#">SN Helios: A Multiply Imaged Type II Supernova Opening Time-Delay Cosmography beyond redshift of 3</a></h3>
    <p class="ds-paper-when"><span class="ds-link-list"><a href="#">PDF<span class="is-sr-only"> of 2609.30440</span></a> <a href="#">HTML<span class="is-sr-only"> of 2609.30440</span></a> <a href="#">TeX Source<span class="is-sr-only"> of 2609.30440</span></a></span>
      <span class="ds-date-row">Submitted <time datetime="2026-09-24">24 Sep 2026</time> UTC <span aria-hidden="true">·</span><span class="is-sr-only">,</span> Announced <time datetime="2026-09">Sep 2026</time></span></p>
    <p class="ds-link-list"><a href="#">Seiji Fujimoto</a>, <a href="#">Conor Larison</a>, <a href="#">Justin D. R. Pierel</a>, <a href="#">Lukas J. Furtak</a>, <a href="#">Masamune Oguri</a>, <a href="#">Adi Zitrin</a>, <a href="#">Jose M. Diego</a>, <a href="#">Keren Sharon</a> <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false">show all 67 authors</button></p>
    <p>We report the discovery and spectroscopic confirmation of SN Helios, a strongly <mark>lensed</mark>, multiply imaged Type II supernova (SN) at behind the galaxy cluster RXC J0018.5+1626. The transient was identified as a red F150W-dropout source (F277W = 26.1 mag) in JWST/NIRCam imaging taken on 2026 July 3 for the VENUS survey, with no counterpart in 2024 Decem… <button type="button" class="ds-show-more" aria-expanded="false">show more</button></p>
    <dl class="ds-data-list">
      <div><dt>Comments</dt><dd>14 pages, 9 figures, 5 tables. Comments welcome!</dd></div>
      <div><dt>arXiv ID</dt><dd><a href="#">2609.30440</a></dd></div>
    </dl>
    <ul class="ds-tag-list" aria-label="Subject categories, primary first">
      <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.GA/recent" class="ds-tag ds-tag--keep-case ds-tag--info" aria-describedby="cat-2-0">astro-ph.GA</a><span class="ds-tooltip" id="cat-2-0" role="tooltip"><span class="ds-tooltip-body">Astrophysics of Galaxies (primary)</span></span></span></li>
      <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.CO/recent" class="ds-tag ds-tag--keep-case" aria-describedby="cat-2-1">astro-ph.CO</a><span class="ds-tooltip" id="cat-2-1" role="tooltip"><span class="ds-tooltip-body">Cosmology and Nongalactic Astrophysics</span></span></span></li>
      <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.HE/recent" class="ds-tag ds-tag--keep-case" aria-describedby="cat-2-2">astro-ph.HE</a><span class="ds-tooltip" id="cat-2-2" role="tooltip"><span class="ds-tooltip-body">High Energy Astrophysical Phenomena</span></span></span></li>
    </ul>
  </li>
</ol>
```

- `.ds-paper-list` — An `<ol>` of papers. Papers are separated by space, four times the space inside one, with no lines or boxes.
- `.ds-paper` — One paper, an `<li>`. Its first child is the title: a heading one level below the list's own heading, linked to the abstract page.
- `.ds-paper-when` — The format links (a `.ds-link-list`) and the dates (`.ds-date-row`) on one line. The links come first in the markup, so a screen reader reaches them straight after the title; the dates are shown first. On a narrow screen the links wrap below the dates.
- `.ds-link-list` — On a `<p>`: the authors. After eight names, Show more for the rest.
- `<p>` — The abstract excerpt and its Show more. See [Show more](progressive-disclosure.md#show-more).
- `.ds-data-list` — Comments, journal reference, DOI and the arXiv ID, in that order, each label beside its value. A paper shows only the rows it has. See [Data list](cards.md#data-list).
- `.ds-tag-list` — The category tags, primary first. See [Displaying categories](#paper-categories). It sits close under the metadata.

> Meets accessibility guidelines [WCAG 2.2 SC 1.3.1](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) Info and Relationships (Level A) and [WCAG 2.2 SC 2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html) Link Purpose (In Context) (Level A)

## Displaying categories

A paper's subject categories show as tags, primary first. Each code links to its listing, and its full name appears in a tooltip.

```html
<ul class="ds-tag-list" aria-label="Subject categories, primary first">
  <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.GA/recent" class="ds-tag ds-tag--keep-case ds-tag--info" aria-describedby="cat-demo-0">astro-ph.GA</a><span class="ds-tooltip" id="cat-demo-0" role="tooltip"><span class="ds-tooltip-body">Astrophysics of Galaxies (primary)</span></span></span></li>
  <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.CO/recent" class="ds-tag ds-tag--keep-case" aria-describedby="cat-demo-1">astro-ph.CO</a><span class="ds-tooltip" id="cat-demo-1" role="tooltip"><span class="ds-tooltip-body">Cosmology and Nongalactic Astrophysics</span></span></span></li>
  <li><span class="ds-tooltip-host"><a href="https://arxiv.org/list/astro-ph.HE/recent" class="ds-tag ds-tag--keep-case" aria-describedby="cat-demo-2">astro-ph.HE</a><span class="ds-tooltip" id="cat-demo-2" role="tooltip"><span class="ds-tooltip-body">High Energy Astrophysical Phenomena</span></span></span></li>
</ul>
```

- `<a class="ds-tag">` — Each category is a link to its listing of recent papers, with `.ds-tag--keep-case` so the code keeps its case. See [Tags](tags.md).
- `.ds-tag--info` — On the primary category only. The others are the plain grey tag.
- `.ds-tooltip` — The full name of the category, on hover and on focus, named by the link's `aria-describedby`. The primary one adds “(primary)”. Load `tooltip.js` once on the page. See [Tooltip](forms.md#tooltip).

> Meets accessibility guideline [WCAG 2.2 SC 1.4.13](https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html) Content on Hover or Focus (Level AA)

## Displaying abstract and primary metadata

On a paper's own page the order is the identity line, the title, the dates and versions, a warning when an older version is open, the authors and the abstract. The version history and the paper's details sit in the sidebar.

**The top of a paper, viewing an older version**

```html
<p class="ds-paper-identity">
  <span><span class="ds-version" aria-hidden="true">arXiv:2604.22725v1</span><span class="is-sr-only">archive paper, I D 2 6 0 4 dot 2 2 7 2 5, version 1</span></span>
  <span>[gr-qc] General Relativity and Quantum Cosmology</span>
  <a href="https://doi.org/10.48550/arXiv.2604.22725">doi:10.48550/arXiv.2604.22725</a>
  <a href="https://creativecommons.org/licenses/by/4.0/">License: CC BY 4.0</a>
</p>
<h1>Gauge-independent approach to inflation in quadratic gravity</h1>
<p class="ds-date-row">
  Submitted <time datetime="2026-04-24">24 Apr 2026</time> UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-04-25T02:07Z">25 Apr 2026, 02:07</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <strong class="ds-version" aria-current="true">v1<span class="is-sr-only">, this version</span></strong>
  <a class="ds-version" href="https://arxiv.org/abs/2604.22725v2">v2<span class="is-sr-only">, version 2</span></a>
  <a class="ds-version" href="https://arxiv.org/abs/2604.22725v3">v3<span class="is-sr-only">, version 3</span></a>
  </span>
</p>
<div class="ds-alert ds-alert--warning">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/></svg>
  <div class="ds-alert-content">
    <p><strong>You are viewing version 1.</strong> A newer version is available — <a href="https://arxiv.org/abs/2604.22725v3">version 3, revised 28 Jun 2026</a>.</p>
  </div>
</div>
<p class="ds-link-list"><a href="#">Adrian Palomares</a>, <a href="#">Ilya L. Shapiro</a>, <a href="#">Maria C. Gonzalez-Garcia</a>, <a href="#">Tomohiro Harada</a>, <a href="#">Elena Castellani</a>, <a href="#">Kei-ichi Maeda</a>, <a href="#">Francesca Vidotto</a>, <a href="#">Abhay Ashtekar</a> <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false">show all 22 authors</button></p>
<h2 class="is-sr-only">Abstract</h2>
<p>We investigate the scalar sector of linear cosmological perturbations in quadratic gravity. Working in the Einstein frame, we derive the equations of motion in a gauge-independent manner and express them in terms of three sets of gauge-invariant variables. This approach allows us to distinguish genuine physical effects from gauge artefacts, which is particularly relevant for assessing the stability of perturbations in this theory. In the superhorizon limit, we obtain the leading-order behaviour of the relevant gauge-invariant variables and analyse the perturbations in several commonly used gauges. We find that the Newtonian gauge exhibits an apparent instability, characterised by the exponential growth of the metric perturbations. However, this growth is non-generic and gauge-dependent; in the other gauges analysed in this work, the perturbations remain well behaved within the perturbative regime. Physical observables can thus be consistently computed, and the apparent instability is identified as a gauge artefact rather than a pathology of the theory. Our analysis also demonstrates how the evolution behaviour of a gauge-invariant variable changes under the frame transformation and clarifies the relation between results obtained in the Jordan and Einstein frames.</p>
```

**The top of a withdrawn paper, viewing the withdrawal notice**

```html
<title>Withdrawn: Gauge-independent approach to inflation in quadratic gravity</title>
…
<p class="ds-paper-identity">
  <span><span class="ds-version" aria-hidden="true">arXiv:2604.22725v4</span><span class="is-sr-only">archive paper, I D 2 6 0 4 dot 2 2 7 2 5, version 4</span></span>
  <span>[gr-qc] General Relativity and Quantum Cosmology</span>
</p>
<h1><span class="ds-paper-status" lang="en">Withdrawn:</span> Gauge-independent approach to inflation in quadratic gravity</h1>
<section class="ds-alert ds-alert--error" aria-labelledby="notice-h">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16h.01"/><path d="M12 8v4"/><path d="M15.312 2a2 2 0 0 1 1.414.586l4.688 4.688A2 2 0 0 1 22 8.688v6.624a2 2 0 0 1-.586 1.414l-4.688 4.688a2 2 0 0 1-1.414.586H8.688a2 2 0 0 1-1.414-.586l-4.688-4.688A2 2 0 0 1 2 15.312V8.688a2 2 0 0 1 .586-1.414l4.688-4.688A2 2 0 0 1 8.688 2z"/></svg>
  <div class="ds-alert-content">
    <h2 class="ds-alert-title" id="notice-h">This paper has been withdrawn by Adrian Palomares.</h2>
    <p>Reason given: “The main result in Section 3 relies on a gauge condition that does not hold in general. A corrected analysis will be submitted as a new paper.” The withdrawn paper can still be read in <a href="https://arxiv.org/abs/2604.22725v3">version 3</a>.</p>
  </div>
</section>
<p class="ds-date-row">…the dates, ending with Withdrawn, and the versions, as in <a href="versions.html#version-row">Version row</a>…</p>
<p class="ds-link-list">…the authors…</p>
<p>…the abstract…</p>
```

**The top of a removed version**

```html
<title>Removed: Gauge-independent approach to inflation in quadratic gravity</title>
…
<h1><span class="ds-paper-status" lang="en">Removed:</span> Gauge-independent approach to inflation in quadratic gravity</h1>
<section class="ds-alert ds-alert--error" aria-labelledby="notice-h">
  <svg class="ds-alert-icon" …>…</svg>
  <div class="ds-alert-content">
    <h2 class="ds-alert-title" id="notice-h">This version has been removed by arXiv.</h2>
    <p>“arXiv admin comment: …” The full text and files are no longer available.</p>
  </div>
</section>
<p class="ds-date-row">
  …Submitted and Announced…
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Removed <time datetime="2026-10-23">23 Oct 2026</time> UTC
</p>
```

```html
<div>
<div>…the abstract…</div>
<aside class="ds-sidebar" aria-label="About this paper">
  <section aria-labelledby="files-h">
    <h2 class="ds-panel-label" id="files-h">Files</h2>
    <ul class="ds-paper-files">
      <li><a class="ds-btn ds-btn-primary" href="https://arxiv.org/pdf/2604.22725v1" target="_blank" rel="noopener" aria-describedby="paper-title-demo"><svg aria-hidden="true">…</svg> Download PDF <small>· 1.2 MB</small><span class="is-sr-only"> (opens in a new tab)</span></a></li>
      <li><a href="https://arxiv.org/src/2604.22725v1" aria-describedby="paper-title-demo">TeX Source</a> <small>.tar.gz · 286 KB</small></li>
      <li><a href="https://arxiv.org/format/2604.22725v1">Other formats</a></li>
      <li>Ancillary files <small>· 3.6 MB</small> <a href="https://arxiv.org/src/2604.22725v1/anc">Download all<span class="is-sr-only"> 3 ancillary files</span></a></li>
    </ul>
  </section>
  <section aria-labelledby="cite-h" class="ds-paper-cite">
    <div class="ds-paper-cite-head">
      <h2 class="ds-panel-label" id="cite-h">Cite</h2>
      <div class="ds-form--compact ds-paper-cite-tools">
        <label class="is-sr-only" for="cite-format">Citation format</label>
        <select class="ds-input" id="cite-format">
          <option value="bibtex" selected>BibTeX</option>
          <option value="apa">APA</option>
          <option value="chicago">Chicago</option>
          <option value="mla">MLA</option>
        </select>
      </div>
    </div>
    <div id="cite-code" class="ds-paper-cite-code">
      <figure data-format="bibtex">
        <figcaption>BibTeX</figcaption>
        <pre>…</pre>
      </figure>
      <figure data-format="apa">
        <figcaption>APA</figcaption>
        <pre>…</pre>
      </figure>
      <figure data-format="chicago">
        <figcaption>Chicago</figcaption>
        <pre>…</pre>
      </figure>
      <figure data-format="mla">
        <figcaption>MLA</figcaption>
        <pre>…</pre>
      </figure>
    </div>
    <button type="button" class="ds-show-more" aria-expanded="false" aria-controls="cite-code" hidden>Show full citation</button>
  </section>
  <section aria-labelledby="info-h">
    <h2 class="ds-panel-label" id="info-h">Paper information</h2>
    <details class="ds-acc" name="paper-info">
      <summary>Version history</summary>
      <div class="ds-acc-body">
        <ol class="ds-paper-versions">
          <li>
            <p class="ds-date-row"><a class="ds-version" href="https://arxiv.org/abs/2604.22725v3">v3<span class="is-sr-only">, version 3</span></a> · <time datetime="2026-06-28">28 Jun 2026</time> UTC · Latest</p>
            <p>18 pages, 6 figures. Updated discussion of scalar spectral index in Sec. 4. Added comparison with Planck 2018 data. Matches published version.</p>
          </li>
          <li>
            <p class="ds-date-row"><a class="ds-version" href="https://arxiv.org/abs/2604.22725v2">v2<span class="is-sr-only">, version 2</span></a> · <time datetime="2026-05-19">19 May 2026</time> UTC</p>
            <p>17 pages, 6 figures. Corrected Eq. (4.7).</p>
          </li>
          <li aria-current="true">
            <p class="ds-date-row"><strong class="ds-version">v1</strong> · <time datetime="2026-04-24">24 Apr 2026</time> UTC · Viewing</p>
            <p>16 pages, 5 figures.</p>
          </li>
        </ol>
      </div>
    </details>
    <details class="ds-acc" name="paper-info">
      <summary>Accessibility</summary>
      <div class="ds-acc-body">
        <ul class="ds-paper-capabilities">
          <li><svg aria-hidden="true">…</svg> HTML, PDF and TeX Source</li>
          <li><svg aria-hidden="true">…</svg> Structured math</li>
        </ul>
      </div>
    </details>
    <details class="ds-acc" name="paper-info">
      <summary>Metadata</summary>
      <div class="ds-acc-body">
        <dl>
          <dt>Subjects</dt><dd>General Relativity and Quantum Cosmology (<a href="https://arxiv.org/list/gr-qc/recent">gr-qc</a>); Cosmology and Nongalactic Astrophysics (<a href="https://arxiv.org/list/astro-ph.CO/recent">astro-ph.CO</a>); High Energy Physics — Theory (<a href="https://arxiv.org/list/hep-th/recent">hep-th</a>)</dd>
          <dt>arXiv DOI</dt><dd><a href="https://doi.org/10.48550/arXiv.2604.22725">10.48550/arXiv.2604.22725</a></dd>
          <dt>License</dt><dd><a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></dd>
          <dt>Journal</dt><dd><a href="#">Journal of Cosmology and Astroparticle Physics, 2026(05), 012</a></dd>
          <dt>Comments</dt><dd>v3: 18 pages, 6 figures. Updated discussion of scalar spectral index in Sec. 4. Added comparison with Planck 2018 data. Matches published version.</dd>
        </dl>
      </div>
    </details>
  </section>
</aside>
</div>
```

- `.ds-paper-identity` — The identity line above the title: the identifier with its version, the primary category code with its full name, the arXiv DOI, and the licence as a link. It is centred, and as a child of `.ds-container` it spans the viewport to the gutters, so it wraps only on narrow screens. The identifier is read out digit by digit from an `.is-sr-only` span; the visible one is hidden from screen readers.
- `<h1>` — The paper title. The demo here uses an `<h2>` at the size of an `<h1>`, because it sits inside this page.
- `.ds-date-row` — The dates and the version links, as in [Indicate which version is being read](../versions.html#version-row). Each version link goes to that version's abstract page, never its HTML: an HTML version may not exist for every version.
- `.ds-alert--warning` — Only when an older version is being viewed. See [Indicate which version is being read](../versions.html#version-row).
- `.ds-link-list` — On a `<p>`: the authors, with Show more after eight.
- `<h2 class="is-sr-only">` — The abstract's heading, “Abstract”, hidden from sight. Sighted readers know the paragraph after the authors is the abstract; screen-reader users can still jump to it by heading. The demo uses an `<h3>`, because its title is an `<h2>`.
- `<p>` — The abstract, in full.
- `<title>` — Starts with the status, “Withdrawn:”, so a reader sees it in the browser tab and a screen reader announces it first.
- `.ds-paper-identity` — The identifier with the notice's version, and the category. With no text to read, the DOI and the licence leave the line; Metadata, in the sidebar, still has the DOI.
- `.ds-paper-status` — “Withdrawn:” before the title, inside the heading, in the error color. It is its own element, so the author's title is not edited, and it has `lang="en"` because the title may be in another language.
- `.ds-alert--error` — On a `<section>`: the notice, straight after the title and before the dates. It says who withdrew the paper, gives the reason as they wrote it, in quotes, and links to the last version that can be read. A `<section>` named by its heading, so a screen reader reaches it second and lists it among the headings. No role, because it is in the page as it loads (see [Alerts](alerts.md)).
- `.ds-alert-title` — On a heading, one level below the title: an `<h2>` on the page. The demo uses an `<h3>` because it sits inside this page.
- `.ds-paper-status` — “Removed:”, built as “Withdrawn:” is.
- `.ds-alert--error` — Says that arXiv removed the version, quotes arXiv's comment as written, and says that the full text and files are gone.
- `.ds-date-row` — Ends with Removed and its date. A removal changes the version in place, so no version is added to the list.
- `.ds-sidebar` — The column beside the abstract: Files, Cite and Paper information, in that order. See [Sidebar](layout-patterns.md#sidebar). Beside a long paper, its frame keeps the controls together. It grows with its content; it never scrolls inside itself.
- `.ds-panel-label` — On an `<h2>`: the label of each block, one level below the paper title, so the outline skips no level. The demo uses `<h3>` because it sits inside this page.
- `.ds-paper-files` — The downloads. PDF is the primary button and fills the sidebar's width; TeX Source, Other formats (when a paper has them) and Ancillary files are text links under it. Each shows its size; TeX Source also shows its file type. Up to two ancillary files are listed by name; with three or more, one line gives the total size and Download all, at the end of the line; the hidden text on the link gives the count.
- `[aria-describedby]` — On each download, pointing to the paper title, so a screen reader names the paper with the link. The visible words stay the link's name, which meets [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A).
- `.ds-paper-cite` — The citation. `.ds-paper-cite-head` holds the Cite label and, on the same line, a compact select (`.ds-form--compact`) to choose the format. Each format is a standard code block, so `copy-code.js` gives it the copy button and its “Copied to clipboard” announcement, and the citation wraps rather than scrolling. `.ds-paper-cite-code` shows the first two lines until the `.ds-show-more` below it opens the rest. Every format is in the page, one `<figure>` each; without JavaScript all four are shown in full with their names, and the select and the button are hidden.
- `.ds-paper-capabilities` — The accessibility panel: one line per capability the paper has, each a `shield-check` icon from `docs/icons/` and words. Only what is present is listed, and there is no score.
- `.ds-acc` — Version history, Accessibility and Metadata are accordions, closed by default, grouped under the Paper information label. They share `name="paper-info"`, so only one is open at a time.

> Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2: the status goes “before the original main title”, and the notice is “a clearly signposted box” in its own color.

> Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.5: a removed article keeps “the article’s title, author list, and relevant metadata”, and only “the main text” goes.

**Rule.** **You are viewing version 1.** A newer version is available — [version 3, revised 28 Jun 2026](https://arxiv.org/abs/2604.22725v3).

**Rule.** This paper has been withdrawn by Adrian Palomares.: Reason given: “The main result in Section 3 relies on a gauge condition that does not hold in general. A corrected analysis will be submitted as a new paper.” The withdrawn paper can still be read in [version 3](#v3).

**Rule.** This version has been removed by arXiv.: “arXiv admin comment: This version has been removed by arXiv administrators as the submitter did not have the rights to agree to the license at the time of submission.” The full text and files are no longer available.

## The version row

The row under the title gives the paper's dates and links to its other versions; the version being read is in a box. The row changes with the number of versions, with the version being read, and when a paper is withdrawn or removed: [Indicate which version is being read](../versions.html#version-row) shows each case.

## Withdrawn and removed papers

A withdrawn paper keeps its title, authors, abstract and metadata, and its earlier versions can still be read. A removed version keeps its title, authors, abstract and metadata, but its full text and files are gone. In both cases, a status before the title and a notice after it say what happened.

**The top of a withdrawn paper, viewing the withdrawal notice**

```html
<title>Withdrawn: Gauge-independent approach to inflation in quadratic gravity</title>
…
<p class="ds-paper-identity">
  <span><span class="ds-version" aria-hidden="true">arXiv:2604.22725v4</span><span class="is-sr-only">archive paper, I D 2 6 0 4 dot 2 2 7 2 5, version 4</span></span>
  <span>[gr-qc] General Relativity and Quantum Cosmology</span>
</p>
<h1><span class="ds-paper-status" lang="en">Withdrawn:</span> Gauge-independent approach to inflation in quadratic gravity</h1>
<section class="ds-alert ds-alert--error" aria-labelledby="notice-h">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16h.01"/><path d="M12 8v4"/><path d="M15.312 2a2 2 0 0 1 1.414.586l4.688 4.688A2 2 0 0 1 22 8.688v6.624a2 2 0 0 1-.586 1.414l-4.688 4.688a2 2 0 0 1-1.414.586H8.688a2 2 0 0 1-1.414-.586l-4.688-4.688A2 2 0 0 1 2 15.312V8.688a2 2 0 0 1 .586-1.414l4.688-4.688A2 2 0 0 1 8.688 2z"/></svg>
  <div class="ds-alert-content">
    <h2 class="ds-alert-title" id="notice-h">This paper has been withdrawn by Adrian Palomares.</h2>
    <p>Reason given: “The main result in Section 3 relies on a gauge condition that does not hold in general. A corrected analysis will be submitted as a new paper.” The withdrawn paper can still be read in <a href="https://arxiv.org/abs/2604.22725v3">version 3</a>.</p>
  </div>
</section>
<p class="ds-date-row">…the dates, ending with Withdrawn, and the versions, as in <a href="versions.html#version-row">Version row</a>…</p>
<p class="ds-link-list">…the authors…</p>
<p>…the abstract…</p>
```

**The top of a removed version**

```html
<title>Removed: Gauge-independent approach to inflation in quadratic gravity</title>
…
<h1><span class="ds-paper-status" lang="en">Removed:</span> Gauge-independent approach to inflation in quadratic gravity</h1>
<section class="ds-alert ds-alert--error" aria-labelledby="notice-h">
  <svg class="ds-alert-icon" …>…</svg>
  <div class="ds-alert-content">
    <h2 class="ds-alert-title" id="notice-h">This version has been removed by arXiv.</h2>
    <p>“arXiv admin comment: …” The full text and files are no longer available.</p>
  </div>
</section>
<p class="ds-date-row">
  …Submitted and Announced…
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Removed <time datetime="2026-10-23">23 Oct 2026</time> UTC
</p>
```

- `<title>` — Starts with the status, “Withdrawn:”, so a reader sees it in the browser tab and a screen reader announces it first.
- `.ds-paper-identity` — The identifier with the notice's version, and the category. With no text to read, the DOI and the licence leave the line; Metadata, in the sidebar, still has the DOI.
- `.ds-paper-status` — “Withdrawn:” before the title, inside the heading, in the error color. It is its own element, so the author's title is not edited, and it has `lang="en"` because the title may be in another language.
- `.ds-alert--error` — On a `<section>`: the notice, straight after the title and before the dates. It says who withdrew the paper, gives the reason as they wrote it, in quotes, and links to the last version that can be read. A `<section>` named by its heading, so a screen reader reaches it second and lists it among the headings. No role, because it is in the page as it loads (see [Alerts](alerts.md)).
- `.ds-alert-title` — On a heading, one level below the title: an `<h2>` on the page. The demo uses an `<h3>` because it sits inside this page.
- `.ds-paper-status` — “Removed:”, built as “Withdrawn:” is.
- `.ds-alert--error` — Says that arXiv removed the version, quotes arXiv's comment as written, and says that the full text and files are gone.
- `.ds-date-row` — Ends with Removed and its date. A removal changes the version in place, so no version is added to the list.

> Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2: the status goes “before the original main title”, and the notice is “a clearly signposted box” in its own color.

> Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.5: a removed article keeps “the article’s title, author list, and relevant metadata”, and only “the main text” goes.

**Rule.** This paper has been withdrawn by Adrian Palomares.: Reason given: “The main result in Section 3 relies on a gauge condition that does not hold in general. A corrected analysis will be submitted as a new paper.” The withdrawn paper can still be read in [version 3](#v3).

**Rule.** This version has been removed by arXiv.: “arXiv admin comment: This version has been removed by arXiv administrators as the submitter did not have the rights to agree to the license at the time of submission.” The full text and files are no longer available.

## Displaying paper actions and full metadata

Beside the abstract, the sidebar holds downloadable files, a citation tool, and additional paper information, in that order.

```html
<div>
<div>…the abstract…</div>
<aside class="ds-sidebar" aria-label="About this paper">
  <section aria-labelledby="files-h">
    <h2 class="ds-panel-label" id="files-h">Files</h2>
    <ul class="ds-paper-files">
      <li><a class="ds-btn ds-btn-primary" href="https://arxiv.org/pdf/2604.22725v1" target="_blank" rel="noopener" aria-describedby="paper-title-demo"><svg aria-hidden="true">…</svg> Download PDF <small>· 1.2 MB</small><span class="is-sr-only"> (opens in a new tab)</span></a></li>
      <li><a href="https://arxiv.org/src/2604.22725v1" aria-describedby="paper-title-demo">TeX Source</a> <small>.tar.gz · 286 KB</small></li>
      <li><a href="https://arxiv.org/format/2604.22725v1">Other formats</a></li>
      <li>Ancillary files <small>· 3.6 MB</small> <a href="https://arxiv.org/src/2604.22725v1/anc">Download all<span class="is-sr-only"> 3 ancillary files</span></a></li>
    </ul>
  </section>
  <section aria-labelledby="cite-h" class="ds-paper-cite">
    <div class="ds-paper-cite-head">
      <h2 class="ds-panel-label" id="cite-h">Cite</h2>
      <div class="ds-form--compact ds-paper-cite-tools">
        <label class="is-sr-only" for="cite-format">Citation format</label>
        <select class="ds-input" id="cite-format">
          <option value="bibtex" selected>BibTeX</option>
          <option value="apa">APA</option>
          <option value="chicago">Chicago</option>
          <option value="mla">MLA</option>
        </select>
      </div>
    </div>
    <div id="cite-code" class="ds-paper-cite-code">
      <figure data-format="bibtex">
        <figcaption>BibTeX</figcaption>
        <pre>…</pre>
      </figure>
      <figure data-format="apa">
        <figcaption>APA</figcaption>
        <pre>…</pre>
      </figure>
      <figure data-format="chicago">
        <figcaption>Chicago</figcaption>
        <pre>…</pre>
      </figure>
      <figure data-format="mla">
        <figcaption>MLA</figcaption>
        <pre>…</pre>
      </figure>
    </div>
    <button type="button" class="ds-show-more" aria-expanded="false" aria-controls="cite-code" hidden>Show full citation</button>
  </section>
  <section aria-labelledby="info-h">
    <h2 class="ds-panel-label" id="info-h">Paper information</h2>
    <details class="ds-acc" name="paper-info">
      <summary>Version history</summary>
      <div class="ds-acc-body">
        <ol class="ds-paper-versions">
          <li>
            <p class="ds-date-row"><a class="ds-version" href="https://arxiv.org/abs/2604.22725v3">v3<span class="is-sr-only">, version 3</span></a> · <time datetime="2026-06-28">28 Jun 2026</time> UTC · Latest</p>
            <p>18 pages, 6 figures. Updated discussion of scalar spectral index in Sec. 4. Added comparison with Planck 2018 data. Matches published version.</p>
          </li>
          <li>
            <p class="ds-date-row"><a class="ds-version" href="https://arxiv.org/abs/2604.22725v2">v2<span class="is-sr-only">, version 2</span></a> · <time datetime="2026-05-19">19 May 2026</time> UTC</p>
            <p>17 pages, 6 figures. Corrected Eq. (4.7).</p>
          </li>
          <li aria-current="true">
            <p class="ds-date-row"><strong class="ds-version">v1</strong> · <time datetime="2026-04-24">24 Apr 2026</time> UTC · Viewing</p>
            <p>16 pages, 5 figures.</p>
          </li>
        </ol>
      </div>
    </details>
    <details class="ds-acc" name="paper-info">
      <summary>Accessibility</summary>
      <div class="ds-acc-body">
        <ul class="ds-paper-capabilities">
          <li><svg aria-hidden="true">…</svg> HTML, PDF and TeX Source</li>
          <li><svg aria-hidden="true">…</svg> Structured math</li>
        </ul>
      </div>
    </details>
    <details class="ds-acc" name="paper-info">
      <summary>Metadata</summary>
      <div class="ds-acc-body">
        <dl>
          <dt>Subjects</dt><dd>General Relativity and Quantum Cosmology (<a href="https://arxiv.org/list/gr-qc/recent">gr-qc</a>); Cosmology and Nongalactic Astrophysics (<a href="https://arxiv.org/list/astro-ph.CO/recent">astro-ph.CO</a>); High Energy Physics — Theory (<a href="https://arxiv.org/list/hep-th/recent">hep-th</a>)</dd>
          <dt>arXiv DOI</dt><dd><a href="https://doi.org/10.48550/arXiv.2604.22725">10.48550/arXiv.2604.22725</a></dd>
          <dt>License</dt><dd><a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></dd>
          <dt>Journal</dt><dd><a href="#">Journal of Cosmology and Astroparticle Physics, 2026(05), 012</a></dd>
          <dt>Comments</dt><dd>v3: 18 pages, 6 figures. Updated discussion of scalar spectral index in Sec. 4. Added comparison with Planck 2018 data. Matches published version.</dd>
        </dl>
      </div>
    </details>
  </section>
</aside>
</div>
```

- `.ds-sidebar` — The column beside the abstract: Files, Cite and Paper information, in that order. See [Sidebar](layout-patterns.md#sidebar). Beside a long paper, its frame keeps the controls together. It grows with its content; it never scrolls inside itself.
- `.ds-panel-label` — On an `<h2>`: the label of each block, one level below the paper title, so the outline skips no level. The demo uses `<h3>` because it sits inside this page.
- `.ds-paper-files` — The downloads. PDF is the primary button and fills the sidebar's width; TeX Source, Other formats (when a paper has them) and Ancillary files are text links under it. Each shows its size; TeX Source also shows its file type. Up to two ancillary files are listed by name; with three or more, one line gives the total size and Download all, at the end of the line; the hidden text on the link gives the count.
- `[aria-describedby]` — On each download, pointing to the paper title, so a screen reader names the paper with the link. The visible words stay the link's name, which meets [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A).
- `.ds-paper-cite` — The citation. `.ds-paper-cite-head` holds the Cite label and, on the same line, a compact select (`.ds-form--compact`) to choose the format. Each format is a standard code block, so `copy-code.js` gives it the copy button and its “Copied to clipboard” announcement, and the citation wraps rather than scrolling. `.ds-paper-cite-code` shows the first two lines until the `.ds-show-more` below it opens the rest. Every format is in the page, one `<figure>` each; without JavaScript all four are shown in full with their names, and the select and the button are hidden.
- `.ds-paper-capabilities` — The accessibility panel: one line per capability the paper has, each a `shield-check` icon from `docs/icons/` and words. Only what is present is listed, and there is no score.
- `.ds-acc` — Version history, Accessibility and Metadata are accordions, closed by default, grouped under the Paper information label. They share `name="paper-info"`, so only one is open at a time.

## The TOC bar on a paper

On a paper, the TOC bar also has the arXiv logo on the left and links to the paper's PDF and TeX source on the right.

```html
<div class="ds-full ds-toc-bar">
  <div class="ds-toc-bar-inner">
    <a class="ds-paper-bar-logo" href="https://arxiv.org/" aria-label="archive home"><svg aria-hidden="true">…</svg></a>
    <details class="ds-toc">
      <summary class="ds-toc-trigger">
        <svg aria-hidden="true">…</svg>
        <span class="ds-toc-text"><span class="ds-toc-prefix">Contents</span></span>
        <svg class="ds-toc-chevron" aria-hidden="true">…</svg>
      </summary>
      <nav class="ds-toc-menu" aria-label="Contents">
        <ol>
          <li><a href="#"><span class="ds-toc-num">1</span>Introduction</a></li>
          <li><a href="#"><span class="ds-toc-num">2</span>Setup</a>
            <ol>
              <li><a href="#"><span class="ds-toc-num">2.1</span>Background equations</a></li>
              <li><a href="#"><span class="ds-toc-num">2.2</span>Perturbed equations</a></li>
            </ol>
          </li>
          <li><a href="#"><span class="ds-toc-num">3</span>Evolution of gauge-invariant variables</a></li>
          <li><a href="#"><span class="ds-toc-num">4</span>Analysis of gauges</a></li>
          <li><a href="#"><span class="ds-toc-num">5</span>Conclusion</a></li>
          <li><a href="#">Acknowledgments</a></li>
          <li><a href="#"><span class="ds-toc-num">A</span>Evolution equations</a></li>
          <li><a href="#">References</a></li>
        </ol>
      </nav>
    </details>
    <nav class="ds-paper-tools" aria-label="Other formats">
      <a href="https://arxiv.org/pdf/2604.22725v1" target="_blank" rel="noopener"><svg aria-hidden="true">…</svg>PDF<span class="is-sr-only"> (opens in a new tab)</span></a>
      <a href="https://arxiv.org/src/2604.22725v1"><svg aria-hidden="true">…</svg><span class="is-sr-only">TeX </span>Source</a>
    </nav>
  </div>
</div>
```

- `.ds-toc-bar` — The bar, as on [Progressive disclosure](progressive-disclosure.md#toc-bar). On a paper it is `.ds-full`, the full width of the page.
- `.ds-paper-bar-logo` — The one-colour Library Grey logo, inlined from `docs/assets/images/logos/logo_arxiv-library-grey.svg` with `fill="currentColor"`, so it follows the theme. It links to the arXiv home page, and its name is “archive home”.
- `.ds-toc-menu` — The paper's own headings, numbers in `.ds-toc-num`, written into the HTML from LaTeXML's contents list. Subsections are an `<ol>` inside their section's `<li>`, indented to the section's title in smaller type.
- `.ds-paper-tools` — PDF and Source, each an icon and its name, in a `<nav>` named “Other formats”. The TeX glyph says TeX, so the visible name is “Source”; an `.is-sr-only` “TeX” makes the spoken name “TeX Source”. The icons are `file-text` and `tex` from `docs/icons/`.

## Section permalinks

Each section heading in a paper has a Permalink control that copies the link to that section, including the version.

```html
<h3 id="S2"><span class="ltx_tag">2 </span>Setup<button type="button" class="ds-permalink"><svg aria-hidden="true">…</svg>Permalink<span class="is-sr-only"> to section 2, Setup</span></button></h3>
<p>We consider quadratic gravity in four dimensions and work in the Einstein frame throughout.</p>
<span class="is-sr-only" role="status"></span>
```

- `.ds-permalink` — The Permalink control from [Linking to a section](links.md#linking-to-a-section), the same as on every other page. The demo holds it open.
- `.is-sr-only` — Completes the name: “Permalink to section 2, Setup”. The name starts with the visible word.
- `[role="status"]` — One region on the page. `anchors.js` writes “Link to section 2, Setup copied” into it, shows the green tick in place of the link icon, and clears both after 2 seconds.
- `.is-active` — Set on the heading by a tap, on screens without hover.

> Meets accessibility guideline [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A)

## Equations, figures and references

A display equation, a figure and a bibliography entry each have a small row of actions on their bottom edge. The row shows on hover, on keyboard focus and after a tap.

```html
<div class="ds-paper-element">
  <!-- LaTeXML's MathML, unchanged -->
  <div class="ds-element-pill" role="toolbar" aria-label="Equation 2.14">
    <button type="button" aria-pressed="false"><svg aria-hidden="true">…</svg>View TeX<span class="is-sr-only"> of equation 2.14</span></button>
    <button type="button"><svg aria-hidden="true">…</svg>Copy<span class="is-sr-only"> equation 2.14</span></button>
    <button type="button"><svg aria-hidden="true">…</svg>Permalink<span class="is-sr-only"> to equation 2.14</span></button>
  </div>
</div>
<figure class="ds-paper-element">
  <details class="ds-marginalia">
    <summary><svg aria-hidden="true">…</svg><span class="is-sr-only">Alt text</span></summary>
    <p class="ds-marginalia-body ds-annotation"><strong>Alt text</strong><br>Line chart of the power spectrum against scale. The solid blue line rises steeply; the dashed red line rises gently.</p>
  </details>
  <img src="fig1.png" alt="Line chart of the power spectrum against scale. The solid blue line rises steeply; the dashed red line rises gently." width="400" height="200">
  <figcaption>Figure 1: The scalar power spectrum in the Newtonian gauge (solid) and the comoving gauge (dashed).</figcaption>
  <div class="ds-element-pill" role="toolbar" aria-label="Figure 1">
    <button type="button" class="is-cta"><svg aria-hidden="true">…</svg>Expand<span class="is-sr-only"> figure 1</span></button>
    <button type="button"><svg aria-hidden="true">…</svg>Permalink<span class="is-sr-only"> to figure 1</span></button>
  </div>
</figure>
<div class="ds-paper-element">
  <p>[30] A. Ashtekar and M. Bojowald. Quantum geometry and the Schwarzschild singularity. <em>Class. Quantum Grav.</em> 23 (2006) 391.</p>
  <div class="ds-element-pill" role="toolbar" aria-label="Reference 30">
    <button type="button"><svg aria-hidden="true">…</svg>Permalink<span class="is-sr-only"> to reference 30</span></button>
  </div>
</div>
<span class="is-sr-only" role="status"></span>
```

- `.ds-paper-element` — The wrapper round one equation, figure or entry. Hovering it, focusing anything inside it, or tapping it shows a hairline border and the pill. The demo holds all three open.
- `.ds-element-pill` — The actions, as on [Buttons](buttons.md#small-actions-attached-to-content): one tab stop per element, with the arrow keys moving between its actions. Focusing an action shows the pill.
- `.is-sr-only` — Each action's name says which element it acts on: “Permalink to equation 2.14”, not “Permalink” a hundred times.
- `[aria-pressed]` — On View TeX, which switches the equation to its TeX and back. Its label becomes “View math”.
- `.ds-marginalia` — The figure's alt text, under the label “Alt text”, in the margin at wide widths and folded to its info mark when narrower. See [Marginalia](layout-patterns.md#marginalia).
- `.is-cta` — Expand, the one main action on a figure. It opens the figure viewer.
- `[role="status"]` — One region on the page, where the script confirms a copy in words: “Link to equation 2.14 copied”.

> **Alt text**Line chart of the power spectrum against scale. The solid blue line rises steeply; the dashed red line rises gently.

## Rules

- **Show the author's text as written.** A title or abstract is never shortened, reworded or corrected. When we display TeX, it is shown exactly as the author wrote it. We excerpt formulas, but never edit them.
- **Leave out what a paper does not have.** No empty labels and no placeholders.
- **Every date has its label.** Readers confuse submitted and announced dates when either stands alone.
- **The primary category comes first** and is told apart by more than colour: its tooltip names it as primary.
- **The identity line comes first.** Many readers arrive at a paper directly, without passing its abstract page. It is centred and spans the page to the gutters.
- **The abstract has a heading, hidden from sight.** An `<h2 class="is-sr-only">Abstract</h2>` puts it in the heading outline without adding a line above it.
- **The paper follows its abstract on the same page.** A reader reaches the first section by scrolling, by the TOC bar or by the skip link, with no click to open the paper.
- **The page has one `<main>`**, from the area above the identity line to the end of the paper, the sidebar included. The site header, the TOC bar and the footer are outside it, and the first skip link goes to it. When LaTeXML's output has no `<main>`, the page around the paper supplies it.
- **An optional area above the identity line** holds a temporary message or link, such as Back to abstract while readers move to HTML papers. It is `.ds-btn-text` for a link, or an alert for a message.
- **The licence is a link, with no explanation.**
- **Other formats, when a paper has them, are a link in the sidebar**, under TeX Source and above Ancillary Files.
- **The sidebar order is Files, Cite, Paper information.** Files and Cite are always open; Version history, Accessibility and Metadata, under Paper information, start closed, and only one is open at a time (see [One panel open at a time](progressive-disclosure.md#one-panel-open-at-a-time)).
- **Every download shows its size.**
- **A citation names the arXiv identifier and the arXiv DOI**, never the HTML page, even when the paper has a journal reference.
- **BibTeX lists every author.** “and others” becomes “et al.” in a reference manager, and the other authors are lost.
- **APA, Chicago and MLA follow their own style rules** for long author lists.
- **Every citation format is in the page.** The script only chooses which one shows.
- **The accessibility panel lists only what the paper has.** A missing capability has no line, and there is no overall score.
- **The status goes before the title, never into it.** “Withdrawn:” or “Removed:” is its own element inside the heading, and the page's `<title>` starts with it. The author's title is not edited.
- **The notice comes straight after the title, before the dates.** It says who withdrew or removed the paper and gives the reason as written, in quotes.
- **Every version of a withdrawn paper shows the notice.** On an earlier version it takes the place of the older-version warning. A reader who arrives at an earlier version by a link must still learn that the paper was withdrawn.
- **The withdrawal notice links to the last version that can be read, except on that version.**
- **Without a text, what acts on a text goes.** The paper body, the TOC bar, Files, Cite and the Accessibility panel are left out; the sidebar holds Paper information alone. An earlier version of a withdrawn paper keeps them all.
- **A removed version keeps its license, but not its cross-listed categories.** arXiv may remove the license, or any other metadata, when there is a legal reason to, as [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2 allows.
- **A citation of an earlier version says the paper was withdrawn.** Each format ends with a note, such as “This paper was withdrawn, 22 Oct 2026”, so the status travels with the citation.
- Display guidelines for withdrawn and removed papers follow [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf).
- **The body markup is LaTeXML's, unchanged.** arXiv styles it from outside with CSS and never rewrites, reorders or wraps the author's elements.
- **ar5iv's stylesheet is in a cascade layer**, so an ordinary rule outranks it without `!important`. The `arxiv-override` layer is only for a property ar5iv itself marks `!important`.
- **Body text is set as on [Typography](typography.md).** ar5iv sets weight 300, so set 400.
- **Body text is left-aligned, never justified.** Inline math gives a justified line nowhere to break.
- **Body text is hyphenated** with `hyphens: auto`. It needs the page's `lang` attribute, which tells the browser which language to hyphenate.
- **A figure caption is Plex Sans at 0.875rem, left-aligned, the width of the figure.** Its label, text and punctuation are as the author wrote them.
- **Paper figures keep ar5iv's white background in dark mode; arXiv's own images do not.** Clear it on the header, TOC bar and footer images.
- **LaTeXML's beta badge and conversion logo are not shown.**
- **The contents list repeats the author's headings exactly**, including subsections, appendices, acknowledgements and references. Math in a heading appears as it renders, never as its TeX: copy LaTeXML's contents entries with their MathML. A script that reads a heading's words leaves out the TeX annotation, as `toc.js` and `anchors.js` do.
- **LaTeXML's own sidebar is not shown.** The `.ds-toc` list replaces it.
- **Each link in the bar shows an icon and its name.**
- **PDF opens in a new tab, in the bar and in the sidebar**, so the reader keeps their place in the HTML paper. It has the external-link icon and “(opens in a new tab)”, as on [Links](links.md).
- **A second skip link goes to the paper's first section**, before the sidebar, so a keyboard user can pass it.
- **Every link to a place in the paper lands below the TOC bar.** The bar sets `scroll-padding-top`, which covers the TOC, a permalink, a citation and a cross-reference; a script that scrolls uses `scrollIntoView`, which respects it.
- **Every section, subsection and appendix heading has a Permalink control.** It copies the address with the section's LaTeXML id and the version: `…/2604.22725v1#S2`.
- **The accessible name starts with the visible word**, then names the section.
- **Copying is announced in words**, as in [Confirm an action that changes nothing on screen](../action-feedback.html).
- **One action gets the Permalink control; several get the element pill.**
- **Inline math gets nothing from arXiv**: no tabindex, role, ARIA or actions. Assistive technology reads its MathML directly.
- **View TeX swaps the equation for its TeX in place**, in plain monospace with no code box. The TeX view is hidden until asked for, and MathML annotations are never displayed.
- **View TeX and Copy use the TeX that LaTeXML keeps with the equation.** LaTeXML expands the author's own macros into standard TeX, so the copy works outside the paper. The author's own files are the TeX Source download.
- **Copy copies what is on screen**: the MathML in math view, the TeX in TeX view.
- **A wide equation scrolls inside its own box, never the page.** The box has `tabindex="0"`, `role="region"` and a name: “Equation 2.14, scrolls sideways”.
- **The equation number stays in view**, pinned to the right edge while the equation scrolls.
- **Only the author's alt text is shown**, whole and unchanged. The image's `alt` is never changed, and no reader-written or machine-written description is added. Write it in with `textContent`.
- **Long alt text is not shortened.** This is the one margin note longer than two sentences.
- **A figure without alt text says so.** Its margin note reads “No alt text provided”, in `--ds-text-muted`, with a link to how to add alt text.
- **Expand opens the figure viewer**, a `.ds-modal.ds-modal--wide` with `closedby="any"`. Clicking the image opens it too; Expand is the keyboard path.
- **The viewer shows a copy.** The figure in the paper is never moved or changed.
- **The viewer shows the caption exactly as the author wrote it**, under the figure. The dialog is named by the caption's own label, such as “Figure 1:”, with `aria-labelledby`.
- **Zoom stays until the reader closes the viewer.** Zoom in, Zoom out and Fit buttons, the wheel, double-click, pinch and the +, - and 0 keys all work; drag or the arrow keys pan.
- **The zoom level is shown and announced**, with `aria-live="polite"`.
- **Closing returns focus to what opened the viewer.**
- **Zoom is animated only when reduced motion is not set.**
- **Print hides the TOC bar, the permalinks, the element pills and every popover.** The identity line prints at 10pt.
- **No page break inside an equation, table or figure, and none straight after a heading.** Sections may break.
- **Paper titles are always a heading**, so a screen reader user can easily find it and move from paper to paper in a list.
- **Name each format link's paper.** In a list, “PDF” alone is the same link text fifty times; an `.is-sr-only` span adds the identifier.
- **Category names are in the tooltip, never only in a `title` attribute.** See [Tooltip](forms.md#tooltip).
- **Paper title just before links.** For screen reader users, to maintain context, the title should appear before the format links, and just before them, so that the context is not forgotten. That means displaying the row with dates and links using the CSS `order` property (ie: the visual display will show the dates first, but the DOM order lists the links first).
- **Say a withdrawal in words.** On a withdrawn or removed paper the status starts the title and the page's `<title>`, and the notice follows the title as a heading, so a screen reader meets both first. The red adds to the words and never replaces them.
