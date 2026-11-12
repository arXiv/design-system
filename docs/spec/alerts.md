---
page: alerts.html
title: "Alerts"
summary: "Alerts are a critical component of successful user journeys. They go hand in hand with [form validation](forms.md) but have many uses beyond forms as well. Alerts are always related to the content of the page they are on. For general announcements, see [messages](messages.md)."
stylesheet: design-system.css
components:
  - id: the-four-states
    title: "The four alert states"
    summary: "arXiv's design system contains four alerts that align with user expectations and established UI practices. Each state conveys a tone through color: **Success** uses green to signal that all is well, **info** is a calm blue, **warning** is an attention-grabbing yellow, while **error** is a powerful red and is reserved for blocking or failed states, and for a paper that has been withdrawn or removed. Color sets the tone; the icon and the title convey the meaning, so a reader who cannot see the color still knows what kind of message it is."
    classes:
      - name: ".ds-alert"
        does: "The container. On its own it is the info state; add a state class for success, warning or error. An alert that appears after the page has loaded takes `role=\"status\"` for success and info, `role=\"alert\"` for warning and error. An alert that is in the page as it loads, such as the warning above, takes no role, and neither does one that focus moves to, such as a [form's error summary](forms.md#alerts-in-forms): focus already makes it heard."
      - name: ".ds-alert--success, --warning, --error"
        does: "The state: `.ds-alert--success`, `.ds-alert--warning`, or `.ds-alert--error`. Sets the background, border, and text colour from the status tokens. There is no info class: info is the container's own colours. The same classes and the same colours on both surfaces."
      - name: ".ds-alert-icon"
        does: "The icon, an inline SVG with `aria-hidden=\"true\"`. Each state has its own shape: a check, an “i”, a triangle, an octagon with a “!”; an “x” would read as a close control. Copy the icon element whole, attributes included: Lucide draws each “!” or “i” dot as a 0.01-unit path that only renders with `stroke-linecap=\"round\"`. Without these attributes it renders as an empty hairline outline."
      - name: ".ds-alert-content"
        does: "Holds the text. One or more `<p>` elements; a link inside it takes the alert’s own colour."
      - name: ".ds-alert-title"
        does: "The leading line, in bold. It names the situation, and it is what conveys the meaning for a reader who cannot see the icon or the colour. Optional on a one-line alert. On a notice that changes how the whole page is read, such as a [withdrawn paper's](papers.md#withdrawn-papers), it is a heading one level below the page heading, and keeps the alert's size and colour."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A), [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA), and [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)"
  - id: single-line
    title: "Single line"
    group: "Modifiers"
    summary: "Some messages are meant to be short and do not need lead-in text. Alerts can also be just a single line."
    classes:
      - name: ".ds-alert-content"
        does: "One `<p>` and no `.ds-alert-title`. The sentence itself has to name the state, because there is no title to do it."
  - id: dismissible
    title: "Dismissible"
    group: "Modifiers"
    summary: "The dismiss control, fully documented on [Buttons](buttons.md#the-close-control), should be used for non-essential messages that the user can ignore without impeding progress. Critical form errors should never be dismissible."
    classes:
      - name: ".ds-close"
        does: "The dismiss control, documented on [Buttons](buttons.md#the-close-control). Put it last inside `.ds-alert`; the alert pushes it to the end of the row and it takes the alert’s colour. Removing the alert from the page is the host’s job: the stylesheet gives the control no behaviour."
      - name: ".is-sr-only"
        does: "Required inside the control. The icon is `aria-hidden`, so without this span the button announces as “button” and nothing more."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A) and [WCAG 2.2 SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) Target Size (Minimum) (Level AA)"
