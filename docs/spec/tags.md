---
page: tags.html
title: "Tags"
summary: "A small rounded element used for categories, search filters, states, and other small multiples. Tags remain the same across public and internal pages."
stylesheet: design-system.css
components:
  - id: the-three-levels
    title: "Three tag levels"
    summary: "Size and shape remain the same across all levels, prominence comes from color and text. Reach for the quietest one that still does the job."
    classes:
      - name: ".ds-tag"
        does: "Base. Mono, uppercase, 999px, `min-height: 24px` for the WCAG 2.2 target floor. Goes on a `<span>`, an `<a>`, or a `<button>`."
      - name: ".ds-tag--keep-case"
        does: "Opt out of uppercase. Required for identifiers, and for long labels: past roughly three words, or with mixed-case names inside, caps slow reading down."
      - name: ".ds-tag--info"
        does: "The info tint, the same blue the info alert uses. Categories, topics, and neutral states."
      - name: ".ds-tag--success, .ds-tag--warning, .ds-tag--error"
        does: "Only when the label reports a condition."
  - id: labels-as-links
    title: "Labels as links"
    group: "Modifiers"
    summary: "A tag is a `<span>` unless it does something. A tag that goes somewhere is an `<a>` with an `href`, and a tag that acts on the page, such as a filter that switches on and off, is a `<button>`. Both take the same classes, both can be reached from the keyboard, and both show the focus ring. A `<span>` with a click handler does neither."
    classes:
      - name: "<a>, <button>"
        does: "The element gives the tag its hover, its focus ring, and its keyboard behaviour; no class does. A link has an `href`; a button has `type=\"button\"`, and `aria-pressed` if it switches something on and off."
    rules:
      - "A tag should not stand in for a link: A tag labels or categorizes the thing it sits on. A label might be a link when it makes sense, but it should never replace a text link as the better way to navigate off the page."
  - id: rectangular-labels
    title: "Rectangular labels"
    summary: "Rectangular instead of pill-shaped, this label variant is useful in very dense interfaces where you need to reclaim the extra left and right margin space."
    classes:
      - name: ".ds-tag--rectangle"
        does: "The shape only: square corners and less side padding. Add it to any tag, at any level, with any other modifier."
  - id: complex-tags
    title: "More complex uses of tags"
    summary: "Different parts of a tag can be combined, even doubled, for more complex uses. Consult with the design team on your specific use case. Below is one example from the Admin console of tags that carry both a category name and a nested `.ds-tag-note` that says where it came from."
    classes:
      - name: ".ds-tag-note"
        does: "A small badge nested inside a tag, saying where it came from — usually a username."
      - name: ".ds-tag-note--auto"
        does: "The same badge, quieter, for provenance the system set rather than a person. “auto” is a fact about the row; a username is someone to ask."
      - name: ".ds-tag-remove"
        does: "The ✕ control inside an editable tag. A `<button type=\"button\">` that is the last child of the tag. Removing the tag is the host’s job."
      - name: ".is-sr-only"
        does: "Required inside the remove control. The ✕ glyph is `aria-hidden`, so without this span the button announces as “button” and nothing more. Say what it removes: “Remove math.AP”."
    rules:
      - "The remove control is the only editing the tag knows about: Anything else a person can do to a tag, such as drag it into a different order or pick it from a search box, belongs to the editor around the tags, not to `.ds-tag`. That editor is not documented yet."
rules:
  - "**Use the element that matches the job.** Use tags for labels, not to replace content that should be buttons or links instead."
  - "**Uppercase is applied with CSS, never typed.** The underlying text then stays correct for copy-and-paste, in-page search, and screen readers."
  - "**Keep the case of every category and identifier.** Put `.ds-tag--keep-case` on any tag that holds a category name or an arXiv ID, so that `physics.optics` is never shown as `PHYSICS.OPTICS`."
  - "**Color is never the only signal.** The label’s own words carry the meaning. A negative or removed state says so in text, not only in red."
  - "**Name the remove control.** Every `.ds-tag-remove` holds a `<span class=\"is-sr-only\">` that says what it removes, such as “Remove cs.AI”, and the ✕ glyph sits in a span with `aria-hidden=\"true\"`. Do not use `title` or `aria-label` for this, because page translation tools skip attributes."
---

# Tags

A small rounded element used for categories, search filters, states, and other small multiples. Tags remain the same across public and internal pages.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Three tag levels

Size and shape remain the same across all levels, prominence comes from color and text. Reach for the quietest one that still does the job.

```html
<span class="ds-tag">Preprint</span>
<span class="ds-tag">12 requests</span>

<!-- A category. Always --keep-case. -->
<span class="ds-tag ds-tag--keep-case">cs.AI</span>
```

```html
<span class="ds-tag ds-tag--info">Policy</span>

<!-- A category. Always --keep-case. -->
<span class="ds-tag ds-tag--info ds-tag--keep-case">math.CO</span>

<!-- A topic that links to its listing -->
<a class="ds-tag ds-tag--info" href="/list/policy">Policy</a>
```

