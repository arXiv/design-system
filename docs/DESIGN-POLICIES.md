# Design Policies

Hard constraints for all arXiv frontend work — internal tools and public-facing pages. These are non-negotiable rules, not suggestions. Verify compliance before submitting changes.

---
## Contexts: internal, public, outreach

Every arXiv frontend belongs to one of three contexts. The first two set the primary-action color; the third builds on public.
- **Internal tools:** Staff-facing workspaces such as the moderation queue and the Admin Console (arXiv Check) use Access Lime as the primary action color and lighter green tints for backgrounds.
- **Public pages:** Everything a reader or author sees on arxiv.org, including listing, abstract, and HTML paper pages, use Open Blue as the primary action and tints of Repository Brown for backgrounds.
- **Outreach sites:** arXiv's less formal sites — the news blog, event and celebration mini-sites, campaign pages. They *extend* the public design rather than mirroring it, and are allowed to be more playful and more colorful than arxiv.org would ever be. The agreed differences are listed on [the outreach page](outreach/). Accessibility, self-hosted fonts, and every other rule in this document apply to them unchanged — the licence is on tone and palette range, not on the floor.
- **The blog theme is a separate project.** It lives in its own repo and ships its own copy of the public stylesheet, because a WordPress theme cannot link one across origins. That copy is **expected to diverge**, and is brought up to date by a deliberate translation pass — someone decides which changes belong there and how they should read in the blog's voice. Never sync it opportunistically, and never overwrite it with the canonical file: that discards decisions the theme made on purpose. `verification/check-drift.py` reports the differences as a NOTE for exactly this reason — the list is the agenda for the next translation, not a defect.
- The internal/public split is not a stylistic choice: the accent tells the person which context they are working in, so the two must never be crossed. A lime primary button on a public page, or an Open Blue primary button on a staff tool, is a violation regardless of how well it reads. When the context is genuinely ambiguous (a shared component or an embedded widget), ask and settle which one the user is in before building, then record the answer in a code comment.
- **A privileged control on a public page stays public** (settled 2026-09-08, from a dashboards question). A staff-only action rendered on a public page — an admin button on a user dashboard, a moderation action on an abstract page — keeps Open Blue. The reader is using the public product with one extra power, not visiting a staff tool, and the accent answers *where am I*, not *what may I do*. Signal the privilege some other way: a `.ds-tag--chrome` label, wording that carries it ("Approve as moderator"), or the destructive tier if the action destroys something. Those survive greyscale, dark mode, and a reader who has never seen the other accent to contrast against.
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
- **UI component contrast:** 3:1 minimum for interactive boundaries (borders, outlines, tracks) against their background
- **Focus indicators:** All interactive elements must have a visible focus ring on keyboard navigation. Use `:focus-visible` (not `:focus`) to avoid showing rings on mouse click
- **Labels:** Every form input must have an associated `<label>` (visible or `sr-only`). Use `aria-label` when a visible label is impractical
- **Required and optional fields:** Mark the *optional* ones, in words — `(optional)` inside the visible label. Leave required fields unmarked, and put `required` + `aria-required="true"` on the control, which is what assistive technology announces. Two reasons for words over an asterisk: a word machine-translates and reads plainly for an international audience with limited English (the same reason contractions are banned), while an asterisk is a convention you must already know and means nothing without a legend the reader has scrolled past. And red is reserved for errors — an empty required field is not an error. Marking only the exception also keeps single-purpose pages clean: most arXiv forms are entirely required, and labelling every field on them would distinguish nothing. Never put either word in `aria-label` or `title`; it must be in the visible label, where it joins the accessible name for free
- **Validation errors:** Link error messages to their field with `aria-describedby`
- **Color alone:** Never use color as the sole means of conveying information (WCAG 1.4.1). Always provide a secondary cue (text, icon, position change)
- **Link underlines:** Inline links in body text must be underlined. Standalone navigation links may omit underlines
- **Responsive design:** All pages must be usable at any screen width. Layouts should be mobile-first and degrade gracefully. No horizontal scrolling on any device.

## Typography

