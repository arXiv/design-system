---
page: using.html
title: "Using the design system"
summary: "This page shares how to get started with the arXiv Design System: basic markup, which files to link to, in what order, and a handful of things to avoid. If you are an AI assistant, `AGENTS.md` at the repository root holds the file map in a form you can route from."
stylesheet: design-system.css
components:
  - id: core-linked-files
    title: "Core linked files"
    summary: "Every core file you need to include in your repo, and in what order."
    rules:
      - "**`fonts.css`.** Include this file before `design-system.css`. The font file declares the faces, the stylesheet names them. Either order renders but we have chosen this way for consistency."
      - "**`design-system.css`.** The foundational tier 1 stylesheet. When working on internal pages, there is a tier 2 stylesheet that builds on this one."
      - "**`theme.js`.** The foundational tier 1 JavaScript. Internal tools add no JavaScript of their own."
      - "**`toc.js`, optional.** Add it when the page has a TOC bar. The bar itself is tier 1; the script closes the menu after a choice and names the section the reader is in. See [TOC bar](navigation.md#toc-bar)."
      - "**`copy.js`, optional.** Add it when the page shows code a reader might take away, or has any other copy button. It needs no markup for code: it finds every `<pre>` on the page and puts a copy button on each one. Other copy buttons are on [Show that something was copied](action-feedback.md)."
      - "**`show-more.js`, optional.** Add it when the page has a Show more, such as the authors after the first eight. The button and the tail are tier 1; the script hides the tail, shows the button and opens and closes the tail. See [Show more](progressive-disclosure.md#show-more)."
      - "**`cite.js`, optional.** Add it, with `copy.js`, when the page has a paper's Cite. The script shows the format chosen in the select and opens the full citation. See [Displaying paper actions and full metadata](papers.md#the-sidebar)."
  - id: basic-page-markup
    title: "Basic page markup"
    summary: "This is all you need for a public arXiv page. Copy it and follow the comments."
    rules:
      - "**`class=\"ds-page\"` on the body is not optional.** A page without it gets components on unstyled ground. The foundation hangs on the class rather than on `<body>` so that a page which is not on the design system can link the stylesheet, for its header and footer, without its own body styles being overwritten."
  - id: internal-tools
    title: "Internal tools"
    group: "Building on the foundation"
    summary: "When building internal tools like arXiv Check or Admin Console pages, one class is added to `<html>` and a tier 2 stylesheet is added to the `<head>` section, in this order."
    rules:
      - "internal-tools.css does not work on its own: `internal-tools.css` is **not** a standalone stylesheet. It is a lightweight file that holds only the special styles or overrides that are specific to internal tools. Load it on its own and you get no foundation at all."
      - "**The accent color defines internal pages.** Access Lime is highly differentiated from the public site's Open Blue and clearly signals that you are in a different environment."
      - "**All you need is a parent class.** `.ds-internal` re-points `--ds-accent` and its family to Access Lime, and every component inside it that reaches for the accent follows without being told. It works on any parent, so a page that shows both surfaces puts it on a wrapper instead of on `<html>`. There is no second copy of the button, the tag or the switch inside the tier 2 stylesheet: it is not needed. Just a handful of new styles and overrides, and that class on the wrapper, are enough."
      - "**Internal tools are compact.** `.ds-internal` also sets less padding inside table cells and cards, through the density tokens (`--ds-cell-padding`, `--ds-card-padding`), so a dense screen holds more. There is no compact class: the density comes with the surface."
      - "**Never copy a component into the tier 2 stylesheet to restyle it.** If it needs to look different on your surface, what you need is a token change, not a second copy. A component that exists twice creates drift and lots of sad devs."
      - "**Maintain the accent even on links to the other environment.** Are you linking to the internal tools from a public page, or vice versa? Maintain the accent color and let the button label clearly tell the user where it will take them. See [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md)."
  - id: container-options
    title: "Container options"
    group: "Building on the foundation"
    summary: "`.ds-container` is a grid with various options for managing section layout."
    rules:
      - "**Sections.** The container's direct children are `<section>` elements, and the container sets the gap between them. Do not add top or bottom margins to sections, the container already does."
      - "**Full width.** A coloured band that runs edge to edge gets `.ds-full` with a zone class (see [Secondary zones](layouts.md#secondary-zones)). Do not add negative margins or use viewport units for placement. Using a calculation like `calc(-50vw + 50%)` overhangs the section band and causes the page to scroll sideways in some environments."
      - "**Page width.** Width comes from `--ds-width-page` and `--ds-gutter`. Need to change the page width? Repoint one of the tokens, do not add a second width beside it."
  - id: combining-components
    title: "Combining components"
    group: "Building on the foundation"
    summary: "Most areas of a page can be built by putting existing components together. Look for a combination before inventing a component."
    rules:
      - "**Examples in these docs.** The [search form](search.md) with the results' settings under it; a [table](tables.md) with its toolbar of filters and bulk actions; a [sidebar](layouts.md#sidebar) of accordions; a [card that links](cards.md#cards-that-link), with a tag; [secondary navigation with a compact filter bar](navigation.md#two-levels-of-navigation)."
      - "**Each component works inside another.** Use a component's documented markup unchanged inside the other."
      - "**A new class is the last step.** If a combination needs CSS, it is a rule on the outer component about what it can hold, written in the design system. Ask before adding a component."
