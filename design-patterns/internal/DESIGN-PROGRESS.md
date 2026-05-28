# arXiv Shared Design System — Progress Notes
**Project:** Admin Console + arXiv Check shared component library
**Last updated:** 2026-05-28

---

## Files in this folder

| File | Purpose |
|---|---|
| `design-system.css` | Source of truth for all shared component CSS |
| `button-styles.html` | Button style guide / visual reference |
| `card-styles.html` | Info card component guide |
| `color-tokens.html` | Full color token reference (light + dark) |
| `link-styles.html` | Text link color reference — states, contexts, visited |
| `table-styles.html` | Data table, sortable headers, filter toolbar |
| `form-styles.html` | Segmented control, toggle switch, form validation |

---

## Decisions made — Button styles

### Dark mode icon buttons
- **Constructive icon button** — lime border (`var(--lime)` = `#c4d82e`), lighter lime-tint hover bg `#2e4a0a` (lime icon 6.28:1 ✓), active bg `#253a08` (7.84:1 ✓)
- **Destructive icon button** — red border matching icon: `#e57373` default, `#ef9a9a` hover/active
- All other icon button states use `--icon-border` (warm grey) for disabled

---

## Decisions made — Link colors

### Why two tokens are required
No single blue satisfies 4.5:1 on both light (white/Warm Wash) and dark (Repository Brown/dark card) simultaneously — the luminance ranges don't overlap. Two tokens with a dark mode override are mandatory.

### Chosen colors

| Token | Hex | Name | Contrast | Mode |
|---|---|---|---|---|
| `--link` | `#1565c0` | Link Blue Light Mode | 5.74:1 on white, 5.38:1 on Warm Wash ✓ AA | Light |
| `--link-hover` | `#1050a0` | — | 7.83:1 on white ✓ | Light |
| `--link-dis` | `#b0aba6` | — | same as `--grey-dis` | Light |
| `--link-visited` | `#7b2fbe` | Visited Purple Light Mode | 7.02:1 on white, 6.58:1 on Warm Wash ✓ AA | Light |
| `--link` | `#64b5f6` | Link Blue Dark Mode | 7.84:1 on Repo Brown, 7.08:1 on dark card ✓ AAA | Dark override |
| `--link-hover` | `#90caf9` | — | lighter tint | Dark override |
| `--link-dis` | `#484340` | — | warm dark grey | Dark override |
| `--link-visited` | `#c084e0` | Visited Purple Dark Mode | 6.30:1 on Repo Brown, 5.68:1 on dark card ✓ AA | Dark override |

### Underline requirement
Link-vs-body-text contrast fails 3:1 in both modes → **underlines are mandatory for all inline links.** Standalone nav links (no surrounding body text) may omit underlines.

### Brand Link Blue `#1e8bc3` status
Retired from body-text use — fails 4.5:1 on white. Kept as a brand reference color only.

---

## Decisions made — Status / alert colors

A shared four-state semantic palette (success, info, warning, error/failure) driving a token-based `.ds-alert` component, light + dark. Promoted from `arxiv-mockups/design-patterns/alert-styles.html` (2026-05-28). Full rationale + the dark-mode table live in `../color-mapping.md`.

| State | Light bg / border / text | Dark bg / border / text | Text contrast (light / dark) |
|---|---|---|---|
| `--success-*` | `#e8f5d8` / `#6b8e1e` / `#4a5a0a` | `#1e2b0d` / `#8fbd3a` / `#c5e1a5` | 6.7:1 / 10.4:1 |
| `--info-*` | `#e7f1fd` / `#5a82c8` / `#1a3a78` | `#132433` / `#64b5f6` / `#90caf9` | 9.6:1 / 9.0:1 |
| `--warning-*` | `#fff8e1` / `#e8b800` / `#7a5c00` | `#2e2410` / `#e8b800` / `#ffe082` | 5.9:1 / 11.8:1 |
| `--error-*` | `#fdeaea` / `#c62828` / `#8b0000` | `#2d1414` / `#e57373` / `#ef9a9a` | 8.6:1 / 8.0:1 |

Key decisions:
- **Success is lime-olive, not a new forest green.** Access Lime `#c4d82e` stays the "staff tools" signal and fails text contrast, so success reuses the `.seg-positive` lime-olive with the border tuned off-yellow (`#6b8e1e`) to read as success, not brand accent.
- **Reuse over invention** — info = `.seg-neutral` navy (darker than `--link` so it isn't read as a link); warning = the abstract version-warning amber; error = `--danger` red.
- **Color is never the sole signal** — each variant pairs with a distinct icon shape + leading word (WCAG 1.4.1), so the states survive grayscale and `forced-colors` mode.
- **OS signals honored** — `prefers-color-scheme` (dark tokens), `forced-colors` (links → `LinkText`, never `forced-color-adjust:none`), `prefers-reduced-motion`. `prefers-contrast` needs nothing (all pairings clear AA).

Deferred: a **toast** pattern (transient/positioned/animated) and an **action-button slot** (Retry / Undo) on alerts.

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
- [x] Secondary button dark mode: `color: var(--lime)` in dark mode block — no new token needed
- [x] Focus ring: `#1565c0` light / `#64b5f6` dark — documented and committed
- [x] Visited link colors confirmed: `#7b2fbe` light / `#c084e0` dark
- [x] Dark mode icon button variants (constructive lime border, destructive red border)
- [x] **Data table** (`.ds-table`) — base styles, header row, hover, footer
- [x] **Sortable headers** (`.sortable`, `.sort-asc`, `.sort-desc`, `.sort-arrow`) — clickable columns with direction indicators
- [x] **Filter select** (`.ds-filter`) — underline-only select with custom chevron for toolbar filters
- [x] **Segmented control** (`.seg-control`, `.seg-btn`) — exclusive-choice button group with positive/neutral/negative active variants
- [x] **Toggle switch** (`.toggle-switch`, `.toggle-track`, `.toggle-thumb`, `.toggle-label`) — boolean on/off with lime-green checked state
- [x] **Form validation** (`.field-required`, `.is-invalid`, `.field-error`) — required indicators, invalid border/ring, inline error messages
- [x] **WCAG AA audit** — added `--grey-ui` (`#8b8680`, 3.61:1 on white) to fill palette gap between `--grey-dis` (2.24:1) and `--grey` (5.83:1). Updated toggle track, toggle off-label, sort arrow, filter underline, seg control border, icon button border, and info card label to pass 3:1 UI / 4.5:1 text thresholds
- [x] **Status / alert colors + `.ds-alert`** — four-state semantic palette (success/info/warning/error) and a token-driven alert banner, light + dark, with `forced-colors` / `prefers-reduced-motion` handling. Mirrored into the public stylesheet. See "Decisions made — Status / alert colors" above

---

## Key brand colors for reference

| Name | Hex |
|---|---|
| Repository Brown | `#1c1a17` |
| Dark Surface (cards) | `#252320` |
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
