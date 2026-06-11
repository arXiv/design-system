# Evaluation of the 2026-06-11 Audits

**Evaluator:** Claude (second-instance review), 2026-06-11
**Method:** verified the audits' factual claims against the repo (design-system.css, README roadmap) and against live re-renders of both mockups at the audited widths; re-measured each flagged issue before fixing.

## Verdict

Both audits are sound and useful. The component audit's claims about promoted patterns all check out (`.ds-btn-*`, `.ds-link`, `.ds-alert`, `.ds-popover`, `.ds-element-pill`, `.ds-annotation` exist in `design-patterns/public/design-system.css` as stated), the four-eras framing matches what the screenshots show, and the footer-first promotion recommendation is correct — it was already validated three ways and is the cheapest unification win. The responsiveness audit's four issues were all real. Corrections and additions below.

## Corrections to the responsiveness audit

1. **Equation-tag clipping was understated.** The audit called it "narrow-viewport-only, slightly subtle" and ranked it last. Re-measurement at 320px: **119 of 145 equation tags** sat beyond the initial viewport width — on a math-heavy paper the reader can't tell which equation is which without scrolling away from it. Fixed (2026-06-11) with `position: sticky; right: 0` on the tag cell inside the scrollable container; all 145 tags now stay visible while the equation scrolls beneath.
2. **The orphan-pipe issue had already resolved itself** before any fix: the header rework that matched the approved Cloud Run deployment removed the "About" link, and the shortened nav no longer wraps at 320px. No action needed — but see "regression worth discussing" below.
3. **"Body text justified with hyphens working appropriately" is listed under "what works."** Justification is under active reconsideration (dyslexia evidence + open issue #6533 asking to disable justify, #5028 on aggressive hyphenation). Don't treat that line as design validation — it only says the CSS executes.
4. The title-size fix landed as fluid `clamp(1.375rem … 2rem)` rather than a breakpoint swap — same intent, smoother behavior, rem-based so user font-size overrides still propagate. 320px now renders the sample title at 3 lines (was 5 with a mid-word break).
5. The license-underline diagnosis was right (abbr default decoration); fixed with a solid 1px underline at 3px offset.

## What the component audit missed

1. **The accessibility dimension of "promotion."** The audit treats promotion as a visual/CSS exercise. Several inventoried components carry hard-won interaction contracts that must travel with them: the citation popover's open/close ARIA lifecycle, the author-truncation tiers (including the 100+ scrollable region), the no-JS fallbacks, the lightbox's dialog semantics. Codifying only the CSS would silently strip those. Pattern pages should document the behavior contract, not just the styles. (The audit's own "What's NOT in this audit" acknowledges this — flagging it here so the promotion work doesn't inherit the blind spot.)
2. **Stale inventory at the margins:** the figure lightbox, section-heading permalinks, and Expand chips (committed the same day, `fb0f1a7`) are absent from the net-new component list. Add to the next inventory pass.
3. **The breadcrumb bar deserves more weight.** It's listed as info-site-only, but the approved abs-page header now includes `logomark › gr-qc › arXiv:2604.22725` — which quietly resolves the long-open "no way back to the category" research item (AUXDH-950/951). Worth recording as resolved in the review doc, and worth noting the breadcrumb is now a cross-page pattern (info-site + abs page) and therefore a promotion candidate by the audit's own frequency criterion.
4. **A regression worth discussing, not just noting:** matching the approved deployment removed "About" from the header — which was the abstract mockup's only newcomer-signposting affordance (research: Dan Miner, "I have no clue what I am walking into"). The dismissable announcement banner partially covers it today, but banners are temporal. When the announcement retires, newcomer signposting has no home again. The open design question from the review doc still stands and now has nowhere on the page pointing at it.
5. **Era count:** account/login + submission flows arguably form a distinct fifth visual era (the audit folds them into "legacy"). Doesn't change conclusions; matters for estimating unification scope.

## Re-prioritization check

The audit's ordering (footer → header → search → form atoms) holds up, with one adjustment: **header codification should carry the announcement banner and breadcrumb bar as part of the pattern**, since the approved deployment treats the three as one unit. Codifying only the black bar would re-fragment the chrome on day one.
