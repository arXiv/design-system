---
page: dark-mode.html
title: "Dark mode"
summary: "In the design system, every colour comes from a token and the tokens flip in each mode. A page or component built from the color tokens follows the mode without any additional work and no hand-picking of values."
stylesheet: design-system.css
components:
  - id: the-theme-control
    title: "The theme control"
    summary: "One control that is identical everywhere it appears. It ships as `.ds-theme-toggle` plus `theme.js`."
    classes:
      - name: "<script src=\"theme.js\">"
        does: "Goes in the head, and it is not deferred; that is load-bearing. The attribute has to be on `<html>` before the first paint or the page renders light and then flips — worst for exactly the reader who chose dark because light hurts. `check-policies.py` fails on a page that defers it. It also puts the class `js` on `<html>`, so the stylesheet can draw scripted states from the first paint, such as a closed Show more tail."
      - name: ".ds-theme-toggle"
        does: "The control. Three states, not two: follow the system, always light, always dark — and *follow the system* is the default a reader has to be able to get back to. A two-way switch cannot express it, so the first touch would lose the machine's setting for good. That is also why it is a `<button>` cycling a value rather than [the switch](forms.md), which means on or off. Leave the element empty: the script fills in the icon, the accessible name and the state as hidden text. Until it does, the stylesheet hides the button, so without JavaScript there is no empty control in the tab order. In the header bar it follows the navigation and comes before the account area, as on [the header unit](header.md#the-header-unit); it is one button, and the three states are never shown side by side. When a public header folds on a phone, it is a row in the menu, and the hidden text shows beside the icon: “Theme: following the system”."
      - name: "id=\"ds-theme-status\""
        does: "The live region the result goes to: “Theme is now dark”. The button's name says which state is on, “Theme: dark. Activate to change.”, because the icon is the only visible part; the live region says what a press did, because a changed name is not reliably read out."
    notes:
      - "The three cards show the icon for each state; the bar below them is the control itself, in the header, and one control cycles through the three. It is live, and so is the one at the top of this page."
  - id: a-component-that-follows-the-tokens
    title: "Example: a card component in light and dark modes"
    summary: "The same card on a public page and in an internal tool. Nothing in its markup changes except `.ds-internal` on the parent, for internal tools. To see it in the other mode, change the theme with the control in the header: the whole page changes, and the cards with it."
    classes:
      - name: ".ds-internal"
        does: "Internal tools. Re-points the accent to Access Lime, from tier 1, and composes with the theme: lime holds its light value in dark, the wash goes to a dark olive, and text that sat on the wash turns lime to stay legible. An internal page puts it on `<html>`."
    notes:
      - "Accents hold in both modes: Open Blue and Access Lime stay themselves, which is why the text on them is a fixed token too."
  - id: a-page-locked-to-light
    title: "Locking to light"
    group: "Modifiers"
    summary: "A page locks to light mode by adding `data-theme=\"light\"` to its `<html>`. Use it only when the page's content has no dark mode, such as complex visualizations from an external engine that cannot follow the theme. The theme belongs to the whole page: a part of a page cannot lock."
  - id: internal-tools
    title: "Internal tools need no modifier"
    group: "Modifiers"
    summary: "Internal tools load the same tier 1 stylesheet as public pages. Their speciall accent color comes from adding `.ds-internal` on `<html>`, so everything above applies to them unchanged. The internal pages tier 2 stylesheet, `internal-tools.css`, re-points only the tokens whose dark value differs on that surface. No manual adjustments are needed."
