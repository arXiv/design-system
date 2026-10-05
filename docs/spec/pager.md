---
page: pager.html
title: "Pager"
summary: "Controls for moving through a list: one item at a time with the pager, or a group of items at a time with numbered pages."
stylesheet: design-system.css
components:
  - id: the-pager
    title: "The pager"
    summary: "This component group is for moving through items one at a time, such as a moderation queue or a run of submissions, where each item has its own screen and someone works through them in order. Our current usage is in the Admin Console but it is available in other contexts."
    classes:
      - name: ".ds-pagination"
        does: "A `<nav>` with an `aria-label` saying which set it steps through. Holds the position, Previous and Next, in that order."
      - name: ".ds-pagination-position"
        does: "The counter. Takes `aria-live=\"polite\"`: without it a reader who cannot see the counter has no way to know that the Next they just pressed did anything. The wording is the host's to choose; the counter takes the slack before the buttons, so the buttons stay put as the number grows."
      - name: ".ds-btn.ds-btn-text"
        does: "The two buttons, text-only, so they read as navigation rather than as actions. At either end of the set the button is `disabled`, not removed: a control that vanishes changes the shape of the toolbar under the reader, and a disabled one says “there is nothing before this”, which is the actual information."
      - name: ".ds-pagination"
        does: "Steps through the requests. It sits above everything that belongs to the current request, so the table and its actions change together when the reader moves on."
      - name: ".ds-btn-group, .ds-bulk-count, .ds-filter"
        does: "The group actions row: the actions, the selection count, and a filter at the far end. See [Bulk actions](tables.html#bulk-actions)."
      - name: ".ds-table, .is-selected"
        does: "The papers in the current request, with a checkbox per row. See [Row selection](tables.html#row-selection)."
    notes:
      - "Only use a pager when the user can focus on just one item at a time without needing context from others in the set."
  - id: numbered-pages
    title: "Numbered pages"
    summary: "Numbered pages are for a long list split across pages, such as search results, where each page has its own address."
    classes:
      - name: ".ds-pagination"
        does: "A `<nav>` with an `aria-label` saying which list it pages through. Holds the position, Previous, the page numbers and Next, in that order."
      - name: ".ds-pagination-position"
        does: "Which items are on this page and how many there are in all, such as “1–50 of 8,291 results”."
      - name: ".ds-pagination-pages"
        does: "An `<ol>` of links, one for each page shown. The current page takes `aria-current=\"page\"`. Each link includes the word “Page” in `.is-sr-only` text, so a screen reader says “Page 2” and not “2”. A gap in the numbers is a list item holding an ellipsis."
      - name: "a.ds-btn.ds-btn-text"
        does: "Previous and Next are links, because each page has its own address. At either end of the list the link has no `href` and takes `aria-disabled=\"true\"` and `.is-disabled`."
      - name: ".ds-pagination-label"
        does: "The words Previous and Next. On a narrow screen they are hidden and the arrows remain. Screen readers still read the words."
      - name: ".ds-filter-bar"
        does: "Filters for the list go in a filter bar above it, and results per page goes in its settings. See [Filter bar](tables.html#filter-bar)."
      - name: ".ds-pagination--top"
        does: "A pager above a list. A light line below it separates it from the list."
      - name: ".ds-pagination--bottom"
        does: "A pager below a list. A light line above it separates it from the list."
      - name: ".ds-pagination-position"
        does: "On its own when the whole list fits on one page: the count still shows, with its line, and there are no controls and no pager below the list."
rules:
  - "**Name the set.** The `<nav>` takes an `aria-label` that says what it steps through, such as “Queue navigation”."
  - "**Announce the position.** The counter is a polite live region, so each step is announced without moving focus."
  - "**Disable the ends, do not remove them.** Previous on the first item and Next on the last stay in place, disabled."
  - "**Mark the current page.** In numbered pages the link to the current page takes `aria-current=\"page\"`."
---

# Pager

Controls for moving through a list: one item at a time with the pager, or a group of items at a time with numbered pages.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The pager

This component group is for moving through items one at a time, such as a moderation queue or a run of submissions, where each item has its own screen and someone works through them in order. Our current usage is in the Admin Console but it is available in other contexts.

```html
<nav class="ds-pagination" aria-label="Queue navigation">
  <span class="ds-pagination-position" aria-live="polite">Request 1 of 15</span>
  <button class="ds-btn ds-btn-text" type="button" disabled><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> Previous</button>
  <button class="ds-btn ds-btn-text" type="button">Next <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></button>
</nav>
```

