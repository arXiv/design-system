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
        does: "Steps through the requests. It sits above the card, because it changes everything in it: the table and its actions change together when the reader moves on."
      - name: ".ds-card-bar"
        does: "The header bar of the current request: the group actions and the selection count at its start, and a filter at its end. See [Bulk actions](tables.md#bulk-actions)."
      - name: ".ds-table, .is-selected"
        does: "The papers in the current request, with a checkbox per row. See [Row selection](tables.md#row-selection)."
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
        does: "An `<ol>` of links, one for each page shown. The current page takes `aria-current=\"page\"`. Each link includes the word “Page” in `.is-sr-only` text, so a screen reader says “Page 2” and not “2”. A gap in the numbers is a list item holding an ellipsis. On a narrow screen the page numbers are hidden, and the pager is one row: Previous, the position, Next."
      - name: "a.ds-btn.ds-btn-text"
        does: "Previous and Next are links, because each page has its own address. At either end of the list the link has no `href` and takes `aria-disabled=\"true\"` and `.is-disabled`."
      - name: ".ds-pagination-label"
        does: "The words Previous and Next, on every pager. On a narrow screen only the arrows show, and screen readers still read the words."
      - name: ".ds-card-bar"
        does: "The filters, with results per page at the end of the row, and the total at the end of the bar. See [Filters](filters.md)."
      - name: ".ds-pagination as the card's last row"
        does: "The pager, below the list only, edge to edge like the header bar: the position on the left, the page numbers on the right."
      - name: ".ds-pagination--top"
        does: "A pager above a list, in a tinted bar."
      - name: ".ds-pagination--bottom"
        does: "A pager below a list, in a tinted bar. With the bar above, it bookends the list."
      - name: ".ds-pagination-position"
        does: "On its own when the whole list fits on one page: the count still shows, in its bar, and there are no controls and no pager below the list."
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
  <button class="ds-btn ds-btn-text" type="button" disabled><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></button>
  <button class="ds-btn ds-btn-text" type="button"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></button>
</nav>
```

```html
<nav class="ds-pagination" aria-label="Moderation queue">
  <span class="ds-pagination-position" aria-live="polite">Request 1–3 of 15</span>
  <button class="ds-btn ds-btn-text" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></button>
  <button class="ds-btn ds-btn-text" type="button"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></button>
</nav>
<div class="ds-card">
  <div class="ds-card-bar">
    <div class="ds-btn-group">
      <button class="ds-btn ds-btn-primary ds-btn-compact" type="button">Approve</button>
      <button class="ds-btn ds-btn-compact" type="button">Hold</button>
      <button class="ds-btn ds-btn-destructive ds-btn-compact" type="button">Remove…</button>
      <span class="ds-bulk-count" role="status">2 selected · <a href="#">Clear selection</a></span>
    </div>
    <form class="ds-form--compact" method="get" action="…" aria-label="Filter papers">
      <label>Show <select class="ds-input" name="show">…</select></label>
      <button class="ds-btn ds-btn-compact" type="submit">Apply</button>
    </form>
  </div>
  <div class="ds-table-scroll" role="region" aria-label="Papers in this request" tabindex="0">
    <table class="ds-table">…</table>
  </div>
</div>
```

- `.ds-pagination` — A `<nav>` with an `aria-label` saying which set it steps through. Holds the position, Previous and Next, in that order.
- `.ds-pagination-position` — The counter. Takes `aria-live="polite"`: without it a reader who cannot see the counter has no way to know that the Next they just pressed did anything. The wording is the host's to choose; the counter takes the slack before the buttons, so the buttons stay put as the number grows.
- `.ds-btn.ds-btn-text` — The two buttons, text-only, so they read as navigation rather than as actions. At either end of the set the button is `disabled`, not removed: a control that vanishes changes the shape of the toolbar under the reader, and a disabled one says “there is nothing before this”, which is the actual information.
- `.ds-pagination` — Steps through the requests. It sits above the card, because it changes everything in it: the table and its actions change together when the reader moves on.
- `.ds-card-bar` — The header bar of the current request: the group actions and the selection count at its start, and a filter at its end. See [Bulk actions](tables.md#bulk-actions).
- `.ds-table, .is-selected` — The papers in the current request, with a checkbox per row. See [Row selection](tables.md#row-selection).

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
<div class="ds-card">
  <div class="ds-card-bar">
    <form class="ds-form--compact" method="get" action="…" aria-label="Filters">
      <label>Type <select class="ds-input" name="type">…</select></label>
      <label>Status <select class="ds-input" name="status">…</select></label>
      <label>Per page <select class="ds-input" name="size">…</select></label>
      <button class="ds-btn ds-btn-compact" type="submit">Apply</button>
    </form>
    <p>1,669 submissions</p>
  </div>
  <div class="ds-table-scroll" …><table class="ds-table">…</table></div>
  <nav class="ds-pagination" aria-label="Submission pages">
    <span class="ds-pagination-position">26–50 of 1,669 submissions</span>
  <a class="ds-btn ds-btn-text" href="?page=1"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
  <ol class="ds-pagination-pages">
    <li><a href="?page=1"><span class="is-sr-only">Page </span>1</a></li>
    <li><a href="?page=2" aria-current="page"><span class="is-sr-only">Page </span>2</a></li>
    <li><a href="?page=3"><span class="is-sr-only">Page </span>3</a></li>
    <li><a href="?page=4"><span class="is-sr-only">Page </span>4</a></li>
    <li><a href="?page=5"><span class="is-sr-only">Page </span>5</a></li>
    <li>…</li>
    <li><a href="?page=67"><span class="is-sr-only">Page </span>67</a></li>
  </ol>
  <a class="ds-btn ds-btn-text" href="?page=3"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
</nav>
</div>
```

```html
<nav class="ds-pagination ds-pagination--top" aria-label="Search results pages">
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
    <li><a href="?page=4"><span class="is-sr-only">Page </span>4</a></li>
    <li><a href="?page=5"><span class="is-sr-only">Page </span>5</a></li>
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
- `.ds-pagination-pages` — An `<ol>` of links, one for each page shown. The current page takes `aria-current="page"`. Each link includes the word “Page” in `.is-sr-only` text, so a screen reader says “Page 2” and not “2”. A gap in the numbers is a list item holding an ellipsis. On a narrow screen the page numbers are hidden, and the pager is one row: Previous, the position, Next.
- `a.ds-btn.ds-btn-text` — Previous and Next are links, because each page has its own address. At either end of the list the link has no `href` and takes `aria-disabled="true"` and `.is-disabled`.
- `.ds-pagination-label` — The words Previous and Next, on every pager. On a narrow screen only the arrows show, and screen readers still read the words.
- `.ds-card-bar` — The filters, with results per page at the end of the row, and the total at the end of the bar. See [Filters](filters.md).
- `.ds-pagination as the card's last row` — The pager, below the list only, edge to edge like the header bar: the position on the left, the page numbers on the right.
- `.ds-pagination--top` — A pager above a list, in a tinted bar.
- `.ds-pagination--bottom` — A pager below a list, in a tinted bar. With the bar above, it bookends the list.
- `.ds-pagination-position` — On its own when the whole list fits on one page: the count still shows, in its bar, and there are no controls and no pager below the list.

## Rules

- **Name the set.** The `<nav>` takes an `aria-label` that says what it steps through, such as “Queue navigation”.
- **Announce the position.** The counter is a polite live region, so each step is announced without moving focus.
- **Disable the ends, do not remove them.** Previous on the first item and Next on the last stay in place, disabled.
- **Mark the current page.** In numbered pages the link to the current page takes `aria-current="page"`.
