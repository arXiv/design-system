---
page: footer.html
title: "Site footer"
summary: "The universal arXiv public-page footer (`.ds-site-footer`): an acknowledgement line and the site's links. The transitional footer is the one in production now; the aspirational footer is the one arXiv's pages will move to."
stylesheet: design-system.css
components:
  - id: transitional-footer
    title: "Transitional footer (currently in production)"
    summary: "The footer in production now. A page includes it from `templates/` rather than copying its markup; the [templates README](../doc.html?src=templates/README.md) says how to install it and what each variable does. The example is a copy of the template's output."
    classes:
      - name: ".ds-site-footer"
        does: "The whole unit, on a `<footer>` element. Canvas ground with a hairline rule above it; hidden in print."
      - name: ".ds-site-footer-grid"
        does: "The row that holds the footer's columns. Columns that do not fit side by side wrap onto their own lines."
      - name: ".ds-site-footer-main"
        does: "The main column: the acknowledgement line, then the link row."
      - name: ".ack-member-inline"
        does: "The reader's member institution, after “member institutions”, when arXiv recognises the network they are on, such as a campus: the template's `member_institution`, which the [templates README](../doc.html?src=templates/README.md) describes. Empty for an anonymous reader. The aspirational footer below shows one."
      - name: ".ds-site-footer-links"
        does: "The link row, on a `<nav aria-label=\"Site navigation\">`. Plain `<a>` elements that wrap as a line; underlined on hover only."
      - name: ".ds-site-footer-sep"
        does: "The dot between two links. A `<span>` holding a middle dot, with `aria-hidden=\"true\"`."
      - name: "target=\"_blank\""
        does: "Only on the Operational Status link, which leaves arxiv.org. It takes `rel=\"noopener noreferrer\"` and a `.is-sr-only` “(opens in new tab)” inside the link text."
  - id: aspirational-footer
    title: "Aspirational footer (post-migration)"
    summary: "The footer arxiv.org will move to. It differs from the transitional footer in two ways: “all contributors” is a link, and the links are separated by space alone, with no dots."
    classes:
      - name: ".ds-site-footer-links"
        does: "As in the transitional footer, with no `.ds-site-footer-sep`: the links are separated by space alone."
rules:
  - "Wording has been carefully workshopped by leadership and must maintain an exact-match to the approved deployment."
  - "Which links the footer includes is set in [Design policies](../doc.html?src=docs/DESIGN-POLICIES.md)."
  - "Type sizes are rem so browser font-size overrides propagate (see [accessibility priorities](../doc.html?src=docs/accessibility-priorities.md))."
  - "The stylesheet hides the footer in print, so only the content prints, not the chrome."
  - "Adding an image or icon? Be sure it has a max-width or height so that it does not print or flash full size before styles are applied."
  - "**Use appropriate landmarks.** The unit is a real `<footer>`, and the link row is a `<nav aria-label=\"Site navigation\">`, so a screen reader user can jump to either one from a list of landmarks."
  - "**Hide the separators from assistive technology.** Every dot separator has `aria-hidden=\"true\"`; screen readers otherwise announce “middot” between every link."
  - "**Say when a link opens a new tab.** An external link (Operational Status) uses `target=\"_blank\"`, `rel=\"noopener noreferrer\"`, and a screen-reader-only “(opens in new tab)” notice inside the link text, so the link’s name says what will happen."
  - "**Keep the institution name inside the sentence.** The IP-matched institution is inserted after “member institutions”, with its comma, so the acknowledgement reads as one sentence. Omit the span when there is no match."
---

# Site footer

The universal arXiv public-page footer (`.ds-site-footer`): an acknowledgement line and the site's links. The transitional footer is the one in production now; the aspirational footer is the one arXiv's pages will move to.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Transitional footer (currently in production)

The footer in production now. A page includes it from `templates/` rather than copying its markup; the [templates README](../doc.html?src=templates/README.md) says how to install it and what each variable does. The example is a copy of the template's output.