rules:
  - "**`theme.js` is not deferred.** The script is deliberately not deferred because it writes the reader's theme onto `<html>` before the first paint. If we added `defer` then the page will render light first, and then flip if the reader chose dark mode in their system. Many readers choose dark mode because light mode is less legible or hurts their eyes and we want to honor that."
  - "**Every section starts with a heading.** Headings provide important navigation structure for screen reader users so a `<section>` without one is hard to find."
  - "**Naming sections (optional).** A name on the section itself (`aria-labelledby` pointing at the heading) is optional, but useful for a section that a reader would want to jump to directly. Use your discretion. Every named section becomes an entry in the landmark list."
  - "**Write the name arXiv so that screen readers say “archive”.** A screen reader reads the Xiv in our name as a Roman numeral. We can take a few steps to fix this: For an image like the logo, add alt text that says “archive”. Where the name is typed this markup will be pronounced correctly: `<span aria-hidden=\"true\">arXiv</span><span class=\"is-sr-only\">archive</span>`. When arXiv's name appears in a paragraph of text that is likely to be copied (ie: citations) we unfortunately must keep it as plain text and live with the screen reader mis-pronunciation. This is because the hidden word is copied along with the visible one and would break every pasted citation."
  - "For an image like the logo, add alt text that says “archive”."
  - "Where the name is typed this markup will be pronounced correctly: `<span aria-hidden=\"true\">arXiv</span><span class=\"is-sr-only\">archive</span>`."
  - "When arXiv's name appears in a paragraph of text that is likely to be copied (ie: citations) we unfortunately must keep it as plain text and live with the screen reader mis-pronunciation. This is because the hidden word is copied along with the visible one and would break every pasted citation."
---

# Using the design system

This page shares how to get started with the arXiv Design System: basic markup, which files to link to, in what order, and a handful of things to avoid. If you are an AI assistant, `AGENTS.md` at the repository root holds the file map in a form you can route from.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Core linked files

Every core file you need to include in your repo, and in what order.

**Rule.** **`fonts.css`.** Include this file before `design-system.css`. The font file declares the faces, the stylesheet names them. Either order renders but we have chosen this way for consistency.

**Rule.** **`design-system.css`.** The foundational tier 1 stylesheet. When working on internal pages, there is a tier 2 stylesheet that builds on this one.

**Rule.** **`theme.js`.** The foundational tier 1 JavaScript. Internal tools add no JavaScript of their own.

