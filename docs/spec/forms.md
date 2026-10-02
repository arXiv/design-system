---
page: forms.html
title: "Forms & validation"
summary: "The design system supports highly accessible forms with robust validation display options. Explore validation examples in action in this [submission metadata mockup](../whiteboard/mockups/public/submission-metadata/index.html)."
stylesheet: design-system.css
components:
  - id: fields
    title: "Fields"
    summary: "A field is a label (for example, Email address), a control (for example, input field, checkbox), optional help text, and a slot for an error, warning or info message. That order never changes. Labels sit above their controls, and related fields group by spacing rather than boxes."
    classes:
      - name: ".ds-form"
        does: "Wraps the fields. Half-width fields share a line, a full-width one takes its own, and anything that is not a field takes a whole row. Optional: a plain `<form>` stacks every field."
      - name: ".ds-field"
        does: "Wraps one label, control, hint and message, in that order, and supplies the spacing between fields."
      - name: ".ds-label"
        does: "The label. Always present, always above the control, and always tied to it with `for`."
      - name: ".label-optional"
        does: "On the label of an *optional* field, holding the word `(optional)`. Required fields have no marker; they take `required` and `aria-required=\"true\"` on the control instead."
      - name: ".ds-input"
        does: "The control. Goes on `input`, `select` and `textarea` alike."
      - name: ".ds-hint"
        does: "Help text, after the control. Give it an `id` and name it in the control's `aria-describedby`. Say what good input looks like *before* someone gets it wrong."
      - name: ".ds-check"
        does: "A checkbox or radio row: a `<label>` holding the native control and a `<span>` with the text. The whole label is the target."
    notes:
      - "Field widths are set by the type of control, on the assumption that the element already tells you about how much someone will type. If you need to override a default width, two classes are available (see [Field width](#field-width))."
  - id: validation
    title: "Validation"
    summary: "Fields can be in three possible states: normal, validated, or disabled. Validation styles change based on the error [disposition](#disposition-tiers), that is, its severity."
    classes:
      - name: ".is-invalid"
        does: "On the control, for the error tier. Pair with `aria-invalid=\"true\"`."
      - name: ".is-warning"
        does: "On the control, for the warning tier. No `aria-invalid`: the value is accepted."
      - name: ".is-info"
        does: "On the control, for the info tier: arXiv changed the value and is telling the author. No `aria-invalid`."
      - name: ".field-error, .field-warning, .field-info"
        does: "The message, **after** the control and after the hint when there is one, one class per tier. Needs an `id` that the control's `aria-describedby` names. Keep it `hidden` until it applies."
      - name: ".field-messages"
        does: "An `<ol>` when one field has several problems. Each `<li>` takes its own tier class, and the list takes the `id` the control points at. The control takes the class of the worst tier in the list."
      - name: "[disabled]"
        does: "On the control. The label and hint stay; the control greys out and leaves the tab order. For a control that could explain why it is unavailable, prefer `aria-disabled=\"true\"`, which looks the same; on a field, pair it with `readonly`, because `aria-disabled` alone does not stop typing. See the accessibility essentials."
      - name: "aria-describedby=\"hb-h hb-m\""
        does: "Names the hint first, then the message, so a screen reader reads them in the order they appear."
  - id: alerts-in-forms
    title: "Alerts in forms"
    summary: "Repeat the problems below the page heading using an alert component. Errors are grouped into alerts by disposition (error, warning, info) and are not mixed. Each alert holds an ordered list of items. See [Alerts](alerts.html) for full documentation. Below is an example of using an alert specifically for validation."
    classes:
      - name: ".ds-alert--error, .ds-alert--warning, .ds-alert"
        does: "One alert per severity, never a mixed one: red has to mean “you cannot proceed”, and a non-blocking item inside a red alert destroys that. Two problems of two severities means two alerts, in severity order. A warning summary is the same construction in `.ds-alert--warning`, and an automatic change is a bare `.ds-alert`, which is the info state. Takes `role=\"alert\"` for error and warning, `role=\"status\"` for info. See [Alerts](alerts.html) for the four severities and their markup."
      - name: ".ds-alert-title"
        does: "Includes the count. The body under it says what that severity means for the reader: whether they may continue."
      - name: "<ol>"
        does: "One row per problem, each an `<a>` linking to its field. Rows repeat the field name even when several name the same field: without it the reader cannot tell whether three problems mean one field to visit or three. Derive every count and every row from the field results; a summary written by hand can disagree with the fields it describes, and eventually will."
    rules:
      - "2 blocking errors: Blocking errors must be corrected before you can continue. Select an item to jump to that field."
  - id: switch
    title: "Switch"
    summary: "A boolean that applies the moment it is flipped. If the change needs a Save step then use a checkbox, not a switch."
    classes:
      - name: ".ds-switch"
        does: "The `<label>` that wraps the whole control. The visible text goes inside it, because that is what names the switch; a switch with only a heading beside it has no accessible name."
      - name: "role=\"switch\""
        does: "On the checkbox input. With it a screen reader says “on” and “off”; without it, “checkbox, checked”. The input stays a real checkbox, so the keyboard behaviour, the state and the form value are native and it works with no JavaScript."
      - name: ".ds-switch-track, .ds-switch-thumb"
        does: "The drawn background and the thumb that moves across it. Both required, nested as shown, directly after the input. Only the background fill changes with the state: Border Light when off, the accent when on (Open Blue public, Access Lime inside `.ds-internal`). The UI Boundary Grey edge and the Repository Brown thumb stay the same in both states and both themes."
      - name: ".ds-switch-label"
        does: "The visible text. Its colour follows the state; nothing else about it changes."
      - name: "[disabled]"
        does: "On the input. The background and the label grey out together."
  - id: segmented-control
    title: "Segmented control"
    summary: "An exclusive choice rendered as adjacent buttons, for a decision where every option should stay visible. Two to four options; past that it is a `<select>` or a radio group, because a row of six buttons stops being scannable and starts being a wall."
    classes:
      - name: ".ds-seg"
        does: "A `<fieldset>` holding two to four `.ds-seg-btn`."
      - name: "<legend>"
        does: "Required. It is the group's accessible name: without it a screen reader announces three buttons and never says what they decide. Hide it with `.is-sr-only` when the surrounding text already says it; hide it, do not omit it."
      - name: ".ds-seg-btn"
        does: "One option, a `<button type=\"button\">`. Buttons and not a radio group on purpose: this is for a decision that acts when clicked. A choice that is part of a form that gets submitted is a radio group."
      - name: ".ds-seg-btn--positive, .ds-seg-btn--negative"
        does: "Accept and reject; a bare `.ds-seg-btn` is informational. They take the success, info and error tokens and mean the same thing those mean everywhere else; they are not free colours to pick from, and they flip for dark mode with the rest of the status palette."
      - name: ".is-active"
        does: "The selected option, with `aria-pressed=\"true\"`; every other option has `aria-pressed=\"false\"`, so a screen reader says which one is selected. Set by script when an option is clicked, and removed from the others; the stylesheet gives the buttons no behaviour."
    notes:
      - "Nothing is selected until something is selected: the undecided example is the resting state of a decision nobody has made yet, and it is a real state, not a bug to hide by pre-selecting the middle option."
  - id: tooltip
    title: "Tooltip"
    summary: "A short explanation attached to a control, on hover and on focus. The lighter half of the popover family: no title, no close button, and never content that exists nowhere else."
    classes:
      - name: ".ds-tooltip-host"
        does: "Wraps the trigger and the bubble, and positions the bubble. It sits beside the `<label>`, never inside it: a label forwards clicks to the control it names, so a button nested in one is a button whose clicks land somewhere else."
      - name: ".ds-label-row"
        does: "Puts a label and its tooltip trigger on one line, in place of the label's own spacing. The icon trigger inside it is compact and still clears the 24px target."
      - name: "aria-describedby=\"tip-doi\""
        does: "On the trigger, naming the tooltip's `id`. The tooltip describes the control and is never its accessible name: a name that only appears on hover is a name most people never get, so an icon trigger has an `.is-sr-only` label of its own, as above."
      - name: "aria-disabled=\"true\""
        does: "On an unavailable action that explains itself. The reason goes in a tooltip by default, because it takes no room and does not move the layout. Where there is room, it can sit under the actions as `.ds-hint` text instead, named in the button's `aria-describedby`. Use `aria-disabled`, not `disabled`: a disabled button cannot take focus, so a keyboard user would never reach the reason. The script must ignore clicks while it is set."
      - name: ".ds-tooltip"
        does: "The bubble, with `role=\"tooltip\"` and the `id`. It opens downward and toward the inline end, on hover and on focus, with no JavaScript. Escape must close it without moving focus, which CSS cannot do: a listener sets `hidden` on it, and clears it when the pointer or focus arrives again. The script on this page is the reference."
      - name: ".ds-tooltip-body"
        does: "The text. Short, and never content that exists nowhere else."
      - name: ".ds-tooltip--end"
        does: "For a host near the trailing edge of its container, like the Continue button above: the bubble runs back toward the start instead of off screen. Both directions use logical properties, so both are correct in a right-to-left script."
    notes:
      - "Not for anything required: if the reader must have it to fill the field in, it is help text under the control, not a tooltip, which is for the person who stops and wonders."
  - id: field-width
    title: "Field width"
    group: "Modifiers"
    summary: "Default field widths are set to follow the expected amount of content and are an important clue for users as to what is expected in any given field. Widths will generally not need any manual adjustment but two overrides exist just in case: `.ds-field--short` and `.ds-field--full`."
    classes:
      - name: ".ds-field--short"
        does: "Caps the field at 11rem, for a code, an identifier or a year."
      - name: ".ds-field--full"
        does: "Releases the cap, for something that genuinely wants the whole measure."
      - name: ".ds-field--sm, .ds-field--md, .ds-field--lg"
        does: "Internal tools only, in `internal-tools.css`: caps the control at 240px, 360px or 480px. Internal screens are dense enough to need field widths chosen rather than inferred, so on an internal form a person picks the size instead of the input `type` picking it. Use the pair above on public pages and this trio on internal pages, and do not mix them on one form."
