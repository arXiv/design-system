---
page: buttons.html
title: "Buttons"
summary: "Each arXiv button family shares the same mechanical spec, with color used to differentiate by context: Open Blue for public pages and Access Lime for internal tools. Public pages are everywhere a reader or author can access. Internal pages include arXiv Check and the Admin Console."
stylesheet: design-system.css
components:
  - id: button-tiers
    title: "Button tiers"
    summary: "arXiv has three button tiers: primary, secondary, and a quiet text-only button (text links can be found on the [typography](typography.html) page)."
    classes:
      - name: ".ds-btn-primary"
        does: "The page's call to action (HTML, PDF on the abstract page). One cluster per view."
      - name: ".ds-btn"
        does: "Adjacent destinations of equal weight but lower priority (TeX Source)."
      - name: ".ds-btn-text"
        does: "Real but minor actions beside a bigger choice: Copy link, Show all authors, Dismiss."
      - name: "Construction"
        does: "Both filled variants share the V3 build: a 1.5px gradient border (lighter top → darker bottom) from dual `padding-box`/`border-box` backgrounds, plus an inner vignette. Hover brightens; press drops 1px and deepens the vignette."
      - name: "Quiet tier"
        does: "The text button borrows the link’s quietness, not its identity: Link Blue, never underlined, and hover is a background wash — the same feedback the other buttons give. Underlines stay with links, so a reader can still tell “this navigates” from “this acts here.”"
      - name: "No outline tier"
        does: "The secondary is already white fill plus border, and on a white canvas a transparent fill is the same pixels as a white one."
      - name: "Icons"
        does: "Any `.ds-btn` accepts an inline SVG. The stylesheet sizes it in `em`, blocks the baseline gap, and stops it shrinking beside a long label. Set `stroke=\"currentColor\"` and nothing else."
      - name: "Disabled"
        does: "One flat `--ds-surface-muted` fill for every variant. An action that is merely not available yet takes `aria-disabled` instead — see [Forms](forms.html#validation)."
    notes:
      - "When to use a text button vs a text link: Use a text button for actions that do not navigate to a new page. Use a text link when navigating to a new page or to an anchor link on the same page."
    rules:
      - "Never mix the two primary accent colors: An Access Lime primary button on a public page, or an Open Blue button in an internal tool, is a policy violation. If the context is ambiguous, settle it first and record the answer in a code comment."
  - id: links-styled-as-buttons
    title: "Links styled as buttons"
    summary: "A control that goes to another page is a link, even when it looks like a button. The formats on the abstract page are the common case: each one is an `<a>` with the button classes, so it announces as a link, opens in a new tab, and works with JavaScript off."
    classes:
      - name: ".ds-btn, .ds-btn-primary, .ds-btn-text"
        does: "The same classes as a button. Nothing about the link changes how they look."
      - name: ".is-disabled"
        does: "Gives a link the disabled look, the same as `disabled` gives a button. It only changes the look: remove the `href` so the link stops working, and add `aria-disabled=\"true\"` so a screen reader says so."
    notes:
      - "A link cannot take the disabled attribute. To disable one, add .is-disabled, remove the href, and add aria-disabled. With the href still there the link still works while looking switched off."
  - id: small-actions-attached-to-content
    title: "Small actions attached to content"
    summary: "This component is a variant of text-only buttons and attach a row of tiny controls to a content element. It is used on the HTML papers page for figures, formula, and more. They differ from default text-only buttons via their font size, color, and surrounding container. They appear when hovering over the parent element."
    classes:
      - name: ".ds-element-pill"
        does: "The container: a white pill straddling the bottom edge of the content it belongs to. The wrapper supplies `position: relative`; the pill positions itself inside it. Documented with the other containers on [Organizing content](organizing-content.html#chrome-anchored-to-content)."
      - name: ".is-revealed"
        does: "The pill is hidden at rest and shown while the wrapped content is hovered or holds focus. The consumer adds and removes this class; the demo above keeps it on."
      - name: "The actions"
        does: "Plain `<button>` or `<a>` elements. The pill gives each a 24px target floor. Their type and colour have no class of their own yet; this page stages them locally."
  - id: the-close-control
    title: "The close control"
    summary: "Dismissing something is a simple job, but it needs a clear and consistent control everywhere it appears. Wether in an alert, a popover, an announcement banner, or an expanded figure, `.ds-close` supplies the right style."
    classes:
      - name: ".ds-close"
        does: "The whole control. 32×32, quiet tier — no fill, no border, no shadow. It takes `color: inherit`, so one rule serves all four alert palettes, the pale announcement band and dark chrome without knowing which it is on. It sets no position."
      - name: ".is-sr-only"
        does: "Required. The icon is `aria-hidden` under the icon policy, so without this span the control announces as “button” and nothing more."
    notes:
      - "Close vs Dismiss: Use Close for something the reader opened, or when there is not space for a dismiss button. Use Dismiss for something the site put in front of the user."
  - id: icon-only-buttons
    title: "Icon-only buttons"
    group: "Modifiers"
    summary: "A button whose whole label is an icon. `.ds-btn-icon` modifies the shape of a primary, secondary, or text-only button."
    classes:
      - name: ".ds-btn-text.ds-btn-destructive"
        does: "The quiet destructive: the text tier in the danger colour, for a remove action in a table row or a toolbar where a filled red on every row would be alarm rather than information. Works with a label as well as with an icon."
      - name: ".ds-btn-icon"
        does: "The shape. Square by `aspect-ratio`, `min-width: 0`, equal padding, no label gap. Always used *with* a tier — `.ds-btn .ds-btn-text .ds-btn-icon`, never `.ds-btn-icon` alone."
      - name: ".is-sr-only"
        does: "**Required.** The icon is `aria-hidden` under the icon policy, so without this span the control announces as “button” and nothing more. Carbon and Primer both make this name a required prop; the systems that leave it optional are the ones with the known gap here. Prefer it to `aria-label`, which does not survive page translation."
  - id: on-dark-surfaces
    title: "On dark surfaces"
    group: "Modifiers"
    summary: "The primary button works everywhere. The gradient border and vignette keep the edge legible on cool, warm, and dark backgrounds. The secondary button can be adapted with a modifier class when using it on a tinted background."
    classes:
      - name: ".on-tint"
        does: "On a *cool* tint, swaps the secondary's white fill for Card Grey (same luminance, warm hue) so it reads as secondary by material rather than by contrast. On a *warm* tint the default white secondary already sits comfortably."
      - name: ".on-dark"
        does: "For a field dark enough to host white text: an outreach masthead, a photo band. A white fill would read as a paper rectangle stuck to the surface, louder than the primary beside it; `.on-dark` drops the fill so the field shows through and carries the boundary on a white border. See [outreach sites](outreach.html) for where such fields are allowed."
      - name: "Not this"
        does: "A default white secondary on a cool tint pops too hard and reads as primary — that is the case `.on-tint` exists for. Do not put `.on-tint` on a warm tint: its Card Grey fill melts into the surface. And `.on-dark` is only correct on a dark field; on a light tint use `.on-tint`."
  - id: button-groups
    title: "Button groups"
    group: "Modifiers"
    summary: "A set of related buttons with a parent container class that spaces them appropriately."
    classes:
      - name: ".ds-btn-group"
        does: "The container. Flex, wrapping, vertically centred, gap `--ds-space-tight`. Nothing about buttons makes their spacing special: two side by side are siblings that belong together, so they take the same gap as any other such pair."
      - name: ".ds-btn-group--stack"
        does: "The same relationship on the other axis. Items align to the start rather than stretching."
      - name: ".ds-btn-group--end"
        does: "Pushes the group to the trailing edge. This is the action area at the end of a form, where the primary action comes last."
      - name: ".ds-btn-group--split"
        does: "One choice at each end, for a pair that goes opposite ways — Back against Continue in a stepped form."
