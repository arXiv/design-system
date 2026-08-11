# Design Policies

Hard constraints for all arXiv frontend work — internal tools and public-facing pages. These are non-negotiable rules, not suggestions. Verify compliance before submitting changes.

---
## Contexts: internal, public, outreach

Every arXiv frontend belongs to one of three contexts. The first two set the primary-action color; the third builds on public.
- **Internal tools:** Staff-facing workspaces such as the moderation queue and the Admin Console (arXiv Check) use Access Lime as the primary action color and lighter green tints for backgrounds.
- **Public pages:** Everything a reader or author sees on arxiv.org, including listing, abstract, and HTML paper pages, use Open Blue as the primary action and tints of Repository Brown for backgrounds.
- **Outreach sites:** arXiv's less formal sites — the news blog, event and celebration mini-sites, campaign pages. They use the public design as-is, plus a short list of agreed differences, all listed on [the outreach page](outreach/). Those differences are about tone only. Accessibility, the color palette, self-hosted fonts, and every other rule in this document apply to them unchanged.
- The internal/public split is not a stylistic choice: the accent tells the person which context they are working in, so the two must never be crossed. A lime primary button on a public page, or an Open Blue primary button on a staff tool, is a violation regardless of how well it reads. When the context is genuinely ambiguous (a shared component or an embedded widget), ask and settle which one the user is in before building, then record the answer in a code comment.
- Borrowing goes one way. An outreach site may use anything from the public design. The reverse does not happen on its own: a style invented for a mini-site moves into the shared stylesheet only once a second site needs it, and that move is about where the CSS lives — not about where the style is allowed. Extending anything to arxiv.org is always a separate decision, made deliberately and written down here. Nothing reaches arxiv.org because it happened to be available.
- Token naming is a separate concern, governed under Design tokens below — the prefix follows the rules of the codebase using it, not the context, so never infer the context from a token name or use a token prefix to signal one.

## Accessibility (WCAG 2.1 AA floor, 2.2 AA target)

arXiv's compliance floor is **WCAG 2.1 Level AA** — the standard the Accessible Canada Act adopts through CAN/ASC–EN 301 549. We build toward **WCAG 2.2 AA** in practice (e.g., the target-size rule under *Chrome and interaction structure* is a 2.2 criterion). Where a 2.2 success criterion is named, treat it as the target; 2.1 AA is the non-negotiable minimum.

- **Text contrast:** 4.5:1 minimum for normal text, 3:1 for large text (18px+ regular or 14px+ bold)
- **UI component contrast:** 3:1 minimum for interactive boundaries (borders, outlines, tracks) against their background
- **Focus indicators:** All interactive elements must have a visible focus ring on keyboard navigation. Use `:focus-visible` (not `:focus`) to avoid showing rings on mouse click
- **Labels:** Every form input must have an associated `<label>` (visible or `sr-only`). Use `aria-label` when a visible label is impractical
- **Required fields:** Mark with a visible indicator (red asterisk via `.field-required`) AND `required` + `aria-required="true"` attributes
- **Validation errors:** Link error messages to their field with `aria-describedby`
- **Color alone:** Never use color as the sole means of conveying information (WCAG 1.4.1). Always provide a secondary cue (text, icon, position change)
- **Link underlines:** Inline links in body text must be underlined. Standalone navigation links may omit underlines
- **Responsive design:** All pages must be usable at any screen width. Layouts should be mobile-first and degrade gracefully. No horizontal scrolling on any device.

## Typography

- **Font families:** Use only IBM Plex Sans, IBM Plex Sans Condensed, IBM Plex Mono, and STIX Two Math. See `docs/typography.md` for the full spec.
- **Self-hosted:** All fonts must be self-hosted from arXiv's static assets. No external font services (Google Fonts, Adobe Typekit, CDN-hosted fonts).
- **Font display:** Use `font-display: swap` for text fonts (prioritize readability). Use `font-display: auto` for STIX Two Math (math rendering needs the correct font).
- **System fallbacks:** Every `font-family` declaration must include system fallbacks. See `typography.md` for the standard stacks.

## Design tokens

- **Canonical names.** The design system defines tokens by their semantic name (e.g., `--lime`, `--grey`, `--link`). These are the authoritative reference names used in `design-system.css`.
- **Namespace in production.** Each codebase should add a prefix appropriate to its context to avoid collisions with framework variables (e.g., `--arxiv-lime` in a React/MUI app, `$arxiv-lime` in Sass). The prefixed names should map 1:1 to the canonical names.
- **Values are the source of truth.** When in doubt, the hex values and behavior defined in `design-system.css` are authoritative. If a framework's token differs from the design system value, the design system wins.

## Spacing

