# DESIGN-POLICIES.md duplicate audit

2026-10-13. Nothing has changed yet. This is the proposal for Shamsi to approve.

The idea: `DESIGN-POLICIES.md` keeps each non-negotiable as one or two sentences, with a link to the page that holds the detail. Detail lives in one place only.

## 1. Already wrong because of duplication (fix whatever we decide)

- **Buttons, padding:** the policy says `10px 20px`; the stylesheet uses `0.715em 1.43em`, so it grows with text size. The policy is out of date.
- **Buttons, third tier:** the policy names `.btn-tertiary`, which no longer exists. There is one `.ds-btn*` family for both surfaces.
- **Dark mode:** "`--ds-text-on-accent` / `--ds-text-on-accent`" names the same token twice (a typo).
- **One name per thing:** now in both *Writing* and layout-patterns.html (added today). Keep it in one place.

## 2. Duplicated: shorten to one line and a link

| Section in DESIGN-POLICIES | Detail also in | Proposed one line |
|---|---|---|
| Typography, what each family is for | typography.html | "IBM Plex and STIX Two Math only; adding a face is a decision recorded here. See typography.html." |
| Font display, system fallbacks | typography.html | Drop; the stylesheet already sets them. |
| Spacing: scale, rem, break names, proximity, gap | spacing.html | "Use the named breaks, never a pixel value; gaps between groups are at least twice the gaps inside one. See spacing.html." |
| Layout: 850px, 1080px, long-form measure | layout-patterns.html, spacing.html | "One width per page, from the width tokens. See Layout patterns." |
| Breakpoints (three bullets) | none yet | Move to layout-patterns.html, keep one line here. |
| Buttons (whole section, 10 bullets) | buttons.html | "Three tiers; disabled is a flat grey, never opacity; a control that navigates is a link. See buttons.html." |
| Segmented controls, filter dropdowns, switches | forms.html | Drop; forms.html holds them. |
| Rectangular labels | tags.html | Drop. |
| Icons | icons.html | "Lucide inline SVG, with a text label. See icons.html." |
| Required and optional fields (long) | forms.html | "Mark optional fields in words; leave required fields unmarked. See forms.html." |
| Dark mode is live (long) | dark-mode.html | "Take every colour from tokens; never hand-pick a dark value. See dark-mode.html." |
| Public header, footer, banner | header.html, footer.html | Keep the fixed facts (single bar, no Cornell branding, acknowledgements only in the footer, banner exception); drop the link lists. |
| Sticky bar, universal navigation length | header.html | Keep both: they are approvals that need a design-team decision to change. Remove the `header.js` folding detail. |
| Z-layer scale | modals.html, progressive-disclosure.html | Keep the scale here (it is the one list); drop the history note into git. |
| Truncation | header.html, PATTERNS.md | Keep; it has no page of its own. |

## 3. Keep as they are (this file is their only home)

Contexts (internal, public, outreach, the blog theme, privileged controls, borrowing one way), browser support, the accessibility floor, self-hosted fonts, token naming, the palette, red means error, Campus Red, opacity for dimming, no contractions, category names copied, the public-page policies (no metrics, citation export, Labs), magnification, no `100vw`, target size, reduced motion, progressive enhancement, no breadcrumbs (already a one-liner).

## Effect

About 160 lines down to about 90. Every value an agent could copy (pixels, timings, token pairs) would then live only on the page that the stylesheet is checked against.
