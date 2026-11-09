---
page: layouts.html
title: "Layouts"
summary: "How to use the page container and other page zones. For guidance on where to put content see the patterns under [Organize complex page content](organize-content.md)."
stylesheet: design-system.css
components:
  - id: the-page-container
    title: "The page container"
    summary: "Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Full-width bands](#full-width-bands)."
    notes:
      - "Research on optimal line width:[Dyson and Haselgrove (2001)](https://doi.org/10.1006/ijhc.2001.0458)[Nanavati and Bias (2005)](https://journals.uc.edu/index.php/vl/article/view/5765)"
    rules:
      - "**One width per page.** Everything on a page has the same left and right edge. A page that needs a different width changes the width token; it does not add a second width."
      - "**Long-form reading is narrower.** For an abstract, a full HTML paper, or wherever we need to support an optimal reading experience, we target a line width of about 65 characters. This is narrower than the standard content width."
  - id: sidebar
    title: "Sidebar"
    summary: "A sidebar sits to the right of the main column and contains supplementary content. If the content is secondary, distinct from the main content, and it is important that it not be pushed far down the page, then a sidebar is appropriate."
    classes:
      - name: ".ds-sidebar"
        does: "On an `<aside>` with an `aria-label` (see Accessibility essentials). Its parent becomes the two-column layout, with the main content taking the spare width, the sidebar 17rem wide, and `--ds-space-section` between them. A border frames it, with 8px inside (`--ds-space-2`), and a line separates its blocks, 16px apart (`--ds-space-4`). Its text is 13px. Nothing in it is sticky."
      - name: "<aside>"
        does: "The sidebar comes after the main content in the markup. When the two no longer fit side by side, the sidebar wraps below the content at full width, 24px below it (`--ds-space-6`), and a screen reader meets the article first."
      - name: ".ds-acc"
        does: "An accordion inside the sidebar is the same ruled accordion as anywhere else, a step smaller to match the sidebar's text, and single-column for the narrow measure. Several in a row go in a `.ds-acc-stack`. No extra class."
    rules:
      - "**Use a sidebar next to content that will have a similar height as the sidebar.**"
      - "**When the main content needs the width or is much longer or shorter, use a different content organization pattern.** See [Where secondary content goes](organize-content.md#where-secondary-content-goes)."
      - "**The sidebar sits next to and starts level with a text block.** To aid readability, put page headings and other one-line content above the sidebar so they have the width they need to wrap."
  - id: marginalia
    title: "Marginalia and gutter space"
    summary: "At wide screen widths, our max content width leaves enough gutter space on the sides for marginalia. A short note beside the block it belongs to is appropriate for annotation-style content. At narrower widths, it is hidden in an info icon in the block’s top-right corner. Try it by widening and narrowing your screen."
    classes:
      - name: ".ds-marginalia"
        does: "The note, a `<details>`. Its first child in the block, so it is read before the thing it annotates. The block supplies `position: relative`; `.ds-card` already does."
      - name: ".ds-marginalia-body"
        does: "The text, with `.ds-annotation` for the voice. In the margin it has no chrome; folded, it opens as a small panel under the mark."
      - name: ".is-sr-only"
        does: "Required on the mark. The icon is `aria-hidden`, so without it the control announces as nothing."
    notes:
      - "A margin note is one or two sentences. Anything longer belongs in the main content."
    rules:
      - "**No JavaScript required.** Even the info links use a native disclosure."
      - "**The marginalia appear at 1314px width.** The page width plus a note and its gaps on each side. Below that width, marginal notes are hidden behind an info icon."
      - "**A note should never contain required information.** A reader on a narrow screen may never open or see it, so annotations must contain only optional content."
  - id: full-width-bands
    title: "Full-width bands"
    group: "Modifiers"
    summary: "`.ds-full` lets a direct child of the container run edge to edge, while its own content lines up with the reading column. It adds no background color of its own."
  - id: secondary-zones
    title: "Secondary zones"
    group: "Modifiers"
    summary: "The default page background is white, and that is the color that primary page content sits on. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material."
    classes:
      - name: ".ds-page-header"
        does: "The page title, an `<h1>`, and its introduction, a plain paragraph with no class of its own. These docs pages mark theirs `.ds-section-desc`, which only flags a summary for the docs' digests; a product page leaves it out."
      - name: ".ds-zone-secondary"
        does: "Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode."
      - name: ".ds-full"
        does: "On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own."
    rules:
      - "**The opening band holds the page title and an introduction of one to five sentences**, never the title alone. A title on its own in a tinted band looks unfinished and takes height the reader does not need. Without an introduction, a page has no opening band, unless its [set](organize-content.md#rules) uses one; then it needs an introduction."
      - "**A contents bar hangs from the opening band's bottom edge.** So a page with a [contents bar](navigation.md#toc-bar) has an opening band, and an introduction in it. A paper is the exception: its contents bar carries the paper's tools and sits under the site header ([The TOC bar on a paper](papers.md#paper-toc-bar))."
      - "**Never a band across the main content.** A band between two parts of the main content interrupts the reading."
      - "**On an admin tool or a data view**, where the reader needs to find and act on content quickly, a tinted band pushes the main content too far down the page. Separate content with spacing and headings instead. The one exception is an opening band that holds a filter for the whole page, as in [Where controls go](organize-content.md#where-controls-go)."
      - "**Only a direct child can run full width.** `.ds-full` works on children of `.ds-container`; nested deeper it does nothing."
      - "**Do not build a full-width band with negative margins and `100vw`.** `.ds-full` measures the container, so it fits exactly; see [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md), *Never size a full-bleed band in viewport units*."
  - id: wide-page
    title: "Wide page"
    group: "Modifiers"
    summary: "A dense internal tool can use a wider page: 1080px instead of 850px. Use it for tables and filters that do not fit the standard width, not for prose."
