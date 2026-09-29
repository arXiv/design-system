---
page: colors.html
title: "Colors"
summary: "The full arXiv palette, rendered. Written spec and rationale: [color-mapping.md](doc.html?src=docs/color-mapping.md) (source of truth — if this page and the spec disagree, the spec wins). Hard rules live in [DESIGN-POLICIES.md](doc.html?src=docs/DESIGN-POLICIES.md): all colors come from this palette; no one-off hex values."
stylesheet: design-system.css
components:
  - id: brand-colors
    title: "Brand colors"
    summary: "arXiv's defining brand colors grouped by prominence and role. These key colors are expanded upon in the design system with additional tints and shades, but the identity remains consistent."
    rules:
      - "Do not cross Open Blue and Access Lime: Access Lime never appears on public pages; Open Blue never on internal tools. The color difference is functional and quickly informs the user staff which context they are working in."
  - id: links-and-interactive
    title: "Links and interactive"
    summary: "Colors that signal \"you can act on this.\" Link-vs-body contrast fails 3:1, so inline links are also underlined — color is never the only signal (WCAG 1.4.1). Link Blue is its own blue, not a brand blue: Open Blue is 1.5:1 on white and cannot carry text at all, and Archival Blue is reserved for headings, so links take a darker blue chosen for reading."
  - id: backgrounds-and-tints
    title: "Backgrounds and tints"
    summary: "Tints for section depth without hard borders fall into two families: warm-toned and cool-toned, following our two primary brand colors."
rules:
  - "No near-whites lighter than Warm Wash. If a lighter step is genuinely needed, add it to color-mapping.md first rather than inventing one locally."
  - "Recommended pairings"
  - "Repository Brown is the workhorse — it clears AA on every approved surface, which is why buttons set Repository Brown on Open Blue."
  - "Buttons change clothes on tinted surfaces"
  - "On white — default secondary"
  - "On a tinted band — add `.on-tint`"
  - "**Use tokens, not hex values.** Take every color from a `--ds-` token. The hex values on this page are specimens to read, not values to paste into a stylesheet. A color with no token is not available to build with."
  - "**Every pairing on this page already passes.** Each text colour clears WCAG AA (4.5:1) on every surface it is documented for, in both modes, and `verification/check-contrast.py` fails if a token change ever breaks one. That is the reason to take colours from tokens and never to override one: a hex typed by hand is a pairing nobody has checked."
  - "**Never use color alone.** Pair a color with a word, an icon, an underline, or a change of position, so a reader who cannot see the color still gets the message (WCAG 1.4.1)."
  - "**Dark mode flips the tokens.** Every token on this page takes its dark value on its own. Never hand-pick a dark value into a page; see [Dark mode](dark-mode.html) for what flips and what stays fixed."
---

# Colors

The full arXiv palette, rendered. Written spec and rationale: [color-mapping.md](doc.html?src=docs/color-mapping.md) (source of truth — if this page and the spec disagree, the spec wins). Hard rules live in [DESIGN-POLICIES.md](doc.html?src=docs/DESIGN-POLICIES.md): all colors come from this palette; no one-off hex values.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Brand colors

arXiv's defining brand colors grouped by prominence and role. These key colors are expanded upon in the design system with additional tints and shades, but the identity remains consistent.

**Rule.** Do not cross Open Blue and Access Lime: Access Lime never appears on public pages; Open Blue never on internal tools. The color difference is functional and quickly informs the user staff which context they are working in.

## Links and interactive

Colors that signal "you can act on this." Link-vs-body contrast fails 3:1, so inline links are also underlined — color is never the only signal (WCAG 1.4.1). Link Blue is its own blue, not a brand blue: Open Blue is 1.5:1 on white and cannot carry text at all, and Archival Blue is reserved for headings, so links take a darker blue chosen for reading.

## Backgrounds and tints

Tints for section depth without hard borders fall into two families: warm-toned and cool-toned, following our two primary brand colors.

## Rules

- No near-whites lighter than Warm Wash. If a lighter step is genuinely needed, add it to color-mapping.md first rather than inventing one locally.
- Recommended pairings
- Repository Brown is the workhorse — it clears AA on every approved surface, which is why buttons set Repository Brown on Open Blue.
- Buttons change clothes on tinted surfaces
- On white — default secondary
- On a tinted band — add `.on-tint`
- **Use tokens, not hex values.** Take every color from a `--ds-` token. The hex values on this page are specimens to read, not values to paste into a stylesheet. A color with no token is not available to build with.
- **Every pairing on this page already passes.** Each text colour clears WCAG AA (4.5:1) on every surface it is documented for, in both modes, and `verification/check-contrast.py` fails if a token change ever breaks one. That is the reason to take colours from tokens and never to override one: a hex typed by hand is a pairing nobody has checked.
- **Never use color alone.** Pair a color with a word, an icon, an underline, or a change of position, so a reader who cannot see the color still gets the message (WCAG 1.4.1).
- **Dark mode flips the tokens.** Every token on this page takes its dark value on its own. Never hand-pick a dark value into a page; see [Dark mode](dark-mode.html) for what flips and what stays fixed.
