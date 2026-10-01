---
page: pager.html
title: "Pager"
summary: "Previous and Next controls with a position counter for going through a set, one item at a time."
stylesheet: design-system.css
components:
  - id: the-pager
    title: "The pager"
    summary: "This component group is for moving through items one at a time, such as a moderation queue or a run of submissions, where each item has its own screen and someone works through them in order. Our current usage is in the Admin Console but it is available in other contexts."
    classes:
      - name: ".ds-pagination"
        does: "A `<nav>` with an `aria-label` saying which set it steps through. Holds Previous, the position and Next, in that order."
      - name: ".ds-pagination-position"
        does: "The counter. Takes `aria-live=\"polite\"`: without it a reader who cannot see the counter has no way to know that the Next they just pressed did anything. The wording is the host's to choose; the counter takes the slack between the buttons, so the buttons stay put as the number grows."
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
rules:
  - "**Name the set.** The `<nav>` takes an `aria-label` that says what it steps through, such as “Queue navigation”."
  - "**Announce the position.** The counter is a polite live region, so each step is announced without moving focus."
  - "**Disable the ends, do not remove them.** Previous on the first item and Next on the last stay in place, disabled."
---

# Pager

Previous and Next controls with a position counter for going through a set, one item at a time.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The pager

This component group is for moving through items one at a time, such as a moderation queue or a run of submissions, where each item has its own screen and someone works through them in order. Our current usage is in the Admin Console but it is available in other contexts.

```html
<nav class="ds-pagination" aria-label="Queue navigation">
  <button class="ds-btn ds-btn-text" type="button" disabled><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> Previous</button>
  <span class="ds-pagination-position" aria-live="polite">Request 1 of 15</span>
  <button class="ds-btn ds-btn-text" type="button">Next <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></button>
</nav>
```

```html
<nav class="ds-pagination" aria-label="Moderation queue">
  <button class="ds-btn ds-btn-text" type="button"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> Previous</button>
  <span class="ds-pagination-position" aria-live="polite">Request 4 of 15</span>
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

- `.ds-pagination` — A `<nav>` with an `aria-label` saying which set it steps through. Holds Previous, the position and Next, in that order.
- `.ds-pagination-position` — The counter. Takes `aria-live="polite"`: without it a reader who cannot see the counter has no way to know that the Next they just pressed did anything. The wording is the host's to choose; the counter takes the slack between the buttons, so the buttons stay put as the number grows.
- `.ds-btn.ds-btn-text` — The two buttons, text-only, so they read as navigation rather than as actions. At either end of the set the button is `disabled`, not removed: a control that vanishes changes the shape of the toolbar under the reader, and a disabled one says “there is nothing before this”, which is the actual information.
- `.ds-pagination` — Steps through the requests. It sits above everything that belongs to the current request, so the table and its actions change together when the reader moves on.
- `.ds-btn-group, .ds-bulk-count, .ds-filter` — The group actions row: the actions, the selection count, and a filter at the far end. See [Bulk actions](tables.html#bulk-actions).
- `.ds-table, .is-selected` — The papers in the current request, with a checkbox per row. See [Row selection](tables.html#row-selection).

> Only use a pager when the user can focus on just one item at a time without needing context from others in the set.

## Rules

- **Name the set.** The `<nav>` takes an `aria-label` that says what it steps through, such as “Queue navigation”.
- **Announce the position.** The counter is a polite live region, so each step is announced without moving focus.
- **Disable the ends, do not remove them.** Previous on the first item and Next on the last stay in place, disabled.
