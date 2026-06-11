# Page Mockups — Preview, NOT Production

This folder contains **in-progress page mockups** for the arXiv redesign. They're hosted here so stakeholders can review the work via a GitHub Pages URL without needing to clone the repo or unzip a bundle.

## What this is

Two whole-page mockups:

- **`abstract-redesign.html`** — the abstract page (paper landing page with title, authors, abstract, format/download actions, and citation section).
- **`html-redesign.html`** — the HTML paper reader (in-browser view of a full paper).

Each is a self-contained static HTML file with inline `<style>` and `<script>`. Open either in a browser to view; no build step, no server required.

## What this is NOT

- **Not a working arXiv build.** Most navigation stays inside the demo page. Links to PDF/TeX source on the abstract page do point to live arxiv.org.
- **Not the canonical design system.** The validated patterns (button styles, link styles, popovers, etc.) live in `../design-patterns/public/`. These mockups *use* the design language being codified there but also include exploratory and in-progress treatments that may never reach production.
- **Not final visuals.** Colors, sizes, typography, and interactions are still iterating. Treat anything you see as a draft.
- **Not the complete redesign.** Search, browse, info pages, the submission flow, and other surfaces are not in this set.

## What to try

### `html-redesign.html`
- Resize the browser. Notable breakpoints: ~1200px (right-margin marginalia toggles on/off), ~700px (mobile chrome kicks in).
- Click any citation chip — `[15, 44, 45, 26, 31, 3]` — to open a reference popover with "Jump to reference."
- Use "Back to your place" to return.
- Hover over equations and figures — a chip pill appears with action affordances.
- Hover over footnote markers, especially in section 2 where they cluster. At wide widths, the corresponding right-margin notes light up.
- Click the "Contents" button in the center of the header — the dropdown follows you as you scroll, with the current section highlighted.
- At narrow widths, the TOC dropdown becomes a full-screen overlay.

### `abstract-redesign.html`
- Resize for responsive behavior.
- Try the Labs toggle switches — opt-in experimental features.
- Browse the citation export section at the bottom (BibTeX / APA / Chicago / MLA).

## Where the source of truth lives

Mockups iterate quickly. Patterns that stabilize get promoted to the canonical design system:

| Want to see... | Look at... |
|---|---|
| Validated component CSS + tokens | [`../design-patterns/public/design-system.css`](../design-patterns/public/design-system.css) |
| Component demo pages | [`../design-patterns/public/`](../design-patterns/public/) (`button-styles.html`, `link-styles.html`, etc.) |
| Color palette and rules | [`../design-patterns/color-mapping.md`](../design-patterns/color-mapping.md) |
| Typography system | [`../design-patterns/typography.md`](../design-patterns/typography.md) |
| Non-negotiable design rules | [`../DESIGN-POLICIES.md`](../DESIGN-POLICIES.md) |
| Pattern roadmap (what's promoted, what's queued) | [`../design-patterns/public/README.md`](../design-patterns/public/README.md) |

## Feedback

Open an issue or message Shamsi directly. Feedback while a mockup is in this folder is treated as in-progress input; once a pattern is promoted to `design-patterns/public/`, it's been validated and changes go through a more deliberate review.