**Rule.** **`toc.js`, optional.** Add it when the page has a TOC bar. The bar itself is tier 1; the script closes the menu after a choice and names the section the reader is in. See [TOC bar](navigation.md#toc-bar).

**Rule.** **`copy.js`, optional.** Add it when the page shows code a reader might take away, or has any other copy button. It needs no markup for code: it finds every `<pre>` on the page and puts a copy button on each one. Other copy buttons are on [Show that something was copied](action-feedback.md).

**Rule.** **`show-more.js`, optional.** Add it when the page has a Show more, such as the authors after the first eight. The button and the tail are tier 1; the script hides the tail, shows the button and opens and closes the tail. See [Show more](progressive-disclosure.md#show-more).

**Rule.** **`cite.js`, optional.** Add it, with `copy.js`, when the page has a paper's Cite. The script shows the format chosen in the select and opens the full citation. See [Displaying paper actions and full metadata](papers.md#the-sidebar).

## Basic page markup

This is all you need for a public arXiv page. Copy it and follow the comments.

**Rule.** **`class="ds-page"` on the body is not optional.** A page without it gets components on unstyled ground. The foundation hangs on the class rather than on `<body>` so that a page which is not on the design system can link the stylesheet, for its header and footer, without its own body styles being overwritten.

## Internal tools  (Building on the foundation)

When building internal tools like arXiv Check or Admin Console pages, one class is added to `<html>` and a tier 2 stylesheet is added to the `<head>` section, in this order.

**Rule.** internal-tools.css does not work on its own: `internal-tools.css` is **not** a standalone stylesheet. It is a lightweight file that holds only the special styles or overrides that are specific to internal tools. Load it on its own and you get no foundation at all.

**Rule.** **The accent color defines internal pages.** Access Lime is highly differentiated from the public site's Open Blue and clearly signals that you are in a different environment.

**Rule.** **All you need is a parent class.** `.ds-internal` re-points `--ds-accent` and its family to Access Lime, and every component inside it that reaches for the accent follows without being told. It works on any parent, so a page that shows both surfaces puts it on a wrapper instead of on `<html>`. There is no second copy of the button, the tag or the switch inside the tier 2 stylesheet: it is not needed. Just a handful of new styles and overrides, and that class on the wrapper, are enough.

**Rule.** **Internal tools are compact.** `.ds-internal` also sets less padding inside table cells and cards, through the density tokens (`--ds-cell-padding`, `--ds-card-padding`), so a dense screen holds more. There is no compact class: the density comes with the surface.

**Rule.** **Never copy a component into the tier 2 stylesheet to restyle it.** If it needs to look different on your surface, what you need is a token change, not a second copy. A component that exists twice creates drift and lots of sad devs.

**Rule.** **Maintain the accent even on links to the other environment.** Are you linking to the internal tools from a public page, or vice versa? Maintain the accent color and let the button label clearly tell the user where it will take them. See [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md).

## Container options  (Building on the foundation)

`.ds-container` is a grid with various options for managing section layout.

**Rule.** **Sections.** The container's direct children are `<section>` elements, and the container sets the gap between them. Do not add top or bottom margins to sections, the container already does.

**Rule.** **Full width.** A coloured band that runs edge to edge gets `.ds-full` with a zone class (see [Secondary zones](layouts.md#secondary-zones)). Do not add negative margins or use viewport units for placement. Using a calculation like `calc(-50vw + 50%)` overhangs the section band and causes the page to scroll sideways in some environments.

**Rule.** **Page width.** Width comes from `--ds-width-page` and `--ds-gutter`. Need to change the page width? Repoint one of the tokens, do not add a second width beside it.

## Combining components  (Building on the foundation)

Most areas of a page can be built by putting existing components together. Look for a combination before inventing a component.

**Rule.** **Examples in these docs.** The [search form](search.md) with the results' settings under it; a [table](tables.md) with its toolbar of filters and bulk actions; a [sidebar](layouts.md#sidebar) of accordions; a [card that links](cards.md#cards-that-link), with a tag; [secondary navigation with a compact filter bar](navigation.md#two-levels-of-navigation).

**Rule.** **Each component works inside another.** Use a component's documented markup unchanged inside the other.

**Rule.** **A new class is the last step.** If a combination needs CSS, it is a rule on the outer component about what it can hold, written in the design system. Ask before adding a component.

## Rules

- **`theme.js` is not deferred.** The script is deliberately not deferred because it writes the reader's theme onto `<html>` before the first paint. If we added `defer` then the page will render light first, and then flip if the reader chose dark mode in their system. Many readers choose dark mode because light mode is less legible or hurts their eyes and we want to honor that.
- **Every section starts with a heading.** Headings provide important navigation structure for screen reader users so a `<section>` without one is hard to find.
- **Naming sections (optional).** A name on the section itself (`aria-labelledby` pointing at the heading) is optional, but useful for a section that a reader would want to jump to directly. Use your discretion. Every named section becomes an entry in the landmark list.
- **Write the name arXiv so that screen readers say “archive”.** A screen reader reads the Xiv in our name as a Roman numeral. We can take a few steps to fix this: For an image like the logo, add alt text that says “archive”. Where the name is typed this markup will be pronounced correctly: `<span aria-hidden="true">arXiv</span><span class="is-sr-only">archive</span>`. When arXiv's name appears in a paragraph of text that is likely to be copied (ie: citations) we unfortunately must keep it as plain text and live with the screen reader mis-pronunciation. This is because the hidden word is copied along with the visible one and would break every pasted citation.
- For an image like the logo, add alt text that says “archive”.
- Where the name is typed this markup will be pronounced correctly: `<span aria-hidden="true">arXiv</span><span class="is-sr-only">archive</span>`.
- When arXiv's name appears in a paragraph of text that is likely to be copied (ie: citations) we unfortunately must keep it as plain text and live with the screen reader mis-pronunciation. This is because the hidden word is copied along with the visible one and would break every pasted citation.