- **What each family is for.** The type family is IBM Plex, plus STIX Two Math for notation. Each face has a job:
  - **IBM Plex Sans** — body copy, headings, and interface text. The default: where nothing below applies, this is the answer.
  - **IBM Plex Sans Condensed** — labels, captions, table headers, and metadata, usually small and uppercase.
  - **IBM Plex Mono** — identifiers and code: arXiv IDs, DOIs, BibTeX, code blocks.
  - **IBM Plex Serif, italic** — the annotation voice: arXiv speaking quietly beside the author's text, as in footnote and figure alt-text marginalia (`.ds-annotation`). It is a voice, not a layout role; placement is a separate decision.
  - **IBM Plex Serif, upright (400 / 600)** — editorial headlines and pull quotes on outreach properties.
  - **STIX Two Math** — mathematical notation.

  Adding a face or a family is a decision, recorded here. `docs/typography.html` holds the full spec, including sizes and weights.
- **Fonts are served from arXiv's own static assets**, self-hosted. This one is a hard constraint rather than a default: an external font service (Google Fonts, Adobe Typekit, a CDN) makes every reader's visit observable by a third party and makes the archive's rendering depend on someone else staying up. Neither is acceptable for a permanent record.
- **Font display:** Use `font-display: swap` for text fonts (prioritize readability). Use `font-display: auto` for STIX Two Math (math rendering needs the correct font).
- **System fallbacks:** Every `font-family` declaration must include system fallbacks. See `typography.md` for the standard stacks.

## Design tokens

- **Every token is prefixed `--ds-`**, matching the `.ds-` class names — one namespace idea across the whole system, not two. The prefix marks what belongs to the design system and is therefore not a page's to redefine, which is the useful distinction on an arXiv page carrying a hundred custom properties, most of them arXiv's own. It also keeps us clear of the ar5iv stylesheet's unprefixed variables, which arrive with the LaTeXML version rather than being authored here.
- **Name the role, not the colour.** `--ds-text`, not `--ds-repository-brown`; `--ds-accent`, not `--ds-open-blue`. Colours may change, roles are more stable — and a colour name stops being true the moment the theme flips, so a token called brown holding `#f0eeec` in dark mode is a trap for whoever reads it next. Brand colour names belong in the documentation and in the primitive layer, never attached to a role.
- **A tier 2 stylesheet may re-point a tier 1 semantic token** for its surface — that is theming, and it is how a staff surface sets its accent. It must never introduce a token that reuses a tier 1 name for a different meaning, and its own tokens take the same `--ds-` prefix, named for things that exist only on that surface (`--ds-marginalia-width`, not `--ds-main-width`).
- **One name, used everywhere.** Each token has exactly one name and every codebase uses it exactly as written — this repo, the dashboards, the search pages, the HTML papers reader, a bug report. No per-repository prefixes and no mapping tables: a mapping that lives in another repo is invisible to everyone here and to every check we run.
- **Values are the source of truth.** When in doubt, the hex values and behavior defined in `design-system.css` are authoritative. If a framework's token differs from the design system value, the design system wins.

## Spacing

- **Scale.** Use the 4px-based scale (`--ds-space-1`…`--ds-space-12` in `design-system.css`): 4, 8, 12, 16, 24, 32, 48. The number is the multiplier — `--ds-space-6` is 6×4px. Only those seven stops exist, so an off-scale value (14, 26, …) has no token to hide behind.
- **In rem, not px.** Spacing scales with the reader's text size. A fixed gap beside growing text compresses the rhythm exactly for the person who asked for more room, and the *ratio* between "within" and "between" is what carries meaning, so it has to survive.
- **Name the break, not the value.** Pages use `--ds-space-tight` (inside a group), `--ds-space-block` (between blocks in a section) or `--ds-space-section` (between sections). Never a pixel value, and never a raw `--ds-space-N`. That is what makes rhythm retunable: change what a break *means* and every page moves together, coherently.
- **Proximity.** The gap between sections must be clearly larger than the gap within one — block is 2× tight, section is 3× block. Below about 1.5× the eye cannot tell "between" from "within" and the grouping silently fails. This is what makes grouping read without borders or boxes.
- **Containers own the space between regions.** A section does not know what follows it, so it cannot know how far away that should be. Put the space on the container as `gap`, not on each child as a margin: gap never collapses, cannot be undone by a child, and needs no last-child resets. Prose flow *inside* a section stays element-owned, because a heading's space depends on its own size, which a container cannot know. Two mechanisms, at two clearly separated levels, never competing at the same one.
- **Gap takes no scale of its own.** "How far apart do these sit" means the same thing whether the space comes from a margin or a gap, and whether it runs down the page or across it, so gap between siblings uses the rhythm above on either axis. One exception: the space between a glyph and its label *inside* a single control is part of the control rather than layout — use `--ds-gap-glyph` (0.5em), which scales with that control's own type. This is the same exemption already given to button padding.
- **A set of related controls needs a container.** Buttons placed as bare siblings are spaced by the HTML whitespace between the tags, which is narrower than any deliberate value and looks like a bug because it is one. Use `.ds-btn-group`.

