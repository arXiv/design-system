---
page: tables.html
title: "Tables"
summary: "The table and what can be built on it: sortable columns, filters, row selection and bulk actions. All of it is shared by the public site and internal tools; internal tools change only the colours."
stylesheet: design-system.css
components:
  - id: the-table
    title: "The table"
    summary: "One table, `.ds-table`, on the public site and in internal tools. It has row dividers and a row hover. The header row comes from the markup: a table with a `<thead>` has one, in condensed uppercase body-colour text on the warm tint, and a table without one does not."
    classes:
      - name: ".ds-table"
        does: "The whole table, on the `<table>` element: the frame, the row dividers and the row hover. Directly inside a card it has no frame of its own; the card is the frame."
      - name: "<thead>"
        does: "Draws the header row. Leave it out and the table has none; no class turns the header row on or off."
      - name: "style=\"table-layout: fixed\""
        does: "Add it inline on the `<table>` when fixed column widths are needed. The table defaults to auto layout."
      - name: ".ds-table-footer"
        does: "A `<div>` below the table for row counts or pagination."
      - name: ".ds-tag--rectangle"
        does: "The Type column: a rectangular tag at the default level, one per row, documented on [Tags](tags.md#rectangular-labels). No colour is mapped to New, Rep or Wdr."
      - name: "scope=\"col\""
        does: "Required on every `<th>` in the header row, so a screen reader reads the column name with each cell."
      - name: ".ds-table-scroll"
        does: "The wrapper. A table wider than the viewport scrolls inside it, so the page never scrolls sideways. It takes `role=\"region\"`, an `aria-label` that names the table, and `tabindex=\"0\"` so a keyboard user can reach it to scroll."
      - name: "scope=\"row\""
        does: "A `<th>` in the body is a row header: it names its row, in the cell type at full weight on a tinted ground, and a screen reader reads it with each cell in the row. The tint comes from the element, so no class is needed."
    notes:
      - "The Type column uses rectangular tags at the default level, documented on [Tags](tags.md#rectangular-labels)."
  - id: outside-borders
    title: "Outside borders"
    summary: "A table has a border all the way round, except directly inside a card, where the card is the frame and the table has none."
  - id: sortable-column-headers
    title: "Sortable column headers"
    summary: "A sortable column's header is a link to the same page sorted by that column, holding the label and a `<span class=\"sort-arrow\">` for the direction. It looks like the plain header, it can be reached and pressed from the keyboard, and it works without JavaScript, as the [sort bar](buttons.md#a-group-of-toggles) does. `aria-sort` goes on the `<th>` of the sorted column, and the arrow follows it."
    classes:
      - name: "<a href=\"?sort=…\">"
        does: "Inside the `<th>`: a link to this page sorted by the column. On the sorted column it sends the reverse direction; on any other, the column's first direction. Styled to look like the header text; the label darkens on hover. No class."
      - name: ".sort-arrow"
        does: "The direction indicator, a `<span aria-hidden=\"true\">` inside the link. The glyph in the markup is replaced by an icon: two arrows in `--ds-text-muted` when the column is unsorted."
      - name: "aria-sort=\"ascending\", aria-sort=\"descending\""
        does: "On the `<th>` of the sorted column only. It tells a screen reader which column orders the table and how, and it turns the arrow up or down in `--ds-text`."
      - name: ".ds-table-footer"
        does: "The row count under the table."
    notes:
      - "The server sorts the rows. In this demo a script sorts them in place instead, because the page is static."
  - id: filters
    title: "Filters"
    summary: "Filters for a table go in the header bar of the card that holds it. For a demo, see [Filters](filters.md)."
  - id: row-selection
    title: "Row selection"
    summary: "Rows a reader can choose, one checkbox per row, so an action can apply to several at once."
    classes:
      - name: ".is-selected"
        does: "On the `<tr>`. Tints the row with `--ds-accent-wash`; the tint aids scanability of the selection set. Selection state must not rely on the tint alone: the row’s checkbox shows the state (WCAG 1.4.1)."
      - name: "<input type=\"checkbox\">"
        does: "The first cell of every row. A direct child of the `<td>`, which gives it a 24px target and this surface’s accent. Each one has a `<label class=\"is-sr-only\">` that names its row."
  - id: bulk-actions
    title: "Bulk actions"
    summary: "Actions that apply to every selected row at once, as in moderation queues and ownership lists. The actions sit in the header bar of the card that holds a table with [row selection](#row-selection)."
    classes:
      - name: ".ds-card-bar"
        does: "The header bar of the card that holds the table: the actions and the selection count at its start, and any filter at its end. It wraps on a narrow screen. See [Cards with a header bar](cards.md#cards-with-a-header-bar)."
      - name: ".ds-btn-group"
        does: "The actions and the selection count, kept together."
      - name: ".ds-btn-primary, .ds-btn, .ds-btn-destructive, with .ds-btn-compact"
        does: "The actions, in the tiers documented on [Buttons](buttons.md), compact like every control in a header bar. The destructive action comes last."
      - name: ".ds-bulk-count"
        does: "The selection count and the “Clear selection” link, beside the actions. Takes `role=\"status\"` so a change in the count is announced."
      - name: "<button disabled>"
        does: "The `disabled` attribute on every action button while nothing is selected. The buttons stay in place; the filter stays live, because it does not depend on a selection."
  - id: selecting-items-in-a-list
    title: "Selecting items in a list"
    summary: "The same selection when the set is a list rather than a table, such as a list of papers. Each item starts with its checkbox, lined up with the item's first line. The actions on the selection sit in the header bar above the list, as for a table. A control that acts on one item only sits at the end of that item, on the right."
    classes:
      - name: "<input type=\"checkbox\">"
        does: "The first child of each item, then its `<label class=\"is-sr-only\">`, which names the item: “Select” and the paper's title. The box is 16px like every checkbox, in a column 24px wide, which is its target, and lines up with the item's first line; everything after it sits beside it. No class."
      - name: ".ds-card-bar"
        does: "The header bar above the list, with the actions on the selection and the count, as in [Bulk actions](#bulk-actions). An action on the selection says so: “Remove selected”, with the trash icon."
      - name: ".ds-btn-group.ds-btn-group--end"
        does: "The last child of an item: the controls for that item only, on the right, as a form's action bar is. Each control's name includes the item's, in an `.is-sr-only` span, because “Remove” alone does not say which."
  - id: striped-rows
    title: "Striped rows"
    group: "Modifiers"
    summary: "Every other row takes a tint, which helps the eye follow a long row across a wide table."
    classes:
      - name: ".ds-table--striped"
        does: "Tints every even row of the body in Warm Tint, on both surfaces."
  - id: numeric-columns
    title: "Numeric columns"
    group: "Modifiers"
    summary: "Numbers align on the right, and their digits line up from row to row."
    classes:
      - name: ".ds-num"
        does: "On every cell of a numeric column, the header included. Aligns the numbers on the right and uses tabular figures."
