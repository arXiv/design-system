---
page: links.html
title: "Links"
summary: "Text links are simple but important to get right. Every link inside a `.ds-page` is the inline text link, with no class to add, and appears in Link Blue, a special blue reserved only for this purpose. Do not override link styles, the colors are carefully chosen to maintain accessibility contrasts in light and dark modes and on tinted and shaded backgrounds."
stylesheet: design-system.css
components:
  - id: the-inline-link
    title: "The inline link"
    summary: "One link, four states. At rest it is Link Blue with a 1px underline set 2px below the text. On hover the colour deepens and the underline thickens. Once followed it turns Visited Purple. When reached by keyboard it shows a 3px Link Blue ring. The four colours are in the [tokens table](#tokens), read live from the stylesheet."
    classes:
      - name: "<a href> inside .ds-page"
        does: "Every anchor with an `href` inside a `.ds-page` takes the link treatment: the colour, the underline, and the hover, visited and focus states. There is no class to add, and the dark values arrive through the same token flip as everything else."
    notes:
      - "All states meet accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A), [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA), and [WCAG 2.2 SC 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) Focus Visible (Level AA)"
    rules:
      - "Inline body links must be underlined: Color contrast against body text is only 3.0:1 in light mode and 1.9:1 in dark mode — too marginal to rely on alone. Underlines are mandatory for inline links per DESIGN-POLICIES.md and WCAG 1.4.1 (use of color). Standalone navigation links (header, footer, button-like surfaces) may omit the underline."
  - id: links-and-text-only-buttons
    title: "Links and text-only buttons"
    summary: "A link goes somewhere: it has an `href`, it is underlined, and it remembers being visited. A text-only button does something on this page, such as opening a panel or copying a value: it is Link Blue too, but has no underline and no visited state. Use the one that matches what happens when it is pressed. Text-only buttons are described on [Buttons](buttons.md#button-tiers)."
    classes:
      - name: "<a href>"
        does: "Goes to another page or another place on this one. Underlined, and takes the visited colour once followed."
      - name: ".ds-btn.ds-btn-text"
        does: "Acts on this page. Plain Link Blue text with no underline and no visited state; the surrounding text sets its size. When it opens or closes something, add `aria-expanded`."
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A)"
  - id: linking-to-a-section
    title: "Linking to a section"
    summary: "A section heading can include a control that copies a link to that section, so a reader can point a colleague at the exact place. It is an option for long pages that readers cite or share in parts, such as HTML papers and these docs; most headings do not need it. Hover a heading on this page, or tab to it, and the control appears."
    classes:
      - name: "<section> > h2, h3"
        does: "The section heading: the `<h2>` or `<h3>` that is the first element in a `<section>`. `anchors.js` adds the control to every section heading that has an `id`. No class is needed."
      - name: "id"
        does: "Written into the HTML, by hand or by whatever builds the page. These docs use `verification/gen-anchors.py`, which makes it from the heading text."
      - name: ".ds-permalink"
        does: "The control, a `<button>` with the link icon and the word “Permalink”, that `anchors.js` adds to every section heading with an `id`. It shows while the heading is hovered, while it has focus, and after a tap on a screen without hover. It stays in the tab order while it is hidden. After a copy, the link icon is a green tick (`.ds-permalink-done`, added by the script) for 2 seconds, in the same space, so the word does not move."
      - name: ".is-sr-only"
        does: "Completes the accessible name with the section: “Permalink to Dividers”. The name starts with the visible word."
      - name: "[role=\"status\"]"
        does: "One region on the page. The script writes “Link to Dividers copied” into it and clears it with the tick."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A) and [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)"
    rules:
      - "**The ids are written into the HTML, not added by a script.** In these docs, `verification/gen-anchors.py` writes them, and `--check` fails when a heading has none. A real id works with JavaScript off, works for a link arriving from another page, and exists when the browser resolves the fragment on first load — none of which a script running at `DOMContentLoaded` can promise."
      - "**The control is a button, not a link.** An `<a href=\"#here\">` inside a heading is a tab stop that goes nowhere the reader wanted to go — they are already looking at the section. What they want is the address, so it copies it."
      - "**An id follows its heading**, so rewording a heading changes its anchor. That is the right trade while nothing links in from outside; re-run the generator after editing a heading and the check will tell you if you forget."
      - "**Its accessible name includes the section.** Twelve buttons all called “Permalink” are useless in a list of controls, so each says which section it belongs to."
      - "**The control is the same wherever it is used**, on a docs page or in an HTML paper. A heading that has one action uses this control; an element with several actions, such as an equation, uses the [element pill](buttons.md#small-actions-attached-to-content)."
  - id: long-lists-of-links
    title: "Long lists of links"
    summary: "A long list of links, such as the other pages in a set, is a list of links set in columns: no bullets, and as many columns as the width holds, so twenty links take a few lines rather than twenty. The page the reader is on stays in the list as a link, and the stylesheet sets it apart."
    classes:
      - name: ".ds-link-list--columns"
        does: "With `.ds-link-list`, on a `<ul>` with one link in each item. No bullets, and as many columns as fit, each at least 14rem wide: one column on a phone. The links run down each column, then across, in the order of the markup."
      - name: "aria-current=\"page\""
        does: "On the link to the page the reader is on, in any `.ds-link-list`. It stays a link. The stylesheet sets it in `--ds-text` and bold, so it does not rest on colour alone, and a screen reader announces it as the current page."
      - name: "role=\"list\""
        does: "Keeps a list without bullets announced as a list: VoiceOver in Safari may not announce it otherwise."
      - name: "<nav aria-label>"
        does: "When the list is navigation, such as the other pages in a set, it sits in a `<nav>` with a name of its own. Use `aria-label`, not `aria-labelledby` pointing at the list's heading: a heading with a Permalink would add the Permalink's words to the name."
    rules:
      - "**The current page stays in the list, as a link.** Mark it with `aria-current=\"page\"` and add nothing else: no bold of your own, and no plain text in its place. The list then reads the same on every page of the set, and a screen reader says which page is open."
