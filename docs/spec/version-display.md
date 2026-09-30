---
page: version-display.html
title: "Versions"
summary: "How a paper shows its submission date, the timestamp it was announced at, its current revision date, and its version history. arXiv displays this info over and over again and in many different contexts. This page will help us stick to a consistent pattern for the benefit of readers and development."
stylesheet: design-system.css
components:
  - id: one-version-near-silent
    title: "One version"
    summary: "The most common case because most papers have a single version. We show the submitted and announced dates and nothing else."
    classes:
      - name: ".ds-date-row"
        does: "The row. One `<p>` that holds the dates and, after them, the version links. Small type in the muted colour, with tabular figures so the digits line up."
      - name: "<time datetime>"
        does: "Every date. Announced is a full instant (`2026-01-11T01:32Z`); Submitted and Revised are date-only (`2026-01-10`). In the visible text, bind the day, month, year and clock time to each other with `&nbsp;`, and bind UTC to its date the same way, outside the element."
      - name: ".is-sr-only"
        does: "The separator. The visible \"·\" is `aria-hidden`, and the sr-only comma beside it is what a screen reader gets between one date and the next."
    notes:
      - "The date row and version classes are not in design-system.css yet, so the demos here take the page defaults until they land."
  - id: a-few-versions-viewing-the-latest
    title: "A few versions"
    summary: "Once a paper has more than one version, the date row displays three dates: **Submitted** and **Announced** are always the v1 dates; **Revised … (this version)** is the date of the version you are reading. Prior versions follow as text links. The current version is displayed in bold, is not a link, and includes the `aria-current` tag."
    classes:
      - name: ".ds-version"
        does: "One version number in the row, in the mono face. A prior version is an `<a>` with an `href`, and takes the page's link colour and underline. The version being viewed is a `<strong>`, not a link."
      - name: "aria-current=\"true\""
        does: "On the version being viewed. Goes with the bold, so the current version is marked twice and never by colour alone. The `.is-sr-only` span inside it says \", this version\", because the attribute alone is not announced by every screen reader."
      - name: "aria-label=\"View version 1\""
        does: "On every prior-version link: \"View version 1\". The visible \"v1\" on its own does not say what the link does."
  - id: viewing-an-older-version
    title: "Viewing an older version"
    summary: "When the reader is on anything but the latest a things change."
    classes:
      - name: ".ds-alert.ds-alert--warning"
        does: "The older-version warning, documented on [Alerts](alerts.html): the warning state, the triangle icon copied whole, and `role=\"alert\"`. Render it only when the version being viewed is not the latest. One sentence that names the version being viewed, then a link straight to the latest one."
      - name: "aria-current=\"true\""
        does: "On v1 here, since v1 is the version being viewed. \"(this version)\" moves to the Submitted date for the same reason."
    rules:
      - "**You are viewing version 1.** A newer version is available — [version 3, revised 24 Apr 2026](#v3)."
  - id: many-versions-elide-the-middle
    title: "Many versions"
    summary: "Once a paper has ten or more versions we make some additional changes."
    classes:
      - name: ".ds-show-more"
        does: "The control that expands the list, documented on [Progressive disclosure](progressive-disclosure.html#show-more). Requires `aria-expanded`, flipped on every press, and `aria-controls` naming every region it shows or hides. The label includes the total: \"show all 12 versions\", and \"show fewer\" once open."
      - name: "[hidden]"
        does: "On the span that holds the elided versions. The attribute, not a class: the hidden links are out of the tab order while they are off screen. The full list is in the HTML the server sends; a script adds `hidden` and the button, so with no JavaScript the reader gets every version."
      - name: "aria-hidden=\"true\""
        does: "On the ellipsis, which is decoration. The `.is-sr-only` span beside it says which versions are hidden. Both sit in one span that the button hides when the list opens."
      - name: "aria-controls=\"v7-elide-a v7-tail-a v7-elide-b v7-tail-b\""
        does: "When the viewed version falls inside the elision there are two ellipses and two hidden spans. List all four ids, separated by spaces, so one press opens the whole list."
      - name: "[hidden]"
        does: "Absent. This is the row as the server sends it: every version in the list, no elision, no button. The row wraps like any other line of text."
    rules:
      - "**You are viewing version 7.** A newer version is available — [version 12, revised 30 Jun 2026](#v12)."
