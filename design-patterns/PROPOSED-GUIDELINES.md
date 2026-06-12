# Proposed Guidelines — for universality review

**Status: PROPOSED, not policy.** These are rules the validated patterns already *embody* but that exist nowhere in writing. Each was extracted during component codification (2026-06-11, reader-header pass) with its evidence and an honest open question about whether it generalizes. Review each; the ones that hold should move into `DESIGN-POLICIES.md` (hard constraints) or the relevant pattern docs (component conventions); the ones that don't should be marked pattern-local so nobody mistakes them for policy.

---

## G1. Sticky chrome must set a global scroll offset

**Rule:** Any page with sticky chrome sets `html { scroll-padding-top }` to at least the chrome's tallest state plus breathing room (reader reference: 80px for a 52px/36px header). Applies to every anchor path — native `#fragment` jumps, TOC clicks, JS `scrollIntoView`, browser back/forward.

**Evidence:** the single most-filed bug class in html_feedback — 12+ independent filings of "clicked a reference, landed under the header" (#244, #2620, #2752, #1988, #2801, #4464, #1058, #3886, #2430, #2146, #320, #6513), still recurring in the open queue (#1285, #3709, #5217). One CSS rule closes the class.

**Open question:** none worth debating — this is the strongest candidate for DESIGN-POLICIES.md as written. The only nuance: pages with *taller* sticky chrome (future variants) must scale the value; consider expressing it as a token (`--arxiv-scroll-offset`).

## G2. Chrome recedes on content-first surfaces

**Rule:** The deeper the user is into content, the quieter the chrome. Two mechanisms: (a) surface-level — content-destination pages (reader) use light chrome (Card Grey) where wayfinding pages (abstract) use dark (Repository Brown); (b) state-level — chrome compacts after the user commits to reading (52px → 36px past the abstract), trading identity (full wordmark) for space while keeping every affordance reachable (icons remain; nothing is removed, only de-emphasized).

**Evidence:** "roughly half of 107 closed UX issues boil down to 'your interface is in my way'" (closed-issue synthesis); the banner/report-button/header-height complaints all reduce to chrome cost. The compact state is the designed answer.

**Open question:** is the two-tone surface rule (dark = wayfinding, light = reading) universal, or specific to the abstract/reader pair? Listings and search pages will force the question — recommend deciding *before* designing those.

## G3. One compact grammar — narrow viewports reuse the compact state

**Rule:** The narrow-viewport treatment of chrome reuses the *same* condensed visual mode as the scrolled-compact state (mini logomark, label-less icon nav, tighter padding) rather than introducing a third mode (e.g., hamburger). A user who knows one knows both. Exception: an element whose entire purpose is its label (the TOC trigger's "you are here") keeps the label everywhere.

**Evidence:** reader header ≤700px. Also implicitly the abstract header, which wraps rather than hamburgers (with the added rationale: no JS dependency, all items visible, voice-control labels intact). The responsiveness audit suggested a hamburger for the abstract page at ≤414px — that suggestion conflicts with this guideline; resolve deliberately.

**Open question:** does this survive pages with more nav items? The rule works at 4–5 items; a future page with 8 may genuinely need a disclosure menu. Suggested resolution: cap visible nav items rather than abandon the grammar.

## G4. The arXiv-layer surface family shares one tint vocabulary

**Rule:** Every "arXiv-added interactive surface" over paper content — citation popovers, footnote popovers, TOC dropdown, inline active states — draws from the same three-token family: `--arxiv-tint-light` (panel surface), `--arxiv-tint-border` (panel edge), `--arxiv-active-bg` (active/hover wash). Reader-recognizable rule: "light blue = arXiv chrome speaking, not the paper."

**Evidence:** already consistent across four components in the reader; this is what makes the added layer feel like one system rather than accumulated widgets.

**Open question:** strong candidate, but needs a dark-mode counterpart family before it can be policy (currently light-only). Also decide whether the *abstract* page's interactive surfaces (cite panel uses tint-border) are bound by it.

## G5. Z-layer scale

**Rule:** A fixed, documented z-index scale instead of ad-hoc values: content chrome (pills, marginalia) below 50 · popovers 50 · header-attached dropdowns 60 · sticky headers 100 · skip link / overlays 200 · modal dialogs use the native `<dialog>` top layer (no z-index at all — this is *why* the lightbox and report modal use native dialogs).

**Evidence:** the open-queue figure complaints included four z-index stacking failures (#522, #3119, #3147, #5760) — the entire class is structural once modals live in the top layer. The mockups already follow this scale implicitly.

**Open question:** none substantive; just confirm the bands leave room (e.g., toasts/notifications would slot at ~150).

## G6. Touch-target floor and the negative-margin technique

**Rule:** In any full-screen or touch-primary surface, interactive items have a ≥44px hit area (WCAG 2.5.5 best practice; 2.5.8 minimum is 24px). Where the *visual* design wants a smaller mark (the dropdown close ×), expand the hit area with padding + compensating negative margin so layout is unchanged.

**Evidence:** TOC full-screen list items (44px min-height), close button (negative-margin expansion), Labs toggles noted touchable in the responsiveness audit.

**Open question:** adopt 44px as the *target* with 24px as the hard floor, or mandate 44px outright? Mandating 44px everywhere conflicts with dense inline affordances (citation chips are exempt as inline-text links under WCAG's own exception) — the guideline should name the exemption explicitly.

## G7. Motion is an enhancement; reduced-motion gates *all* of it

**Rule:** Every animated property (CSS transitions, the progress fill, header height changes, chevron rotation) and every JS-driven motion (`scrollIntoView({behavior:'smooth'})`) is disabled under `prefers-reduced-motion: reduce`. CSS media queries do not catch JS scrolling — JS must check `matchMedia` per call.

**Evidence:** the reader's reduced-motion blocks + the smooth-scroll gating added 2026-06-11. The JS half of this rule is the part teams forget; it belongs in DESIGN-POLICIES.md next to the existing `:focus-visible` rule.

**Open question:** none — candidate for policy as written.

## G8. Enhancement never carries content (progressive enhancement)

**Rule:** The server-rendered HTML is complete and readable before any JavaScript runs. Scripts add conveniences (popovers, dropdowns, compact states, lightboxes); they never carry content. Concretely: anything hidden pending a JS reveal is hidden under an `html.js` scope; controls that do nothing without JS are hidden without it; controls with a meaningful non-JS equivalent degrade to it (search button → search-page link).

**Evidence:** the 2026-06-11 no-JS audit (footnotes were invisible without JS — now inline; hidden authors unreachable — now shown; dead search button — now a link). Coornaert browses with JS off by choice; low-bandwidth users get it off by circumstance.

**Open question:** none on substance — this is already de-facto policy across both mockups and the harness enforces parts of it. Recommend promoting to DESIGN-POLICIES.md so production teams inherit it explicitly.

## G9. Passive orientation indicators stay silent for AT

**Rule:** Continuously-updating orientation chrome (current-section label, reading-progress bar, "N min left") must not announce on update — no `aria-live` on scroll-driven values. AT users get equivalent orientation from structural navigation (headings, landmarks) and can poll the progressbar's `aria-valuenow` on demand. Announce-on-update is reserved for user-initiated changes (e.g., "Copied!").

**Evidence:** reader header (trigger label and progress are silent; the zoom-level readout in the lightbox *does* announce because zooming is user-initiated). This distinction — *who caused the change* decides announcement — is the generalizable principle.

**Open question:** verify the user-initiated/ambient distinction against real screen-reader user preference in the next AT testing round before making it policy.

## G10. Truncation always signals continuation

**Rule:** When content is cut by a scrollable or collapsed region, the cut must be visible as such: a fade mask at the cut edge ("scroll for more"), an explicit count on the control ("show all 1,247 authors"), or both. Never a hard clip that looks like the end. Corollary: every scrollable region is keyboard-reachable (`tabindex="0"` + accessible name) — axe flagged exactly this on the citation boxes.

**Evidence:** TOC mobile list fade mask; the 100+ author region (count + bounded scroll + collapse at both ends); the equation-number sticky fix (the *number* no longer vanishes when the equation overflows).

**Open question:** the fade-mask technique uses `mask-image` (good support, but verify in forced-colors mode where masks can hide the affordance entirely). The principle is sound; the technique needs an HCM fallback note.

---

## Suggested dispositions (for the review discussion)

| # | Proposal | Suggested home |
|---|---|---|
| G1 | Scroll offset under sticky chrome | DESIGN-POLICIES.md (hard constraint) |
| G2 | Chrome recedes | Pattern doc (needs the surface-rule decision first) |
| G3 | One compact grammar | Pattern doc; resolve the hamburger question explicitly |
| G4 | arXiv-layer tint family | color-mapping.md after dark-mode counterpart exists |
| G5 | Z-layer scale | DESIGN-POLICIES.md (small, mechanical, prevents drift) |
| G6 | Touch-target floor + exemptions | DESIGN-POLICIES.md with the inline-link exemption named |
| G7 | Reduced-motion incl. JS scrolling | DESIGN-POLICIES.md (extends the existing a11y section) |
| G8 | Progressive enhancement | DESIGN-POLICIES.md (already de-facto; make it explicit) |
| G9 | Silent ambient indicators | Hold for AT-testing validation |
| G10 | Truncation signals continuation | Pattern doc; add HCM note |