- **Scale.** Use the 4px-based / 8-point spacing scale (`--space-1`…`--space-12` in `design-system.css`): 4, 8, 12, 16, 24, 32, 48. Don't introduce off-scale values (14, 26, …).
- **Proximity.** The gap *between* sections should be clearly larger than the gap *within* a section — aim for ~3× (e.g., 16px within, 48px between). This is what makes grouping read without borders or boxes.

## Layout and content width

- **Content-driven, not audience-driven.** The same usability principle applies in every context; only the content differs, so there is no separate rule for "public" vs "internal."
- **Text respects the measure.** Any block of continuous prose targets a ~65-character line length (~640–720px), on public and internal pages alike.
- **Shell width follows density.** The page container's max-width is set by content type: data-dense layouts (tables, multi-column metadata) get more room (internal tools land around 1080px, centered); reading-first pages hug the measure (abstract pages around 920px). These px values are a consequence of content, not a rule about the audience.

## Colors

- **Use the palette.** All colors must come from the documented palette in `docs/color-mapping.md`. Do not introduce one-off hex values.
- **Warm grey ladder:** The palette provides specific stops for specific contrast needs:
  - `--grey-dis` (`#b0aba6`) — disabled/exempt states only (2.24:1, below AA thresholds)
  - `--grey-ui` (`#8b8680`) — interactive UI boundaries: borders, tracks, arrows (3.61:1 on white, passes 3:1)
  - `--grey` (`#6b6459`) — body-weight text, muted labels (5.83:1 on white, passes 4.5:1)
- **Semantic colors:** Use danger tokens (`--danger`) only for destructive actions and error states. Not for brand accents.
- **Campus Red (`#b31b1b`):** Heritage color only. Use for the logo X mark and rare accents. Never for headers, buttons, large color fields, or text.
- **Internal vs public:** Internal tools use Access Lime as the primary button color. Public pages use Open Blue. Do not cross these — the color difference signals which context the user is in.
- **Dark mode:** dark token values exist as foundation only. New pages and components are light-only until the dark program resumes (`planning/dark-mode-decision.md`); never hand-pick dark values into light pages; demo pages lock with `<html data-theme="light">`. See `docs/dark-mode.html` for what is dark-aware today.

## Components