rules:
  - "A sortable header is a link that reloads the page sorted, as the sort bar is a form that does. Pressing the sorted column's header reverses the order; pressing another column's header sorts by it, in its first direction, and the previous column becomes unsorted. Only the sorted column has `aria-sort`."
  - "Action buttons come first, then their descriptive text (selection count, “Clear selection”), with any filter at the far end of the row, all in the header bar of the card that holds the table. Destructive actions (Remove, Delete) come last among the actions and always require a confirmation step."
  - "**Mark the header cells.** Put `scope=\"col\"` on every `<th>` in the header row, so a screen reader reads the column name with each cell instead of a bare value."
  - "**Give the table a name.** A `<caption>`, or an `aria-label` on the scrolling region around the table, as the examples on this page do. Without one, a screen reader user lands in “table, 4 columns” with no idea which table it is."
  - "**Say which column is sorted.** Put `aria-sort=\"ascending\"` or `aria-sort=\"descending\"` on the sorted `<th>` and remove it from the others when the sort changes. The arrow is a glyph, and the class is invisible to a screen reader."
  - "**Label every row checkbox.** Each checkbox gets a `<label class=\"is-sr-only\">` that names its row, such as “Select Asymptotic Expansions”. Without it the choice reads as “checkbox, not checked” and nothing more. Prefer the label to `aria-label`, because page translation tools skip attributes."
  - "**Announce the count.** The selection count sits in an element with `role=\"status\"`, so a screen reader user hears “2 selected” when it changes without leaving the checkbox they just ticked."
  - "**Actions disable, they never disappear.** When nothing is selected, bulk-action buttons render disabled — not removed. Controls that appear and vanish cost users their bearings. This rule is universal (it also appears in the agent guide’s hard rules)."
---

# Tables

The table and what can be built on it: sortable columns, filters, row selection and bulk actions. All of it is shared by the public site and internal tools; internal tools change only the colours.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The table

One table, `.ds-table`, on the public site and in internal tools. It has row dividers and a row hover. The header row comes from the markup: a table with a `<thead>` has one, in condensed uppercase body-colour text on the warm tint, and a table without one does not.

