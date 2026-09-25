# Color Mapping — Internal vs Public

**Status:** Active
**Last updated:** 2026-07-24

---

## The arXiv palette

### Primary colors — browns & blues

These are arXiv's core identity colors post-spinout. They carry the weight of the brand on both internal and public platforms.

| Name | Hex | Role |
|---|---|---|
| **Repository Brown** | `#1c1a17` | Body text, dark backgrounds, primary headers |
| **Library Grey** | `#6b6459` | Secondary text, labels, muted interactive elements (5.83:1 on white) |
| **UI Boundary Grey** | `#8b8680` | Interactive borders, tracks, arrows — WCAG 3:1 compliant (3.61:1 on white) |
| **Disabled Grey** | `#b0aba6` | Disabled states, exempt from WCAG contrast requirements |
| **Link Blue** | `#1565c0` | All interactive links, light mode (5.74:1 on white) |
| **Link Hover** | `#1050a0` | Link hover state (7.83:1 on white) |
| **Visited Purple** | `#7b2fbe` | Visited link state (7.02:1 on white) |
| **Archival Blue** | `#1f5e96` | Brand accent blue. Candidate for public button identity. Close to Link Blue — may need to shift for differentiation. |
| **Open Blue** | `#a5d6fe` | Public primary action fill (with Repository Brown text, 11.3:1 AA); also a light-blue tint for section backgrounds and highlights |

### Accent colors

Used for energy and personality. These are "pop" colors, not workhorses.

| Name | Hex | Contrast on white | Suitable for |
|---|---|---|---|
| **Access Lime** | `#c4d82e` | ~1.5:1 | Background fills, badges, accent stripes. NOT for text or small elements. |
| **Smileybones Yellow** | `#ffe000` | ~1.3:1 | Background fills, the smileybones icon, celebratory/playful accents. NOT for text or fine detail. |

Both accent colors fail text contrast on white — they are strictly "big gesture" colors for fills, borders at sufficient thickness, and graphic elements.

If a darker yellow is needed for smaller accents (thin borders, small badges), a golden variant like `#d4b800` (~2.5:1 on white) could work while staying in the yellow family. This would need to be derived from the original if the use case arises.

### Heritage colors — used sparingly

These connect arXiv to its history. They are not primary brand colors post-spinout.

| Name | Hex | Origin | Usage |
|---|---|---|---|
| **Campus Red** | `#b31b1b` | Formerly "Cornell Red" | The X in the arXiv logo. Very occasional accent — a thin rule, a hover detail. Never for headers, buttons, large color fields, or text. |
| **Publishing Pink** | `#fb595a` | Complement to Campus Red | Rare accent for playful or celebratory contexts. Announcements, limited-time callouts. Never for errors or body text. |

### Functional colors — shared

These serve specific UI functions and are not part of the brand identity.

| Name | Hex | Role |
|---|---|---|
| **Danger Red** | `#c62828` | Destructive actions, error states. Distinct from Campus Red — this is functional, not brand. |
| **Focus Ring** | `#1565c0` light / `#64b5f6` dark | Keyboard focus indicator |

### Status & alert colors — shared

Semantic colors for the `.ds-alert` component and any success / informational / warning / error messaging. One system in both the public (white) and internal (Warm Wash) surfaces, light and dark. Each state is also distinguished by an icon and a leading word — never color alone (WCAG 1.4.1). All text/background pairings clear AA; most clear AAA.

| State | Light bg | Light border | Light text/icon | Dark bg | Dark border | Dark text/icon | Text contrast (light / dark) |
|---|---|---|---|---|---|---|---|
| **Success** | `#e8f5d8` | `#6b8e1e` | `#4a5a0a` | `#1e2b0d` | `#8fbd3a` | `#c5e1a5` | 6.7:1 / 10.4:1 |
| **Info** | `#e7f1fd` | `#5a82c8` | `#1a3a78` | `#132433` | `#64b5f6` | `#90caf9` | 9.6:1 / 9.0:1 |
| **Warning** | `#fff8e1` | `#e8b800` | `#7a5c00` | `#2e2410` | `#e8b800` | `#ffe082` | 5.9:1 / 11.8:1 |
| **Error / failure** | `#fdeaea` | `#c62828` | `#8b0000` | `#2d1414` | `#e57373` | `#ef9a9a` | 8.6:1 / 8.0:1 |

Why these values:

