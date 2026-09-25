# arXiv Shared Design System — Progress Notes
**Project:** Admin Console + arXiv Check shared component library
**Last updated:** 2026-07-24

---

## Files in this folder

| File | Purpose |
|---|---|
| `internal-tools.css` | Source of truth for all shared component CSS |
| `buttons.html` | Button style guide / visual reference |
| `cards.html` | Info card component guide |
| `colors.html` | The palette, both surfaces; the separate internal token page was folded into it |
| `link-styles.html` | Text link color reference — states, contexts, visited |
| `tables.html` | Data table, sortable headers, filter toolbar |
| *(merged)* | Segmented control, toggle switch and form validation moved to `docs/forms.html` |
| `alert-styles.html` | Alert / status banner — live examples + self-syncing token table |

---

## Decisions made — Button styles

### Dark mode icon buttons
- **Constructive icon button** — lime border (`var(--ds-accent)` = `#c4d82e`), lighter lime-tint hover bg `#2e4a0a` (lime icon 6.28:1 ✓), active bg `#253a08` (7.84:1 ✓)
- **Destructive icon button** — red border matching icon: `#e57373` default, `#ef9a9a` hover/active
- All other icon button states use `--ds-border-strong` (warm grey) for disabled

---

## Decisions made — Link colors

### Why two tokens are required
No single blue satisfies 4.5:1 on both light (white/Warm Wash) and dark (Repository Brown/dark card) simultaneously — the luminance ranges do not overlap. Two tokens with a dark mode override are mandatory.

### Chosen colors

| Token | Hex | Name | Contrast | Mode |
|---|---|---|---|---|
| `--ds-link` | `#1565c0` | Link Blue Light Mode | 5.74:1 on white, 5.38:1 on Warm Wash ✓ AA | Light |
| `--ds-link-hover` | `#1050a0` | — | 7.83:1 on white ✓ | Light |
| `--ds-link-disabled` | `#b0aba6` | — | same as `--ds-text-disabled` | Light |
| `--ds-link-visited` | `#7b2fbe` | Visited Purple Light Mode | 7.02:1 on white, 6.58:1 on Warm Wash ✓ AA | Light |
| `--ds-link` | `#64b5f6` | Link Blue Dark Mode | 7.84:1 on Repo Brown, 7.08:1 on dark card ✓ AAA | Dark override |
| `--ds-link-hover` | `#90caf9` | — | lighter tint | Dark override |
| `--ds-link-disabled` | `#484340` | — | warm dark grey | Dark override |
| `--ds-link-visited` | `#c084e0` | Visited Purple Dark Mode | 6.30:1 on Repo Brown, 5.68:1 on dark card ✓ AA | Dark override |

### Underline requirement
Link-vs-body-text contrast fails 3:1 in both modes → **underlines are mandatory for all inline links.** Standalone nav links (no surrounding body text) may omit underlines.

### Brand Link Blue `#1e8bc3` status
Retired from body-text use — fails 4.5:1 on white. Kept as a brand reference color only.

---

## Decisions made — Status / alert colors

A shared four-state semantic palette (success, info, warning, error/failure) driving a token-based `.ds-alert` component, light + dark. Promoted from `arxiv-mockups/docs/alert-styles.html` (2026-05-28). Full rationale + the dark-mode table live in `../color-mapping.md`.

The full four-state table (light + dark bg / border / text, with contrast ratios) is single-sourced in [`../color-mapping.md`](../color-mapping.md) → *Status & alert colors — shared*; not duplicated here.

Key decisions:
- **Success is lime-olive, not a new forest green.** Access Lime `#c4d82e` stays the "internal tools" signal and fails text contrast, so success reuses the `.ds-ds-seg-btn--positive` lime-olive with the border tuned off-yellow (`#6b8e1e`) to read as success, not brand accent.
- **Reuse over invention** — info = `.ds-ds-seg-btn` navy (darker than `--ds-link` so it is not read as a link); warning = the abstract version-warning amber; error = `--ds-danger` red.
- **Color is never the sole signal** — each variant pairs with a distinct icon shape + leading word (WCAG 1.4.1), so the states survive grayscale and `forced-colors` mode.
- **OS signals honored** — `prefers-color-scheme` (dark tokens), `forced-colors` (links → `LinkText`, never `forced-color-adjust:none`), `prefers-reduced-motion`. `prefers-contrast` needs nothing (all pairings clear AA).

Deferred: a **toast** pattern (transient/positioned/animated) and an **action-button slot** (Retry / Undo) on alerts.

## Decisions made — Admin console session (paper detail + edit metadata)

Session mockup: `../../mockups/internal/admin-console/paper-details/index.html`. Codified in the files noted; items marked *pending* still want a fuller pattern page.