**With a header row**

```html
<div class="ds-table-scroll" role="region" aria-label="Submissions" tabindex="0">
  <table class="ds-table">
    <thead>
      <tr>
        <th scope="col">Date</th>
        <th scope="col">Title</th>
        <th scope="col">Submitter</th>
        <th scope="col">Type</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2026-03-24</td>
        <td>Asymptotic Expansions of Schrödinger Operators</td>
        <td>Esther McGill-Henry</td>
        <td><span class="ds-tag ds-tag--rectangle">New</span></td>
      </tr>
      <tr>
        <td>2025-07-09</td>
        <td>Symmetry Breaking in Non-Abelian Gauge Theories</td>
        <td>Esther McGill-Henry</td>
        <td><span class="ds-tag ds-tag--rectangle">Rep</span></td>
      </tr>
      <!-- … one row per record -->
    </tbody>
  </table>
</div>
```

- `.ds-table` — The whole table, on the `<table>` element: the frame, the row dividers and the row hover. Directly inside a card it has no frame of its own; the card is the frame.
- `<thead>` — Draws the header row. Leave it out and the table has none; no class turns the header row on or off.
- `style="table-layout: fixed"` — Add it inline on the `<table>` when fixed column widths are needed. The table defaults to auto layout.
- `.ds-table-footer` — A `<div>` below the table for row counts or pagination.
- `.ds-tag--rectangle` — The Type column: a rectangular tag at the default level, one per row, documented on [Tags](tags.md#rectangular-labels). No colour is mapped to New, Rep or Wdr.
- `scope="col"` — Required on every `<th>` in the header row, so a screen reader reads the column name with each cell.
- `.ds-table-scroll` — The wrapper. A table wider than the viewport scrolls inside it, so the page never scrolls sideways. It takes `role="region"`, an `aria-label` that names the table, and `tabindex="0"` so a keyboard user can reach it to scroll.

**With a header column**

```html
<table class="ds-table">
  <tbody>
    <tr><th scope="row">Primary category</th><td>math.SP</td></tr>
    <tr><th scope="row">Submitted</th><td>2026-03-24</td></tr>
    <tr><th scope="row">License</th><td>CC BY 4.0</td></tr>
  </tbody>
</table>
```

- `scope="row"` — A `<th>` in the body is a row header: it names its row, in the cell type at full weight on a tinted ground, and a screen reader reads it with each cell in the row. The tint comes from the element, so no class is needed.

> The Type column uses rectangular tags at the default level, documented on [Tags](tags.md#rectangular-labels).

## Outside borders

A table has a border all the way round, except directly inside a card, where the card is the frame and the table has none.

## Sortable column headers

A sortable column's header is a link to the same page sorted by that column, holding the label and a `<span class="sort-arrow">` for the direction. It looks like the plain header, it can be reached and pressed from the keyboard, and it works without JavaScript, as the [sort bar](buttons.md#a-group-of-toggles) does. `aria-sort` goes on the `<th>` of the sorted column, and the arrow follows it.

**Sortable headers**

```html
<table class="ds-table">
  <thead>
    <tr>
      <th scope="col" aria-sort="descending">
        <a href="?sort=date-asc">Date <span class="sort-arrow" aria-hidden="true">↓</span></a>
      </th>
      <th scope="col">Title</th>
      <th scope="col"><a href="?sort=type-asc">Type <span class="sort-arrow" aria-hidden="true">⇅</span></a></th>
      <th scope="col"><a href="?sort=status-asc">Status <span class="sort-arrow" aria-hidden="true">⇅</span></a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2026-03-24</td>
      <td>Asymptotic Expansions</td>
      <td><span class="ds-tag ds-tag--rectangle">New</span></td>
      <td>On Hold</td>
    </tr>
    <tr>
      <td>2025-07-09</td>
      <td>Symmetry Breaking</td>
      <td><span class="ds-tag ds-tag--rectangle">Rep</span></td>
      <td>Removed</td>
    </tr>
    <!-- … one row per record -->
  </tbody>
</table>
<div class="ds-table-footer">1–4 of 4</div>
```

- `<a href="?sort=…">` — Inside the `<th>`: a link to this page sorted by the column. On the sorted column it sends the reverse direction; on any other, the column's first direction. Styled to look like the header text; the label darkens on hover. No class.
- `.sort-arrow` — The direction indicator, a `<span aria-hidden="true">` inside the link. The glyph in the markup is replaced by an icon: two arrows in `--ds-text-muted` when the column is unsorted.
- `aria-sort="ascending", aria-sort="descending"` — On the `<th>` of the sorted column only. It tells a screen reader which column orders the table and how, and it turns the arrow up or down in `--ds-text`.
- `.ds-table-footer` — The row count under the table.

> The server sorts the rows. In this demo a script sorts them in place instead, because the page is static.

## Filters

Filters for a table go in the header bar of the card that holds it. For a demo, see [Filters](filters.md).

## Row selection

Rows a reader can choose, one checkbox per row, so an action can apply to several at once.

```html
<div class="ds-table-scroll" role="region" aria-label="Owned papers" tabindex="0">
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
        <td>
          <input type="checkbox" id="sel-1" checked>
          <label for="sel-1" class="is-sr-only">Select Asymptotic Expansions of Schrödinger Operators</label>
        </td>
        <td>2026-03-24</td>
        <td>Asymptotic Expansions of Schrödinger Operators</td>
        <td><span class="ds-tag ds-tag--rectangle">New</span></td>
      </tr>
      <tr class="is-selected">
        <td>
          <input type="checkbox" id="sel-2" checked>
          <label for="sel-2" class="is-sr-only">Select Symmetry Breaking in Non-Abelian Gauge Theories</label>
        </td>
        <td>2025-07-09</td>
        <td>Symmetry Breaking in Non-Abelian Gauge Theories</td>
        <td><span class="ds-tag ds-tag--rectangle">Rep</span></td>
      </tr>
      <!-- … one row per record -->
    </tbody>
  </table>
</div>
```

- `.is-selected` — On the `<tr>`. Tints the row with `--ds-accent-wash`; the tint aids scanability of the selection set. Selection state must not rely on the tint alone: the row’s checkbox shows the state (WCAG 1.4.1).
- `<input type="checkbox">` — The first cell of every row. A direct child of the `<td>`, which gives it a 24px target and this surface’s accent. Each one has a `<label class="is-sr-only">` that names its row.

## Bulk actions

Actions that apply to every selected row at once, as in moderation queues and ownership lists. The actions sit in the header bar of the card that holds a table with [row selection](#row-selection).

**Selection active**

```html
<div class="ds-card">
  <div class="ds-card-bar">
    <div class="ds-btn-group">
      <button class="ds-btn ds-btn-primary ds-btn-compact" type="button">Approve</button>
      <button class="ds-btn ds-btn-compact" type="button">Hold</button>
      <button class="ds-btn ds-btn-destructive ds-btn-compact" type="button"><svg aria-hidden="true">…</svg> Remove selected</button>
      <span class="ds-bulk-count" role="status">2 selected · <a href="#">Clear selection</a></span>
    </div>
    <form class="ds-form--compact" method="get" action="…" aria-label="Filter papers">
      <label>Show <select class="ds-input" name="show">…</select></label>
      <button class="ds-btn ds-btn-compact" type="submit">Apply</button>
    </form>
  </div>
  <div class="ds-table-scroll" role="region" aria-label="Owned papers" tabindex="0">
    <table class="ds-table">…</table>
  </div>
</div>
```

- `.ds-card-bar` — The header bar of the card that holds the table: the actions and the selection count at its start, and any filter at its end. It wraps on a narrow screen. See [Cards with a header bar](cards.md#cards-with-a-header-bar).
- `.ds-btn-group` — The actions and the selection count, kept together.
- `.ds-btn-primary, .ds-btn, .ds-btn-destructive, with .ds-btn-compact` — The actions, in the tiers documented on [Buttons](buttons.md), compact like every control in a header bar. The destructive action comes last.
- `.ds-bulk-count` — The selection count and the “Clear selection” link, beside the actions. Takes `role="status"` so a change in the count is announced.

**Nothing selected**

```html
<div class="ds-card-bar">
  <div class="ds-btn-group">
    <button class="ds-btn ds-btn-primary ds-btn-compact" type="button" disabled>Approve</button>
    <button class="ds-btn ds-btn-compact" type="button" disabled>Hold</button>
    <button class="ds-btn ds-btn-destructive ds-btn-compact" type="button" disabled><svg aria-hidden="true">…</svg> Remove selected</button>
    <span class="ds-bulk-count" role="status">0 selected</span>
  </div>
  <form class="ds-form--compact" method="get" action="…" aria-label="Filter papers">…</form>
</div>
```

- `<button disabled>` — The `disabled` attribute on every action button while nothing is selected. The buttons stay in place; the filter stays live, because it does not depend on a selection.

## Selecting items in a list

The same selection when the set is a list rather than a table, such as a list of papers. Each item starts with its checkbox, lined up with the item's first line. The actions on the selection sit in the header bar above the list, as for a table. A control that acts on one item only sits at the end of that item, on the right.

**Two papers selected**

```html
<div class="ds-card">
  <div class="ds-card-bar">
    <div class="ds-btn-group">
      <button class="ds-btn ds-btn-destructive ds-btn-compact" type="button"><svg aria-hidden="true">…</svg> Remove selected</button>
      <span class="ds-bulk-count" role="status">2 selected · <a href="#">Clear selection</a></span>
    </div>
  </div>
  <ol class="ds-paper-list" aria-label="Saved papers">
    <li class="ds-paper">
      <input type="checkbox" id="lists-1" checked><label for="lists-1" class="is-sr-only">Select LUMA: A CNN for Strong Gravitational Lens Searches in Astronomical Imaging</label>
      <h3><a href="https://arxiv.org/abs/2609.36857">LUMA: A CNN for Strong Gravitational Lens Searches in Astronomical Imaging</a></h3>
      <p class="ds-link-list">…the authors…</p>
      <div class="ds-btn-group ds-btn-group--end">
        <button type="button" class="ds-btn ds-btn-text ds-btn-compact">Remove<span class="is-sr-only"> LUMA: A CNN for Strong Gravitational Lens Searches in Astronomical Imaging</span></button>
      </div>
    </li>
    …
  </ol>
</div>
```

- `<input type="checkbox">` — The first child of each item, then its `<label class="is-sr-only">`, which names the item: “Select” and the paper's title. The box is 16px like every checkbox, in a column 24px wide, which is its target, and lines up with the item's first line; everything after it sits beside it. No class.
- `.ds-card-bar` — The header bar above the list, with the actions on the selection and the count, as in [Bulk actions](#bulk-actions). An action on the selection says so: “Remove selected”, with the trash icon.
- `.ds-btn-group.ds-btn-group--end` — The last child of an item: the controls for that item only, on the right, as a form's action bar is. Each control's name includes the item's, in an `.is-sr-only` span, because “Remove” alone does not say which.

## Striped rows  (Modifiers)

Every other row takes a tint, which helps the eye follow a long row across a wide table.

```html
<table class="ds-table ds-table--striped">
  …
</table>
```

- `.ds-table--striped` — Tints every even row of the body in Warm Tint, on both surfaces.

## Numeric columns  (Modifiers)

Numbers align on the right, and their digits line up from row to row.

```html
<th scope="col" class="ds-num">New submissions</th>
…
<td class="ds-num">3,961</td>
```

- `.ds-num` — On every cell of a numeric column, the header included. Aligns the numbers on the right and uses tabular figures.

## Rules

### Sort interaction

A sortable header is a link that reloads the page sorted, as the sort bar is a form that does. Pressing the sorted column's header reverses the order; pressing another column's header sorts by it, in its first direction, and the previous column becomes unsorted. Only the sorted column has `aria-sort`.

### Bulk-action bar layout

Action buttons come first, then their descriptive text (selection count, “Clear selection”), with any filter at the far end of the row, all in the header bar of the card that holds the table. Destructive actions (Remove, Delete) come last among the actions and always require a confirmation step.

### Accessibility essentials

- **Mark the header cells.** Put `scope="col"` on every `<th>` in the header row, so a screen reader reads the column name with each cell instead of a bare value.
- **Give the table a name.** A `<caption>`, or an `aria-label` on the scrolling region around the table, as the examples on this page do. Without one, a screen reader user lands in “table, 4 columns” with no idea which table it is.
- **Say which column is sorted.** Put `aria-sort="ascending"` or `aria-sort="descending"` on the sorted `<th>` and remove it from the others when the sort changes. The arrow is a glyph, and the class is invisible to a screen reader.
- **Label every row checkbox.** Each checkbox gets a `<label class="is-sr-only">` that names its row, such as “Select Asymptotic Expansions”. Without it the choice reads as “checkbox, not checked” and nothing more. Prefer the label to `aria-label`, because page translation tools skip attributes.
- **Announce the count.** The selection count sits in an element with `role="status"`, so a screen reader user hears “2 selected” when it changes without leaving the checkbox they just ticked.
- **Actions disable, they never disappear.** When nothing is selected, bulk-action buttons render disabled — not removed. Controls that appear and vanish cost users their bearings. This rule is universal (it also appears in the agent guide’s hard rules).