rules:
  - "**Use the right element.** Use a `<button>` for an action that happens on this page, and an `<a>` for anything that goes to another page or another place on this one. Both take the same classes. Do not put a click handler on a link or an `href` on a button."
  - "**Every button needs a text label.** An icon-only button gets its name from a `<span class=\"is-sr-only\">` inside it that says what the button does, such as “Copy link”. Without it, a screen reader says only “button”. Do not use `title` for this, and prefer the span to `aria-label`, because page translation tools skip attributes."
  - "**Say what will happen.** Label a button with the action it performs: “Save changes”, “Download PDF”, “Delete file”. Avoid “OK”, “Yes” and “Submit” on their own, because they only make sense to someone who can see the whole screen."
  - "**Disable, do not hide.** When an action is not available, keep the button in place and add the `disabled` attribute. A button that disappears leaves the user wondering where it went. When the user can do something to make the action available, use `aria-disabled=\"true\"` instead and say what they need to do; see [Forms](forms.html#validation)."
  - "**When a button acts like a toggle.** If a button switches something on and off and stays pressed, set `aria-pressed=\"true\"` or `\"false\"` on it and update it when it changes. A colour change on its own tells a screen reader user nothing. For a setting that is saved, use the [switch](forms.html#switch) instead."
---

# Buttons

Each arXiv button family shares the same mechanical spec, with color used to differentiate by context: Open Blue for public pages and Access Lime for internal tools. Public pages are everywhere a reader or author can access. Internal pages include arXiv Check and the Admin Console.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Button tiers

