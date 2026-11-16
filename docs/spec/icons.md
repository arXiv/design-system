---
page: icons.html
title: "Icons"
summary: "The design system uses the Lucide icon set which is open source, community supported, and available for both commercial and non-commercial use under the ISC license. The source files are in `docs/icons/`, one file per icon."
stylesheet: design-system.css
components:
  - id: the-set
    title: "The set"
    summary: "Selected icons currently in use. The name under each is the file name."
    notes:
      - "app-window; arrow-down; arrow-left; arrow-up; calendar; check; chevron-down; chevron-left; chevron-right; circle-alert; circle-check; circle-question-mark; circle-user; circle-x; clipboard; code; copy; download; external-link; eye; file-text; info; link; list-filter; list; maximize-2; menu; message-square; minimize-2; octagon-alert; paperclip; pencil; plus; refresh-cw; search; send; shield-check; tex; trash; triangle-alert; x; zoom-in; zoom-out"
  - id: using-an-icon
    title: "Using an icon"
    summary: "The icon inherits the text colour around it, and it is hidden from assistive technology, so the control or text beside it conveys the meaning."
    classes:
      - name: "aria-hidden=\"true\""
        does: "On every icon. The icon never conveys meaning on its own: a button gets its name from its label or an `.is-sr-only` span, and an icon beside text is decoration."
      - name: "stroke=\"currentColor\""
        does: "The icon takes the colour of the text around it, in every state and both themes."
      - name: "No width or height"
        does: "The component that holds the icon sizes it in `em`, so it follows the control’s own type size. A bare icon in text takes the line’s height."
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) Non-text Content (Level A)"
  - id: adding-an-icon
    title: "Adding an icon"
    summary: ""
    rules:
      - "**From the Lucide set.** Find the file in the Lucide release named in `docs/icons/VERSION`, keep its name unchanged, and put it in `docs/icons/`. This page will update automatically the next time it is built."
      - "**Drawing a custom icon.** Follow these specs: A 24-unit grid, a 2-unit stroke, round caps and joins, no fills, no ids or styles. Export an svg from Illustrator and add it to the icon folder. You know it is working when it cannot be told apart from the original Lucide set."
      - "**Rebuilding this page.** Then run `python3 verification/gen-icons.py`. The icon list will update itself based on the folder contents."
rules:
  - "**Color is inherited.** If not otherwise specified, the icon inherits the text colour around it. Using the Design System and not overriding colors ensures accessible contrast in both light and dark modes."
  - "**Icons are decorative, not informative.** In our markup icons are hidden from assistive technology by default, so the text beside it or control it is inside of must convey the meaning."
  - "**Automated sizing.** Do not set explicit width or height. Icons are sized by the text or component it is inside of. This allows content to reflow naturally and supports assistive magnification tools."
---

# Icons

The design system uses the Lucide icon set which is open source, community supported, and available for both commercial and non-commercial use under the ISC license. The source files are in `docs/icons/`, one file per icon.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The set

Selected icons currently in use. The name under each is the file name.

> app-window; arrow-down; arrow-left; arrow-up; calendar; check; chevron-down; chevron-left; chevron-right; circle-alert; circle-check; circle-question-mark; circle-user; circle-x; clipboard; code; copy; download; external-link; eye; file-text; info; link; list-filter; list; maximize-2; menu; message-square; minimize-2; octagon-alert; paperclip; pencil; plus; refresh-cw; search; send; shield-check; tex; trash; triangle-alert; x; zoom-in; zoom-out

## Using an icon

The icon inherits the text colour around it, and it is hidden from assistive technology, so the control or text beside it conveys the meaning.

```html
<button class="ds-btn" type="button">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">…</svg>
    Download PDF
  </button>
```

- `aria-hidden="true"` — On every icon. The icon never conveys meaning on its own: a button gets its name from its label or an `.is-sr-only` span, and an icon beside text is decoration.
- `stroke="currentColor"` — The icon takes the colour of the text around it, in every state and both themes.
- `No width or height` — The component that holds the icon sizes it in `em`, so it follows the control’s own type size. A bare icon in text takes the line’s height.

> Meets accessibility guideline [WCAG 2.2 SC 1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) Non-text Content (Level A)

## Adding an icon



**Rule.** **From the Lucide set.** Find the file in the Lucide release named in `docs/icons/VERSION`, keep its name unchanged, and put it in `docs/icons/`. This page will update automatically the next time it is built.

**Rule.** **Drawing a custom icon.** Follow these specs: A 24-unit grid, a 2-unit stroke, round caps and joins, no fills, no ids or styles. Export an svg from Illustrator and add it to the icon folder. You know it is working when it cannot be told apart from the original Lucide set.

**Rule.** **Rebuilding this page.** Then run `python3 verification/gen-icons.py`. The icon list will update itself based on the folder contents.

## Rules

### Accessibility essentials

- **Color is inherited.** If not otherwise specified, the icon inherits the text colour around it. Using the Design System and not overriding colors ensures accessible contrast in both light and dark modes.
- **Icons are decorative, not informative.** In our markup icons are hidden from assistive technology by default, so the text beside it or control it is inside of must convey the meaning.
- **Automated sizing.** Do not set explicit width or height. Icons are sized by the text or component it is inside of. This allows content to reflow naturally and supports assistive magnification tools.
