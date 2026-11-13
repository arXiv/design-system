---
page: colors.html
title: "Colors"
summary: "The full arXiv palette, rendered, with what each color is for. Hard rules live in [DESIGN-POLICIES.md](../doc.html?src=docs/DESIGN-POLICIES.md): all colors come from this palette; no one-off hex values. The values themselves are in `design-system.css`."
stylesheet: design-system.css
components:
  - id: brand-colors
    title: "Brand colors"
    summary: "arXiv's defining brand colors grouped by prominence and role. These key colors are expanded upon in the design system with additional tints and shades, but the identity remains consistent."
  - id: links-and-interactive
    title: "Links and interactive"
    summary: "Link colors signal \"you can act on this\" and are a foundational part of accessibility. All link colors maintain accessible contrast levels with their background color in light and dark mode. In addition, inline links are always underlined and color is not the only signal."
    notes:
      - "Meets accessibility guidelines [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA) and [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)"
      - "Meets accessibility guideline [WCAG 2.2 SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) Non-text Contrast (Level AA)"
  - id: tints-and-shades
    title: "Tints and shades"
    summary: "Tints and shades are used in a variety of ways: to define page areas and boundaries, to fill components, and to indicate disabled states. They come in two color families, warm brown and cool blue, which can be used to establish two kinds of content on complex pages. As an example, blue tints are used on HTML papers to distinguish content that belongs to arXiv (DOI, citation tools, and more) while author-created content belongs on the warm tints and white."
    classes:
      - name: "--ds-tint-warm"
        does: "The warm tint. The same value on both surfaces."
      - name: "--ds-tint-accent"
        does: "The accent tint: blue on public pages, a lime wash inside `.ds-internal`. A component uses the token and gets the right color on each surface."
rules:
  - "\"No one-off hex values\" has three tiers. **Tier 1 — palette tokens** (everything on this page): free to use in their documented roles. **Tier 2 — component-internal constants**: a handful of values that exist only inside a component's own CSS: the button-border gradient stops (`#b0d5ed`, `#6ba8da`, `#8fc1e8`, `#4a86b8`, `#c8c4be`, `#b3ada4`, `#7eb8e0`), the destructive button's border stops (`#d4453f`, `#8e1c1c`, `#e0605a`, `#a52626`) and inner shadow (`rgb(90, 10, 10)` at any opacity), the close button's wash (`rgb(128, 128, 128)` at any opacity), and the dark header's hover fill `#302c28` and divider `#4a433d`. They are part of those components, not the palette; do not lift them for new uses. `verification/check-policies.py` reads this list. **Tier 3 — everything else**: does not exist. If a new value seems needed, it is a change to the palette, made with the design team, not a local invention."
  - "No near-whites lighter than Warm Tint. If a lighter step is genuinely needed, add it to the palette first rather than inventing one locally."
  - "A component fill uses a tint or a status color. A new fill color is discussed with the design team first."
  - "The recommended set — what to reach for on each surface. It is deliberately not exhaustive: any pairing not listed here, and any new tint, must be checked against WCAG AA before use (4.5:1 normal text; 3:1 large text and UI boundaries)."
  - "Repository Brown is the workhorse — it clears AA on every approved surface, which is why buttons set Repository Brown on Open Blue."
  - "The secondary button's white fill reads as \"primary\" against a tinted band, so tinted sections add the `.on-tint` modifier: the fill swaps to Warm Tint — same luminance as the surface, *warm* hue — so the button reads as secondary through warm-on-cool material difference, not through low contrast. Live from [the button pattern](buttons.md):"
  - "**Use tokens, not hex values.** Take every color from a `--ds-` token. The hex values on this page are specimens to read, not values to paste into a stylesheet. A color with no token is not available to build with."
  - "**Every pairing on this page already passes.** Each text color clears WCAG AA (4.5:1) on every surface it is documented for, in both modes, and `verification/check-contrast.py` fails if a token change ever breaks one. That is the reason to take colors from tokens and never to override one: a hex typed by hand is a pairing nobody has checked."
  - "**Never use color alone.** Pair a color with a word, an icon, an underline, or a change of position, so a reader who cannot see the color still gets the message (WCAG 1.4.1)."
  - "**Dark mode flips the tokens.** Every token on this page takes its dark value on its own. Never hand-pick a dark value into a page; see [Dark mode](dark-mode.md) for what flips and what stays fixed."
