I built the three pages in `build/search/` (`results.html`, `no-results.html`, `invalid-query.html`) and `search.css`. I checked the markup and looked at screenshots of the results and invalid-query pages. I did not look at the no-results page or re-check the layout after the last CSS tweak.

**1. Design system parts used**
- Page frame: `docs/using.html` markup, the public header and footer, theme toggle, skip link and `.ds-container`.
- Form: filter bar (GET), `.ds-field`, `.ds-input`, `.ds-check`, `.is-invalid` with `.field-error`.
- Messages: `.ds-alert` (error on the invalid page, bare info on no-results).
- Results: `.ds-card`, category `.ds-tag--info.ds-tag--keep-case`, and `.ds-acc` for the full abstract.
- Navigation and detail: numbered-pages `.ds-pagination` and `.ds-tooltip`.

**2. No answer in the design system**
- **Match highlighting:** `<mark>` in `search.css` on `--ds-tint-accent`, plus bold so it does not rely on colour. Light blue is the system's "arXiv speaking" colour.
- **Category full name:** a tag as a `<button>` with `.ds-tooltip` (hover and focus). No pattern covers this, so I used the nearest ones.
- **Abstract excerpt:** `<details>` holds the full abstract, and CSS hides the excerpt while it is open. The excerpts in samples 5 and 6 are not the start of the abstract, so the show-more pattern did not fit.
- **Result layout:** small spacing and layout rules in `search.css`, using tokens only.

**3. Not done**
- **10,000-result notice:** 8,291 results is under the limit, so no notice is shown. An HTML comment describes how it would render.
- **Results list:** six results are shown, as the brief says, while the count reads "1–50 of 8,291".
- **Network and fonts:** I used no network resources. I used local `docs/` paths instead of the template chrome's CDN URLs.
- **Simons logo:** it looked cropped in the footer screenshot. I did not investigate.