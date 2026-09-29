---
page: using.html
title: "Using the design system"
summary: "This page shares how to get started with the arXiv Design System: basic markup, which files to link to, in what order, and a handful of things to avoid. If you are an AI assistant, `AGENTS.md` at the repository root holds the file map in a form you can route from."
stylesheet: design-system.css
components:
  - id: core-linked-files
    title: "Core linked files"
    summary: "Every core file you need to include in your repo, and in what order."
  - id: basic-page-markup
    title: "Basic page markup"
    summary: "This is all you need for a public arXiv page. Copy it and follow the comments."
  - id: internal-tools
    title: "Internal tools"
    group: "Building on the foundation"
    summary: "When building internal tools like arXiv Check or Admin Console pages, one class is added to `<html>` and a tier 2 stylesheet is added to the `<head>` section, in this order."
    rules:
      - "internal-tools.css does not work on its own: `internal-tools.css` is **not** a standalone stylesheet. It is a lightweight file that holds only the special styles or overrides that are specific to internal tools. Load it on its own and you get no foundation at all."
  - id: container-options
    title: "Container options"
    group: "Building on the foundation"
    summary: "`.ds-container` is a grid with various options for managing section layout."
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

## Basic page markup

This is all you need for a public arXiv page. Copy it and follow the comments.

## Internal tools  (Building on the foundation)

When building internal tools like arXiv Check or Admin Console pages, one class is added to `<html>` and a tier 2 stylesheet is added to the `<head>` section, in this order.

**Rule.** internal-tools.css does not work on its own: `internal-tools.css` is **not** a standalone stylesheet. It is a lightweight file that holds only the special styles or overrides that are specific to internal tools. Load it on its own and you get no foundation at all.

## Container options  (Building on the foundation)

`.ds-container` is a grid with various options for managing section layout.

## Rules

- **`theme.js` is not deferred.** The script is deliberately not deferred because it writes the reader's theme onto `<html>` before the first paint. If we added `defer` then the page will render light first, and then flip if the reader chose dark mode in their system. Many readers choose dark mode because light mode is less legible or hurts their eyes and we want to honor that.
- **Every section starts with a heading.** Headings provide important navigation structure for screen reader users so a `<section>` without one is hard to find.
- **Naming sections (optional).** A name on the section itself (`aria-labelledby` pointing at the heading) is optional, but useful for a section that a reader would want to jump to directly. Use your discretion. Every named section becomes an entry in the landmark list.
- **Write the name arXiv so that screen readers say “archive”.** A screen reader reads the Xiv in our name as a Roman numeral. We can take a few steps to fix this: For an image like the logo, add alt text that says “archive”. Where the name is typed this markup will be pronounced correctly: `<span aria-hidden="true">arXiv</span><span class="is-sr-only">archive</span>`. When arXiv's name appears in a paragraph of text that is likely to be copied (ie: citations) we unfortunately must keep it as plain text and live with the screen reader mis-pronunciation. This is because the hidden word is copied along with the visible one and would break every pasted citation.
- For an image like the logo, add alt text that says “archive”.
- Where the name is typed this markup will be pronounced correctly: `<span aria-hidden="true">arXiv</span><span class="is-sr-only">archive</span>`.
- When arXiv's name appears in a paragraph of text that is likely to be copied (ie: citations) we unfortunately must keep it as plain text and live with the screen reader mis-pronunciation. This is because the hidden word is copied along with the visible one and would break every pasted citation.