rules:
  - "**Labels go above the control.** A label-left, field-right layout gives a ragged edge and reads badly on a phone."
  - "**Group related content with spacing**, not by adding more bordered divs. If spacing is insufficient then the form might be calling for subsections or to be broken up into different pages."
  - "**The action bar is right-aligned**, with the primary action button (Save, Continue, etc.) the last one on the right. On long forms, consider repeating it at the top so the user does not need to scroll as much."
  - "**Disabled, not missing.** An action that is unavailable renders disabled, with the reason in a tooltip, or as help text under the actions where there is room (see [Tooltip](#tooltip)). The reader can see it exists and is not left wondering what is happening."
  - "**Every control has a label.** Put a real `<label for>` on every control, pointing at the control's `id`. Hide it with `.is-sr-only` when there is no room for it; do not leave it out."
  - "**Mark the optional fields, not the required ones.** Put `(optional)` inside the visible label of an optional field. Put `required` and `aria-required=\"true\"` on every required control: required fields have no visual marker, so this pair is the only signal a screen reader gets. Never put either word in `aria-label` or `title`."
  - "**Connect every hint and message to its control.** Give each `.ds-hint` and each message an `id`, and list them in the control's `aria-describedby`. Without that a screen reader announces the field and nothing else."
  - "**Use `aria-invalid` for errors only.** Set `aria-invalid=\"true\"` on a control in the error tier and remove it when the error clears. A warning is not invalid, and an info message is not a problem at all."
  - "**Say the tier in words.** Colour and a border are never the only signal (WCAG 1.4.1). The message says what is wrong or what changed, or includes a visually hidden “Error:” or “Warning:” prefix."
  - "**Validate on submit, then move focus.** Do not tell someone they are wrong while they are still typing. Once a field is invalid, re-check it on every `input` event so the error clears the moment it is fixed. When submission fails, move focus to the first invalid field."
  - "**Give the summary its role.** The alert above the form takes `role=\"alert\"` for errors and warnings, so a screen reader announces it at once, and every row in it links to its field."
  - "**Prefer `aria-disabled` to `disabled` for a control that could explain itself.** `disabled` leaves the tab order entirely, so a user who cannot proceed finds nothing there and no reason why. The two must look identical."
