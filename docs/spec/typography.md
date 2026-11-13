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
        does: "Labels, table headers and metadata, usually small and uppercase. Weights 500 / 600."
      - name: ".ds-panel-label"
        does: "The ready-made label in this face; see [Panel label](#panel-label) below."
      - name: "--ds-font-mono"
        does: "Identifiers and code. Weights 400 / 500. Inline `<code>` and `<pre>` already use it; see [Code blocks](#code-blocks-and-the-copy-button) below."
      - name: ".ds-annotation"
        does: "The annotation voice: `--ds-font-serif`, italic, 400, 0.8125rem, `--ds-text-muted`. It is a voice, not a layout role; where it sits is the consumer's decision."
      - name: "--ds-font-serif"
        does: "The serif stack. On the public site and in internal tools it is used only through `.ds-annotation`."
      - name: "<math>"
        does: "No font token exists for math; use the stack directly on the notation. Loads with `font-display: auto` per DESIGN-POLICIES."
  - id: the-type-scale
    title: "The body text scale"
    summary: "The text sizes are set in rem so they move with the reader's base size. Browsers set the base size to 16px unless the reader changes it, so 1rem is 16px by default; the pixel sizes on this page assume that default."
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
        does: "0.9em, so it follows the size of its parent. When to use it rather than a block: [Code blocks and the copy button](#code-blocks-and-the-copy-button)."
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) Resize Text (Level AA)"
  - id: the-heading-scale
    title: "The heading scale"
    summary: "Four levels, each larger than the one below it. On a laptop the step is about a quarter, which puts h1 at twice body size; on a phone it is 4px, so a long title takes fewer lines. Sizes are in rem so they follow the user's base setting. That base is 16px unless the reader has changed the browser's default, so the pixel sizes below assume 16px."
    classes:
      - name: "<h1>"
        does: "The page's one subject: what the page is about, stated once — a paper title, a form name, a console view. A page that seems to need two h1s is two pages. `clamp(1.75rem, 1rem + 2vw, 2rem)`: 28px on a phone, 32px from about 800px wide · 700 · line-height 1.25 · space above 0, below `--ds-space-4`."
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
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)"
  - id: matched-words
    title: "Search-matched words"
    summary: "The words that matched a search are marked with `<mark>`, in the accent wash and a heavier weight."
    classes:
      - name: "<mark>"
        does: "One matched word or phrase. No class: the element is styled inside `.ds-page`. The weight marks it as well as the colour, so it is never colour alone. In internal tools the wash is Access Lime."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A) and [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA)"
  - id: code-blocks-and-the-copy-button
    title: "Code blocks and the copy button"
    summary: "A code block uses Plex Mono on Repository Brown, and always includes a copy button. Use a block for code a reader copies, or code that runs over more than one line. A short name or example in running text that a reader would not copy, such as a file name or a list of allowed characters, is inline `<code>`, which has no button."
    classes:
      - name: "<code>"
        does: "Inline code: a short name or example inside a sentence, which a reader would not copy. No copy button."
      - name: "<pre><code>"
        does: "The block, for code a reader copies or code that runs over more than one line. Escape `<`, `>` and `&` inside it. No wrapper and no button of your own."
      - name: "<script src=\"copy.js\" defer>"
        does: "Once per page, at the foot. It finds every `<pre>` on the page and adds the control."
      - name: ".ds-code, .ds-code-copy"
        does: "The wrapper and the button. The script writes both; never hand-build them."
      - name: "[data-no-copy]"
        does: "On a `<pre>`, opts that block out — for a block that is an illustration of output rather than something to take away."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A) and [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)"
  - id: panel-label
    title: "Panel label"
    summary: "The small uppercase Condensed label that names a panel, a column or a group. It is not a heading level and stays out of the document outline — if a reader needs to navigate to it, it is an `h3` or an `h4` at the sizes above."
    classes:
      - name: ".ds-panel-label"
        does: "One class for the whole system: 0.75rem · 600 · Condensed · uppercase · 0.04em · `--ds-text-muted`. Use it wherever this treatment appears — panel headings, column labels, the label above a group of controls — on whichever element is semantically right. A component that owns its internal spacing takes the margin back."
    notes:
      - "Do not reach for it as a heading substitute. A label that a reader needs to navigate to is a heading."
