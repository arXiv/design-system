# arXiv Shared Design System — Progress Notes
**Project:** Admin Console + arXiv Check shared component library
**Last updated:** 2026-03-16

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

## What is still pending

### Longer term (open questions)
- [ ] **Visited link hover state** — what color when you hover a visited link? Darken the purple, or reset to default blue?
- [ ] **Form input base styles** — text inputs, checkboxes, radio buttons, full select styling (beyond filter select)
- [ ] **Modal / dialog pattern** — backdrop, container, footer button grouping
- [ ] **Dark mode** for new components — tables, segmented control, filter select, validation states

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
