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
    summary: "Link colors signal \"you can act on this\" and are a foundational part of accessibility. All link colors maintain accessible contrast levels with their background color in light and dark mode. In addition, inline links are always underlined and color is not the only signal."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA) and [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)"
      - "Meets accessibility guideline [WCAG 2.2 SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) Non-text Contrast (Level AA)"
  - id: tints-and-shades
    title: "Tints and shades"
    summary: "Tints and shades are used in a variety of ways: to define page areas and boundaries, to fill components, and to indicate disabled states. They come in two color families, warm brown and cool blue, which can be used to establish two content languages on complex pages. As an example, blue tints are used on HTML papers to distinguish content that belongs to arXiv (DOI, citation tools, and more) while author-created content belongs on the warm tints and white."
    classes:
      - name: "--ds-tint-warm"
        does: "The warm tint. The same value on both surfaces."
      - name: "--ds-tint-accent"
        does: "The accent tint. Tint Light on public pages, the Access Lime wash inside `.ds-internal`. A component uses the token and gets the right colour on each surface."
rules:
  - "No near-whites lighter than Warm Wash. If a lighter step is genuinely needed, add it to color-mapping.md first rather than inventing one locally."
  - "A component fill uses a tint or a status color. A new fill color is discussed with the design team first."
  - "Repository Brown is the workhorse — it clears AA on every approved surface, which is why buttons set Repository Brown on Open Blue."
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

Link colors signal "you can act on this" and are a foundational part of accessibility. All link colors maintain accessible contrast levels with their background color in light and dark mode. In addition, inline links are always underlined and color is not the only signal.

> Meets accessibility guidelines [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA) and [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)

> Meets accessibility guideline [WCAG 2.2 SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) Non-text Contrast (Level AA)

## Tints and shades

Tints and shades are used in a variety of ways: to define page areas and boundaries, to fill components, and to indicate disabled states. They come in two color families, warm brown and cool blue, which can be used to establish two content languages on complex pages. As an example, blue tints are used on HTML papers to distinguish content that belongs to arXiv (DOI, citation tools, and more) while author-created content belongs on the warm tints and white.

```html
background: var(--ds-tint-warm);
background: var(--ds-tint-accent);
```

- `--ds-tint-warm` — The warm tint. The same value on both surfaces.
- `--ds-tint-accent` — The accent tint. Tint Light on public pages, the Access Lime wash inside `.ds-internal`. A component uses the token and gets the right colour on each surface.

## Rules

- No near-whites lighter than Warm Wash. If a lighter step is genuinely needed, add it to color-mapping.md first rather than inventing one locally.
- A component fill uses a tint or a status color. A new fill color is discussed with the design team first.
- Repository Brown is the workhorse — it clears AA on every approved surface, which is why buttons set Repository Brown on Open Blue.
- On white — default secondary
- On a tinted band — add `.on-tint`
- **Use tokens, not hex values.** Take every color from a `--ds-` token. The hex values on this page are specimens to read, not values to paste into a stylesheet. A color with no token is not available to build with.
- **Every pairing on this page already passes.** Each text colour clears WCAG AA (4.5:1) on every surface it is documented for, in both modes, and `verification/check-contrast.py` fails if a token change ever breaks one. That is the reason to take colours from tokens and never to override one: a hex typed by hand is a pairing nobody has checked.
- **Never use color alone.** Pair a color with a word, an icon, an underline, or a change of position, so a reader who cannot see the color still gets the message (WCAG 1.4.1).
- **Dark mode flips the tokens.** Every token on this page takes its dark value on its own. Never hand-pick a dark value into a page; see [Dark mode](dark-mode.html) for what flips and what stays fixed.