---

# Colors

The full arXiv palette, rendered, with what each color is for. Hard rules live in [DESIGN-POLICIES.md](../doc.html?src=docs/DESIGN-POLICIES.md): all colors come from this palette; no one-off hex values. The values themselves are in `design-system.css`.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Brand colors

arXiv's defining brand colors grouped by prominence and role. These key colors are expanded upon in the design system with additional tints and shades, but the identity remains consistent.

These colors harken back to arXiv's legacy as part of Cornell University. Campus Red is Cornell's primary brand color, while Publishing Pink was a complement color to make it our own. Campus Red can still be found in arXiv's primary logomark which was developed and trademarked in 2021. Since the arXiv spinout these colors are used sparingly when we need to reference our history or are co-branding with Cornell University.

## Links and interactive

Link colors signal "you can act on this" and are a foundational part of accessibility. All link colors maintain accessible contrast levels with their background color in light and dark mode. In addition, inline links are always underlined and color is not the only signal.

> Meets accessibility guidelines [WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) Contrast (Minimum) (Level AA) and [WCAG 2.2 SC 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) Use of Color (Level A)

> Meets accessibility guideline [WCAG 2.2 SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) Non-text Contrast (Level AA)

## Tints and shades

Tints and shades are used in a variety of ways: to define page areas and boundaries, to fill components, and to indicate disabled states. They come in two color families, warm brown and cool blue, which can be used to establish two kinds of content on complex pages. As an example, blue tints are used on HTML papers to distinguish content that belongs to arXiv (DOI, citation tools, and more) while author-created content belongs on the warm tints and white.

```html
background: var(--ds-tint-warm);
background: var(--ds-tint-accent);
```

- `--ds-tint-warm` — The warm tint. The same value on both surfaces.
- `--ds-tint-accent` — The accent tint: blue on public pages, a lime wash inside `.ds-internal`. A component uses the token and gets the right color on each surface.

| Color and tokens | Light | Dark | Why it exists |
|---|---|---|---|
| Canvas `--ds-canvas` | `#ffffff` | `#1c1a17` | The ground of every page and the footer. In dark mode the page is Repository Brown. |
| Warm Tint `--ds-tint-warm` `--ds-surface-hover` | `#f0f0ee` | `#282622` | The warm tint: the secondary page band, data cards, the table header row, row headers, striped rows, notes, tags, and the disabled button fill. Also the hover fill on a white surface. |
| Accent Tint `--ds-tint-accent` `--ds-accent-surface` | `#edf7ff` | `#202b38` | The accent tint on public pages: selected table rows and a pressed button. Also the ground of a panel arXiv adds over the paper: a popover, a dropdown, the reader footer band. |
| Accent Tint, internal `--ds-tint-accent` | `#f0f9e8` | `#292b18` | The accent tint in internal tools: selected table rows and a pressed button. Inside `.ds-internal`, the accent tokens take Access Lime values. |
| Accent Wash `--ds-accent-wash` | `#d2eafe` | `#22344a` | The deepest chrome blue that still holds AA for body text: an active inline anchor, a hover inside a panel, the read-aloud highlight. |
| Accent Hover `--ds-accent-hover` `--ds-accent-border` | `#c0e2fe` | `#c0e2fe` hover `#2a4a7a` panel edges | The hover step of an Open Blue fill, which takes `--ds-text-on-accent` like the fill it hovers from, and the edge of a panel arXiv adds over the paper. |
| Border `--ds-border` | `#dad8d6` | `#383531` | Hairlines on inputs and cards, pressed fills, pill borders, the footer edge. Decorative only: it is below 3:1, so it is never the only edge of a control, and body-size gray text and links miss AA on it. |
| Strong Border `--ds-border-strong` | `#89837a` | `#89837a` | The edge of a control: input borders, switch edges, sort arrows. The one gray that clears 3:1 on white, which is what the edge of a control needs. |
| Disabled Text `--ds-text-disabled` | `#aeaaa4` | `#5a554f` | Disabled text only. A disabled control is exempt from contrast requirements. |

