---
page: versions.html
title: "Indicate which version is being read"
summary: "A paper can have many versions, and a reader can arrive at any of them from a link. Show which version is open, how it relates to the others and whether the paper has been withdrawn. Version display patterns should be applied consistently on both public and internal pages."
stylesheet: design-system.css
components:
  - id: where-it-is-used
    title: "Where it is used"
    summary: ""
    notes:
      - "A paper's own HTML page or abstract: the version row under the title, and the Version history panel in the sidebar (see [Papers](papers.md#the-sidebar)).; Internal tools that show a paper by version, such as the admin console's paper details."
  - id: version-row
    title: "Version row"
    summary: "Every paper shows its dates under the title, and its versions once there is more than one. What is shown depends on how many versions there are, which one the reader is viewing, and whether the paper has been withdrawn or a version removed."
    classes:
      - name: ".ds-date-row"
        does: "The row. One `<p>` that holds the dates and, after them, the version links. Small type in the muted colour, with tabular figures so the digits line up."
      - name: "<time datetime>"
        does: "Every date. Announced is a full instant (`2026-01-11T01:32Z`); Submitted and Revised are date-only (`2026-01-10`). In the visible text, bind the day, month, year and clock time to each other with `&nbsp;`, and bind UTC to its date the same way, outside the element."
      - name: ".is-sr-only"
        does: "The separator. The visible \"·\" is `aria-hidden`, and the sr-only comma beside it is what a screen reader gets between one date and the next."
      - name: ".ds-version-list"
        does: "The versions. A `<span>` at the end of the `.ds-date-row`, after a dot: every version, oldest first. A taller line and wider word spacing keep the version links 24px apart."
      - name: ".ds-version"
        does: "One version number, in the mono face. A prior version is an `<a>` with an `href`, and takes the page's link colour and underline. The version being viewed is a `<strong>`, not a link, in a box: the accent tint, edged in the strong accent."
      - name: "aria-current=\"true\""
        does: "On the version being viewed, which draws the box. The current version is marked by the box, the bold and the missing underline, never by colour alone. The `.is-sr-only` span inside it says \", this version\", because the attribute alone is not announced by every screen reader."
      - name: ".is-sr-only"
        does: "Inside every prior-version link, after the visible \"v1\": \", version 1\". The visible \"v1\" on its own does not say which version the link opens. A screen reader reads the link as \"v1, version 1\"."
      - name: ".ds-alert.ds-alert--warning"
        does: "The older-version warning, documented on [Alerts](alerts.md): the warning state, the triangle icon copied whole, and no role, because it is in the page as it loads. Render it only when the version being viewed is not the latest. One sentence that names the version being viewed, then a link straight to the latest one."
      - name: "aria-current=\"true\""
        does: "On v1 here, since v1 is the version being viewed. \"(this version)\" moves to the Submitted date for the same reason."
      - name: ".ds-show-more"
        does: "The control that expands the list, documented on [Progressive disclosure](progressive-disclosure.md#show-more). Requires `aria-expanded`, flipped on every press, and `aria-controls` naming every region it shows or hides; `show-more.js`, once per page, does the flipping. The label includes the total: \"show all 12 versions\", and \"show fewer\" once open."
      - name: "[hidden]"
        does: "On the span that holds the elided versions. The attribute, not a class: the hidden links are out of the tab order while they are off screen. The full list is in the HTML the server sends; a script adds `hidden` and the button, so with no JavaScript the reader gets every version."
      - name: "aria-hidden=\"true\""
        does: "On the ellipsis, which is decoration. The `.is-sr-only` span beside it says which versions are hidden. Both sit in one span that the button hides when the list opens."
      - name: "aria-controls=\"v7-elide-a v7-tail-a v7-elide-b v7-tail-b\""
        does: "When the viewed version falls inside the elision there are two ellipses and two hidden spans. List all four ids, separated by spaces, so one press opens the whole list."
      - name: "[hidden]"
        does: "Absent. This is the row as the server sends it: every version in the list, no elision, no button. The row wraps like any other line of text."
      - name: ".ds-version--error"
        does: "With `.ds-version`: the withdrawal notice, in the error colors. Being viewed, it is a `<strong>` in a red box; anywhere else, a red link to the notice."
      - name: ".ds-date-row"
        does: "Ends with “Withdrawn” and the date of the withdrawal."
      - name: ".is-sr-only"
        does: "\", this page\" on the notice being viewed. It is a notice, not a revision, so it does not say \", this version\"."
      - name: ".ds-version--error"
        does: "On the withdrawn version when it is being viewed, and on the link to the notice. Any other version keeps its usual look. The paper's withdrawal notice, under its title, says the same in words, so the color is never the only sign."
      - name: ".ds-alert--warning"
        does: "Not on an earlier version of a withdrawn paper: the withdrawal notice under the title takes the place of the older-version warning. See [Withdrawn and removed papers](papers.md#withdrawn-papers)."
      - name: "aria-current=\"true\""
        does: "On v2, without `.ds-version--error`: v2 is not the withdrawn version, so its box keeps the accent, as on any paper. v3 is an ordinary link, and only the link to the notice is red."
      - name: ".ds-date-row"
        does: "Ends with Removed and its date. A removal changes the version in place, so no version is added to the list. What else changes on the page is in [Withdrawn and removed papers](papers.md#withdrawn-papers)."
      - name: ".ds-date-row"
        does: "Revised is this version's date, and Removed and its date follow it."
      - name: ".ds-version--error"
        does: "On the removed version when it is being viewed, as on a withdrawn version. Any other version keeps its usual look, so on v3 the link to v2 is an ordinary link; Version history says that v2 was removed."
      - name: ".ds-alert--warning"
        does: "Not on a removed version: the removal notice under the title takes the place of the older-version warning, and links to the latest version."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A) and [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A)"
      - "Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §1.2, which states that a retraction notice is “a distinct publication”."
      - "Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2, which sets a retracted publication apart “in a different color from other site elements”."
      - "If you are viewing V1, we add **(this version)** to the submitted date.; In all cases, an amber warning appears (not error red or neutral blue) pointing to the current version."
      - "The inline list keeps its first three and last three and elides the middle with an ellipsis. The elided versions are still in the DOM, but hidden with `hidden` and `aria-hidden`.; The ellipsis has `aria-hidden` and a screen-reader-only span beside it says \"versions 4 through 9 hidden,\" so the reader knows there are more versions than they can see.; The version being viewed always stays visible, wherever it falls in the list. It may interrupt the ellipsis.; A text button displays the total count and expands the full list.; The expanded list shows all versions in a list, wrapping if necessary. No javascript required."
  - id: version-history-panel
    title: "Version history panel"
    summary: "In the sidebar, Version history lists every version, newest first, with its date and the comments the author wrote for it. The newest version is labelled Latest, and the one being read is labelled Viewing."
    classes:
      - name: ".ds-paper-versions"
        does: "An `<ol>` inside the Version history accordion, under Paper information in the sidebar (see [Papers](papers.md#the-sidebar)). Every version, newest first. Each entry is a `.ds-date-row` with the version, its date and its labels, then the comments the author wrote for that version."
      - name: "aria-current=\"true\""
        does: "On the `<li>` being read. It draws the bar beside the entry and the box around its number in the accent. The number is a `<strong>`, not a link, and the visible label “Viewing” says the same in words."
      - name: ".ds-version"
        does: "Every other version is a link to its abstract page, with a hidden “, version 2”, as in the version row."
      - name: "aria-current=\"true\""
        does: "Moves to the entry being read. “Latest” stays on the newest version, which stays a link."
      - name: ".ds-paper-versions"
        does: "Newest first, as on any paper, with the withdrawal notice first, in its place in the paper's history. Its line says who withdrew the paper. No entry says “Latest”: the notice is not a version."
      - name: ".ds-version--error"
        does: "On the notice's `<li>` and its name. Being viewed, the notice takes a red box and a red bar, and says “Viewing” like any entry being read."
      - name: ".ds-version--error"
        does: "On the notice's `<li>` and its link. When the withdrawn version is being viewed, also on its `<li>` and its number, which turns the bar beside the entry red."
      - name: ".ds-version--error"
        does: "Only on the notice's `<li>` and its link. v2 is not the withdrawn version, so its entry keeps the accent bar and box."
      - name: ".ds-version--error"
        does: "On the removed version's `<li>` and its number only while it is being viewed, which turns the bar beside the entry red. On any other version, the entry keeps its usual look and the line under the date says it was removed."
      - name: ".ds-paper-versions > li > p"
        does: "The removal line comes first, then the author's comments for that version, which stay: a removal takes the full text, not the metadata."
    notes:
      - "Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2: “Display related links and updates chronologically to tell the retracted publication’s story over time.”"
