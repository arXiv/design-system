---
page: action-feedback.html
title: "Show that something was copied"
summary: "Copy and Permalink do their work out of sight: nothing on the page changes. Say that it worked, in words for a screen reader and with a tick for everyone, and leave focus where it was. If it failed, show that too, and say what to do instead. The same rules apply to any action whose result is not otherwise announced, such as the theme control."
stylesheet: design-system.css
components:
  - id: where-it-is-used
    title: "Where it is used"
    summary: ""
    notes:
      - "The copy button on every code block, including each citation format in a paper's Cite. See [Typography](typography.md#code-blocks-and-the-copy-button).; Permalink on a section heading, on a docs page and in a paper. See [Linking to a section](links.md#linking-to-a-section).; Copy and Permalink on an equation, a figure or a reference. See [Equations, figures and references](papers.md#paper-elements).; Copy emails, the one action in a list's header bar on the moderators dashboard. The mockup has its own script for now.; The theme control, which says which theme is now in use. It changes the page, but not in a way a screen reader hears. See [Dark mode](dark-mode.md#the-theme-control)."
  - id: a-copy-button
    title: "A copy button"
    summary: "Any button that copies, here one that copies an identifier. Press Copy: the tick takes the icon's place for two seconds, a screen reader hears “Identifier copied”, and focus stays on the button, which is still called Copy. Below it, the same button after a copy that failed; pressing it tries again."
    classes:
      - name: "copy.js"
        does: "Once per page. It copies for every button below, adds the copy button to every code block, and makes the page's status region. A copy button does nothing without it, so write the button `hidden`, and `copy.js` shows it. A Permalink is a link to its `#id` instead, which works without the script."
      - name: "[data-copy]"
        does: "The text to copy. `data-copy-link=\"#S2\"` copies the page's address with that fragment instead, and `data-copy-from=\"S2.E14\"` copies that element's text, or an equation's MathML."
      - name: "[data-copied]"
        does: "What a screen reader hears after the copy. It names what was copied where a page has many such buttons. Without it, “Copied to clipboard”."
      - name: ".ds-copy-done"
        does: "The tick, beside the button's own icon. For two seconds after a copy the script adds `.is-done` to the button, and the tick takes the icon's place."
      - name: "[data-copy-failed]"
        does: "Optional: what to do if the copy fails. Without it, a link says “Copy failed — copy the link from the address bar”, after the script has put the link there, and other text says “Copy failed — select the text and copy it manually”."
      - name: ".ds-copy-failed"
        does: "The alert. The script adds it to the button the first time a copy fails, and adds `.is-failed`: the alert takes the icon's place until the button is pressed again."
      - name: ".ds-copy-failed-message"
        does: "The line that says what to do instead, which also describes the button. The script puts it under the code block, heading, equation or paragraph the button belongs to, or under the button itself when the button is in the margin."
    notes:
      - "Meets accessibility guideline [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)"
rules:
  - "**Say what happened, in words.** A visually hidden `role=\"status\"` region says it: “Copied to clipboard”. Where a page has many controls that do the same thing, it names what was copied: “Link to equation 2.14 copied”."
  - "**Focus stays on the control.**"
  - "**The control keeps its name.** The name says what it does: Copy is still Copy after copying."
  - "**Show it too, where nothing else on the page changes.** A visible sign goes with the words, such as a green tick, and both reset after two seconds."
  - "**Show a failure, and say what to do instead.** An alert takes the icon's place, and a line under the control says it: “Copy failed — select the code and copy it manually”. Both stay until the control is pressed again, and a control that shows on hover stays in view while they do."
  - "**A link that could not be copied goes in the address bar.** The address is not on the page, so the script puts it where people already copy links from, without moving the page, and the line says “Copy failed — copy the link from the address bar”."
  - "**The line goes under the control's line**, as a field's error goes under the field: under the code block, heading, equation or paragraph. A control in the margin keeps the line under itself, in the margin, so it stays beside the control however long the paragraph."
  - "**Every copy button uses `copy.js`.** A page never writes its own copy handler, so every copy gives the same feedback."