- **Spacing scale** — `--ds-space-1`…`--ds-space-12` added to `internal-tools.css`; scale + proximity rule in `DESIGN-POLICIES.md` (Spacing).
- **Layout & content width** — content-driven, not audience-driven (measure for text; shell width by density). In `DESIGN-POLICIES.md` (Layout and content width).
- **Versions** — context + current text-link treatment in `../../README.md` (Versions); stale filled "version pills" retired in `../color-mapping.md`. *Pending:* a proper `version-nav` pattern page covering the one-version → many-versions spectrum on both surfaces.
- **Read-only vs editable cards** — `cards.html` now documents the editable "section card" alongside the read-only `.ds-info-card`, and the deliberate visual distinction. *Pending:* extract the section-card CSS into `internal-tools.css`.
- **Form layout + category editor** — documented in `docs/forms.html` (Layout): top-aligned labels, typographic grouping, content-matched field widths, standardized action bar. *Pending:* interactive demos + extracting the category-editor / form-field classes into `internal-tools.css`.
- **Nav selected state** — reuses the existing active/pressed convention (tint fill + darkened text, from the `--ds-accent-wash` ladder), not a bespoke white pill. No new rule needed.
- **Raw / Browse display** — two variants of one toggle: a *display swap* on read-only pages, a *preview reveal* on editable forms.
- **To reconcile:** the Edit-Endorsements modal uses a blue Save — internal primary is Access Lime (existing rule); update the modal.

---

## What is still pending

### Longer term (open questions)
- [ ] **Visited link hover state** — what color when you hover a visited link? Darken the purple, or reset to default blue?
- [ ] **Form input base styles** — text inputs, checkboxes, radio buttons, full select styling (beyond filter select)
- [ ] **Modal / dialog pattern** — backdrop, container, footer button grouping
- [ ] **Dark mode** for new components — tables, segmented control, filter select, validation states
- [ ] **Typography migration** — move from Google Fonts to self-hosted IBM Plex woff2 files. See `../typography.md` for the full spec

## Completed
- [x] All button tokens finalized and committed
- [x] `@media (prefers-color-scheme: dark)` block added (fully replaces `.on-dark` preview approach)
- [x] Secondary button dark mode: `color: var(--ds-accent)` in dark mode block — no new token needed
- [x] Focus ring: `#1565c0` light / `#64b5f6` dark — documented and committed
- [x] Visited link colors confirmed: `#7b2fbe` light / `#c084e0` dark
- [x] Dark mode icon button variants (constructive lime border, destructive red border)
- [x] **Data table** (`.ds-table`) — base styles, header row, hover, footer
- [x] **Sortable headers** (`.sortable`, `.sort-asc`, `.sort-desc`, `.sort-arrow`) — clickable columns with direction indicators
- [x] **Filter select** (`.ds-filter`) — underline-only select with custom chevron for toolbar filters
- [x] **Segmented control** (`.ds-seg`, `.ds-seg-btn`) — exclusive-choice button group with positive/neutral/negative active variants
- [x] **Toggle switch** (`.toggle-switch`, `.toggle-track`, `.toggle-thumb`, `.toggle-label`) — boolean on/off with lime-green checked state
- [x] **Form validation** (`.is-invalid`, `.field-error`) — invalid border/ring, inline error messages. The red required asterisk (`.field-required`) was removed 2026-09-23: every surface marks the optional fields in words instead (DESIGN-POLICIES)
- [x] **WCAG AA audit** — added `--ds-border-strong` (`#8b8680`, 3.61:1 on white) to fill palette gap between `--ds-text-disabled` (2.24:1) and `--ds-text-muted` (5.83:1). Updated toggle track, toggle off-label, sort arrow, filter underline, seg control border, icon button border, and info card label to pass 3:1 UI / 4.5:1 text thresholds
- [x] **Status / alert colors + `.ds-alert`** — four-state semantic palette (success/info/warning/error) and a token-driven alert banner, light + dark, with `forced-colors` / `prefers-reduced-motion` handling. Mirrored into the public stylesheet. See "Decisions made — Status / alert colors" above

---

## Key brand colors for reference

| Name | Hex |
|---|---|
| Repository Brown | `#1c1a17` |
| Dark Surface (cards) | `#2e2b26` |
| Warm Wash | `#f9f7f7` |
| UI Boundary Grey | `#8b8680` |
| Library Grey | `#6b6459` |
| Access Lime | `#c4d82e` |
| Archival Blue | `#1f5e96` |
| Brand Link Blue | `#1e8bc3` (retired for body text) |

---

## WCAG rules that drove decisions

- **4.5:1** — AA normal text (body copy, links)
- **3:1** — AA large text / UI component boundaries
- **7:1** — AAA
- **1.4.1** — Color alone cannot identify a link; underlines required when link vs body text < 3:1
- **1.4.11** — Non-text contrast for UI boundaries (buttons, icons) must pass 3:1