arXiv has three button tiers: primary, secondary, and a quiet text-only button (text links can be found on the [typography](typography.html) page).

```html
<!-- Primary / secondary / text -->
<a class="ds-btn ds-btn-primary" href="/html/2604.22725v1">HTML</a>
<a class="ds-btn" href="/src/2604.22725v1">TeX Source</a>
<button class="ds-btn ds-btn-text" type="button">Copy link</button>
```

- `.ds-btn-primary` — The page's call to action (HTML, PDF on the abstract page). One cluster per view.
- `.ds-btn` — Adjacent destinations of equal weight but lower priority (TeX Source).
- `.ds-btn-text` — Real but minor actions beside a bigger choice: Copy link, Show all authors, Dismiss.
- `Construction` — Both filled variants share the V3 build: a 1.5px gradient border (lighter top → darker bottom) from dual `padding-box`/`border-box` backgrounds, plus an inner vignette. Hover brightens; press drops 1px and deepens the vignette.
- `Quiet tier` — The text button borrows the link’s quietness, not its identity: Link Blue, never underlined, and hover is a background wash — the same feedback the other buttons give. Underlines stay with links, so a reader can still tell “this navigates” from “this acts here.”
- `No outline tier` — The secondary is already white fill plus border, and on a white canvas a transparent fill is the same pixels as a white one.
- `Icons` — Any `.ds-btn` accepts an inline SVG. The stylesheet sizes it in `em`, blocks the baseline gap, and stops it shrinking beside a long label. Set `stroke="currentColor"` and nothing else.
- `Disabled` — One flat `--ds-surface-muted` fill for every variant. An action that is merely not available yet takes `aria-disabled` instead — see [Forms](forms.html#validation).

> When to use a text button vs a text link: Use a text button for actions that do not navigate to a new page. Use a text link when navigating to a new page or to an anchor link on the same page.

**Rule.** Never mix the two primary accent colors: An Access Lime primary button on a public page, or an Open Blue button in an internal tool, is a policy violation. If the context is ambiguous, settle it first and record the answer in a code comment.

## Links styled as buttons

A control that goes to another page is a link, even when it looks like a button. The formats on the abstract page are the common case: each one is an `<a>` with the button classes, so it announces as a link, opens in a new tab, and works with JavaScript off.

```html
<a class="ds-btn ds-btn-primary" href="/html/2604.22725v1">HTML</a>
<a class="ds-btn" href="/pdf/2604.22725v1">PDF</a>

<!-- disabled: no href, and both the class and the attribute -->
<a class="ds-btn is-disabled" aria-disabled="true">Other formats</a>
```

- `.ds-btn, .ds-btn-primary, .ds-btn-text` — The same classes as a button. Nothing about the link changes how they look.
- `.is-disabled` — Gives a link the disabled look, the same as `disabled` gives a button. It only changes the look: remove the `href` so the link stops working, and add `aria-disabled="true"` so a screen reader says so.

> A link cannot take the disabled attribute. To disable one, add .is-disabled, remove the href, and add aria-disabled. With the href still there the link still works while looking switched off.

## Small actions attached to content

This component is a variant of text-only buttons and attach a row of tiny controls to a content element. It is used on the HTML papers page for figures, formula, and more. They differ from default text-only buttons via their font size, color, and surrounding container. They appear when hovering over the parent element.

```html
<figure class="fig-wrap" style="position: relative;">
  <!-- the figure, formula, or other content -->
  <div class="ds-element-pill" style="bottom: -14px; left: 50%; transform: translateX(-50%);">
    <button type="button"><svg aria-hidden="true">…</svg> Permalink</button>
    <button type="button"><svg aria-hidden="true">…</svg> Alt text</button>
    <button type="button"><svg aria-hidden="true">…</svg> Expand</button>
  </div>
</figure>
```

- `.ds-element-pill` — The container: a white pill straddling the bottom edge of the content it belongs to. The wrapper supplies `position: relative`; the pill positions itself inside it. Documented with the other containers on [Organizing content](organizing-content.html#chrome-anchored-to-content).
- `.is-revealed` — The pill is hidden at rest and shown while the wrapped content is hovered or holds focus. The consumer adds and removes this class; the demo above keeps it on.
- `The actions` — Plain `<button>` or `<a>` elements. The pill gives each a 24px target floor. Their type and colour have no class of their own yet; this page stages them locally.

## The close control

Dismissing something is a simple job, but it needs a clear and consistent control everywhere it appears. Wether in an alert, a popover, an announcement banner, or an expanded figure, `.ds-close` supplies the right style.

```html
<button type="button" class="ds-close">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="M18 6 6 18"/>
    <path d="m6 6 12 12"/>
  </svg>
  <span class="is-sr-only">Dismiss announcement</span>
</button>
```

- `.ds-close` — The whole control. 32×32, quiet tier — no fill, no border, no shadow. It takes `color: inherit`, so one rule serves all four alert palettes, the pale announcement band and dark chrome without knowing which it is on. It sets no position.
- `.is-sr-only` — Required. The icon is `aria-hidden` under the icon policy, so without this span the control announces as “button” and nothing more.

> Close vs Dismiss: Use Close for something the reader opened, or when there is not space for a dismiss button. Use Dismiss for something the site put in front of the user.

## Icon-only buttons  (Modifiers)

A button whose whole label is an icon. `.ds-btn-icon` modifies the shape of a primary, secondary, or text-only button.

- `.ds-btn-text.ds-btn-destructive` — The quiet destructive: the text tier in the danger colour, for a remove action in a table row or a toolbar where a filled red on every row would be alarm rather than information. Works with a label as well as with an icon.
- `.ds-btn-icon` — The shape. Square by `aspect-ratio`, `min-width: 0`, equal padding, no label gap. Always used *with* a tier — `.ds-btn .ds-btn-text .ds-btn-icon`, never `.ds-btn-icon` alone.
- `.is-sr-only` — **Required.** The icon is `aria-hidden` under the icon policy, so without this span the control announces as “button” and nothing more. Carbon and Primer both make this name a required prop; the systems that leave it optional are the ones with the known gap here. Prefer it to `aria-label`, which does not survive page translation.

## On dark surfaces  (Modifiers)

The primary button works everywhere. The gradient border and vignette keep the edge legible on cool, warm, and dark backgrounds. The secondary button can be adapted with a modifier class when using it on a tinted background.

```html
<!-- Secondary on a cool tint, and on a committed color field -->
<a class="ds-btn on-tint" href="/issues">Submit a fix</a>
<a class="ds-btn on-dark" href="/subscribe">Subscribe</a>
```

- `.on-tint` — On a *cool* tint, swaps the secondary's white fill for Card Grey (same luminance, warm hue) so it reads as secondary by material rather than by contrast. On a *warm* tint the default white secondary already sits comfortably.
- `.on-dark` — For a field dark enough to host white text: an outreach masthead, a photo band. A white fill would read as a paper rectangle stuck to the surface, louder than the primary beside it; `.on-dark` drops the fill so the field shows through and carries the boundary on a white border. See [outreach sites](outreach.html) for where such fields are allowed.
- `Not this` — A default white secondary on a cool tint pops too hard and reads as primary — that is the case `.on-tint` exists for. Do not put `.on-tint` on a warm tint: its Card Grey fill melts into the surface. And `.on-dark` is only correct on a dark field; on a light tint use `.on-tint`.

## Button groups  (Modifiers)

A set of related buttons with a parent container class that spaces them appropriately.

- `.ds-btn-group` — The container. Flex, wrapping, vertically centred, gap `--ds-space-tight`. Nothing about buttons makes their spacing special: two side by side are siblings that belong together, so they take the same gap as any other such pair.
- `.ds-btn-group--stack` — The same relationship on the other axis. Items align to the start rather than stretching.
- `.ds-btn-group--end` — Pushes the group to the trailing edge. This is the action area at the end of a form, where the primary action comes last.
- `.ds-btn-group--split` — One choice at each end, for a pair that goes opposite ways — Back against Continue in a stepped form.

## Rules

- **Use the right element.** Use a `<button>` for an action that happens on this page, and an `<a>` for anything that goes to another page or another place on this one. Both take the same classes. Do not put a click handler on a link or an `href` on a button.
- **Every button needs a text label.** An icon-only button gets its name from a `<span class="is-sr-only">` inside it that says what the button does, such as “Copy link”. Without it, a screen reader says only “button”. Do not use `title` for this, and prefer the span to `aria-label`, because page translation tools skip attributes.
- **Say what will happen.** Label a button with the action it performs: “Save changes”, “Download PDF”, “Delete file”. Avoid “OK”, “Yes” and “Submit” on their own, because they only make sense to someone who can see the whole screen.
- **Disable, do not hide.** When an action is not available, keep the button in place and add the `disabled` attribute. A button that disappears leaves the user wondering where it went. When the user can do something to make the action available, use `aria-disabled="true"` instead and say what they need to do; see [Forms](forms.html#validation).
- **When a button acts like a toggle.** If a button switches something on and off and stays pressed, set `aria-pressed="true"` or `"false"` on it and update it when it changes. A colour change on its own tells a screen reader user nothing. For a setting that is saved, use the [switch](forms.html#switch) instead.