rules:
  - "**One main landmark.** Put the page's content in a single `<main>`. A page with two, or with none, gives a screen-reader user nothing to jump to."
  - "**Label every aside.** A sidebar is an `<aside>` with an `aria-label` that says what it holds, so it announces as a complementary landmark with a name, not as part of the article."
---

# Layouts

How to use the page container and other page zones. For guidance on where to put content see the patterns under [Organize complex page content](organize-content.md).

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The page container

Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Full-width bands](#full-width-bands).

> Research on optimal line width:[Dyson and Haselgrove (2001)](https://doi.org/10.1006/ijhc.2001.0458)[Nanavati and Bias (2005)](https://journals.uc.edu/index.php/vl/article/view/5765)

**Rule.** **One width per page.** Everything on a page has the same left and right edge. A page that needs a different width changes the width token; it does not add a second width.

**Rule.** **Long-form reading is narrower.** For an abstract, a full HTML paper, or wherever we need to support an optimal reading experience, we target a line width of about 65 characters. This is narrower than the standard content width.

## Sidebar

A sidebar sits to the right of the main column and contains supplementary content. If the content is secondary, distinct from the main content, and it is important that it not be pushed far down the page, then a sidebar is appropriate.

```html
<div>
<article>…</article>
<aside class="ds-sidebar" aria-label="Paper details">
  <div class="ds-acc-stack">
    <details class="ds-acc" open>
      <summary>Versions</summary>
      <div class="ds-acc-body">
        <dl>
          <dt>v3 · current</dt><dd>24 Apr 2026</dd>
          <dt>v2</dt><dd><a href="#">2 Mar 2026</a></dd>
        </dl>
      </div>
    </details>
    <details class="ds-acc">
      <summary>Paper information</summary>
      <div class="ds-acc-body">…</div>
    </details>
  </div>
</aside>
</div>
```

- `.ds-sidebar` — On an `<aside>` with an `aria-label` (see Accessibility essentials). Its parent becomes the two-column layout, with the main content taking the spare width, the sidebar 17rem wide, and `--ds-space-section` between them. A border frames it, with 8px inside (`--ds-space-2`), and a line separates its blocks, 16px apart (`--ds-space-4`). Its text is 13px. Nothing in it is sticky.
- `<aside>` — The sidebar comes after the main content in the markup. When the two no longer fit side by side, the sidebar wraps below the content at full width, 24px below it (`--ds-space-6`), and a screen reader meets the article first.
- `.ds-acc` — An accordion inside the sidebar is the same ruled accordion as anywhere else, a step smaller to match the sidebar's text, and single-column for the narrow measure. Several in a row go in a `.ds-acc-stack`. No extra class.

**Rule.** **Use a sidebar next to content that will have a similar height as the sidebar.**

**Rule.** **When the main content needs the width or is much longer or shorter, use a different content organization pattern.** See [Where secondary content goes](organize-content.md#where-secondary-content-goes).

**Rule.** **The sidebar sits next to and starts level with a text block.** To aid readability, put page headings and other one-line content above the sidebar so they have the width they need to wrap.

## Marginalia and gutter space

At wide screen widths, our max content width leaves enough gutter space on the sides for marginalia. A short note beside the block it belongs to is appropriate for annotation-style content. At narrower widths, it is hidden in an info icon in the block’s top-right corner. Try it by widening and narrowing your screen.

```html
<div class="ds-card">
<details class="ds-marginalia">
  <summary><svg aria-hidden="true">…</svg><span class="is-sr-only">Note</span></summary>
  <p class="ds-marginalia-body ds-annotation">The note.</p>
</details>
…
</div>
```

- `.ds-marginalia` — The note, a `<details>`. Its first child in the block, so it is read before the thing it annotates. The block supplies `position: relative`; `.ds-card` already does.
- `.ds-marginalia-body` — The text, with `.ds-annotation` for the voice. In the margin it has no chrome; folded, it opens as a small panel under the mark.
- `.is-sr-only` — Required on the mark. The icon is `aria-hidden`, so without it the control announces as nothing.

> A margin note is one or two sentences. Anything longer belongs in the main content.

**Rule.** **No JavaScript required.** Even the info links use a native disclosure.

**Rule.** **The marginalia appear at 1314px width.** The page width plus a note and its gaps on each side. Below that width, marginal notes are hidden behind an info icon.

**Rule.** **A note should never contain required information.** A reader on a narrow screen may never open or see it, so annotations must contain only optional content.

## Full-width bands  (Modifiers)

`.ds-full` lets a direct child of the container run edge to edge, while its own content lines up with the reading column. It adds no background color of its own.

## Secondary zones  (Modifiers)

The default page background is white, and that is the color that primary page content sits on. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material.

```html
<div class="ds-container">
  <div class="ds-full ds-zone-secondary">               <!-- tinted: introduces -->
    <header class="ds-page-header">
      <h1>Page title</h1>
      <p>One to five sentences that say what the page is for.</p>
    </header>
  </div>
  <section>…</section>                                  <!-- page ground: the thing itself -->
  <div class="ds-full ds-zone-secondary">               <!-- tinted: supports -->
    <section>…</section>
  </div>
</div>
```

- `.ds-page-header` — The page title, an `<h1>`, and its introduction, a plain paragraph with no class of its own. These docs pages mark theirs `.ds-section-desc`, which only flags a summary for the docs' digests; a product page leaves it out.
- `.ds-zone-secondary` — Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode.
- `.ds-full` — On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own.

**Rule.** **The opening band holds the page title and an introduction of one to five sentences**, never the title alone. A title on its own in a tinted band looks unfinished and takes height the reader does not need. Without an introduction, a page has no opening band, unless its [set](organize-content.md#rules) uses one; then it needs an introduction.

**Rule.** **A contents bar hangs from the opening band's bottom edge.** So a page with a [contents bar](navigation.md#toc-bar) has an opening band, and an introduction in it. A paper is the exception: its contents bar carries the paper's tools and sits under the site header ([The TOC bar on a paper](papers.md#paper-toc-bar)).

**Rule.** **Never a band across the main content.** A band between two parts of the main content interrupts the reading.

**Rule.** **On an admin tool or a data view**, where the reader needs to find and act on content quickly, a tinted band pushes the main content too far down the page. Separate content with spacing and headings instead. The one exception is an opening band that holds a filter for the whole page, as in [Where controls go](organize-content.md#where-controls-go).

**Rule.** **Only a direct child can run full width.** `.ds-full` works on children of `.ds-container`; nested deeper it does nothing.

**Rule.** **Do not build a full-width band with negative margins and `100vw`.** `.ds-full` measures the container, so it fits exactly; see [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md), *Never size a full-bleed band in viewport units*.

## Wide page  (Modifiers)

A dense internal tool can use a wider page: 1080px instead of 850px. Use it for tables and filters that do not fit the standard width, not for prose.

## Rules

- **One main landmark.** Put the page's content in a single `<main>`. A page with two, or with none, gives a screen-reader user nothing to jump to.
- **Label every aside.** A sidebar is an `<aside>` with an `aria-label` that says what it holds, so it announces as a complementary landmark with a name, not as part of the article.