rules:
  - "The default position is at the top of the main content area, below the page title."
  - "When possible, place alerts close to the content they refer to. This reduces cognitive load on our users."
  - "Alerts live in the main content area, not tucked away in a sidebar."
  - "We cannot expect a user to scroll up or down to catch a timely message. It either needs to appear in the area where they are working, or the page needs to scroll them to the area where the message appears."
  - "**Mark what needs attention where it is.** When some items in a set need attention, put a [status tag](tags.md) on each card or row, not an alert that lists the items, which the reader then has to find."
  - "**Title:** Announce the situation in a few words, for example “No files found”."
  - "**Body:** What the user should do about it, for example “Check the contents of the tarball or zip.”"
  - "**Links help:** When available, offer links inside the body that take the user to the next step."
  - "**Focus on action:** Stay focused on what the user needs to do, do not explain what went wrong internally. “Enter a complete email address” is better than “Validation failed”."
  - "**arXiv’s voice:** Plain, jargon-free, contraction-free, and we never blame the user. “The file failed to render” is better than “You uploaded a bad file”."
  - "**One row when possible:** Shorter is better. Alerts should not crowd out the content they are supporting."
  - "**Choose the role by state.** Put `role=\"status\"` on a success or info alert: it is polite, and a screen reader announces it when idle. Put `role=\"alert\"` on a warning or error alert: it is assertive, and a screen reader announces it immediately. Do not use `role=\"alert\"` for anything that can wait."
  - "**No role on an alert that is in the page as it loads, or that focus moves to.** A role announces a change, and a screen reader does not reliably announce an alert that was there from the start, such as the warning on an older version of a paper. Put that alert where the reader meets it early, straight after the page heading. An alert that focus moves to, such as a [form's error summary](forms.md#alerts-in-forms), needs no role either: focus already makes it heard."
  - "**Announce the result of an action.** Copy, Permalink and the theme control change nothing a reader can see: see [Show that something was copied](action-feedback.md)."
  - "**Say the state in words.** The icon is `aria-hidden=\"true\"` and the colour is invisible to a screen reader, so the title or the first words of the message must convey the meaning: “Could not load the PDF”, not “Oops”."
  - "**Copy the icon whole.** Each state has its own icon shape, and the shape is part of the meaning. Copy the `<svg>` element with every attribute it has: the “i” and “!” dots are drawn as tiny paths that only render with `stroke-linecap=\"round\"`, and without it the icon is an empty outline."
  - "**Name the dismiss control.** The `.ds-close` button needs a `<span class=\"is-sr-only\">` that says what it dismisses, such as “Dismiss this message”. Do not use `title` or `aria-label` for this, because page translation tools skip attributes."
  - "**Put focus somewhere after a dismiss.** Removing the alert removes the focused button with it. Move focus to the element just before where the alert was, so a keyboard user is not dropped back to the top of the page."
---

# Alerts

Alerts are a critical component of successful user journeys. They go hand in hand with [form validation](forms.md) but have many uses beyond forms as well. Alerts are always related to the content of the page they are on. For general announcements, see [messages](messages.md).

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The four alert states

arXiv's design system contains four alerts that align with user expectations and established UI practices. Each state conveys a tone through color: **Success** uses green to signal that all is well, **info** is a calm blue, **warning** is an attention-grabbing yellow, while **error** is a powerful red and is reserved for blocking or failed states, and for a paper that has been withdrawn or removed. Color sets the tone; the icon and the title convey the meaning, so a reader who cannot see the color still knows what kind of message it is.

```html
<div class="ds-alert ds-alert--warning">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2"
       stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <!-- Lucide icon paths -->
  </svg>
  <div class="ds-alert-content">
    <p class="ds-alert-title">You are viewing version 1</p>
    <p>A newer version is available — <a href="…">version 3</a>.</p>
  </div>
</div>
```