rules:
  - "**Submitted [v1 date] UTC · Announced [announcement date and time] UTC** are always shown, in that order, separated by a dot. Announced is when the paper first entered the public listing. Revision dates are when subsequent versions of the same paper went public. Dates use `<time datetime>`."
  - "Announcement is the date that readers care about the most. It renders as **11 Jan 2026, 01:32 UTC**. Submitted and Revised stay date-only to save space."
  - "arXiv's platform serves a global audience across all timezones. UTC was chosen as the universal standard to ensure consistency and clarity for all users. It is a group decision, made with arXiv staff."
  - "Times are rendered in plain-text **UTC** bound to its date with `&nbsp;` so a wrap never separates them. The `<time>` element is not bound to the date."
  - "Inside `datetime`, announced is a full instant (`2026-01-11T01:32Z`), Submitted and Revised stay date-only (`2026-01-10`)."
  - "The version being viewed is distinguished by weight and by `aria-current` and does not depend on color alone. It is deliberately not a link because the reader is already viewing it."
  - "Prior versions are inline links alongside other text, so they are underlined. Each is also tagged with an explicit `aria-label` (\"View version 1\")."
  - "The ellipsis is decoration (`aria-hidden`) with an sr-only count of what is hidden; the working affordance is a text button showing the explicit total (\"show all 127 versions\"), toggling `aria-expanded`. The full list is server-rendered and collapsed by the script in `html.js`. Without JavaScript, the fallback is that readers see the full list of versions."
  - "**Mark the version being viewed.** Put `aria-current=\"true\"` on it, make it a `<strong>` and not a link, and put `<span class=\"is-sr-only\">, this version</span>` inside it. Bold alone is invisible to a screen reader, and the attribute alone is not read out by every one."
  - "**Say which version each link opens.** Every prior-version link has `aria-label=\"View version 2\"`. The visible \"v2\" does not say what the link does, and a screen reader user listing the links on the page hears each one out of context."
  - "**Give the warning its role.** The older-version warning takes `role=\"alert\"`, so a screen reader announces it as soon as the page loads. Render it only when the reader is not on the latest version; an alert that is always there is noise."
  - "**Separate the dates in words.** The visible \"·\" between dates is `aria-hidden=\"true\"`, and a `<span class=\"is-sr-only\">, </span>` sits beside it. Without the comma the three dates are read as one run-on sentence."
  - "**Say what the ellipsis hides.** The \"…\" is decoration and is `aria-hidden=\"true\"`. The `.is-sr-only` span beside it says which versions are hidden, and the button says the total: \"show all 12 versions\". Use the `hidden` attribute on the hidden versions, never a class, so they are out of the tab order while they are off screen."
---

# Versions

How a paper shows its submission date, the timestamp it was announced at, its current revision date, and its version history. arXiv displays this info over and over again and in many different contexts. This page will help us stick to a consistent pattern for the benefit of readers and development.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## One version

The most common case because most papers have a single version. We show the submitted and announced dates and nothing else.

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10 Jan 2026</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11 Jan 2026, 01:32</time> UTC
</p>
```

- `.ds-date-row` — The row. One `<p>` that holds the dates and, after them, the version links. Small type in the muted colour, with tabular figures so the digits line up.
- `<time datetime>` — Every date. Announced is a full instant (`2026-01-11T01:32Z`); Submitted and Revised are date-only (`2026-01-10`). In the visible text, bind the day, month, year and clock time to each other with `&nbsp;`, and bind UTC to its date the same way, outside the element.
- `.is-sr-only` — The separator. The visible "·" is `aria-hidden`, and the sr-only comma beside it is what a screen reader gets between one date and the next.

> The date row and version classes are not in design-system.css yet, so the demos here take the page defaults until they land.

## A few versions

Once a paper has more than one version, the date row displays three dates: **Submitted** and **Announced** are always the v1 dates; **Revised … (this version)** is the date of the version you are reading. Prior versions follow as text links. The current version is displayed in bold, is not a link, and includes the `aria-current` tag.

**Viewing v3 of 3 (latest)**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10 Jan 2026</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11 Jan 2026, 01:32</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-04-24">24 Apr 2026</time> UTC (this version)
  <a class="ds-version" href="#v1" aria-label="View version 1">v1</a>
  <a class="ds-version" href="#v2" aria-label="View version 2">v2</a>
  <strong class="ds-version" aria-current="true">v3<span class="is-sr-only">, this version</span></strong>
</p>
```