- **Success is lime-olive, not forest green.** arXiv has no success-green, and Access Lime `#c4d82e` is reserved as the "internal tools" signal *and* fails text contrast — so it cannot double as success. Rather than introduce a new green family, success reuses the existing `.ds-ds-seg-btn--positive` lime-olive (bg `#e8f5d8`, text `#4a5a0a`) with the border pulled off-yellow (`#6b8e1e` — lower red channel than `--ds-accent-border` `#9cb522`) so it reads as "success," not "brand accent." A forest-green alternative was considered and rejected to keep the palette tight.
- **Info is navy, deliberately darker than Link Blue** `#1565c0`, so an info banner is never mistaken for a link. Reuses the `.ds-ds-seg-btn` / `.ds-badge--new` family.
- **Warning is the existing version-warning amber** (`#fff8e1` / `#e8b800` / `#7a5c00`), promoted from the one-off abstract-page banner.
- **Error reuses Danger Red** `#c62828` for the border, with a light tint background and the `.ds-ds-seg-btn--negative` deep-red text `#8b0000`.

Tokens: both stylesheets expose `--ds-success-*` / `--ds-info-*` / `--ds-warning-*` / `--ds-error-*` under the same names, with per-surface values. Both drive an identical `.ds-alert` component (icon + leading word, `role="status"` vs `role="alert"`, light + dark, plus `forced-colors` / `prefers-reduced-motion` handling).

### Background tints

Barely perceptible tints for creating section depth without hard borders.

| Name | Hex | Use |
|---|---|---|
| **Warm Wash** | `#f9f7f7` | Warm background — footer, metadata sections |
| **Cool Wash** | `#f7fafc` | Cool background — section differentiation |
| **Grey Hover** | `#f0eeec` | Table headers, hover fills, Related section background |
| **Grey Active** | `#e4e0db` | Active/pressed fills, footer background |
| **Border Light** | `#ddd8d2` | Component hairline borders — inputs, toggle tracks, card edges. Decorative only (below 3:1); not for sole interactive boundaries. Promoted from the mockups 2026-06-11. |
| **Blue tint** | `#f0f5ff` | Code/identifier backgrounds, citation display boxes |

---

## Internal tools — color vibe

**Warm, utilitarian, lime-accented.** The internal tools (arXiv Check, Admin Console) are staff-facing workspaces where efficiency matters. Access Lime signals "arXiv internal tools" and distinguishes them from public pages.

| Element | Color | Token |
|---|---|---|
| Primary button | Access Lime `#c4d82e` | `--ds-accent` |
| Secondary button | Lime tint `#f0f9e8` border `#9cb522` | `--ds-accent-wash`, `--ds-accent-border` |
| Page background | Warm Wash `#f9f7f7` | — |
| Header | (varies by tool) | — |
| Text | Repository Brown `#1c1a17` | `--ds-text` |
| Secondary text | Library Grey `#6b6459` | `--ds-text-muted` |

---

## Public pages — color vibe

**Clean, fast, brown-and-blue.** The public pages (abstract, HTML papers, listings, homepage) are researcher-facing. The design is restrained — content-first, minimal chrome. Color comes from the logo, links, and subtle tinted sections.

| Element | Color | Notes |
|---|---|---|
| **Header bar** | Black (phase 1) → Repository Brown (phase 2) | See phasing notes below. |
| **Page background** | White `#ffffff` | Clean reading surface. |
| **Related section background** | Grey Hover `#f0eeec` | Full-width band, clearly secondary. |
| **Footer background** | Grey Active `#e4e0db` | Darker than Related, anchors the bottom. |
| **Body text** | Repository Brown `#1c1a17` | — |
| **Secondary text** | Library Grey `#6b6459` | Metadata labels, dates, muted captions. |
| **Links** | Link Blue `#1565c0` | All interactive links. Author names, category links, DOIs. |
| **Primary action buttons (PDF, HTML)** | Open Blue `#a5d6fe`, Repository Brown text | Locked public primary. Repository Brown is the only AA text color on Open Blue (11.3:1). |
| **Secondary buttons (TeX Source)** | White with UI Boundary Grey border `#8b8680` | Lighter weight for secondary actions. |
| **Version link (current)** | Repository Brown `#1c1a17`, bold | Inline text link, **not** a filled pill; sets `aria-current`. |
| **Version link (other)** | Link Blue `#1565c0`, underlined | Navigates to that version. (Supersedes the earlier filled "version pills" — see `version-display.html`.) |
| **Version warning banner** | Light amber `#fff8e1` border `#e8b800` | — |
| **Cite section borders** | `#e4e0db` | Bordered columns within the cite section. |
| **Labs toggles (on)** | Link Blue `#1565c0` | Indicates active state. |

