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
        does: "Holds the panel content, directly after the `<summary>`. A `<dl>` inside it renders as label and value pairs, one column on a narrow screen. Each label is grey and a step smaller than the value."
      - name: ".ds-acc-stack"
        does: "The container for a list of disclosures. Stacked in it they butt together and read as one ruled list: each shared edge is a single line, because the preceding item's lower rule is the next item's upper one."
      - name: "[open]"
        does: "Present on the one panel that starts open, if any. See [Which affordance](#which-affordance) under Rules."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) Keyboard (Level A) and [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A)"
  - id: show-more
    title: "Show more"
    summary: "While an accordion hides an entire labelled section, the 'show more' control reveals the hidden *tail end* of partially displayed content. When hiding the remainder of a list we display the additional item count in the link."
    classes:
      - name: ".ds-show-more"
        does: "On a `<button type=\"button\">` at the end of the visible part. It takes the link colour, because in running text it is the one thing a reader can act on. An accordion is `<details>`, so the browser supplies the semantics; a tail cannot be, so this is a real `<button>` that has to declare for itself what the browser would otherwise have said, with the three attributes below. It starts `hidden`, and `show-more.js` shows it."
      - name: ".ds-show-more--among-links"
        does: "For a tail at the end of a run of links, such as an author list: grey and italic, so the control does not read as one more link."
      - name: "[aria-expanded]"
        does: "`\"false\"` / `\"true\"`, flipped on every toggle. Without it the control announces as a button that does something unspecified."
      - name: "[aria-controls]"
        does: "The id of the region it reveals. Several ids, separated by spaces, open and close together, as a version list's ellipsis and the versions behind it do ([Indicate which version is being read](versions.md#version-row))."
      - name: ".ds-show-more-tail"
        does: "On the region. While the page loads, it keeps the tail closed before the script runs, so a long author list does not show in full and then collapse. Without JavaScript it does nothing, and the whole text shows."
      - name: ".is-open"
        does: "Set on the region by the script while the tail is open, together with removing `hidden`."
      - name: "[hidden]"
        does: "On the region, the attribute and not a class, set by the script when it shows the button. Without JavaScript the region is never hidden, so the whole text shows and there is no button. While hidden, the names are out of the tab order and out of find-in-page, and the collapse still works with no CSS loaded at all."
      - name: "[data-open-label]"
        does: "The label while the tail is open; without it, “show fewer”. The closed label is the button's own text."
      - name: "[data-closed-label]"
        does: "Only on a button that starts open, with `aria-expanded=\"true\"`: the label once it closes."
      - name: "<script src=\"show-more.js\" defer>"
        does: "Once per page, at the foot. It works on every `.ds-show-more` with `aria-controls`: it hides each tail and shows its button, and each press flips `aria-expanded`, the label and `hidden` on every region the button names. A page writes no script of its own."
    notes:
      - "\"Show more\" is a button, not a `<details>` element (the element the accordion uses). A `<details>` element cannot sit inside a paragraph, and its label must come before the hidden text, not after it."
  - id: popover
    title: "Popover"
    summary: "A quick lookup the reader can access without losing their place. Popovers are used on HTML papers pages for citations and footnotes, which is especially helpful for screen reader users. Popovers can contain nearly any type of content including links but should be used only for short bursts of information, or a list the reader opens, looks through and closes, such as the categories a report covers. The filter panel, a popover of filters for a set of data, is on [Filters](filters.md)."
    classes:
      - name: ".ds-popover"
        does: "The panel. It is `position: fixed`: the host sets `top` and `left`, and moves it to `<body>` if the trigger has a transformed ancestor. Closed, it has the `hidden` attribute."
      - name: ".ds-popover-title"
        does: "The label line at the top of the panel. It leaves room for the close control."
      - name: ".ds-close"
        does: "The close control, the same one the alert and the announcement band use, documented on [Buttons](buttons.md#the-close-control). The popover supplies its corner position and nothing else. It needs a `<span class=\"is-sr-only\">` that says what it closes."
      - name: "[role=\"region\"], [aria-label]"
        does: "Together they make the panel a named landmark, so a screen reader user can find it and hear what it holds."
      - name: "--ds-popover-width, --ds-popover-max-height"
        does: "Set per use; past that height it scrolls, and `overscroll-behavior: contain` stops that scroll running on into the page beneath once it reaches the end."
      - name: ".ds-inline-active"
        does: "On the trigger while its popover is open: a light-blue wash and an underline, so a reader glancing back at the paragraph can see which citation the panel belongs to. Pair it with `aria-expanded` on the trigger, which is what gives the same fact to a screen reader; the wash is the visible half of one state, not a decoration."
    notes:
      - "Popovers resize to the content but should be reserved for short pieces of information. If the content gets too long it may not be contained within the viewport."
  - id: tabs
    title: "Tabs"
    summary: "Tabs switch between views of the same page. Each tab shows one panel and hides the others. To move between pages, use the [secondary navigation](navigation.md#secondary-navigation) instead; it looks the same but provides different signals to screen readers."
    classes:
      - name: ".ds-tabs"
        does: "Holds two or more panels. `data-label` names the set for a screen reader."
      - name: ".ds-tabs-panel"
        does: "One view, a `<section>` that starts with a heading. The heading becomes the tab label."
      - name: "tabs.js"
        does: "Builds the tab list from the panel headings and adds the roles, the selected state and the keyboard: Tab reaches the selected tab, the arrow keys move between tabs, Home and End go to the first and last. Moving to a tab shows its panel. Without the script, every panel shows under its own heading."
      - name: ".ds-tabs-list"
        does: "The row of tabs, added by the script. The selected tab is bold, a box joined to its panel with the accent along its top. It takes the background of the zone it sits in: the page ground (white in light mode), or the secondary zone's tint (light grey in light mode) inside a [secondary band](layouts.md#secondary-zones). The row wraps on a narrow screen."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) Keyboard (Level A) and [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A)"
  - id: accordion-inside-a-card
    title: "Accordion inside a card"
    group: "Variants"
    summary: "A disclosure inside another one is the second level: indented one step, its label a step smaller. Two levels is the limit a reader can follow. Shown inside a card with a heading, the paper reader's sidebar, where the stack ends the card and the card's own edge closes it."
    classes:
      - name: ".ds-acc inside .ds-acc-body"
        does: "The second level. Indented one step, its label a step smaller."
      - name: ".ds-card > .ds-acc-stack:last-child"
        does: "A stack that ends a card drops the last disclosure's lower rule, because the card's edge closes it. With content below the stack, the rule stays."
      - name: "h3.ds-panel-label before the stack"
        does: "The heading names the group, so it is found by heading navigation and every disclosure inside it is announced under that name. It is a panel label, so it reads as a level above the accordion labels below it."
  - id: one-panel-open-at-a-time
    title: "One panel open at a time"
    group: "Variants"
    summary: "Opening one panel closes the panel that was open. There is no class: give every `<details>` in the group the same `name` attribute, and the browser does the rest without JavaScript."
    classes:
      - name: "[name]"
        does: "The same value on every `<details>` in the group, and a value no other group on the page uses. Opening one closes the others. In a browser too old to support it, every panel opens on its own, as in a plain stack."
      - name: "[open]"
        does: "On one panel in the group at most, if one starts open."