rules:
  - "**Version links go to abstract pages.**"
  - "**The dates and the older-version warning stay by the title.** The full history goes in the sidebar."
  - "**Each version shows its own comments**, as the author wrote them for that version."
  - "Display guidelines for withdrawn and removed papers follow [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf). The status before the title, the notice and what leaves the page are in [Papers](papers.md#withdrawn-paper-rules)."
  - "**We use the term “Withdrawal notice” in the version dates and Version history**, because that is a more accurate description of its role. The identity line still shows the version number."
  - "**Red marks a withdrawn or removed version only when it is being read.** Any earlier version being read keeps its usual look, and the link to the notice is always red."
  - "**Submitted [v1 date] UTC · Announced [announcement date and time] UTC** are always shown, in that order, separated by a dot. Announced is when the paper first entered the public listing. Revision dates are when subsequent versions of the same paper went public. Dates use `<time datetime>`."
  - "Announcement is the date that readers care about the most. It renders as **11 Jan 2026, 01:32 UTC**. Submitted and Revised stay date-only to save space."
  - "When only the month of the announcement is known, as in a search index, show the month: **Announced Sep 2026**, with `datetime=\"2026-09\"`."
  - "arXiv's platform serves a global audience across all timezones. UTC was chosen as the universal standard to ensure consistency and clarity for all users. It is a group decision, made with arXiv staff."
  - "Times are rendered in plain-text **UTC** bound to its date with `&nbsp;` so a wrap never separates them. The `<time>` element is not bound to the date."
  - "Inside `datetime`, announced is a full instant (`2026-01-11T01:32Z`), Submitted and Revised stay date-only (`2026-01-10`)."
  - "The version being viewed is distinguished by a box, by weight and by `aria-current` and does not depend on color alone. It is deliberately not a link because the reader is already viewing it."
  - "Prior versions are inline links alongside other text, so they are underlined. Each also has a hidden span that says which version it opens, so a screen reader reads \"v1, version 1\"."
  - "The ellipsis is decoration (`aria-hidden`) with an sr-only count of what is hidden; the working affordance is a text button showing the explicit total (\"show all 127 versions\"), toggling `aria-expanded`. The full list is server-rendered and collapsed by the script in `html.js`. Without JavaScript, the fallback is that readers see the full list of versions."
  - "**Mark the version being viewed.** Put `aria-current=\"true\"` on it, make it a `<strong>` and not a link, and put `<span class=\"is-sr-only\">, this version</span>` inside it. Bold alone is invisible to a screen reader, and the attribute alone is not read out by every one."
  - "**Say which version each link opens.** Every prior-version link has `<span class=\"is-sr-only\">, version 2</span>` after its visible \"v2\". The visible \"v2\" does not say which version the link opens, and a screen reader user listing the links on the page hears each one out of context. Use the span, not an `aria-label`: the link's name has to start with the \"v2\" that a speech recognition user sees and says, and translation tools do not translate `aria-label`."
  - "**Put the warning where it is read early.** The older-version warning is part of the page as it loads, so it takes no role (see [Alerts](alerts.md)); it comes straight after the title and the dates. Render it only when the reader is not on the latest version; an alert that is always there is noise."
  - "**Separate the dates in words.** The visible \"·\" between dates is `aria-hidden=\"true\"`, and a `<span class=\"is-sr-only\">, </span>` sits beside it. Without the comma the three dates are read as one run-on sentence."
  - "**Say what the ellipsis hides.** The \"…\" is decoration and is `aria-hidden=\"true\"`. The `.is-sr-only` span beside it says which versions are hidden, and the button says the total: \"show all 12 versions\". Use the `hidden` attribute on the hidden versions, never a class, so they are out of the tab order while they are off screen."