rules:
  - "One family, three contexts. Internal tools and the public site share the working set; [outreach properties](../outreach.html) add the upright serif and the heaviest sans. A face without a mark is not used in that context."
  - "**700 is the ceiling.** IBM Plex ships no heavier weight, so a CSS `800` either falls back or gets faux-bolded, differently per browser. Ask for the weight that exists."
  - "**Two serif jobs, kept apart.** Upright serif is the editorial voice — headlines, quotes, drop caps. Italic serif stays the annotation voice everywhere. A heading that must not read as \"another article\" uses the heavy *sans* instead, which is why 700 exists in this context at all."
  - "**Mono as display type** is an outreach liberty: the typewriter register echoes the main site's identifiers. On the public site, mono still means \"this is an identifier or code.\""
  - "Space is given as spacing tokens, not pixels, because that is what `design-system.css` implements — `--ds-space-8` is 2rem, `--ds-space-6` is 1.5rem, and so on down the scale."
  - "**On a laptop, the ratio is 1.25** — a major third — rounded to quarter-rem steps: 1, 1.25, 1.5, 2rem. A strict geometric run would put h2 at 1.5625rem; a quarter of a rem is the number a person can hold in their head and type without checking. The rounding is what makes h1 land on exactly double the body size."
  - "**700 appears once, at h1.** IBM Plex ships nothing heavier, so 700 is the ceiling and it is spent on the one heading that names the page. Everything below is 600. Always state the weight: a rule that sets only `font-size` inherits the browser default bold, which is how several pages ended up with an h3 heavier than the h2 above it."
  - "**Space above is at least twice the space below.** A heading belongs to the text it introduces, not the text it follows, and the gap has to say so. The values sit on the 4px rhythm in [Spacing](spacing.md)."
  - "**The page heading scales with the screen, and the steps shrink with it.** A step can shrink but never disappear: each level is at least a quarter of a rem (4px) larger than the one below. Most of its size is in rem and the largest is less than 2.5 times the smallest, so browser zoom scales it fully (WCAG 1.4.4); text-only zoom scales only the rem part, so there it grows a little less than body text."
  - "**The 11px uppercase Condensed label is not a heading level.** Set in `--ds-font-condensed` and `--ds-text-muted`, it marks a panel or a column and stays out of the document outline. If a reader needs to navigate to it, it is an h3 or an h4 at the size above, not a label."
  - "**There is no markup for the button**, and that is the design. `copy.js` finds every `<pre>` on the page, wraps it in `.ds-code` and inserts the control, which is `.ds-code-copy`. A block added next year is covered without anyone remembering, which a per-block wrapper would not be. Every page under `docs/` already loads the script."
  - "**The button sits over the top corner of the code, on a solid ground.** The block keeps even padding, and a long line that scrolls under the button is hidden behind it rather than showing through."
  - "**It is an icon, and it still says “Copy”.** The two overlapping sheets are the glyph people already know, so the control needs no label taking up room over the code. Both SVGs are `aria-hidden` and the button has `aria-label=\"Copy code\"`, which is what a screen reader announces. A block inside a `<figure>` is named by its `<figcaption>` instead: “Copy BibTeX” for a paper's citation. The `title` is the pointer affordance only — assistive technology takes the `aria-label` and ignores it."
  - "**Success is announced, not just shown.** The icon becomes a green tick, and the status region says “Copied to clipboard”, as in [Show that something was copied](action-feedback.md)."
  - "**It works from disk.** The asynchronous Clipboard API needs a secure context, which `file://` is not, and it rejects when the window is not focused. Both cases fall back to `execCommand`, and if that fails too the status region says so rather than the button quietly doing nothing. Either way, focus stays on the button."
  - "**A block wider than its box can be reached by keyboard.** When a line of code is too long to show, the script adds `tabindex=\"0\"` to the block, so a keyboard user can tab to it and scroll it with the arrow keys. It does this for every block, opted out or not, and takes it away again when the window is wide enough to show the whole block."
  - "**Without JavaScript there is no button** and the code is still selectable. The button is a convenience; it is never the only way to get the text."
  - "**Opt a block out with `<pre data-no-copy>`** — for a block that is an illustration of output rather than something to take away."
  - "A browser font-size setting has to reach arXiv content (accessibility-priorities.md, cognitive/dyslexia section), so every type size is `rem`. But a label that grows inside a box that does not is no better than a label that never grew: set a control's padding and minimum width in `em`, against its own label, and the whole control follows the reader. Absolute floors stay absolute — `min-height: 24px` is a WCAG target size, not a type size. Body text never scales fluidly — it follows the user's base size exactly."
  - "No Google Fonts, no Typekit, no CDN fonts (DESIGN-POLICIES.md). Every `font-family` declaration includes system fallbacks; text fonts load with `font-display: swap` (readability first), STIX Two Math with `font-display: auto` (math must render in the correct face)."
  - "No fixed line-heights, no pinned letter-spacing, no `!important` on font-family in content areas. User stylesheets, reader-mode extensions, and OS settings win — \"HTML gives you freedom: you can use software to change colors or typefaces\" (research, dyslexia section)."
  - "**Keep the heading order.** One `<h1>` per page, then `<h2>`, `<h3>` and `<h4>` in order, without skipping a level, inside a card too. Choose the level from the outline, not from the size you want; the scale gives each level its size. A screen reader user moves through the page by these levels."
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

