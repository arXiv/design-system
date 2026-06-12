# Proposed Guidelines — for universality review

**Status: PROPOSED, not policy.** These are rules the validated patterns already *embody* but that exist nowhere in writing. Each was extracted during component codification (2026-06-11, reader-header pass) with its evidence and an honest open question about whether it generalizes. Review each; the ones that hold should move into `DESIGN-POLICIES.md` (hard constraints) or the relevant pattern docs (component conventions); the ones that don't should be marked pattern-local so nobody mistakes them for policy.

---

## G1. Sticky chrome must set a global scroll offset

**Rule:** Any page with sticky chrome sets `html { scroll-padding-top }` to at least the chrome's tallest state plus breathing room (reader reference: 80px for a 52px/36px header). Applies to every anchor path — native `#fragment` jumps, TOC clicks, JS `scrollIntoView`, browser back/forward.

**Evidence:** the single most-filed bug class in html_feedback — 12+ independent filings of "clicked a reference, landed under the header" (#244, #2620, #2752, #1988, #2801, #4464, #1058, #3886, #2430, #2146, #320, #6513), still recurring in the open queue (#1285, #3709, #5217). One CSS rule closes the class.

**Resolved 2026-06-11 (Shamsi):** promoted to DESIGN-POLICIES.md, with a sharper framing: **sticky chrome is exceptional at arXiv.** The HTML reader is intended to be the *only* page with a sticky header — arXiv is not a complex site (discovery, documentation, account, submission, and papers), and only the long-document reading surface earns persistent chrome. The policy therefore covers both halves: don't add sticky chrome elsewhere without explicit approval; where it exists, the scroll-offset rule applies.

**Flag raised during review:** the abstract-page mockup and the codified `.ds-site-header` currently use `position: sticky` — contradicting the reader-only intent. Needs a decision: keep it sticky (then the abstract page is a second sticky-chrome page and inherits the scroll-offset duty) or make it static (consistent with the stated view; also returns ~52px of mobile viewport). See the discussion note in DESIGN-POLICIES.md.

## G2. Chrome recedes on content-first surfaces

**Rule:** The deeper the user is into content, the quieter the chrome. Two mechanisms: (a) surface-level — content-destination pages (reader) use light chrome (Card Grey) where wayfinding pages (abstract) use dark (Repository Brown); (b) state-level — chrome compacts after the user commits to reading (52px → 36px past the abstract), trading identity (full wordmark) for space while keeping every affordance reachable (icons remain; nothing is removed, only de-emphasized).

**Evidence:** "roughly half of 107 closed UX issues boil down to 'your interface is in my way'" (closed-issue synthesis); the banner/report-button/header-height complaints all reduce to chrome cost. The compact state is the designed answer.

**Clarified 2026-06-11 (Shamsi):** the reader's light header is intentional — it visually ties the HTML version to the PDF version of the paper, supporting the co-equal-formats accessibility goal (decided several years ago, when the aim was to stop being PDF-first with HTML as a second-class citizen). Keep as pattern rationale, not yet universal policy; listings/search will test the broader two-tone rule.

**Strategic question recorded (not decided):** is it time to reconsider co-equal and set an HTML-first goal, with PDF as the second-class citizen? Raised by Shamsi as food for thought 2026-06-11. This would touch the reader's visual identity, the abstract page's action ordering (HTML already listed first), and the accessibility-priorities framing — a leadership/team conversation, not a design-system decision.

## G3. One compact grammar — narrow viewports reuse the compact state

**Rule:** The narrow-viewport treatment of chrome reuses the *same* condensed visual mode as the scrolled-compact state (mini logomark, label-less icon nav, tighter padding) rather than introducing a third mode (e.g., hamburger). A user who knows one knows both. Exception: an element whose entire purpose is its label (the TOC trigger's "you are here") keeps the label everywhere.

**Evidence:** reader header ≤700px. Also implicitly the abstract header, which wraps rather than hamburgers (with the added rationale: no JS dependency, all items visible, voice-control labels intact). The responsiveness audit suggested a hamburger for the abstract page at ≤414px — that suggestion conflicts with this guideline; resolve deliberately.

**Resolved 2026-06-11 (Shamsi):** the universal navigation stays deliberately short — the cap is the policy, and link-creep into the header will be resisted over time. A hamburger remains a permitted *fallback* at very narrow viewports if the short nav still doesn't fit, but is never the default pattern. Recorded in DESIGN-POLICIES.md.

## G4. The arXiv-layer surface family shares one tint vocabulary

**Rule:** Every "arXiv-added interactive surface" over paper content — citation popovers, footnote popovers, TOC dropdown, inline active states — draws from the same three-token family: `--arxiv-tint-light` (panel surface), `--arxiv-tint-border` (panel edge), `--arxiv-active-bg` (active/hover wash). Reader-recognizable rule: "light blue = arXiv chrome speaking, not the paper."

**Evidence:** already consistent across four components in the reader; this is what makes the added layer feel like one system rather than accumulated widgets.

**Resolved 2026-06-11 (Shamsi):** keep as a working rule and good goal; expect it to grow and flex as more pages apply it in new contexts. Dark-mode counterpart deliberately deferred until light mode is further along (avoid duplicating work — consistent with dark-mode-decision). Revisit for policy promotion when the dark family exists.

## G5. Z-layer scale

**Rule:** A fixed, documented z-index scale instead of ad-hoc values: content chrome (pills, marginalia) below 50 · popovers 50 · header-attached dropdowns 60 · sticky headers 100 · skip link / overlays 200 · modal dialogs use the native `<dialog>` top layer (no z-index at all — this is *why* the lightbox and report modal use native dialogs).

**Evidence:** the open-queue figure complaints included four z-index stacking failures (#522, #3119, #3147, #5760) — the entire class is structural once modals live in the top layer. The mockups already follow this scale implicitly.

**Resolved 2026-06-11 (Shamsi):** promoted to DESIGN-POLICIES.md with the ~150 band reserved for toasts/notifications — alongside a recorded values note: arXiv wants very few toasts/notifications at all. The anti-corporate, anti-advertising vibe is part of the brand; revisit this note whenever toast/notification work begins.

## G6. Touch-target floor and the negative-margin technique

**Rule:** In any full-screen or touch-primary surface, interactive items have a ≥44px hit area (WCAG 2.5.5 best practice; 2.5.8 minimum is 24px). Where the *visual* design wants a smaller mark (the dropdown close ×), expand the hit area with padding + compensating negative margin so layout is unchanged.

**Evidence:** TOC full-screen list items (44px min-height), close button (negative-margin expansion), Labs toggles noted touchable in the responsiveness audit.

**Resolved 2026-06-11 (researched against external practice, per Shamsi's direction to learn from others rather than invent):** the converged industry answer is a two-tier rule, which we adopt as-is:

- **Hard floor: 24×24 CSS px** ([WCAG 2.2 SC 2.5.8, Level AA](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)) — binding anyway given arXiv's WCAG 2.2 AA posture, with WCAG's own exceptions: inline targets within a sentence (citation chips, version links), spacing-equivalent targets, and user-agent defaults.
- **Design target: 44×44 on touch-primary surfaces** — where Apple HIG (44pt), BBC GEL (7mm ≈ 44px), and Android Material (48dp) all land; WCAG 2.5.5 (AAA) uses the same 44px figure. Applied where touch is the expected input: full-screen menus, mobile pill bars, toggles.

Promoted to DESIGN-POLICIES.md in exactly this two-tier form with the inline exemption named.

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

**Resolved 2026-06-11 (Shamsi):** added to the future user-testing wish list (accessibility-research-questions.md) — interviews/surveys are being planned; this question waits for that round. Until then the rule stands as pattern convention, not policy.

## G10. Truncation always signals continuation

**Rule:** When content is cut by a scrollable or collapsed region, the cut must be visible as such: a fade mask at the cut edge ("scroll for more"), an explicit count on the control ("show all 1,247 authors"), or both. Never a hard clip that looks like the end. Corollary: every scrollable region is keyboard-reachable (`tabindex="0"` + accessible name) — axe flagged exactly this on the citation boxes.

**Evidence:** TOC mobile list fade mask; the 100+ author region (count + bounded scroll + collapse at both ends); the equation-number sticky fix (the *number* no longer vanishes when the equation overflows).

**Resolved 2026-06-11 (researched):** there IS a simpler method that needs no fallback — **the half-item peek**: size the scrollable region so the last visible item is visibly cut mid-item. The continuation signal is geometry, not paint, so it survives Windows High Contrast / forced-colors, zoom, and user stylesheets unchanged (paint-based signals like gradients and masks are exactly what HCM strips — the same class of problem as [box-shadow disappearing in HCM](https://darekkay.com/blog/accessible-focus-indicator/)). Adopted preference order:

1. **Prefer disclosure over internal scrolling** where feasible — "show all N" with an explicit count (the 100+ author pattern). No scroll region, no signal needed.
2. **When a region must scroll internally: half-item peek** (set max-height so a partial item is always visible at the cut).
3. **Fade masks become decoration only** — allowed on top of the peek, never as the sole signal.

Screen-reader support, beyond the keyboard corollary (tabindex="0" + accessible name on every scrollable region): give the region an accessible name that carries the total ("Full author list, 1,247 authors"), use real list semantics so AT announces "list, N items" on entry, and keep collapse/exit controls inside the region at both ends. Updated guidance promoted to DESIGN-POLICIES.md; the reader TOC's mobile fade mask should gain the half-item peek as its primary signal (small follow-up).

---

## Suggested dispositions (for the review discussion)

| # | Proposal | Disposition (reviewed with Shamsi 2026-06-11) |
|---|---|---|
| G1 | Sticky chrome exceptional + scroll offset | ✅ DESIGN-POLICIES.md. Open flag: abstract header is currently sticky — decide. |
| G2 | Chrome recedes | Pattern rationale (PDF-parity intent recorded). HTML-first strategic question logged, undecided. |
| G3 | Short universal nav; one compact grammar | ✅ DESIGN-POLICIES.md (nav cap). Hamburger = permitted narrow-viewport fallback, never default. |
| G4 | arXiv-layer tint family | Working rule; promote after dark-mode family exists. |
| G5 | Z-layer scale | ✅ DESIGN-POLICIES.md, with minimal-toasts values note. |
| G6 | Touch targets: 24px floor / 44px touch-primary | ✅ DESIGN-POLICIES.md (industry-converged two-tier rule). |
| G7 | Reduced-motion incl. JS scrolling | ✅ DESIGN-POLICIES.md. |
| G8 | Progressive enhancement | ✅ DESIGN-POLICIES.md. |
| G9 | Silent ambient indicators | Pattern convention; queued for future AT testing (research-questions list). |
| G10 | Truncation: disclosure > half-item peek > decorative fade | ✅ DESIGN-POLICIES.md; reader TOC peek follow-up noted. |
