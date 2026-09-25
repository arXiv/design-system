---
page: alerts.html
title: "Alerts"
summary: "Alerts are a critical component of successful user journeys. They go hand in hand with [form validation](forms.html) but have many uses beyond forms as well. Alerts are always related to the content of the page they are on. For general announcements, see [messages](messages.html)."
stylesheet: design-system.css
components:
  - id: the-four-states
    title: "The four alert states"
    summary: "arXiv's design system contains four alerts that align with user expectations and established UI practices. Each state conveys a tone through color: **Success** uses green to signal that all is well, **info** is a calm blue, **warning** is an attention-grabbing yellow, while **error** is a powerful red and is reserved for blocking or failed states. Color sets the tone; the icon and the title carry the meaning, so a reader who cannot see the color still knows what kind of message it is."
    classes:
      - name: ".ds-alert"
        does: "The container. Always used with one of the four state classes, never alone. Takes `role=\"status\"` for success and info, `role=\"alert\"` for warning and error."
      - name: ".ds-alert--success, -info, -warning, -error"
        does: "The state: `.ds-alert--success`, `.ds-alert--warning`, or `.ds-alert--error`. Sets the background, border, and text colour from the status tokens. The same four classes and the same colours on both surfaces."
      - name: ".ds-alert-icon"
        does: "The icon, an inline SVG with `aria-hidden=\"true\"`. Each state has its own shape: a check, an “i”, a triangle, an “x”. Copy the icon element whole, attributes included: Lucide draws each “!” or “i” dot as a 0.01-unit path that only renders with `stroke-linecap=\"round\"`. Without these attributes it renders as an empty hairline outline."
      - name: ".ds-alert-content"
        does: "Holds the text. One or more `<p>` elements; a link inside it takes the alert’s own colour."
      - name: ".ds-alert-title"
        does: "The leading line, in bold. It names the situation, and it is what carries the meaning for a reader who cannot see the icon or the colour. Optional on a one-line alert."
    rules:
      - "Preferences saved: You will get a weekly digest of new papers in your selected categories."
      - "Submission limits added: Due to increased volume, arXiv is limiting submissions to 2 per month."
      - "You are viewing version 1: A newer version is available — [version 3, revised 24 Apr 2026](#)."
      - "Could not load the PDF: The file failed to render. [Try the HTML version](#) instead."
  - id: single-line
    title: "Single line"
    group: "Modifiers"
    summary: "Some messages are meant to be short and do not need lead-in text. Alerts can also be just a single line."
    classes:
      - name: ".ds-alert-content"
        does: "One `<p>` and no `.ds-alert-title`. The sentence itself has to name the state, because there is no title to do it."
    rules:
      - "Link copied to clipboard."
  - id: dismissible
    title: "Dismissible"
    group: "Modifiers"
    summary: "The dismiss control, fully documented on [Buttons](buttons.html#the-close-control), should be used for non-essential messages that the user can ignore without impeding progress. Critical form errors should never be dismissible."
    classes:
      - name: ".ds-close"
        does: "The dismiss control, documented on [Buttons](buttons.html#the-close-control). Put it last inside `.ds-alert`; the alert pushes it to the end of the row and it takes the alert’s colour. Removing the alert from the page is the host’s job: the stylesheet gives the control no behaviour."
      - name: ".is-sr-only"
        does: "Required inside the control. The icon is `aria-hidden`, so without this span the button announces as “button” and nothing more."
    rules:
      - "Choosing the wrong category may delay announcement."
rules:
  - "**Title:** Announce the situation in a few words, for example “No files found”."
  - "**Body:** What the user should do about it, for example “Check the contents of the tarball or zip.”"
  - "**Links help:** When available, offer links inside the body that take the user to the next step."
  - "**Focus on action:** Stay focused on what the user needs to do, do not explain what went wrong internally. “Enter a complete email address” is better than “Validation failed”."
  - "**arXiv’s voice:** Plain, jargon-free, contraction-free, and we never blame the user. “The file failed to render” is better than “You uploaded a bad file”."
  - "**One row when possible:** Shorter is better. Alerts should not crowd out the content they are supporting."
  - "**Choose the role by state.** Put `role=\"status\"` on a success or info alert: it is polite, and a screen reader announces it when idle. Put `role=\"alert\"` on a warning or error alert: it is assertive, and a screen reader announces it immediately. Do not use `role=\"alert\"` for anything that can wait."
  - "**Say the state in words.** The icon is `aria-hidden=\"true\"` and the colour is invisible to a screen reader, so the title or the first words of the message must carry the meaning: “Could not load the PDF”, not “Oops”."
  - "**Copy the icon whole.** Each state has its own icon shape, and the shape is part of the meaning. Copy the `<svg>` element with every attribute it carries: the “i” and “!” dots are drawn as tiny paths that only render with `stroke-linecap=\"round\"`, and without it the icon is an empty outline."
  - "**Name the dismiss control.** The `.ds-close` button needs a `<span class=\"is-sr-only\">` that says what it dismisses, such as “Dismiss this message”. Do not use `title` or `aria-label` for this, because page translation tools skip attributes."
  - "**Put focus somewhere after a dismiss.** Removing the alert removes the focused button with it. Move focus to the element just before where the alert was, so a keyboard user is not dropped back to the top of the page."
