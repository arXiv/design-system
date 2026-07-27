# arXiv Design System

## What this is

A proto-design-system for arXiv's frontend. It contains design tokens, component specifications, typography and color decisions, accessibility requirements, and interactive HTML/CSS pattern references. These are not production code — they define the visual language and interaction patterns that production code should follow.

The design system serves two audiences with different visual treatments but shared foundations:
- **Internal tools** (arXiv Check, Admin Console) — warm, utilitarian, lime-accented
- **Public-facing pages** (arxiv.org, abstract pages, HTML papers) — clean, fast, brown-and-blue

## Who this is for

- **Designers / product owners** — open any `.html` file in a browser to see component references. Read `color-mapping.md` and `typography.md` for brand decisions.
- **Developers** — reference `design-patterns/` for component specs, tokens, and accessibility requirements. Start with `DESIGN-POLICIES.md` for hard constraints.
- **AI coding agents** — read this file first, then `BRAND.md`, then `DESIGN-POLICIES.md`, then `design-patterns/typography.md` and `design-patterns/color-mapping.md`. Check `design-patterns/internal/DESIGN-PROGRESS.md` for current status. Follow all policies strictly. **If a request conflicts with any policy, flag the conflict to the user before proceeding.** See `CLAUDE.md` for detailed guardrail instructions.

## Directory structure

```
CONTEXT.md                        ← this file: project overview
BRAND.md                          ← voice + brand statement + the design principles they drive
DESIGN-POLICIES.md                ← hard constraints (a11y, tokens, conventions)
NEXT-STEPS.md                     ← program-level backlog and priorities
CLAUDE.md                         ← AI agent entry point (pointer to context files)

audits/                           ← all audits (the "why")
  audit-visual.md                 ←   platform-wide 11-silo visual audit (+ images/)
  audit-labs.md                   ←   functional audit of 16 arXiv Labs (+ labs-screenshots/)
  2026-06-11/                     ←   component / responsiveness audit run

design-patterns/
  typography.md                   ← font families, weights, self-hosting plan (shared)
  color-mapping.md                ← full palette, internal vs public color usage (shared)

  internal/                       ← arXiv Check + Admin Console (active)
    design-system.css             ←   all component CSS + design tokens (:root)
    button-styles.html            ←   button component reference
    card-styles.html              ←   info card component reference
    color-tokens.html             ←   full color palette with contrast ratios
    link-styles.html              ←   link color states reference
    table-styles.html             ←   data table, sortable headers, filter toolbar
    form-styles.html              ←   segmented control, toggle switch, validation
    DESIGN-PROGRESS.md            ←   decisions made, what's pending

  public/                         ← arxiv.org + abstract pages (in progress)
    README.md                     ←   scope and status
```

## Tech context

arXiv's production frontend spans multiple stacks accumulated over 30+ years:
- **Cloud-native:** Python (Flask/Jinja) + React
- **Legacy:** PHP, Perl/CGI, static HTML
- Components must work across stacks — the design system uses plain CSS custom properties (no build step, no framework dependency)

## Key decisions

### Typography
All platforms use the IBM Plex type family, self-hosted (no Google Fonts, no Adobe Typekit). See `design-patterns/typography.md` for the full spec, font stack, and migration plan from current fonts (Rival Sans, Freight).

### Color
- **Primary palette:** Repository Brown + Library Grey (neutrals), Link Blue + Archival Blue + Open Blue (blues)
- **Internal accent:** Access Lime — signals "staff tools"
- **Public accent:** Open Blue — primary buttons on public pages
- **Heritage:** Campus Red (formerly Cornell Red) — logo X only, used sparingly post-spinout
- See `design-patterns/color-mapping.md` for the full palette and usage rules

### Accessibility
WCAG 2.1 AA compliance is mandatory — the Accessible Canada Act floor, adopted via CAN/ASC–EN 301 549. arXiv targets WCAG 2.2 AA in practice. See `DESIGN-POLICIES.md` for all accessibility rules. The color palette was audited and a new token (`--grey-ui` at `#8b8680`) was added to fill a contrast gap.