```html
<footer class="ds-site-footer">
  <div class="ds-site-footer-grid">
    <div class="ds-site-footer-main">
      <div class="ds-site-footer-ack">
        We gratefully acknowledge support from our <a href="https://info.arxiv.org/about/major_funders.html"><strong>major funders</strong></a>,
        <a href="https://info.arxiv.org/about/ourmembers.html"><strong>member institutions</strong></a>,
        and all contributors.
      </div>
      <nav class="ds-site-footer-links" aria-label="Site navigation">
        <a href="https://info.arxiv.org/about">About</a> <span class="ds-site-footer-sep" aria-hidden="true">&middot;</span>
        <a href="https://info.arxiv.org/help">Help</a> <span class="ds-site-footer-sep" aria-hidden="true">&middot;</span>
        <a href="https://info.arxiv.org/help/contact.html">Contact</a> <span class="ds-site-footer-sep" aria-hidden="true">&middot;</span>
        <a href="https://info.arxiv.org/help/subscribe.html">Subscribe</a> <span class="ds-site-footer-sep" aria-hidden="true">&middot;</span>
        <a href="https://info.arxiv.org/help/license/index.html">Copyright</a> <span class="ds-site-footer-sep" aria-hidden="true">&middot;</span>
        <a href="https://info.arxiv.org/help/policies/privacy_policy.html">Privacy</a> <span class="ds-site-footer-sep" aria-hidden="true">&middot;</span>
        <a href="https://info.arxiv.org/help/web_accessibility.html">Accessibility</a> <span class="ds-site-footer-sep" aria-hidden="true">&middot;</span>
        <a href="https://status.arxiv.org/" target="_blank" rel="noopener noreferrer">Operational Status<span class="is-sr-only"> (opens in new tab)</span></a>
      </nav>
    </div>
  </div>
</footer>
```

- `.ds-site-footer` — The whole unit, on a `<footer>` element. Canvas ground with a hairline rule above it; hidden in print.
- `.ds-site-footer-grid` — The row that holds the footer's columns. Columns that do not fit side by side wrap onto their own lines.
- `.ds-site-footer-main` — The main column: the acknowledgement line, then the link row.
- `.ack-member-inline` — The reader's member institution, after “member institutions”, when arXiv recognises the network they are on, such as a campus: the template's `member_institution`, which the [templates README](../doc.html?src=templates/README.md) describes. Empty for an anonymous reader. The aspirational footer below shows one.
- `.ds-site-footer-links` — The link row, on a `<nav aria-label="Site navigation">`. Plain `<a>` elements that wrap as a line; underlined on hover only.
- `.ds-site-footer-sep` — The dot between two links. A `<span>` holding a middle dot, with `aria-hidden="true"`.
- `target="_blank"` — Only on the Operational Status link, which leaves arxiv.org. It takes `rel="noopener noreferrer"` and a `.is-sr-only` “(opens in new tab)” inside the link text.

## Aspirational footer (post-migration)

The footer arxiv.org will move to. It differs from the transitional footer in two ways: “all contributors” is a link, and the links are separated by space alone, with no dots.

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
        <a href="https://info.arxiv.org/about">About</a>
        <a href="https://info.arxiv.org/help">Help</a>
        <!-- … Contact, Subscribe, Copyright, Privacy, Accessibility, with no separators … -->
        <a href="https://status.arxiv.org/" target="_blank" rel="noopener noreferrer">Operational Status<span class="is-sr-only"> (opens in new tab)</span></a>
      </nav>
    </div>
  </div>
</footer>
```

- `.ds-site-footer-links` — As in the transitional footer, with no `.ds-site-footer-sep`: the links are separated by space alone.

## Rules

### Content

- Wording has been carefully workshopped by leadership and must maintain an exact-match to the approved deployment.
- Which links the footer includes is set in [Design policies](../doc.html?src=docs/DESIGN-POLICIES.md).

### Type and print

- Type sizes are rem so browser font-size overrides propagate (see [accessibility priorities](../doc.html?src=docs/accessibility-priorities.md)).
- The stylesheet hides the footer in print, so only the content prints, not the chrome.
- Adding an image or icon? Be sure it has a max-width or height so that it does not print or flash full size before styles are applied.

### Accessibility essentials

- **Use appropriate landmarks.** The unit is a real `<footer>`, and the link row is a `<nav aria-label="Site navigation">`, so a screen reader user can jump to either one from a list of landmarks.
- **Hide the separators from assistive technology.** Every dot separator has `aria-hidden="true"`; screen readers otherwise announce “middot” between every link.
- **Say when a link opens a new tab.** An external link (Operational Status) uses `target="_blank"`, `rel="noopener noreferrer"`, and a screen-reader-only “(opens in new tab)” notice inside the link text, so the link’s name says what will happen.
- **Keep the institution name inside the sentence.** The IP-matched institution is inserted after “member institutions”, with its comma, so the acknowledgement reads as one sentence. Omit the span when there is no match.
