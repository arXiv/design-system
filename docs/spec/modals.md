---
page: modals.html
title: "Modal dialogs"
summary: "A window that overlays the background page until it is answered or dismissed. There are many ways to build a modal wrong. The design system starts with a native `<dialog>`, which gets four of the five hard parts right by default. The last part is achieved with css."
stylesheet: design-system.css
components:
  - id: the-modal-dialog
    title: "The modal dialog"
    summary: "Click either button below to open a real `.ds-modal`. Modals can be closed with Escape, the close button, or by clicking one of the action buttons."
    classes:
      - name: ".ds-modal"
        does: "The dialog, on a native `<dialog>` element opened with `showModal()`. Sized against the viewport rather than its content, because a modal that outgrows the window puts its own actions out of reach."
      - name: "aria-labelledby=\"…\""
        does: "Required on the `<dialog>`, pointing at the title. It is the one thing the native element cannot infer, and without it the dialog announces with no name at all."
      - name: ".ds-modal-header, .ds-modal-body, .ds-modal-footer"
        does: "The three regions, in this order. Header and footer hold their size; the body takes what is left and scrolls, which is what keeps the title and the actions on screen when the content is long."
      - name: ".ds-modal-title"
        does: "The heading inside the header. It has the id that `aria-labelledby` points at."
      - name: ".ds-modal-footer-start"
        does: "Pushes one control to the opposite end — Cancel reads better away from the action it undoes."
      - name: ".ds-close"
        does: "The same close control as everywhere else; see [Buttons](buttons.html#the-close-control). It sits inside `.ds-modal-header`, after the title."
      - name: "data-open=\"…\", data-close"
        does: "Hooks for this page's demo script, which finds the button that opens a dialog and the controls that close it. The stylesheet gives them no meaning; your own script may use any hook it likes."
      - name: ".ds-modal-body"
        does: "Takes whatever height the header and footer leave and scrolls inside it. Nothing to add: the same markup as a short dialog, with more in the body. It scrolls whenever its content does not fit, at any screen size, including content a script adds after the dialog opens. On a screen too short to hold the header, the footer and some of the body, the whole dialog scrolls instead, so the actions are never cut off."
      - name: "tabindex=\"0\", role=\"region\", aria-labelledby (added by script)"
        does: "Not in the markup: the page script adds them while the body overflows and removes them when it fits. A scrolling area with no links or buttons in it cannot be reached from the keyboard in every browser, so a keyboard user could not scroll it. The tab stop fixes that, and the region takes the dialog's title as its name so a screen reader says what it is. Adding it only while the body overflows means a short dialog has no empty tab stop, and a body that grows later, because a script added content or the window got smaller, gets one without anyone changing the markup. The reference script is at the end of this page."
  - id: wide-for-a-viewer
    title: "Wide viewer"
    group: "Modifiers"
    summary: "For a dialog where you need maximum viewing space, like a figure, add class `.ds-modal--wide`. Don't use the wide modifier for more text only. The default width is set to a comfortable line lenth and increasing the width reduces readability."
    classes:
      - name: ".ds-modal--wide"
        does: "Added to `.ds-modal`. The dialog takes nearly the whole viewport, and its height is fixed rather than fitted to the content."
      - name: "closedby=\"any\""
        does: "Light dismiss: a click outside the dialog closes it. Off by default, on purpose. Add it to a dialog the reader is looking *through* — a figure viewer, an image. Leave it off anything that asks a question, because a stray click outside must not answer it."
      - name: ".ds-modal-footer"
        does: "Left out. A viewer has nothing to confirm, so the close control in the header is its only action."
    notes:
      - "Where the closedby attribute is unsupported the dialog keeps its close button and Escape, which is the correct thing to fall back to."
