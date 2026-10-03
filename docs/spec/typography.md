---
page: typography.html
title: "Typography"
summary: "arXiv sets all text in the IBM Plex family with STIX Two Math for notation. All fonts are self-hosted and open source with no external font services."
stylesheet: design-system.css
components:
  - id: the-font-stack
    title: "The font stack"
    summary: "The type family is IBM Plex, plus STIX Two Math for notation. Each face has a job."
    classes:
      - name: "--ds-font-sans"
        does: "The default: where no other face applies, this is the answer. Weights 400 / 500 / 600."
      - name: "--ds-font-condensed"
        does: "Labels, captions, table headers and metadata, usually small and uppercase. Weights 500 / 600."
      - name: ".ds-panel-label"
        does: "The ready-made label in this face; see [Panel label](#panel-label) below."
      - name: "--ds-font-mono"
        does: "Identifiers and code. Weights 400 / 500. Inline `<code>` and `<pre>` already use it; see [Code blocks](#code-blocks-and-the-copy-button) below."
      - name: ".ds-annotation"
        does: "The annotation voice: `--ds-font-serif`, italic, 400, 0.8125rem, `--ds-text-muted`. It is a voice, not a layout role; where it sits is the consumer's decision."
      - name: "--ds-font-serif"
        does: "The serif stack. On the public site and in internal tools it is used only through `.ds-annotation`."
      - name: "--ds-font-serif"
        does: "Upright, weights 400 and 600. Outreach properties only; see [outreach sites](outreach.html)."
      - name: "<math>"
        does: "No font token exists for math; use the stack directly on the notation. Loads with `font-display: auto` per DESIGN-POLICIES."
  - id: the-type-scale
    title: "The body text scale"
    summary: "The text sizes are set in rem so they move with the reader's base size."
    classes:
      - name: "<p>"
        does: "1rem, the reader's base size. Nothing sets it; the browser does."
      - name: "<small>"
        does: "0.875rem in `--ds-text-muted`."
      - name: "<pre>"
        does: "0.875rem, line-height 1.6, on the dark chrome ground."
      - name: ".ds-annotation"
        does: "0.8125rem, serif italic, line-height 1.45."
      - name: ".ds-panel-label"
        does: "0.75rem, condensed, uppercase."
      - name: "<code>"
        does: "0.9em, so it follows the size of its parent."
  - id: the-heading-scale
    title: "The heading scale"
    summary: "Four levels, each level is a quarter larger than the one below it, which puts h1 at exactly twice body size. Sizes are in rem so they follow the user's base setting."
    classes:
      - name: "<h1>"
        does: "The page's one subject: what the page is about, stated once — a paper title, a form name, a console view. A page that seems to need two h1s is two pages. 2rem (32px) · 700 · line-height 1.25 · space above 0, below `--ds-space-4`."
      - name: "<h2>"
        does: "A major section: a top-level division of that subject — Abstract, Submission history, References, each step of a submission form. 1.5rem (24px) · 600 · line-height 1.25 · space above `--ds-space-8`, below `--ds-space-3`."
      - name: "<h3>"
        does: "A division inside one section: a subsection of a paper, or a card heading inside a panel. It only exists where an h2 already does. 1.25rem (20px) · 600 · line-height 1.25 · space above `--ds-space-8`, below `--ds-space-2`."
      - name: "<h4>"
        does: "The smallest named step: a named paragraph in a paper, a field group in a form. This is the last level the scale defines; needing an h5 is a sign the content wants restructuring, not a fifth size. 1rem (16px) · 600 · line-height 1.25 · space above `--ds-space-4`, below `--ds-space-2`."
  - id: text-links
    title: "Text links"
    summary: "Links are typography too. Inline links in body text are always underlined (to pass WCAG 1.4.1). Standalone navigation links and groups of links that are not part of body text (headers, footers, author list) drop the underline to reduce noise."
    classes:
      - name: ".ds-link"
        does: "The inline text link. Both surfaces use `.ds-link` and the `--ds-link-*` tokens: the same grammar, the same names and the same values. Inside a `.ds-page` a bare `<a>` gets the same treatment without the class."
      - name: "--ds-link, --ds-link-hover, --ds-link-visited"
        does: "Rest, hover and visited colours. The underline does not change between states."
      - name: "--ds-focus-ring"
        does: "The 3px keyboard focus ring, drawn on `:focus-visible` only."
      - name: ".ds-link-list"
        does: "On the element that holds a list in which every item is a link, such as an author list or a column of footer links. The links drop the underline at rest and keep everything else: Link Blue, the underline on hover, the focus ring and the visited colour. There is no ordinary text beside them for the underline to separate them from, so colour alone is enough here."
  - id: matched-words
    title: "Matched words"
    summary: "The words that matched a search are marked with `<mark>`, in the accent wash and a heavier weight."
    classes:
      - name: "<mark>"
        does: "One matched word or phrase. No class: the element is styled inside `.ds-page`. The weight marks it as well as the colour, so it is never colour alone. In internal tools the wash is Access Lime."
  - id: code-blocks-and-the-copy-button
    title: "Code blocks and the copy button"
    summary: "A code block uses Plex Mono on Repository Brown, and always includes a copy button."
    classes:
      - name: "<pre><code>"
        does: "The block. Escape `<`, `>` and `&` inside it. No wrapper and no button of your own."
      - name: "<script src=\"copy-code.js\" defer>"
        does: "Once per page, at the foot. It finds every `<pre>` on the page and adds the control."
      - name: ".ds-code, .ds-code-copy"
        does: "The wrapper and the button. The script writes both; never hand-build them."
      - name: "[data-no-copy]"
        does: "On a `<pre>`, opts that block out — for a block that is an illustration of output rather than something to take away."
  - id: panel-label
    title: "Panel label"
    summary: "The small uppercase Condensed label that names a panel, a column or a group. It is not a heading level and stays out of the document outline — if a reader needs to navigate to it, it is an `h3` or an `h4` at the sizes above."
    classes:
      - name: ".ds-panel-label"
        does: "One class for the whole system: 0.75rem · 600 · Condensed · uppercase · 0.04em · `--ds-text-muted`. Use it wherever this treatment appears — panel headings, column labels, the label above a group of controls — on whichever element is semantically right. A component that owns its internal spacing takes the margin back."
      - name: "<dt>"
        does: "A definition term inside `.ds-acc-body` is this label, and has no class."
    notes:
      - "Do not reach for it as a heading substitute. A label that a reader needs to navigate to is a heading, and belongs in the outline."
