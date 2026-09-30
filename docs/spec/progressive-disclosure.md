---
page: progressive-disclosure.html
title: "Progressive disclosure"
summary: "Options to toggle open additional content. HTML paper pages, for example, hold far more than a reader wants to see all at once, so they use every progressive disclosure mechanism we have: A \"show more\" link to toggle open a full author list, accordions for secondary metadata, and popovers for footnotes."
stylesheet: design-system.css
components:
  - id: accordion
    title: "Accordion"
    summary: "Using the native `<details>/<summary>` elements means no JavaScript is needed, and accordions are keyboard and screen-reader friendly by default. Another bonus is that the browser's find-in-page can open a closed panel to show a match inside it. A +/− glyph replaces the default marker."
    classes:
      - name: ".ds-acc"
        does: "On a `<details>`. Ruled: no box, no fill, no horizontal padding. The label sits on the same left edge as the prose around it, with a rule above and below. The `<summary>` is the label; the +/− marker comes from the stylesheet."
      - name: ".ds-acc-body"
        does: "Holds the panel content, directly after the `<summary>`. A `<dl>` inside it renders as label and value pairs, one column on a narrow screen."
      - name: ".ds-acc-stack"
        does: "The container for a list of disclosures. Stacked in it they butt together and read as one ruled list: each shared edge is a single line, because the preceding item's lower rule is the next item's upper one."
      - name: "[open]"
        does: "Present on the one panel that starts open, if any. See [Which affordance](#which-affordance) under Rules."
  - id: show-more
    title: "Show more"
    summary: "While an accordion hides an entire labelled section, the 'show more' control reveals the hidden *tail end* of partially displayed content. When hiding the remainder of a list we display the additional item count in the link."
    classes:
      - name: ".ds-show-more"
        does: "On a `<button type=\"button\">` at the end of the visible part. It takes the link colour, because in running text it is the one thing a reader can act on. An accordion is `<details>`, so the browser supplies the semantics; a tail cannot be, so this is a real `<button>` that has to declare for itself what the browser would otherwise have said, with the three attributes below."
      - name: ".ds-show-more--among-links"
        does: "For a tail at the end of a run of links, such as an author list: grey and italic, so the control does not read as one more link."
      - name: "[aria-expanded]"
        does: "`\"false\"` / `\"true\"`, flipped on every toggle. Without it the control announces as a button that does something unspecified."
      - name: "[aria-controls]"
        does: "The id of the region it reveals."
      - name: "[hidden]"
        does: "On the region, the attribute and not a class. The hidden names are then out of the tab order and out of find-in-page while they are off screen, and the collapse still works with no CSS loaded at all."
      - name: "[data-open-label]"
        does: "Read by the script on this page: the label while the tail is open. The closed label is the button's own text."
    notes:
      - "A tail cannot be a details element, because a summary would put a heading in the middle of a sentence."
  - id: popover
    title: "Popover"
    summary: "A quick lookup the reader can access without losing their place. Popovers are used on HTML papers pages for citations and footnotes, which is especially helpful for screen reader users. Popovers can contain nearly any type of content including links but should be used only for short bursts of information."
    classes:
      - name: ".ds-popover"
        does: "The panel. It is `position: fixed`: the host sets `top` and `left`, and moves it to `<body>` if the trigger has a transformed ancestor. Closed, it carries the `hidden` attribute."
      - name: ".ds-popover-title"
        does: "The label line at the top of the panel. It leaves room for the close control."
      - name: ".ds-close"
        does: "The close control, the same one the alert and the announcement band use, documented on [Buttons](buttons.html#the-close-control). The popover supplies its corner position and nothing else. It needs a `<span class=\"is-sr-only\">` that says what it closes."
      - name: "[role=\"region\"], [aria-label]"
        does: "Together they make the panel a named landmark, so a screen reader user can find it and hear what it holds."
      - name: "--ds-popover-width, --ds-popover-max-height"
        does: "Set per use; past that height it scrolls, and `overscroll-behavior: contain` stops that scroll running on into the page beneath once it reaches the end."
      - name: ".ds-inline-active"
        does: "On the trigger while its popover is open: a light-blue wash and an underline, so a reader glancing back at the paragraph can see which citation the panel belongs to. Pair it with `aria-expanded` on the trigger, which is what carries the same fact to a screen reader; the wash is the visible half of one state, not a decoration."
    notes:
      - "Popovers resize to the content but should be reserved for short pieces of information. If the content gets too long it may not be contained within the viewport."
  - id: toc-bar
    title: "TOC bar"
    summary: "Need in-page navigation? The TOC bar is a row that carries a single disclosure control, which opens a list of the page’s sections. The bar is always sticky and it stays at the top of the viewport while the reader scrolls through the page."
    classes:
      - name: ".ds-toc"
        does: "The control, a `<details>`. It works on its own anywhere, and it opens with JavaScript off."
      - name: ".ds-toc-trigger"
        does: "The `<summary>`. Holds the list icon, `.ds-toc-text` with its `.ds-toc-prefix`, and `.ds-toc-chevron`."
      - name: ".ds-toc-menu"
        does: "The list, a `<nav>` holding an `<ol>`. The link to the current section gets `.is-current`. A page whose sections are numbered puts each number in `.ds-toc-num`."
      - name: ".ds-toc-bar"
        does: "The edge-to-edge row that carries the control. A direct child of `.ds-container`, with `.ds-full`. Placed directly before `.ds-zone-primary`, it sits on that zone’s top edge. The bar is always sticky: it keeps to the top of the viewport, where it becomes `.is-stuck` and tightens, and it sets `scroll-padding-top` so an anchor lands below it. Sticky chrome is governed by [DESIGN-POLICIES](doc.html?src=docs/DESIGN-POLICIES.md); check there before adding the bar to a page."
      - name: ".ds-toc-bar-inner"
        does: "The bar’s three-slot grid, which keeps the control centred whatever sits beside it."
      - name: "[data-toc-scope]"
        does: "Optional, on `.ds-toc`: a selector for the element whose headings fill an empty list. Without it, `toc.js` reads `<main>`, or the whole page when there is no `<main>`."
  - id: accordion-inside-a-card
    title: "Accordion inside a card"
    group: "Variants"
    summary: "A disclosure inside another one is the second level: indented one step, its label a step smaller. Two levels is the limit a reader can keep track of. Shown inside a card with a heading, the paper reader's sidebar, where the stack ends the card and the card's own edge closes it."
    classes:
      - name: ".ds-acc inside .ds-acc-body"
        does: "The second level. Indented one step, its label a step smaller."
      - name: ".ds-card > .ds-acc-stack:last-child"
        does: "A stack that ends a card drops the last disclosure's lower rule, because the card's edge closes it. With content below the stack, the rule stays."
      - name: "h3 before the stack"
        does: "The heading names the group, so it is found by heading navigation and every disclosure inside it is announced under that name."
