# Design Policies

Hard constraints for all arXiv frontend work — internal tools and public-facing pages. These are non-negotiable rules, not suggestions. Verify compliance before submitting changes.

---
## Contexts: internal, public, outreach

Every arXiv frontend belongs to one of three contexts. The first two set the primary-action color; the third builds on public.
- **Internal tools:** Staff-facing workspaces such as the moderation queue and the Admin Console (arXiv Check) use Access Lime as the primary action color and lighter green tints for backgrounds.
- **Public pages:** Everything a reader or author sees on arxiv.org, including listing, abstract, and HTML paper pages, use Open Blue as the primary action and tints of Repository Brown for backgrounds.
- **Outreach sites:** arXiv's less formal sites — the news blog, event and celebration mini-sites, campaign pages. They *extend* the public design rather than mirroring it, and are allowed to be more playful and more colorful than arxiv.org would ever be. The agreed differences are listed on [the outreach page](outreach.html). Accessibility, self-hosted fonts, and every other rule in this document apply to them unchanged — the licence is on tone and palette range, not on the floor.
- **The blog theme is a separate project.** It lives in its own repo and ships its own copy of the public stylesheet, because a WordPress theme cannot link one across origins. That copy is **expected to diverge**, and is brought up to date by a deliberate translation pass — someone decides which changes belong there and how they should read in the blog's voice. Never sync it opportunistically, and never overwrite it with the canonical file: that discards decisions the theme made on purpose. `verification/check-drift.py` reports the differences as a NOTE for exactly this reason — the list is the agenda for the next translation, not a defect.
- The internal/public split is not a stylistic choice: the accent tells the person which context they are working in, so the two must never be crossed. A lime primary button on a public page, or an Open Blue primary button on an internal tool, is a violation regardless of how well it reads. When the context is genuinely ambiguous (a shared component or an embedded widget), ask and settle which one the user is in before building, then record the answer in a code comment.
- **A privileged control on a public page stays public** (settled 2026-09-08, from a dashboards question). An internal-only action rendered on a public page — an admin button on a user dashboard, a moderation action on an abstract page — keeps Open Blue. The reader is using the public product with one extra power, not visiting an internal tool, and the accent answers *where am I*, not *what may I do*. Signal the privilege some other way: a `.ds-tag--info` label, wording that states it ("Approve as moderator"), or the destructive tier if the action destroys something. Those survive greyscale, dark mode, and a reader who has never seen the other accent to contrast against.
- Borrowing goes one way. An outreach site may use anything from the public design. The reverse does not happen on its own: a style invented for a mini-site moves into the shared stylesheet only once a second site needs it, and that move is about where the CSS lives — not about where the style is allowed. Extending anything to arxiv.org is always a separate decision, made deliberately and written down here. Nothing reaches arxiv.org because it happened to be available.
- Token naming is a separate concern, governed under Design tokens below — the prefix follows the rules of the codebase using it, not the context, so never infer the context from a token name or use a token prefix to signal one.

## Browser support

