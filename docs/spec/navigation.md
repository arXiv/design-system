---
page: navigation.html
title: "Navigation"
summary: "The bars under the [site header](header.md) that tell a reader where they are inside an area: secondary navigation, two levels of it, and steps."
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
  - id: two-levels-of-navigation
    title: "Two levels of navigation"
    summary: "An area with its own sections, each with several views, such as a report with parts and views. A section menu starts the row, and the views of the current section follow it as tabs. The row keeps to one line by folding: first the views fold into a View menu beside the section menu, then the section menu takes a row of its own."
    classes:
      - name: ".ds-subnav-section"
        does: "The section menu, a `<details>` at the start of the row: a cell in the accent's light tint, from the row's edge, with a hairline after it. Its summary names the current section; `aria-current=\"true\"` marks it in the menu."
      - name: ".ds-menu"
        does: "A dropdown's menu: square corners and rows with hairlines, 32px with a mouse and 44px on a touch screen, hanging from its control. A menu matches its control, so the section menu's is in the same tint and the View menu's is white."
      - name: "<a> for each view"
        does: "The row's own links, after the section menu, in the [tab style](#secondary-navigation). Each view is its own page."
      - name: "<script src=\"subnav.js\" defer>, .ds-subnav-views, .is-views-folded, .is-menu-row"
        does: "The script, once per page. It builds the View menu (`.ds-subnav-views`) from the row's links and sets the state classes on the row: `.is-views-folded` when the views do not fit beside the section menu, and `.is-menu-row` when the section menu takes a row of its own. It closes an open menu on Escape and on a click outside. Without the script the tabs wrap."
    notes:
      - "The script answers to the width of the row, so the narrower examples fold inside narrower boxes. Open the menus to see their colours."
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
        does: "On the link for the current step. It shows in bold, and its circle has a heavier border in the accent colour."
      - name: "<a> for an available step"
        does: "A link with its number."
      - name: "<span> for a step not available yet"
        does: "A `<span>`, not a link, so it is not a tab stop. A dashed circle and `.is-sr-only` text “, not available yet”."
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
  - "**A step not available yet is not a tab stop.** It is a `<span>`, and its `.is-sr-only` text says “, not available yet”."
---

# Navigation

The bars under the [site header](header.md) that tell a reader where they are inside an area: secondary navigation, two levels of it, and steps.

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
- `.ds-menu` — A dropdown's menu: square corners and rows with hairlines, 32px with a mouse and 44px on a touch screen, hanging from its control. A menu matches its control, so the section menu's is in the same tint and the View menu's is white.
- `<a> for each view` — The row's own links, after the section menu, in the [tab style](#secondary-navigation). Each view is its own page.
- `<script src="subnav.js" defer>, .ds-subnav-views, .is-views-folded, .is-menu-row` — The script, once per page. It builds the View menu (`.ds-subnav-views`) from the row's links and sets the state classes on the row: `.is-views-folded` when the views do not fit beside the section menu, and `.is-menu-row` when the section menu takes a row of its own. It closes an open menu on Escape and on a click outside. Without the script the tabs wrap.

> The script answers to the width of the row, so the narrower examples fold inside narrower boxes. Open the menus to see their colours.

## Steps

The steps of one ordered process, such as a submission, and which one the reader is on. Steps is a variant of the secondary navigation bar. To move through a queue one item at a time, use the [pager](pager.md). Which steps are available is the application's logic: submission, for example, lets the reader go back to a complete step but not jump ahead.

```html
<nav class="ds-subnav ds-subnav--steps" aria-label="Submission steps">
  <ol role="list">
    <li><a href="#"><span class="ds-step-number" aria-hidden="true"><svg …check…></span>Start<span class="is-sr-only">, completed</span></a></li>
    <li><a href="#" aria-current="step"><span class="ds-step-number" aria-hidden="true">5</span>Metadata</a></li>
    <li><a href="#"><span class="ds-step-number" aria-hidden="true">6</span>Categories</a></li>
    <li><span><span class="ds-step-number" aria-hidden="true">7</span>Preview<span class="is-sr-only">, not available yet</span></span></li>
  </ol>
</nav>
```

- `.ds-subnav--steps` — On the secondary navigation bar. It holds an `<ol role="list">`, one `<li>` per step. It wraps onto more lines on a narrow screen, so every step stays visible.
- `.ds-step-number` — The step number in a circle, hidden from screen readers because the list gives the position. A complete step shows a check mark instead of its number.
- `<a> for a complete step` — A link, with the check mark and `.is-sr-only` text “, completed”.
- `aria-current="step"` — On the link for the current step. It shows in bold, and its circle has a heavier border in the accent colour.
- `<a> for an available step` — A link with its number.
- `<span> for a step not available yet` — A `<span>`, not a link, so it is not a tab stop. A dashed circle and `.is-sr-only` text “, not available yet”.

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
      <li><a href="#"><span class="ds-step-number" aria-hidden="true"><svg …check…></span>Check<span class="is-sr-only">, completed</span></a></li>
      <li><a href="#" aria-current="step"><span class="ds-step-number" aria-hidden="true">2</span>Classify</a></li>
      <li><span><span class="ds-step-number" aria-hidden="true">3</span>Announce<span class="is-sr-only">, not available yet</span></span></li>
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
- **A step not available yet is not a tab stop.** It is a `<span>`, and its `.is-sr-only` text says “, not available yet”.
