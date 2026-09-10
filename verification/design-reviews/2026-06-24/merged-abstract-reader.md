# Design system review: merged abstract + HTML reader mockup

**Context:** public · source review (`design-system/mockups/public/merged-abstract-reader.html`)
**Reviewed against:** `design-system/` @ master
- [`DESIGN-POLICIES.md`](../../../docs/DESIGN-POLICIES.md)
- [`docs/public/design-system.css`](../../../docs/public/design-system.css)
- [`docs/buttons.html`](../../../docs/buttons.html)
- [`docs/color-mapping.md`](../../../docs/color-mapping.md)
- [`docs/typography.md`](../../../docs/typography.md)
- [`BRAND.md`](../../../docs/BRAND.md)
- [`CLAUDE.md`](../../../CLAUDE.md) (guardrails)

## Summary

The merged page is **largely compliant on brand foundations** (IBM Plex throughout, palette tokens for most colors, proper landmarks, `:focus-visible`, semantic markup, BibTeX/APA/Chicago/MLA per policy, no metrics, real `.ds-site-footer`). **Drift is concentrated in components**, not tokens or a11y primitives: the page reimplements primary button, skip link, TOC trigger, site header (3-col override), and the Labs section as custom `.mg-*` classes instead of reusing the canonical `.ds-*` patterns. Four specific policy violations need fixing — touch-target floor on the citation Copy button, a missing reduced-motion guard, the toggle on-state color override needing documentation, and sticky chrome on a non-reader surface (abstract mode).

The user-flagged button drift (Download PDF not matching `buttons.html`) is real and is one of several places where the merged page diverged from the canonical patterns during iteration. The fix path is to reconcile those components back to the design system, and where the merged page genuinely needs new patterns (the Reader-view toggle, the mid-page sticky TOC bar), to codify them into `docs/public/` rather than continuing to live as page-local `.mg-*` styles.

---

## Blocking — accessibility & policy violations

### A. Touch target below WCAG 2.5.8 hard floor — citation Copy button
- **Where:** `mockups/public/merged-abstract-reader.html` — `.mg-cite-copy`
  - styles: `padding: 3px 8px;` + `font-size: 0.72rem` (~11.5px) → visible button is ~17×40px.
- **Policy:** `DESIGN-POLICIES.md` → Chrome and interaction structure:
  > "Hard floor 24×24 CSS px (WCAG 2.2 SC 2.5.8 AA), with WCAG's own exceptions (inline targets within a sentence — citation chips, version links — spacing-equivalent, user-agent defaults). … Use the padding + negative-margin technique to grow hit areas without changing layout."
- **Why it matters:** The Copy button is NOT an inline target — it's a standalone control sitting in the code block's corner. The hard floor applies. A touch user can't reliably hit a 17px-tall button.
- **Fix:** Increase padding so the visible target reaches ≥24×24 (or 44×44 for touch-primary):
  ```css
  .mg-cite-copy { padding: 6px 12px; font-size: 0.78rem; }
  ```
  Or keep the small visible chrome and grow the hit area via padding + negative margin:
  ```css
  .mg-cite-copy { padding: 8px 12px; margin: -2px -3px; }
  ```

### B. No `prefers-reduced-motion` handling for injected transitions
- **Where:** `.mg-reader-toggle .tk` (track slide), `.mg-reader-toggle .tk::after` (knob slide), `.mg-toc-bar` (background fade on stuck), `.mg-toc-trigger .toc-chev` (chevron rotate), and several others have `transition:` declarations.
- **Policy:** `DESIGN-POLICIES.md` → Chrome and interaction structure:
  > "Reduced motion covers JavaScript. `prefers-reduced-motion: reduce` must disable ALL motion: CSS transitions/animations AND JS-driven motion."
- **Why it matters:** Users with vestibular sensitivity get unwanted motion — toggle slide, sticky-bar background fade, chevron rotation. Other parts of the file honor this (10 `prefers-reduced-motion` rules elsewhere), but **my injected `.mg-*` block has zero**.
- **Fix:** Add a guard block at the end of the `mg-merge-styles` block:
  ```css
  @media (prefers-reduced-motion: reduce) {
    .mg-reader-toggle .tk, .mg-reader-toggle .tk::after,
    .mg-toc-bar, .mg-toc-trigger .toc-chev,
    .mg-labs-track, .mg-labs-track::after,
    .mg-cite-copy { transition: none !important; }
  }
  ```