rules:
  - "In order. Each step links to the reasoning below. If you follow only this list and read nothing else, dark mode will work."
  - "**Take every colour from a token.** Never write a dark hex into a page or a component. Components that consume tokens flip for free. [How it works](#the-mechanism)"
  - "**Decide whether the colour is content or identity.** Content flips. Identity is pinned to a literal with a comment saying why — a masthead, a brand fill, a colour specimen whose subject is the value itself."
  - "**Fill raised things with `--ds-surface`.** Not `--ds-canvas`: the page ground is white in light and Repository Brown in dark, so anything filled with it disappears."
  - "**Check any text sitting on an accent fill.** Accents hold their light values in dark, so the text on them must not flip either — `--ds-text-on-accent` on lime and on Open Blue alike. Reaching for the plain token puts near-white text on a light fill, about 1.3:1."
  - "**Set the page's own background and text from tokens.** An inherited colour from a platform preset or a third-party stylesheet cannot flip, and it will not announce itself."
  - "**Do not use `color-scheme` to force a mode.** It governs browser-rendered widgets only — scrollbars, form controls — and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme` on `<html>`. [Locking to light](#a-page-locked-to-light)"
  - "**The theme belongs to the whole page.** Set `data-theme` on `<html>` only: no part of a page is lighter or darker than the rest. To show both modes, use the theme control in the header. One case follows from another rule: a popover takes the ground of the row that opened it, so a popover from the dark site header opens in dark mode. `filter-panel.js` sets that; a page never does."
  - "**If anything can set `data-theme`, mirror the dark block under the attribute** as well as the media query — including inherited code you did not write. [How the attribute works](#the-mechanism)"
  - "**Verify computed styles in both modes, and measure contrast.** Do not trust the cascade and do not judge by eye. Check the states a reader can actually reach: OS dark, OS light, and the attribute forced either way."
  - "Component CSS consumes tokens. Do not write hex values directly."
  - "`color-scheme` does not lock a page to a mode. It governs browser-rendered widgets like scrollbars, form controls, and the default canvas. It does not touch a stylesheet's `prefers-color-scheme` rules. If absolutely needed, use `data-theme` on `<html>` to lock a mode."
  - "**Respect the setting the reader already made.** A page follows the operating system's colour scheme unless the reader says otherwise on the page itself. Without JavaScript there is no button and the page follows the OS: the control is an addition, never the only route to a readable page."
  - "**The icon is the only visible part, so the name gives the state.** The button's accessible name says which state is on (“Theme: following the system. Activate to change.”), and a press announces its result in the live region, as in [Show that something was copied](action-feedback.md). A sighted reader learns the three icons from the cards above; a screen reader user is told, and is never guessing whether the moon means “it is dark” or “make it dark”."
  - "**Never a dark value by hand.** Take every colour from a token and it flips with the rest of the page. A hex written into a page or a component cannot flip, and it will not announce itself."
  - "**Check contrast in both modes.** Verify computed styles and measure contrast in every state a reader can reach: OS dark, OS light, and the attribute forced either way. Do not trust the cascade and do not judge by eye. Anything that uses colour to convey meaning keeps its second cue (icon, word, position) in dark mode too — the WCAG 1.4.1 requirement applies in both modes."
  - "**Let form controls follow.** The stylesheet sets `color-scheme` beside the tokens, so native form controls, scrollbars and the default canvas take the same mode as the page. Do not set it yourself to force a mode: it governs those browser-rendered widgets only and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme`."
---

# Dark mode

In the design system, every colour comes from a token and the tokens flip in each mode. A page or component built from the color tokens follows the mode without any additional work and no hand-picking of values.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The theme control

One control that is identical everywhere it appears. It ships as `.ds-theme-toggle` plus `theme.js`.

Though we honor the user's OS-level mode preference, it is still useful for users to have a manual override. A person might be on a shared library computer, not everyone knows how to set the OS-level preference, and the environment can change quickly. Think of a user looking at a paper on their phone on a train, moving from tunnels to the glare of sunlight. A simple affordance makes papers more accessible in more situations.

```html
<!-- in the head, NOT deferred -->
<script src="theme.js"></script>

<!-- in the header bar, after the navigation -->
<div class="ds-site-header-tools">
  <button type="button" class="ds-theme-toggle"></button>
  <span id="ds-theme-status" class="is-sr-only" role="status"></span>
</div>
```

- `<script src="theme.js">` — Goes in the head, and it is not deferred; that is load-bearing. The attribute has to be on `<html>` before the first paint or the page renders light and then flips — worst for exactly the reader who chose dark because light hurts. `check-policies.py` fails on a page that defers it. It also puts the class `js` on `<html>`, so the stylesheet can draw scripted states from the first paint, such as a closed Show more tail.
- `.ds-theme-toggle` — The control. Three states, not two: follow the system, always light, always dark — and *follow the system* is the default a reader has to be able to get back to. A two-way switch cannot express it, so the first touch would lose the machine's setting for good. That is also why it is a `<button>` cycling a value rather than [the switch](forms.md), which means on or off. Leave the element empty: the script fills in the icon, the accessible name and the state as hidden text. Until it does, the stylesheet hides the button, so without JavaScript there is no empty control in the tab order. In the header bar it follows the navigation and comes before the account area, as on [the header unit](header.md#the-header-unit); it is one button, and the three states are never shown side by side. When a public header folds on a phone, it is a row in the menu, and the hidden text shows beside the icon: “Theme: following the system”.
- `id="ds-theme-status"` — The live region the result goes to: “Theme is now dark”. The button's name says which state is on, “Theme: dark. Activate to change.”, because the icon is the only visible part; the live region says what a press did, because a changed name is not reliably read out.

