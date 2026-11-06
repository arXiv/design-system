---
page: layout-patterns.html
title: "Layouts"
summary: "The frame every page is built in: the page container and its widths, page zones, the sidebar, dividers and margin notes. How to arrange a page's content in that frame is on [Organize complex page content](../organize-content.html)."
stylesheet: design-system.css
components:
  - id: the-page-container
    title: "The page container"
    summary: "Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Page zones](#page-zones)."
    rules:
      - "**One width per page.** Prose, tables, demos, code and callouts share the reading column, so everything on a page has the same left and right edge. A page that needs a different width changes the width token; it does not add a second width."
      - "**Long-form reading is narrower.** An abstract, a paper body or an explanation read from start to finish targets a line of about 65 characters, set on the page, not on the paragraph."
      - "**Reference pages accept a longer line.** At 850px a line is about 109 characters. That suits short reference paragraphs and two-column layouts; it is not a reason to set long text that wide."
      - "**Few breakpoints, each for a change in structure.** Prefer a layout that needs no query, then a container query, then a media query. Breakpoints about text are in rem; breakpoints about fixed widths are in px. A threshold that CSS and JavaScript share is a custom property, read by the script with `getComputedStyle`."
      - "**Width decides where a control sits; the pointer decides its size.** A narrow window on a laptop still has a mouse. Give larger targets and tap-to-reveal where the pointer is coarse, never because the window is narrow."
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
      - "**A sidebar is for a page whose main content is about as long as the sidebar**, such as an abstract page beside its versions and citation. The main content gives up the sidebar's width and the gap, about 22rem."
      - "**When the main content needs its width or runs long, choose another home.** Charts, tables and wide pages need the width, and beside a long main column a sidebar leaves an empty column for most of the page. See [Where secondary content goes](../organize-content.html#where-secondary-content-goes)."
      - "**A sidebar starts level with the block it supports.** Above it, the page heading and any long one-line content, such as a paper's title and authors, use the full width: titles can be very long, and an author list reads better on one wide line."
  - id: dividers
    title: "Dividers"
    summary: "A rule between things. It belongs in the same conversation as the card, because both answer the same question and the answer is usually neither: this system groups with space first, and a line drawn where space would have done adds noise without adding meaning."
    classes:
      - name: "<hr>"
        does: "The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role=\"separator\"` for free."
      - name: ".ds-divider--tight"
        does: "Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning."
      - name: ".ds-divider--flush"
        does: "No margin at all; the caller owns the spacing."
      - name: ".ds-divider"
        does: "The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`."
      - name: ".ds-divider--vertical"
        does: "For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context."
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
  - id: page-zones
    title: "Page zones"
    group: "Modifiers"
    summary: "The default page background is white, and that is the color that primary page content sits on. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material. The zone is named for its role, because the ground changes in dark mode."
    classes:
      - name: ".ds-zone-secondary"
        does: "Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode."
      - name: ".ds-full"
        does: "On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own."
    rules:
      - "**Never a band across the main content.** Supporting material goes beside the opening, in a sidebar, or after all of the main content, in a closing band. A band between two parts of the main content interrupts the reading."
      - "**Dense pages do not use page zones**, and neither do the lighter pages of the same tool, so every page of the tool looks the same. On an admin tool or a data view, where the reader needs to find and act on content quickly, a tinted band pushes the main content too far down the page. Separate content with spacing and headings instead. The one exception is an opening band that holds a filter for the whole page, as in [Where controls go](../organize-content.html#where-controls-go)."
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