---

# Alerts

Alerts are a critical component of successful user journeys. They go hand in hand with [form validation](forms.html) but have many uses beyond forms as well. Alerts are always related to the content of the page they are on. For general announcements, see [messages](messages.html).

Load `design-system.css`; internal tools also load `internal/internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The four alert states

arXiv's design system contains four alerts that align with user expectations and established UI practices. Each state conveys a tone through color: **Success** uses green to signal that all is well, **info** is a calm blue, **warning** is an attention-grabbing yellow, while **error** is a powerful red and is reserved for blocking or failed states. Color sets the tone; the icon and the title carry the meaning, so a reader who cannot see the color still knows what kind of message it is.

```html
<div class="ds-alert ds-alert--warning" role="alert">
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

- `.ds-alert` — The container. Always used with one of the four state classes, never alone. Takes `role="status"` for success and info, `role="alert"` for warning and error.
- `.ds-alert--success, -info, -warning, -error` — The state: `.ds-alert--success`, `.ds-alert--warning`, or `.ds-alert--error`. Sets the background, border, and text colour from the status tokens. The same four classes and the same colours on both surfaces.
- `.ds-alert-icon` — The icon, an inline SVG with `aria-hidden="true"`. Each state has its own shape: a check, an “i”, a triangle, an “x”. Copy the icon element whole, attributes included: Lucide draws each “!” or “i” dot as a 0.01-unit path that only renders with `stroke-linecap="round"`. Without these attributes it renders as an empty hairline outline.
- `.ds-alert-content` — Holds the text. One or more `<p>` elements; a link inside it takes the alert’s own colour.
- `.ds-alert-title` — The leading line, in bold. It names the situation, and it is what carries the meaning for a reader who cannot see the icon or the colour. Optional on a one-line alert.

**Rule.** Preferences saved: You will get a weekly digest of new papers in your selected categories.

**Rule.** Submission limits added: Due to increased volume, arXiv is limiting submissions to 2 per month.

**Rule.** You are viewing version 1: A newer version is available — [version 3, revised 24 Apr 2026](#).

**Rule.** Could not load the PDF: The file failed to render. [Try the HTML version](#) instead.

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

**Rule.** Link copied to clipboard.

## Dismissible  (Modifiers)

The dismiss control, fully documented on [Buttons](buttons.html#the-close-control), should be used for non-essential messages that the user can ignore without impeding progress. Critical form errors should never be dismissible.

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

- `.ds-close` — The dismiss control, documented on [Buttons](buttons.html#the-close-control). Put it last inside `.ds-alert`; the alert pushes it to the end of the row and it takes the alert’s colour. Removing the alert from the page is the host’s job: the stylesheet gives the control no behaviour.
- `.is-sr-only` — Required inside the control. The icon is `aria-hidden`, so without this span the button announces as “button” and nothing more.

**Rule.** Choosing the wrong category may delay announcement.

## Rules

- **Title:** Announce the situation in a few words, for example “No files found”.
- **Body:** What the user should do about it, for example “Check the contents of the tarball or zip.”
- **Links help:** When available, offer links inside the body that take the user to the next step.
- **Focus on action:** Stay focused on what the user needs to do, do not explain what went wrong internally. “Enter a complete email address” is better than “Validation failed”.
- **arXiv’s voice:** Plain, jargon-free, contraction-free, and we never blame the user. “The file failed to render” is better than “You uploaded a bad file”.
- **One row when possible:** Shorter is better. Alerts should not crowd out the content they are supporting.
- **Choose the role by state.** Put `role="status"` on a success or info alert: it is polite, and a screen reader announces it when idle. Put `role="alert"` on a warning or error alert: it is assertive, and a screen reader announces it immediately. Do not use `role="alert"` for anything that can wait.
- **Say the state in words.** The icon is `aria-hidden="true"` and the colour is invisible to a screen reader, so the title or the first words of the message must carry the meaning: “Could not load the PDF”, not “Oops”.
- **Copy the icon whole.** Each state has its own icon shape, and the shape is part of the meaning. Copy the `<svg>` element with every attribute it carries: the “i” and “!” dots are drawn as tiny paths that only render with `stroke-linecap="round"`, and without it the icon is an empty outline.
- **Name the dismiss control.** The `.ds-close` button needs a `<span class="is-sr-only">` that says what it dismisses, such as “Dismiss this message”. Do not use `title` or `aria-label` for this, because page translation tools skip attributes.
- **Put focus somewhere after a dismiss.** Removing the alert removes the focused button with it. Move focus to the element just before where the alert was, so a keyboard user is not dropped back to the top of the page.