- `.ds-version` — One version number in the row, in the mono face. A prior version is an `<a>` with an `href`, and takes the page's link colour and underline. The version being viewed is a `<strong>`, not a link.
- `aria-current="true"` — On the version being viewed. Goes with the bold, so the current version is marked twice and never by colour alone. The `.is-sr-only` span inside it says ", this version", because the attribute alone is not announced by every screen reader.
- `aria-label="View version 1"` — On every prior-version link: "View version 1". The visible "v1" on its own does not say what the link does.

## Viewing an older version

When the reader is on anything but the latest a things change.

**Viewing v1, latest is v3**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10 Jan 2026</time> UTC (this version)
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11 Jan 2026, 01:32</time> UTC
  <strong class="ds-version" aria-current="true">v1<span class="is-sr-only">, this version</span></strong>
  <a class="ds-version" href="#v2" aria-label="View version 2">v2</a>
  <a class="ds-version" href="#v3" aria-label="View version 3">v3</a>
</p>
<div class="ds-alert ds-alert--warning" role="alert">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
    <path d="M12 9v4"/>
    <path d="M12 17h.01"/>
  </svg>
  <div class="ds-alert-content">
    <p><strong>You are viewing version 1.</strong> A newer version is available — <a href="#v3">version 3, revised 24 Apr 2026</a>.</p>
  </div>
</div>
```

- `.ds-alert.ds-alert--warning` — The older-version warning, documented on [Alerts](alerts.html): the warning state, the triangle icon copied whole, and `role="alert"`. Render it only when the version being viewed is not the latest. One sentence that names the version being viewed, then a link straight to the latest one.
- `aria-current="true"` — On v1 here, since v1 is the version being viewed. "(this version)" moves to the Submitted date for the same reason.

**Rule.** **You are viewing version 1.** A newer version is available — [version 3, revised 24 Apr 2026](#v3).

## Many versions

Once a paper has ten or more versions we make some additional changes.

**Viewing v12 of 12 (latest), collapsed**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10 Jan 2026</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11 Jan 2026, 01:32</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-06-30">30 Jun 2026</time> UTC (this version)
  <a class="ds-version" href="#v1" aria-label="View version 1">v1</a>
  <a class="ds-version" href="#v2" aria-label="View version 2">v2</a>
  <a class="ds-version" href="#v3" aria-label="View version 3">v3</a>
  <span id="v12-elide"><span aria-hidden="true">…</span><span class="is-sr-only">versions 4 through 9 hidden,</span></span>
  <span id="v12-tail" hidden>
    <a class="ds-version" href="#v4" aria-label="View version 4">v4</a>
    <a class="ds-version" href="#v5" aria-label="View version 5">v5</a>
    <a class="ds-version" href="#v6" aria-label="View version 6">v6</a>
    <a class="ds-version" href="#v7" aria-label="View version 7">v7</a>
    <a class="ds-version" href="#v8" aria-label="View version 8">v8</a>
    <a class="ds-version" href="#v9" aria-label="View version 9">v9</a>
  </span>
  <a class="ds-version" href="#v10" aria-label="View version 10">v10</a>
  <a class="ds-version" href="#v11" aria-label="View version 11">v11</a>
  <strong class="ds-version" aria-current="true">v12<span class="is-sr-only">, this version</span></strong>
  <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false" aria-controls="v12-elide v12-tail">show all 12 versions</button>
</p>
```

