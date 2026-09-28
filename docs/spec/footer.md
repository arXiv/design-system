---
page: footer.html
title: "Site footer"
summary: "The universal arXiv public-page footer (`.ds-site-footer`). Note that the footer is still changing post-spinout as we figure out the best way to acknowledge major funders. The footer below is accurate as of 9/28/2026."
stylesheet: design-system.css
components:
  - id: the-footer
    title: "The footer"
    summary: "Rendered directly from `design-system.css`: the acknowledgement line followed by footer links. Funders have been removed from the right side for now."
    classes:
      - name: ".ds-site-footer"
        does: "The whole unit, on a `<footer>` element. Canvas ground with a hairline rule above it; hidden in print."
      - name: ".ds-site-footer-grid"
        does: "The row that holds the footer's columns. Columns that do not fit side by side wrap onto their own lines."
      - name: ".ds-site-footer-main"
        does: "The main column: the acknowledgement line, then the link row. Capped at 720px."
      - name: ".ds-site-footer-links"
        does: "The link row, on a `<nav aria-label=\"Site navigation\">`. Plain `<a>` elements that wrap as a line; underlined on hover only."
      - name: ".ds-site-footer-sep"
        does: "The dot between two links. A `<span>` holding a middle dot, with `aria-hidden=\"true\"`."
      - name: "target=\"_blank\""
        does: "Only on the Operational Status link, which leaves arxiv.org. It takes `rel=\"noopener noreferrer\"` and a `.is-sr-only` “(opens in new tab)” inside the link text."
  - id: the-acknowledgement-line
    title: "The acknowledgement line"
    summary: "The institutional mention after “member institutions” is an optional IP-matched insertion that will appear when a user accesses arXiv from campus or nearby. Omit when no match exists."
rules:
  - "Wording has been carefully workshopped by leadership and must maintain an exact-match to the approved deployment."
  - "Which links the footer carries is set in [Design policies](doc.html?src=docs/DESIGN-POLICIES.md)."
  - "Major funders were removed from the footer in September 2026. They may be added to the footer again in the future. Stay tuned."
  - "Type sizes are rem so browser font-size overrides propagate ([accessibility priorities](doc.html?src=docs/accessibility-priorities.md))."
  - "When implementing, use `@media print` on the footer so only the content prints, not the chrome."
  - "Adding an image or icon? Be sure it has a max-width or height so that it does not print or flash full size before styles are applied."
  - "**Use appropriate landmarks.** The unit is a real `<footer>`, and the link row is a `<nav aria-label=\"Site navigation\">`, so a screen reader user can jump to either one from a list of landmarks."
  - "**Hide the separators from assistive technology.** Every dot separator carries `aria-hidden=\"true\"`; screen readers otherwise announce “middot” between every link."
  - "**Say when a link opens a new tab.** An external link (Operational Status) uses `target=\"_blank\"`, `rel=\"noopener noreferrer\"`, and a screen-reader-only “(opens in new tab)” notice inside the link text, so the link’s name says what will happen."
  - "**Keep the institution inside the sentence.** The IP-matched institution is inserted after “member institutions”, with its comma, so the acknowledgement reads as one sentence. Omit the span when there is no match."
---

# Site footer

The universal arXiv public-page footer (`.ds-site-footer`). Note that the footer is still changing post-spinout as we figure out the best way to acknowledge major funders. The footer below is accurate as of 9/28/2026.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The footer

Rendered directly from `design-system.css`: the acknowledgement line followed by footer links. Funders have been removed from the right side for now.

```html
<footer class="ds-site-footer">
  <div class="ds-site-footer-grid">
    <div class="ds-site-footer-main">
      <div class="ds-site-footer-ack">
        We gratefully acknowledge support from our <a href="#"><strong>major funders</strong></a>,
        <a href="#"><strong>member institutions</strong></a><span class="ack-member-inline">,
        <strong>Rheinisch-Westfälische Technische Hochschule Aachen</strong></span>,
        and <a href="#">all contributors</a>.
      </div>
      <nav class="ds-site-footer-links" aria-label="Site navigation">
        <a href="https://info.arxiv.org/about">About</a> <span class="ds-site-footer-sep" aria-hidden="true">·</span>
        <a href="https://info.arxiv.org/help">Help</a> <span class="ds-site-footer-sep" aria-hidden="true">·</span>
        <!-- … Contact, Subscribe, Copyright, Privacy, Accessibility, each followed by a separator … -->
        <a href="https://status.arxiv.org/" target="_blank" rel="noopener noreferrer">Operational Status<span class="is-sr-only"> (opens in new tab)</span></a>
      </nav>
    </div>
  </div>
</footer>
```

- `.ds-site-footer` — The whole unit, on a `<footer>` element. Canvas ground with a hairline rule above it; hidden in print.
- `.ds-site-footer-grid` — The row that holds the footer's columns. Columns that do not fit side by side wrap onto their own lines.
- `.ds-site-footer-main` — The main column: the acknowledgement line, then the link row. Capped at 720px.
- `.ds-site-footer-links` — The link row, on a `<nav aria-label="Site navigation">`. Plain `<a>` elements that wrap as a line; underlined on hover only.
- `.ds-site-footer-sep` — The dot between two links. A `<span>` holding a middle dot, with `aria-hidden="true"`.
- `target="_blank"` — Only on the Operational Status link, which leaves arxiv.org. It takes `rel="noopener noreferrer"` and a `.is-sr-only` “(opens in new tab)” inside the link text.

## The acknowledgement line

The institutional mention after “member institutions” is an optional IP-matched insertion that will appear when a user accesses arXiv from campus or nearby. Omit when no match exists.

## Rules

- Wording has been carefully workshopped by leadership and must maintain an exact-match to the approved deployment.
- Which links the footer carries is set in [Design policies](doc.html?src=docs/DESIGN-POLICIES.md).
- Major funders were removed from the footer in September 2026. They may be added to the footer again in the future. Stay tuned.
- Type sizes are rem so browser font-size overrides propagate ([accessibility priorities](doc.html?src=docs/accessibility-priorities.md)).
- When implementing, use `@media print` on the footer so only the content prints, not the chrome.
- Adding an image or icon? Be sure it has a max-width or height so that it does not print or flash full size before styles are applied.
- **Use appropriate landmarks.** The unit is a real `<footer>`, and the link row is a `<nav aria-label="Site navigation">`, so a screen reader user can jump to either one from a list of landmarks.
- **Hide the separators from assistive technology.** Every dot separator carries `aria-hidden="true"`; screen readers otherwise announce “middot” between every link.
- **Say when a link opens a new tab.** An external link (Operational Status) uses `target="_blank"`, `rel="noopener noreferrer"`, and a screen-reader-only “(opens in new tab)” notice inside the link text, so the link’s name says what will happen.
- **Keep the institution inside the sentence.** The IP-matched institution is inserted after “member institutions”, with its comma, so the acknowledgement reads as one sentence. Omit the span when there is no match.