rules:
  - "**Never open one unprompted.** A modal is a response to something the reader did. One that appears on load is an interruption they did not ask for, and arXiv does not interrupt readers to tell them things."
  - "**Never nest them.** A second modal over the first leaves no way back except forward. If a modal needs a modal, it needed a page."
  - "**Nothing animates.** An entrance animation also animates the moment the page goes inert, and there is nothing here for `prefers-reduced-motion` to switch off when nothing moves."
  - "**Use the native element.** Build every modal on a `<dialog class=\"ds-modal\">` and open it with `showModal()`. Never use `show()`: it opens a *non*-modal dialog, with no backdrop, no inert page and no focus trap — every guarantee quietly absent, on markup that looks correct. Never build one from a `<div role=\"dialog\">`, which starts with none of those guarantees either."
  - "**Name the dialog.** Put `aria-labelledby` on the `<dialog>`, pointing at the id of its `.ds-modal-title`. It is the one thing the native element cannot infer, and without it the dialog announces with no name at all."
  - "**Let the browser move focus.** `showModal()` moves focus into the dialog, and `close()` returns it to the control that opened it. Do not set focus by hand on open or on close, and always close with `close()`: a dialog hidden by removing its `open` attribute or by CSS never gives focus back."
  - "**Keep Escape.** The browser closes the dialog on Escape and fires a `cancel` event first. Only intercept that event to warn about unsaved changes, and then still offer a way to close."
  - "**Keep a visible close control, and name it.** Every modal needs a visible close. Escape is not enough: it is invisible, and it is not available to someone using a pointer alone or a touch screen. The `.ds-close` holds a `<span class=\"is-sr-only\">` that says what it closes, such as “Close figure viewer”. Do not use `title` or `aria-label` for this, because page translation tools skip attributes."
  - "**Confirm the action, do not just ask.** The primary button says what it does — “Withdraw”, not “OK” — so a reader who has stopped reading the sentence still knows what they are about to press."
---

# Modal dialogs

A window that overlays the background page until it is answered or dismissed. There are many ways to build a modal wrong. The design system starts with a native `<dialog>`, which gets four of the five hard parts right by default. The last part is achieved with css.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The modal dialog

Click either button below to open a real `.ds-modal`. Modals can be closed with Escape, the close button, or by clicking one of the action buttons.

**A decision**

```html
<button class="ds-btn ds-btn-primary" type="button" data-open="demo-confirm">A decision</button>

<dialog class="ds-modal" id="demo-confirm" aria-labelledby="demo-confirm-title">
  <div class="ds-modal-header">
    <h2 class="ds-modal-title" id="demo-confirm-title">Withdraw this submission?</h2>
    <button type="button" class="ds-close" data-close>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
      <span class="is-sr-only">Close</span>
    </button>
  </div>
  <div class="ds-modal-body">
    <p>Withdrawing replaces the paper with a withdrawal notice. The submission stays in the record and keeps its identifier — arXiv is a permanent archive, so nothing is removed.</p>
    <p>This cannot be undone from here.</p>
  </div>
  <div class="ds-modal-footer">
    <button class="ds-btn ds-btn-text ds-modal-footer-start" type="button" data-close>Cancel</button>
    <button class="ds-btn ds-btn-primary" type="button" data-close>Withdraw</button>
  </div>
</dialog>
```

**A decision**

```html
// Open and close. Focus trap, focus restore, Escape and stacking are
// the element's own doing; the scroll lock is in the stylesheet.
document.getElementById('demo-confirm').showModal();
document.getElementById('demo-confirm').close();
```

**Long content**

```html
<button class="ds-btn" type="button" data-open="demo-long">Long content</button>

<dialog class="ds-modal" id="demo-long" aria-labelledby="demo-long-title">
  <div class="ds-modal-header">
    <h2 class="ds-modal-title" id="demo-long-title">What reading data is collected</h2>
    <button type="button" class="ds-close" data-close>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
      <span class="is-sr-only">Close</span>
    </button>
  </div>
  <div class="ds-modal-body">
    <p>The header and the actions stay put; only this region scrolls. That is the reason the dialog caps its own height — a modal that grows with its content eventually puts its own buttons below the bottom of the window, where the reader cannot reach the thing they opened it to do.</p>
    <p>Which papers you open, in what order, and for how long. Nothing you type. Nothing from outside arXiv.</p>
    <!-- … more paragraphs … -->
  </div>
  <div class="ds-modal-footer">
    <button class="ds-btn ds-btn-text" type="button" data-close>No thanks</button>
    <button class="ds-btn ds-btn-primary" type="button" data-close>I agree</button>
  </div>
</dialog>
```