```html
<nav class="ds-pagination" aria-label="Moderation queue">
  <span class="ds-pagination-position" aria-live="polite">Request 1–3 of 15</span>
  <button class="ds-btn ds-btn-text" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> Previous</button>
  <button class="ds-btn ds-btn-text" type="button">Next <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></button>
</nav>
<div class="ds-btn-group">
  <button class="ds-btn ds-btn-primary" type="button">Approve</button>
  <button class="ds-btn" type="button">Hold</button>
  <button class="ds-btn ds-btn-destructive" type="button">Remove…</button>
  <span class="ds-bulk-count" role="status">2 selected · <a href="#">Clear selection</a></span>
  <div class="ds-filter">
    <label for="queue-filter">Show</label>
    <select id="queue-filter"><option selected>All</option><option>New</option><option>Replaced</option></select>
  </div>
</div>
<div class="ds-table-scroll" role="region" aria-label="Papers in this request" tabindex="0">
  <table class="ds-table">
    <thead>
      <tr>
        <th scope="col"><span class="is-sr-only">Select</span></th>
        <th scope="col">Date</th>
        <th scope="col">Title</th>
        <th scope="col">Type</th>
      </tr>
    </thead>
    <tbody>
      <tr class="is-selected">
        <td><input type="checkbox" id="q-1" checked><label for="q-1" class="is-sr-only">Select Asymptotic Expansions of Schrödinger Operators</label></td>
        <td>2026-03-24</td>
        <td>Asymptotic Expansions of Schrödinger Operators</td>
        <td><span class="ds-tag ds-tag--rectangle">New</span></td>
      </tr>
      <tr class="is-selected">
        <td><input type="checkbox" id="q-2" checked><label for="q-2" class="is-sr-only">Select Symmetry Breaking in Non-Abelian Gauge Theories</label></td>
        <td>2025-07-09</td>
        <td>Symmetry Breaking in Non-Abelian Gauge Theories</td>
        <td><span class="ds-tag ds-tag--rectangle">Rep</span></td>
      </tr>
      <tr>
        <td><input type="checkbox" id="q-3"><label for="q-3" class="is-sr-only">Select Spectral Properties of Discrete Schrödinger Operators</label></td>
        <td>2024-07-08</td>
        <td>Spectral Properties of Discrete Schrödinger Operators</td>
        <td><span class="ds-tag ds-tag--rectangle">Wdr</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

- `.ds-pagination` — A `<nav>` with an `aria-label` saying which set it steps through. Holds the position, Previous and Next, in that order.
- `.ds-pagination-position` — The counter. Takes `aria-live="polite"`: without it a reader who cannot see the counter has no way to know that the Next they just pressed did anything. The wording is the host's to choose; the counter takes the slack before the buttons, so the buttons stay put as the number grows.
- `.ds-btn.ds-btn-text` — The two buttons, text-only, so they read as navigation rather than as actions. At either end of the set the button is `disabled`, not removed: a control that vanishes changes the shape of the toolbar under the reader, and a disabled one says “there is nothing before this”, which is the actual information.
- `.ds-pagination` — Steps through the requests. It sits above everything that belongs to the current request, so the table and its actions change together when the reader moves on.
- `.ds-btn-group, .ds-bulk-count, .ds-filter` — The group actions row: the actions, the selection count, and a filter at the far end. See [Bulk actions](tables.html#bulk-actions).
- `.ds-table, .is-selected` — The papers in the current request, with a checkbox per row. See [Row selection](tables.html#row-selection).

> Only use a pager when the user can focus on just one item at a time without needing context from others in the set.

## Numbered pages

Numbered pages are for a long list split across pages, such as search results, where each page has its own address.

```html
<nav class="ds-pagination" aria-label="Search results pages">
  <span class="ds-pagination-position">1–50 of 8,291 results</span>
  <a class="ds-btn ds-btn-text is-disabled" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
  <ol class="ds-pagination-pages">
    <li><a href="?page=1" aria-current="page"><span class="is-sr-only">Page </span>1</a></li>
    <li><a href="?page=2"><span class="is-sr-only">Page </span>2</a></li>
    <li><a href="?page=3"><span class="is-sr-only">Page </span>3</a></li>
    <li><a href="?page=4"><span class="is-sr-only">Page </span>4</a></li>
    <li><a href="?page=5"><span class="is-sr-only">Page </span>5</a></li>
    <li>…</li>
    <li><a href="?page=166"><span class="is-sr-only">Page </span>166</a></li>
  </ol>
  <a class="ds-btn ds-btn-text" href="?page=2"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
</nav>
```

```html
<nav class="ds-pagination" aria-label="Search results pages">
  <span class="ds-pagination-position">2,451–2,500 of 8,291 results</span>
  <a class="ds-btn ds-btn-text" href="?page=49"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
  <ol class="ds-pagination-pages">
    <li><a href="?page=1"><span class="is-sr-only">Page </span>1</a></li>
    <li>…</li>
    <li><a href="?page=49"><span class="is-sr-only">Page </span>49</a></li>
    <li><a href="?page=50" aria-current="page"><span class="is-sr-only">Page </span>50</a></li>
    <li><a href="?page=51"><span class="is-sr-only">Page </span>51</a></li>
    <li>…</li>
    <li><a href="?page=166"><span class="is-sr-only">Page </span>166</a></li>
  </ol>
  <a class="ds-btn ds-btn-text" href="?page=51"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