---

# Show that something was copied

Copy and Permalink do their work out of sight: nothing on the page changes. Say that it worked, in words for a screen reader and with a tick for everyone, and leave focus where it was. If it failed, show that too, and say what to do instead. The same rules apply to any action whose result is not otherwise announced, such as the theme control.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Where it is used



> The copy button on every code block, including each citation format in a paper's Cite. See [Typography](typography.md#code-blocks-and-the-copy-button).; Permalink on a section heading, on a docs page and in a paper. See [Linking to a section](links.md#linking-to-a-section).; Copy and Permalink on an equation, a figure or a reference. See [Equations, figures and references](papers.md#paper-elements).; Copy emails, the one action in a list's header bar on the moderators dashboard. The mockup has its own script for now.; The theme control, which says which theme is now in use. It changes the page, but not in a way a screen reader hears. See [Dark mode](dark-mode.md#the-theme-control).

## A copy button

Any button that copies, here one that copies an identifier. Press Copy: the tick takes the icon's place for two seconds, a screen reader hears “Identifier copied”, and focus stays on the button, which is still called Copy. Below it, the same button after a copy that failed; pressing it tries again.

```html
<button type="button" class="ds-btn ds-btn-compact" hidden data-copy="arXiv:2604.22725" data-copied="Identifier copied">
  <svg aria-hidden="true">…</svg>
  <svg class="ds-copy-done" aria-hidden="true">…</svg>
  Copy<span class="is-sr-only"> identifier</span>
</button>
<script src="copy.js" defer></script>
```

- `copy.js` — Once per page. It copies for every button below, adds the copy button to every code block, and makes the page's status region. A copy button does nothing without it, so write the button `hidden`, and `copy.js` shows it. A Permalink is a link to its `#id` instead, which works without the script.
- `[data-copy]` — The text to copy. `data-copy-link="#S2"` copies the page's address with that fragment instead, and `data-copy-from="S2.E14"` copies that element's text, or an equation's MathML.
- `[data-copied]` — What a screen reader hears after the copy. It names what was copied where a page has many such buttons. Without it, “Copied to clipboard”.
- `.ds-copy-done` — The tick, beside the button's own icon. For two seconds after a copy the script adds `.is-done` to the button, and the tick takes the icon's place.
- `[data-copy-failed]` — Optional: what to do if the copy fails. Without it, a link says “Copy failed — copy the link from the address bar”, after the script has put the link there, and other text says “Copy failed — select the text and copy it manually”.
- `.ds-copy-failed` — The alert. The script adds it to the button the first time a copy fails, and adds `.is-failed`: the alert takes the icon's place until the button is pressed again.
- `.ds-copy-failed-message` — The line that says what to do instead, which also describes the button. The script puts it under the code block, heading, equation or paragraph the button belongs to, or under the button itself when the button is in the margin.

> Meets accessibility guideline [WCAG 2.2 SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) Status Messages (Level AA)

## Rules

### Copy, Permalink and similar actions

- **Say what happened, in words.** A visually hidden `role="status"` region says it: “Copied to clipboard”. Where a page has many controls that do the same thing, it names what was copied: “Link to equation 2.14 copied”.
- **Focus stays on the control.**
- **The control keeps its name.** The name says what it does: Copy is still Copy after copying.
- **Show it too, where nothing else on the page changes.** A visible sign goes with the words, such as a green tick, and both reset after two seconds.
- **Show a failure, and say what to do instead.** An alert takes the icon's place, and a line under the control says it: “Copy failed — select the code and copy it manually”. Both stay until the control is pressed again, and a control that shows on hover stays in view while they do.
- **A link that could not be copied goes in the address bar.** The address is not on the page, so the script puts it where people already copy links from, without moving the page, and the line says “Copy failed — copy the link from the address bar”.
- **The line goes under the control's line**, as a field's error goes under the field: under the code block, heading, equation or paragraph. A control in the margin keeps the line under itself, in the margin, so it stays beside the control however long the paragraph.
- **Every copy button uses `copy.js`.** A page never writes its own copy handler, so every copy gives the same feedback.