### When to use accent colors on public pages

**Access Lime** `#c4d82e`:
- **Not used on public pages.** Access Lime is the internal-tools signal, and putting it on a public page crosses the one line the two accent colors exist to draw. The public stylesheet has no lime token, deliberately.
- The design system's own documentation pages carry a lime header rule; those are internal reference material, not public arXiv pages.
- *Removed 2026-08-11:* this entry used to offer lime for a public "category marker" or "new" badge. It contradicted both the stylesheet and the never-cross rule (Shamsi: "that is crossing the internal/public line").

**Smileybones Yellow** `#ffe000` — token `--ds-brand-smileybones-yellow`:
- The smileybones icon itself (Labs branding, mascot appearances)
- Celebratory or playful contexts (anniversaries, milestones)
- Background fills for callout banners or badges
- **Framing images, and only horizontally.** On [outreach properties](outreach/) it appears as thick rules above and below a figure, bracketing the whole plate including the caption. It is never a vertical rule or a column divider — that job belongs to Open Blue (decided 2026-08-11).
- Never for text, small UI elements, or anything requiring contrast on white
- Holds its value in dark mode, like the other accents

**Campus Red** `#b31b1b`:
- The X in the arXiv logo mark
- Very occasional accent
- Never for headers, buttons, large color fields, or text

**Publishing Pink** `#fb595a`:
- Rare. Time-limited announcements, celebratory accents
- Heritage throwback contexts
- Never for errors or body text

---

## Which tint for which job

*(Added 2026-06-17. Rendered on the colors page: `colors.html#uses`.)*

The tints sorted by the job they do. Reach for the named token; if a job is not listed, it is a change to this document, not a new local value.

| The job | Reach for | Where it shows up |
|---|---|---|
| Page / section background, warm | **Warm Wash** `--ds-canvas` | Default subtle ground — footer, metadata bands, internal page background |
| Section background, cooler | **Cool Wash** `#f7fafc` | When a band should read cooler than Warm Wash to differentiate adjacent sections |
| Secondary content band | **Card Grey** `--ds-surface-muted` | Related band, reader header — one step down from the page, no hard border |
| Card surface / hover fill | **Card Grey** `--ds-surface-muted` | Card fills and hover fills |
| Active / pressed fill, deepest warm band | **Grey Active** `--ds-border-muted` `#e4e0db` | Footer edge, pressed states, pill borders. Body-size grey/links miss AA here — use Repository Brown or Link Hover |
| Decorative hairline | **Border Light** `--ds-border` | Input / card / track edges. Below 3:1 — never the sole boundary of a control |
| arXiv chrome floating over paper | **Tint Light** + **Tint Border** | Popovers, TOC dropdown — the "light blue = arXiv speaking, not the paper" rule (G4) |
| Inline active anchor · read-aloud highlight · panel hover | **Active Wash** `--ds-accent-wash` | Deepest arXiv-chrome blue that still holds AA for normal-size text |
| Open Blue hover step | **Open Blue Bright** `--ds-accent-hover` `#c2e2ff` | Hover state for Open Blue primary fills |
| Code / identifier background | **Blue Tint** `#f0f5ff` | Code blocks, citation/identifier display boxes |
| Public primary action fill | **Open Blue** `--ds-accent` | The one brand fill that carries Repository Brown text at AA |
| Status surface | the four status tints | See "Status & alert colors" above — each pairs with an icon + leading word |

**Ready-to-use pairings** (the contrast matrix read as instructions):

| On this surface | Body text & links (AA) | Large text / borders only (3:1) | Do not use |
|---|---|---|---|
| White · Warm Wash · Card Grey · Tint Light | Repository Brown, Library Grey, Link Blue, Link Hover, Archival Blue, Visited Purple | UI Boundary Grey (borders) | — |
| Active Wash `#d6e8f7` | Repository Brown, Library Grey, Link Blue, Link Hover, Archival Blue, Visited Purple | — | UI Boundary Grey |
| Grey Active `#e4e0db` | Repository Brown, Link Hover, Archival Blue, Visited Purple | Library Grey, Link Blue (≥18px) | UI Boundary Grey |
| Open Blue `#a5d6fe` | Repository Brown only | Library Grey, Link Blue, Archival Blue (≥18px) | UI Boundary Grey; body-size grey & links |

> **Drift reconciled (2026-06-17):** the mockups' off-palette one-offs were snapped to tokens — near-white grounds `#fafaf8` / `#fafaf9` → Warm Wash; light-blue footer band `#e8f4ff` → Tint Light; hover blue `#0d4a96` → Link Hover `#1050a0`. Do not reintroduce near-whites lighter than Warm Wash; if a lighter step is ever needed, add it here first.

