# Page Mockups — Preview, NOT Production

This folder contains **in-progress page mockups** for the arXiv redesign. They're hosted here so stakeholders can review the work via a GitHub Pages URL without needing to clone the repo or unzip a bundle.

> **Agent contract:** nothing in `mockups/` is a build or style reference. Patterns are promoted into `docs/` when stable — only the promoted version is canonical. See `AGENTS.md` at the repo root.

## What this is

Mockups are organized by surface, mirroring `docs/` (migrated 2026-07-30 from Shamsi's local working folder; all sets data-scrubbed before publishing — every person, email, IP, and paper in them is fictional):

**`public/` — arxiv.org surfaces**

- **`abstract-redesign.html`** — the abstract page (paper landing page with title, authors, abstract, format/download actions, and citation section).
- **`html-redesign.html`** — the HTML paper reader (in-browser view of a full paper).
- **`merged-abstract-reader.html`** — the merged HTML-first abstract + reader exploration; **`merged-abstract-reader-phase1.html`** is its reduced Phase 1 implementation proposal.
- **`optin-modal/`** — the Labs opt-in modal, layered on a saved arxiv.org page.
- (`images/` and `lib/` are shared assets for these pages.)

**`internal/` — staff tools**

- **`admin-console/`** — Admin Console mockups: `user-page/`, `ownership-requests/`, `category-management/`, `paper-details/`. Home of the metadata-panel, action-bar, and category-editor patterns queued for promotion.
- **`arxiv-check/`** — arXiv Check checkmark/save affordances: `checkmark-buttons.html` plus three annotated design images.

Each page is static HTML (some with a sibling `styles.css`/`script.js`). Open in a browser; no build step, no server required.

## What this is NOT

- **Not a working arXiv build.** Most navigation stays inside the demo page. Links to PDF/TeX source on the abstract page do point to live arxiv.org.
- **Not the canonical design system.** The validated patterns (button styles, link styles, popovers, etc.) live in `../docs/public/`. These mockups *use* the design language being codified there but also include exploratory and in-progress treatments that may never reach production.
- **Not final visuals.** Colors, sizes, typography, and interactions are still iterating. Treat anything you see as a draft.
- **Not the complete redesign.** Search, browse, info pages, the submission flow, and other surfaces are not in this set.

## Where the source of truth lives

Mockups iterate quickly. Patterns that stabilize get promoted to the canonical design system:

| Want to see... | Look at... |
|---|---|
| Validated component CSS + tokens | [`../docs/public/design-system.css`](../docs/public/design-system.css) |
| Component demo pages | [`../docs/public/`](../docs/public/) (`button-styles.html`, `link-styles.html`, etc.) |
| Color palette and rules | [`../docs/color-mapping.md`](../docs/color-mapping.md) |
| Typography system | [`../docs/typography.md`](../docs/typography.md) |
| Non-negotiable design rules | [`../docs/DESIGN-POLICIES.md`](../docs/DESIGN-POLICIES.md) |
| Pattern roadmap (what's promoted, what's queued) | [`../docs/public/README.md`](../docs/public/README.md) |

## Feedback

Projects that generate mockups will have their own communication channels (Slack and shared google docs). To share other feedback or random thoughts open an issue or message Shamsi directly.