</nav>
```

```html
<form class="ds-filter-bar" method="get" action="pager.html#numbered-pages" aria-label="Filters">
  <div class="ds-filter-bar-group">
    <div class="ds-field">
      <label class="ds-label" for="pg-type">Type</label>
      <select class="ds-input" id="pg-type" name="type"><option>Any</option><option>New</option><option>Replacement</option></select>
    </div>
    <div class="ds-field">
      <label class="ds-label" for="pg-status">Status</label>
      <select class="ds-input" id="pg-status" name="status"><option>Any</option><option>On hold</option></select>
    </div>
  </div>
  <fieldset class="ds-filter-bar-group ds-filter-bar-group--settings">
    <legend class="is-sr-only">Settings</legend>
    <div class="ds-field">
      <label class="ds-label" for="pg-size">Results per page</label>
      <select class="ds-input" id="pg-size" name="size"><option selected>25</option><option>50</option><option>100</option><option>200</option></select>
    </div>
  </fieldset>
  <div class="ds-filter-bar-actions">
    <button class="ds-btn ds-btn-primary" type="submit">Apply</button>
  </div>
</form>
<nav class="ds-pagination" aria-label="Submission pages">
  <span class="ds-pagination-position">26–50 of 1,669 submissions</span>
  <a class="ds-btn ds-btn-text" href="?page=1"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
  <ol class="ds-pagination-pages">
    <li><a href="?page=1"><span class="is-sr-only">Page </span>1</a></li>
    <li><a href="?page=2" aria-current="page"><span class="is-sr-only">Page </span>2</a></li>
    <li><a href="?page=3"><span class="is-sr-only">Page </span>3</a></li>
    <li>…</li>
    <li><a href="?page=67"><span class="is-sr-only">Page </span>67</a></li>
  </ol>
  <a class="ds-btn ds-btn-text" href="?page=3"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
</nav>
```

```html
<nav class="ds-pagination ds-pagination--top" aria-label="Search results pages">
  <span class="ds-pagination-position">1–50 of 8,291 results</span>
  <a class="ds-btn ds-btn-text is-disabled" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
  <ol class="ds-pagination-pages">
    <li><a href="?page=1" aria-current="page"><span class="is-sr-only">Page </span>1</a></li>
    <li><a href="?page=2"><span class="is-sr-only">Page </span>2</a></li>
    <li><a href="?page=3"><span class="is-sr-only">Page </span>3</a></li>
    <li>…</li>
    <li><a href="?page=166"><span class="is-sr-only">Page </span>166</a></li>
  </ol>
  <a class="ds-btn ds-btn-text" href="?page=2"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
</nav>
<ol class="demo-list">
  <li>The first result</li>
  <li>The last result on this page</li>
</ol>
<nav class="ds-pagination ds-pagination--bottom" aria-label="Search results pages, below the list">
  <span class="ds-pagination-position">1–50 of 8,291 results</span>
  <a class="ds-btn ds-btn-text is-disabled" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
  <ol class="ds-pagination-pages">
    <li><a href="?page=1" aria-current="page"><span class="is-sr-only">Page </span>1</a></li>
    <li><a href="?page=2"><span class="is-sr-only">Page </span>2</a></li>
    <li><a href="?page=3"><span class="is-sr-only">Page </span>3</a></li>
    <li>…</li>
    <li><a href="?page=166"><span class="is-sr-only">Page </span>166</a></li>
  </ol>
  <a class="ds-btn ds-btn-text" href="?page=2"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
</nav>
```

```html
<nav class="ds-pagination ds-pagination--top" aria-label="Search results pages">
  <span class="ds-pagination-position">3 results</span>
</nav>
```

- `.ds-pagination` — A `<nav>` with an `aria-label` saying which list it pages through. Holds the position, Previous, the page numbers and Next, in that order.
- `.ds-pagination-position` — Which items are on this page and how many there are in all, such as “1–50 of 8,291 results”.
- `.ds-pagination-pages` — An `<ol>` of links, one for each page shown. The current page takes `aria-current="page"`. Each link includes the word “Page” in `.is-sr-only` text, so a screen reader says “Page 2” and not “2”. A gap in the numbers is a list item holding an ellipsis.
- `a.ds-btn.ds-btn-text` — Previous and Next are links, because each page has its own address. At either end of the list the link has no `href` and takes `aria-disabled="true"` and `.is-disabled`.
- `.ds-pagination-label` — The words Previous and Next. On a narrow screen they are hidden and the arrows remain. Screen readers still read the words.
- `.ds-filter-bar` — Filters for the list go in a filter bar above it, and results per page goes in its settings. See [Filter bar](tables.html#filter-bar).
- `.ds-pagination--top` — A pager above a list. A light line below it separates it from the list.
- `.ds-pagination--bottom` — A pager below a list. A light line above it separates it from the list.
- `.ds-pagination-position` — On its own when the whole list fits on one page: the count still shows, with its line, and there are no controls and no pager below the list.

## Rules

- **Name the set.** The `<nav>` takes an `aria-label` that says what it steps through, such as “Queue navigation”.
- **Announce the position.** The counter is a polite live region, so each step is announced without moving focus.
- **Disable the ends, do not remove them.** Previous on the first item and Next on the last stay in place, disabled.
- **Mark the current page.** In numbered pages the link to the current page takes `aria-current="page"`.