### Versions
Version information appears on both admin tools and public pages, so treat it as one shared pattern — but design it from the context below rather than a fixed layout, so future work isn't boxed in.
- **Who cares, and who doesn't.** Authors, publishers, and overlay journals care a lot about versions — provenance, and citing or linking a *specific* version. Readers usually don't: they want the latest and dive straight into reading.
- **The distribution is lopsided.** The vast majority of papers have a single version; some have two or three; a tiny minority have many. Any version affordance must accommodate the whole spectrum: near-silent when there's only one version, scannable at a few, and unbroken when there are 20+.
- **Current treatment.** Prior versions render as inline text links (Link Blue, underlined); the version being viewed is bold Repository Brown with `aria-current`, not a link. An older-version notice uses the `.ds-alert` warning variant. This supersedes the earlier "filled version pills" idea (see `design-patterns/color-mapping.md`).

### Cornell spinout
arXiv is spinning out from Cornell into an independent 501(c)(3). This drives several design changes:
- Cornell logo and red header bar are being removed
- Typekit font access (Rival Sans, Freight) will be lost — replaced by self-hosted IBM Plex
- The new public header is a single dark bar with the arXiv logo and minimal navigation
- Campus Red is retained as a heritage accent, not a primary color

## What the design draws from — user feedback

The decisions in this system are grounded in arXiv user research, not taste. The major recurring themes below are what the design responds to; each notes roughly what it drove. For the raw feedback, see *Where the feedback lives* at the end.

1. **HTML is first-class, not a PDF afterthought.** The strongest, most consistent signal — loudest from accessibility users ("HTML + MathML and you are done"). *(accessibility interviews; UX Research Hub; GitHub issues)*
2. **The interface should get out of the way.** Roughly half of closed UX issues reduce to "your interface is in my way". *(GitHub issues; UX Research Hub)*
3. **Core tasks must be obvious and easy.** Make it easy to read a paper, download a PDF, find a citation, and surface ancially files. *(UX Research Hub; BPS 2025; accessibility interviews)*
4. **Keep the paper sovereign — don't crowd it with non-paper content.** Most user feedback after adding the Labs tabs to the abstract page were highly negative ("This is an actively bad idea," "keep it simple and clean"). A small minority welcomed the new features. *(UX Research Hub; BPS 2025)*
5. **Reference and citation navigation must work for both sighted and AT users** The single most-filed reader bug was that footnote/citation links and hover popups were unusable. Wayfinding should be seamless and users whould never feel like they have lost their place. *(GitHub issues; accessibility interviews)*
6. **Core tasks should be owned by arXiv.** Example: Bibliographic Explorer was the most-used Lab, but was unsupported and buggy. Finding citation info is a core task for researchers so we are bringing the feature in-house. *(Labs audit; UX Research Hub)*
8. **Accessibility is a floor, not a feature.** Accessibility goes way beyond color contrast and aria tags. It includes semantic structure (headings/landmarks), wayfinding that works for all users, keeping extraneous content to a minimum, providing multiple formats for papers and math, keyboard reachability, reduced motion, forced colors, JS-off usability, and flexible and responsive typography. *(accessibility interviews; GitHub issues)*
9. **Mobile reality: small screens, small targets.** Never let header chrome eat the mobile viewport, keep tap targets generous, and ensure flexible layouts still make sense when stacking in narrow viewports. *(UX Research Hub; GitHub issues)*

### Where the feedback lives

- **BPS 2025 Annual Survey** — 9,419 respondents; design/UX comments volunteered in open-ended responses.
- **UX Research Hub (Jira)** — the running log of user observations and quotes (2019–present).
- **GitHub — arXiv/html_feedback** — ~180 UX-labeled issues (open + closed), mostly HTML-reader bugs.
- **Accessibility interviews** — 42 interviews with assistive-technology users and experts (2022–2023).
- **arXiv Labs audit** — functional review of 16 Labs integrations (2026).

Synthesized writeups of each (themes, quotes, provenance) live in the UX research references folder.

## Scope

**Internal tools (active):** The `internal/` patterns cover arXiv Check (moderation tool) and the Admin Console. These are staff-facing tools with a utilitarian, information-dense design language.

**Public-facing pages (in progress):** The `public/` patterns are being developed starting with the abstract page (arXiv's most-visited page, ~2M views/month). HTML mockups exist for the redesigned header, footer, abstract page layout, citation section, and HTML paper reader. These mockups live in a separate working directory and will be codified into pattern pages as they stabilize.

## How to modify

- Check `DESIGN-POLICIES.md` for hard constraints before making changes
- Use tokens from the palette documented in `color-mapping.md` — don't introduce one-off hex values
- Use fonts from the stack documented in `typography.md` — don't introduce new font families
- After adding or changing a component pattern, update the relevant pattern page
- When a policy or spec conflicts with a mockup's current implementation, the policy wins — update the mockup