## Layout and content width

- **Content-driven, not audience-driven.** The same usability principle applies in every context; only the content differs, so there is no separate rule for "public" vs "internal."
- **One width per page.** The default content width is **850px** (`--ds-width-page` in `design-system.css`). Prose, tables, demo blocks, code and callouts all share it, so everything on a page has the same left and right edge. Individual elements do not declare their own width. A page that needs a different width changes the one token; it does not add a second width beside it.
- **Long-form reading narrows toward the measure.** Sustained reading — abstract text, a paper body, an extended explanation someone reads start to finish — targets a ~65-character line (~510px in IBM Plex Sans at a 16px root, ~590px at the 75-character upper bound). This is where the readability research applies most strongly, and where the return sweep between lines is most costly. Set it on the page, not on the paragraph.
- **Reference pages accept a longer line, knowingly.** At 850px a line runs about 109 characters, past the researched comfortable range. This is a deliberate trade for pages built from short reference paragraphs of two to five lines, where the return-sweep cost is smallest, and where a container narrow enough for 65 characters cannot hold a two-column layout at all. It is a cost, not a target: do not cite 850px as evidence that long lines are fine.
- **Dense internal tools may go wider.** Around 1080px, centered. The reason is tables and multi-column metadata that cannot compress further, not that staff deserve more room. Do not widen a page that has no such content.
- **Few breakpoints, named, and content-derived.** A breakpoint marks a structural change, not a device — there is no "tablet". Prefer, in this order: **a layout that needs no query at all** (a grid track that runs out is better than a rule that hides something), then **a container query** where a component asks about its own width, then a media query for genuinely page-level structure. Nine breakpoints inside 500px is not a design; it is one idea written down nine times.
- **Breakpoints are in rem when they are about text, px when they are about geometry.** A threshold governing whether a column of prose still reads should scale with the reader's text size. A threshold derived from fixed pixel widths should not, or it fires at a viewport the geometry does not agree with.
- **A threshold used by both CSS and JavaScript is declared once.** Put it in a custom property and have the script read it with `getComputedStyle`. `@media` cannot read custom properties, so the query repeats the literal — but the script must not carry a third copy.

## Colors

- **Use the palette.** All colors must come from the documented palette in `docs/color-mapping.md`. Do not introduce one-off hex values.
- **Warm grey ladder:** The palette provides specific stops for specific contrast needs:
  - `--ds-text-disabled` (`#b0aba6`) — disabled/exempt states only (2.24:1, below AA thresholds)
  - `--ds-border-strong` (`#8b8680`) — interactive UI boundaries: borders, tracks, arrows (3.61:1 on white, passes 3:1)
  - `--ds-text-muted` (`#6b6459`) — body-weight text, muted labels (5.83:1 on white, passes 4.5:1)
