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
| `blog-theme/` | packaged copy (zip) of the blog.arxiv.org WordPress theme — a **separate project** that extends the design system; its source lives in another repo | **Never.** Its CSS carries agreed blog-only exceptions; do not read it as the rule, and do not sync it — see below |

## Before any frontend change

1. Read `docs/DESIGN-POLICIES.md` — hard constraints. Non-negotiable.
2. Read `docs/brand.html` — the *why*; use it when no explicit rule covers your case.
3. Use the routing table to read **only** what your task touches. Do not read the whole repo.

## Routing — building X? read Y, reuse Z

| Building / touching | Read | Reuse |
|---|---|---|
| Anything with color | `docs/color-mapping.md`, `docs/colors.html` | tokens in that context's stylesheet |
| Typography, text sizes | `docs/typography.html`, `docs/typography.html` | `--ds-font-*` |
| Spacing, gaps, grouping | `docs/spacing.html` + DESIGN-POLICIES *Spacing* / *Layout* | `--ds-space-*` |
| Buttons | `docs/buttons.html`, then your context's deep page (`docs/public/button-styles.html` / `docs/internal/button-styles.html`) | `.ds-btn*` (public, incl. `.ds-btn-text` and `.on-tint` / `.on-dark`), `.btn-*` (internal) |
| Alerts, status & feedback messages | `docs/alerts.html`, then `docs/public/alert-styles.html` or `docs/internal/alert-styles.html` | `.ds-alert*` — never rebuild its chrome |
| Cards, rails, page organization | `docs/organizing-content.html` | card conventions, dl row grammar, `.ds-acc-rail` in a sidebar |
| Accordions, show more, popovers — anything hiding content behind a control | `docs/progressive-disclosure.html` | `.ds-acc*`, `.ds-show-more`, `.ds-popover` |
| A modal, dialog, confirmation, or anything that takes over the page | `docs/modals.html` | `.ds-modal*` on a native `<dialog>` + `showModal()` — never a `<div role="dialog">`, never `show()` |
| A close or dismiss control | `docs/buttons.html` | `.ds-close` — one control on both surfaces; the host supplies position only |
| Links | `docs/public/link-styles.html` or `docs/internal/link-styles.html` | link tokens; inline links underlined |
| Tables (internal tools), row selection, bulk actions | `docs/internal/table-styles.html` | `.ds-table`, sortable headers, `.ds-filter`; bulk-bar + selection rules documented there |
| One record's details (label + value panel) | `docs/internal/metadata-panel-styles.html` (concept: `docs/organizing-content.html`) | `.ds-meta-panel` + `--editable` / `--reference` / `--ruled` |
| Forms, validation | `docs/forms.html` — one page, both surfaces | `.ds-field`/`.ds-label`/`.ds-input`/`.ds-hint`, `.is-invalid`, `.field-error`, `.ds-check`, `.ds-switch`, `.ds-seg` |
| Version display | `docs/version-display.html` | inline version links + `.ds-alert` warning |
| Site header / footer | `docs/public/header-styles.html`, `docs/public/footer-styles.html` | `.ds-site-header` (+ `--light`), `.ds-site-footer` — never hand-build chrome or draw logos from text |
| Category / topic / state labels | `docs/tags.html` + DESIGN-POLICIES *Content and interaction* | `.ds-tag` (+ `--chrome` / status / `--keep-case`); category names are copied, never restyled |
| Type badges | `docs/tags.html` + DESIGN-POLICIES *Content and interaction* | `.ds-badge` + `--new/--rep/--wdr/--cross` |
| Dark mode (status, mechanism, what flips) | `docs/dark-mode.html` | tokens flip automatically; never hand-pick dark values; lock demo pages light |
| The blog, an event or campaign mini-site | `docs/outreach/` + DESIGN-POLICIES *Contexts* | the public stylesheet, plus only the differences listed there |
| Error messages, form help, instructions | `docs/STYLE.md`, then `docs/brand.html` for voice | existing wording — one name per thing, never a synonym |
| Something with no pattern | nearest pattern above + `docs/brand.html` | derive from documented rationale; say so in comments |

**Stylesheets are tiered.** `docs/design-system.css` is **tier 1** — the foundation and every component more than one surface could use. Everything loads it.

`docs/internal/design-system-staff.css` is **tier 2 for staff tools**, and is *not* self-contained: a staff page loads tier 1 first, then this. It holds only what is staff-only (the `.btn-*` family, tables, metadata panels, segmented controls, toggles, type badges, info cards) plus the tokens whose values differ on that surface — chiefly Access Lime as `--ds-accent`.

```html
<link rel="stylesheet" href="../design-system.css">
<link rel="stylesheet" href="design-system-staff.css">
```

A tier 2 file may re-point a tier 1 token, which is how a surface gets its accent. It must never introduce a token that reuses a tier 1 name for a different meaning. **Never copy a component into tier 2 to restyle it** — if it needs to look different, that is a token, not a second copy.

## Rules agents break most (verified by our agent tests)

- **Self-hosted everything.** Never load fonts, icons, or CSS from external URLs — no Google Fonts, no CDNs. If an existing page does it, that page is wrong, not the rule.
- **Dark mode is live — build for it.** Take colors from tokens and pages flip on their own; never hand-pick a dark value. Text on an accent fill and specimen colors are the exceptions that stay fixed. Only lock a page light when it exists to show light-mode rendering. (`docs/dark-mode.html`.)
- **Two accent colors, never crossed.** Internal tools: Access Lime primary. Public pages: Open Blue primary. The accent tells people where they are. Outreach sites (blog, mini-sites) use the public design and may differ from it only in the ways listed in `docs/outreach/`.
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
- After changing either `design-system.css`, run `python3 verification/check-drift.py`. It guards the places where a value is written down twice — chiefly the mirrored dark palette. Any FAIL is yours to fix.
- **Never sync the blog theme as a side effect of other work.** It is a separate project that *extends* the design system — more playful and more colorful than arxiv.org would ever be — and it is updated by a deliberate translation pass, where a person decides which changes belong there and how they should read in the blog's voice. The drift check reports blog differences as a NOTE, never a FAIL: that list is the agenda for the next translation, not a defect to clear. Overwriting the theme's copy with the canonical file destroys decisions it made on purpose.

## Repo conventions

- Small team: never add anything needing manual upkeep.
- Git: commit direct to master (WIP repo), identity SBBCornell. Published via GitHub Pages.
- Tests: `verification/token-burn/` measures whether agents can work in this repo. Its tasks/rubrics are excluded from test workspaces — don't tune to them.