Body text — paragraphs, author names, abstracts, UI.

Labels — metadata labels, table headers, uppercase section labels.

Code & identifiers — arXiv IDs, DOIs, BibTeX, code blocks.

Annotation voice — footnote text and figure alt-text in the reader margins. “The editor speaking quietly next to the body text.”

Mathematical notation.

```html
font-family: var(--ds-font-sans);
```

- `--ds-font-sans` — The default: where no other face applies, this is the answer. Weights 400 / 500 / 600.

```html
font-family: var(--ds-font-condensed);
```

- `--ds-font-condensed` — Labels, table headers and metadata, usually small and uppercase. Weights 500 / 600.
- `.ds-panel-label` — The ready-made label in this face; see [Panel label](#panel-label) below.

```html
font-family: var(--ds-font-mono);
```

- `--ds-font-mono` — Identifiers and code. Weights 400 / 500. Inline `<code>` and `<pre>` already use it; see [Code blocks](#code-blocks-and-the-copy-button) below.

```html
<p class="ds-annotation">Figure 2: the scalaron potential.</p>
```

- `.ds-annotation` — The annotation voice: `--ds-font-serif`, italic, 400, 0.8125rem, `--ds-text-muted`. It is a voice, not a layout role; where it sits is the consumer's decision.
- `--ds-font-serif` — The serif stack. On the public site and in internal tools it is used only through `.ds-annotation`.

```html
font-family: "STIX Two Math", "Cambria Math", math;
```

- `<math>` — No font token exists for math; use the stack directly on the notation. Loads with `font-display: auto` per DESIGN-POLICIES.

## The body text scale

The text sizes are set in rem so they move with the reader's base size. Browsers set the base size to 16px unless the reader changes it, so 1rem is 16px by default; the pixel sizes on this page assume that default.

```html
<p>Body text.</p>
<small>Secondary text.</small>
<p class="ds-annotation">A margin footnote.</p>
<p class="ds-panel-label">Paper information</p>
<p>An identifier: <code>arXiv:2604.22725</code></p>
```

- `<p>` — 1rem, the reader's base size. Nothing sets it; the browser does.
- `<small>` — 0.875rem in `--ds-text-muted`.
- `<pre>` — 0.875rem, line-height 1.6, on the dark chrome ground.
- `.ds-annotation` — 0.8125rem, serif italic, line-height 1.45.
- `.ds-panel-label` — 0.75rem, condensed, uppercase.
- `<code>` — 0.9em, so it follows the size of its parent. When to use it rather than a block: [Code blocks and the copy button](#code-blocks-and-the-copy-button).

> Meets accessibility guideline [WCAG 2.2 SC 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) Resize Text (Level AA)

## The heading scale

Four levels, each larger than the one below it. On a laptop the step is about a quarter, which puts h1 at twice body size; on a phone it is 4px, so a long title takes fewer lines. Sizes are in rem so they follow the user's base setting. That base is 16px unless the reader has changed the browser's default, so the pixel sizes below assume 16px.

```html
<h1>Gauge-independent approach to inflation</h1>
  <h2>Submission history</h2>
    <h3>Gauge-invariant perturbations</h3>
      <h4>Boundary conditions</h4>
```

- `<h1>` — The page's one subject: what the page is about, stated once — a paper title, a form name, a console view. A page that seems to need two h1s is two pages. `clamp(1.75rem, 1rem + 2vw, 2rem)`: 28px on a phone, 32px from about 800px wide · 700 · line-height 1.25 · space above 0, below `--ds-space-4`.
- `<h2>` — A major section: a top-level division of that subject — Abstract, Submission history, References, each step of a submission form. 1.5rem (24px) · 600 · line-height 1.25 · space above `--ds-space-8`, below `--ds-space-3`.
- `<h3>` — A division inside one section: a subsection of a paper, or a card heading inside a panel. It only exists where an h2 already does. 1.25rem (20px) · 600 · line-height 1.25 · space above `--ds-space-8`, below `--ds-space-2`.
- `<h4>` — The smallest named step: a named paragraph in a paper, a field group in a form. This is the last level the scale defines; needing an h5 is a sign the content wants restructuring, not a fifth size. 1rem (16px) · 600 · line-height 1.25 · space above `--ds-space-4`, below `--ds-space-2`.

## Text links

Links are typography too. Inline links in body text are always underlined (to pass WCAG 1.4.1). Standalone navigation links and groups of links that are not part of body text (headers, footers, author list) drop the underline to reduce noise.

Full state-by-state references (rest / hover / visited / focus / disabled, light and dark): [Links](links.md). Link color tokens with ratios: [Colors](colors.md).

```html
Reading text with <a href="/abs/2604.22725">an inline link</a> in it.
```

- `.ds-link` — The inline text link. Both surfaces use `.ds-link` and the `--ds-link-*` tokens: the same grammar, the same names and the same values. Inside a `.ds-page` a bare `<a>` gets the same treatment without the class.
- `--ds-link, --ds-link-hover, --ds-link-visited` — Rest, hover and visited colours. The underline does not change between states.
- `--ds-focus-ring` — The 3px keyboard focus ring, drawn on `:focus-visible` only.

```html
<p class="ds-link-list">
  <a href="/a/palomares_a_1">Adrian Palomares</a>,
  <a href="/a/chen_m_1">Mei Lin Chen</a>,
  <a href="/a/mensah_k_1">Kwame Mensah</a>
</p>
```

- `.ds-link-list` — On the element that holds a list in which every item is a link, such as an author list or a column of footer links. The links drop the underline at rest and keep everything else: Link Blue, the underline on hover, the focus ring and the visited colour. There is no ordinary text beside them for the underline to separate them from, so colour alone is enough here.

> Meets accessibility guideline [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)

## Search-matched words

The words that matched a search are marked with `<mark>`, in the accent wash and a heavier weight.

```html
<p>Weak-<mark>Lensing</mark> Shear Response for Photometric Redshift-Based Tomographic Binning</p>
```

- `<mark>` — One matched word or phrase. No class: the element is styled inside `.ds-page`. The weight marks it as well as the colour, so it is never colour alone. In internal tools the wash is Access Lime.

> Meets accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A) and [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA)

## Code blocks and the copy button

A code block uses Plex Mono on Repository Brown, and always includes a copy button. Use a block for code a reader copies, or code that runs over more than one line. A short name or example in running text that a reader would not copy, such as a file name or a list of allowed characters, is inline `<code>`, which has no button.

```html
<!-- A name in running text: inline -->
<p>The main action on a page takes <code>.ds-btn-primary</code>:</p>

<!-- Code to copy: a block, written the way you already do -->
<pre><code>&lt;button class="ds-btn ds-btn-primary" type="button"&gt;Save&lt;/button&gt;</code></pre>

<!-- And include the script once, at the foot of the page -->
<script src="copy.js" defer></script>
```

- `<code>` — Inline code: a short name or example inside a sentence, which a reader would not copy. No copy button.
- `<pre><code>` — The block, for code a reader copies or code that runs over more than one line. Escape `<`, `>` and `&` inside it. No wrapper and no button of your own.
- `<script src="copy.js" defer>` — Once per page, at the foot. It finds every `<pre>` on the page and adds the control.
- `.ds-code, .ds-code-copy` — The wrapper and the button. The script writes both; never hand-build them.
- `[data-no-copy]` — On a `<pre>`, opts that block out — for a block that is an illustration of output rather than something to take away.

> Meets accessibility guidelines [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A) and [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)

## Panel label

The small uppercase Condensed label that names a panel, a column or a group. It is not a heading level and stays out of the document outline — if a reader needs to navigate to it, it is an `h3` or an `h4` at the sizes above.

The test: if a paragraph follows it, or it covers several examples, it is a heading. Otherwise it is a panel label, naming the one example directly below it. A panel label is a few words, never a sentence. Public and internal versions of one example take panel labels.

```html
<p class="ds-panel-label">Paper information</p>
```

- `.ds-panel-label` — One class for the whole system: 0.75rem · 600 · Condensed · uppercase · 0.04em · `--ds-text-muted`. Use it wherever this treatment appears — panel headings, column labels, the label above a group of controls — on whichever element is semantically right. A component that owns its internal spacing takes the margin back.

> Do not reach for it as a heading substitute. A label that a reader needs to navigate to is a heading.

## Rules

### Which faces where — the three contexts

One family, three contexts. Internal tools and the public site share the working set; [outreach properties](../outreach.html) add the upright serif and the heaviest sans. A face without a mark is not used in that context.

| Face · weights | Internal tools | Public site | Outreach |
|---|---|---|---|
| IBM Plex Sans · 400 / 500 / 600 | ✓ all text | ✓ all text | ✓ all text |
| IBM Plex Sans · 700 + 700 *italic* | ✓ h1 only | ✓ h1 only | ✓ the one heading that must not read as an article |
| IBM Plex Sans Condensed · 500 / 600 | ✓ labels, table headers | ✓ labels | ✓ labels |
| IBM Plex Mono · 400 / 500 | ✓ IDs, code | ✓ arXiv IDs, code | ✓ code, plus a display register (wordmark, standfirst) |
| IBM Plex Serif · 400 *italic* | annotation voice only (`.ds-annotation`) | annotation voice only (`.ds-annotation`) | ✓ emphasis, bylines, prev/next |
| IBM Plex Serif · 400 / 600 upright | — | — | ✓ headlines to display size, pull quotes, drop caps |
| STIX Two Math · 400 | — | ✓ math in HTML papers | — |

- **700 is the ceiling.** IBM Plex ships no heavier weight, so a CSS `800` either falls back or gets faux-bolded, differently per browser. Ask for the weight that exists.
- **Two serif jobs, kept apart.** Upright serif is the editorial voice — headlines, quotes, drop caps. Italic serif stays the annotation voice everywhere. A heading that must not read as "another article" uses the heavy *sans* instead, which is why 700 exists in this context at all.
- **Mono as display type** is an outreach liberty: the typewriter register echoes the main site's identifiers. On the public site, mono still means "this is an identifier or code."

### Headings

Space is given as spacing tokens, not pixels, because that is what `design-system.css` implements — `--ds-space-8` is 2rem, `--ds-space-6` is 1.5rem, and so on down the scale.

- **On a laptop, the ratio is 1.25** — a major third — rounded to quarter-rem steps: 1, 1.25, 1.5, 2rem. A strict geometric run would put h2 at 1.5625rem; a quarter of a rem is the number a person can hold in their head and type without checking. The rounding is what makes h1 land on exactly double the body size.
- **700 appears once, at h1.** IBM Plex ships nothing heavier, so 700 is the ceiling and it is spent on the one heading that names the page. Everything below is 600. Always state the weight: a rule that sets only `font-size` inherits the browser default bold, which is how several pages ended up with an h3 heavier than the h2 above it.
- **Space above is at least twice the space below.** A heading belongs to the text it introduces, not the text it follows, and the gap has to say so. The values sit on the 4px rhythm in [Spacing](spacing.md).
- **The page heading scales with the screen, and the steps shrink with it.** A step can shrink but never disappear: each level is at least a quarter of a rem (4px) larger than the one below. Most of its size is in rem and the largest is less than 2.5 times the smallest, so browser zoom scales it fully (WCAG 1.4.4); text-only zoom scales only the rem part, so there it grows a little less than body text.
- **The 11px uppercase Condensed label is not a heading level.** Set in `--ds-font-condensed` and `--ds-text-muted`, it marks a panel or a column and stays out of the document outline. If a reader needs to navigate to it, it is an h3 or an h4 at the size above, not a label.

### The copy button

- **There is no markup for the button**, and that is the design. `copy.js` finds every `<pre>` on the page, wraps it in `.ds-code` and inserts the control, which is `.ds-code-copy`. A block added next year is covered without anyone remembering, which a per-block wrapper would not be. Every page under `docs/` already loads the script.
- **The button sits over the top corner of the code, on a solid ground.** The block keeps even padding, and a long line that scrolls under the button is hidden behind it rather than showing through.
- **It is an icon, and it still says “Copy”.** The two overlapping sheets are the glyph people already know, so the control needs no label taking up room over the code. Both SVGs are `aria-hidden` and the button has `aria-label="Copy code"`, which is what a screen reader announces. A block inside a `<figure>` is named by its `<figcaption>` instead: “Copy BibTeX” for a paper's citation. The `title` is the pointer affordance only — assistive technology takes the `aria-label` and ignores it.
- **Success is announced, not just shown.** The icon becomes a green tick, and the status region says “Copied to clipboard”, as in [Show that something was copied](action-feedback.md).
- **It works from disk.** The asynchronous Clipboard API needs a secure context, which `file://` is not, and it rejects when the window is not focused. Both cases fall back to `execCommand`, and if that fails too the status region says so rather than the button quietly doing nothing. Either way, focus stays on the button.
- **A block wider than its box can be reached by keyboard.** When a line of code is too long to show, the script adds `tabindex="0"` to the block, so a keyboard user can tab to it and scroll it with the arrow keys. It does this for every block, opted out or not, and takes it away again when the window is wide enough to show the whole block.
- **Without JavaScript there is no button** and the code is still selectable. The button is a convenience; it is never the only way to get the text.
- **Opt a block out with `<pre data-no-copy>`** — for a block that is an illustration of output rather than something to take away.

### Sizes are rem, and a box that holds text scales with its text

A browser font-size setting has to reach arXiv content (accessibility-priorities.md, cognitive/dyslexia section), so every type size is `rem`. But a label that grows inside a box that does not is no better than a label that never grew: set a control's padding and minimum width in `em`, against its own label, and the whole control follows the reader. Absolute floors stay absolute — `min-height: 24px` is a WCAG target size, not a type size. Body text never scales fluidly — it follows the user's base size exactly.

### Self-hosted, with honest fallbacks

No Google Fonts, no Typekit, no CDN fonts (DESIGN-POLICIES.md). Every `font-family` declaration includes system fallbacks; text fonts load with `font-display: swap` (readability first), STIX Two Math with `font-display: auto` (math must render in the correct face).

### Do not fight the reader

No fixed line-heights, no pinned letter-spacing, no `!important` on font-family in content areas. User stylesheets, reader-mode extensions, and OS settings win — "HTML gives you freedom: you can use software to change colors or typefaces" (research, dyslexia section).

### Accessibility essentials

- **Keep the heading order.** One `<h1>` per page, then `<h2>`, `<h3>` and `<h4>` in order, without skipping a level, inside a card too. Choose the level from the outline, not from the size you want; the scale gives each level its size. A screen reader user moves through the page by these levels.
- **Write sizes in rem, never in px.** A reader who raises the browser font size must see every piece of text grow. Give a control its padding and minimum width in `em`, so the box grows with its label.
- **Let text reflow at 200% zoom.** Do not give a box that holds text a fixed height, and do not cut text off with `overflow: hidden` unless there is another way to read all of it. At 400% page zoom a 1280px screen is a 320px screen, and the page must not scroll sideways there.
- **Put text in text, not in images.** An image of words cannot be resized, translated, searched or read aloud. If an image must include words, the same words go in its `alt` text or next to it.
- **Uppercase comes from CSS, never from the keyboard.** The panel label is uppercase because `.ds-panel-label` makes it so. Type it in sentence case, so copy-and-paste, search and screen readers get the real words.

## Spec

### Why IBM Plex

Open source under the SIL Open Font License, so there is no licensing cost and no vendor dependency; self-hostable as woff2 from arXiv's own assets; one designer's family covering Sans, Condensed, Mono and Serif so nothing is mixed; broad language coverage including Latin Extended, Cyrillic, Greek, Arabic, Hebrew, Devanagari and Thai; and it pairs with STIX Two Math, which is built for the same technical context. The family was re-evaluated in June 2026 against Atkinson Hyperlegible Next, Source Sans 3, Inter and Public Sans, and kept — that comparison lives in [whiteboard/planning/proposals](../doc.html?src=whiteboard/planning/proposals/typeface-re-evaluation-2026-06.md), not here.

### Tokens

```
--ds-font-sans:      "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
--ds-font-condensed: "IBM Plex Sans Condensed", "IBM Plex Sans", sans-serif;
--ds-font-mono:      "IBM Plex Mono", ui-monospace, "SF Mono", Menlo, monospace;
--ds-font-serif:     "IBM Plex Serif", Georgia, "STIX Two Text", "Times New Roman", serif;
```

Every stack includes system fallbacks so text stays readable if the web fonts fail: sans falls to the OS system font, mono to the platform monospace. **There is no math token** — STIX Two Math is applied by the paper renderer on HTML paper pages, not by the design system, so the stylesheet does not declare one.

### Available weights, and sanctioned ones

Every weight and style IBM Plex ships is self-hosted — Thin 100, ExtraLight 200, Light 300, Regular 400, Text 450, Medium 500, SemiBold 600 and Bold 700, each with an italic, across Sans, Sans Condensed, Mono and Serif. That is 64 files and about 4 MB in the repository, and it costs a reader nothing: a `@font-face` rule downloads only when a page uses that face.

**Available is not the same as approved.** Only the faces the design system uses are declared in [fonts.css](../fonts.css); the rest are present but commented out, so you can see what exists without going to look for it. Uncommenting one is how you turn it on — and it is a decision, not a formality.

| Weight | Use it for |
|---|---|
| 400 Regular | Body copy, and anything that is read rather than scanned. |
| 500 Medium | Navigation, table headers, the quieter emphasis. |
| 600 SemiBold | Headings, button labels, and the label half of a label/value pair. |
| 700 Bold | The h1, and nothing else — see the heading scale. |
| 100, 200, 300, 450 | Lighter weights are present, but unused and commented out. See warning below. |

Thin, ExtraLight and Light are in the repository but not used. At interface sizes their strokes are too fine for many readers to resolve even when the colour passes AA — the ratio measures the hue, not whether the letterform survives. **Body and interface text use 400 or heavier.** Anything lighter belongs at display sizes, if anywhere, and is worth testing before it ships.

### The files

Self-hosted woff2, from arXiv's static assets. No external font service — see [DESIGN-POLICIES](../doc.html?src=docs/DESIGN-POLICIES.md) for why that one is a hard constraint.

```
/static/fonts/
  IBMPlexSans-*.woff2            8 weights x roman/italic  = 16 files
  IBMPlexSansCondensed-*.woff2   8 weights x roman/italic  = 16 files
  IBMPlexMono-*.woff2            8 weights x roman/italic  = 16 files
  IBMPlexSerif-*.woff2           8 weights x roman/italic  = 16 files
  STIXTwoMath-Regular.woff2      ← HTML paper pages only
```

This repo's pattern pages serve the same files from `docs/fonts/`, declared in [fonts.css](../fonts.css), which every page links ahead of the stylesheet. The `@font-face` rules live in that separate file rather than in the design system itself, because consumers bundle the design system with their own font paths. Files come from [IBM/plex](https://github.com/IBM/plex) (OFL).

### @font-face

```
@font-face {
  font-family: "IBM Plex Sans";
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexSans-Regular.woff2") format("woff2");
}
/* …one per weight and style… */

@font-face {
  font-family: "STIX Two Math";
  font-weight: 400;
  font-display: auto;
  src: local("STIX Two Math"),
       url("/static/fonts/STIXTwoMath-Regular.woff2") format("woff2");
}
```

- `font-display: swap` for text: the fallback shows immediately and swaps when the real font arrives. Readability beats visual stability.
- `font-display: auto` for STIX Two Math: maths in a fallback font can be actively wrong, so it is better to wait briefly.
- `local()` for STIX Two Math skips the ~300KB download if the reader already has it.
- Total: about 135KB for the Plex woff2 files, plus STIX only on paper pages.

### Which faces each surface uses

| Surface | Body | Labels | Code | Math |
|---|---|---|---|---|
| Abstract pages | Plex Sans | Plex Sans Condensed | Plex Mono | — |
| HTML paper pages | Plex Sans | Plex Sans Condensed | Plex Mono | STIX Two Math |
| Internal tools | Plex Sans | Plex Sans Condensed | Plex Mono | — |
| Homepage, listings, search | Plex Sans | Plex Sans Condensed | Plex Mono | — |

### Sizes in use

The sizes the stylesheet sets, in rem, with the pixel size at the browser's default base size of 16px.

| Use | Size | Weight | Face |
|---|---|---|---|
| Page heading (h1) | 1.75–2rem · 28–32px | 700 | Plex Sans |
| Section heading (h2) | 1.5rem · 24px | 600 | Plex Sans |
| Subsection heading (h3) | 1.25rem · 20px | 600 | Plex Sans |
| h4; body text | 1rem · 16px | 600; 400 | Plex Sans |
| Secondary text, captions | 0.875rem · 14px | 400 | Plex Sans |
| Code blocks | 0.875rem · 14px | 400 | Plex Mono |
| Inline code, identifiers | 0.9em of the text around it | 400 | Plex Mono |
| Annotation (margin footnote, alt text) | 0.8125rem · 13px, italic | 400 | Plex Serif |
| Header links | 0.8125rem · 13px | 500 | Plex Sans |
| Panel labels, table headers | 0.75rem · 12px, uppercase | 600 | Plex Sans Condensed |