---

# Indicate which version is being read

A paper can have many versions, and a reader can arrive at any of them from a link. Show which version is open, how it relates to the others and whether the paper has been withdrawn. Version display patterns should be applied consistently on both public and internal pages.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Where it is used



> A paper's own HTML page or abstract: the version row under the title, and the Version history panel in the sidebar (see [Papers](papers.md#the-sidebar)).; Internal tools that show a paper by version, such as the admin console's paper details.

## Version row

Every paper shows its dates under the title, and its versions once there is more than one. What is shown depends on how many versions there are, which one the reader is viewing, and whether the paper has been withdrawn or a version removed.

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10&nbsp;Jan&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11&nbsp;Jan&nbsp;2026,&nbsp;01:32</time>&nbsp;UTC
</p>
```

- `.ds-date-row` — The row. One `<p>` that holds the dates and, after them, the version links. Small type in the muted colour, with tabular figures so the digits line up.
- `<time datetime>` — Every date. Announced is a full instant (`2026-01-11T01:32Z`); Submitted and Revised are date-only (`2026-01-10`). In the visible text, bind the day, month, year and clock time to each other with `&nbsp;`, and bind UTC to its date the same way, outside the element.
- `.is-sr-only` — The separator. The visible "·" is `aria-hidden`, and the sr-only comma beside it is what a screen reader gets between one date and the next.

**Viewing v3 of 3 (latest)**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10&nbsp;Jan&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11&nbsp;Jan&nbsp;2026,&nbsp;01:32</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-04-24">24&nbsp;Apr&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a>
  <strong class="ds-version" aria-current="true">v3<span class="is-sr-only">, this version</span></strong>
  </span>
</p>
```