> The three cards show the icon for each state; the bar below them is the control itself, in the header, and one control cycles through the three. It is live, and so is the one at the top of this page.

## Example: a card component in light and dark modes

The same card on a public page and in an internal tool. Nothing in its markup changes except `.ds-internal` on the parent, for internal tools. To see it in the other mode, change the theme with the control in the header: the whole page changes, and the cards with it.

```html
<!-- The component: nothing in it knows which mode it is in -->
<div class="ds-card">
  <p>Body text on a raised surface, with <a href="…">an inline link</a>.</p>
  <div class="ds-alert ds-alert--success" role="status">…</div>
  <div class="ds-btn-group">
    <button class="ds-btn ds-btn-primary" type="button">Primary</button>
    <button class="ds-btn" type="button">Secondary</button>
  </div>
</div>

<!-- Internal tools: the accent comes from the class on a parent, the mode from the page -->
<html lang="en" class="ds-internal">
```

- `.ds-internal` — Internal tools. Re-points the accent to Access Lime, from tier 1, and composes with the theme: lime holds its light value in dark, the wash goes to a dark olive, and text that sat on the wash turns lime to stay legible. An internal page puts it on `<html>`.

> Accents hold in both modes: Open Blue and Access Lime stay themselves, which is why the text on them is a fixed token too.

## Locking to light  (Modifiers)

A page locks to light mode by adding `data-theme="light"` to its `<html>`. Use it only when the page's content has no dark mode, such as complex visualizations from an external engine that cannot follow the theme. The theme belongs to the whole page: a part of a page cannot lock.

```html
<html lang="en" data-theme="light">
```

## Internal tools need no modifier  (Modifiers)

Internal tools load the same tier 1 stylesheet as public pages. Their speciall accent color comes from adding `.ds-internal` on `<html>`, so everything above applies to them unchanged. The internal pages tier 2 stylesheet, `internal-tools.css`, re-points only the tokens whose dark value differs on that surface. No manual adjustments are needed.

## Rules

### Adding or changing a component

In order. Each step links to the reasoning below. If you follow only this list and read nothing else, dark mode will work.