### C. Toggle on-state color violates the documented toggle pattern
- **Where:** `.mg-reader-toggle[aria-pressed="true"] .tk { background: var(--arxiv-open-blue); }` and the same color used for `.mg-labs-toggle input:checked + .mg-labs-track`.
- **Policy:** `DESIGN-POLICIES.md` → Content and interaction:
  > "Toggle switches: Off state uses `--grey-ui`. On state uses lime green (internal) or **Link Blue** (public). Label text uses `--grey` (off) shifting to a darker shade (on)."
- **Why it matters:**
  1. Direct deviation from a written policy (Link Blue `#1565c0`, not Open Blue `#a5d6fe`).
  2. **Likely WCAG 1.4.11 contrast failure:** white circle on pale Open Blue track — non-text contrast for adjacent UI components must be ≥ 3:1. Open Blue is light enough that the white circle on the active track will fail. (Link Blue's `#1565c0` against white is 5.74:1 — well clear.)
- **Override context:** The user explicitly requested Open Blue for brand consistency on 2026-06-23 ("more on brand"). `CLAUDE.md` guardrails:
  > "Only proceed with a policy violation if the user explicitly acknowledges the conflict and confirms they want to override it. Document the override in a code comment explaining the exception."
- **Fix (choose one):**
  - **Revert to Link Blue** for both toggles. Active state would be `var(--arxiv-link-blue)`.
  - **Keep Open Blue** but add the override comment AND verify/fix contrast. Suggested comment:
    ```css
    /* Override 2026-06-23: Open Blue on-state per design decision to keep
       brand consistency across the page. Departs from DESIGN-POLICIES.md
       "Toggle switches" policy (Link Blue for public toggles). Contrast of
       circle vs track verified at X:1 (1.4.11 threshold 3:1). */
    ```

### D. Sticky chrome on a non-reader surface
- **Where:** `.mg-toc-bar { position: sticky; top: 0; z-index: 30; }` — sticky in BOTH abstract and reader modes.
- **Policy:** `DESIGN-POLICIES.md` → Chrome and interaction structure:
  > "Sticky chrome is exceptional. The HTML paper reader is the only surface approved to use a sticky header — it alone is a long-document reading context that earns persistent chrome. Do not add sticky chrome to other pages without explicit approval."
- **Why it matters:** The merged page in abstract mode is a new surface and shows the full paper inline (reader-like), so the case for sticky TOC is real — but the policy is conservative and currently lists "the HTML reader" as the sole approved surface.
- **Fix (choose one):**
  - Make the TOC sticky **only in reader mode**: `body.mg-reader .mg-toc-bar { position: sticky; }`, otherwise `position: static`. The TOC button still exists in abstract mode — it just doesn't follow the scroll.
  - **Or** document the merged page as a second approved sticky-chrome surface in `PROPOSED-GUIDELINES.md` (the merged page is a reader-first surface in spirit). Update DESIGN-POLICIES.md to match.

---

## Should fix — token / brand / component drift

### E. Primary button reimplemented instead of using `.ds-btn-primary`
*This is the user-flagged drift.*

- **Where:** `mockups/public/merged-abstract-reader.html` — `.mg-files-pdf` (the Download PDF button in the Files column).
- **What's missing vs `docs/buttons.html` + `design-system.css` `.ds-btn-primary` (line ~191):**

| Spec | Canonical `.ds-btn-primary` | This page's `.mg-files-pdf` |
|---|---|---|
| Border | `1.5px solid transparent` + dual-background gradient (border-box → padding-box) | flat `1px solid #6ba8da` |
| Fill | dual-background, gradient endpoints `#a5d6fe → #a5d6fe` (solid) | flat `var(--arxiv-open-blue)` |
| Inner vignette | `inset 0 0 6px rgba(31,94,150,0.20)` | none |
| Outer drop shadow | `0 1px 3px rgba(0,0,0,0.12)` | none |
| Padding | `10px 20px` | `8px 16px` |
| Font | `14px / 600` | `0.85rem / 600` (~13.6px) |
| Min-width | `120px` | none |
| Hover | brighten fill + deepen border + soften vignette | bg swap to `--arxiv-open-blue-bright` only |
| Press | `translateY(1px)` + flatten border + deeper vignette | none |
| Focus | `:focus-visible` → `outline: 3px solid var(--arxiv-focus-ring)` + 2px offset | inherits from `.mg-btn:focus-visible` (2px solid, offset 2) |

- **Why it matters:** `buttons.html` is the source of truth for primary actions on public pages. A user moving from `/abs` to the merged page sees a different "feel" for the same primary action. This is precisely the drift the user noticed.
- **Fix:** Replace the markup with the canonical class:
  ```html
  <a class="ds-btn ds-btn-primary" href="https://arxiv.org/pdf/2604.22725v1">
    Download PDF <small style="font-weight: 400; color: var(--arxiv-library-grey);">· 1.2&nbsp;MB</small>
  </a>
  ```
  Drop the `.mg-files-pdf` CSS block. Let `.ds-btn-primary` carry construction, hover, press, focus.

### F. Skip link doesn't use canonical `.ds-skip-link`
- **Where:** `.mg-skip-to-paper` (custom) injected after the abstract.
- **Two issues:**
  1. Custom styles instead of canonical `.ds-skip-link` (`design-system.css` line ~873).
  2. **Skip link must be the FIRST focusable element on the page** — per `design-system.css` behavior contract: *"The skip link (.ds-skip-link) is the FIRST focusable element on the page, visible only on keyboard focus."* My skip link is mid-DOM (after the abstract), not at the top of `<body>`.
- **Why it matters:** Keyboard users entering the page hit the announcement-close `×` first, then the header logo, then nav, then the abstract content, only THEN see the "Skip past document tools to paper content" link. By that point they've already passed the announcement and header. The skip link's purpose is to be reachable IMMEDIATELY on `Tab`.
- **Fix:**
  - Add a canonical skip link as the first child of `<body>`:
    ```html
    <a class="ds-skip-link" href="#main">Skip to main content</a>
    ```
    (Assumes `<main>` or `#main` exists — `.ltx_page_main role="main"` qualifies; give it `id="main"`.)
  - Optionally keep `.mg-skip-to-paper` as a **secondary** skip link before the band (a context-specific skip), but ALSO have the canonical first-focus skip link.

### G. Custom site header diverges from `.ds-site-header`
- **Where:** `mockups/public/merged-abstract-reader.html` overrides `.ds-site-header` to `display: grid; grid-template-columns: 1fr auto 1fr;` to add a center cell for the Reader-view toggle.
- **What's wrong:**
  1. Page-local CSS shadows a canonical design-system class — future updates to `.ds-site-header` won't propagate cleanly.
  2. The Reader-view toggle in the header center adds visual prominence to a mode-switcher inside the universal header. Policy:
     > "Universal navigation stays short. The header nav is capped at its current five items (Search, Submit, Donate, Log in + logo). Resist link-creep permanently."
     The toggle isn't a nav item exactly, but it's chrome that the canonical pattern doesn't include.
- **Fix (two options):**
  - **(a)** Define a new pattern `.ds-merged-header` (or `.ds-site-header--with-toggle` modifier) and codify it in `docs/public/` so the divergence is documented, not shadowed.
  - **(b)** Move the Reader-view toggle out of the universal header to a separate sticky chrome row (similar to the TOC bar) so the universal header stays exactly as `.ds-site-header` defines it.

### H. Custom TOC ignores canonical `.ds-toc-trigger` / `.ds-toc-dropdown`
- **Where:** `.mg-toc-trigger` and `.mg-toc-dropdown`.
- **What's wrong:** The reader has a full TOC system in `design-system.css` (`.ds-toc-trigger` ~line 1282; `.ds-toc-dropdown` ~line 1334) with documented behavior contract. My TOC is a separate implementation styled similarly but with different classes.
- **Why this matters:** Two TOC implementations means two places to maintain visual, behavior, accessibility, and the touch-target/contrast spec. The pattern is established.
- **Fix:** Either
  - **Reuse the canonical classes** (`.ds-toc-trigger` + `.ds-toc-dropdown` + the surrounding JS pattern), OR
  - If my centered/sticky placement is genuinely a different pattern, **extract a new `.ds-toc-bar`** to `docs/public/design-system.css` and document it.

### I. Labs section duplicated as `.mg-labs-*` instead of canonical `.ds-labs-*`
- **Where:** `mockups/public/merged-abstract-reader.html` `.mg-labs-*` styles + markup, copy of `abstract-redesign.html` `.abs-labs-*`.
- **Current state:** The same Labs pattern (grouped toggle list + content area + "What are arXiv Labs?" footer) now exists in:
  - `mockups/public/abstract-redesign.html` as `.abs-labs-*`
  - `mockups/public/merged-abstract-reader.html` as `.mg-labs-*`
  - NOT in `design-system.css` (no `.ds-labs-*`)
- **Policy:** `DESIGN-POLICIES.md` → Components:
  > "New patterns: If a UI element appears in two or more pages, extract it into a design system CSS file and create or update a pattern page in `docs/`."
- **Fix:** Extract `.ds-labs-layout` / `.ds-labs-toggle` / `.ds-labs-content` / etc. to `design-system.css`, create `docs/public/labs-styles.html`, and update both mockups to consume the shared classes.

### J. `z-index` for sticky TOC bar doesn't match the documented scale
- **Where:** `.mg-toc-bar { z-index: 30; }`.
- **Policy:** `DESIGN-POLICIES.md` → Chrome and interaction structure:
  > "Z-layer scale. Content chrome (pills, marginalia) < 50 · popovers 50 · header-attached dropdowns 60 · **sticky headers 100** · ~150 reserved for toasts/notifications · skip link/overlays 200 · modal dialogs use the native `<dialog>` top layer (no z-index)."
- **Why it matters:** The TOC bar is functionally sticky header chrome. At `z-index: 30` it's in the "content chrome" tier; sticky headers belong at 100. (`.arxiv-html-header` in the same file is at 100 — consistent.) The TOC dropdown at `z-index: 40` is OK as a "header-attached dropdown" (60 per policy — slightly low but not wrong-tier).
- **Fix:**
  ```css
  .mg-toc-bar { z-index: 100; }      /* sticky chrome tier */
  .mg-toc-dropdown { z-index: 110; } /* attached dropdown above its own bar */
  ```

### K. Palette literals where tokens exist
- **Where (in the `mg-merge-styles` block):**
  - `#4a5a0a` — A11y "present" text color → use `var(--arxiv-success-fg)`
  - `#6b8e1e` — A11y "present" icon color → use `var(--arxiv-success-border)`
  - `#a5d6fe` — Open Blue (appears in `.mg-cite-copy.is-copied`, button bgs) → use `var(--arxiv-open-blue)`
  - `#6ba8da`, `#7eb8e0` — button-gradient stops; per `color-mapping.md` these are Tier-2 component-internal constants, OK as literals **inside the component's own CSS** but my file uses them in two unrelated places now (`.mg-files-pdf` and `.mg-labs-track`) — once `.ds-btn-primary` and `.ds-labs-*` are reused (findings E + I), these should disappear.
  - `#2a2723`, `#3a3631` — custom dark surfaces for the Reader-view toggle on the black header. **Not in the palette.** Per `color-mapping.md` tier rules: "Tier 3 — everything else doesn't exist." Either:
    - (a) Accept as Tier-2 component-internal constants and document the choice in `color-mapping.md`.
    - (b) Replace with an existing palette step. No good fit currently — the palette doesn't carry a "Repository Brown one step lighter" step.

### L. Reader file is missing a `display: none` default for `.eqn-tex-view`
- **Where:** Not drift in MY merged page — drift in the reader file itself.
- **What this is:** `design-system/mockups/public/html-redesign.html` (line ~2032) defines `.eqn-tex-view` typography but lacks a default `display: none`. The toggled-on rule (`.eqn-region.show-tex .eqn-tex-view { display: block }`) is incomplete. Without the default-hide, `<pre class="eqn-tex-view">` falls back to the browser's default `display: block` and the TeX source rendered under every one of the 99 equations.
- **Where I worked around it:** `mockups/public/merged-abstract-reader.html` adds `.eqn-tex-view { display: none; }` as a defensive rule.
- **Recommendation:** Push the default-hide into `mockups/public/html-redesign.html` itself so all reader-derived work inherits it. Then remove the defensive rule from the merged page.

---

## Consider — minor / stylistic

These are notes, not policy violations.

- **Cite Copy button placement at small widths:** the absolute-positioned button overlaps the `@article{` opening line of the citation code. At ≤390px it covers part of the first line. Moving it to the Cite header row (right of the dropdown) would avoid overlap, but cost the convenient "always at the code block's corner" affordance.
- **Class name `mg-ext`:** used for the external-link icon inside Labs. A clearer name like `mg-ext-icon` would scan better in markup search.
- **A11y heading capitalization:** my h3 is "Accessibility notes" (sentence case); the canonical convention in this repo elsewhere uses Title Case. Verify against `abstract-redesign.html` and align.
- **`.mg-reader-toggle` visual:** the dark fill (`#2a2723`) on the black header has very low contrast with the header bg (`#1c1a17`) — intentional ("subtle, doesn't signal state"), but a person used to the standard arXiv header chrome might initially miss it. Worth user-testing.

---

## Compliant — worth noting

So you know these were checked, not skipped:

- **Typography:** every `font-family` uses `var(--arxiv-font-*)` tokens; no Times/Arial fallbacks introduced. ✓
- **Fonts self-hosted:** no Google Fonts, no Typekit, no external font services. ✓
- **`:focus-visible` (not `:focus`):** my injected CSS uses `:focus-visible` consistently (28 uses across the file, no problematic `:focus` rules I authored). ✓
- **Color palette compliance (mostly):** Repository Brown for ink, Card Grey for code blocks, Warm Wash for tints, Open Blue for hover steps, Light blue family for arXiv-chrome surfaces — all via tokens. (Literals flagged in finding K.)
- **Landmarks & headings:** `<aside aria-label="Document tools and metadata">` for the tinted band, h3 column headers (Cite / Files / Accessibility notes), h1 paper title from LaTeXML, h2 sections from LaTeXML. ✓
- **Citation export formats:** BibTeX (default) + APA + Chicago + MLA, generated from data, per policy. ✓
- **No metrics displayed:** no view/download/citation counts. ✓
- **Footer:** canonical `.ds-site-footer` markup (acknowledgment, links, Simons + Schmidt funders). ✓
- **`scroll-padding-top: 80px`:** set globally for sticky-header anchor targets, per policy. ✓
- **Status colors map to the right family:** greens for A11y "present" map to the `--arxiv-success-*` palette (even if as literals — see finding K). ✓
- **Announcement banner:** glyph + short sentence + Learn-more link + dismiss button, per policy. ✓
- **Tinted band reaches viewport edge:** earlier review found this; fix is in place via `width: 100vw` + symmetric negative margins + `.ltx_page_content { margin-right: 0 !important }` override. ✓

---

## Suggested fix order (most impactful first)

1. **(A)** Grow the citation Copy button to ≥24×24 — 1-line CSS change, blocking accessibility issue.
2. **(B)** Add a `prefers-reduced-motion` guard — 5-line CSS block, blocking policy.
3. **(E)** Replace `.mg-files-pdf` with `.ds-btn-primary` — restores brand consistency on the page's primary action (the user-flagged issue).
4. **(F)** Add canonical `.ds-skip-link` as the first focusable element on the page.
5. **(C)** Decide on toggle on-state (Link Blue vs Open Blue + documented override); whichever, add the explanatory comment.
6. **(D)** Decide sticky-TOC scope (reader-mode only, or document the merged page as a new approved sticky-chrome surface in `PROPOSED-GUIDELINES.md`).
7. **(J)** Fix `z-index` for the sticky TOC bar (one-line change).
8. **(K)** Swap the four palette literals to tokens (`#a5d6fe`, `#4a5a0a`, `#6b8e1e`).
9. **(I, H, G)** Larger reconciliation work: extract `.ds-labs-*`, reconcile TOC, decide site-header modifier vs new pattern.
10. **(L)** Push the `.eqn-tex-view { display: none }` default into the reader file itself.