- `.ds-version-list` — The versions. A `<span>` at the end of the `.ds-date-row`, after a dot: every version, oldest first. A taller line and wider word spacing keep the version links 24px apart.
- `.ds-version` — One version number, in the mono face. A prior version is an `<a>` with an `href`, and takes the page's link colour and underline. The version being viewed is a `<strong>`, not a link, in a box: the accent tint, edged in the strong accent.
- `aria-current="true"` — On the version being viewed, which draws the box. The current version is marked by the box, the bold and the missing underline, never by colour alone. The `.is-sr-only` span inside it says ", this version", because the attribute alone is not announced by every screen reader.
- `.is-sr-only` — Inside every prior-version link, after the visible "v1": ", version 1". The visible "v1" on its own does not say which version the link opens. A screen reader reads the link as "v1, version 1".

**Viewing v1, latest is v3**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10&nbsp;Jan&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11&nbsp;Jan&nbsp;2026,&nbsp;01:32</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <strong class="ds-version" aria-current="true">v1<span class="is-sr-only">, this version</span></strong>
  <a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a>
  <a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a>
  </span>
</p>
<div class="ds-alert ds-alert--warning">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
    <path d="M12 9v4"/>
    <path d="M12 17h.01"/>
  </svg>
  <div class="ds-alert-content">
    <p><strong>You are viewing version 1.</strong> A newer version is available — <a href="#v3">version 3, revised 24&nbsp;Apr&nbsp;2026</a>.</p>
  </div>
</div>
```

- `.ds-alert.ds-alert--warning` — The older-version warning, documented on [Alerts](alerts.md): the warning state, the triangle icon copied whole, and no role, because it is in the page as it loads. Render it only when the version being viewed is not the latest. One sentence that names the version being viewed, then a link straight to the latest one.
- `aria-current="true"` — On v1 here, since v1 is the version being viewed. "(this version)" moves to the Submitted date for the same reason.

**Viewing v12 of 12 (latest), collapsed**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10&nbsp;Jan&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11&nbsp;Jan&nbsp;2026,&nbsp;01:32</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-06-30">30&nbsp;Jun&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a>
  <a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a>
  <span id="v12-elide"><span aria-hidden="true">…</span><span class="is-sr-only">versions 4 through 9 hidden,</span></span>
  <span id="v12-tail" hidden>
    <a class="ds-version" href="#v4">v4<span class="is-sr-only">, version 4</span></a>
    <a class="ds-version" href="#v5">v5<span class="is-sr-only">, version 5</span></a>
    <a class="ds-version" href="#v6">v6<span class="is-sr-only">, version 6</span></a>
    <a class="ds-version" href="#v7">v7<span class="is-sr-only">, version 7</span></a>
    <a class="ds-version" href="#v8">v8<span class="is-sr-only">, version 8</span></a>
    <a class="ds-version" href="#v9">v9<span class="is-sr-only">, version 9</span></a>
  </span>
  <a class="ds-version" href="#v10">v10<span class="is-sr-only">, version 10</span></a>
  <a class="ds-version" href="#v11">v11<span class="is-sr-only">, version 11</span></a>
  <strong class="ds-version" aria-current="true">v12<span class="is-sr-only">, this version</span></strong>
  <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false" aria-controls="v12-elide v12-tail">show all 12 versions</button>
  </span>
</p>
<script src="show-more.js" defer></script>
```

