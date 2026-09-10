# Dark / Light Theme — Audit & Decision Doc

**Status:** Draft for review — 2026-05-28. No code yet; this is the plan to agree on first.
**Scope:** Both stylesheets (`docs/design-system.css`, `docs/internal/internal-tools.css`).

---

## 1. Goal

A real, switchable light/dark theme: **OS-driven by default**, but **user-overridable** with a manual toggle that works on any OS. Today dark mode is OS-only (`@media prefers-color-scheme`), there's no working manual override, and coverage is partial.

---

## 2. Current dark-mode coverage (audited from the CSS)

| Surface | Component | Dark status | Notes |
|---|---|---|---|
| Internal | Token palette (lime, grey, danger, link, status) | ✅ has dark values | The foundation is solid |
| Internal | Buttons (primary/secondary/tertiary/destructive/link) | ✅ | Token-driven + a secondary-text override |
| Internal | Icon buttons (constructive/destructive) | ✅ | Explicit dark overrides |
| Internal | Info card | ✅ | Explicit dark override |
| Internal | **Alerts** (`.ds-alert`) | ✅ | Dark tokens (this session) |
| Internal | Form validation | ✅ | Token-driven (`--ds-danger`) |
| Internal | Type badges | ❌ | Hardcoded light fills (`#d4e9ff`, `#fef3c7`…) — glaring on dark |
| Internal | **Data table** | ❌ | Hardcoded `#fff` / `#f0eeec` / `#ddd8d2` — white table on a dark page |
| Internal | **Segmented control** | ❌ | Hardcoded `#fff` surface; active variants duplicate the alert palette |
| Internal | Filter select | ⚠️ | Token border, but hardcoded text colors |
| Internal | Sortable headers | ⚠️ | Mostly token; `#1c1a17` hardcoded |
| Internal | Toggle switch | ⚠️ | Token track; `#fff` thumb + dark-text checked label need attention |
| Public | **Alerts** (`.ds-alert`) | ✅ | The *only* dark-aware tokens on public |
| Public | All other `:root` tokens | ❌ | ~14 brand/surface tokens have no dark values |
| Public | **Buttons** (`.ds-btn`) | ❌ | Hardcoded gradient + vignette + shadow — needs a dark *redesign*, not a swap |
| Public | inline-active / annotation / popover | ⚠️ | Token-driven → will flip once public tokens get dark values |
| Public | Element pill | ❌ | Hardcoded `#fff` |

Legend: ✅ ready · ⚠️ partly token-driven, flips once tokens/surfaces are sorted · ❌ hardcoded light, breaks on dark.

---

## 3. The real blocker isn't color — it's tokenized surfaces

The dark *values* mostly exist. What's missing is that the ❌/⚠️ components **hardcode** surfaces, borders, and text (`#fff`, `#f0eeec`, `#ddd8d2`, `#1c1a17`, `#6b6459`) instead of consuming tokens — so there's nothing to flip.

**Proposal: a small semantic surface-token layer** that both stylesheets adopt and that flips in dark. Indicative values (dark values from the chrome we already use in the demo pages):

| Token | Light | Dark | Replaces hardcoded |
|---|---|---|---|
| `--ds-surface` | `#ffffff` | `#252118` | table/seg/pill `#fff` |
| `--ds-surface-muted` | `#f0eeec` | `#302c28` | table `th`, hover fills |
| `--ds-surface-hover` | `#faf9f8` | `#2a2520` | row/seg hover |
| `--ds-border` | `#ddd8d2` | `#3a3530` | table/footer borders |
| `--ds-text` (exists) | `#1c1a17` | `#f0eeec` | body/cell text |
| `--text-muted` (≈`--ds-text-muted`) | `#6b6459` | `#b0aba6` | labels, footer |

Once components consume these, ~all of the ❌/⚠️ internal components and the var-driven public components convert almost mechanically. (Bonus: the segmented control's active variants duplicate the alert palette — they can be re-pointed at the `--success/info/error` status tokens.)

---

## 4. Decision A — the toggle mechanism

| Option | Pro | Con |
|---|---|---|
| **A. `light-dark()` + `color-scheme`** | No duplication; OS *and* manual override for free; one value pair per token | Browser floor ~2024 — risky for arXiv's long-tail audience, especially public pages |
| **B. `@media` + `[data-theme]` dual-selector** | Universal browser support | Duplicates the dark token block (~40 lines), kept in sync by hand |

**Recommendation:** **B**, for compatibility with arXiv's broad/old browser base — keep the duplication contained to the one token block with a sync comment. Revisit `light-dark()` later if/when we're comfortable setting a browser floor (it could land internal-first, since staff browsers are more controlled).

---

## 5. Decision B — public button dark treatment (design work, not a swap)

The public button's "lit-from-above" gradient + inner vignette + drop shadow is hardcoded and tuned for light. Dark needs a deliberate equivalent: darker fills, re-aimed gradient, and a shadow that reads on a dark surface. This is the one genuinely *new* color/design decision still open. Everything else is tokenization.

---

## 6. Other (non-color) decisions

- **Toggle UX:** where the control lives on real pages (header? footer?), and its iconography. (The demo pages don't need it — they're OS-driven.)
- **Persistence & precedence:** default to OS, allow override, remember via `localStorage`; explicit choice beats OS.
- **Rollout order:** internal first (staff, fewer browsers, more components already done) then public? Or both together?

---

## 7. Proposed phasing

- **Phase 0 (this doc):** agree the mechanism (Decision A), the surface-token layer (§3), and the public-button approach (Decision B).
- **Phase 1:** add the surface-token layer + the chosen opt-in mechanism; convert the token-izable components (internal: table, seg, filter, toggle, badges, sortable; public: give the `:root` tokens dark values + tokenize element-pill, which flips popover/annotation/inline-active too). Verify against the `alert-styles.html` demo pattern.
- **Phase 2:** the public button dark redesign; the toggle UI + persistence; a final audit pass for anything missed.

---

## 8. Bottom line

Feasible to start now. The color foundation is mostly there; the work is (1) a surface-token layer so hardcoded components can flip, (2) picking the opt-in mechanism, and (3) one real design decision (the public button). Not a one-pass job — but Phase 1 is well-scoped and unblocks a working toggle plus most of the coverage.
