---
page: navigation.html
title: "Navigation"
summary: "The bars under the [site header](header.md) that tell a reader where they are inside an area or on a page: secondary navigation, two levels of it, steps, and the TOC bar."
stylesheet: design-system.css
components:
  - id: secondary-navigation
    title: "Secondary navigation"
    summary: "A row of section links directly under the header, for an area that has its own sections, such as the account pages. It wraps onto a second line rather than scrolling sideways, so every section stays visible on a phone and at high zoom. Its links are tabs, in the same style as [tabs](progressive-disclosure.md#tabs) within a page: the current one is a box joined to what follows it, with the accent along its top."
    classes:
      - name: ".ds-subnav"
        does: "A `<nav>` directly after the header, with an `aria-label` that names the area, such as “Account sections”. Plain links; never `role=\"tab\"`, which would promise arrow-key behaviour that page links do not have. Hidden in print."
      - name: "aria-current=\"page\""
        does: "On the link for the current page. It shows as a bold tab joined to the page below, with the accent along its top, so the current section never depends on colour alone, and a screen reader announces it. The current tab takes the background of the zone below it: the page ground (white in light mode) above primary content, or the secondary zone's tint (light grey in light mode) when the page opens with a [secondary band](layout-patterns.md#page-zones)."
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)"
  - id: two-levels-of-navigation
    title: "Two levels of navigation"
    summary: "An area with its own sections, each with several views, such as a report with parts and views. A section menu starts the row, and the views of the current section follow it as tabs. The row keeps to one line by folding: first the views fold into a View menu beside the section menu, then the section menu takes a row of its own."
    classes:
      - name: ".ds-subnav-section"
        does: "The section menu, a `<details>` at the start of the row: a cell in the accent's light tint, from the row's edge, with a hairline after it. Its summary names the current section; `aria-current=\"true\"` marks it in the menu."
      - name: ".ds-menu"
        does: "A dropdown's menu: square corners and rows with hairlines, 32px with a mouse and 44px on a touch screen, hanging from its control. A menu opens in the background of the row it comes from. The tinted section cell counts as a row of its own, so its menu is tinted; the View menu, from the white row, is white."
      - name: "<a> for each view"
        does: "The row's own links, after the section menu, in the [tab style](#secondary-navigation). Each view is its own page."
      - name: "<script src=\"subnav.js\" defer>, .ds-subnav-views, .is-views-folded, .is-menu-row"
        does: "The script, once per page. It builds the View menu (`.ds-subnav-views`) from the row's links and sets the state classes on the row: `.is-views-folded` when the views do not fit beside the section menu, and `.is-menu-row` when the section menu takes a row of its own. It closes an open menu on Escape and on a click outside. Without the script the tabs wrap."
    notes:
      - "The script answers to the width of the row, so the narrower examples fold inside narrower boxes. Open the menus to see their colours."
    rules:
      - "**Two levels at most.** A third level is a sign the content needs restructuring."
      - "**Each row keeps the same links on every page it appears on.** Only the current link changes."
      - "**Choices that apply to one view go inside that view**, below the row."
      - "**When the views share one address** and swap in place, use [tabs](progressive-disclosure.md#tabs) for the second level instead."
  - id: steps
    title: "Steps"
    summary: "The steps of one ordered process, such as a submission, and which one the reader is on. Steps is a variant of the secondary navigation bar. To move through a queue one item at a time, use the [pager](pager.md). Which steps are available is the application's logic: submission, for example, lets the reader go back to a complete step but not jump ahead."
    classes:
      - name: ".ds-subnav--steps"
        does: "On the secondary navigation bar. It holds an `<ol role=\"list\">`, one `<li>` per step. It wraps onto more lines on a narrow screen, so every step stays visible."
      - name: ".ds-step-number"
        does: "The step number in a circle, hidden from screen readers because the list gives the position. A complete step shows a check mark instead of its number."
      - name: "<a> for a complete step"
        does: "A link, with the check mark and `.is-sr-only` text “, completed”."
      - name: "aria-current=\"step\""
        does: "On the link for the current step. Its name is bold, and its circle has a heavier border in the accent colour."
      - name: ".ds-step-label"
        does: "The step's name, with the same name in `data-label`. Every step keeps the width of its name in bold, so the row does not move when the current step changes."
      - name: "<a> for an available step"
        does: "A link with its number."
      - name: "<span> for a step not available yet"
        does: "A `<span>`, not a link, so it is not a tab stop. A dashed circle and `.is-sr-only` text “, not available yet”."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 1.3.1](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) Info and Relationships (Level A) and [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)"
    rules:
      - "**One bar under the header.** A page shows either secondary navigation or steps, never both."
  - id: toc-bar
    title: "TOC bar"
    summary: "Need in-page navigation? The TOC bar is a row that holds a single disclosure control, which opens a list of the page’s sections. The bar is sticky and it stays at the top of the viewport while the reader scrolls through the page."
    classes:
      - name: ".ds-toc"
        does: "The control, a `<details>`. It works on its own anywhere, and it opens with JavaScript off."
      - name: ".ds-toc-trigger"
        does: "The `<summary>`. Holds the list icon, `.ds-toc-text` with its `.ds-toc-prefix`, and `.ds-toc-chevron`."
      - name: ".ds-toc-menu"
        does: "The list, a `<nav>` holding an `<ol>`. The link to the current section gets `.is-current`. A page whose sections are numbered puts each number in `.ds-toc-num`."
      - name: ".ds-toc-bar"
        does: "The edge-to-edge row that holds the control. A direct child of `.ds-container`, with `.ds-full`. Placed directly after a `.ds-zone-secondary` band, it sits on that band’s bottom edge. The bar is sticky: it keeps to the top of the viewport, where it becomes `.is-stuck` and tightens, and it sets `scroll-padding-top` so an anchor lands below it. On a viewport shorter than 30rem, such as a phone on its side or a laptop at 400% zoom, it scrolls away with the page instead, so the reader keeps the height for the text. Sticky chrome is governed by [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md); check there before adding the bar to a page."
      - name: ".ds-toc-bar-inner"
        does: "The bar’s three-slot grid, which keeps the control centred whatever sits beside it."
      - name: "[data-toc-scope]"
        does: "Optional, on `.ds-toc`: a selector for the element whose headings fill an empty list. Without it, `toc.js` reads `<main>`, or the whole page when there is no `<main>`."
    rules:
      - "**The list is written or generated.** Write the `<ol>` by hand, or leave it empty and `toc.js` fills it when the page loads, with one link for every `h2` and `h3` that has an `id`. A written list works with JavaScript off, so these docs write theirs: `verification/gen-anchors.py` fills the `<ol>` from the page’s section headings, and `--check` fails when the two disagree."
      - "**It opens without JavaScript.** `toc.js` adds closing on Escape, closing on a click outside, and the name of the current section on the control."
      - "**One per page.** `toc.js` drives the first `.ds-toc` it finds, which on this page is the bar at the top; the control in the card above comes later in the document, so it opens and closes on its own and nothing else."
      - "**The contents list repeats the page's headings exactly**, in the same words and the same order. On a paper, the list is the author's headings; see [Papers](papers.md#paper-toc-bar-rules)."
  - id: internal
    title: "Internal"
    group: "Modifiers"
    summary: "The secondary navigation and steps in an internal tool. `.ds-internal` on a parent turns the current tab’s top line and the current step’s circle Access Lime, and the section menu’s background and lines the Access Lime washes."
    classes:
      - name: ".ds-internal"
        does: "On a parent, it turns the current tab's top line Access Lime. Nothing else changes; see [Secondary navigation](#secondary-navigation)."
      - name: ".ds-internal"
        does: "On a parent, it turns the section menu's background, its hover and open state and its edge line to the Access Lime washes, and the current view's top line and the current row's bar in the open menu Access Lime. The markup and the folding are the same as in [Two levels of navigation](#two-levels-of-navigation)."
      - name: ".ds-internal"
        does: "On a parent, it turns the current step’s circle Access Lime."