rules:
  - "A disabled link has no `href`, so it cannot be reached or followed by keyboard or pointer. `pointer-events: none` alone is not enough: it stops a mouse, but a keyboard can still follow the link. Add `role=\"link\"` and `aria-disabled=\"true\"`, so a screen reader still announces it as a link that is unavailable, and the stylesheet colours it `--ds-text-disabled` (`#aeaaa4`). The underline stays so it is still recognisable as a (currently unavailable) link. The disabled state falls below AA on contrast — WCAG exempts disabled controls from contrast requirements."
  - "A list of author names, a navigation bar, a footer column: these are lists in which every item is a link, and none of them is underlined. The underline exists to tell a link apart from the text around it, and in a list of links there is no such text; underlining every item would add visual noise and tell the reader nothing. WCAG asks for the underline only where colour alone would have to separate a link from ordinary text, which is the case for an inline link and not for a list. The links keep Link Blue, the hover and focus states, and the visited colour where it means something. Put `.ds-link-list` on the element that holds the list. A long list is set in columns, as [Long lists of links](#long-lists-of-links) shows."
  - "Meets accessibility guideline [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A). An underline is needed only where a link sits in running text; in a list, the layout shows which words are links."
  - "[Adrian Palomares](#lists-of-links), [Mei Lin Chen](#lists-of-links), [Kwame Mensah](#lists-of-links)"
  - "The Visited Purple is intentionally strong, not a faint after-state. Researchers reading long bibliographies and listings benefit from seeing what they have already followed up on; a too-subtle visited treatment defeats the purpose. If a specific surface (e.g., a navigation breadcrumb) needs to suppress visited styling, override `:visited { color: inherit }` locally."
  - "**Say where the link goes.** The link text on its own must make sense to someone who hears only the links on the page: “Endorsement policy”, not “click here”, “here” or “read more”. Put the name of the destination inside the `<a>`, not beside it."
  - "**A link always has an `href`, unless it is disabled.** Without one the element is not focusable, has no visited state, and does not announce as a link. Something that acts on this page rather than going somewhere is a [button](buttons.md), not a link with a click handler."
  - "**Keep the underline in body text.** Do not set `text-decoration: none` on an inline link. The underline is the only cue that survives forced-colors mode and a reader who cannot see the colour difference. Only a standalone link, such as one in navigation, may drop it."
  - "**Keep the visited colour in content.** Do not override `:visited` on links to papers, listings or references. Suppress it only where “where have I been” has no meaning, such as a breadcrumb or a menu."
  - "**Do not remove the focus ring.** The stylesheet draws it on `:focus-visible`, so it appears for keyboard users and not on mouse click. An `outline: none` on a link takes it away for everyone."
  - "**Links open in the same tab** unless the reader would lose work in progress. A reader's place in an HTML paper is work in progress, so a link from a paper to its PDF opens a new tab. A link that opens a new tab includes the external-link icon (`docs/icons/external-link.svg`) after its text, with `aria-hidden=\"true\"` on the icon and “(opens in a new tab)” in an `.is-sr-only` span, so the change is announced and survives page translation. In a row of links that each already have an icon, such as a paper's TOC bar, the external-link icon is left out; the hidden text stays."
  - "**In print, an external link shows its address after its text.** An in-page link, a button and a link that is an image do not. The stylesheet does this; nothing is needed in the markup."