**Viewing v7 of 12: the viewed version stays visible inside the elision**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10 Jan 2026</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11 Jan 2026, 01:32</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-03-12">12 Mar 2026</time> UTC (this version)
  <a class="ds-version" href="#v1" aria-label="View version 1">v1</a>
  <a class="ds-version" href="#v2" aria-label="View version 2">v2</a>
  <a class="ds-version" href="#v3" aria-label="View version 3">v3</a>
  <span id="v7-elide-a"><span aria-hidden="true">…</span><span class="is-sr-only">versions 4 through 6 hidden,</span></span>
  <span id="v7-tail-a" hidden>
    <a class="ds-version" href="#v4" aria-label="View version 4">v4</a>
    <a class="ds-version" href="#v5" aria-label="View version 5">v5</a>
    <a class="ds-version" href="#v6" aria-label="View version 6">v6</a>
  </span>
  <strong class="ds-version" aria-current="true">v7<span class="is-sr-only">, this version</span></strong>
  <span id="v7-elide-b"><span aria-hidden="true">…</span><span class="is-sr-only">versions 8 through 9 hidden,</span></span>
  <span id="v7-tail-b" hidden>
    <a class="ds-version" href="#v8" aria-label="View version 8">v8</a>
    <a class="ds-version" href="#v9" aria-label="View version 9">v9</a>
  </span>
  <a class="ds-version" href="#v10" aria-label="View version 10">v10</a>
  <a class="ds-version" href="#v11" aria-label="View version 11">v11</a>
  <a class="ds-version" href="#v12" aria-label="View version 12">v12</a>
  <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false" aria-controls="v7-elide-a v7-tail-a v7-elide-b v7-tail-b">show all 12 versions</button>
</p>
<div class="ds-alert ds-alert--warning" role="alert">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
    <path d="M12 9v4"/>
    <path d="M12 17h.01"/>
  </svg>
  <div class="ds-alert-content">
    <p><strong>You are viewing version 7.</strong> A newer version is available — <a href="#v12">version 12, revised 30 Jun 2026</a>.</p>
  </div>
</div>
```

**Expanded, show all 24 versions**

```html
<p class="ds-date-row">
  Submitted <time datetime="2026-01-10">10 Jan 2026</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Announced <time datetime="2026-01-11T01:32Z">11 Jan 2026, 01:32</time> UTC
  <span aria-hidden="true"> · </span><span class="is-sr-only">, </span>
  Revised <time datetime="2026-06-30">30 Jun 2026</time> UTC (this version)
  <a class="ds-version" href="#v1" aria-label="View version 1">v1</a>
  <a class="ds-version" href="#v2" aria-label="View version 2">v2</a>
  <a class="ds-version" href="#v3" aria-label="View version 3">v3</a>
  <span id="v24-elide" hidden><span aria-hidden="true">…</span><span class="is-sr-only">versions 4 through 21 hidden,</span></span>
  <span id="v24-tail">
    <a class="ds-version" href="#v4" aria-label="View version 4">v4</a>
    <a class="ds-version" href="#v5" aria-label="View version 5">v5</a>
    <a class="ds-version" href="#v6" aria-label="View version 6">v6</a>
    <a class="ds-version" href="#v7" aria-label="View version 7">v7</a>
    <a class="ds-version" href="#v8" aria-label="View version 8">v8</a>
    <a class="ds-version" href="#v9" aria-label="View version 9">v9</a>
    <a class="ds-version" href="#v10" aria-label="View version 10">v10</a>
    <a class="ds-version" href="#v11" aria-label="View version 11">v11</a>
    <a class="ds-version" href="#v12" aria-label="View version 12">v12</a>
    <a class="ds-version" href="#v13" aria-label="View version 13">v13</a>
    <a class="ds-version" href="#v14" aria-label="View version 14">v14</a>
    <a class="ds-version" href="#v15" aria-label="View version 15">v15</a>
    <a class="ds-version" href="#v16" aria-label="View version 16">v16</a>
    <a class="ds-version" href="#v17" aria-label="View version 17">v17</a>
    <a class="ds-version" href="#v18" aria-label="View version 18">v18</a>
    <a class="ds-version" href="#v19" aria-label="View version 19">v19</a>
    <a class="ds-version" href="#v20" aria-label="View version 20">v20</a>
    <a class="ds-version" href="#v21" aria-label="View version 21">v21</a>
  </span>
  <a class="ds-version" href="#v22" aria-label="View version 22">v22</a>
  <a class="ds-version" href="#v23" aria-label="View version 23">v23</a>
  <strong class="ds-version" aria-current="true">v24<span class="is-sr-only">, this version</span></strong>
  <button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="true" aria-controls="v24-elide v24-tail" data-closed-label="show all 24 versions">show fewer</button>
