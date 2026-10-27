---
page: search.html
title: "Search"
summary: "A search page contains many components and elements documented elsewhere. This page is about how to put them together, the hierarchy of content, and other design considerations when building a search form and results page."
stylesheet: design-system.css
components:
  - id: before-a-search
    title: "Before a search"
    summary: "Before a search, the form is the primary content so it sits on the default page ground (white in light mode). Tips for searching are secondary content and sit in a tinted band below it."
    classes:
      - name: "<h1>"
        does: "The page heading. The demo here uses a smaller heading because it sits inside this page."
      - name: ".ds-form--compact"
        does: "The search form. See [Compact form](forms.md#compact-form)."
      - name: ".ds-full.ds-zone-secondary"
        does: "The help, in a tinted band. See [Page zones](layout-patterns.md#page-zones)."
  - id: after-a-search
    title: "After a search"
    summary: "After a search, the form stays where it was, on the page ground. A heading names the query, and tinted bars with the range and page numbers bookend the results."
    classes:
      - name: "<h1>"
        does: "The page heading. The demo here uses smaller headings because it sits inside this page."
      - name: ".ds-form--compact"
        does: "The search form, on the page ground before and after a search."
      - name: "<label> with a select"
        does: "The settings for the results, such as order and results per page, as compact selects beside the other options under the search row. A link to another page, such as Advanced search, takes the end of that line."
      - name: "<section>"
        does: "The results: the heading, the notice, the two bars and the list are one region of the page, named by the heading. Inside it, the bars keep the list's own spacing."
      - name: "<h2>"
        does: "The results heading, “Results for” and the query. It gives no count: the count is in the bar below it."
      - name: ".ds-alert"
        does: "A message about the whole set of results, such as a limit on how many can be reached. It goes above the page numbers."
      - name: ".ds-pagination--top, .ds-pagination--bottom"
        does: "The range and page numbers above and below the results, in tinted bars. See [Numbered pages](pager.md#numbered-pages)."
      - name: "<section aria-labelledby> for the results"
        does: "Whatever the search finds. A paper is shown as on [Papers](papers.md#a-paper-in-a-list); another kind of record has its own pattern."
    rules:
      - "Search shows the first 10,000 results. To see the rest, narrow the search."
rules:
  - "**The search form stays on the page ground**, before and after a search."
  - "**A heading names the results:** “Results for” and the query, with no count."
  - "**Settings for the results go with the search, never in the pager.** Choose a default for each; the reader changes it under the search row."
  - "**An alert goes at the top of the part of the page it is about.** A message about the query goes below the page heading, above the form; a message about the results goes below the results heading. See [Alerts](alerts.md)."
  - "**The range and page numbers belong to the results.** They sit in tinted bars above and below the results, under the results heading."
  - "**Matched words are marked** with `<mark>`. See [Search-matched words](typography.md#matched-words)."
  - "**No results is a message, not an empty page.** An info alert where the results would be says what was searched for, and the help for searching follows it."
  - "**Name the form.** The search form takes `role=\"search\"` and an `aria-label`."
  - "**Say what was found in the page title.** The `<title>` names the query and the number of results, so a screen reader announces both when the page loads."
---

# Search

A search page contains many components and elements documented elsewhere. This page is about how to put them together, the hierarchy of content, and other design considerations when building a search form and results page.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Before a search

Before a search, the form is the primary content so it sits on the default page ground (white in light mode). Tips for searching are secondary content and sit in a tinted band below it.

```html
<div class="ds-container">
  <h1>Search</h1>
  <form class="ds-form--compact" method="get" action="search.html" role="search" aria-label="Search arXiv">
    <div class="ds-input-group">
      <label class="is-sr-only" for="sq1">Search term</label>
      <input class="ds-input" id="sq1" name="query" type="search" value="">
      <label class="is-sr-only" for="sf1">Field to search</label>
      <select class="ds-input" id="sf1" name="searchtype"><option>All fields</option><option>Title</option><option>Author(s)</option><option>Abstract</option></select>
    </div>
    <button class="ds-btn ds-btn-primary" type="submit">Search</button>
    <label class="ds-check"><input type="checkbox" name="abstracts" value="show" checked><span>Show abstracts</span></label>
    <a href="search.html">Advanced search</a>
  </form>
  <div class="ds-full ds-zone-secondary">
    <p><strong>Search tips</strong></p>
    <p>How to search by author, by category, with wildcards and phrases.</p>
  </div>
</div>
```

