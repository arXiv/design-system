---
page: dividers.html
title: "Dividers"
summary: "A line between things: between sections, between items in a group, or between controls in a row. Reach for proximity first, with gaps and margins; when a line is still needed, use this component."
stylesheet: design-system.css
components:
  - id: the-divider
    title: "The divider"
    summary: "The same divider works anywhere: in the main content, in a sidebar, in a card. It is an `<hr>`, with the standard gap above and below it."
    classes:
      - name: "<hr>"
        does: "The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role=\"separator\"` for free."
  - id: tight-gap
    title: "Tight gap"
    group: "Modifiers"
    summary: "A smaller gap, for a line between items in a group."
    classes:
      - name: ".ds-divider--tight"
        does: "Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning."
      - name: ".ds-divider--flush"
        does: "No margin at all; the caller owns the spacing."
  - id: vertical-dividers
    title: "Vertical dividers"
    group: "Modifiers"
    summary: "For a row of controls, where an `<hr>` will not fit."
    classes:
      - name: ".ds-divider"
        does: "The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`."
      - name: ".ds-divider--vertical"
        does: "For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context."
---

# Dividers

A line between things: between sections, between items in a group, or between controls in a row. Reach for proximity first, with gaps and margins; when a line is still needed, use this component.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The divider

The same divider works anywhere: in the main content, in a sidebar, in a card. It is an `<hr>`, with the standard gap above and below it.

```html
<p>A section of content.</p>
<hr>
<p>The next section.</p>
<hr>
<p>And the one after it.</p>
```

- `<hr>` — The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role="separator"` for free.

## Tight gap  (Modifiers)

A smaller gap, for a line between items in a group.

```html
<p>An item in a group.</p>
<hr class="ds-divider ds-divider--tight">
<p>The next item in the same group.</p>
<hr class="ds-divider ds-divider--tight">
<p>And the one after it.</p>
```

- `.ds-divider--tight` — Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning.
- `.ds-divider--flush` — No margin at all; the caller owns the spacing.

## Vertical dividers  (Modifiers)

For a row of controls, where an `<hr>` will not fit.

```html
<div class="ds-btn-group">
<span>Search</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Submit</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Donate</span>
</div>
```

- `.ds-divider` — The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`.
- `.ds-divider--vertical` — For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context.