---

# Forms & validation

The design system supports highly accessible forms with robust validation display options. Explore validation examples in action in this [submission metadata mockup](../whiteboard/mockups/public/submission-metadata/index.html).

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Fields

A field is a label (for example, Email address), a control (for example, input field, checkbox), optional help text, and a slot for an error, warning or info message. That order never changes. Labels sit above their controls, and related fields group by spacing rather than boxes.

```html
<form class="ds-form">
  <div class="ds-field">
    <label class="ds-label" for="f-email">Email address</label>
    <input class="ds-input" id="f-email" type="email" required aria-required="true" aria-describedby="f-email-hint" value="e.vasquez@example.edu">
    <p class="ds-hint" id="f-email-hint">Used only to confirm your submission.</p>
  </div>
  <div class="ds-field">
    <label class="ds-label" for="f-cat">Primary category</label>
    <select class="ds-input" id="f-cat" required aria-required="true">
      <option>hep-th — High Energy Physics – Theory</option>
      <option>math.CO — Combinatorics</option>
      <option>physics.optics — Optics</option>
    </select>
  </div>
  <div class="ds-field ds-field--short">
    <label class="ds-label" for="f-orcid">ORCID iD<span class="label-optional">(optional)</span></label>
    <input class="ds-input" id="f-orcid" type="text" placeholder="0000-0000-0000-0000">
  </div>
  <label class="ds-check">
    <input type="checkbox" checked>
    <span>Email me when the moderators respond</span>
  </label>
  <div class="ds-btn-group ds-btn-group--end">
    <button class="ds-btn ds-btn-text" type="button">Cancel</button>
    <button class="ds-btn ds-btn-primary" type="submit">Save changes</button>
  </div>
</form>
```