- `<h1>` — The page heading. The demo here uses a smaller heading because it sits inside this page.
- `.ds-form--compact` — The search form. See [Compact form](forms.md#compact-form).
- `.ds-full.ds-zone-secondary` — The help, in a tinted band. See [Page zones](layout-patterns.md#page-zones).

## After a search

After a search, the form stays where it was, on the page ground. A heading names the query, and tinted bars with the range and page numbers bookend the results.

```html
<div class="ds-container">
  <h1>Search</h1>
  <form class="ds-form--compact" method="get" action="search.html" role="search" aria-label="Search arXiv">
    <div class="ds-input-group">
    <label class="is-sr-only" for="sq2">Search term</label>
    <input class="ds-input" id="sq2" name="query" type="search" value="lensing">
    <label class="is-sr-only" for="sf2">Field to search</label>
    <select class="ds-input" id="sf2" name="searchtype"><option>All fields</option><option>Title</option><option>Author(s)</option><option>Abstract</option></select>
    </div>
    <button class="ds-btn ds-btn-primary" type="submit">Search</button>
    <label class="ds-check"><input type="checkbox" name="abstracts" value="show" checked><span>Show abstracts</span></label>
    <label>Sort by <select class="ds-input" name="order"><option>Newest announced</option><option>Relevance</option></select></label>
    <label>Per page <select class="ds-input" name="size"><option>25</option><option selected>50</option><option>100</option></select></label>
    <a href="search.html">Advanced search</a>
  </form>
  <section aria-labelledby="results">
    <h2 id="results">Results for “lensing”</h2>
    <div class="ds-alert" role="status"><p>Search shows the first 10,000 results. To see the rest, narrow the search.</p></div>
    <nav class="ds-pagination ds-pagination--top" aria-label="Search results pages">
      <span class="ds-pagination-position">1–50 of 18,659 results</span>
      <a class="ds-btn ds-btn-text is-disabled" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
      <ol class="ds-pagination-pages">
      <li><a href="?page=1" aria-current="page"><span class="is-sr-only">Page </span>1</a></li>
      <li><a href="?page=2"><span class="is-sr-only">Page </span>2</a></li>
      <li><a href="?page=3"><span class="is-sr-only">Page </span>3</a></li>
      <li><a href="?page=4"><span class="is-sr-only">Page </span>4</a></li>
      <li><a href="?page=5"><span class="is-sr-only">Page </span>5</a></li>
      <li>…</li>
      <li><a href="?page=374"><span class="is-sr-only">Page </span>374</a></li>
      </ol>
      <a class="ds-btn ds-btn-text" href="?page=2"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
    </nav>
    <ol class="demo-list">
      <li>The first result</li>
      <li>The last result on this page</li>
    </ol>
    <nav class="ds-pagination ds-pagination--bottom" aria-label="Search results pages, below the list">
      <span class="ds-pagination-position">1–50 of 18,659 results</span>
      <a class="ds-btn ds-btn-text is-disabled" aria-disabled="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg> <span class="ds-pagination-label">Previous</span></a>
      <ol class="ds-pagination-pages">
      <li><a href="?page=1" aria-current="page"><span class="is-sr-only">Page </span>1</a></li>
      <li><a href="?page=2"><span class="is-sr-only">Page </span>2</a></li>
      <li><a href="?page=3"><span class="is-sr-only">Page </span>3</a></li>
      <li><a href="?page=4"><span class="is-sr-only">Page </span>4</a></li>
      <li><a href="?page=5"><span class="is-sr-only">Page </span>5</a></li>
      <li>…</li>
      <li><a href="?page=374"><span class="is-sr-only">Page </span>374</a></li>
      </ol>
      <a class="ds-btn ds-btn-text" href="?page=2"><span class="ds-pagination-label">Next</span> <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg></a>
    </nav>
  </section>
</div>
```

- `<h1>` — The page heading. The demo here uses smaller headings because it sits inside this page.
- `.ds-form--compact` — The search form, on the page ground before and after a search.
- `<label> with a select` — The settings for the results, such as order and results per page, as compact selects beside the other options under the search row. A link to another page, such as Advanced search, takes the end of that line.
- `<section>` — The results: the heading, the notice, the two bars and the list are one region of the page, named by the heading. Inside it, the bars keep the list's own spacing.
- `<h2>` — The results heading, “Results for” and the query. It gives no count: the count is in the bar below it.
- `.ds-alert` — A message about the whole set of results, such as a limit on how many can be reached. It goes above the page numbers.
- `.ds-pagination--top, .ds-pagination--bottom` — The range and page numbers above and below the results, in tinted bars. See [Numbered pages](pager.md#numbered-pages).
- `<section aria-labelledby> for the results` — Whatever the search finds. A paper is shown as on [Papers](papers.md#a-paper-in-a-list); another kind of record has its own pattern.

**Rule.** Search shows the first 10,000 results. To see the rest, narrow the search.

## Rules

- **The search form stays on the page ground**, before and after a search.
- **A heading names the results:** “Results for” and the query, with no count.
- **Settings for the results go with the search, never in the pager.** Choose a default for each; the reader changes it under the search row.
- **An alert goes at the top of the part of the page it is about.** A message about the query goes below the page heading, above the form; a message about the results goes below the results heading. See [Alerts](alerts.md).
- **The range and page numbers belong to the results.** They sit in tinted bars above and below the results, under the results heading.
- **Matched words are marked** with `<mark>`. See [Search-matched words](typography.md#matched-words).
- **No results is a message, not an empty page.** An info alert where the results would be says what was searched for, and the help for searching follows it.
- **Name the form.** The search form takes `role="search"` and an `aria-label`.
- **Say what was found in the page title.** The `<title>` names the query and the number of results, so a screen reader announces both when the page loads.
