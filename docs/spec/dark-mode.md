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
        does: "Goes in the head, and it is not deferred; that is load-bearing. The attribute has to be on `<html>` before the first paint or the page renders light and then flips — worst for exactly the reader who chose dark because light hurts. `check-policies.py` fails on a page that defers it."
      - name: ".ds-theme-toggle"
        does: "The control. Three states, not two: follow the system, always light, always dark — and *follow the system* is the default a reader has to be able to get back to. A two-way switch cannot express it, so the first touch would lose the machine's setting for good. That is also why it is a `<button>` cycling a value rather than [the switch](forms.html), which means on or off. Leave the element empty: the script fills in the icon and the accessible name. It is the last item in the header bar, one button; the three states are never shown side by side."
      - name: "id=\"ds-theme-status\""
        does: "The live region the result goes to. The button's name does not change when the theme does — the name of a control is what it does, and it is still the theme control; the live region says “Theme is now dark”. Same rule as the copy button and the switch."
    notes:
      - "The three cards show the icon for each state; the bar below them is the control itself, the last item in the header, and one control cycles through the three. It is live, and so is the one at the top of this page."
  - id: a-component-that-follows-the-tokens
    title: "Example: a card component in light and dark modes"
    summary: "The same card in light and dark modes, on a public page vs. an internal page. Nothing in its markup changes except the `data-theme` attribute and, for internal tools, `.ds-internal` is added to the parent element."
    classes:
      - name: "data-theme=\"dark\", data-theme=\"light\""
        does: "On any element, not only the root. The tokens are declared on any element carrying the attribute and custom properties inherit, so the *nearest* ancestor with `data-theme` wins, and nesting works in both directions: a dark sample inside a light panel inside a page following the OS renders correctly. The attribute re-points tokens and paints nothing itself. Anything inside that already reads tokens follows; the container has to take its own ground and text from tokens too, which here is `.ds-card` for the ground and `color: var(--ds-text)` for the text."
      - name: ".ds-internal"
        does: "Internal tools. Re-points the accent to Access Lime, from tier 1, and composes with the attribute: lime holds its light value in dark, the wash goes to a dark olive, and text that sat on the wash turns lime to stay legible. An internal page puts it on `<html>`."
    notes:
      - "Accents hold in both modes: Open Blue and Access Lime stay themselves, which is why the text on them is a fixed token too."
    rules:
      - "Preferences saved."
      - "Preferences saved."
      - "Preferences saved."
      - "Preferences saved."
  - id: a-page-locked-to-light
    title: "Locking to light"
    group: "Modifiers"
    summary: "Any page or element can lock to light mode only by adding `data-theme=\"light\"`. We use this feature when demonstrating light mode, but it can also be useful if the content being worked with has no dark mode. For example, if porting in complex visualizations from an external engine that does not support dark mode."
    classes:
      - name: "data-theme=\"light\" on <html>"
        does: "Locks the page to light and opts it out of the `@media` block. Check that nothing rewrites it: a static attribute in the markup is not a lock if a script on the page sets the attribute at load. `theme.js` does exactly that, so a page that carries the theme control cannot also be locked."
      - name: "data-theme=\"light\" on a container"
        does: "One demo shows light while the page follows the reader. The same scoping as the dark island above, in the other direction."
    notes:
      - "Test it with the theme control in the header: the page changes but this panel does not."
  - id: internal-tools
    title: "Internal tools need no modifier"
    group: "Modifiers"
    summary: "Internal tools load the same tier 1 stylesheet as public pages. Their speciall accent color comes from adding `.ds-internal` on `<html>`, so everything above applies to them unchanged. The internal pages tier 2 stylesheet, `internal-tools.css`, re-points only the tokens whose dark value differs on that surface. No manual adjustments are needed."
