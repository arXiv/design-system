I built the four pages in `build/reports/`: `sections.html`, `cs-activity.html`, `cs-submissions.html` and `staff.html`. I checked that the markup balances and that every class exists in the stylesheets. I did not open the pages in a browser, so I have not seen how they render. I wrote no `reports.css` because I needed no extra CSS. The only other file I made is the generator script in `/tmp/rptgen/`, outside the repo.

**1. Design system used**
- **Page frame:** `using.html`, internal-tools tier 1 and 2 with `.ds-internal`, the Admin Console header and the standard footer.
- **Navigation:** two-level secondary navigation (`.ds-subnav`, in-page views) with `aria-current`.
- **Layout and content:** link cards (`.ds-card--link`), data list, warning tag, accordion, compact form, filter bar and `.ds-btn-text` Refresh.
- **Table and paging:** sortable `.ds-table` headers as GET submit buttons, and `.ds-pagination--top` and `--bottom` with numbered pages.

**2. Where the design system had no answer or the brief conflicted**
- **Chart and figure placeholders:** I used a short `.ds-annotation` line, inside a `.ds-card` for the charts and totals, as `AGENTS.md` says for "no pattern".
- **Page 1 cards:** I left out the figures placeholder. `layout-patterns.html` says a card shows only a name, a count or an attention mark, and the figures belong on the page it opens.
- **Date range on page 3:** it is a `.ds-form--compact` row, not a second filter bar, because the Layout patterns rules say never two filter bars in a view.
- **Page 2 sort:** I used Sort by and Order selects with a Sort button. The segmented control is for decisions.
- **Breadcrumbs:** none, as the secondary navigation shows the place. "All sections" is a header link.

**3. Not done, or assumed**
- **Link targets:** I did not build the pages they point to. They are `{code}-activity.html` for the other subject groups, `physics-archives.html`, `staff-*.html`, and the other parts and views. The arXiv Check URL `https://check.arxiv.org/submissions/{id}` and the CSV address are my guesses.
- **Rows shown:** page 2 shows only cs.DB and cs.SY, as the brief asked. Page 3 shows the 10 sample rows under a "1–100 of 16,590" pager.
- **Held column:** a blank "Held" cell carries hidden "No" text for screen readers.
- **Greeting name:** "Shamsi" is copied from the docs example.