- **Semantic colors:** Use danger tokens (`--ds-danger`) only for destructive actions and error states. Not for brand accents.
- **Red means one thing: error.** Nothing else may use it — not required-field markers, not inline `<code>`, not emphasis. A form that spends red on a non-error state cannot then use red to mean "you cannot proceed."
- **Dimming:** Use `opacity` only for *transient or recoverable* dimming — a secondary control quieted until hover or focus returns it to full strength (`.ds-tag-remove`), or presence animated between 0 and 1. Persistent states use explicit colours. Opacity dims fill, border, shadow and label by the same amount, which is rarely what a state wants; it can render a light fill nearly invisible; and it creates a stacking context.
- **Campus Red (`#b31b1b`):** Heritage color only. Use for the logo X mark and rare accents. Never for headers, buttons, large color fields, or text.
- **Internal vs public:** Internal tools use Access Lime as the primary button color. Public pages use Open Blue. Do not cross these — the color difference signals which context the user is in.
- **Dark mode is live.** Build every page dark-aware from the start: take colors from tokens and they flip on their own. Never hand-pick a dark value into a page. Two things legitimately hold a fixed value in both modes — an accent that must not shift (text on a lime or Open Blue fill uses `--ds-text-on-accent` / `--ds-text-on-accent`), and a specimen whose color *is* the documentation (a swatch, a simulated state). If a demo must show one specific mode, put `data-theme` on the demo's own container — `<div data-theme="light">` — rather than locking the whole page; the tokens apply at any level and the nearest ancestor wins. Lock a whole page with `<html data-theme="light">` only when the entire page exists to demonstrate light-mode rendering. See `docs/dark-mode.html` for the mechanism and the traps.

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
- **Disabled state:** `cursor: not-allowed`, a flat neutral grey fill, and an explicit label colour — never opacity (see *Colors → Dimming*). Flat means no gradient, no inset vignette, no drop shadow: removing the "lit from above" construction is what distinguishes a disabled button from a live one, and every hover and active response must be cancelled too, or a dead control still feels live. The label must still clear AA, even though WCAG exempts disabled controls: a label nobody can read is worse than one they can, and the flat fill is already carrying the "unavailable" message. Public uses `--ds-surface-muted` fill with a `--ds-text-muted` label (5.05:1 light, 6.51:1 dark — both tokens flip, so no hand-picked dark value). Disabled is neutral in every variant: the message is "you cannot use this," which does not need to also encode which button it was.
- **`aria-disabled` and `disabled` look identical:** a control that is unavailable-but-focusable must be visually indistinguishable from one that is inert. The difference between them is behavioural, not visual, and the user has no use for it. Prefer `aria-disabled` for anything that should still be able to explain itself (see *Content and interaction*).
- **Three tiers, built differently in each context:** primary, secondary, and a quiet third tier. The third tier is reached by removing whatever the surface's secondary uses to hold the page — public secondary leans on its border, so `.ds-btn-text` drops the border and keeps no fill; internal secondary leans on a lime fill, so `.btn-tertiary` drops the fill and keeps a border. Never add a tier whose only difference from its neighbor is a shadow.
- **Text buttons are not links:** a text button carries Link Blue but is never underlined, and its hover feedback is a background wash. Underlines belong to links (inline always, standalone on hover). If a control navigates, make it a link.
- **Icons in buttons** are sized in `em` so they track the button's own font-size, and never shrink when the label is long.

## Content and interaction

- **Category names are copied, never restyled.** Show a category exactly as arXiv publishes it — `cs.AI`, `physics.optics`, `cond-mat.str-el` — capitalization included. Never uppercase, lowercase, or otherwise transform it for display. The same string appears in the URL, in the API, and in what researchers type, so changing its case makes it a different string. Most categories are uppercase after the final period, but every `physics.*` and `cond-mat.*` subcategory is lowercase — which is why this is a copy rule and not a capitalization rule. The same holds for any arXiv identifier, a paper ID included.
- **Tags label or categorize; they never stand in for a link.** A tag is the small rounded label used for subject categories, topics, and states. It may link to a listing, but it must never replace a text link as the way to get somewhere — which is why version links are inline text and not filled pills. When a tag carries a status color, that color reports a real condition; never use one for emphasis.
- **Submission type badges:** Use the established palette: `.ds-badge--new` (blue), `.ds-badge--rep` (yellow), `.ds-badge--wdr` (dark), `.ds-badge--cross` (light grey)
- **Segmented controls:** Use semantic variants — `.ds-seg-btn--positive` (green/accept), `.ds-seg-btn--neutral` (blue/informational), `.ds-seg-btn--negative` (red/reject)
- **Filter dropdowns:** Use `.ds-filter` with a visible `<label>`. Always include an "All" option as the inclusive default.
- **Toggle switches:** Off state uses `--ds-border-strong`. On state uses lime green (internal) or Link Blue (public). Label text uses `--ds-text-muted` (off) shifting to a darker shade (on).

## Writing

- **No contractions.** Write "do not," not "don't." arXiv's audience is international and many readers have limited English, so the compressed form costs them a parsing step. Applies to everything with words — interface copy, error messages, documentation, alt text, commit messages. Possessives are unaffected ("arXiv's palette" is correct).
- **One name per thing.** A component is called what the stylesheet calls it, in every document and every string. Never substitute a synonym.
- **Load-bearing text is stricter.** Error messages, form help, and instructions follow the additional rules in [STYLE.md](STYLE.md), which carries the full set and the reasoning behind it.

## Public pages — additional policies