rules:
  - "A view has one level of tabs. Tabs inside a tab panel are not used."
  - "The question that separates them is not how much is hidden. It is what relationship the hidden thing has to what the reader is looking at."
  - "**Never put must-see information only behind a disclosure.** Anything legally or practically required, such as a warning or a licence, also appears in the page's always-visible flow: the older-version warning is in the main column even though the full history lives in the Versions accordion. A closed accordion, a folded margin note and a popover are all places a reader may never open."
  - "**Disclosure is not a fix for too much content.** If a page needs six accordions to be tolerable, the page has a structure problem and hiding things postpones it. Ask what can be cut or moved before asking what can be collapsed."
  - "**Default state is closed**, except that a single most-relevant panel may start open. Open state is not persisted — predictability beats memory here."
  - "**One panel open at a time is for panels read one at a time.** When a reader needs two panels open together to compare them, leave the group without a `name`."
  - "**One panel, one label.** If a summary needs a sentence to explain what is inside, the content is not a section and probably wants show-more or a page of its own."
  - "**An abstract cut short is show more, not an accordion.** This holds when the excerpt starts partway through the abstract, as a search result’s can: the full abstract replaces the excerpt in place, and Show less puts the excerpt back."
  - "**Show more among links is grey and italic.** At the end of a run of links — author names, category links — a Link Blue “show all 22 authors” is one more link in that run, indistinguishable from a name. It is not a link: it goes nowhere, it changes this page. Reading as a different *kind* of thing than its neighbours is the whole job, which is what `.ds-show-more--among-links` is for. Anywhere else, the default link colour is right."
  - "**Never put content in a popover that exists nowhere else.** A popover is a shortcut to something already on the page or already at a URL — the reference list, the footnote. It is not a place to store text."
  - "**Nothing animates.** These components have no transitions, so there is nothing for `prefers-reduced-motion` to switch off. An accordion that animates its height also animates the position of everything below it, which is motion a reader did not ask for."
  - "**A popover sits above sticky chrome** (`z-index: 110`, per the [Z-layer scale](../doc.html?src=docs/DESIGN-POLICIES.md)). A popover is always the thing the reader just asked for, so it is never the thing that gets hidden."
  - "**Prefer native markup.** Where a disclosure can be a `<details>` element, as the accordion and the TOC bar are, use it. It includes the expanded state, the keyboard behaviour and the announcement without any script, and find-in-page can open a closed panel to reveal a match. A hand-built accordion loses all four, and losing find-in-page on a research site is the expensive one."
  - "**In a `<details>`, the summary is the whole label.** Never put a second interactive control inside it — a link or button in a `<summary>` is reachable but its activation fights the disclosure's own."
  - "**Hide with the `hidden` attribute, not with a class.** Content hidden by a class that fails to load is invisible but still tabbable, which puts a keyboard user in a place they cannot see."
  - "**Every custom toggle owns `aria-expanded`.** A show-more button and a popover trigger are not `<details>`, so they state it themselves. Its absence is the single most common defect in this pattern: the control announces as a button, does something visible to everyone else, and says nothing."
  - "**A show-more label counts what it hides.** “show all 22 authors”, not “show more”, whenever the hidden part is a list. A reader deciding whether to expand is asking how much is behind it, and someone using a screen reader hears the control with no view of the list at all. Return the label to “show fewer” when open."
  - "**Escape closes a popover and returns focus** to the chip that opened it. A reader who opened it from the keyboard must not be stranded at the end of the document. Close it on outside click and on scroll as well: the panel is `position: fixed`, so left open it would follow the viewport while the sentence it belongs to scrolls away."
  - "**Everything is reachable from the keyboard, with JavaScript off.** Open, close and keyboard operation are native; outside-click and Escape are enhancements layered on top. Show more needs a script, so its script does the hiding: without JavaScript the tail shows and the button does not."
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
- `.ds-acc-body` — Holds the panel content, directly after the `<summary>`. A `<dl>` inside it renders as label and value pairs, one column on a narrow screen. Each label is grey and a step smaller than the value.
- `.ds-acc-stack` — The container for a list of disclosures. Stacked in it they butt together and read as one ruled list: each shared edge is a single line, because the preceding item's lower rule is the next item's upper one.
- `[open]` — Present on the one panel that starts open, if any. See [Which affordance](#which-affordance) under Rules.

> Meets accessibility guidelines [WCAG 2.2 SC 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) Keyboard (Level A) and [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A)

## Show more

While an accordion hides an entire labelled section, the 'show more' control reveals the hidden *tail end* of partially displayed content. When hiding the remainder of a list we display the additional item count in the link.

```html
<!-- The rest of a paragraph -->
<p>We study the convergence … under heavy-tailed noise<span id="abstract-tail" class="ds-show-more-tail">, and show that …</span>.
<button type="button" class="ds-show-more" aria-expanded="false" aria-controls="abstract-tail"
        data-open-label="show less" hidden>show more</button></p>

<!-- The rest of a countable list: the label carries the count -->
<p>Keywords: stochastic optimisation, …<span id="keywords-tail" class="ds-show-more-tail">, non-convex analysis, …</span>
<button type="button" class="ds-show-more" aria-expanded="false" aria-controls="keywords-tail"
        data-open-label="show fewer" hidden>show 4 more keywords</button></p>

<!-- The rest of a list of links -->
<ul>
  <li><a href="#">R. Almeida</a></li>
  …
  <li><a href="#">L. Cheng</a></li></ul><span id="authors-tail" class="ds-show-more-tail">, <a href="#">T. Okonkwo</a>, …</span>
<button type="button" class="ds-show-more ds-show-more--among-links" aria-expanded="false"
        aria-controls="authors-tail" data-open-label="show fewer" hidden>… show all 22 authors</button>

<!-- And include the script once, at the foot of the page -->
<script src="show-more.js" defer></script>
```

- `.ds-show-more` — On a `<button type="button">` at the end of the visible part. It takes the link colour, because in running text it is the one thing a reader can act on. An accordion is `<details>`, so the browser supplies the semantics; a tail cannot be, so this is a real `<button>` that has to declare for itself what the browser would otherwise have said, with the three attributes below. It starts `hidden`, and `show-more.js` shows it.
- `.ds-show-more--among-links` — For a tail at the end of a run of links, such as an author list: grey and italic, so the control does not read as one more link.
- `[aria-expanded]` — `"false"` / `"true"`, flipped on every toggle. Without it the control announces as a button that does something unspecified.
- `[aria-controls]` — The id of the region it reveals. Several ids, separated by spaces, open and close together, as a version list's ellipsis and the versions behind it do ([Indicate which version is being read](versions.md#version-row)).
- `.ds-show-more-tail` — On the region. While the page loads, it keeps the tail closed before the script runs, so a long author list does not show in full and then collapse. Without JavaScript it does nothing, and the whole text shows.
- `.is-open` — Set on the region by the script while the tail is open, together with removing `hidden`.
- `[hidden]` — On the region, the attribute and not a class, set by the script when it shows the button. Without JavaScript the region is never hidden, so the whole text shows and there is no button. While hidden, the names are out of the tab order and out of find-in-page, and the collapse still works with no CSS loaded at all.
- `[data-open-label]` — The label while the tail is open; without it, “show fewer”. The closed label is the button's own text.
- `[data-closed-label]` — Only on a button that starts open, with `aria-expanded="true"`: the label once it closes.
- `<script src="show-more.js" defer>` — Once per page, at the foot. It works on every `.ds-show-more` with `aria-controls`: it hides each tail and shows its button, and each press flips `aria-expanded`, the label and `hidden` on every region the button names. A page writes no script of its own.

> "Show more" is a button, not a `<details>` element (the element the accordion uses). A `<details>` element cannot sit inside a paragraph, and its label must come before the hidden text, not after it.

## Popover

A quick lookup the reader can access without losing their place. Popovers are used on HTML papers pages for citations and footnotes, which is especially helpful for screen reader users. Popovers can contain nearly any type of content including links but should be used only for short bursts of information, or a list the reader opens, looks through and closes, such as the categories a report covers. The filter panel, a popover of filters for a set of data, is on [Filters](filters.md).

For a screen reader user, the trigger is an ordinary link whose accessible name includes the reference itself, such as “Reference 47: Ashtekar and Bojowald (2006)”, so most readers hear what they need without opening anything. Opening the popover does not move focus: the trigger reports that it is expanded, and the reader can continue through the main text. To read the popover, they move to it as a named region, from the screen reader's list of landmarks. Escape closes it and returns focus to the trigger.

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

- `.ds-popover` — The panel. It is `position: fixed`: the host sets `top` and `left`, and moves it to `<body>` if the trigger has a transformed ancestor. Closed, it has the `hidden` attribute.
- `.ds-popover-title` — The label line at the top of the panel. It leaves room for the close control.
- `.ds-close` — The close control, the same one the alert and the announcement band use, documented on [Buttons](buttons.md#the-close-control). The popover supplies its corner position and nothing else. It needs a `<span class="is-sr-only">` that says what it closes.
- `[role="region"], [aria-label]` — Together they make the panel a named landmark, so a screen reader user can find it and hear what it holds.
- `--ds-popover-width, --ds-popover-max-height` — Set per use; past that height it scrolls, and `overscroll-behavior: contain` stops that scroll running on into the page beneath once it reaches the end.
- `.ds-inline-active` — On the trigger while its popover is open: a light-blue wash and an underline, so a reader glancing back at the paragraph can see which citation the panel belongs to. Pair it with `aria-expanded` on the trigger, which is what gives the same fact to a screen reader; the wash is the visible half of one state, not a decoration.

> Popovers resize to the content but should be reserved for short pieces of information. If the content gets too long it may not be contained within the viewport.

## Tabs

Tabs switch between views of the same page. Each tab shows one panel and hides the others. To move between pages, use the [secondary navigation](navigation.md#secondary-navigation) instead; it looks the same but provides different signals to screen readers.

```html
<div class="ds-tabs" data-label="Membership activity">
  <section class="ds-tabs-panel">
    <h3>Members</h3>
    <p>1,284 member institutions in 46 countries.</p>
  </section>
  <section class="ds-tabs-panel">
    <h3>Submissions</h3>
    <p>2,391 submissions from member institutions this month.</p>
  </section>
  <section class="ds-tabs-panel">
    <h3>Downloads</h3>
    <p>4.2 million downloads from member institutions this month.</p>
  </section>
</div>

<script src="tabs.js" defer></script>
```

- `.ds-tabs` — Holds two or more panels. `data-label` names the set for a screen reader.
- `.ds-tabs-panel` — One view, a `<section>` that starts with a heading. The heading becomes the tab label.
- `tabs.js` — Builds the tab list from the panel headings and adds the roles, the selected state and the keyboard: Tab reaches the selected tab, the arrow keys move between tabs, Home and End go to the first and last. Moving to a tab shows its panel. Without the script, every panel shows under its own heading.
- `.ds-tabs-list` — The row of tabs, added by the script. The selected tab is bold, a box joined to its panel with the accent along its top. It takes the background of the zone it sits in: the page ground (white in light mode), or the secondary zone's tint (light grey in light mode) inside a [secondary band](layouts.md#secondary-zones). The row wraps on a narrow screen.

> Meets accessibility guidelines [WCAG 2.2 SC 2.1.1](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) Keyboard (Level A) and [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A)

## Accordion inside a card  (Variants)

A disclosure inside another one is the second level: indented one step, its label a step smaller. Two levels is the limit a reader can follow. Shown inside a card with a heading, the paper reader's sidebar, where the stack ends the card and the card's own edge closes it.

```html
<div class="ds-card">
  <h3 class="ds-panel-label">Paper information</h3>
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
- `h3.ds-panel-label before the stack` — The heading names the group, so it is found by heading navigation and every disclosure inside it is announced under that name. It is a panel label, so it reads as a level above the accordion labels below it.

## One panel open at a time  (Variants)

Opening one panel closes the panel that was open. There is no class: give every `<details>` in the group the same `name` attribute, and the browser does the rest without JavaScript.

```html
<div class="ds-card">
  <h3 class="ds-panel-label">Paper information</h3>
  <div class="ds-acc-stack">
    <details class="ds-acc" name="paper-info">
      <summary>Versions</summary>
      <div class="ds-acc-body">…</div>
    </details>
    <details class="ds-acc" name="paper-info">
      <summary>Metadata</summary>
      <div class="ds-acc-body">…</div>
    </details>
    <details class="ds-acc" name="paper-info">
      <summary>Related</summary>
      <div class="ds-acc-body">…</div>
    </details>
  </div>
</div>
```

- `[name]` — The same value on every `<details>` in the group, and a value no other group on the page uses. Opening one closes the others. In a browser too old to support it, every panel opens on its own, as in a plain stack.
- `[open]` — On one panel in the group at most, if one starts open.

## Rules

### One level of tabs

A view has one level of tabs. Tabs inside a tab panel are not used.

### Which affordance

The question that separates them is not how much is hidden. It is what relationship the hidden thing has to what the reader is looking at.

| Use | When the hidden content is | Costs the reader |
|---|---|---|
| Accordion `.ds-acc` | A **labelled section** the reader can decide about from its label alone — Versions, Paper information, Related. More than a line or two; a single line goes on the page. | One click, stays on the page, keeps their place. |
| Show more `.ds-show-more` | The **tail of something already begun** — authors nine through twenty-two, the rest of a category list, the rest of an abstract. There is no label to give it, because it is not a different thing. | One click, expands in place, no new surface. |
| Popover `.ds-popover` | A **lookup** the reader wants without leaving their sentence — what reference 47 is, what footnote 3 says. | Nothing permanent. It closes on Escape and does not move the page. |
| A link to a full page | Something with **its own identity** — a different paper, an author's other work, the full licence. | Leaves the page. Pay this only when the destination deserves a URL. |

- **Never put must-see information only behind a disclosure.** Anything legally or practically required, such as a warning or a licence, also appears in the page's always-visible flow: the older-version warning is in the main column even though the full history lives in the Versions accordion. A closed accordion, a folded margin note and a popover are all places a reader may never open.
- **Disclosure is not a fix for too much content.** If a page needs six accordions to be tolerable, the page has a structure problem and hiding things postpones it. Ask what can be cut or moved before asking what can be collapsed.
- **Default state is closed**, except that a single most-relevant panel may start open. Open state is not persisted — predictability beats memory here.
- **One panel open at a time is for panels read one at a time.** When a reader needs two panels open together to compare them, leave the group without a `name`.
- **One panel, one label.** If a summary needs a sentence to explain what is inside, the content is not a section and probably wants show-more or a page of its own.
- **An abstract cut short is show more, not an accordion.** This holds when the excerpt starts partway through the abstract, as a search result’s can: the full abstract replaces the excerpt in place, and Show less puts the excerpt back.
- **Show more among links is grey and italic.** At the end of a run of links — author names, category links — a Link Blue “show all 22 authors” is one more link in that run, indistinguishable from a name. It is not a link: it goes nowhere, it changes this page. Reading as a different *kind* of thing than its neighbours is the whole job, which is what `.ds-show-more--among-links` is for. Anywhere else, the default link colour is right.
- **Never put content in a popover that exists nowhere else.** A popover is a shortcut to something already on the page or already at a URL — the reference list, the footnote. It is not a place to store text.

### Motion and layering

- **Nothing animates.** These components have no transitions, so there is nothing for `prefers-reduced-motion` to switch off. An accordion that animates its height also animates the position of everything below it, which is motion a reader did not ask for.
- **A popover sits above sticky chrome** (`z-index: 110`, per the [Z-layer scale](../doc.html?src=docs/DESIGN-POLICIES.md)). A popover is always the thing the reader just asked for, so it is never the thing that gets hidden.

### Accessibility essentials

- **Prefer native markup.** Where a disclosure can be a `<details>` element, as the accordion and the TOC bar are, use it. It includes the expanded state, the keyboard behaviour and the announcement without any script, and find-in-page can open a closed panel to reveal a match. A hand-built accordion loses all four, and losing find-in-page on a research site is the expensive one.
- **In a `<details>`, the summary is the whole label.** Never put a second interactive control inside it — a link or button in a `<summary>` is reachable but its activation fights the disclosure's own.
- **Hide with the `hidden` attribute, not with a class.** Content hidden by a class that fails to load is invisible but still tabbable, which puts a keyboard user in a place they cannot see.
- **Every custom toggle owns `aria-expanded`.** A show-more button and a popover trigger are not `<details>`, so they state it themselves. Its absence is the single most common defect in this pattern: the control announces as a button, does something visible to everyone else, and says nothing.
- **A show-more label counts what it hides.** “show all 22 authors”, not “show more”, whenever the hidden part is a list. A reader deciding whether to expand is asking how much is behind it, and someone using a screen reader hears the control with no view of the list at all. Return the label to “show fewer” when open.
- **Escape closes a popover and returns focus** to the chip that opened it. A reader who opened it from the keyboard must not be stranded at the end of the document. Close it on outside click and on scroll as well: the panel is `position: fixed`, so left open it would follow the viewport while the sentence it belongs to scrolls away.
- **Everything is reachable from the keyboard, with JavaScript off.** Open, close and keyboard operation are native; outside-click and Escape are enhancements layered on top. Show more needs a script, so its script does the hiding: without JavaScript the tail shows and the button does not.
