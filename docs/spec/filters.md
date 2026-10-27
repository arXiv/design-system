---
page: filters.html
title: "Filters"
summary: "Filters narrow a set of data, such as a table, a list of cards or a chart, to the items a reader wants. When each filter takes one choice, such as one status, the filters are selects in a row. When a filter takes several choices at once, such as three categories, the filters go in a panel behind a Filters button. Both go in the header bar of the set they change."
stylesheet: design-system.css
components:
  - id: single-choice-filters
    title: "Single-choice filters"
    summary: "Each filter takes one choice, so each is a select. Two or three selects sit in a row in the header bar of the set they change, with one Apply button. Each is always set, with an inclusive default such as “All”, so the row shows every choice in force."
    classes:
      - name: ".ds-card-bar"
        does: "The header bar of the set, with the filters at its start. A total ends it only when the reader cannot see the whole set; here every category is in view, so there is none. See [Cards with a header bar](cards.md#cards-with-a-header-bar)."
      - name: ".ds-form--compact"
        does: "The filters, as a [compact form](forms.md#compact-form): one row, each select inside its label. It is a `<form method=\"get\">`, so the choices go in the page address and a filtered view can be linked."
      - name: "<button type=\"submit\">"
        does: "Apply: a compact secondary button (`.ds-btn-compact`), at the end of the row."
      - name: "<fieldset>, <legend>"
        does: "The two dates of a range are one fieldset, so they stay together on the row and a screen reader reads each with the range's name: “Submitted, from”."
  - id: multiple-choice-filters
    title: "Multiple-choice filters"
    summary: "A filter that takes several choices at once is a group of checkboxes, in a filter panel opened by a Filters button. The panel holds every filter for the set, including single-choice ones, so it is also the home for more filters than fit in a row. The filters that are applied show beside the button as tags, with Clear all after them."
    classes:
      - name: ".ds-filter-button"
        does: "A compact secondary button with the filter icon (`list-filter`) and no chevron. `popovertarget` names its panel. While the panel is open the button shows its pressed state."
      - name: ".ds-filter-value"
        does: "Optional, inside the button: what is applied, after the button's name. It shortens with an ellipsis when the row is narrow."
      - name: ".ds-filter-panel"
        does: "The filter panel, a `popover` with `role=\"dialog\"` and a name. Its background is the open button's background, and it attaches to the button's bottom edge. It holds a [compact form](forms.md#compact-form), one short column. `--ds-panel-width` sets its width."
      - name: "<fieldset> with checkboxes"
        does: "A filter that takes several values, such as categories, is a fieldset of `.ds-check` checkboxes."
      - name: "<fieldset> with the legend Settings"
        does: "A setting, such as threshold days, changes a calculation and is not a filter. It goes after the filters, in a fieldset of its own, and is not shown as a tag."
      - name: ".ds-tag, .ds-tag-remove"
        does: "One tag for each applied filter, after the button. Its remove control is a link to the page without that filter. See [Tags](tags.md#complex-tags)."
      - name: "<a> Clear all"
        does: "A link to the page without filters, after the tags, while a filter is applied."
      - name: "<script src=\"filter-panel.js\" defer>"
        does: "Places the panel at the button's edge and keeps `aria-expanded` current. Without it the panel opens in the centre of the window."
rules:
  - "**One set of filters for each set of data**, in the set's header bar. A filter applies to everything in the set."
  - "**A total ends the header bar only when the reader cannot see the whole set**: the set runs over more than one page, as in “1,669 submissions”, or the filters hide part of it, as in “3 of 120 holds”. A set with every item in view needs no total. When the controls do not fit on one line, the bar wraps and the total takes a line of its own."
  - "**Keep Apply when a change reloads the page.** See [Compact form](forms.md#compact-form)."
  - "**After Apply, the page shows what was applied**: the server writes the chosen values back into the fields, and into the tags."
  - "**Sorting is not filtering.** A Sort by select can end the row of filters; a table sorts from its [column headers](tables.md#sortable-column-headers)."
  - "**Every control sits inside its label.** A date range or a group of checkboxes is a fieldset with a legend."
  - "**The filter panel is a named dialog.** The button reports whether it is open with `aria-expanded`. Escape closes the panel and returns focus to the button."
  - "**Each remove control says what it removes**, in a `<span class=\"is-sr-only\">`: “Remove the filter Status: On hold”."
  - "**On a touch screen every target is 44px.** Compact fields, compact buttons and remove controls have it built in."
---

# Filters

Filters narrow a set of data, such as a table, a list of cards or a chart, to the items a reader wants. When each filter takes one choice, such as one status, the filters are selects in a row. When a filter takes several choices at once, such as three categories, the filters go in a panel behind a Filters button. Both go in the header bar of the set they change.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Single-choice filters

Each filter takes one choice, so each is a select. Two or three selects sit in a row in the header bar of the set they change, with one Apply button. Each is always set, with an inclusive default such as “All”, so the row shows every choice in force.

```html
<div class="ds-card">
  <div class="ds-card-bar">
    <form class="ds-form--compact" method="get" action="…" aria-label="Filter categories">
      <label>Group <select class="ds-input" name="group">…</select></label>
      <label>Archive <select class="ds-input" name="archive">…</select></label>
      <label>Category <select class="ds-input" name="category">…</select></label>
      <button class="ds-btn ds-btn-compact" type="submit">Apply</button>
    </form>
  </div>
  <div class="ds-table-scroll" …><table class="ds-table">…</table></div>
</div>
```