</p>
```

- `.ds-show-more` — The control that expands the list, documented on [Progressive disclosure](progressive-disclosure.html#show-more). Requires `aria-expanded`, flipped on every press, and `aria-controls` naming every region it shows or hides. The label includes the total: "show all 12 versions", and "show fewer" once open.
- `[hidden]` — On the span that holds the elided versions. The attribute, not a class: the hidden links are out of the tab order while they are off screen. The full list is in the HTML the server sends; a script adds `hidden` and the button, so with no JavaScript the reader gets every version.
- `aria-hidden="true"` — On the ellipsis, which is decoration. The `.is-sr-only` span beside it says which versions are hidden. Both sit in one span that the button hides when the list opens.
- `aria-controls="v7-elide-a v7-tail-a v7-elide-b v7-tail-b"` — When the viewed version falls inside the elision there are two ellipses and two hidden spans. List all four ids, separated by spaces, so one press opens the whole list.
- `[hidden]` — Absent. This is the row as the server sends it: every version in the list, no elision, no button. The row wraps like any other line of text.

**Rule.** **You are viewing version 7.** A newer version is available — [version 12, revised 30 Jun 2026](#v12).

## Rules

- **Submitted [v1 date] UTC · Announced [announcement date and time] UTC** are always shown, in that order, separated by a dot. Announced is when the paper first entered the public listing. Revision dates are when subsequent versions of the same paper went public. Dates use `<time datetime>`.
- Announcement is the date that readers care about the most. It renders as **11 Jan 2026, 01:32 UTC**. Submitted and Revised stay date-only to save space.
- arXiv's platform serves a global audience across all timezones. UTC was chosen as the universal standard to ensure consistency and clarity for all users. It is a group decision, made with arXiv staff.
- Times are rendered in plain-text **UTC** bound to its date with `&nbsp;` so a wrap never separates them. The `<time>` element is not bound to the date.
- Inside `datetime`, announced is a full instant (`2026-01-11T01:32Z`), Submitted and Revised stay date-only (`2026-01-10`).
- The version being viewed is distinguished by weight and by `aria-current` and does not depend on color alone. It is deliberately not a link because the reader is already viewing it.
- Prior versions are inline links alongside other text, so they are underlined. Each is also tagged with an explicit `aria-label` ("View version 1").
- The ellipsis is decoration (`aria-hidden`) with an sr-only count of what is hidden; the working affordance is a text button showing the explicit total ("show all 127 versions"), toggling `aria-expanded`. The full list is server-rendered and collapsed by the script in `html.js`. Without JavaScript, the fallback is that readers see the full list of versions.
- **Mark the version being viewed.** Put `aria-current="true"` on it, make it a `<strong>` and not a link, and put `<span class="is-sr-only">, this version</span>` inside it. Bold alone is invisible to a screen reader, and the attribute alone is not read out by every one.
- **Say which version each link opens.** Every prior-version link has `aria-label="View version 2"`. The visible "v2" does not say what the link does, and a screen reader user listing the links on the page hears each one out of context.
- **Give the warning its role.** The older-version warning takes `role="alert"`, so a screen reader announces it as soon as the page loads. Render it only when the reader is not on the latest version; an alert that is always there is noise.
- **Separate the dates in words.** The visible "·" between dates is `aria-hidden="true"`, and a `<span class="is-sr-only">, </span>` sits beside it. Without the comma the three dates are read as one run-on sentence.
- **Say what the ellipsis hides.** The "…" is decoration and is `aria-hidden="true"`. The `.is-sr-only` span beside it says which versions are hidden, and the button says the total: "show all 12 versions". Use the `hidden` attribute on the hidden versions, never a class, so they are out of the tab order while they are off screen.
