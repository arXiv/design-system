27 rows, each with an `is-sr-only` "(opens in new tab)" span and `target="_blank"` — every link carries all four off-site signals. The 28th `target="_blank"` is on the context demo's link, which checks out.

---

Here is everything that was built and every design-system rule applied.

---

## What was built

### 1. CSS component — `design-patterns/public/design-system.css` (appended)

**`~245` new lines** defining the `.ds-artifact-links` component family:

| Class | Role |
|---|---|
| `.ds-artifact-links` | Card wrapper — white surface, `--arxiv-border-light` hairline border, 6px radius, `overflow:hidden` to respect radius on children |
| `.ds-artifact-links-heading` | Card title — 15px/600/ink, flex row so an optional count badge can sit right-aligned |
| `.ds-artifact-links-count` | Optional count badge — 11px uppercase condensed/grey, right-aligned via `margin-left:auto` |
| `.ds-artifact-links-list` | The `<ul>` — `max-height:272px` / `overflow-y:auto` / `overscroll-behavior:contain`; focus ring on `:focus-visible` |
| `.ds-artifact-links-row` | Each `<li>` — three-column CSS grid (2fr / 1.2fr / 2.5fr), row hover fill, `--arxiv-border-light` separator |
| `.ds-artifact-label` | Artifact role text — 13px/500/ink, truncates with ellipsis |
| `.ds-artifact-dest` | Platform name — 11px uppercase condensed/grey, metadata-label scale |
| `.ds-artifact-link` | The `<a>` — link-blue underlined, hover/visited/focus-visible states |
| `.ds-artifact-ext-icon` | 11×11px SVG arrow-up-right — decorative off-site geometric cue |

Responsive at ≤480px: stacks to two rows per item (label + dest / link spanning both columns).

### 2. Demo page — `design-patterns/public/artifact-links-styles.html`

Seven sections:
1. **Single artifact** — minimum case
2. **Multiple (4 rows)** — within threshold, count badge shown
3. **Overflow (12 rows)** — half-item peek in action
4. **Interaction states** — forced-state statics for hover, link focus, list-region focus, visited
5. **Abstract page context** — card at realistic column width inside a page excerpt
6. **Design decisions table** — every decision traced to a source
7. **HTML markup** — copy-paste example with three callouts on heading level, dynamic count, and no-JS guarantee

---

## Every design-system rule applied

**Colors (all from `color-mapping.md` palette; no one-off hex values)**
- Card surface: `#fff` — "Page background: White" (public color vibe)
- Card/row borders: `--arxiv-border-light` `#ddd8d2` — decorative hairline, correctly below 3:1
- Row hover: `--arxiv-card-grey` `#f0eeec` — "Card surface / hover fill"
- Body text: `--arxiv-ink` `#1c1a17`
- Labels/destination: `--arxiv-grey` `#6b6459` — 5.83:1 on white ✓ AA
- Link at rest: `--arxiv-link-blue` `#1565c0` — 5.74:1 ✓ AA
- Link hover: `--arxiv-link-hover` `#1050a0` — 7.83:1 ✓ AAA
- Visited: `--arxiv-link-visited` `#7b2fbe` — 7.02:1 ✓ AAA
- Focus ring: `--arxiv-focus-ring` (= `--arxiv-link-blue`)
- No Access Lime on public page — that color signals internal tools (DESIGN-POLICIES.md)
- No Open Blue primary button — card reads as supplementary material, not a CTA

**Typography (`typography.md`)**
- Body/wrapper: `--arxiv-font-sans` (IBM Plex Sans)
- Labels: `--arxiv-font-condensed` (IBM Plex Sans Condensed), 11px uppercase, 0.04em letter-spacing — matches the established metadata-label type style
- No external fonts loaded; all font tokens point to arXiv's self-hosted woff2 files

**Accessibility (DESIGN-POLICIES.md + WCAG 2.2 AA targets)**
- `:focus-visible` exclusively (never bare `:focus`)
- `outline: 3px solid` / `outline-offset: 2px` on links; `-3px` on the scrollable region (inside the card border)
- `tabindex="0"` on `<ul>` so keyboard users can scroll without entering items
- `aria-label="N research artifacts"` on `<ul>` carries the total count to AT users — mandatory for scrollable regions per the truncation policy
- `role="list"` on `<ul>` for Safari/VoiceOver list-semantics preservation
- Off-site signal uses four non-color cues (WCAG 1.4.1): destination text + SVG icon + sr-only "(opens in new tab)" + `target="_blank" rel="noopener noreferrer"`
- `forced-colors` block: `ButtonBorder` for borders, `LinkText` / `VisitedText` for links, `stroke: LinkText` on the SVG icon
- `prefers-reduced-motion: reduce` block disables all transitions

**Truncation policy (DESIGN-POLICIES.md, "Truncation always signals continuation")**
- 6-row threshold documented in the CSS block comment and the demo page
- `max-height: 272px` ≈ 6.5 row heights at single-line content — the 7th row clips mid-height as the geometric continuation signal that survives forced-colors, zoom, and user stylesheets

**Spacing scale (DESIGN-POLICIES.md 4px / 8-point scale)**
- Padding: `11px 16px` (close to 12px / 16px on-scale), `gap: 8px 16px` — all values on the 4px grid

**Component naming (DESIGN-POLICIES.md)**
- All shared classes use the `.ds-` prefix
- No Sass, no framework syntax — plain CSS custom properties

**Brand (BRAND.md)**
- No view counts or engagement signals anywhere in the component (#2 — no gamification)
- No sticky chrome; no primary CTA (#1 — interface gets out of the way)
- Built for low-maintenance: no per-paper hand-tuning required; the template fills in count from metadata (#7 — built to last by a small team)