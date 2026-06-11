# Responsiveness Audit — 2026-06-11

**Scope:** the two redesign mockups (`mockups/html-redesign.html`, `mockups/abstract-redesign.html`).
**Method:** Playwright captured viewport-only screenshots at 6 widths (320, 375, 414, 768, 1024, 1440) × 2–3 scroll positions (top, mid, bottom). Live arXiv pages were excluded from this pass — they're known to lack mobile responsiveness; auditing them would yield no actionable signal.
**Screenshots:** `screenshots/responsiveness/<page>/<width>-<position>.png`. 30 captures total.

## Headline

Both mockup pages are **broadly responsive** with a small set of specific issues. No catastrophic breakage at any viewport. Most issues are polish — clipping, sizing, or visual artefacts — rather than structural failures.

---

## `html-redesign.html` — the HTML paper reader

### What works
- Header chrome adapts cleanly: mini-logomark + icon-only nav + centered "Contents" trigger at ≤700px; full logo + labels at ≥768px.
- The **Contents trigger label** updates as you scroll (320-mid shows "Flat slicing"), demonstrating the orientation behavior at narrow widths.
- Watermark stacks to two lines at narrow widths (arXiv ID + license).
- **Abstract** gets its bordered-box treatment at mobile, indented padding at desktop — clean transition.
- Body text justified with hyphens working appropriately at all widths.
- Marginalia (right-margin footnotes, alt-text) hide at ≤1199 and the page reflows without leaving empty gutters.
- "Help improve this paper" footer band visible and well-formed across viewports (320-bottom).

### Issues found

**1. "License: CC BY 4.0" link renders with strikethrough-looking underline** — visible at every viewport (320-top, 414-top, 768-top, 1024-top, 1440-top). The underline appears to cut through the text vertically rather than sit below it. Likely a `text-underline-offset` issue with the `<abbr>` element interacting with the link's underline. *Fix: explicitly set `text-underline-offset` or `text-decoration-thickness` on `.new-watermark a abbr`, or strip the abbr's default styling.*

**2. Display equation tags ("(4.7)" etc.) clip on the right edge at narrow widths** — visible at 320-mid. The equations themselves are horizontally scrollable (the overflow-x:auto we added) but the equation number sits flush with the viewport edge and gets cut. *Fix: either reserve right-side padding for equation tags in the scrollable container, or move the equation tag to a position that's not clipped (above the equation, or sticky-aligned).*

**3. Title centering at 768/1024 widths** — the title is centered correctly but appears to sit slightly left of dead center on the page because the content column is offset by the (hidden) marginalia gutter. Visual artifact, not a layout failure. Worth noting if the centering looks off to your eye.

### Per-viewport notes (worth eyeballing yourself)
- **320 / 375 / 414**: chrome compresses correctly, title wraps to 3 lines, authors flow as inline link cluster.
- **768**: full logo returns, nav labels visible. Watermark on single line.
- **1024**: similar to 768; no breakage at the in-between.
- **1440**: marginalia still hidden (the breakpoint is 1199); no right-margin content visible. Note: at >1199 widths the marginalia would appear — not tested in this pass.

---

## `abstract-redesign.html` — the abstract page

### What works
- Two-column layout (paper text left + action buttons right at 1024/1440) collapses to a single column at 768 and stacks naturally at mobile.
- Action buttons (HTML, PDF, TeX Source) wrap intelligently — side-by-side on mobile, stacked on desktop.
- Version warning amber alert renders correctly at all widths.
- Author list flows as inline links, wrapping naturally.
- Footer with funder logos and member-institution acknowledgment stacks cleanly.
- Labs section ("Hugging Face Spaces" toggle + "What is arXiv Labs?") renders at mobile, with the toggle target large enough to be touchable.

### Issues found

**1. Title font is too aggressive at 320px** — visible at 320-top. The 24px+ title size causes "Gauge-independent approach to inflation in quadratic gravity" to wrap as: "Gauge-" / "independent" / "approach to" / "inflation in" / "quadratic gravity" — five lines for a 7-word title. *Fix: reduce title font-size at ≤414px (e.g., to 22px) or add `hyphens: manual` so it breaks at sensible word boundaries.*

**2. Header has an orphan vertical pipe character at narrow widths** — visible at 320-top, the top dark header shows "Search · About · Submit · Donate |" followed by "Log in" on a new line below. The pipe was meant as a visual divider before "Log in" but when "Log in" wraps to its own row, the pipe is stranded at the right edge of the upper row. *Fix: at ≤700px either remove the pipe-divider entirely (CSS `display: none` on the divider) or move "Log in" into the upper row's flexbox with a proper wrap rule.*

**3. Black header bar feels disproportionately tall at 320** — the two-row top chrome (nav row + login row) takes ~120px of an already-narrow viewport. The chrome is a higher percentage of the visible reading area than is comfortable. *Possible fix: collapse the nav into a hamburger pattern at ≤414 like the html-redesign mockup does. (Tradeoff: introduces a second nav dropdown the user has to learn.)*

### Per-viewport notes
- **320**: title size + orphan pipe issues above. Otherwise clean.
- **375 / 414**: title still wraps aggressively but with the larger viewport, fewer lines.
- **768**: two-column layout activates cleanly. Action buttons stack on the right.
- **1024 / 1440**: full two-column with comfortable margins.

---

## Things to fix soon

In priority order:

1. **Title font-size at mobile (`abstract-redesign.html`)** — most visible issue, smallest fix.
2. **License-link underline rendering (`html-redesign.html`)** — appears at every width, looks unprofessional.
3. **Header orphan pipe (`abstract-redesign.html`)** — narrow-viewport-only but obvious when it happens.
4. **Equation tag clipping (`html-redesign.html`)** — narrow-viewport-only, slightly subtle.

## Things to verify in a follow-up pass

- **Marginalia behavior at ≥1200px** — this audit didn't go above 1440. Worth a 1600px or 1920px screenshot to confirm the right-margin marginalia displays cleanly.
- **iOS Safari** — Playwright uses Chromium. iOS Safari has its own quirks (overscroll, viewport units, sticky positioning) that won't show up here. Real-device test recommended for the final cut.
- **Interaction states** — this audit captured static positions only. Hover, focus, popover-open, and dropdown-open states aren't tested. Could be added in a follow-up Playwright pass with explicit interactions before each screenshot.