rules:
  - "**700 is the ceiling.** IBM Plex ships no heavier weight, so a CSS `800` either falls back or gets faux-bolded, differently per browser. Ask for the weight that exists."
  - "**Two serif jobs, kept apart.** Upright serif is the editorial voice — headlines, quotes, drop caps. Italic serif stays the annotation voice everywhere. A heading that must not read as \"another article\" uses the heavy *sans* instead, which is why 700 exists in this context at all."
  - "**Mono as display type** is an outreach liberty: the typewriter register echoes the main site's identifiers. On the public site, mono still means \"this is an identifier or code.\""
  - "**The ratio is 1.25** — a major third — rounded to quarter-rem steps: 1, 1.25, 1.5, 2rem. A strict geometric run would put h2 at 1.5625rem; a quarter of a rem is the number a person can hold in their head and type without checking. The rounding is what makes h1 land on exactly double the body size."
  - "**700 appears once, at h1.** IBM Plex ships nothing heavier, so 700 is the ceiling and it is spent on the one heading that names the page. Everything below is 600. Always state the weight: a rule that sets only `font-size` inherits the browser default bold, which is how several pages ended up with an h3 heavier than the h2 above it."
  - "**Space above is at least twice the space below.** A heading belongs to the text it introduces, not the text it follows, and the gap has to say so. The values sit on the 4px rhythm in [Spacing](spacing.html)."
  - "**Long titles clamp.** An h1 that can run to seven words uses `clamp()` between rem bounds rather than a fixed 2rem — see \"Fluid where titles meet phones\" below."
  - "**The 11px uppercase Condensed label is not a heading level.** Set in `--ds-font-condensed` and `--ds-text-muted`, it marks a panel or a column and stays out of the document outline. If a reader needs to navigate to it, it is an h3 or an h4 at the size above, not a label."
  - "Space is given as spacing tokens, not pixels, because that is what `design-system.css` implements — `--ds-space-8` is 2rem, `--ds-space-6` is 1.5rem, and so on down the scale."
  - "**There is no markup for the button**, and that is the design. `copy-code.js` finds every `<pre>` on the page, wraps it in `.ds-code` and inserts the control, which is `.ds-code-copy`. A block added next year is covered without anyone remembering, which a per-block wrapper would not be. Every page under `docs/` already loads the script."
  - "**The button reserves a strip at the top, not the side.** A `<pre>` scrolls horizontally, so padding at its inline end does not hold the visible right edge clear — a long line runs straight under a right-hand button. A lane across the top works at every line length."
  - "**It is an icon, and it still says “Copy”.** The two overlapping sheets are the glyph people already know, so the control needs no label taking up room over the code. Both SVGs are `aria-hidden` and the button has `aria-label=\"Copy code\"`, which is what a screen reader announces. The `title` is the pointer affordance only — assistive technology takes the `aria-label` and ignores it."
  - "**Success is announced, not just shown.** The icon becomes a green tick, and a visually hidden `role=\"status\"` region says “Copied to clipboard”. Both are needed: a tick is invisible to a screen reader, and the button’s own name does not change because its action did not change — it is still the copy button. Both reset after two seconds."
  - "**The name stays put while the icon moves.** Relabelling a control to report a result is the same mistake as bolding a switch label on toggle: the name of a control is what it does, not what just happened. The result belongs in the live region."
  - "**It works from disk.** The asynchronous Clipboard API needs a secure context, which `file://` is not, and it rejects when the window is not focused. Both cases fall back to `execCommand`, and if that fails too the status region says so rather than the button quietly doing nothing."
  - "**Without JavaScript there is no button** and the code is still selectable. The button is a convenience; it is never the only way to get the text."
  - "**Opt a block out with `<pre data-no-copy>`** — for a block that is an illustration of output rather than something to take away."
  - "A browser font-size setting has to reach arXiv content (accessibility-priorities.md, cognitive/dyslexia section), so every type size is `rem`. But a label that grows inside a box that does not is no better than a label that never grew: set a control's padding and minimum width in `em`, against its own label, and the whole control follows the reader. Absolute floors stay absolute — `min-height: 24px` is a WCAG target size, not a type size."
  - "No Google Fonts, no Typekit, no CDN fonts (DESIGN-POLICIES.md). Every `font-family` declaration includes system fallbacks; text fonts load with `font-display: swap` (readability first), STIX Two Math with `font-display: auto` (math must render in the correct face)."
  - "No fixed line-heights, no pinned letter-spacing, no `!important` on font-family in content areas. User stylesheets, reader-mode extensions, and OS settings win — \"HTML gives you freedom: you can use software to change colors or typefaces\" (research, dyslexia section)."
  - "Paper titles use `clamp()` between rem bounds (22px–32px equivalent) so a seven-word title does not wrap to five lines at 320px. Body text never scales fluidly — it follows the user's base size exactly."
  - "**Keep the heading order.** One `<h1>` per page, then `<h2>`, `<h3>` and `<h4>` in order, without skipping a level. Choose the level from the outline, not from the size you want; the scale gives each level its size. A screen reader user moves through the page by these levels."
  - "**Write sizes in rem, never in px.** A reader who raises the browser font size must see every piece of text grow. Give a control its padding and minimum width in `em`, so the box grows with its label."
  - "**Let text reflow at 200% zoom.** Do not give a box that holds text a fixed height, and do not cut text off with `overflow: hidden` unless there is another way to read all of it. At 400% page zoom a 1280px screen is a 320px screen, and the page must not scroll sideways there."
  - "**Put text in text, not in images.** An image of words cannot be resized, translated, searched or read aloud. If an image must include words, the same words go in its `alt` text or next to it."
  - "**Uppercase comes from CSS, never from the keyboard.** The panel label is uppercase because `.ds-panel-label` makes it so. Type it in sentence case, so copy-and-paste, search and screen readers get the real words."