- `.ds-modal` — The dialog, on a native `<dialog>` element opened with `showModal()`. Sized against the viewport rather than its content, because a modal that outgrows the window puts its own actions out of reach.
- `aria-labelledby="…"` — Required on the `<dialog>`, pointing at the title. It is the one thing the native element cannot infer, and without it the dialog announces with no name at all.
- `.ds-modal-header, .ds-modal-body, .ds-modal-footer` — The three regions, in this order. Header and footer hold their size; the body takes what is left and scrolls, which is what keeps the title and the actions on screen when the content is long.
- `.ds-modal-title` — The heading inside the header. It has the id that `aria-labelledby` points at.
- `.ds-modal-footer-start` — Pushes one control to the opposite end — Cancel reads better away from the action it undoes.
- `.ds-close` — The same close control as everywhere else; see [Buttons](buttons.html#the-close-control). It sits inside `.ds-modal-header`, after the title.
- `data-open="…", data-close` — Hooks for this page's demo script, which finds the button that opens a dialog and the controls that close it. The stylesheet gives them no meaning; your own script may use any hook it likes.
- `.ds-modal-body` — Takes whatever height the header and footer leave and scrolls inside it. Nothing to add: the same markup as a short dialog, with more in the body. It scrolls whenever its content does not fit, at any screen size, including content a script adds after the dialog opens. On a screen too short to hold the header, the footer and some of the body, the whole dialog scrolls instead, so the actions are never cut off.
- `tabindex="0", role="region", aria-labelledby (added by script)` — Not in the markup: the page script adds them while the body overflows and removes them when it fits. A scrolling area with no links or buttons in it cannot be reached from the keyboard in every browser, so a keyboard user could not scroll it. The tab stop fixes that, and the region takes the dialog's title as its name so a screen reader says what it is. Adding it only while the body overflows means a short dialog has no empty tab stop, and a body that grows later, because a script added content or the window got smaller, gets one without anyone changing the markup. The reference script is at the end of this page.

## Wide viewer  (Modifiers)

For a dialog where you need maximum viewing space, like a figure, add class `.ds-modal--wide`. Don't use the wide modifier for more text only. The default width is set to a comfortable line lenth and increasing the width reduces readability.

```html
<button class="ds-btn" type="button" data-open="demo-wide">Wide — a viewer</button>

<dialog class="ds-modal ds-modal--wide" id="demo-wide" closedby="any" aria-labelledby="demo-wide-title">
  <div class="ds-modal-header">
    <h2 class="ds-modal-title" id="demo-wide-title">Figure 3 — scalar perturbation growth</h2>
    <button type="button" class="ds-close" data-close>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
      <span class="is-sr-only">Close figure viewer</span>
    </button>
  </div>
  <div class="ds-modal-body">
    <!-- the figure, at full size -->
  </div>
</dialog>
```

- `.ds-modal--wide` — Added to `.ds-modal`. The dialog takes nearly the whole viewport, and its height is fixed rather than fitted to the content.
- `closedby="any"` — Light dismiss: a click outside the dialog closes it. Off by default, on purpose. Add it to a dialog the reader is looking *through* — a figure viewer, an image. Leave it off anything that asks a question, because a stray click outside must not answer it.
- `.ds-modal-footer` — Left out. A viewer has nothing to confirm, so the close control in the header is its only action.

> Where the closedby attribute is unsupported the dialog keeps its close button and Escape, which is the correct thing to fall back to.

## Rules

- **Never open one unprompted.** A modal is a response to something the reader did. One that appears on load is an interruption they did not ask for, and arXiv does not interrupt readers to tell them things.
- **Never nest them.** A second modal over the first leaves no way back except forward. If a modal needs a modal, it needed a page.
- **Nothing animates.** An entrance animation also animates the moment the page goes inert, and there is nothing here for `prefers-reduced-motion` to switch off when nothing moves.
- **Use the native element.** Build every modal on a `<dialog class="ds-modal">` and open it with `showModal()`. Never use `show()`: it opens a *non*-modal dialog, with no backdrop, no inert page and no focus trap — every guarantee quietly absent, on markup that looks correct. Never build one from a `<div role="dialog">`, which starts with none of those guarantees either.
- **Name the dialog.** Put `aria-labelledby` on the `<dialog>`, pointing at the id of its `.ds-modal-title`. It is the one thing the native element cannot infer, and without it the dialog announces with no name at all.
- **Let the browser move focus.** `showModal()` moves focus into the dialog, and `close()` returns it to the control that opened it. Do not set focus by hand on open or on close, and always close with `close()`: a dialog hidden by removing its `open` attribute or by CSS never gives focus back.
- **Keep Escape.** The browser closes the dialog on Escape and fires a `cancel` event first. Only intercept that event to warn about unsaved changes, and then still offer a way to close.
- **Keep a visible close control, and name it.** Every modal needs a visible close. Escape is not enough: it is invisible, and it is not available to someone using a pointer alone or a touch screen. The `.ds-close` holds a `<span class="is-sr-only">` that says what it closes, such as “Close figure viewer”. Do not use `title` or `aria-label` for this, because page translation tools skip attributes.
- **Confirm the action, do not just ask.** The primary button says what it does — “Withdraw”, not “OK” — so a reader who has stopped reading the sentence still knows what they are about to press.
