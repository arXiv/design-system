# Dark mode tints and shades: audit

2026-10-05. Do the public site's surface and tint tokens do the same jobs in dark mode as in light mode? Values are read from `docs/design-system.css` (`:root` and the public dark block). Internal tools (Access Lime) are not covered yet.

The numbers are contrast ratios between two fills, the same measure as text contrast. 1.00 means the two are the same colour. Fills do not need to pass 3:1; what matters is that a step that shows in light mode also shows in dark mode, and about as strongly.

## The tokens

| Token | Its job | Light | Dark |
|---|---|---|---|
| `--ds-canvas` | The page ground | `#ffffff` | `#1c1a17` |
| `--ds-surface` | Cards, inputs, raised things | `#ffffff` | `#2b2723` |
| `--ds-surface-muted` | Table header cells, the pager bars, secondary bands | `#f0f0ee` | `#2b2723` |
| `--ds-surface-hover` | A row or control under the pointer | `#f8f7f7` | `#1c1a17` |
| `--ds-tint-warm` / `--ds-zone-secondary-bg` | The tinted band, striped rows, the filter bar | `#f0f0ee` | `#221f1b` |
| `--ds-tint-accent` | Selected rows, the current page, tooltips, popovers | `#edf7ff` | `#1e3a5f` |
| `--ds-accent-wash` | The deeper accent fill: matched words, a pressed text button | `#d2eafe` | `#1e3a5f` |
| `--ds-border` | Hairlines | `#dad8d6` | `#3a3530` |

## The layers, measured

| Fill | On | Light | Dark | Finding |
|---|---|---|---|---|
| surface-muted | surface | 1.14 | **1.00** | 1. Collapses |
| surface-hover | canvas | 1.07 | **1.00** | 2. Collapses |
| accent-wash | tint-accent | 1.14 | **1.00** | 3. Collapses |
| tint-warm | canvas | 1.14 | 1.06 | 4. Half as strong |
| tint-accent | canvas | 1.09 | 1.51 | 5. Much stronger |
| border | surface | 1.42 | 1.22 | 6. Weaker |
| surface | canvas | 1.00 | 1.17 | By design: dark mode raises cards |
| surface-muted | canvas | 1.14 | 1.17 | Matches |
| border | canvas | 1.42 | 1.43 | Matches |

## Findings

1. **Inside a card, grey fills disappear in dark mode.** `--ds-surface-muted` is the same colour as `--ds-surface`. A table's header row, a pager bar or a secondary band inside a card has no fill at all. This is how the pager demo on `search.html` looks in dark mode.
2. **Hover does nothing on the page ground in dark mode.** `--ds-surface-hover` is the page ground itself. A table row that sits on the page (not in a card) gives no hover feedback. Inside a card it works.
3. **The two accent fills are one colour in dark mode.** Light mode has a pale tint and a deeper wash; dark mode uses one value for both. Anything that relies on the difference, such as a matched word inside a selected row, loses it.
4. **The tinted band is half as visible in dark mode.** The band behind a page's introduction, and the filter bar, are much fainter than in light mode.
5. **The accent tint is far louder in dark mode.** The dark navy stands out about five times more against the page than the pale blue does in light mode. Selected rows, tooltips and the current page draw more attention in dark than they were designed to.
6. **Hairlines are fainter on cards in dark mode.**

## What would make dark a mirror of light

One ladder of fills, each a visible step from the one below, in both modes:

- page ground, then tinted band, then card, then a grey fill inside a card, each a little lighter than the last in dark mode, as each is a little darker in light mode;
- hover is always one step from whatever it sits on, never the page ground itself;
- the accent tint and the accent wash are two steps in dark as in light, and both closer to the light-mode strength.

These are new dark values for existing tokens, not new colours in light mode. Each would need its text contrast checked (`verification/check-contrast.py`). No values are proposed here until Shamsi has read the findings.

## Not yet covered

- Internal tools (Access Lime): the same measurements with `.ds-internal`.
- Status fills (alerts, status tags) in dark mode.
- The site header in dark mode: `--ds-chrome` is only 1.09 against the page ground, so the header barely separates from the page.