- **Take every colour from a token.** Never write a dark hex into a page or a component. Components that consume tokens flip for free. [How it works](#the-mechanism)
- **Decide whether the colour is content or identity.** Content flips. Identity is pinned to a literal with a comment saying why — a masthead, a brand fill, a colour specimen whose subject is the value itself.
- **Fill raised things with `--ds-surface`.** Not `--ds-canvas`: the page ground is white in light and Repository Brown in dark, so anything filled with it disappears.
- **Check any text sitting on an accent fill.** Accents hold their light values in dark, so the text on them must not flip either — `--ds-text-on-accent` on lime and on Open Blue alike. Reaching for the plain token puts near-white text on a light fill, about 1.3:1.
- **Set the page's own background and text from tokens.** An inherited colour from a platform preset or a third-party stylesheet cannot flip, and it will not announce itself.
- **Do not use `color-scheme` to force a mode.** It governs browser-rendered widgets only — scrollbars, form controls — and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme` on `<html>`. [Locking to light](#a-page-locked-to-light)
- **The theme belongs to the whole page.** Set `data-theme` on `<html>` only: no part of a page is lighter or darker than the rest. To show both modes, use the theme control in the header. One case follows from another rule: a popover takes the ground of the row that opened it, so a popover from the dark site header opens in dark mode. `filter-panel.js` sets that; a page never does.
- **If anything can set `data-theme`, mirror the dark block under the attribute** as well as the media query — including inherited code you did not write. [How the attribute works](#the-mechanism)
- **Verify computed styles in both modes, and measure contrast.** Do not trust the cascade and do not judge by eye. Check the states a reader can actually reach: OS dark, OS light, and the attribute forced either way.

### Forcing a mode

- Component CSS consumes tokens. Do not write hex values directly.
- `color-scheme` does not lock a page to a mode. It governs browser-rendered widgets like scrollbars, form controls, and the default canvas. It does not touch a stylesheet's `prefers-color-scheme` rules. If absolutely needed, use `data-theme` on `<html>` to lock a mode.

### Accessibility essentials

- **Respect the setting the reader already made.** A page follows the operating system's colour scheme unless the reader says otherwise on the page itself. Without JavaScript there is no button and the page follows the OS: the control is an addition, never the only route to a readable page.
- **The icon is the only visible part, so the name gives the state.** The button's accessible name says which state is on (“Theme: following the system. Activate to change.”), and a press announces its result in the live region, as in [Show that something was copied](action-feedback.md). A sighted reader learns the three icons from the cards above; a screen reader user is told, and is never guessing whether the moon means “it is dark” or “make it dark”.
- **Never a dark value by hand.** Take every colour from a token and it flips with the rest of the page. A hex written into a page or a component cannot flip, and it will not announce itself.
- **Check contrast in both modes.** Verify computed styles and measure contrast in every state a reader can reach: OS dark, OS light, and the attribute forced either way. Do not trust the cascade and do not judge by eye. Anything that uses colour to convey meaning keeps its second cue (icon, word, position) in dark mode too — the WCAG 1.4.1 requirement applies in both modes.
- **Let form controls follow.** The stylesheet sets `color-scheme` beside the tokens, so native form controls, scrollbars and the default canvas take the same mode as the page. Do not set it yourself to force a mode: it governs those browser-rendered widgets only and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme`.

## Spec

### The mechanism

Dark values are declared twice in each stylesheet: once in a `@media screen and (prefers-color-scheme: dark)` block that follows the OS, and once under `:root[data-theme="dark"]` so the attribute can force a mode. Both are for screens only, so a page always prints light. A page takes one of three states:

```
<html data-theme="dark">    <!-- dark, whatever the OS says -->
<html data-theme="light">   <!-- light, whatever the OS says -->
<html>                      <!-- follows the OS -->
```

Only semantic tokens change between modes. Primitives such as Repository Brown keep their value; what changes is the role a token points them at.

### Color tokens

The table below is written from `design-system.css` by `verification/gen-theme-values.py`, and a check fails when it no longer matches the stylesheet. Do not edit it by hand.

| Token | Light | Dark | Between modes |
|---|---|---|---|
| `--ds-text` | `#1c1a17` | `#f0f0ee` | flips |
| `--ds-text-muted` | `#6b6459` | `#aeaaa4` | flips |
| `--ds-text-disabled` | `#aeaaa4` | `#5a554f` | flips |
| `--ds-text-on-accent` | `#1c1a17` | `#1c1a17` | holds |
| `--ds-canvas` | `#ffffff` | `#1c1a17` | flips |
| `--ds-surface` | `#ffffff` | `#1c1a17` | flips |
| `--ds-surface-hover` | `#f0f0ee` | `#282622` | flips |
| `--ds-tint-warm` | `#f0f0ee` | `#282622` | flips |
| `--ds-zone-secondary-bg` | `#f0f0ee` | `#282622` | flips |
| `--ds-chrome` | `#1c1a17` | `#262119` | flips |
| `--ds-border` | `#dad8d6` | `#383531` | flips |
| `--ds-border-strong` | `#89837a` | `#89837a` | holds |
| `--ds-accent` | `#a5d6fe` | `#a5d6fe` | holds |
| `--ds-accent-strong` | `#1f5e96` | `#6ba8da` | flips |
| `--ds-accent-wash` | `#d2eafe` | `#22344a` | flips |
| `--ds-accent-surface` | `#edf7ff` | `#202b38` | flips |
| `--ds-accent-border` | `#c0e2fe` | `#2a4a7a` | flips |
| `--ds-link` | `#1565c0` | `#64b5f6` | flips |
| `--ds-link-hover` | `#1050a0` | `#90caf9` | flips |
| `--ds-link-visited` | `#7b2fbe` | `#c690e3` | flips |
| `--ds-danger-fg` | `#c62828` | `#e57373` | flips |
| `--ds-success-bg` | `#e8f5d8` | `#1e2b0d` | flips |
| `--ds-success-border` | `#6b8e1e` | `#8fbd3a` | flips |
| `--ds-success-fg` | `#4a5a0a` | `#c5e1a5` | flips |
| `--ds-info-bg` | `#e7f1fd` | `#132433` | flips |
| `--ds-info-border` | `#5a82c8` | `#64b5f6` | flips |
| `--ds-info-fg` | `#1a3a78` | `#90caf9` | flips |
| `--ds-warning-bg` | `#fff8e1` | `#2e2410` | flips |
| `--ds-warning-border` | `#e8b800` | `#e8b800` | holds |
| `--ds-warning-fg` | `#7a5c00` | `#ffe082` | flips |
| `--ds-error-bg` | `#fdeaea` | `#2d1414` | flips |
| `--ds-error-border` | `#c62828` | `#e57373` | flips |
| `--ds-error-fg` | `#8b0000` | `#ef9a9a` | flips |