rules:
  - "**Never put must-see information only behind a disclosure.** The older-version warning appears in the main column even though the full history lives in the Versions accordion. A reader who never opens anything must still meet everything that matters."
  - "**Disclosure is not a fix for too much content.** If a page needs six accordions to be tolerable, the page has a structure problem and hiding things postpones it. Ask what can be cut or moved before asking what can be collapsed."
  - "**Default state is closed**, except that a single most-relevant panel may start open. Open state is not persisted — predictability beats memory here."
  - "**One panel, one label.** If a summary needs a sentence to explain what is inside, the content is not a section and probably wants show-more or a page of its own."
  - "**Show more among links is grey and italic.** At the end of a run of links — author names, category links — a Link Blue “show all 22 authors” is one more link in that run, indistinguishable from a name. It is not a link: it goes nowhere, it changes this page. Reading as a different *kind* of thing than its neighbours is the whole job, which is what `.ds-show-more--among-links` is for. Anywhere else, the default link colour is right."
  - "**Never put content in a popover that exists nowhere else.** A popover is a shortcut to something already on the page or already at a URL — the reference list, the footnote. It is not a place to store text."
  - "**Nothing animates.** These components have no transitions, so there is nothing for `prefers-reduced-motion` to switch off. An accordion that animates its height also animates the position of everything below it, which is motion a reader did not ask for."
  - "**A popover sits above sticky chrome** (`z-index: 110`, per the [Z-layer scale](doc.html?src=docs/DESIGN-POLICIES.md)). A popover is always the thing the reader just asked for, so it is never the thing that gets hidden."
  - "**Prefer native markup.** Where a disclosure can be a `<details>` element, as the accordion and the TOC bar are, use it. It carries the expanded state, the keyboard behaviour and the announcement without any script, and find-in-page can open a closed panel to reveal a match. A hand-built accordion loses all four, and losing find-in-page on a research site is the expensive one."
  - "**In a `<details>`, the summary is the whole label.** Never put a second interactive control inside it — a link or button in a `<summary>` is reachable but its activation fights the disclosure's own."
  - "**Hide with the `hidden` attribute, not with a class.** Content hidden by a class that fails to load is invisible but still tabbable, which puts a keyboard user in a place they cannot see."
  - "**Every custom toggle owns `aria-expanded`.** A show-more button and a popover trigger are not `<details>`, so they state it themselves. Its absence is the single most common defect in this pattern: the control announces as a button, does something visible to everyone else, and says nothing."
  - "**A show-more label counts what it hides.** “show all 22 authors”, not “show more”, whenever the hidden part is a list. A reader deciding whether to expand is asking how much is behind it, and someone using a screen reader hears the control with no view of the list at all. Return the label to “show fewer” when open."
  - "**Escape closes a popover and returns focus** to the chip that opened it. A reader who opened it from the keyboard must not be stranded at the end of the document. Close it on outside click and on scroll as well: the panel is `position: fixed`, so left open it would follow the viewport while the sentence it belongs to scrolls away."
  - "**The TOC bar's list is a disclosure, not an ARIA menu.** `role=\"menu\"` is for application menus — the kind with arrow-key roving focus and menu items that are not links. A list of links is a disclosure, and W3C’s own guidance is to build it this way. Using `role=\"menu\"` here would make a screen reader promise keyboard behaviour the component does not have."
  - "**Mark where the reader is.** `toc.js` gives the TOC bar's link to the current section `aria-current=\"location\"`."
  - "**Everything is reachable from the keyboard, with JavaScript off.** Open, close and keyboard operation are native; outside-click and Escape are enhancements layered on top. Escape closes the TOC bar's list and returns focus to its control, but only when focus was inside the list — Escape pressed elsewhere on the page must not move it."
