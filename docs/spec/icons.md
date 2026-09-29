---
page: icons.html
title: "Icons"
summary: "The design system uses the Lucide icon set which is open source, community supported, and available for both commercial and non-commercial use under the ISC license. The source files are in `docs/icons/`, one file per icon."
stylesheet: design-system.css
components:
  - id: the-set
    title: "The set"
    summary: "Selected icons currently in use. The name under each is the file name."
  - id: using-an-icon
    title: "Using an icon"
    summary: "The icon inherits the text colour around it, and it is hidden from assistive technology, so the control or text beside it carries the meaning."
    classes:
      - name: "aria-hidden=\"true\""
        does: "On every icon. The icon never carries meaning on its own: a button gets its name from its label or an `.is-sr-only` span, and an icon beside text is decoration."
      - name: "stroke=\"currentColor\""
        does: "The icon takes the colour of the text around it, in every state and both themes."
      - name: "No width or height"
        does: "The component that holds the icon sizes it in `em`, so it follows the control’s own type size. A bare icon in text takes the line’s height."
  - id: adding-an-icon
    title: "Adding an icon"
    summary: ""
rules:
  - "**Color is inherited.** If not otherwise specified, the icon inherits the text colour around it. Using the Design System and not overriding colors ensures accessible contrast in both light and dark modes."
  - "**Icons are decorative, not informative.** In our markup icons are hidden from assistive technology by default, so the text beside it or control it is inside of must carry the meaning."
  - "**Automated sizing.** Do not set explicit width or height. Icons are sized by the text or component it is inside of. This allows content to reflow naturally and supports assistive magnification tools."
---

# Icons

The design system uses the Lucide icon set which is open source, community supported, and available for both commercial and non-commercial use under the ISC license. The source files are in `docs/icons/`, one file per icon.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The set

Selected icons currently in use. The name under each is the file name.

## Using an icon

The icon inherits the text colour around it, and it is hidden from assistive technology, so the control or text beside it carries the meaning.

```html
<button class="ds-btn" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">…</svg>
    Download PDF
  </button>
```

- `aria-hidden="true"` — On every icon. The icon never carries meaning on its own: a button gets its name from its label or an `.is-sr-only` span, and an icon beside text is decoration.
- `stroke="currentColor"` — The icon takes the colour of the text around it, in every state and both themes.
- `No width or height` — The component that holds the icon sizes it in `em`, so it follows the control’s own type size. A bare icon in text takes the line’s height.

## Adding an icon



## Rules

- **Color is inherited.** If not otherwise specified, the icon inherits the text colour around it. Using the Design System and not overriding colors ensures accessible contrast in both light and dark modes.
- **Icons are decorative, not informative.** In our markup icons are hidden from assistive technology by default, so the text beside it or control it is inside of must carry the meaning.
- **Automated sizing.** Do not set explicit width or height. Icons are sized by the text or component it is inside of. This allows content to reflow naturally and supports assistive magnification tools.