- `.ds-alert` — The container. On its own it is the info state; add a state class for success, warning or error. An alert that appears after the page has loaded takes `role="status"` for success and info, `role="alert"` for warning and error. An alert that is in the page as it loads, such as the warning above, takes no role, and neither does one that focus moves to, such as a [form's error summary](forms.md#alerts-in-forms): focus already makes it heard.
- `.ds-alert--success, --warning, --error` — The state: `.ds-alert--success`, `.ds-alert--warning`, or `.ds-alert--error`. Sets the background, border, and text colour from the status tokens. There is no info class: info is the container's own colours. The same classes and the same colours on both surfaces.
- `.ds-alert-icon` — The icon, an inline SVG with `aria-hidden="true"`. Each state has its own shape: a check, an “i”, a triangle, an octagon with a “!”; an “x” would read as a close control. Copy the icon element whole, attributes included: Lucide draws each “!” or “i” dot as a 0.01-unit path that only renders with `stroke-linecap="round"`. Without these attributes it renders as an empty hairline outline.
- `.ds-alert-content` — Holds the text. One or more `<p>` elements; a link inside it takes the alert’s own colour.
- `.ds-alert-title` — The leading line, in bold. It names the situation, and it is what conveys the meaning for a reader who cannot see the icon or the colour. Optional on a one-line alert. On a notice that changes how the whole page is read, such as a [withdrawn paper's](papers.md#withdrawn-papers), it is a heading one level below the page heading, and keeps the alert's size and colour.

> Meets accessibility guidelines [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A), [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA), and [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)

## Single line  (Modifiers)

Some messages are meant to be short and do not need lead-in text. Alerts can also be just a single line.

```html
<div class="ds-alert ds-alert--success" role="status">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <circle cx="12" cy="12" r="10"/>
    <path d="m9 12 2 2 4-4"/>
  </svg>
  <div class="ds-alert-content">
    <p>Link copied to clipboard.</p>
  </div>
</div>
```

- `.ds-alert-content` — One `<p>` and no `.ds-alert-title`. The sentence itself has to name the state, because there is no title to do it.

## Dismissible  (Modifiers)

The dismiss control, fully documented on [Buttons](buttons.md#the-close-control), should be used for non-essential messages that the user can ignore without impeding progress. Critical form errors should never be dismissible.

```html
<div class="ds-alert" role="status">
  <svg class="ds-alert-icon" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <circle cx="12" cy="12" r="10"/>
    <path d="M12 16v-4"/>
    <path d="M12 8h.01"/>
  </svg>
  <div class="ds-alert-content">
    <p>Choosing the wrong category may delay announcement.</p>
  </div>
  <button type="button" class="ds-close">
    <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M18 6 6 18"/>
      <path d="m6 6 12 12"/>
    </svg>
    <span class="is-sr-only">Dismiss this message</span>
  </button>
</div>
```

- `.ds-close` — The dismiss control, documented on [Buttons](buttons.md#the-close-control). Put it last inside `.ds-alert`; the alert pushes it to the end of the row and it takes the alert’s colour. Removing the alert from the page is the host’s job: the stylesheet gives the control no behaviour.
- `.is-sr-only` — Required inside the control. The icon is `aria-hidden`, so without this span the button announces as “button” and nothing more.

> Meets accessibility guidelines [WCAG 2.2 SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) Name, Role, Value (Level A) and [WCAG 2.2 SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) Target Size (Minimum) (Level AA)

## Rules

### Placement

The default position is at the top of the main content area, below the page title.

When possible, place alerts close to the content they refer to. This reduces cognitive load on our users.

Alerts live in the main content area, not tucked away in a sidebar.

We cannot expect a user to scroll up or down to catch a timely message. It either needs to appear in the area where they are working, or the page needs to scroll them to the area where the message appears.

- **Mark what needs attention where it is.** When some items in a set need attention, put a [status tag](tags.md) on each card or row, not an alert that lists the items, which the reader then has to find.

### Writing the message

- **Title:** Announce the situation in a few words, for example “No files found”.
- **Body:** What the user should do about it, for example “Check the contents of the tarball or zip.”
- **Links help:** When available, offer links inside the body that take the user to the next step.
- **Focus on action:** Stay focused on what the user needs to do, do not explain what went wrong internally. “Enter a complete email address” is better than “Validation failed”.
- **arXiv’s voice:** Plain, jargon-free, contraction-free, and we never blame the user. “The file failed to render” is better than “You uploaded a bad file”.
- **One row when possible:** Shorter is better. Alerts should not crowd out the content they are supporting.

### Accessibility essentials

- **Choose the role by state.** Put `role="status"` on a success or info alert: it is polite, and a screen reader announces it when idle. Put `role="alert"` on a warning or error alert: it is assertive, and a screen reader announces it immediately. Do not use `role="alert"` for anything that can wait.
- **No role on an alert that is in the page as it loads, or that focus moves to.** A role announces a change, and a screen reader does not reliably announce an alert that was there from the start, such as the warning on an older version of a paper. Put that alert where the reader meets it early, straight after the page heading. An alert that focus moves to, such as a [form's error summary](forms.md#alerts-in-forms), needs no role either: focus already makes it heard.
- **Announce the result of an action.** Copy, Permalink and the theme control change nothing a reader can see: see [Show that something was copied](action-feedback.md).
- **Say the state in words.** The icon is `aria-hidden="true"` and the colour is invisible to a screen reader, so the title or the first words of the message must convey the meaning: “Could not load the PDF”, not “Oops”.
- **Copy the icon whole.** Each state has its own icon shape, and the shape is part of the meaning. Copy the `<svg>` element with every attribute it has: the “i” and “!” dots are drawn as tiny paths that only render with `stroke-linecap="round"`, and without it the icon is an empty outline.
- **Name the dismiss control.** The `.ds-close` button needs a `<span class="is-sr-only">` that says what it dismisses, such as “Dismiss this message”. Do not use `title` or `aria-label` for this, because page translation tools skip attributes.
- **Put focus somewhere after a dismiss.** Removing the alert removes the focused button with it. Move focus to the element just before where the alert was, so a keyboard user is not dropped back to the top of the page.