---

# Links

Text links are simple but important to get right. Every link inside a `.ds-page` is the inline text link, with no class to add, and appears in Link Blue, a special blue reserved only for this purpose. Do not override link styles, the colors are carefully chosen to maintain accessibility contrasts in light and dark modes and on tinted and shaded backgrounds.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The inline link

One link, four states. At rest it is Link Blue with a 1px underline set 2px below the text. On hover the colour deepens and the underline thickens. Once followed it turns Visited Purple. When reached by keyboard it shows a 3px Link Blue ring. The four colours are in the [tokens table](#tokens), read live from the stylesheet.

```html
<p>Read the <a href="/help/endorsement">Endorsement policy</a> before you ask a colleague to endorse you.</p>
```

- `<a href> inside .ds-page` — Every anchor with an `href` inside a `.ds-page` takes the link treatment: the colour, the underline, and the hover, visited and focus states. There is no class to add, and the dark values arrive through the same token flip as everything else.

> All states meet accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A), [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA), and [WCAG 2.2 SC 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) Focus Visible (Level AA)

**Rule.** Inline body links must be underlined: Color contrast against body text is only 3.0:1 in light mode and 1.9:1 in dark mode — too marginal to rely on alone. Underlines are mandatory for inline links per DESIGN-POLICIES.md and WCAG 1.4.1 (use of color). Standalone navigation links (header, footer, button-like surfaces) may omit the underline.

## Links and text-only buttons

