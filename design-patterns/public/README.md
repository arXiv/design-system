# Public-Facing Design Patterns

Design patterns for arxiv.org, abstract pages, HTML paper pages, search, and other researcher-facing interfaces.

## Status

In progress. HTML mockups are being developed for the abstract page redesign and the unified header/footer. Pattern pages will be added here as components stabilize.

## Color vibe

**Clean, fast, brown-and-blue.** The public pages are researcher-facing and content-first. The design is restrained — Repository Brown for structure, Open Blue for primary actions, Link Blue for interactive links, and light tints for section depth.

See `../color-mapping.md` for the full palette and usage rules.

Key differences from internal:
- Primary buttons: **Open Blue** `#a5d6fe` with black text (internal uses Access Lime)
- Secondary buttons: white with **Library Grey** `#6b6459` outline (internal uses lime tint)
- Header: **black** (phase 1) → Repository Brown (phase 2) — single bar, no red
- Toggle on-state: **Link Blue** `#1565c0` (internal uses lime green)
- Section headings: **Archival Blue** `#1f5e96`

## What is shared with internal

- Typography: IBM Plex Sans, Condensed, Mono (see `../typography.md`)
- Accessibility: all WCAG 2.0 AA rules (see `../../DESIGN-POLICIES.md`)
- Button mechanics: 6px radius, 10px 20px padding, subtle shadow, press effect, 0.12s transitions
- Focus ring: `var(--focus-ring)` with dark mode override
- Warm grey ladder: same tokens (`--grey`, `--grey-ui`, `--grey-dis`)
- Segmented controls: same semantic variants (positive/neutral/negative)
- Form validation: same patterns (`.is-invalid`, `.field-error`, `.field-required`)

## Mockups in development

These live in the working directory (`/Desktop/arXiv-mockups/arxiv-public/`) and will be codified into pattern pages here as they stabilize:

- **abstract-spinout.html** — interim header for the Cornell spinout. Original page content preserved, only header and footer changed. Production-ready proposal.
- **abstract-redesign.html** — bold reimagining of the abstract page. Single column, no sidebar, integrated citation section, Labs toggles. Phase 2 vision.
- **html-redesign.html** — HTML paper reader with light header variant. Sibling of the abstract page.

## Planned pattern pages

- [ ] Button styles (primary Open Blue, secondary grey, tertiary text-only)
- [ ] Header component (dark bar for abstract pages, light bar for HTML reader)
- [ ] Footer component
- [ ] Citation section (BibTeX, APA, Chicago, MLA with source toggle)
- [ ] Version display (pills, warning banner)
- [ ] Author list with truncation
- [ ] Labs toggle section
- [ ] Announcement/banner component

## Current reference

- Color palette: `../color-mapping.md`
- Typography: `../typography.md`
- Internal patterns (shared foundations): `../internal/`
- Visual audit (the "why"): `../../visual-audit/audit-report.md`