---

# Progressive disclosure

Options to toggle open additional content. HTML paper pages, for example, hold far more than a reader wants to see all at once, so they use every progressive disclosure mechanism we have: A "show more" link to toggle open a full author list, accordions for secondary metadata, and popovers for footnotes.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Accordion

Using the native `<details>/<summary>` elements means no JavaScript is needed, and accordions are keyboard and screen-reader friendly by default. Another bonus is that the browser's find-in-page can open a closed panel to show a match inside it. A +/− glyph replaces the default marker.

```html
<div class="ds-acc-stack">
  <details class="ds-acc" open>
    <summary>Versions</summary>
    <div class="ds-acc-body">
      <dl>
        <dt>v3 · current</dt><dd>24 Apr 2026</dd>
        <dt>v2</dt><dd><a href="#">2 Mar 2026</a></dd>
        <dt>v1</dt><dd><a href="#">10 Jan 2026</a></dd>
      </dl>
    </div>
  </details>
  <details class="ds-acc">
    <summary>Paper information</summary>
    <div class="ds-acc-body">
      <dl>
        <dt>arXiv ID</dt><dd><a href="#">2604.22725</a></dd>
        <dt>Subjects</dt><dd>gr-qc · hep-th</dd>
        <dt>Licence</dt><dd><a href="#">CC BY 4.0</a></dd>
      </dl>
    </div>
  </details>
  <details class="ds-acc">
    <summary>Related</summary>
    <div class="ds-acc-body">Connected papers, datasets, and code links.</div>
  </details>
</div>
```

