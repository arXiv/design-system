---
page: spacing.html
title: "Spacing"
summary: "Every gap on arXiv pages comes from the scale defined below. The scale is a 4px-based / 8-point scale, with no off-scale values permitted. More details in [DESIGN-POLICIES.md](doc.html?src=docs/DESIGN-POLICIES.md). Token values `--ds-space-1`…`--ds-space-12` are found in `design-system.css`."
stylesheet: design-system.css
components:
  - id: the-scale
    title: "The scale"
    summary: "A seven step scale, with each step roughly 1.5x larger than the previous. The width of the bars below are the token values pulled live from `--ds-space-*`."
    classes:
      - name: "--ds-space-1"
        does: "4px. Tightest — label→value, icon→text."
      - name: "--ds-space-2"
        does: "8px. Closely related inline items."
      - name: "--ds-space-3"
        does: "12px. Related stacked elements."
      - name: "--ds-space-4"
        does: "16px. Default gap between elements in a section."
      - name: "--ds-space-6"
        does: "24px. Sub-section separation / card padding."
      - name: "--ds-space-8"
        does: "32px. Larger internal padding."
      - name: "--ds-space-12"
        does: "48px. Breathing space *between* major sections."
  - id: the-proximity-rule
    title: "The proximity rule"
    summary: "The gap *between* sections should be clearly larger than the gap *within* a section. We aim for at least 2× (e.g., 16px between paragraphs, 32px before the next heading, 48px between sections). This is what allows grouping to work without adding extra lines, borders or boxes."
    classes:
      - name: "<h3>"
        does: "32px above (`--ds-space-8`) and 8px below (`--ds-space-2`), so a heading sits four times closer to its own text than to the text before it."
      - name: "<p>"
        does: "16px below (`--ds-space-4`), between paragraphs of the same group: half the 32px that starts the next group."
      - name: "--ds-space-section"
        does: "48px. Between the sections of a page, such as the sections of this one."
    notes:
      - "The markup is plain headings and paragraphs with no classes. The spacing is the design system's own default for those elements."
  - id: the-layout-tokens
    title: "The layout tokens"
    summary: "Three tokens set the shape of every page: the width of the content column, the gutter that keeps it off the viewport edge, and the space the container puts between one region and the next. The container that reads them is documented on [Layout patterns](layout-patterns.html#the-page-container)."
    classes:
      - name: "--ds-width-page"
        does: "850px. The width of the content track, and the one width on a page: prose, tables, demo blocks, code and callouts all share it. An element never declares its own."
      - name: "--ds-gutter"
        does: "`--ds-space-6`, 24px. The least space between the content track and the viewport edge. A `.ds-full` band uses the same token as its inline padding, so the band and the column cannot drift apart."
      - name: "--ds-space-section"
        does: "48px. The container's `row-gap`: the space between one direct child and the next. A section carries no margin of its own."