rules:
  - "**Name each bar.** The `<nav>` takes an `aria-label` that names the area, such as “Account sections” or “Submission steps”, so a screen reader can tell it from the header's navigation."
  - "**Mark the current page or step with `aria-current`.** The tab's shape and weight show it too, so the current section never depends on colour alone."
  - "**Links, not tabs.** Each view is its own page, so the row holds plain links and never `role=\"tab\"`, which would promise arrow-key behaviour that page links do not have."
  - "**The menus close from the keyboard.** The section menu and the View menu are `<details>`, so they open and close with no script; `subnav.js` also closes an open menu on Escape and returns focus to its summary."
  - "**The TOC bar's list is a disclosure, not an ARIA menu.** `role=\"menu\"` is for application menus — the kind with arrow-key roving focus and menu items that are not links. A list of links is a disclosure, and W3C’s own guidance is to build it this way. Using `role=\"menu\"` here would make a screen reader promise keyboard behaviour the component does not have."
  - "**Mark where the reader is in the TOC bar.** `toc.js` gives the link to the current section `aria-current=\"location\"`."
  - "**Escape closes the TOC bar's list** and returns focus to its control, but only when focus was inside the list — Escape pressed elsewhere on the page must not move it."
  - "**A step not available yet is not a tab stop.** It is a `<span>`, and its `.is-sr-only` text says “, not available yet”."