rules:
  - "**Take every colour from a token.** Never write a dark hex into a page or a component. Components that consume tokens flip for free. [How it works](#the-mechanism)"
  - "**Decide whether the colour is content or identity.** Content flips. Identity is pinned to a literal with a comment saying why — a masthead, a brand fill, a colour specimen whose subject is the value itself."
  - "**Fill raised things with `--ds-surface`.** Not `--ds-canvas`: the wash is a pale tint in light and *is* the canvas in dark, so anything filled with it disappears."
  - "**Check any text sitting on an accent fill.** Accents hold their light values in dark, so the text on them must not flip either — `--ds-text-on-accent` on lime and on Open Blue alike. Reaching for the plain token puts near-white text on a light fill, about 1.3:1."
  - "**Set the page's own background and text from tokens.** An inherited colour from a platform preset or a third-party stylesheet cannot flip, and it will not announce itself."
  - "**Do not use `color-scheme` to force a mode.** It governs browser-rendered widgets only — scrollbars, form controls — and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme`. [Scoping a mode](#scoping-a-mode)"
  - "**Scope a demo that must show one mode.** Put `data-theme` on the demo's own container, not on the page. Pages should follow the reader. [Scoping a mode](#scoping-a-mode)"
  - "**If anything can set `data-theme`, mirror the dark block under the attribute** as well as the media query — including inherited code you did not write. [How the attribute works](#the-mechanism)"
  - "**Verify computed styles in both modes, and measure contrast.** Do not trust the cascade and do not judge by eye. Check the states a reader can actually reach: OS dark, OS light, and the attribute forced either way."
  - "Component CSS consumes tokens. Do not write hex values directly."
  - "`color-scheme` does not lock a page to a mode. It governs browser-rendered widgets like scrollbars, form controls, and the default canvas. It does not touch a stylesheet's `prefers-color-scheme` rules. If absolutely needed, use `data-theme` to lock a mode."
  - "**Respect the setting the reader already made.** A page follows the operating system's colour scheme unless the reader says otherwise on the page itself. Without JavaScript there is no button and the page follows the OS: the control is an addition, never the only route to a readable page."
  - "**The icon is the only visible part, so the name carries the state.** The button's accessible name says which state is on (“Theme: following the system. Activate to change.”), and a press announces its result in the live region. A sighted reader learns the three icons from the cards above; a screen reader user is told, and is never guessing whether the moon means “it is dark” or “make it dark”."
  - "**Never a dark value by hand.** Take every colour from a token and it flips with the rest of the page. A hex written into a page or a component cannot flip, and it will not announce itself."
  - "**Check contrast in both modes.** Verify computed styles and measure contrast in every state a reader can reach: OS dark, OS light, and the attribute forced either way. Do not trust the cascade and do not judge by eye. Anything that uses colour to carry meaning keeps its second cue (icon, word, position) in dark mode too — the WCAG 1.4.1 requirement applies in both modes."
  - "**Let form controls follow.** The stylesheet sets `color-scheme` beside the tokens, so native form controls, scrollbars and the default canvas take the same mode as the page. Do not set it yourself to force a mode: it governs those browser-rendered widgets only and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme`."
---

# Dark mode

In the design system, every colour comes from a token and the tokens flip in each mode. A page or component built from the color tokens follows the mode without any additional work and no hand-picking of values.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The theme control

One control that is identical everywhere it appears. It ships as `.ds-theme-toggle` plus `theme.js`.

```html
<!-- in the head, NOT deferred -->
<script src="theme.js"></script>

<!-- in the header bar -->
<button type="button" class="ds-theme-toggle"></button>
<span id="ds-theme-status" class="is-sr-only" role="status"></span>
```

- `<script src="theme.js">` — Goes in the head, and it is not deferred; that is load-bearing. The attribute has to be on `<html>` before the first paint or the page renders light and then flips — worst for exactly the reader who chose dark because light hurts. `check-policies.py` fails on a page that defers it.
- `.ds-theme-toggle` — The control. Three states, not two: follow the system, always light, always dark — and *follow the system* is the default a reader has to be able to get back to. A two-way switch cannot express it, so the first touch would lose the machine's setting for good. That is also why it is a `<button>` cycling a value rather than [the switch](forms.html), which means on or off. Leave the element empty: the script fills in the icon and the accessible name. It is the last item in the header bar, one button; the three states are never shown side by side.
- `id="ds-theme-status"` — The live region the result goes to. The button's name does not change when the theme does — the name of a control is what it does, and it is still the theme control; the live region says “Theme is now dark”. Same rule as the copy button and the switch.

> The three cards show the icon for each state; the bar below them is the control itself, the last item in the header, and one control cycles through the three. It is live, and so is the one at the top of this page.

## Example: a card component in light and dark modes

The same card in light and dark modes, on a public page vs. an internal page. Nothing in its markup changes except the `data-theme` attribute and, for internal tools, `.ds-internal` is added to the parent element.

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

<!-- The same component, forced dark on any page -->
<div class="ds-card" data-theme="dark" style="color: var(--ds-text)">…</div>

<!-- Internal tools: the accent comes from the class, the mode from the attribute -->
<div class="ds-card ds-internal" data-theme="dark" style="color: var(--ds-text)">…</div>
```

- `data-theme="dark", data-theme="light"` — On any element, not only the root. The tokens are declared on any element carrying the attribute and custom properties inherit, so the *nearest* ancestor with `data-theme` wins, and nesting works in both directions: a dark sample inside a light panel inside a page following the OS renders correctly. The attribute re-points tokens and paints nothing itself. Anything inside that already reads tokens follows; the container has to take its own ground and text from tokens too, which here is `.ds-card` for the ground and `color: var(--ds-text)` for the text.
- `.ds-internal` — Internal tools. Re-points the accent to Access Lime, from tier 1, and composes with the attribute: lime holds its light value in dark, the wash goes to a dark olive, and text that sat on the wash turns lime to stay legible. An internal page puts it on `<html>`.

> Accents hold in both modes: Open Blue and Access Lime stay themselves, which is why the text on them is a fixed token too.

**Rule.** Preferences saved.

**Rule.** Preferences saved.

**Rule.** Preferences saved.

**Rule.** Preferences saved.

## Locking to light  (Modifiers)

Any page or element can lock to light mode only by adding `data-theme="light"`. We use this feature when demonstrating light mode, but it can also be useful if the content being worked with has no dark mode. For example, if porting in complex visualizations from an external engine that does not support dark mode.

```html
<!-- The whole page: only when the page exists to show light rendering -->
<html lang="en" data-theme="light">