The frame every page is built in: the page container and its widths, page zones, the sidebar, dividers and margin notes. How to arrange a page's content in that frame is on [Organize complex page content](../organize-content.html).

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The page container

Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Page zones](#page-zones).

**Rule.** **One width per page.** Prose, tables, demos, code and callouts share the reading column, so everything on a page has the same left and right edge. A page that needs a different width changes the width token; it does not add a second width.

**Rule.** **Long-form reading is narrower.** An abstract, a paper body or an explanation read from start to finish targets a line of about 65 characters, set on the page, not on the paragraph.

**Rule.** **Reference pages accept a longer line.** At 850px a line is about 109 characters. That suits short reference paragraphs and two-column layouts; it is not a reason to set long text that wide.

**Rule.** **Few breakpoints, each for a change in structure.** Prefer a layout that needs no query, then a container query, then a media query. Breakpoints about text are in rem; breakpoints about fixed widths are in px. A threshold that CSS and JavaScript share is a custom property, read by the script with `getComputedStyle`.

**Rule.** **Width decides where a control sits; the pointer decides its size.** A narrow window on a laptop still has a mouse. Give larger targets and tap-to-reveal where the pointer is coarse, never because the window is narrow.

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

**Rule.** **A sidebar is for a page whose main content is about as long as the sidebar**, such as an abstract page beside its versions and citation. The main content gives up the sidebar's width and the gap, about 22rem.

**Rule.** **When the main content needs its width or runs long, choose another home.** Charts, tables and wide pages need the width, and beside a long main column a sidebar leaves an empty column for most of the page. See [Where secondary content goes](../organize-content.html#where-secondary-content-goes).

**Rule.** **A sidebar starts level with the block it supports.** Above it, the page heading and any long one-line content, such as a paper's title and authors, use the full width: titles can be very long, and an author list reads better on one wide line.

## Dividers

A rule between things. It belongs in the same conversation as the card, because both answer the same question and the answer is usually neither: this system groups with space first, and a line drawn where space would have done adds noise without adding meaning.

```html
<p>A section of content.</p>
<hr>
<p>The next section.</p>
<hr>
<p>And the one after it.</p>
```

```html
<p>An item in a group.</p>
<hr class="ds-divider ds-divider--tight">
<p>The next item in the same group.</p>
<hr class="ds-divider ds-divider--tight">
<p>And the one after it.</p>
```

```html
<div class="ds-btn-group">
<span>Search</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Submit</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Donate</span>
</div>
```

- `<hr>` — The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role="separator"` for free.
- `.ds-divider--tight` — Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning.
- `.ds-divider--flush` — No margin at all; the caller owns the spacing.
- `.ds-divider` — The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`.
- `.ds-divider--vertical` — For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context.

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

## Page zones  (Modifiers)

The default page background is white, and that is the color that primary page content sits on. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material. The zone is named for its role, because the ground changes in dark mode.

```html
<div class="ds-container">
  <div class="ds-full ds-zone-secondary">               <!-- tinted: introduces -->
    <header class="ds-page-header">…</header>
  </div>
  <section>…</section>                                  <!-- page ground: the thing itself -->
  <div class="ds-full ds-zone-secondary">               <!-- tinted: supports -->
    <section>…</section>
  </div>
</div>
```

- `.ds-zone-secondary` — Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode.
- `.ds-full` — On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own.

**Rule.** **Never a band across the main content.** Supporting material goes beside the opening, in a sidebar, or after all of the main content, in a closing band. A band between two parts of the main content interrupts the reading.

**Rule.** **Dense pages do not use page zones**, and neither do the lighter pages of the same tool, so every page of the tool looks the same. On an admin tool or a data view, where the reader needs to find and act on content quickly, a tinted band pushes the main content too far down the page. Separate content with spacing and headings instead. The one exception is an opening band that holds a filter for the whole page, as in [Where controls go](../organize-content.html#where-controls-go).

**Rule.** **Only a direct child can run full width.** `.ds-full` works on children of `.ds-container`; nested deeper it does nothing.

**Rule.** **Do not build a full-width band with negative margins and `100vw`.** `.ds-full` measures the container, so it fits exactly; see [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md), *Never size a full-bleed band in viewport units*.

## Wide page  (Modifiers)

A dense internal tool can use a wider page: 1080px instead of 850px. Use it for tables and filters that do not fit the standard width, not for prose.

## Rules

- **One main landmark.** Put the page's content in a single `<main>`. A page with two, or with none, gives a screen-reader user nothing to jump to.
- **Label every aside.** A sidebar is an `<aside>` with an `aria-label` that says what it holds, so it announces as a complementary landmark with a name, not as part of the article.
