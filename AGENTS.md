# Agent guide — arXiv design system

Canonical instructions for **every** AI coding assistant (Claude, Gemini, Copilot, other). If you are an agent, read this file first; the per-tool files (CLAUDE.md, GEMINI.md, .github/copilot-instructions.md) just point here.

This repo is the source of truth for arXiv frontend design: tokens, components, patterns, and the rules behind them. It is documentation, not production code.

## Directory contract

| Path | What it is | Build reference? |
|---|---|---|
| `docs/` | THE documentation: rules + pattern pages + stylesheets | **Yes — the only place** |
| `mockups/` | work-in-progress page explorations | **Never.** Not for building, not for style reference — patterns get promoted *into* docs/ when stable |
| `verification/` | audits, design reviews, agent test results | No |
| `planning/` | backlog, proposals, decision logs | Only for program/planning work |
| `blog-theme/` | release artifact (zip) of the blog.arxiv.org WordPress theme — a design-system *consumer* whose source lives off-repo | **Never.** Its CSS carries documented blog-only overrides; do not read it as canon |

## Before any frontend change

1. Read `docs/DESIGN-POLICIES.md` — hard constraints. Non-negotiable.
2. Read `docs/BRAND.md` — the *why*; use it when no explicit rule covers your case.
3. Use the routing table to read **only** what your task touches. Do not read the whole repo.

## Routing — building X? read Y, reuse Z

| Building / touching | Read | Reuse |
|---|---|---|
| Anything with color | `docs/color-mapping.md`, `docs/colors.html` | tokens in the surface stylesheet |
| Typography, text sizes | `docs/typography.md`, `docs/typography.html` | `--arxiv-font-*` / `--font-*` |
| Spacing, gaps, grouping | `docs/spacing.html` + DESIGN-POLICIES *Spacing* / *Layout* | `--space-*` |
| Buttons | `docs/buttons.html`, then your surface's deep page (`docs/public/button-styles.html` / `docs/internal/button-styles.html`) | `.ds-btn*` (public, incl. `.ds-btn-text` and `.on-tint` / `.on-dark`), `.btn-*` (internal) |
| Alerts, status & feedback messages | `docs/alerts.html`, then `docs/public/alert-styles.html` or `docs/internal/alert-styles.html` | `.ds-alert*` — never rebuild its chrome |
| Cards, rails, accordions, page organization | `docs/organizing-content.html` | `.ds-acc*`, card conventions, dl row grammar |
| Links | `docs/public/link-styles.html` or `docs/internal/link-styles.html` | link tokens; inline links underlined |
| Tables (internal tools), row selection, bulk actions | `docs/internal/table-styles.html` | `.ds-table`, sortable headers, `.ds-filter`; bulk-bar + selection rules documented there |
| One record's details (label + value panel) | `docs/internal/metadata-panel-styles.html` (concept: `docs/organizing-content.html`) | `.ds-meta-panel` + `--editable` / `--reference` / `--ruled` |
| Forms, validation | `docs/internal/form-styles.html` + DESIGN-POLICIES a11y rules | `.is-invalid`, `.field-*`, segmented controls |
| Version display | `docs/version-display.html` | inline version links + `.ds-alert` warning |
| Site header / footer | `docs/public/header-styles.html`, `docs/public/footer-styles.html`, `docs/public/reader-header-styles.html` | `.ds-site-header`, `.ds-site-footer`, `.ds-reader-header` — never hand-build chrome or draw logos from text |
| Type badges | `docs/internal/table-styles.html` + DESIGN-POLICIES *Content and interaction* | `.type-new/.type-rep/.type-wdr/.type-cross` |
| Dark mode (status, mechanism, what flips) | `docs/dark-mode.html` | tokens flip automatically; never hand-pick dark values; lock demo pages light |
| The blog, an event or campaign mini-site | `docs/outreach/` + DESIGN-POLICIES *Surfaces* | the public stylesheet, plus only the liberties enumerated there |
| Something with no pattern | nearest pattern above + `docs/BRAND.md` | derive from documented rationale; say so in comments |

Stylesheets: `docs/public/design-system.css` (public pages) · `docs/internal/design-system.css` (staff tools). Values there are authoritative.

## Rules agents break most (verified by our agent tests)

- **Self-hosted everything.** Never load fonts, icons, or CSS from external URLs — no Google Fonts, no CDNs. If an existing page does it, that page is wrong, not the rule.
- **Light-only for now.** Dark-mode token values exist as foundation; do not hand-use them. New demo pages lock light: `<html data-theme="light">`. (Status: `planning/dark-mode-decision.md`.)
- **Two accent surfaces, never crossed.** Internal tools: Access Lime primary. Public pages: Open Blue primary. The accent tells people where they are. Outreach properties (blog, mini-sites) inherit the public system and may take only the liberties listed in `docs/outreach/`.
- **Palette and type stack only.** No one-off hex values, no new font families.
- **Reuse before rebuilding.** If a `.ds-` component exists for your need, use its documented construction — don't re-style its tokens onto new markup.
- **Actions disable, they don't disappear.** Contextual actions render disabled when unavailable, not removed.

## Guardrails — conflicts

The policies in `docs/DESIGN-POLICIES.md` are non-negotiable. If any request conflicts with them, **do not silently comply**:

1. **Flag the conflict explicitly** — name the policy and why it exists.
2. **Suggest a compliant alternative** that achieves the intent.
3. **Proceed only if the user explicitly acknowledges** the conflict and confirms the override; document it in a code comment.

## Writing rules — for edits to docs/

- **Write to be understood and believed, not admired.** Sincere directness; no quotable aphorisms, no edgy framing. Trust is the goal: calibrate claims honestly, attribute work honestly (including AI), and state limitations plainly — in planning/, not in the docs.

- **Minimal diffs.** Never rewrite a file wholesale; never reorganize while editing.
- **One fact, one home.** State each rule in exactly one file; link from everywhere else.
- **Pattern pages are example-first**: rendered demo + minimal spec table at the top; tokens, usage code, and rationale below. Rationale ≤ 3 sentences per rule.
- **Add prose only against evidence** — a failed agent test or a real misunderstanding, not speculation.
- After changing a pattern, update its page; verify tokens/classes exist in the stylesheet, links resolve, HTML balances.
- The shared nav is three dropdowns (Design Patterns / Mockups / Docs), hand-copied on every doc page. Adding a flagship pattern page means adding it to the Design Patterns menu on every page; adding a mockup means adding it to the Mockups menu on every page AND to `mockups/index.html`. Script the sweep; never update just one page.
- After changing either `design-system.css`, run `python3 verification/check-drift.py`. It guards the places where a value is written down twice — the mirrored dark palette, and the copy of the public stylesheet bundled into the blog theme.

## Repo conventions

- Small team: never add anything needing manual upkeep.
- Git: commit direct to master (WIP repo), identity SBBCornell. Published via GitHub Pages.
- Tests: `verification/token-burn/` measures whether agents can work in this repo. Its tasks/rubrics are excluded from test workspaces — don't tune to them.