rules:
  - "Use the step tokens, never hand-code the spacing. Do not fight the grid. If the need arises for different spacing reach out to the design team. The new values mean a change to DESIGN-POLICIES, not a local override."
  - "When applying your own spacing use the named `--ds-space-block` for spacing *within*, and `--ds-space-section` for spacing *between*. Spacing between blocks is 2× tight while spacing between sections is 3× block; Lower than 1.5× the eye cannot tell the two apart and the grouping signal fails."
  - "Feel like you need a border to separate content? First try widening the gap, using cards, or applying designated background colors for primary and secondary content zones."
  - "The scale is expressed in `rem`, so spacing also scales with the reader's text size. A fixed gap next to growing text would destroy the ratio for *within* and *between* sizes and lose visual meaning at different zoom levels."
  - "Named breaks include `--ds-space-tight` inside a group, `--ds-space-block` between blocks in a section, or `--ds-space-section` between sections. We name spacing roles like we do colors: for their role and not their raw value. That flexibility enables the dark mode flip and our responsive spacing system."
  - "A section does not know what follows it, so it cannot know how far away that next piece of content should be Spacing is added to the container as `gap`, not on each child as a margin. If you find yourself reaching for `:last-child { margin-bottom: 0 }` let the design team know asap. It is a symptom that the spacing is on the wrong element."
  - "One exception:prose spacing *inside* a section stays element-owned, because a heading's margin depends on its own text size, which the container does not know."
  - "“How far apart do these sit” means the same thing whether the space comes from a margin or a gap, and whether the space is vertical or horizontal. Gap between siblins uses the standard scale."
  - "One exception: the space between a glyph and its label *inside* a single control is part of the control rather than layout. Use `--ds-gap-glyph` (`0.5em`), which scales with that control's own type."
  - "Buttons placed as bare siblings are spaced by the HTML whitespace between the tags, which are narrower than any deliberate value. It will look like a bug because it is one. For the button use case you would use `.ds-btn-group` or the `--stack` variant. For other elements, visit their pattern pages to find the right container and code example."
  - "There is one name per scale step and every codebase uses it exactly as written. No per-repository prefixes or mapping tables. Anything kept in another repo is invisible here."
  - "**Do not shrink controls.** Every button, link and other control keeps a hit area of at least 24 by 24 CSS pixels (WCAG 2.2, 2.5.8), however tight the gap between it and its neighbours."
  - "**Spacing survives zoom.** The scale is in `rem`, so every gap grows with the reader's text size (WCAG 1.4.4). At 400% page zoom the page is only 320 pixels wide. Let the tokens do their work and never set a gap or a width that forces the page to scroll sideways."
  - "**Spacing is not structure.** Proximity tells a sighted reader what belongs together, but a screen reader does not see it. Give groups a heading, a `<fieldset>` or a landmark, so the grouping is in the markup as well as visual."
---

# Spacing

Every gap on arXiv pages comes from the scale defined below. The scale is a 4px-based / 8-point scale, with no off-scale values permitted. More details in [DESIGN-POLICIES.md](doc.html?src=docs/DESIGN-POLICIES.md). Token values `--ds-space-1`…`--ds-space-12` are found in `design-system.css`.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The scale

A seven step scale, with each step roughly 1.5x larger than the previous. The width of the bars below are the token values pulled live from `--ds-space-*`.

```html
/* A stop is used as written: a token, in rem, never a pixel value */
.ds-card {
  padding: var(--ds-space-4) var(--ds-space-6);   /* 16px 24px at a 16px root */
}
```

- `--ds-space-1` — 4px. Tightest — label→value, icon→text.
- `--ds-space-2` — 8px. Closely related inline items.
- `--ds-space-3` — 12px. Related stacked elements.
- `--ds-space-4` — 16px. Default gap between elements in a section.
- `--ds-space-6` — 24px. Sub-section separation / card padding.
- `--ds-space-8` — 32px. Larger internal padding.
- `--ds-space-12` — 48px. Breathing space *between* major sections.

## The proximity rule

The gap *between* sections should be clearly larger than the gap *within* a section. We aim for at least 2× (e.g., 16px between paragraphs, 32px before the next heading, 48px between sections). This is what allows grouping to work without adding extra lines, borders or boxes.

```html
<h3>Submission</h3>
<p>Submitted by A. Palomares on 14 July 2026.</p>
<p>Revised on 2 August 2026.</p>
<h3>Classification</h3>
<p>Primary category: General Relativity and Quantum Cosmology (gr-qc).</p>
<p>License: CC BY 4.0.</p>
```

- `<h3>` — 32px above (`--ds-space-8`) and 8px below (`--ds-space-2`), so a heading sits four times closer to its own text than to the text before it.
- `<p>` — 16px below (`--ds-space-4`), between paragraphs of the same group: half the 32px that starts the next group.
- `--ds-space-section` — 48px. Between the sections of a page, such as the sections of this one.