```html
<span class="ds-tag ds-tag--success">Valid</span>
<span class="ds-tag ds-tag--warning">On hold</span>
<span class="ds-tag ds-tag--error">Removed</span>

<!-- A neutral state is info, not a status -->
<span class="ds-tag ds-tag--info">Under review</span>
```

- `.ds-tag` — Base. Mono, uppercase, 999px, `min-height: 24px` for the WCAG 2.2 target floor. Goes on a `<span>`, an `<a>`, or a `<button>`.
- `.ds-tag--keep-case` — Opt out of uppercase. Required for identifiers, and for long labels: past roughly three words, or with mixed-case names inside, caps slow reading down.
- `.ds-tag--info` — The info tint, the same blue the info alert uses. Categories, topics, and neutral states.
- `.ds-tag--success, .ds-tag--warning, .ds-tag--error` — Only when the label reports a condition.

## Labels as links  (Modifiers)

A tag is a `<span>` unless it does something. A tag that goes somewhere is an `<a>` with an `href`, and a tag that acts on the page, such as a filter that switches on and off, is a `<button>`. Both take the same classes, both can be reached from the keyboard, and both show the focus ring. A `<span>` with a click handler does neither.

```html
<!-- Goes to the category listing -->
<a class="ds-tag ds-tag--info ds-tag--keep-case" href="/list/cs.AI">cs.AI</a>

<!-- Acts on this page: a filter that is on -->
<button type="button" class="ds-tag" aria-pressed="true">Open access</button>
```

- `<a>, <button>` — The element gives the tag its hover, its focus ring, and its keyboard behaviour; no class does. A link has an `href`; a button has `type="button"`, and `aria-pressed` if it switches something on and off.

**Rule.** A tag should not stand in for a link: A tag labels or categorizes the thing it sits on. A label might be a link when it makes sense, but it should never replace a text link as the better way to navigate off the page.

## Rectangular labels

Rectangular instead of pill-shaped, this label variant is useful in very dense interfaces where you need to reclaim the extra left and right margin space.

```html
<span class="ds-tag ds-tag--success ds-tag--rectangle">Approved</span>
<span class="ds-tag ds-tag--warning ds-tag--rectangle">Flagged</span>
<span class="ds-tag ds-tag--error ds-tag--rectangle">Removed</span>
<span class="ds-tag ds-tag--info ds-tag--rectangle">Submitted</span>
```

- `.ds-tag--rectangle` — The shape only: square corners and less side padding. Add it to any tag, at any level, with any other modifier.

## More complex uses of tags

Different parts of a tag can be combined, even doubled, for more complex uses. Consult with the design team on your specific use case. Below is one example from the Admin console of tags that carry both a category name and a nested `.ds-tag-note` that says where it came from.

```html
<!-- With a nested provenance badge -->
<span class="ds-tag ds-tag--info ds-tag--keep-case">physics.bio-ph
  <span class="ds-tag-note">bsmith</span>
</span>
<span class="ds-tag ds-tag--info ds-tag--keep-case">cs.CV
  <span class="ds-tag-note ds-tag-note--auto">auto</span>
</span>

<!-- Revoked: the error variant carries the whole thing -->
<span class="ds-tag ds-tag--error ds-tag--keep-case">− physics.gen-ph
  <span class="ds-tag-note">ginsparg</span>
</span>

<!-- Editable, with a remove control -->
<span class="ds-tag ds-tag--info ds-tag--keep-case">math.AP
  <button class="ds-tag-remove" type="button">
    <span aria-hidden="true">✕</span>
    <span class="is-sr-only">Remove math.AP</span>
  </button>
</span>
```

- `.ds-tag-note` — A small badge nested inside a tag, saying where it came from — usually a username.
- `.ds-tag-note--auto` — The same badge, quieter, for provenance the system set rather than a person. “auto” is a fact about the row; a username is someone to ask.
- `.ds-tag-remove` — The ✕ control inside an editable tag. A `<button type="button">` that is the last child of the tag. Removing the tag is the host’s job.
- `.is-sr-only` — Required inside the remove control. The ✕ glyph is `aria-hidden`, so without this span the button announces as “button” and nothing more. Say what it removes: “Remove math.AP”.

**Rule.** The remove control is the only editing the tag knows about: Anything else a person can do to a tag, such as drag it into a different order or pick it from a search box, belongs to the editor around the tags, not to `.ds-tag`. That editor is not documented yet.

## Rules

- **Use the element that matches the job.** Use tags for labels, not to replace content that should be buttons or links instead.
- **Uppercase is applied with CSS, never typed.** The underlying text then stays correct for copy-and-paste, in-page search, and screen readers.
- **Keep the case of every category and identifier.** Put `.ds-tag--keep-case` on any tag that holds a category name or an arXiv ID, so that `physics.optics` is never shown as `PHYSICS.OPTICS`.
- **Color is never the only signal.** The label’s own words carry the meaning. A negative or removed state says so in text, not only in red.
- **Name the remove control.** Every `.ds-tag-remove` holds a `<span class="is-sr-only">` that says what it removes, such as “Remove cs.AI”, and the ✕ glyph sits in a span with `aria-hidden="true"`. Do not use `title` or `aria-label` for this, because page translation tools skip attributes.