- **New patterns:** If a UI element appears in two or more pages, extract it into a design system CSS file and create or update a pattern page in `docs/`.
- **Platform independence:** Components use plain CSS custom properties — no Sass, no CSS-in-JS, no framework-specific syntax. This allows consumption from React, Jinja, PHP, or static HTML.
- **Naming:** Use `.ds-` prefix for shared design system classes (e.g., `.ds-table`, `.ds-filter`). Page-specific styles stay in the page's own `<style>` block or stylesheet.
- **Icons:** One icon language: inline SVG from the [Lucide](https://lucide.dev) set (ISC license) — stroke-based, `stroke-width="2"`, round caps/joins, `aria-hidden="true"` with an adjacent visible or `.is-sr-only` text label (reference impl: `alerts.html`). No icon fonts. Brand glyphs Lucide lacks (social logos) are one-off inline SVGs following the same sizing rules.

## Buttons

- **Border radius:** 6px for all buttons, icon buttons, and segmented controls
- **Padding:** 10px 20px for standard buttons
- **Shadow:** Subtle shadow at rest: `0 1px 2px rgba(0,0,0,0.08)`. No shadow on tertiary or text-only buttons.
- **Press effect:** All buttons use `transform: translateY(1px)` with shadow removal on `:active`
- **Transition timing:** 0.12s for background, border, color, and shadow. 0.08s for transform.
- **Disabled state:** `cursor: not-allowed`, reduced opacity. WCAG exempts disabled controls from contrast requirements.
- **Three tiers, built differently in each context:** primary, secondary, and a quiet third tier. The third tier is reached by removing whatever the surface's secondary uses to hold the page — public secondary leans on its border, so `.ds-btn-text` drops the border and keeps no fill; internal secondary leans on a lime fill, so `.btn-tertiary` drops the fill and keeps a border. Never add a tier whose only difference from its neighbor is a shadow.
- **Text buttons are not links:** a text button carries Link Blue but is never underlined, and its hover feedback is a background wash. Underlines belong to links (inline always, standalone on hover). If a control navigates, make it a link.
- **Icons in buttons** are sized in `em` so they track the button's own font-size, and never shrink when the label is long.

## Content and interaction

- **Submission type badges:** Use the established palette: `.type-new` (blue), `.type-rep` (yellow), `.type-wdr` (dark), `.type-cross` (light grey)
- **Segmented controls:** Use semantic variants — `.seg-positive` (green/accept), `.seg-neutral` (blue/informational), `.seg-negative` (red/reject)
- **Filter dropdowns:** Use `.ds-filter` with a visible `<label>`. Always include an "All" option as the inclusive default.
- **Toggle switches:** Off state uses `--grey-ui`. On state uses lime green (internal) or Link Blue (public). Label text uses `--grey` (off) shifting to a darker shade (on).

## Public pages — additional policies

- **No metrics display:** arXiv does not display view counts, download counts, or citation counts on public pages. This is a core operating value — arXiv does not promote or rank papers.
- **Citation export:** On abstract pages, we provide BibTeX (default), APA, Chicago, and MLA formats. Generate from metadata to save manual work for the user.
- **arXiv Labs:** Labs tools that collect user data must be behind an opt-in toggle, not on by default (this policy is still in the early implementation phase as 6/24/26 and not enforced for Labs yet). Labs that require login to a third party platform should be deprioritized in placement.
- **Header:** Single bar. Black (phase 1, spinout) transitioning to Repository Brown (phase 2). Logo, Search, Submit, Donate, Log in. No Cornell branding post-spinout. Outreach sites may run an Open Blue header instead — an agreed exception for them, never valid here.
- **Footer:** Acknowledgment text (Simons Foundation, member institutions, IP matched institution name). Links: About, Help, Contact, Subscribe, Copyright, Privacy, Accessibility, Status. Special section for major funders on the right side. All acknowledgements are presented in the footer, never in the header.
- **Banner:** A minimal and time-bound banner can be displayed with short announcements. It includes a small icon, a short sentence and link, and a dismiss button. After dismissing, the banner should not display for that user again.

## Chrome and interaction structure

*Added 2026-06-11 from the PROPOSED-GUIDELINES review (see `planning/PROPOSED-GUIDELINES.md` for evidence and rationale).*

- **Sticky chrome is exceptional.** The HTML paper reader is the only page approved to use a sticky header — it alone is a long-document reading context that earns persistent chrome. Do not add sticky chrome to other pages without explicit approval. Any page that does carry sticky chrome MUST set `html { scroll-padding-top }` to at least the chrome's tallest state plus breathing room (reader reference: 80px), covering every anchor path including JS `scrollIntoView`. (Decided 2026-06-11: the abstract-page header is static — it scrolls away like any other content. The reader is the only sticky-chrome surface in fact as well as intent.)
- **Universal navigation stays short.** The header nav is capped at its current five items (Search, Submit, Donate, Log in + logo). Resist link-creep permanently. Narrow viewports condense (wrap or compact grammar) rather than hamburger; a hamburger is a permitted last-resort fallback at very narrow widths, never the default.
- **Z-layer scale.** Content chrome (pills, marginalia) < 50 · popovers 50 · header-attached dropdowns 60 · sticky headers 100 · ~150 reserved for toasts/notifications · skip link/overlays 200 · modal dialogs use the native `<dialog>` top layer (no z-index). Do not introduce ad-hoc z-index values. *Values note: arXiv wants very few toasts/notifications at all — anti-corporate, anti-advertising is part of the brand.*
- **Target size.** Hard floor 24×24 CSS px (WCAG 2.2 SC 2.5.8 AA), with WCAG's own exceptions (inline targets within a sentence — citation chips, version links — spacing-equivalent, user-agent defaults). Design target 44×44 on touch-primary surfaces (full-screen menus, mobile pill bars, toggles) — where Apple HIG, BBC GEL, and Android guidance converge. Use the padding + negative-margin technique to grow hit areas without changing layout.
- **Reduced motion covers JavaScript.** `prefers-reduced-motion: reduce` must disable ALL motion: CSS transitions/animations AND JS-driven motion — `scrollIntoView({behavior:'smooth'})` ignores CSS rules, so JS must check `matchMedia('(prefers-reduced-motion: reduce)')` per call.
- **Progressive enhancement: scripts never carry content.** Server-rendered HTML is complete and readable before any JavaScript runs. Anything hidden pending a JS reveal is scoped under `html.js`; controls that do nothing without JS are hidden without it; controls with a meaningful non-JS equivalent degrade to it (search button → search-page link).
- **Truncation always signals continuation.** Preference order: (1) disclosure with an explicit count ("show all 1,247 authors") over internal scrolling; (2) where a region must scroll internally, size it so the last visible item is visibly cut mid-item (the half-item peek — a geometric signal that survives forced-colors, zoom, and user stylesheets); (3) fade masks are decoration only, never the sole signal. Every scrollable region is keyboard-reachable (`tabindex="0"`) with an accessible name carrying the total, uses real list semantics, and keeps its exit/collapse controls inside the region.

---

*These policies expand as UX research and production requirements are incorporated. When a policy conflicts with a mockup's current implementation, the policy wins — update the mockup.*
