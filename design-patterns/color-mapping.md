# Color Mapping — Internal vs Public

**Status:** Draft
**Last updated:** 2026-04-29

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
| **Open Blue** | `#a5d6fe` | Light blue tint for section backgrounds, highlights, dark mode hover states |

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

### Background tints

Barely perceptible tints for creating section depth without hard borders.

| Name | Hex | Use |
|---|---|---|
| **Warm Wash** | `#f9f7f7` | Warm background — footer, metadata sections |
| **Cool Wash** | `#f7fafc` | Cool background — section differentiation |
| **Grey Hover** | `#f0eeec` | Table headers, hover fills, Related section background |
| **Grey Active** | `#e4e0db` | Active/pressed fills, footer background |
| **Blue tint** | `#f0f5ff` | Code/identifier backgrounds, citation display boxes |

---

## Internal tools — color vibe

**Warm, utilitarian, lime-accented.** The internal tools (arXiv Check, Admin Console) are staff-facing workspaces where efficiency matters. Access Lime signals "arXiv staff tools" and distinguishes them from public pages.

| Element | Color | Token |
|---|---|---|
| Primary button | Access Lime `#c4d82e` | `--lime` |
| Secondary button | Lime tint `#f0f9e8` border `#8a9b1e` | `--sec-bg`, `--sec-border` |
| Page background | Warm Wash `#f9f7f7` | — |
| Header | (varies by tool) | — |
| Text | Repository Brown `#1c1a17` | `--text` |
| Secondary text | Library Grey `#6b6459` | `--grey` |

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
| **Action buttons (PDF, HTML)** | Repository Brown `#1c1a17` (placeholder) | Will get a strong color identity — TBD. |
| **Secondary buttons (TeX Source)** | White with UI Boundary Grey border `#8b8680` | Lighter weight for secondary actions. |
| **Version pills (current)** | Repository Brown `#1c1a17` | — |
| **Version pills (other)** | Grey Hover `#f0eeec` background | — |
| **Version warning banner** | Light amber `#fff8e1` border `#e8b800` | — |
| **Cite section borders** | `#e4e0db` | Bordered columns within the cite section. |
| **Labs toggles (on)** | Link Blue `#1565c0` | Indicates active state. |

### When to use accent colors on public pages

**Access Lime** `#c4d82e`:
- Small highlights: accent stripe, category marker, "new" badge
- The lime-accented header border on the internal design system pattern pages could appear on public pages as a design-system-aware accent
- Never for buttons or large interactive elements on public pages

**Smileybones Yellow** `#ffe000`:
- The smileybones icon itself (Labs branding, mascot appearances)
- Celebratory or playful contexts (anniversaries, milestones)
- Background fills for callout banners or badges
- Never for text, small UI elements, or anything requiring contrast on white

**Campus Red** `#b31b1b`:
- The X in the arXiv logo mark
- Very occasional accent
- Never for headers, buttons, large color fields, or text

**Publishing Pink** `#fb595a`:
- Rare. Time-limited announcements, celebratory accents
- Heritage throwback contexts
- Never for errors or body text

---

## Decisions made

- **Browns and blues are the primary palette.** Post-spinout, arXiv's visual identity is built on Repository Brown, Library Grey, and the blue family. These carry the brand.

- **Access Lime and Smileybones Yellow are accent colors.** Both are high-energy "pop" colors used sparingly. Both fail text contrast on white, so they're restricted to fills, borders, and graphic elements.

- **Campus Red and Publishing Pink are heritage colors.** They stay in the palette as nods to arXiv's roots but are no longer primary. Campus Red lives in the logo X; Publishing Pink is for rare celebratory use.

- **Public buttons need a strong color identity.** Repository Brown is a placeholder. A distinct, high-contrast button color is needed — Archival Blue is the leading candidate but may need to shift to differentiate from Link Blue. This is a key usability priority.

- **Dark mode** — the internal tools' dark mode tokens are a good foundation for public pages.

- **Header color phasing:**
  - **Phase 1 (spinout):** Black header. Clean break from the red era.
  - **Phase 2 (later):** Transition to Repository Brown `#1c1a17`. Introduced after users have adjusted to the new minimal header.

## Open questions

- [ ] **Archival Blue shift** — explore shifting `#1f5e96` to create more differentiation from Link Blue `#1565c0`. It could anchor the public button identity.
- [ ] **Public primary button color** — what color best serves the "unmissable primary action" role? Candidates: shifted Archival Blue, a dedicated new blue, or something derived from the existing palette.
- [ ] **Smileybones Yellow as a darker variant** — if a golden variant is needed for smaller accents, explore `#d4b800` or similar. Must stay in the yellow family.
- [ ] **Dark mode token extension** — extend the internal dark mode overrides to cover public page components.