<!-- One demo, while the page follows the reader -->
<div class="ds-card" data-theme="light" style="color: var(--ds-text)">…</div>
```

- `data-theme="light" on <html>` — Locks the page to light and opts it out of the `@media` block. Check that nothing rewrites it: a static attribute in the markup is not a lock if a script on the page sets the attribute at load. `theme.js` does exactly that, so a page that carries the theme control cannot also be locked.
- `data-theme="light" on a container` — One demo shows light while the page follows the reader. The same scoping as the dark island above, in the other direction.

> Test it with the theme control in the header: the page changes but this panel does not.

## Internal tools need no modifier  (Modifiers)

Internal tools load the same tier 1 stylesheet as public pages. Their speciall accent color comes from adding `.ds-internal` on `<html>`, so everything above applies to them unchanged. The internal pages tier 2 stylesheet, `internal-tools.css`, re-points only the tokens whose dark value differs on that surface. No manual adjustments are needed.

## Rules

- **Take every colour from a token.** Never write a dark hex into a page or a component. Components that consume tokens flip for free. [How it works](#the-mechanism)
- **Decide whether the colour is content or identity.** Content flips. Identity is pinned to a literal with a comment saying why — a masthead, a brand fill, a colour specimen whose subject is the value itself.
- **Fill raised things with `--ds-surface`.** Not `--ds-canvas`: the wash is a pale tint in light and *is* the canvas in dark, so anything filled with it disappears.
- **Check any text sitting on an accent fill.** Accents hold their light values in dark, so the text on them must not flip either — `--ds-text-on-accent` on lime and on Open Blue alike. Reaching for the plain token puts near-white text on a light fill, about 1.3:1.
- **Set the page's own background and text from tokens.** An inherited colour from a platform preset or a third-party stylesheet cannot flip, and it will not announce itself.
- **Do not use `color-scheme` to force a mode.** It governs browser-rendered widgets only — scrollbars, form controls — and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme`. [Scoping a mode](#scoping-a-mode)
- **Scope a demo that must show one mode.** Put `data-theme` on the demo's own container, not on the page. Pages should follow the reader. [Scoping a mode](#scoping-a-mode)
- **If anything can set `data-theme`, mirror the dark block under the attribute** as well as the media query — including inherited code you did not write. [How the attribute works](#the-mechanism)
- **Verify computed styles in both modes, and measure contrast.** Do not trust the cascade and do not judge by eye. Check the states a reader can actually reach: OS dark, OS light, and the attribute forced either way.
- Component CSS consumes tokens. Do not write hex values directly.
- `color-scheme` does not lock a page to a mode. It governs browser-rendered widgets like scrollbars, form controls, and the default canvas. It does not touch a stylesheet's `prefers-color-scheme` rules. If absolutely needed, use `data-theme` to lock a mode.
- **Respect the setting the reader already made.** A page follows the operating system's colour scheme unless the reader says otherwise on the page itself. Without JavaScript there is no button and the page follows the OS: the control is an addition, never the only route to a readable page.
- **The icon is the only visible part, so the name carries the state.** The button's accessible name says which state is on (“Theme: following the system. Activate to change.”), and a press announces its result in the live region. A sighted reader learns the three icons from the cards above; a screen reader user is told, and is never guessing whether the moon means “it is dark” or “make it dark”.
- **Never a dark value by hand.** Take every colour from a token and it flips with the rest of the page. A hex written into a page or a component cannot flip, and it will not announce itself.
- **Check contrast in both modes.** Verify computed styles and measure contrast in every state a reader can reach: OS dark, OS light, and the attribute forced either way. Do not trust the cascade and do not judge by eye. Anything that uses colour to carry meaning keeps its second cue (icon, word, position) in dark mode too — the WCAG 1.4.1 requirement applies in both modes.
- **Let form controls follow.** The stylesheet sets `color-scheme` beside the tokens, so native form controls, scrollbars and the default canvas take the same mode as the page. Do not set it yourself to force a mode: it governs those browser-rendered widgets only and does nothing to any stylesheet's `prefers-color-scheme` rules. Use `data-theme`.