> The markup is plain headings and paragraphs with no classes. The spacing is the design system's own default for those elements.

## The layout tokens

Three tokens set the shape of every page: the width of the content column, the gutter that keeps it off the viewport edge, and the space the container puts between one region and the next. The container that reads them is documented on [Layout patterns](layout-patterns.html#the-page-container).

```html
<div class="ds-container">
  <header class="ds-page-header">…</header>
  <section>…</section>   <!-- --ds-space-section above it, from the container -->
  <section>…</section>
</div>
```

```html
/* A page that needs a different width changes the one token;
   it never adds a second width beside it. Here: a dense internal
   tool with tables that cannot compress. */
:root { --ds-width-page: 1080px; }
```

- `--ds-width-page` — 850px. The width of the content track, and the one width on a page: prose, tables, demo blocks, code and callouts all share it. An element never declares its own.
- `--ds-gutter` — `--ds-space-6`, 24px. The least space between the content track and the viewport edge. A `.ds-full` band uses the same token as its inline padding, so the band and the column cannot drift apart.
- `--ds-space-section` — 48px. The container's `row-gap`: the space between one direct child and the next. A section carries no margin of its own.

## Rules

- Use the step tokens, never hand-code the spacing. Do not fight the grid. If the need arises for different spacing reach out to the design team. The new values mean a change to DESIGN-POLICIES, not a local override.
- When applying your own spacing use the named `--ds-space-block` for spacing *within*, and `--ds-space-section` for spacing *between*. Spacing between blocks is 2× tight while spacing between sections is 3× block; Lower than 1.5× the eye cannot tell the two apart and the grouping signal fails.
- Feel like you need a border to separate content? First try widening the gap, using cards, or applying designated background colors for primary and secondary content zones.
- The scale is expressed in `rem`, so spacing also scales with the reader's text size. A fixed gap next to growing text would destroy the ratio for *within* and *between* sizes and lose visual meaning at different zoom levels.
- Named breaks include `--ds-space-tight` inside a group, `--ds-space-block` between blocks in a section, or `--ds-space-section` between sections. We name spacing roles like we do colors: for their role and not their raw value. That flexibility enables the dark mode flip and our responsive spacing system.
- A section does not know what follows it, so it cannot know how far away that next piece of content should be Spacing is added to the container as `gap`, not on each child as a margin. If you find yourself reaching for `:last-child { margin-bottom: 0 }` let the design team know asap. It is a symptom that the spacing is on the wrong element.
- One exception:prose spacing *inside* a section stays element-owned, because a heading's margin depends on its own text size, which the container does not know.
- “How far apart do these sit” means the same thing whether the space comes from a margin or a gap, and whether the space is vertical or horizontal. Gap between siblins uses the standard scale.
- One exception: the space between a glyph and its label *inside* a single control is part of the control rather than layout. Use `--ds-gap-glyph` (`0.5em`), which scales with that control's own type.
- Buttons placed as bare siblings are spaced by the HTML whitespace between the tags, which are narrower than any deliberate value. It will look like a bug because it is one. For the button use case you would use `.ds-btn-group` or the `--stack` variant. For other elements, visit their pattern pages to find the right container and code example.
- There is one name per scale step and every codebase uses it exactly as written. No per-repository prefixes or mapping tables. Anything kept in another repo is invisible here.
- **Do not shrink controls.** Every button, link and other control keeps a hit area of at least 24 by 24 CSS pixels (WCAG 2.2, 2.5.8), however tight the gap between it and its neighbours.
- **Spacing survives zoom.** The scale is in `rem`, so every gap grows with the reader's text size (WCAG 1.4.4). At 400% page zoom the page is only 320 pixels wide. Let the tokens do their work and never set a gap or a width that forces the page to scroll sideways.
- **Spacing is not structure.** Proximity tells a sighted reader what belongs together, but a screen reader does not see it. Give groups a heading, a `<fieldset>` or a landmark, so the grouping is in the markup as well as visual.