---

# Navigation

The bars under the [site header](header.md) that tell a reader where they are inside an area or on a page: secondary navigation, two levels of it, steps, and the TOC bar.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Secondary navigation

A row of section links directly under the header, for an area that has its own sections, such as the account pages. It wraps onto a second line rather than scrolling sideways, so every section stays visible on a phone and at high zoom. Its links are tabs, in the same style as [tabs](progressive-disclosure.md#tabs) within a page: the current one is a box joined to what follows it, with the accent along its top.

```html
<header class="ds-site-header">…</header>
<nav class="ds-subnav" aria-label="Account sections">
  <a href="/account">Account home</a>
  <a href="/account/submissions">Submissions</a>
  <a href="/account/works" aria-current="page">Works you own</a>
  <a href="/account/endorse">Endorse</a>
</nav>
```

- `.ds-subnav` — A `<nav>` directly after the header, with an `aria-label` that names the area, such as “Account sections”. Plain links; never `role="tab"`, which would promise arrow-key behaviour that page links do not have. Hidden in print.
- `aria-current="page"` — On the link for the current page. It shows as a bold tab joined to the page below, with the accent along its top, so the current section never depends on colour alone, and a screen reader announces it. The current tab takes the background of the zone below it: the page ground (white in light mode) above primary content, or the secondary zone's tint (light grey in light mode) when the page opens with a [secondary band](layout-patterns.md#page-zones).

> Meets accessibility guideline [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)

## Two levels of navigation

An area with its own sections, each with several views, such as a report with parts and views. A section menu starts the row, and the views of the current section follow it as tabs. The row keeps to one line by folding: first the views fold into a View menu beside the section menu, then the section menu takes a row of its own.

```html
<nav class="ds-subnav" aria-label="Moderator reports">
  <details class="ds-subnav-section">
    <summary>Submissions and holds</summary>
    <div class="ds-menu">
      <a href="/submissions" aria-current="true">Submissions and holds</a>
      <a href="/moderators">Moderators</a>
      <a href="/recruitment">Recruitment</a>
    </div>
  </details>
  <a href="/submissions">Overview</a>
  <a href="/submissions/charts" aria-current="page">Activity charts</a>
  <!-- … -->
</nav>
<script src="subnav.js" defer></script>
```

- `.ds-subnav-section` — The section menu, a `<details>` at the start of the row: a cell in the accent's light tint, from the row's edge, with a hairline after it. Its summary names the current section; `aria-current="true"` marks it in the menu.
- `.ds-menu` — A dropdown's menu: square corners and rows with hairlines, 32px with a mouse and 44px on a touch screen, hanging from its control. A menu opens in the background of the row it comes from. The tinted section cell counts as a row of its own, so its menu is tinted; the View menu, from the white row, is white.
- `<a> for each view` — The row's own links, after the section menu, in the [tab style](#secondary-navigation). Each view is its own page.
- `<script src="subnav.js" defer>, .ds-subnav-views, .is-views-folded, .is-menu-row` — The script, once per page. It builds the View menu (`.ds-subnav-views`) from the row's links and sets the state classes on the row: `.is-views-folded` when the views do not fit beside the section menu, and `.is-menu-row` when the section menu takes a row of its own. It closes an open menu on Escape and on a click outside. Without the script the tabs wrap.

> The script answers to the width of the row, so the narrower examples fold inside narrower boxes. Open the menus to see their colours.

**Rule.** **Two levels at most.** A third level is a sign the content needs restructuring.

**Rule.** **Each row keeps the same links on every page it appears on.** Only the current link changes.

**Rule.** **Choices that apply to one view go inside that view**, below the row.

**Rule.** **When the views share one address** and swap in place, use [tabs](progressive-disclosure.md#tabs) for the second level instead.

## Steps

The steps of one ordered process, such as a submission, and which one the reader is on. Steps is a variant of the secondary navigation bar. To move through a queue one item at a time, use the [pager](pager.md). Which steps are available is the application's logic: submission, for example, lets the reader go back to a complete step but not jump ahead.

```html
<nav class="ds-subnav ds-subnav--steps" aria-label="Submission steps">
  <ol role="list">
    <li><a href="#"><span class="ds-step-number" aria-hidden="true"><svg …check…></span><span class="ds-step-label" data-label="Start">Start</span><span class="is-sr-only">, completed</span></a></li>
    <li><a href="#" aria-current="step"><span class="ds-step-number" aria-hidden="true">5</span><span class="ds-step-label" data-label="Metadata">Metadata</span></a></li>
    <li><a href="#"><span class="ds-step-number" aria-hidden="true">6</span><span class="ds-step-label" data-label="Categories">Categories</span></a></li>
    <li><span><span class="ds-step-number" aria-hidden="true">7</span><span class="ds-step-label" data-label="Preview">Preview</span><span class="is-sr-only">, not available yet</span></span></li>
  </ol>
</nav>
```

- `.ds-subnav--steps` — On the secondary navigation bar. It holds an `<ol role="list">`, one `<li>` per step. It wraps onto more lines on a narrow screen, so every step stays visible.
- `.ds-step-number` — The step number in a circle, hidden from screen readers because the list gives the position. A complete step shows a check mark instead of its number.
- `<a> for a complete step` — A link, with the check mark and `.is-sr-only` text “, completed”.
- `aria-current="step"` — On the link for the current step. Its name is bold, and its circle has a heavier border in the accent colour.
- `.ds-step-label` — The step's name, with the same name in `data-label`. Every step keeps the width of its name in bold, so the row does not move when the current step changes.
- `<a> for an available step` — A link with its number.
- `<span> for a step not available yet` — A `<span>`, not a link, so it is not a tab stop. A dashed circle and `.is-sr-only` text “, not available yet”.

> Meets accessibility guidelines [WCAG 2.2 SC 1.3.1](https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html) Info and Relationships (Level A) and [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)

**Rule.** **One bar under the header.** A page shows either secondary navigation or steps, never both.

## TOC bar

Need in-page navigation? The TOC bar is a row that holds a single disclosure control, which opens a list of the page’s sections. The bar is sticky and it stays at the top of the viewport while the reader scrolls through the page.

```html
<div class="ds-container">
  <div class="ds-full ds-zone-secondary">
    <header class="ds-page-header">…</header>
  </div>

  <div class="ds-full ds-toc-bar">
    <div class="ds-toc-bar-inner">
      <details class="ds-toc">
        <summary class="ds-toc-trigger">
          <svg aria-hidden="true">…</svg>
          <span class="ds-toc-text"><span class="ds-toc-prefix">Contents</span></span>
          <svg class="ds-toc-chevron" aria-hidden="true">…</svg>
        </summary>
        <nav class="ds-toc-menu" aria-label="Contents">
          <ol></ol>      <!-- written by hand, or left empty for toc.js to fill -->
        </nav>
      </details>
    </div>
  </div>

  <section>…</section>
</div>
<script src="toc.js" defer></script>
```

- `.ds-toc` — The control, a `<details>`. It works on its own anywhere, and it opens with JavaScript off.
- `.ds-toc-trigger` — The `<summary>`. Holds the list icon, `.ds-toc-text` with its `.ds-toc-prefix`, and `.ds-toc-chevron`.
- `.ds-toc-menu` — The list, a `<nav>` holding an `<ol>`. The link to the current section gets `.is-current`. A page whose sections are numbered puts each number in `.ds-toc-num`.
- `.ds-toc-bar` — The edge-to-edge row that holds the control. A direct child of `.ds-container`, with `.ds-full`. Placed directly after a `.ds-zone-secondary` band, it sits on that band’s bottom edge. The bar is sticky: it keeps to the top of the viewport, where it becomes `.is-stuck` and tightens, and it sets `scroll-padding-top` so an anchor lands below it. On a viewport shorter than 30rem, such as a phone on its side or a laptop at 400% zoom, it scrolls away with the page instead, so the reader keeps the height for the text. Sticky chrome is governed by [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md); check there before adding the bar to a page.
- `.ds-toc-bar-inner` — The bar’s three-slot grid, which keeps the control centred whatever sits beside it.
- `[data-toc-scope]` — Optional, on `.ds-toc`: a selector for the element whose headings fill an empty list. Without it, `toc.js` reads `<main>`, or the whole page when there is no `<main>`.

**Rule.** **The list is written or generated.** Write the `<ol>` by hand, or leave it empty and `toc.js` fills it when the page loads, with one link for every `h2` and `h3` that has an `id`. A written list works with JavaScript off, so these docs write theirs: `verification/gen-anchors.py` fills the `<ol>` from the page’s section headings, and `--check` fails when the two disagree.

**Rule.** **It opens without JavaScript.** `toc.js` adds closing on Escape, closing on a click outside, and the name of the current section on the control.

**Rule.** **One per page.** `toc.js` drives the first `.ds-toc` it finds, which on this page is the bar at the top; the control in the card above comes later in the document, so it opens and closes on its own and nothing else.

**Rule.** **The contents list repeats the page's headings exactly**, in the same words and the same order. On a paper, the list is the author's headings; see [Papers](papers.md#paper-toc-bar-rules).

## Internal  (Modifiers)

The secondary navigation and steps in an internal tool. `.ds-internal` on a parent turns the current tab’s top line and the current step’s circle Access Lime, and the section menu’s background and lines the Access Lime washes.

```html
<div class="ds-internal">
  <header class="ds-site-header">…</header>
  <nav class="ds-subnav" aria-label="Admin Console sections">
    <a href="/admin" aria-current="page">Dashboard</a>
    <a href="/admin/users">Users</a>
    <a href="/admin/moderators">Moderators</a>
  </nav>
</div>
```

```html
<div class="ds-internal">
  <nav class="ds-subnav" aria-label="Moderator reports">
    <details class="ds-subnav-section">
      <summary>Submissions and holds</summary>
      <div class="ds-menu">
        <a href="…" aria-current="true">Submissions and holds</a>
        <a href="…">Moderators</a>
        <a href="…">Recruitment</a>
      </div>
    </details>
    <a href="…">Overview</a>
    <a href="…" aria-current="page">Activity charts</a>
    <a href="…">Recent holds</a>
  </nav>
</div>
<script src="subnav.js" defer></script>
```

```html
<div class="ds-internal">
  <nav class="ds-subnav ds-subnav--steps" aria-label="Review steps">
    <ol role="list">
      <li><a href="#"><span class="ds-step-number" aria-hidden="true"><svg …check…></span><span class="ds-step-label" data-label="Check">Check</span><span class="is-sr-only">, completed</span></a></li>
      <li><a href="#" aria-current="step"><span class="ds-step-number" aria-hidden="true">2</span><span class="ds-step-label" data-label="Classify">Classify</span></a></li>
      <li><span><span class="ds-step-number" aria-hidden="true">3</span><span class="ds-step-label" data-label="Announce">Announce</span><span class="is-sr-only">, not available yet</span></span></li>
    </ol>
  </nav>
</div>
```

- `.ds-internal` — On a parent, it turns the current tab's top line Access Lime. Nothing else changes; see [Secondary navigation](#secondary-navigation).
- `.ds-internal` — On a parent, it turns the section menu's background, its hover and open state and its edge line to the Access Lime washes, and the current view's top line and the current row's bar in the open menu Access Lime. The markup and the folding are the same as in [Two levels of navigation](#two-levels-of-navigation).
- `.ds-internal` — On a parent, it turns the current step’s circle Access Lime.

## Rules

- **Name each bar.** The `<nav>` takes an `aria-label` that names the area, such as “Account sections” or “Submission steps”, so a screen reader can tell it from the header's navigation.
- **Mark the current page or step with `aria-current`.** The tab's shape and weight show it too, so the current section never depends on colour alone.
- **Links, not tabs.** Each view is its own page, so the row holds plain links and never `role="tab"`, which would promise arrow-key behaviour that page links do not have.
- **The menus close from the keyboard.** The section menu and the View menu are `<details>`, so they open and close with no script; `subnav.js` also closes an open menu on Escape and returns focus to its summary.
- **The TOC bar's list is a disclosure, not an ARIA menu.** `role="menu"` is for application menus — the kind with arrow-key roving focus and menu items that are not links. A list of links is a disclosure, and W3C’s own guidance is to build it this way. Using `role="menu"` here would make a screen reader promise keyboard behaviour the component does not have.
- **Mark where the reader is in the TOC bar.** `toc.js` gives the link to the current section `aria-current="location"`.
- **Escape closes the TOC bar's list** and returns focus to its control, but only when focus was inside the list — Escape pressed elsewhere on the page must not move it.
- **A step not available yet is not a tab stop.** It is a `<span>`, and its `.is-sr-only` text says “, not available yet”.