- **No metrics display:** arXiv does not display view counts, download counts, or citation counts on public pages. This is a core operating value — arXiv does not promote or rank papers.
- **Citation export:** On abstract pages, we provide BibTeX (default), APA, Chicago, and MLA formats. Generate from metadata to save manual work for the user.
- **arXiv Labs:** Labs tools that collect user data must be behind an opt-in toggle, not on by default (this policy is still in the early implementation phase as 6/24/26 and not enforced for Labs yet). Labs that require login to a third party platform should be deprioritized in placement.
- **Header:** Single bar. Black (phase 1, spinout) transitioning to Repository Brown (phase 2). Logo, Search, Submit, Donate, Log in. No Cornell branding post-spinout. Outreach sites may run an Open Blue header instead — an agreed exception for them, never valid here.
- **Footer:** Acknowledgment text (Simons Foundation, member institutions, IP matched institution name). Links: About, Help, Contact, Subscribe, Copyright, Privacy, Accessibility, Status. Special section for major funders on the right side. All acknowledgements are presented in the footer, never in the header.
- **Banner:** A minimal and time-bound banner can be displayed with short announcements. It includes a small icon, a short sentence and link, and a dismiss button. After dismissing, the banner should not display for that user again.

## Chrome and interaction structure


- **Sticky chrome is exceptional.** The HTML paper reader is the only page approved to use a sticky header — it alone is a long-document reading context that earns persistent chrome. Do not add sticky chrome to other pages without explicit approval. Any page that does carry sticky chrome MUST set `html { scroll-padding-top }` to at least the chrome's tallest state plus breathing room (reader reference: 80px), covering every anchor path including JS `scrollIntoView`. The abstract-page header is static — it scrolls away like any other content, so the reader is the only sticky-chrome surface in fact as well as intent.
- **arXiv's universal navigation stays short.** The constraint is on arxiv.org's own top-level navigation, not on the header component: five items (Search, Submit, Donate, Log in + logo). Resist link-creep permanently. Other properties built on the same component — the design system documentation, info and outreach sites — carry the navigation their content needs, including grouped menus, and are not bound by this number. Narrow viewports condense (wrap or compact grammar) rather than hamburger; a hamburger is a permitted last-resort fallback at very narrow widths, never the default.
- **Z-layer scale.** Content chrome (pills, marginalia) < 50 · popovers 50 · header-attached dropdowns 60 · sticky headers 100 · ~150 reserved for toasts/notifications · skip link/overlays 200 · modal dialogs use the native `<dialog>` top layer (no z-index). Do not introduce ad-hoc z-index values. *Values note: arXiv wants very few toasts/notifications at all — anti-corporate, anti-advertising is part of the brand.*
- **Target size.** Hard floor 24×24 CSS px (WCAG 2.2 SC 2.5.8 AA), with WCAG's own exceptions (inline targets within a sentence — citation chips, version links — spacing-equivalent, user-agent defaults). Design target 44×44 on touch-primary surfaces (full-screen menus, mobile pill bars, toggles) — where Apple HIG, BBC GEL, and Android guidance converge. Use the padding + negative-margin technique to grow hit areas without changing layout.
- **Reduced motion covers JavaScript.** `prefers-reduced-motion: reduce` must disable ALL motion: CSS transitions/animations AND JS-driven motion — `scrollIntoView({behavior:'smooth'})` ignores CSS rules, so JS must check `matchMedia('(prefers-reduced-motion: reduce)')` per call.
- **Progressive enhancement: scripts never carry content.** Server-rendered HTML is complete and readable before any JavaScript runs. Anything hidden pending a JS reveal is scoped under `html.js`; controls that do nothing without JS are hidden without it; controls with a meaningful non-JS equivalent degrade to it (search button → search-page link).
- **Truncation always signals continuation.** Preference order: (1) disclosure with an explicit count ("show all 1,247 authors") over internal scrolling; (2) where a region must scroll internally, size it so the last visible item is visibly cut mid-item (the half-item peek — a geometric signal that survives forced-colors, zoom, and user stylesheets); (3) fade masks are decoration only, never the sole signal. Every scrollable region is keyboard-reachable (`tabindex="0"`) with an accessible name carrying the total, uses real list semantics, and keeps its exit/collapse controls inside the region.

---

*These policies expand as UX research and production requirements are incorporated. When a policy conflicts with a mockup's current implementation, the policy wins — update the mockup.*