A link goes somewhere: it has an `href`, it is underlined, and it remembers being visited. A text-only button does something on this page, such as opening a panel or copying a value: it is Link Blue too, but has no underline and no visited state. Use the one that matches what happens when it is pressed. Text-only buttons are described on [Buttons](buttons.md#button-tiers).

```html
<p>
  Submitted 14 Jan 2024 · <a href="/abs/2401.00001v2">view revision history</a> ·
  <button class="ds-btn ds-btn-text" type="button" aria-expanded="false">Show all versions</button>
</p>
```

- `<a href>` — Goes to another page or another place on this one. Underlined, and takes the visited colour once followed.
- `.ds-btn.ds-btn-text` — Acts on this page. Plain Link Blue text with no underline and no visited state; the surrounding text sets its size. When it opens or closes something, add `aria-expanded`.

> Meets accessibility guideline [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A)

## Linking to a section

A section heading can include a control that copies a link to that section, so a reader can point a colleague at the exact place. It is an option for long pages that readers cite or share in parts, such as HTML papers and these docs; most headings do not need it. Hover a heading on this page, or tab to it, and the control appears.

```html
<!-- 1. The section heading, with an id -->
<section>
  <h2 id="dividers">Dividers</h2>
  …
</section>

<!-- 2. The scripts, once per page: copy.js copies, anchors.js adds the control -->
<script src="copy.js" defer></script>
<script src="anchors.js" defer></script>

<!-- What renders -->
<h2 id="dividers">Dividers
  <button type="button" class="ds-permalink"><svg aria-hidden="true">…</svg>Permalink<span class="is-sr-only"> to Dividers</span></button>
</h2>
```

- `<section> > h2, h3` — The section heading: the `<h2>` or `<h3>` that is the first element in a `<section>`. `anchors.js` adds the control to every section heading that has an `id`. No class is needed.
- `id` — Written into the HTML, by hand or by whatever builds the page. These docs use `verification/gen-anchors.py`, which makes it from the heading text.
- `.ds-permalink` — The control, a `<button>` with the link icon and the word “Permalink”, that `anchors.js` adds to every section heading with an `id`. It shows while the heading is hovered, while it has focus, and after a tap on a screen without hover. It stays in the tab order while it is hidden. After a copy, the link icon is a green tick (`.ds-permalink-done`, added by the script) for 2 seconds, in the same space, so the word does not move.
- `.is-sr-only` — Completes the accessible name with the section: “Permalink to Dividers”. The name starts with the visible word.
- `[role="status"]` — One region on the page. The script writes “Link to Dividers copied” into it and clears it with the tick.

> Meets accessibility guidelines [WCAG 2.2 SC 2.5.3](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) Label in Name (Level A) and [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)

**Rule.** **The ids are written into the HTML, not added by a script.** In these docs, `verification/gen-anchors.py` writes them, and `--check` fails when a heading has none. A real id works with JavaScript off, works for a link arriving from another page, and exists when the browser resolves the fragment on first load — none of which a script running at `DOMContentLoaded` can promise.

**Rule.** **The control is a button, not a link.** An `<a href="#here">` inside a heading is a tab stop that goes nowhere the reader wanted to go — they are already looking at the section. What they want is the address, so it copies it.

**Rule.** **An id follows its heading**, so rewording a heading changes its anchor. That is the right trade while nothing links in from outside; re-run the generator after editing a heading and the check will tell you if you forget.

**Rule.** **Its accessible name includes the section.** Twelve buttons all called “Permalink” are useless in a list of controls, so each says which section it belongs to.

**Rule.** **The control is the same wherever it is used**, on a docs page or in an HTML paper. A heading that has one action uses this control; an element with several actions, such as an equation, uses the [element pill](buttons.md#small-actions-attached-to-content).

## Long lists of links

A long list of links, such as the other pages in a set, is a list of links set in columns: no bullets, and as many columns as the width holds, so twenty links take a few lines rather than twenty. The page the reader is on stays in the list as a link, and the stylesheet sets it apart.

```html
<nav aria-label="Archives">
  <ul class="ds-link-list ds-link-list--columns" role="list">
    <li><a href="/archive/astro-ph">Astrophysics</a></li>
    <li><a href="/archive/cond-mat">Condensed Matter</a></li>
    …
    <li><a href="/archive/math" aria-current="page">Mathematics</a></li>
    …
  </ul>
</nav>
```

- `.ds-link-list--columns` — With `.ds-link-list`, on a `<ul>` with one link in each item. No bullets, and as many columns as fit, each at least 14rem wide: one column on a phone. The links run down each column, then across, in the order of the markup.
- `aria-current="page"` — On the link to the page the reader is on, in any `.ds-link-list`. It stays a link. The stylesheet sets it in `--ds-text` and bold, so it does not rest on colour alone, and a screen reader announces it as the current page.
- `role="list"` — Keeps a list without bullets announced as a list: VoiceOver in Safari may not announce it otherwise.
- `<nav aria-label>` — When the list is navigation, such as the other pages in a set, it sits in a `<nav>` with a name of its own. Use `aria-label`, not `aria-labelledby` pointing at the list's heading: a heading with a Permalink would add the Permalink's words to the name.

**Rule.** **The current page stays in the list, as a link.** Mark it with `aria-current="page"` and add nothing else: no bold of your own, and no plain text in its place. The list then reads the same on every page of the set, and a screen reader says which page is open.

## Rules

- A disabled link has no `href`, so it cannot be reached or followed by keyboard or pointer. `pointer-events: none` alone is not enough: it stops a mouse, but a keyboard can still follow the link. Add `role="link"` and `aria-disabled="true"`, so a screen reader still announces it as a link that is unavailable, and the stylesheet colours it `--ds-text-disabled` (`#aeaaa4`). The underline stays so it is still recognisable as a (currently unavailable) link. The disabled state falls below AA on contrast — WCAG exempts disabled controls from contrast requirements.
- A list of author names, a navigation bar, a footer column: these are lists in which every item is a link, and none of them is underlined. The underline exists to tell a link apart from the text around it, and in a list of links there is no such text; underlining every item would add visual noise and tell the reader nothing. WCAG asks for the underline only where colour alone would have to separate a link from ordinary text, which is the case for an inline link and not for a list. The links keep Link Blue, the hover and focus states, and the visited colour where it means something. Put `.ds-link-list` on the element that holds the list. A long list is set in columns, as [Long lists of links](#long-lists-of-links) shows.
- Meets accessibility guideline [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A). An underline is needed only where a link sits in running text; in a list, the layout shows which words are links.
- [Adrian Palomares](#lists-of-links), [Mei Lin Chen](#lists-of-links), [Kwame Mensah](#lists-of-links)
- The Visited Purple is intentionally strong, not a faint after-state. Researchers reading long bibliographies and listings benefit from seeing what they have already followed up on; a too-subtle visited treatment defeats the purpose. If a specific surface (e.g., a navigation breadcrumb) needs to suppress visited styling, override `:visited { color: inherit }` locally.
- **Say where the link goes.** The link text on its own must make sense to someone who hears only the links on the page: “Endorsement policy”, not “click here”, “here” or “read more”. Put the name of the destination inside the `<a>`, not beside it.
- **A link always has an `href`, unless it is disabled.** Without one the element is not focusable, has no visited state, and does not announce as a link. Something that acts on this page rather than going somewhere is a [button](buttons.md), not a link with a click handler.
- **Keep the underline in body text.** Do not set `text-decoration: none` on an inline link. The underline is the only cue that survives forced-colors mode and a reader who cannot see the colour difference. Only a standalone link, such as one in navigation, may drop it.
- **Keep the visited colour in content.** Do not override `:visited` on links to papers, listings or references. Suppress it only where “where have I been” has no meaning, such as a breadcrumb or a menu.
- **Do not remove the focus ring.** The stylesheet draws it on `:focus-visible`, so it appears for keyboard users and not on mouse click. An `outline: none` on a link takes it away for everyone.
- **Links open in the same tab** unless the reader would lose work in progress. A reader's place in an HTML paper is work in progress, so a link from a paper to its PDF opens a new tab. A link that opens a new tab includes the external-link icon (`docs/icons/external-link.svg`) after its text, with `aria-hidden="true"` on the icon and “(opens in a new tab)” in an `.is-sr-only` span, so the change is announced and survives page translation. In a row of links that each already have an icon, such as a paper's TOC bar, the external-link icon is left out; the hidden text stays.
- **In print, an external link shows its address after its text.** An in-page link, a button and a link that is an image do not. The stylesheet does this; nothing is needed in the markup.