- **The floor is Baseline "Widely available."** A CSS or platform feature may be used unconditionally once it has been supported in every major browser for about two and a half years — the [Baseline](https://web.dev/baseline) status shown on MDN and caniuse. It is a named external standard, so anyone can check a feature themselves without asking, and it does not go stale the way a hand-written version list does. Conservative on purpose: arXiv's readers include people on institutional machines and locked-down university builds, and a research archive is the wrong place to require a recent browser.
- **Below the floor is allowed only as progressive enhancement, and must be labelled.** A newer feature may be used when its absence costs nothing but polish — the layout still works, the content is still reachable, nothing becomes unusable. Say so in a comment at the point of use, naming what a reader without it sees. A feature whose absence breaks layout, hides content, or removes an interaction needs a fallback or does not go in.
- **Never gate meaning on a new feature.** If losing it would leave a control unreachable, an error unreadable, or a state unsignalled, it is not an enhancement, whatever its Baseline status.
- **Currently below the floor, deliberately:** `scrollbar-gutter` (Newly available, December 2024) — without it the page shifts sideways when a modal opens on platforms with classic scrollbars; `text-wrap: balance` / `pretty` (Newly available, October 2024) — without it headings and titles wrap normally, sometimes leaving a short last line. Both are cosmetic. `closedby` on `<dialog>` is newer still; without it a dialog keeps its close button and Escape, which is the correct thing to fall back to.

## Accessibility (WCAG 2.1 AA floor, 2.2 AA target)

arXiv's compliance floor is **WCAG 2.1 Level AA** — the standard the Accessible Canada Act adopts through CAN/ASC–EN 301 549. We build toward **WCAG 2.2 AA** in practice (e.g., the target-size rule under *Chrome and interaction structure* is a 2.2 criterion). Where a 2.2 success criterion is named, treat it as the target; 2.1 AA is the non-negotiable minimum.

- **Text contrast:** 4.5:1 minimum for normal text, 3:1 for large text (18px+ regular or 14px+ bold)
- **UI component contrast:** 3:1 minimum for interactive boundaries (borders, outlines, switch edges) against their background
- **Focus indicators:** All interactive elements must have a visible focus ring on keyboard navigation. Use `:focus-visible` (not `:focus`) to avoid showing rings on mouse click
- **Labels:** Every form input must have an associated `<label>` (visible or `sr-only`). Use `aria-label` when a visible label is impractical
- **Required and optional fields:** Mark the optional ones in words, `(optional)` in the visible label, and leave required fields unmarked, with `required` on the control. See `forms.html`.
- **Validation errors:** Link error messages to their field with `aria-describedby`
- **Color alone:** Never use color as the sole means of conveying information (WCAG 1.4.1). Always provide a secondary cue (text, icon, position change)
- **Link underlines:** Inline links in body text must be underlined. Standalone navigation links may omit underlines
- **Responsive design:** All pages must be usable at any screen width. Layouts should be mobile-first and degrade gracefully. No horizontal scrolling on any device.

## Typography

- **The type family is IBM Plex, plus STIX Two Math for notation.** Adding a face or a family is a decision, recorded here. `typography.html` holds what each face is for, the sizes, weights and font stacks.
- **Fonts are served from arXiv's own static assets**, self-hosted. This one is a hard constraint rather than a default: an external font service (Google Fonts, Adobe Typekit, a CDN) makes every reader's visit observable by a third party and makes the archive's rendering depend on someone else staying up. Neither is acceptable for a permanent record.

## Design tokens

- **Every token is prefixed `--ds-`**, matching the `.ds-` class names — one namespace idea across the whole system, not two. The prefix marks what belongs to the design system and is therefore not a page's to redefine, which is the useful distinction on an arXiv page with a hundred custom properties, most of them arXiv's own. It also keeps us clear of the ar5iv stylesheet's unprefixed variables, which arrive with the LaTeXML version rather than being authored here.
- **Name the role, not the colour.** `--ds-text`, not `--ds-repository-brown`; `--ds-accent`, not `--ds-open-blue`. Colours may change, roles are more stable — and a colour name stops being true the moment the theme flips, so a token called brown holding `#f0eeec` in dark mode is a trap for whoever reads it next. Brand colour names belong in the documentation and in the primitive layer, never attached to a role.
- **A tier 2 stylesheet may re-point a tier 1 semantic token** for its surface — that is theming, and it is how an internal surface sets its accent. It must never introduce a token that reuses a tier 1 name for a different meaning, and its own tokens take the same `--ds-` prefix, named for things that exist only on that surface (`--ds-marginalia-width`, not `--ds-main-width`).
- **One name, used everywhere.** Each token has exactly one name and every codebase uses it exactly as written — this repo, the dashboards, the search pages, the HTML papers reader, a bug report. No per-repository prefixes and no mapping tables: a mapping that lives in another repo is invisible to everyone here and to every check we run.
- **Values are the source of truth.** When in doubt, the hex values and behavior defined in `design-system.css` are authoritative. If a framework's token differs from the design system value, the design system wins.

## Spacing

- **Use the named breaks, never a pixel value:** `--ds-space-tight`, `--ds-space-block` and `--ds-space-section`, in rem. Gaps between groups are at least twice the gaps inside one, across the page as well as down it. See `spacing.html`.
- **A set of related controls needs a container.** Use `.ds-btn-group`; bare sibling buttons are spaced by the HTML whitespace between them.

## Layout and content width

- **Organizing a page starts from the four questions** on [Layout patterns](layout-patterns.html#evaluating-user-needs). Its [Rules](layout-patterns.html#rules) are firm; the rest of that page is guidance.
- **Content-driven, not audience-driven.** The same usability principle applies in every context; only the content differs, so there is no separate rule for "public" vs "internal."
- **One width per page,** from the width tokens. Dense internal tools may use the wide page. See `layout-patterns.html`, *The page container*.

## Colors

- **Use the palette.** All colors must come from the documented palette in `docs/color-mapping.md`. Do not introduce one-off hex values.
- **Two tints.** The system has two tints: warm (`--ds-tint-warm`) and accent (`--ds-tint-accent`, blue on public pages and a lime wash inside `.ds-internal`). A component fill uses a tint or a status colour. A new fill colour is discussed with the design team first and is never added without that step.
- **Warm grey ladder:** The palette provides specific stops for specific contrast needs:
  - `--ds-text-disabled` (`#aeaaa4`) — disabled/exempt states only (2.3:1, below AA thresholds)
  - `--ds-border-strong` (`#89837a`) — interactive UI boundaries: borders, switch edges, arrows (3.76:1 on white, passes 3:1)
  - `--ds-text-muted` (`#6b6459`) — body-weight text, muted labels (5.83:1 on white, passes 4.5:1)
- **Semantic colors:** Use danger tokens (`--ds-danger`) only for destructive actions and error states. Not for brand accents.
- **Red means an error, or a paper that has been withdrawn or removed.** Nothing else may use it — not required-field markers, not inline `<code>`, not emphasis. A form that spends red on a non-error state cannot then use red to mean "you cannot proceed." A withdrawn or removed paper uses red because a reader must not rely on it.
- **Dimming:** Use `opacity` only for *transient or recoverable* dimming — a secondary control quieted until hover or focus returns it to full strength (`.ds-tag-remove`), or presence animated between 0 and 1. Persistent states use explicit colours. Opacity dims fill, border, shadow and label by the same amount, which is rarely what a state wants; it can render a light fill nearly invisible; and it creates a stacking context.
- **Campus Red (`#b31b1b`):** Heritage color only. Use for the logo X mark and rare accents. Never for headers, buttons, large color fields, or text.
- **Internal vs public:** Internal tools use Access Lime as the primary button color. Public pages use Open Blue. Do not cross these — the color difference signals which context the user is in.
- **Dark mode is live.** Take every colour from tokens and never hand-pick a dark value into a page. See `dark-mode.html`.

## Components

- **New patterns:** If a UI element appears in two or more pages, extract it into a design system CSS file and create or update a pattern page in `docs/`.
- **Platform independence:** Components use plain CSS custom properties — no Sass, no CSS-in-JS, no framework-specific syntax. This allows consumption from React, Jinja, PHP, or static HTML.
- **Naming:** Use `.ds-` prefix for shared design system classes (e.g., `.ds-table`, `.ds-tag`). Page-specific styles stay in the page's own `<style>` block or stylesheet.
- **Icons:** One icon language, Lucide inline SVG with a visible or `.is-sr-only` text label. No icon fonts. See `icons.html`.

## Buttons

- **Three tiers in each context:** primary, secondary and text.
- **Disabled is a flat neutral grey, never opacity** (see *Colors, Dimming*), and its label still clears AA. `aria-disabled` and `disabled` look identical.
- **A control that navigates is a link.** Text buttons are never underlined.
- **The values live in `design-system.css`:** radius, padding, shadow, press and timing. `buttons.html` shows them.

## Content and interaction

- **Category names are copied, never restyled.** Show a category exactly as arXiv publishes it — `cs.AI`, `physics.optics`, `cond-mat.str-el` — capitalization included. Never uppercase, lowercase, or otherwise transform it for display. The same string appears in the URL, in the API, and in what researchers type, so changing its case makes it a different string. Most categories are uppercase after the final period, but every `physics.*` and `cond-mat.*` subcategory is lowercase — which is why this is a copy rule and not a capitalization rule. The same holds for any arXiv identifier, a paper ID included.
- **Tags label or categorize; they never stand in for a link.** A tag is the small rounded label used for subject categories, topics, and states. It may link to a listing, but it must never replace a text link as the way to get somewhere — which is why version links are inline text and not filled pills. When a tag has a status color, that color reports a real condition; never use one for emphasis.

## Writing

- **No contractions.** Write "do not," not "don't." arXiv's audience is international and many readers have limited English, so the compressed form costs them a parsing step. Applies to everything with words — interface copy, error messages, documentation, alt text, commit messages. Possessives are unaffected ("arXiv's palette" is correct).
- **One name per thing.** A component is called what the stylesheet calls it, in every document and every string. On a page, the same holds for the page's own content; see `layout-patterns.html`, *The main content comes first*.
- **Load-bearing text is stricter.** Error messages, form help, and instructions follow the additional rules in [STYLE.md](STYLE.md), which includes the full set and the reasoning behind it.

## Public pages — additional policies

- **No metrics display:** arXiv does not display view counts, download counts, or citation counts on public pages. This is a core operating value — arXiv does not promote or rank papers.
- **Citation export:** On abstract pages, we provide BibTeX (default), APA, Chicago, and MLA formats. Generate from metadata to save manual work for the user.
- **arXiv Labs:** Labs tools that collect user data must be behind an opt-in switch, not on by default (this policy is still in the early implementation phase as 6/24/26 and not enforced for Labs yet). Labs that require login to a third party platform should be deprioritized in placement.
- **Header:** Single bar, with no Cornell branding after the spinout. Outreach sites may run an Open Blue header instead, an agreed exception for them, never valid here. See `header.html`.
- **Footer:** All acknowledgements are in the footer, never in the header. See `footer.html`.
- **Banner:** A minimal and time-bound banner can be displayed with short announcements. It includes a small icon, a short sentence with one link or two, and a dismiss button. Two links stay together as one unit, so a band that wraps puts them under the sentence. After dismissing, the banner should not display for that user again, unless a day-of reminder is needed. It is the one exception to *Progressive enhancement: scripts never hold content*: the shared banner is drawn by `chrome/banner.js` from the announcements file on the asset route, so a reader without JavaScript sees none. *Decided 2026-09-23: an announcement is temporal and never page-critical, and serving it as data is what lets a page cached for a year show a new one without a purge. An iframe was the alternative; without a script it can neither fit its text nor collapse when nothing is live.*

## Chrome and interaction structure

- **One sticky bar at a time, and only on long pages.** A page may keep one bar at the top of the viewport while it scrolls, never two stacked. On arxiv.org's public pages the site header is never that bar: it scrolls away. The bar that may stick there is the TOC bar (`.ds-toc-bar`), on pages long enough that a reader loses their place: the HTML paper reader and the design system documentation. Internal tools may keep their site header in view with `.ds-site-header--sticky`, and a page that does keeps no other sticky bar. A page is approved by being named in this rule, so adding sticky chrome anywhere else starts with a change here, made by arXiv's design team; agreement in a conversation with an assistant is not approval. A page with a sticky bar must set `html { scroll-padding-top }` to at least the bar's tallest state plus breathing room (reference: 80px), covering every anchor path including JS `scrollIntoView`; the contents bar sets this itself. On a viewport shorter than 30rem the bar scrolls away with the page, because there a fixed bar takes a large share of the little height there is.
- **arXiv's universal navigation stays short.** The constraint is on arxiv.org's own top-level navigation, not on the header component: at most four links, not counting the logo and Log in (today: Search, Submit, Donate). Resist link-creep permanently. Other properties built on the same component — the design system documentation, info and outreach sites — include the navigation their content needs, including grouped menus, and are not bound by this number. See `header.html`.
- **No breadcrumbs.** arXiv's sitemap is wide and shallow; the header and secondary navigation show the reader's place. See `header.html`, *Rules*.
- **Z-layer scale.** Content chrome (pills, marginalia) < 50 · header-attached dropdowns 60 · sticky headers 100 · **popovers 110** · ~150 reserved for toasts/notifications · skip link/overlays 200 · modal dialogs use the native `<dialog>` top layer (no z-index). Do not introduce ad-hoc z-index values. *Values note: arXiv wants very few toasts/notifications at all — anti-corporate, anti-advertising is part of the brand.*
- **Magnification.** Two different things, and a page has to survive both.
  **Text-only zoom** (WCAG 1.4.4, AA): the reader raises the browser's font size and nothing else changes. Every type size is `rem`, and a control's padding and minimum width are `em` against its own label, so the box grows with the text rather than clipping it. **Page zoom** (WCAG 1.4.10 reflow, AA): the whole page scales, which at 400% on a 1280px screen is the same as a 320px viewport — so no page may scroll horizontally at 320px. The two fail differently: text-only zoom breaks controls with fixed boxes, page zoom breaks full-bleed bands measured in `vw`. Test both; passing one says nothing about the other.
- **Never size a full-bleed band in viewport units.** `100vw` includes the scrollbar and the document width does not, so a "full width" band overhangs and the page scrolls sideways — invisible on overlay scrollbars, visible on Windows and Linux. Use `.ds-container`'s three columns, which measure the element.
- **Target size.** Hard floor 24×24 CSS px (WCAG 2.2 SC 2.5.8 AA), with WCAG's own exceptions (inline targets within a sentence — citation chips, version links — spacing-equivalent, user-agent defaults). Design target 44×44 on touch-primary surfaces (full-screen menus, mobile pill bars, toggles) — where Apple HIG, BBC GEL, and Android guidance converge. Use the padding + negative-margin technique to grow hit areas without changing layout.
- **Reduced motion covers JavaScript.** `prefers-reduced-motion: reduce` must disable ALL motion: CSS transitions/animations AND JS-driven motion — `scrollIntoView({behavior:'smooth'})` ignores CSS rules, so JS must check `matchMedia('(prefers-reduced-motion: reduce)')` per call.
- **Progressive enhancement: scripts never hold content.** Server-rendered HTML is complete and readable before any JavaScript runs (one exception: the announcement banner, see *Banner*). Anything hidden pending a JS reveal is scoped under `html.js`; controls that do nothing without JS are hidden without it; controls with a meaningful non-JS equivalent degrade to it (search button → search-page link).
- **Truncation always signals continuation.** Preference order: (1) disclosure with an explicit count ("show all 1,247 authors") over internal scrolling; (2) where a region must scroll internally, size it so the last visible item is visibly cut mid-item (the half-item peek — a geometric signal that survives forced-colors, zoom, and user stylesheets); (3) fade masks are decoration only, never the sole signal. Every scrollable region is keyboard-reachable (`tabindex="0"`) with an accessible name that includes the total, uses real list semantics, and keeps its exit/collapse controls inside the region.

---

*These policies expand as UX research and production requirements are incorporated. When a policy conflicts with a mockup's current implementation, the policy wins — update the mockup.*