---

# Typography

arXiv sets all text in the IBM Plex family with STIX Two Math for notation. All fonts are self-hosted and open source with no external font services.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The font stack

The type family is IBM Plex, plus STIX Two Math for notation. Each face has a job.

```html
font-family: var(--ds-font-sans);
```

```html
font-family: var(--ds-font-condensed);
```

```html
font-family: var(--ds-font-mono);
```

```html
<p class="ds-annotation">Figure 2: the scalaron potential.</p>
```

```html
font-family: var(--ds-font-serif);
```

```html
font-family: "STIX Two Math", "Cambria Math", math;
```

- `--ds-font-sans` — The default: where no other face applies, this is the answer. Weights 400 / 500 / 600.
- `--ds-font-condensed` — Labels, captions, table headers and metadata, usually small and uppercase. Weights 500 / 600.
- `.ds-panel-label` — The ready-made label in this face; see [Panel label](#panel-label) below.
- `--ds-font-mono` — Identifiers and code. Weights 400 / 500. Inline `<code>` and `<pre>` already use it; see [Code blocks](#code-blocks-and-the-copy-button) below.
- `.ds-annotation` — The annotation voice: `--ds-font-serif`, italic, 400, 0.8125rem, `--ds-text-muted`. It is a voice, not a layout role; where it sits is the consumer's decision.
- `--ds-font-serif` — The serif stack. On the public site and in internal tools it is used only through `.ds-annotation`.
- `--ds-font-serif` — Upright, weights 400 and 600. Outreach properties only; see [outreach sites](outreach.html).
- `<math>` — No font token exists for math; use the stack directly on the notation. Loads with `font-display: auto` per DESIGN-POLICIES.

## The body text scale

The text sizes are set in rem so they move with the reader's base size.

```html
<p>Body text.</p>
<small>Secondary text.</small>
<p class="ds-annotation">A margin footnote.</p>
<p class="ds-panel-label">Paper information</p>
<p>An identifier: arXiv:2604.22725</p>
```

- `<p>` — 1rem, the reader's base size. Nothing sets it; the browser does.
- `<small>` — 0.875rem in `--ds-text-muted`.
- `<pre>` — 0.875rem, line-height 1.6, on the dark chrome ground.
- `.ds-annotation` — 0.8125rem, serif italic, line-height 1.45.
- `.ds-panel-label` — 0.75rem, condensed, uppercase.
- `<code>` — 0.9em, so it follows the size of its parent.

## The heading scale

Four levels, each level is a quarter larger than the one below it, which puts h1 at exactly twice body size. Sizes are in rem so they follow the user's base setting.

```html
<h1>Gauge-independent approach to inflation</h1>
  <h2>Submission history</h2>
    <h3>Gauge-invariant perturbations</h3>
      <h4>Boundary conditions</h4>
```

- `<h1>` — The page's one subject: what the page is about, stated once — a paper title, a form name, a console view. A page that seems to need two h1s is two pages. 2rem (32px) · 700 · line-height 1.25 · space above 0, below `--ds-space-4`.
- `<h2>` — A major section: a top-level division of that subject — Abstract, Submission history, References, each step of a submission form. 1.5rem (24px) · 600 · line-height 1.25 · space above `--ds-space-8`, below `--ds-space-3`.
- `<h3>` — A division inside one section: a subsection of a paper, or a card heading inside a panel. It only exists where an h2 already does. 1.25rem (20px) · 600 · line-height 1.25 · space above `--ds-space-8`, below `--ds-space-2`.
- `<h4>` — The smallest named step: a named paragraph in a paper, a field group in a form. This is the last level the scale defines; needing an h5 is a sign the content wants restructuring, not a fifth size. 1rem (16px) · 600 · line-height 1.25 · space above `--ds-space-4`, below `--ds-space-2`.

## Text links

Links are typography too. Inline links in body text are always underlined (to pass WCAG 1.4.1). Standalone navigation links and groups of links that are not part of body text (headers, footers, author list) drop the underline to reduce noise.

```html
Reading text with <a href="/abs/2604.22725">an inline link</a> in it.
```

```html
<p class="ds-link-list">
  <a href="/a/palomares_a_1">Adrian Palomares</a>,
  <a href="/a/chen_m_1">Mei Lin Chen</a>,
  <a href="/a/mensah_k_1">Kwame Mensah</a>
</p>
```

- `.ds-link` — The inline text link. Both surfaces use `.ds-link` and the `--ds-link-*` tokens: the same grammar, the same names and the same values. Inside a `.ds-page` a bare `<a>` gets the same treatment without the class.
- `--ds-link, --ds-link-hover, --ds-link-visited` — Rest, hover and visited colours. The underline does not change between states.
- `--ds-focus-ring` — The 3px keyboard focus ring, drawn on `:focus-visible` only.
- `.ds-link-list` — On the element that holds a list in which every item is a link, such as an author list or a column of footer links. The links drop the underline at rest and keep everything else: Link Blue, the underline on hover, the focus ring and the visited colour. There is no ordinary text beside them for the underline to separate them from, so colour alone is enough here.

## Matched words

The words that matched a search are marked with `<mark>`, in the accent wash and a heavier weight.

```html
<p>Weak-<mark>Lensing</mark> Shear Response for Photometric Redshift-Based Tomographic Binning</p>
```

- `<mark>` — One matched word or phrase. No class: the element is styled inside `.ds-page`. The weight marks it as well as the colour, so it is never colour alone. In internal tools the wash is Access Lime.

## Code blocks and the copy button

A code block uses Plex Mono on Repository Brown, and always includes a copy button.

```html
<!-- Write the block the way you already do -->
<pre><button class="ds-btn">Save</button></pre>

<!-- And include the script once, at the foot of the page -->
<script src="copy-code.js" defer></script>
```

- `<pre><code>` — The block. Escape `<`, `>` and `&` inside it. No wrapper and no button of your own.
- `<script src="copy-code.js" defer>` — Once per page, at the foot. It finds every `<pre>` on the page and adds the control.
- `.ds-code, .ds-code-copy` — The wrapper and the button. The script writes both; never hand-build them.
- `[data-no-copy]` — On a `<pre>`, opts that block out — for a block that is an illustration of output rather than something to take away.

## Panel label

The small uppercase Condensed label that names a panel, a column or a group. It is not a heading level and stays out of the document outline — if a reader needs to navigate to it, it is an `h3` or an `h4` at the sizes above.

```html
<p class="ds-panel-label">Paper information</p>
```

- `.ds-panel-label` — One class for the whole system: 0.75rem · 600 · Condensed · uppercase · 0.04em · `--ds-text-muted`. Use it wherever this treatment appears — panel headings, column labels, the label above a group of controls — on whichever element is semantically right. A component that owns its internal spacing takes the margin back.
- `<dt>` — A definition term inside `.ds-acc-body` is this label, and has no class.

> Do not reach for it as a heading substitute. A label that a reader needs to navigate to is a heading, and belongs in the outline.

## Rules

- **700 is the ceiling.** IBM Plex ships no heavier weight, so a CSS `800` either falls back or gets faux-bolded, differently per browser. Ask for the weight that exists.
- **Two serif jobs, kept apart.** Upright serif is the editorial voice — headlines, quotes, drop caps. Italic serif stays the annotation voice everywhere. A heading that must not read as "another article" uses the heavy *sans* instead, which is why 700 exists in this context at all.
- **Mono as display type** is an outreach liberty: the typewriter register echoes the main site's identifiers. On the public site, mono still means "this is an identifier or code."
- **The ratio is 1.25** — a major third — rounded to quarter-rem steps: 1, 1.25, 1.5, 2rem. A strict geometric run would put h2 at 1.5625rem; a quarter of a rem is the number a person can hold in their head and type without checking. The rounding is what makes h1 land on exactly double the body size.
- **700 appears once, at h1.** IBM Plex ships nothing heavier, so 700 is the ceiling and it is spent on the one heading that names the page. Everything below is 600. Always state the weight: a rule that sets only `font-size` inherits the browser default bold, which is how several pages ended up with an h3 heavier than the h2 above it.
- **Space above is at least twice the space below.** A heading belongs to the text it introduces, not the text it follows, and the gap has to say so. The values sit on the 4px rhythm in [Spacing](spacing.html).
- **Long titles clamp.** An h1 that can run to seven words uses `clamp()` between rem bounds rather than a fixed 2rem — see "Fluid where titles meet phones" below.
- **The 11px uppercase Condensed label is not a heading level.** Set in `--ds-font-condensed` and `--ds-text-muted`, it marks a panel or a column and stays out of the document outline. If a reader needs to navigate to it, it is an h3 or an h4 at the size above, not a label.
- Space is given as spacing tokens, not pixels, because that is what `design-system.css` implements — `--ds-space-8` is 2rem, `--ds-space-6` is 1.5rem, and so on down the scale.
- **There is no markup for the button**, and that is the design. `copy-code.js` finds every `<pre>` on the page, wraps it in `.ds-code` and inserts the control, which is `.ds-code-copy`. A block added next year is covered without anyone remembering, which a per-block wrapper would not be. Every page under `docs/` already loads the script.
- **The button reserves a strip at the top, not the side.** A `<pre>` scrolls horizontally, so padding at its inline end does not hold the visible right edge clear — a long line runs straight under a right-hand button. A lane across the top works at every line length.
- **It is an icon, and it still says “Copy”.** The two overlapping sheets are the glyph people already know, so the control needs no label taking up room over the code. Both SVGs are `aria-hidden` and the button has `aria-label="Copy code"`, which is what a screen reader announces. The `title` is the pointer affordance only — assistive technology takes the `aria-label` and ignores it.
- **Success is announced, not just shown.** The icon becomes a green tick, and a visually hidden `role="status"` region says “Copied to clipboard”. Both are needed: a tick is invisible to a screen reader, and the button’s own name does not change because its action did not change — it is still the copy button. Both reset after two seconds.
- **The name stays put while the icon moves.** Relabelling a control to report a result is the same mistake as bolding a switch label on toggle: the name of a control is what it does, not what just happened. The result belongs in the live region.
- **It works from disk.** The asynchronous Clipboard API needs a secure context, which `file://` is not, and it rejects when the window is not focused. Both cases fall back to `execCommand`, and if that fails too the status region says so rather than the button quietly doing nothing.
- **Without JavaScript there is no button** and the code is still selectable. The button is a convenience; it is never the only way to get the text.
- **Opt a block out with `<pre data-no-copy>`** — for a block that is an illustration of output rather than something to take away.
- A browser font-size setting has to reach arXiv content (accessibility-priorities.md, cognitive/dyslexia section), so every type size is `rem`. But a label that grows inside a box that does not is no better than a label that never grew: set a control's padding and minimum width in `em`, against its own label, and the whole control follows the reader. Absolute floors stay absolute — `min-height: 24px` is a WCAG target size, not a type size.
- No Google Fonts, no Typekit, no CDN fonts (DESIGN-POLICIES.md). Every `font-family` declaration includes system fallbacks; text fonts load with `font-display: swap` (readability first), STIX Two Math with `font-display: auto` (math must render in the correct face).
- No fixed line-heights, no pinned letter-spacing, no `!important` on font-family in content areas. User stylesheets, reader-mode extensions, and OS settings win — "HTML gives you freedom: you can use software to change colors or typefaces" (research, dyslexia section).
- Paper titles use `clamp()` between rem bounds (22px–32px equivalent) so a seven-word title does not wrap to five lines at 320px. Body text never scales fluidly — it follows the user's base size exactly.
- **Keep the heading order.** One `<h1>` per page, then `<h2>`, `<h3>` and `<h4>` in order, without skipping a level. Choose the level from the outline, not from the size you want; the scale gives each level its size. A screen reader user moves through the page by these levels.
- **Write sizes in rem, never in px.** A reader who raises the browser font size must see every piece of text grow. Give a control its padding and minimum width in `em`, so the box grows with its label.
- **Let text reflow at 200% zoom.** Do not give a box that holds text a fixed height, and do not cut text off with `overflow: hidden` unless there is another way to read all of it. At 400% page zoom a 1280px screen is a 320px screen, and the page must not scroll sideways there.
- **Put text in text, not in images.** An image of words cannot be resized, translated, searched or read aloud. If an image must include words, the same words go in its `alt` text or next to it.
- **Uppercase comes from CSS, never from the keyboard.** The panel label is uppercase because `.ds-panel-label` makes it so. Type it in sentence case, so copy-and-paste, search and screen readers get the real words.