## Rules

### Working on tinted backgrounds

"No one-off hex values" has three tiers. **Tier 1 — palette tokens** (everything on this page): free to use in their documented roles. **Tier 2 — component-internal constants**: a handful of values that exist only inside a component's own CSS: the button-border gradient stops (`#b0d5ed`, `#6ba8da`, `#8fc1e8`, `#4a86b8`, `#c8c4be`, `#b3ada4`, `#7eb8e0`), the destructive button's border stops (`#d4453f`, `#8e1c1c`, `#e0605a`, `#a52626`) and inner shadow (`rgb(90, 10, 10)` at any opacity), the close button's wash (`rgb(128, 128, 128)` at any opacity), and the dark header's hover fill `#302c28` and divider `#4a433d`. They are part of those components, not the palette; do not lift them for new uses. `verification/check-policies.py` reads this list. **Tier 3 — everything else**: does not exist. If a new value seems needed, it is a change to the palette, made with the design team, not a local invention.

No near-whites lighter than Warm Tint. If a lighter step is genuinely needed, add it to the palette first rather than inventing one locally.

A component fill uses a tint or a status color. A new fill color is discussed with the design team first.

The recommended set — what to reach for on each surface. It is deliberately not exhaustive: any pairing not listed here, and any new tint, must be checked against WCAG AA before use (4.5:1 normal text; 3:1 large text and UI boundaries).

| On this surface | Text & links | UI borders |
|---|---|---|
| **Canvas · Warm Tint · Accent Tint** | Repository Brown, Library Grey, Link Blue / Link Hover, Archival Blue, Visited Purple | Strong Border |
| **Accent Wash** #d2eafe | Repository Brown, Library Grey, Link Blue / Link Hover, Archival Blue, Visited Purple | Library Grey |
| **Border** #dad8d6 | Repository Brown, Link Hover, Archival Blue, Visited Purple | Library Grey |
| **Open Blue** #a5d6fe | Repository Brown | Repository Brown |

Repository Brown is the workhorse — it clears AA on every approved surface, which is why buttons set Repository Brown on Open Blue.

The secondary button's white fill reads as "primary" against a tinted band, so tinted sections add the `.on-tint` modifier: the fill swaps to Warm Tint — same luminance as the surface, *warm* hue — so the button reads as secondary through warm-on-cool material difference, not through low contrast. Live from [the button pattern](buttons.md):

### Accessibility essentials

- **Use tokens, not hex values.** Take every color from a `--ds-` token. The hex values on this page are specimens to read, not values to paste into a stylesheet. A color with no token is not available to build with.
- **Every pairing on this page already passes.** Each text color clears WCAG AA (4.5:1) on every surface it is documented for, in both modes, and `verification/check-contrast.py` fails if a token change ever breaks one. That is the reason to take colors from tokens and never to override one: a hex typed by hand is a pairing nobody has checked.
- **Never use color alone.** Pair a color with a word, an icon, an underline, or a change of position, so a reader who cannot see the color still gets the message (WCAG 1.4.1).
- **Dark mode flips the tokens.** Every token on this page takes its dark value on its own. Never hand-pick a dark value into a page; see [Dark mode](dark-mode.md) for what flips and what stays fixed.
