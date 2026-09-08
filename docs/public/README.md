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
- Accessibility: all WCAG 2.1 AA rules — the ACA floor; 2.2 AA is the working target (see `../../DESIGN-POLICIES.md`)
- Button mechanics: 6px radius, 10px 20px padding, subtle shadow, press effect, 0.12s transitions
- Focus ring: `var(--ds-focus-ring)` with dark mode override
- Warm grey ladder: same tokens (`--ds-text-muted`, `--ds-border-strong`, `--ds-text-disabled`)
- Segmented controls: same semantic variants (positive/neutral/negative)
- Form validation: same patterns (`.is-invalid`, `.field-error`, `.field-required`)

## Pattern pages

- [x] **Button styles** — primary (Open Blue) and secondary (white + warm-grey border) with V3 construction validated 2026-05-14. The `.on-tint` modifier for secondary buttons on tinted surfaces (Card Grey fill, hover-brightens to Warm Wash) was added 2026-05-22 — see `button-styles.html` and `design-system.css`.
- [x] **Inline active state** (`.ds-inline-active`) — light-blue background + underline applied to inline interactive elements (citation chips, footnote markers) when they are the active anchor. Validated 2026-05-27 in `arxiv-mockups/arxiv-public/html-redesign.html`. See `design-system.css`.
- [x] **Link** (`.ds-link`) — inline text link with rest / hover / visited / focus states. Tokens `--ds-link`, `--ds-link-hover`, `--ds-link-visited` (with dark-mode overrides) match the `color-mapping.md` spec. Validated 2026-05-28 — see `link-styles.html` and `design-system.css`.
- [x] **Annotation typography** (`.ds-annotation`) — serif italic in warm-grey for secondary editorial commentary (footnote text, figure alt-text in margin). Uses `--ds-font-serif` (IBM Plex Serif). Validated 2026-05-27. See `design-system.css`.
- [x] **Popover panel** (`.ds-popover` + parts) — light-blue tint floating panel anchored to inline elements. Used by citation chips and footnote markers. Validated 2026-05-27. See `design-system.css`.
- [x] **Element pill** (`.ds-element-pill`) — small white pill that floats anchored to a piece of content (equation, figure) to host action affordances. Distill-style chrome. Validated 2026-05-27. See `design-system.css`.
- [x] **Accordion** (`.ds-acc` + `.ds-acc-stack` / `.ds-acc-body`, rail variant `.ds-acc-rail`) — native `<details>/<summary>` disclosure with a +/− marker; card dressing by default, chrome-dropped rail dressing inside `<aside>` rails. No new tokens. Validated as `.mg-acc` in `mockups/public/merged-abstract-reader.html` (removed 2026-08-10; the pattern lives on in `mockups/public/html-phase1.html`), promoted 2026-07-28 — see `../organizing-content.html` and `design-system.css`.
- [x] **Forms & validation** (`.ds-field` family) — label + control + hint + error, width helpers, the three validation moments, and the accessibility contract. No new tokens. Built 2026-08-11 — see [forms.html](../forms.html).
- [x] **Tags** (`.ds-tag`) — the small rounded label for subject categories, topics, and states. Quiet / chrome / status levels, uppercase by default with `.ds-tag--keep-case` for identifiers, plus `.ds-tag-remove` and `.ds-tag-note`. No new tokens. Validated 2026-08-11 against the admin-console category editors — see [tags.html](../tags.html).
- [x] Text button (`.ds-btn-text`) — the quiet tier, built 2026-08-11. An outline-only variant was considered and rejected: the secondary is already white-fill-plus-border, so on a white canvas the two would differ by a drop shadow alone. Rationale on [buttons.html](../buttons.html).
- [x] **Header component (abstract page variant)** (`.ds-announcement` + `.ds-site-header`) — *Design approved and codified 2026-06-11*, validated against the spinout-header-footer Cloud Run deployment (which covers only the banner + black bar; nothing below is approved chrome). The behavior contract (skip link first, "archive" pronunciation, search-as-link progressive enhancement, dark-bar focus rings, no-hamburger narrow-width wrap) is documented with the pattern. The `.ds-skip-link` utility was promoted alongside it. A breadcrumb band was briefly included and removed 2026-06-11 (too shallow to justify real estate; links exist elsewhere). See `header-styles.html` and `design-system.css`.
- [ ] **Header component (HTML reader variant)** — the reader chrome is a header bar, a sticky contents bar and a reading indicator. The earlier single-bar version was retired: the design moved on in `mockups/public/html-phase1.html`, which is where it is being worked out. Promote when it settles.
- [x] **Footer component** (`.ds-site-footer`) — *Design approved and codified 2026-06-11.* Wording exact-match to the spinout-header-footer Cloud Run deployment. Three pieces: ack line (with optional IP-matched institutional mention), footer nav (About · Help · Contact · Subscribe · Copyright · Privacy · Accessibility · Operational Status), and "Major funding support from" + Simons + Schmidt funder logos. The behavior contract (landmarks, aria-hidden separators, sr-only external-link notices, rem type) is documented with the pattern. See `footer-styles.html` and `design-system.css`. The `.is-sr-only` utility was promoted alongside it.
- [ ] Citation section (BibTeX, APA, Chicago, MLA with source toggle)
- [ ] Version display (inline version links + warning banner)
- [ ] Author list with truncation
- [ ] Labs toggle section
- [ ] Announcement/banner component

## Current reference

- Color palette: `../color-mapping.md`
- Typography: `../typography.md`
- Internal patterns (shared foundations): `../internal/`
- Visual audit (the "why"): `../../verification/audits/audit-visual.md`