```html
<form class="ds-form--compact" method="get" action="…" aria-label="Filter submissions by date">
  <fieldset>
    <legend>Submitted</legend>
    <label>from <input class="ds-input" name="from" type="date"></label>
    <label>to <input class="ds-input" name="to" type="date"></label>
  </fieldset>
  <button class="ds-btn ds-btn-compact" type="submit">Apply</button>
</form>
```

- `.ds-card-bar` — The header bar of the set, with the filters at its start. A total ends it only when the reader cannot see the whole set; here every category is in view, so there is none. See [Cards with a header bar](cards.md#cards-with-a-header-bar).
- `.ds-form--compact` — The filters, as a [compact form](forms.md#compact-form): one row, each select inside its label. It is a `<form method="get">`, so the choices go in the page address and a filtered view can be linked.
- `<button type="submit">` — Apply: a compact secondary button (`.ds-btn-compact`), at the end of the row.
- `<fieldset>, <legend>` — The two dates of a range are one fieldset, so they stay together on the row and a screen reader reads each with the range's name: “Submitted, from”.

## Multiple-choice filters

A filter that takes several choices at once is a group of checkboxes, in a filter panel opened by a Filters button. The panel holds every filter for the set, including single-choice ones, so it is also the home for more filters than fit in a row. The filters that are applied show beside the button as tags, with Clear all after them.

```html
<div class="ds-card-bar">
  <div class="ds-btn-group" role="group" aria-label="Filters on recent holds">
    <button type="button" class="ds-btn ds-btn-compact ds-filter-button" popovertarget="holds-panel" aria-expanded="false">
      <svg …the list-filter icon… aria-hidden="true">…</svg>
      Filters
    </button>
    <span class="ds-tag ds-tag--keep-case">Status: On hold<a class="ds-tag-remove" href="…"><span aria-hidden="true">✕</span><span class="is-sr-only">Remove the filter Status: On hold</span></a></span>
    …
    <a href="…">Clear all</a>
  </div>
  <p>3 of 120 holds</p>
</div>
<div class="ds-filter-panel" id="holds-panel" popover role="dialog" aria-label="Filters on recent holds">
  <form class="ds-form--compact" method="get" action="…">
    <label>Status <select class="ds-input" name="status" autofocus>…</select></label>
    <fieldset>
      <legend>Category</legend>
      <label class="ds-check"><input type="checkbox" name="category" value="cs.AI"><span>cs.AI</span></label>
      …
    </fieldset>
    …
    <fieldset>
      <legend>Settings</legend>
      <label>Threshold days <input class="ds-input" name="threshold" type="number"></label>
    </fieldset>
    <button class="ds-btn ds-btn-compact" type="submit">Apply</button>
  </form>
</div>
<script src="filter-panel.js" defer></script>
```

- `.ds-filter-button` — A compact secondary button with the filter icon (`list-filter`) and no chevron. `popovertarget` names its panel. While the panel is open the button shows its pressed state.
- `.ds-filter-value` — Optional, inside the button: what is applied, after the button's name. It shortens with an ellipsis when the row is narrow.
- `.ds-filter-panel` — The filter panel, a `popover` with `role="dialog"` and a name. Its background is the open button's background, and it attaches to the button's bottom edge. It holds a [compact form](forms.md#compact-form), one short column. `--ds-panel-width` sets its width.
- `<fieldset> with checkboxes` — A filter that takes several values, such as categories, is a fieldset of `.ds-check` checkboxes.
- `<fieldset> with the legend Settings` — A setting, such as threshold days, changes a calculation and is not a filter. It goes after the filters, in a fieldset of its own, and is not shown as a tag.
- `.ds-tag, .ds-tag-remove` — One tag for each applied filter, after the button. Its remove control is a link to the page without that filter. See [Tags](tags.md#complex-tags).
- `<a> Clear all` — A link to the page without filters, after the tags, while a filter is applied.
- `<script src="filter-panel.js" defer>` — Places the panel at the button's edge and keeps `aria-expanded` current. Without it the panel opens in the centre of the window.

## Rules

- **One set of filters for each set of data**, in the set's header bar. A filter applies to everything in the set.
- **A total ends the header bar only when the reader cannot see the whole set**: the set runs over more than one page, as in “1,669 submissions”, or the filters hide part of it, as in “3 of 120 holds”. A set with every item in view needs no total. When the controls do not fit on one line, the bar wraps and the total takes a line of its own.
- **Keep Apply when a change reloads the page.** See [Compact form](forms.md#compact-form).
- **After Apply, the page shows what was applied**: the server writes the chosen values back into the fields, and into the tags.
- **Sorting is not filtering.** A Sort by select can end the row of filters; a table sorts from its [column headers](tables.md#sortable-column-headers).
- **Every control sits inside its label.** A date range or a group of checkboxes is a fieldset with a legend.
- **The filter panel is a named dialog.** The button reports whether it is open with `aria-expanded`. Escape closes the panel and returns focus to the button.
- **Each remove control says what it removes**, in a `<span class="is-sr-only">`: “Remove the filter Status: On hold”.
- **On a touch screen every target is 44px.** Compact fields, compact buttons and remove controls have it built in.