- `.ds-acc` — On a `<details>`. Ruled: no box, no fill, no horizontal padding. The label sits on the same left edge as the prose around it, with a rule above and below. The `<summary>` is the label; the +/− marker comes from the stylesheet.
- `.ds-acc-body` — Holds the panel content, directly after the `<summary>`. A `<dl>` inside it renders as label and value pairs, one column on a narrow screen.
- `.ds-acc-stack` — The container for a list of disclosures. Stacked in it they butt together and read as one ruled list: each shared edge is a single line, because the preceding item's lower rule is the next item's upper one.
- `[open]` — Present on the one panel that starts open, if any. See [Which affordance](#which-affordance) under Rules.

## Show more

While an accordion hides an entire labelled section, the 'show more' control reveals the hidden *tail end* of partially displayed content. When hiding the remainder of a list we display the additional item count in the link.

```html
<!-- The rest of a paragraph -->
<p>We study the convergence … under heavy-tailed noise<span id="abstract-tail" hidden>, and show that …</span>.
<button type="button" class="ds-show-more" aria-expanded="false" aria-controls="abstract-tail"
        data-open-label="show less">show more</button></p>

<!-- The rest of a countable list: the label carries the count -->
<p>Keywords: stochastic optimisation, …<span id="keywords-tail" hidden>, non-convex analysis, …</span>
<button type="button" class="ds-show-more" aria-expanded="false" aria-controls="keywords-tail"
        data-open-label="show fewer">show 4 more keywords</button></p>

<!-- The rest of a list of links -->
<ul>
  <li><a href="#">R. Almeida</a></li>
  …
  <li><a href="#">L. Cheng</a></li></ul><span id="authors-tail" hidden>, <a href="#">T. Okonkwo</a>, …</span>
<button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false"
        aria-controls="authors-tail" data-open-label="show fewer">… show all 22 authors</button>
```

- `.ds-show-more` — On a `<button type="button">` at the end of the visible part. It takes the link colour, because in running text it is the one thing a reader can act on. An accordion is `<details>`, so the browser supplies the semantics; a tail cannot be, so this is a real `<button>` that has to declare for itself what the browser would otherwise have said, with the three attributes below.
- `.ds-show-more--among-links` — For a tail at the end of a run of links, such as an author list: grey and italic, so the control does not read as one more link.
- `[aria-expanded]` — `"false"` / `"true"`, flipped on every toggle. Without it the control announces as a button that does something unspecified.
- `[aria-controls]` — The id of the region it reveals.
- `[hidden]` — On the region, the attribute and not a class. The hidden names are then out of the tab order and out of find-in-page while they are off screen, and the collapse still works with no CSS loaded at all.
- `[data-open-label]` — Read by the script on this page: the label while the tail is open. The closed label is the button's own text.

> A tail cannot be a details element, because a summary would put a heading in the middle of a sentence.

## Popover

A quick lookup the reader can access without losing their place. Popovers are used on HTML papers pages for citations and footnotes, which is especially helpful for screen reader users. Popovers can contain nearly any type of content including links but should be used only for short bursts of information.

```html
<span class="ds-popover" role="region" aria-label="Reference 47">
  <div class="ds-popover-title">Reference 47</div>
  <button type="button" class="ds-close">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
    <span class="is-sr-only">Close reference 47</span>
  </button>
  Ashtekar, A. and Bojowald, M. <em>Quantum geometry and the Schwarzschild singularity.</em>
  Class. Quantum Grav. 23 (2006).
  <a href="#">Jump to reference</a>
</span>
```

- `.ds-popover` — The panel. It is `position: fixed`: the host sets `top` and `left`, and moves it to `<body>` if the trigger has a transformed ancestor. Closed, it carries the `hidden` attribute.
- `.ds-popover-title` — The label line at the top of the panel. It leaves room for the close control.
- `.ds-close` — The close control, the same one the alert and the announcement band use, documented on [Buttons](buttons.html#the-close-control). The popover supplies its corner position and nothing else. It needs a `<span class="is-sr-only">` that says what it closes.
- `[role="region"], [aria-label]` — Together they make the panel a named landmark, so a screen reader user can find it and hear what it holds.
- `--ds-popover-width, --ds-popover-max-height` — Set per use; past that height it scrolls, and `overscroll-behavior: contain` stops that scroll running on into the page beneath once it reaches the end.
- `.ds-inline-active` — On the trigger while its popover is open: a light-blue wash and an underline, so a reader glancing back at the paragraph can see which citation the panel belongs to. Pair it with `aria-expanded` on the trigger, which is what carries the same fact to a screen reader; the wash is the visible half of one state, not a decoration.

> Popovers resize to the content but should be reserved for short pieces of information. If the content gets too long it may not be contained within the viewport.

## TOC bar

Need in-page navigation? The TOC bar is a row that carries a single disclosure control, which opens a list of the page’s sections. The bar is always sticky and it stays at the top of the viewport while the reader scrolls through the page.

```html
<div class="ds-container ds-zone-secondary">
  <header class="ds-page-header">…</header>

  <div class="ds-full ds-toc-bar">
    <div class="ds-toc-bar-inner">
      <details class="ds-toc">
        <summary class="ds-toc-trigger">
          <svg aria-hidden="true">…</svg>
          <span class="ds-toc-text"><span class="ds-toc-prefix">Contents</span></span>
          <svg class="ds-toc-chevron" aria-hidden="true">…</svg>
        </summary>
        <nav class="ds-toc-menu" aria-label="Contents">
          <ol></ol>      <!-- written by hand, or left empty for toc.js to fill -->
        </nav>
      </details>
    </div>
  </div>

  <div class="ds-full ds-zone-primary">…</div>
</div>
<script src="toc.js" defer></script>
```

- `.ds-toc` — The control, a `<details>`. It works on its own anywhere, and it opens with JavaScript off.
- `.ds-toc-trigger` — The `<summary>`. Holds the list icon, `.ds-toc-text` with its `.ds-toc-prefix`, and `.ds-toc-chevron`.
- `.ds-toc-menu` — The list, a `<nav>` holding an `<ol>`. The link to the current section gets `.is-current`. A page whose sections are numbered puts each number in `.ds-toc-num`.
- `.ds-toc-bar` — The edge-to-edge row that carries the control. A direct child of `.ds-container`, with `.ds-full`. Placed directly before `.ds-zone-primary`, it sits on that zone’s top edge. The bar is always sticky: it keeps to the top of the viewport, where it becomes `.is-stuck` and tightens, and it sets `scroll-padding-top` so an anchor lands below it. Sticky chrome is governed by [DESIGN-POLICIES](doc.html?src=docs/DESIGN-POLICIES.md); check there before adding the bar to a page.
- `.ds-toc-bar-inner` — The bar’s three-slot grid, which keeps the control centred whatever sits beside it.
- `[data-toc-scope]` — Optional, on `.ds-toc`: a selector for the element whose headings fill an empty list. Without it, `toc.js` reads `<main>`, or the whole page when there is no `<main>`.

## Accordion inside a card  (Variants)

A disclosure inside another one is the second level: indented one step, its label a step smaller. Two levels is the limit a reader can keep track of. Shown inside a card with a heading, the paper reader's sidebar, where the stack ends the card and the card's own edge closes it.

```html
<div class="ds-card">
  <h3>Paper information</h3>
  <div class="ds-acc-stack">
    <details class="ds-acc" open>
      <summary>Versions</summary>
      <div class="ds-acc-body">
        <dl>
          <dt>v3 · current</dt><dd>24 Apr 2026</dd>
          <dt>v2</dt><dd><a href="#">2 Mar 2026</a></dd>
          <dt>v1</dt><dd><a href="#">10 Jan 2026</a></dd>
        </dl>
      </div>
    </details>
    <details class="ds-acc">
      <summary>Metadata</summary>
      <div class="ds-acc-body">
        <details class="ds-acc">
          <summary>Subjects</summary>
          <div class="ds-acc-body">General Relativity and Quantum Cosmology (<a href="#">gr-qc</a>); Cosmology and Nongalactic Astrophysics (<a href="#">astro-ph.CO</a>)</div>
        </details>
        <details class="ds-acc">
          <summary>Identifiers</summary>
          <div class="ds-acc-body">
            <dl>
              <dt>arXiv ID</dt><dd><a href="#">2604.22725</a></dd>
              <dt>DOI</dt><dd><a href="#">10.48550/arXiv.2604.22725</a></dd>
            </dl>
          </div>
        </details>
      </div>
    </details>
    <details class="ds-acc">
      <summary>Related</summary>
      <div class="ds-acc-body">Connected papers, datasets, and code links.</div>
    </details>
  </div>
</div>
```

- `.ds-acc inside .ds-acc-body` — The second level. Indented one step, its label a step smaller.
- `.ds-card > .ds-acc-stack:last-child` — A stack that ends a card drops the last disclosure's lower rule, because the card's edge closes it. With content below the stack, the rule stays.
- `h3 before the stack` — The heading names the group, so it is found by heading navigation and every disclosure inside it is announced under that name.

## Rules

- **Never put must-see information only behind a disclosure.** The older-version warning appears in the main column even though the full history lives in the Versions accordion. A reader who never opens anything must still meet everything that matters.
- **Disclosure is not a fix for too much content.** If a page needs six accordions to be tolerable, the page has a structure problem and hiding things postpones it. Ask what can be cut or moved before asking what can be collapsed.
- **Default state is closed**, except that a single most-relevant panel may start open. Open state is not persisted — predictability beats memory here.
- **One panel, one label.** If a summary needs a sentence to explain what is inside, the content is not a section and probably wants show-more or a page of its own.
- **Show more among links is grey and italic.** At the end of a run of links — author names, category links — a Link Blue “show all 22 authors” is one more link in that run, indistinguishable from a name. It is not a link: it goes nowhere, it changes this page. Reading as a different *kind* of thing than its neighbours is the whole job, which is what `.ds-show-more--among-links` is for. Anywhere else, the default link colour is right.
- **Never put content in a popover that exists nowhere else.** A popover is a shortcut to something already on the page or already at a URL — the reference list, the footnote. It is not a place to store text.
- **Nothing animates.** These components have no transitions, so there is nothing for `prefers-reduced-motion` to switch off. An accordion that animates its height also animates the position of everything below it, which is motion a reader did not ask for.
- **A popover sits above sticky chrome** (`z-index: 110`, per the [Z-layer scale](doc.html?src=docs/DESIGN-POLICIES.md)). A popover is always the thing the reader just asked for, so it is never the thing that gets hidden.
- **Prefer native markup.** Where a disclosure can be a `<details>` element, as the accordion and the TOC bar are, use it. It carries the expanded state, the keyboard behaviour and the announcement without any script, and find-in-page can open a closed panel to reveal a match. A hand-built accordion loses all four, and losing find-in-page on a research site is the expensive one.
- **In a `<details>`, the summary is the whole label.** Never put a second interactive control inside it — a link or button in a `<summary>` is reachable but its activation fights the disclosure's own.
- **Hide with the `hidden` attribute, not with a class.** Content hidden by a class that fails to load is invisible but still tabbable, which puts a keyboard user in a place they cannot see.
- **Every custom toggle owns `aria-expanded`.** A show-more button and a popover trigger are not `<details>`, so they state it themselves. Its absence is the single most common defect in this pattern: the control announces as a button, does something visible to everyone else, and says nothing.
- **A show-more label counts what it hides.** “show all 22 authors”, not “show more”, whenever the hidden part is a list. A reader deciding whether to expand is asking how much is behind it, and someone using a screen reader hears the control with no view of the list at all. Return the label to “show fewer” when open.
- **Escape closes a popover and returns focus** to the chip that opened it. A reader who opened it from the keyboard must not be stranded at the end of the document. Close it on outside click and on scroll as well: the panel is `position: fixed`, so left open it would follow the viewport while the sentence it belongs to scrolls away.
- **The TOC bar's list is a disclosure, not an ARIA menu.** `role="menu"` is for application menus — the kind with arrow-key roving focus and menu items that are not links. A list of links is a disclosure, and W3C’s own guidance is to build it this way. Using `role="menu"` here would make a screen reader promise keyboard behaviour the component does not have.
- **Mark where the reader is.** `toc.js` gives the TOC bar's link to the current section `aria-current="location"`.
- **Everything is reachable from the keyboard, with JavaScript off.** Open, close and keyboard operation are native; outside-click and Escape are enhancements layered on top. Escape closes the TOC bar's list and returns focus to its control, but only when focus was inside the list — Escape pressed elsewhere on the page must not move it.