- `.ds-show-more` — The control that expands the list, documented on [Progressive disclosure](progressive-disclosure.md#show-more). Requires `aria-expanded`, flipped on every press, and `aria-controls` naming every region it shows or hides; `show-more.js`, once per page, does the flipping. The label includes the total: "show all 12 versions", and "show fewer" once open.
- `[hidden]` — On the span that holds the elided versions. The attribute, not a class: the hidden links are out of the tab order while they are off screen. The full list is in the HTML the server sends; a script adds `hidden` and the button, so with no JavaScript the reader gets every version.
- `aria-hidden="true"` — On the ellipsis, which is decoration. The `.is-sr-only` span beside it says which versions are hidden. Both sit in one span that the button hides when the list opens.

**Viewing v7 of 12**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10&nbsp;Jan&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11&nbsp;Jan&nbsp;2026,&nbsp;01:32</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-03-12">12&nbsp;Mar&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a>
  <a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a>
  <span id="v7-elide-a"><span aria-hidden="true">…</span><span class="is-sr-only">versions 4 through 6 hidden,</span></span>
  <span id="v7-tail-a" hidden>
    <a class="ds-version" href="#v4">v4<span class="is-sr-only">, version 4</span></a>
    <a class="ds-version" href="#v5">v5<span class="is-sr-only">, version 5</span></a>
    <a class="ds-version" href="#v6">v6<span class="is-sr-only">, version 6</span></a>
  </span>
  <strong class="ds-version" aria-current="true">v7<span class="is-sr-only">, this version</span></strong>
  <span id="v7-elide-b"><span aria-hidden="true">…</span><span class="is-sr-only">versions 8 through 9 hidden,</span></span>
  <span id="v7-tail-b" hidden>
    <a class="ds-version" href="#v8">v8<span class="is-sr-only">, version 8</span></a>
    <a class="ds-version" href="#v9">v9<span class="is-sr-only">, version 9</span></a>
  </span>
  <a class="ds-version" href="#v10">v10<span class="is-sr-only">, version 10</span></a>
  <a class="ds-version" href="#v11">v11<span class="is-sr-only">, version 11</span></a>
  <a class="ds-version" href="#v12">v12<span class="is-sr-only">, version 12</span></a>
  <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false" aria-controls="v7-elide-a v7-tail-a v7-elide-b v7-tail-b">show all 12 versions</button>
  </span>
</p>
<div class="ds-alert ds-alert--warning">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
    <path d="M12 9v4"/>
    <path d="M12 17h.01"/>
  </svg>
  <div class="ds-alert-content">
    <p><strong>You are viewing version 7.</strong> A newer version is available — <a href="#v12">version 12, revised 30&nbsp;Jun&nbsp;2026</a>.</p>
  </div>
</div>
```

- `aria-controls="v7-elide-a v7-tail-a v7-elide-b v7-tail-b"` — When the viewed version falls inside the elision there are two ellipses and two hidden spans. List all four ids, separated by spaces, so one press opens the whole list.

**Expanded, show all 24 versions**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10&nbsp;Jan&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11&nbsp;Jan&nbsp;2026,&nbsp;01:32</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-06-30">30&nbsp;Jun&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a>
  <a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a>
  <span id="v24-elide" hidden><span aria-hidden="true">…</span><span class="is-sr-only">versions 4 through 21 hidden,</span></span>
  <span id="v24-tail">
    <a class="ds-version" href="#v4">v4<span class="is-sr-only">, version 4</span></a>
    <a class="ds-version" href="#v5">v5<span class="is-sr-only">, version 5</span></a>
    <a class="ds-version" href="#v6">v6<span class="is-sr-only">, version 6</span></a>
    <a class="ds-version" href="#v7">v7<span class="is-sr-only">, version 7</span></a>
    <a class="ds-version" href="#v8">v8<span class="is-sr-only">, version 8</span></a>
    <a class="ds-version" href="#v9">v9<span class="is-sr-only">, version 9</span></a>
    <a class="ds-version" href="#v10">v10<span class="is-sr-only">, version 10</span></a>
    <a class="ds-version" href="#v11">v11<span class="is-sr-only">, version 11</span></a>
    <a class="ds-version" href="#v12">v12<span class="is-sr-only">, version 12</span></a>
    <a class="ds-version" href="#v13">v13<span class="is-sr-only">, version 13</span></a>
    <a class="ds-version" href="#v14">v14<span class="is-sr-only">, version 14</span></a>
    <a class="ds-version" href="#v15">v15<span class="is-sr-only">, version 15</span></a>
    <a class="ds-version" href="#v16">v16<span class="is-sr-only">, version 16</span></a>
    <a class="ds-version" href="#v17">v17<span class="is-sr-only">, version 17</span></a>
    <a class="ds-version" href="#v18">v18<span class="is-sr-only">, version 18</span></a>
    <a class="ds-version" href="#v19">v19<span class="is-sr-only">, version 19</span></a>
    <a class="ds-version" href="#v20">v20<span class="is-sr-only">, version 20</span></a>
    <a class="ds-version" href="#v21">v21<span class="is-sr-only">, version 21</span></a>
  </span>
  <a class="ds-version" href="#v22">v22<span class="is-sr-only">, version 22</span></a>
  <a class="ds-version" href="#v23">v23<span class="is-sr-only">, version 23</span></a>
  <strong class="ds-version" aria-current="true">v24<span class="is-sr-only">, this version</span></strong>
  <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="true" aria-controls="v24-elide v24-tail" data-closed-label="show all 24 versions">show fewer</button>
  </span>
</p>
```

- `[hidden]` — Absent. This is the row as the server sends it: every version in the list, no elision, no button. The row wraps like any other line of text.

**Viewing the withdrawal notice**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-04-24">24&nbsp;Apr&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-04-25T02:07Z">25&nbsp;Apr&nbsp;2026,&nbsp;02:07</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Withdrawn <time datetime="2026-10-22">22&nbsp;Oct&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a>
  <a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a>
  <strong class="ds-version ds-version--error" aria-current="true">Withdrawal notice<span class="is-sr-only">, this page</span></strong>
  </span>
</p>
```

- `.ds-version--error` — With `.ds-version`: the withdrawal notice, in the error colors. Being viewed, it is a `<strong>` in a red box; anywhere else, a red link to the notice.
- `.ds-date-row` — Ends with “Withdrawn” and the date of the withdrawal.
- `.is-sr-only` — ", this page" on the notice being viewed. It is a notice, not a revision, so it does not say ", this version".

**Viewing the impacted version**

```html
<p class="ds-date-row">
  …Submitted and Announced, as above…
  Revised <time datetime="2026-06-28">28&nbsp;Jun&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a>
  <strong class="ds-version ds-version--error" aria-current="true">v3<span class="is-sr-only">, this version</span></strong>
  <a class="ds-version ds-version--error" href="#withdrawal">Withdrawal notice</a>
  </span>
</p>
```

- `.ds-version--error` — On the withdrawn version when it is being viewed, and on the link to the notice. Any other version keeps its usual look. The paper's withdrawal notice, under its title, says the same in words, so the color is never the only sign.
- `.ds-alert--warning` — Not on an earlier version of a withdrawn paper: the withdrawal notice under the title takes the place of the older-version warning. See [Withdrawn and removed papers](papers.md#withdrawn-papers).

**Viewing v2 of a withdrawn paper**

```html
<p class="ds-date-row">
  …Submitted and Announced, as above…
  Revised <time datetime="2026-05-19">19&nbsp;May&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <strong class="ds-version" aria-current="true">v2<span class="is-sr-only">, this version</span></strong>
  <a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a>
  <a class="ds-version ds-version--error" href="#withdrawal">Withdrawal notice</a>
  </span>
</p>
```

- `aria-current="true"` — On v2, without `.ds-version--error`: v2 is not the withdrawn version, so its box keeps the accent, as on any paper. v3 is an ordinary link, and only the link to the notice is red.

**A paper with one version**

```html
<p class="ds-date-row">
  …Submitted and Announced…
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Removed <time datetime="2026-10-23">23&nbsp;Oct&nbsp;2026</time>&nbsp;UTC
</p>
```

- `.ds-date-row` — Ends with Removed and its date. A removal changes the version in place, so no version is added to the list. What else changes on the page is in [Withdrawn and removed papers](papers.md#withdrawn-papers).

**Viewing v2, which arXiv removed**

```html
<p class="ds-date-row">
  …Submitted and Announced, as above…
  Revised <time datetime="2026-05-19">19&nbsp;May&nbsp;2026</time>&nbsp;UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Removed <time datetime="2026-10-23">23&nbsp;Oct&nbsp;2026</time>&nbsp;UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span><span class="ds-version-list">
  <a class="ds-version" href="#v1">v1<span class="is-sr-only">, version 1</span></a>
  <strong class="ds-version ds-version--error" aria-current="true">v2<span class="is-sr-only">, this version</span></strong>
  <a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a>
  </span>
</p>
```

- `.ds-date-row` — Revised is this version's date, and Removed and its date follow it.
- `.ds-version--error` — On the removed version when it is being viewed, as on a withdrawn version. Any other version keeps its usual look, so on v3 the link to v2 is an ordinary link; Version history says that v2 was removed.
- `.ds-alert--warning` — Not on a removed version: the removal notice under the title takes the place of the older-version warning, and links to the latest version.

> Meets accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A) and [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A)

> Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §1.2, which states that a retraction notice is “a distinct publication”.

> Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2, which sets a retracted publication apart “in a different color from other site elements”.

> If you are viewing V1, we add **(this version)** to the submitted date.; In all cases, an amber warning appears (not error red or neutral blue) pointing to the current version.

> The inline list keeps its first three and last three and elides the middle with an ellipsis. The elided versions are still in the DOM, but hidden with `hidden` and `aria-hidden`.; The ellipsis has `aria-hidden` and a screen-reader-only span beside it says "versions 4 through 9 hidden," so the reader knows there are more versions than they can see.; The version being viewed always stays visible, wherever it falls in the list. It may interrupt the ellipsis.; A text button displays the total count and expands the full list.; The expanded list shows all versions in a list, wrapping if necessary. No javascript required.

## Version history panel

In the sidebar, Version history lists every version, newest first, with its date and the comments the author wrote for it. The newest version is labelled Latest, and the one being read is labelled Viewing.

**Viewing v3 of 3 (latest)**

```html
<details class="ds-acc">
  <summary>Version history</summary>
  <div class="ds-acc-body">
    <ol class="ds-paper-versions">
      <li aria-current="true">
        <p class="ds-date-row"><strong class="ds-version">v3</strong> · <time datetime="2026-06-28">28&nbsp;Jun&nbsp;2026</time>&nbsp;UTC · Latest · Viewing</p>
        <p>18 pages, 6 figures. Updated discussion of scalar spectral index in Sec. 4. Added comparison with Planck 2018 data. Matches published version.</p>
      </li>
      <li>
        <p class="ds-date-row"><a class="ds-version" href="#v2">v2<span class="is-sr-only">, version 2</span></a> · <time datetime="2026-05-19">19&nbsp;May&nbsp;2026</time>&nbsp;UTC</p>
        <p>17 pages, 6 figures. Corrected Eq. (4.7).</p>
      </li>
      <li>…v1, as v2…</li>
    </ol>
  </div>
</details>
```

- `.ds-paper-versions` — An `<ol>` inside the Version history accordion, under Paper information in the sidebar (see [Papers](papers.md#the-sidebar)). Every version, newest first. Each entry is a `.ds-date-row` with the version, its date and its labels, then the comments the author wrote for that version.
- `aria-current="true"` — On the `<li>` being read. It draws the bar beside the entry and the box around its number in the accent. The number is a `<strong>`, not a link, and the visible label “Viewing” says the same in words.
- `.ds-version` — Every other version is a link to its abstract page, with a hidden “, version 2”, as in the version row.

**Viewing v1, latest is v3**

```html
<ol class="ds-paper-versions">
  <li>
    <p class="ds-date-row"><a class="ds-version" href="#v3">v3<span class="is-sr-only">, version 3</span></a> · <time datetime="2026-06-28">28&nbsp;Jun&nbsp;2026</time>&nbsp;UTC · Latest</p>
    <p>18 pages, 6 figures. …</p>
  </li>
  <li>…v2…</li>
  <li aria-current="true">
    <p class="ds-date-row"><strong class="ds-version">v1</strong> · <time datetime="2026-04-24">24&nbsp;Apr&nbsp;2026</time>&nbsp;UTC · Viewing</p>
    <p>16 pages, 5 figures.</p>
  </li>
</ol>
```

- `aria-current="true"` — Moves to the entry being read. “Latest” stays on the newest version, which stays a link.

**Viewing the withdrawal notice**

```html
<ol class="ds-paper-versions">
  <li class="ds-version--error" aria-current="true">
    <p class="ds-date-row"><strong class="ds-version ds-version--error">Withdrawal notice</strong> · <time datetime="2026-10-22">22&nbsp;Oct&nbsp;2026</time>&nbsp;UTC · Viewing</p>
    <p>Withdrawn by Adrian Palomares.</p>
  </li>
  <li>…v3, v2 and v1, as on any paper…</li>
</ol>
```

- `.ds-paper-versions` — Newest first, as on any paper, with the withdrawal notice first, in its place in the paper's history. Its line says who withdrew the paper. No entry says “Latest”: the notice is not a version.
- `.ds-version--error` — On the notice's `<li>` and its name. Being viewed, the notice takes a red box and a red bar, and says “Viewing” like any entry being read.

**Viewing the impacted version: version history panel**

```html
<ol class="ds-paper-versions">
  <li class="ds-version--error">
    <p class="ds-date-row"><a class="ds-version ds-version--error" href="…">Withdrawal notice</a> · <time datetime="2026-10-22">22&nbsp;Oct&nbsp;2026</time>&nbsp;UTC</p>
    <p>Withdrawn by Adrian Palomares.</p>
  </li>
  <li class="ds-version--error" aria-current="true">
    <p class="ds-date-row"><strong class="ds-version ds-version--error">v3</strong> · <time datetime="2026-06-28">28&nbsp;Jun&nbsp;2026</time>&nbsp;UTC · Viewing</p>
    <p>18 pages, 6 figures. …</p>
  </li>
  <li>…v2 and v1, as on any paper…</li>
</ol>
```

- `.ds-version--error` — On the notice's `<li>` and its link. When the withdrawn version is being viewed, also on its `<li>` and its number, which turns the bar beside the entry red.

**Viewing v2 of a withdrawn paper**

```html
<ol class="ds-paper-versions">
  <li class="ds-version--error">
    <p class="ds-date-row"><a class="ds-version ds-version--error" href="…">Withdrawal notice</a> · <time datetime="2026-10-22">22&nbsp;Oct&nbsp;2026</time>&nbsp;UTC</p>
    <p>Withdrawn by Adrian Palomares.</p>
  </li>
  <li>…v3, as on any paper…</li>
  <li aria-current="true">
    <p class="ds-date-row"><strong class="ds-version">v2</strong> · <time datetime="2026-05-19">19&nbsp;May&nbsp;2026</time>&nbsp;UTC · Viewing</p>
    <p>17 pages, 6 figures. Corrected Eq. (4.7).</p>
  </li>
  <li>…v1…</li>
</ol>
```

- `.ds-version--error` — Only on the notice's `<li>` and its link. v2 is not the withdrawn version, so its entry keeps the accent bar and box.

**Viewing v2, which arXiv removed**

```html
<ol class="ds-paper-versions">
  <li>…v3, as on any paper…</li>
  <li class="ds-version--error" aria-current="true">
    <p class="ds-date-row"><strong class="ds-version ds-version--error">v2</strong> · <time datetime="2026-05-19">19&nbsp;May&nbsp;2026</time>&nbsp;UTC · Viewing</p>
    <p>Removed by arXiv on <time datetime="2026-10-23">23&nbsp;Oct&nbsp;2026</time>&nbsp;UTC.</p>
    <p>17 pages, 6 figures. Corrected Eq. (4.7).</p>
  </li>
  <li>…v1…</li>
</ol>
```

- `.ds-version--error` — On the removed version's `<li>` and its number only while it is being viewed, which turns the bar beside the entry red. On any other version, the entry keeps its usual look and the line under the date says it was removed.
- `.ds-paper-versions > li > p` — The removal line comes first, then the author's comments for that version, which stay: a removal takes the full text, not the metadata.

> Follows [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf) §4.2: “Display related links and updates chronologically to tell the retracted publication’s story over time.”

## Rules

### Versions

- **Version links go to abstract pages.**
- **The dates and the older-version warning stay by the title.** The full history goes in the sidebar.
- **Each version shows its own comments**, as the author wrote them for that version.

### Withdrawn papers

Display guidelines for withdrawn and removed papers follow [NISO RP-45-2024](https://groups.niso.org/higherlogic/ws/public/download/30869/NISO_RP-45-2024_CREC.pdf). The status before the title, the notice and what leaves the page are in [Papers](papers.md#withdrawn-paper-rules).

- **We use the term “Withdrawal notice” in the version dates and Version history**, because that is a more accurate description of its role. The identity line still shows the version number.
- **Red marks a withdrawn or removed version only when it is being read.** Any earlier version being read keeps its usual look, and the link to the notice is always red.

### Formatting the three dates

**Submitted [v1 date] UTC · Announced [announcement date and time] UTC** are always shown, in that order, separated by a dot. Announced is when the paper first entered the public listing. Revision dates are when subsequent versions of the same paper went public. Dates use `<time datetime>`.

Announcement is the date that readers care about the most. It renders as **11 Jan 2026, 01:32 UTC**. Submitted and Revised stay date-only to save space.

When only the month of the announcement is known, as in a search index, show the month: **Announced Sep 2026**, with `datetime="2026-09"`.

arXiv's platform serves a global audience across all timezones. UTC was chosen as the universal standard to ensure consistency and clarity for all users. It is a group decision, made with arXiv staff.

Times are rendered in plain-text **UTC** bound to its date with `&nbsp;` so a wrap never separates them. The `<time>` element is not bound to the date.

Inside `datetime`, announced is a full instant (`2026-01-11T01:32Z`), Submitted and Revised stay date-only (`2026-01-10`).

The version being viewed is distinguished by a box, by weight and by `aria-current` and does not depend on color alone. It is deliberately not a link because the reader is already viewing it.

Prior versions are inline links alongside other text, so they are underlined. Each also has a hidden span that says which version it opens, so a screen reader reads "v1, version 1".

### Formatting the ellipsis and show all toggle

The ellipsis is decoration (`aria-hidden`) with an sr-only count of what is hidden; the working affordance is a text button showing the explicit total ("show all 127 versions"), toggling `aria-expanded`. The full list is server-rendered and collapsed by the script in `html.js`. Without JavaScript, the fallback is that readers see the full list of versions.

### Accessibility essentials

- **Mark the version being viewed.** Put `aria-current="true"` on it, make it a `<strong>` and not a link, and put `<span class="is-sr-only">, this version</span>` inside it. Bold alone is invisible to a screen reader, and the attribute alone is not read out by every one.
- **Say which version each link opens.** Every prior-version link has `<span class="is-sr-only">, version 2</span>` after its visible "v2". The visible "v2" does not say which version the link opens, and a screen reader user listing the links on the page hears each one out of context. Use the span, not an `aria-label`: the link's name has to start with the "v2" that a speech recognition user sees and says, and translation tools do not translate `aria-label`.
- **Put the warning where it is read early.** The older-version warning is part of the page as it loads, so it takes no role (see [Alerts](alerts.md)); it comes straight after the title and the dates. Render it only when the reader is not on the latest version; an alert that is always there is noise.
- **Separate the dates in words.** The visible "·" between dates is `aria-hidden="true"`, and a `<span class="is-sr-only">, </span>` sits beside it. Without the comma the three dates are read as one run-on sentence.
- **Say what the ellipsis hides.** The "…" is decoration and is `aria-hidden="true"`. The `.is-sr-only` span beside it says which versions are hidden, and the button says the total: "show all 12 versions". Use the `hidden` attribute on the hidden versions, never a class, so they are out of the tab order while they are off screen.