---

## Tints, tiers, and combinations on tinted backgrounds

*(Added 2026-06-13. Rendered with computed ratios on the colors page: `colors.html#tinted`.)*

Every tint in the system belongs to one of two families: the **warm tints** (Repository Brown stepped toward white — Warm Wash, Grey Hover/Card Grey, Grey Active, Border Light, plus the text greys) and the **arXiv Chrome family** (Open Blue's tints — Tint Light, Tint Border, Active Wash, and the hover step `#c2e2ff`).

**"No one-off hex values" has three tiers:**

1. **Palette tokens** — everything in this document. Free to use in their documented roles.
2. **Component-internal constants** — values that exist only inside a component's own CSS: the button-border gradient stops (`#b0d5ed`, `#6ba8da`, `#8fc1e8`, `#4a86b8`, `#c8c4be`, `#b3ada4`, `#7eb8e0`), the dark header's hover fill `#302c28` and divider `#4a433d`. They are part of those components, not the palette — do not lift them for new uses.
3. **Everything else** — does not exist. A new value is a change to this document, not a local invention.

**Accessible combinations on tints** (computed, WCAG; full matrix on the colors page):

- **Repository Brown `#1c1a17` passes AA on every approved surface** — including Open Blue (11.3:1), which is why buttons set Repository Brown on Open Blue.
- **Library Grey and Link Blue hold AA through Active Wash** (`#d6e8f7`) but miss it on **Grey Active** (`#e4e0db`: 4.45 / 4.37) — on Grey Active use Repository Brown, Link Hover `#1050a0` (6.0:1), or large text.
- **UI Boundary Grey holds its 3:1 only through Tint Light** — on Grey Active, Active Wash, or Open Blue, draw boundaries with Library Grey instead.
- **On Open Blue itself, Repository Brown is the only text color.**
- **Secondary buttons on tinted bands take the `.on-tint` modifier** (fill swaps to Card Grey — secondary via warm-on-cool material difference, not low contrast). See `design-system.css`.

---

## Decisions made

- **Browns and blues are the primary palette.** Post-spinout, arXiv's visual identity is built on Repository Brown, Library Grey, and the blue family. These carry the brand.

- **Access Lime and Smileybones Yellow are accent colors.** Both are high-energy "pop" colors used sparingly. Both fail text contrast on white, so they are restricted to fills, borders, and graphic elements.

- **Campus Red and Publishing Pink are heritage colors.** They stay in the palette as nods to arXiv's roots but are no longer primary. Campus Red lives in the logo X; Publishing Pink is for rare celebratory use.

- **Public primary buttons are Open Blue (locked).** The public primary action fill is Open Blue `#a5d6fe` with Repository Brown text (11.3:1, AA). Archival Blue stays available as a secondary brand-accent blue, not the primary.

- **Dark mode** — the internal tools' dark mode tokens are a good foundation for public pages.

- **Status / alert colors defined (2026-05-28).** A shared four-state semantic palette (success, info, warning, error/failure) plus a `.ds-alert` component, light + dark, on both internal and public surfaces. Success stays in the lime-olive family rather than adding a forest green. See "Status & alert colors — shared" above. This also lands the *first* dark-aware tokens in the public stylesheet.

- **Header color phasing:**
  - **Phase 1 (spinout):** Black header. Clean break from the red era.
  - **Phase 2 (later):** Transition to Repository Brown `#1c1a17`. Introduced after users have adjusted to the new minimal header.

## Which text is safe on which surface

The full pairing table — every text-role token against every surface, measured in both modes — lives on [colors.html](colors.html), in the "Which text is safe on which surface" section. It is generated from the stylesheets by `verification/check-contrast.py`, which fails when the table and the tokens disagree; regenerate rather than hand-edit. The short rule the table encodes: text colors come from the text tiers (primary, secondary, links, status foregrounds); the border, disabled, and UI tiers are never for reading text, however close their ratios look.

## Open questions

- [ ] **Archival Blue shift** — optionally shift `#1f5e96` for more differentiation from Link Blue `#1565c0` in its secondary-accent role. (The public *primary* button is settled: Open Blue — see Decisions made.)
- [ ] **Smileybones Yellow as a darker variant** — if a golden variant is needed for smaller accents, explore `#d4b800` or similar. Must stay in the yellow family.
- [ ] **Dark mode token extension** — extend the internal dark mode overrides to cover public page components.