- `.ds-form` — Wraps the fields. Half-width fields share a line, a full-width one takes its own, and anything that is not a field takes a whole row. Optional: a plain `<form>` stacks every field.
- `.ds-field` — Wraps one label, control, hint and message, in that order, and supplies the spacing between fields.
- `.ds-label` — The label. Always present, always above the control, and always tied to it with `for`.
- `.label-optional` — On the label of an *optional* field, holding the word `(optional)`. Required fields have no marker; they take `required` and `aria-required="true"` on the control instead.
- `.ds-input` — The control. Goes on `input`, `select` and `textarea` alike.
- `.ds-hint` — Help text, after the control. Give it an `id` and name it in the control's `aria-describedby`. Say what good input looks like *before* someone gets it wrong.
- `.ds-check` — A checkbox or radio row: a `<label>` holding the native control and a `<span>` with the text. The whole label is the target.

> Field widths are set by the type of control, on the assumption that the element already tells you about how much someone will type. If you need to override a default width, two classes are available (see [Field width](#field-width)).

## Validation

Fields can be in three possible states: normal, validated, or disabled. Validation styles change based on the error [disposition](#disposition-tiers), that is, its severity.

```html
<div class="ds-field ds-field--full">
  <label class="ds-label" for="v3">Abstract</label>
  <input class="ds-input is-invalid" id="v3" type="text" aria-invalid="true" aria-describedby="v3-m" value="<br>Our analysis introduces">
  <p class="field-error" id="v3-m">Remove the HTML markup <br>.</p>
</div>

<div class="ds-field ds-field--full">
  <label class="ds-label" for="v4">ACM classification<span class="label-optional">(optional)</span></label>
  <input class="ds-input is-warning" id="v4" type="text" aria-describedby="v4-m" value="s 25">
  <p class="field-warning" id="v4-m">This does not look like an ACM code. Expected form: F.2.2.</p>
</div>

<div class="ds-field ds-field--full">
  <label class="ds-label" for="m1">Abstract</label>
  <textarea class="ds-input is-invalid" id="m1" rows="3" aria-invalid="true" aria-describedby="m1-m">Abstract: We study the convergence of stochastic gradient methods.<br>Data at https://example.org/sgd.</textarea>
  <ol class="field-messages" id="m1-m">
    <li class="field-error">Do not begin the abstract with the word “Abstract”.</li>
    <li class="field-error">Remove the HTML markup <br>.</li>
    <li class="field-warning">Font commands are not processed and appear literally.</li>
    <li class="field-warning">Add a space between a URL and the punctuation after it.</li>
  </ol>
</div>
```

```html
<div class="ds-field ds-field--full">
  <label class="ds-label" for="hb">ACM classification<span class="label-optional">(optional)</span></label>
  <input class="ds-input is-warning" id="hb" type="text" aria-describedby="hb-h hb-m" value="s 25">
  <p class="ds-hint" id="hb-h">Example: F.2.2; I.2.7</p>
  <p class="field-warning" id="hb-m">This does not look like an ACM code. Expected form: F.2.2.</p>
</div>
```

- `.is-invalid` — On the control, for the error tier. Pair with `aria-invalid="true"`.
- `.is-warning` — On the control, for the warning tier. No `aria-invalid`: the value is accepted.
- `.is-info` — On the control, for the info tier: arXiv changed the value and is telling the author. No `aria-invalid`.
- `.field-error, .field-warning, .field-info` — The message, **after** the control and after the hint when there is one, one class per tier. Needs an `id` that the control's `aria-describedby` names. Keep it `hidden` until it applies.
- `.field-messages` — An `<ol>` when one field has several problems. Each `<li>` takes its own tier class, and the list takes the `id` the control points at. The control takes the class of the worst tier in the list.
- `[disabled]` — On the control. The label and hint stay; the control greys out and leaves the tab order. For a control that could explain why it is unavailable, prefer `aria-disabled="true"`, which looks the same; on a field, pair it with `readonly`, because `aria-disabled` alone does not stop typing. See the accessibility essentials.
- `aria-describedby="hb-h hb-m"` — Names the hint first, then the message, so a screen reader reads them in the order they appear.

## Alerts in forms

Repeat the problems below the page heading using an alert component. Errors are grouped into alerts by disposition (error, warning, info) and are not mixed. Each alert holds an ordered list of items. See [Alerts](alerts.html) for full documentation. Below is an example of using an alert specifically for validation.

```html
<div class="ds-alert ds-alert--error" role="alert">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" aria-hidden="true">
    <circle cx="12" cy="12" r="10"/>
    <path d="m15 9-6 6"/>
    <path d="m9 9 6 6"/>
  </svg>
  <div class="ds-alert-content">
    <p class="ds-alert-title">2 blocking errors</p>
    <p>Blocking errors must be corrected before you can continue. Select an item to jump to that field.</p>
    <ol>
      <li><a href="#m1">Abstract — do not begin with the word “Abstract”</a></li>
      <li><a href="#m1">Abstract — remove the HTML markup <br></a></li>
    </ol>
  </div>
</div>
```

- `.ds-alert--error, .ds-alert--warning, .ds-alert` — One alert per severity, never a mixed one: red has to mean “you cannot proceed”, and a non-blocking item inside a red alert destroys that. Two problems of two severities means two alerts, in severity order. A warning summary is the same construction in `.ds-alert--warning`, and an automatic change is a bare `.ds-alert`, which is the info state. Takes `role="alert"` for error and warning, `role="status"` for info. See [Alerts](alerts.html) for the four severities and their markup.
- `.ds-alert-title` — Includes the count. The body under it says what that severity means for the reader: whether they may continue.
- `<ol>` — One row per problem, each an `<a>` linking to its field. Rows repeat the field name even when several name the same field: without it the reader cannot tell whether three problems mean one field to visit or three. Derive every count and every row from the field results; a summary written by hand can disagree with the fields it describes, and eventually will.

**Rule.** 2 blocking errors: Blocking errors must be corrected before you can continue. Select an item to jump to that field.

## Switch

A boolean that applies the moment it is flipped. If the change needs a Save step then use a checkbox, not a switch.

```html
<label class="ds-switch">
  <input type="checkbox" role="switch" checked>
  <span class="ds-switch-track"><span class="ds-switch-thumb"></span></span>
  <span class="ds-switch-label">Email digest</span>
</label>
```

- `.ds-switch` — The `<label>` that wraps the whole control. The visible text goes inside it, because that is what names the switch; a switch with only a heading beside it has no accessible name.
- `role="switch"` — On the checkbox input. With it a screen reader says “on” and “off”; without it, “checkbox, checked”. The input stays a real checkbox, so the keyboard behaviour, the state and the form value are native and it works with no JavaScript.
- `.ds-switch-track, .ds-switch-thumb` — The drawn background and the thumb that moves across it. Both required, nested as shown, directly after the input. Only the background fill changes with the state: Border Light when off, the accent when on (Open Blue public, Access Lime inside `.ds-internal`). The UI Boundary Grey edge and the Repository Brown thumb stay the same in both states and both themes.
- `.ds-switch-label` — The visible text. Its colour follows the state; nothing else about it changes.
- `[disabled]` — On the input. The background and the label grey out together.

## Segmented control

An exclusive choice rendered as adjacent buttons, for a decision where every option should stay visible. Two to four options; past that it is a `<select>` or a radio group, because a row of six buttons stops being scannable and starts being a wall.

```html
<fieldset class="ds-seg">
  <legend class="is-sr-only">Positive example</legend>
  <button aria-pressed="true" type="button" class="ds-seg-btn ds-seg-btn--positive is-active">Author</button>
  <button aria-pressed="false" type="button" class="ds-seg-btn">Proxy</button>
  <button aria-pressed="false" type="button" class="ds-seg-btn ds-seg-btn--negative">No</button>
</fieldset>
```

- `.ds-seg` — A `<fieldset>` holding two to four `.ds-seg-btn`.
- `<legend>` — Required. It is the group's accessible name: without it a screen reader announces three buttons and never says what they decide. Hide it with `.is-sr-only` when the surrounding text already says it; hide it, do not omit it.
- `.ds-seg-btn` — One option, a `<button type="button">`. Buttons and not a radio group on purpose: this is for a decision that acts when clicked. A choice that is part of a form that gets submitted is a radio group.
- `.ds-seg-btn--positive, .ds-seg-btn--negative` — Accept and reject; a bare `.ds-seg-btn` is informational. They take the success, info and error tokens and mean the same thing those mean everywhere else; they are not free colours to pick from, and they flip for dark mode with the rest of the status palette.
- `.is-active` — The selected option, with `aria-pressed="true"`; every other option has `aria-pressed="false"`, so a screen reader says which one is selected. Set by script when an option is clicked, and removed from the others; the stylesheet gives the buttons no behaviour.

> Nothing is selected until something is selected: the undecided example is the resting state of a decision nobody has made yet, and it is a real state, not a bug to hide by pre-selecting the middle option.

## Tooltip

A short explanation attached to a control, on hover and on focus. The lighter half of the popover family: no title, no close button, and never content that exists nowhere else.

```html
<!-- Label with a tooltip -->
<div class="ds-field">
  <div class="ds-label-row">
    <label class="ds-label" for="f-doi">DOI</label>
    <span class="ds-tooltip-host">
      <button type="button" class="ds-btn ds-btn-text ds-btn-icon" aria-describedby="tip-doi">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="12" cy="12" r="10"/>
          <path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/>
          <path d="M12 17h.01"/>
        </svg>
        <span class="is-sr-only">What is a DOI?</span>
      </button>
      <span class="ds-tooltip" id="tip-doi" role="tooltip">
        <span class="ds-tooltip-body">If the paper has been published, the publisher's DOI. Leave it empty otherwise; arXiv mints its own.</span>
      </span>
    </span>
  </div>
  <input class="ds-input" id="f-doi" type="text" placeholder="10.1000/example">
</div>

<!-- Disabled action, reason in a tooltip -->
<div class="ds-btn-group ds-btn-group--end">
  <button type="button" class="ds-btn ds-btn-text">Cancel</button>
  <span class="ds-tooltip-host">
    <button type="button" class="ds-btn ds-btn-primary" aria-disabled="true" aria-describedby="tip-continue">Continue</button>
    <span class="ds-tooltip ds-tooltip--end" id="tip-continue" role="tooltip">
      <span class="ds-tooltip-body">Correct the 2 blocking errors to continue.</span>
    </span>
  </span>
</div>

<!-- Disabled action, reason as help text -->
<div class="ds-btn-group ds-btn-group--end">
  <button type="button" class="ds-btn ds-btn-text">Cancel</button>
  <button type="button" class="ds-btn ds-btn-primary" aria-disabled="true" aria-describedby="continue-why">Continue</button>
</div>
<p class="ds-hint" id="continue-why">Correct the 2 blocking errors to continue.</p>
```

- `.ds-tooltip-host` — Wraps the trigger and the bubble, and positions the bubble. It sits beside the `<label>`, never inside it: a label forwards clicks to the control it names, so a button nested in one is a button whose clicks land somewhere else.
- `.ds-label-row` — Puts a label and its tooltip trigger on one line, in place of the label's own spacing. The icon trigger inside it is compact and still clears the 24px target.
- `aria-describedby="tip-doi"` — On the trigger, naming the tooltip's `id`. The tooltip describes the control and is never its accessible name: a name that only appears on hover is a name most people never get, so an icon trigger has an `.is-sr-only` label of its own, as above.
- `aria-disabled="true"` — On an unavailable action that explains itself. The reason goes in a tooltip by default, because it takes no room and does not move the layout. Where there is room, it can sit under the actions as `.ds-hint` text instead, named in the button's `aria-describedby`. Use `aria-disabled`, not `disabled`: a disabled button cannot take focus, so a keyboard user would never reach the reason. The script must ignore clicks while it is set.
- `.ds-tooltip` — The bubble, with `role="tooltip"` and the `id`. It opens downward and toward the inline end, on hover and on focus, with no JavaScript. Escape must close it without moving focus, which CSS cannot do: a listener sets `hidden` on it, and clears it when the pointer or focus arrives again. The script on this page is the reference.
- `.ds-tooltip-body` — The text. Short, and never content that exists nowhere else.
- `.ds-tooltip--end` — For a host near the trailing edge of its container, like the Continue button above: the bubble runs back toward the start instead of off screen. Both directions use logical properties, so both are correct in a right-to-left script.

> Not for anything required: if the reader must have it to fill the field in, it is help text under the control, not a tooltip, which is for the person who stops and wonders.

## Field width  (Modifiers)

Default field widths are set to follow the expected amount of content and are an important clue for users as to what is expected in any given field. Widths will generally not need any manual adjustment but two overrides exist just in case: `.ds-field--short` and `.ds-field--full`.

```html
<form class="ds-form">
  <div class="ds-field ds-field--short">
    <label class="ds-label" for="w-year">Year</label>
    <input class="ds-input" id="w-year" type="text" inputmode="numeric" value="2026">
  </div>
  <div class="ds-field">
    <label class="ds-label" for="w-date">Date</label>
    <input class="ds-input" id="w-date" type="date" value="2026-09-23">
  </div>
  <div class="ds-field ds-field--full">
    <label class="ds-label" for="w-title">Title</label>
    <input class="ds-input" id="w-title" type="text" value="Heavy-tailed gradients in deep networks: a study of convergence under stochastic optimisation">
  </div>
</form>
```

- `.ds-field--short` — Caps the field at 11rem, for a code, an identifier or a year.
- `.ds-field--full` — Releases the cap, for something that genuinely wants the whole measure.
- `.ds-field--sm, .ds-field--md, .ds-field--lg` — Internal tools only, in `internal-tools.css`: caps the control at 240px, 360px or 480px. Internal screens are dense enough to need field widths chosen rather than inferred, so on an internal form a person picks the size instead of the input `type` picking it. Use the pair above on public pages and this trio on internal pages, and do not mix them on one form.

## Rules

- **Labels go above the control.** A label-left, field-right layout gives a ragged edge and reads badly on a phone.
- **Group related content with spacing**, not by adding more bordered divs. If spacing is insufficient then the form might be calling for subsections or to be broken up into different pages.
- **The action bar is right-aligned**, with the primary action button (Save, Continue, etc.) the last one on the right. On long forms, consider repeating it at the top so the user does not need to scroll as much.
- **Disabled, not missing.** An action that is unavailable renders disabled, with the reason in a tooltip, or as help text under the actions where there is room (see [Tooltip](#tooltip)). The reader can see it exists and is not left wondering what is happening.
- **Every control has a label.** Put a real `<label for>` on every control, pointing at the control's `id`. Hide it with `.is-sr-only` when there is no room for it; do not leave it out.
- **Mark the optional fields, not the required ones.** Put `(optional)` inside the visible label of an optional field. Put `required` and `aria-required="true"` on every required control: required fields have no visual marker, so this pair is the only signal a screen reader gets. Never put either word in `aria-label` or `title`.
- **Connect every hint and message to its control.** Give each `.ds-hint` and each message an `id`, and list them in the control's `aria-describedby`. Without that a screen reader announces the field and nothing else.
- **Use `aria-invalid` for errors only.** Set `aria-invalid="true"` on a control in the error tier and remove it when the error clears. A warning is not invalid, and an info message is not a problem at all.
- **Say the tier in words.** Colour and a border are never the only signal (WCAG 1.4.1). The message says what is wrong or what changed, or includes a visually hidden “Error:” or “Warning:” prefix.
- **Validate on submit, then move focus.** Do not tell someone they are wrong while they are still typing. Once a field is invalid, re-check it on every `input` event so the error clears the moment it is fixed. When submission fails, move focus to the first invalid field.
- **Give the summary its role.** The alert above the form takes `role="alert"` for errors and warnings, so a screen reader announces it at once, and every row in it links to its field.
- **Prefer `aria-disabled` to `disabled` for a control that could explain itself.** `disabled` leaves the tab order entirely, so a user who cannot proceed finds nothing there and no reason why. The two must look identical.
