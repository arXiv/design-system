# Handoff — 2026-09-28

Written for the next session. Everything below is committed and pushed to
`master` unless it says otherwise.

## Where the programme is

The documentation is the work. Every pattern page has been brought to one
shape (see *The page shape* below) and Shamsi is reviewing the pages one at
a time, visually, sending notes as she goes; the session acts on the notes,
she wordsmiths the prose herself. That loop is the whole job right now.

Reviewed by her so far (notes acted on): buttons, alerts, tags, messages,
icons, using, links, header, cards, colors, dark-mode (her prose pass on
dark-mode.html was committed 2026-09-28). Not yet reviewed: forms, modals,
progressive-disclosure, spacing, typography, version-display,
organizing-content, footer, tables, brand, outreach.

Digests (`docs/spec/<page>.md`, for agents) exist only for pages on
`verification/reviewed-pages.txt`: buttons, alerts, tags, messages. Add a
page there when she says it is finished; `gen-digest.py` does the rest.

Verification, all clean at handoff:

    python3 verification/check-policies.py    policies, page shape, documented classes, toc.js on every bar
    python3 verification/check-drift.py       dark mirror = media block (tier 1 and tier 2)
    python3 verification/check-contrast.py    63 promised text pairings clear AA in both themes (no generated table any more)
    python3 verification/gen-anchors.py       run after editing any heading; fills each page's contents list
    python3 verification/gen-digest.py        run after editing a reviewed page
    python3 verification/gen-icons.py         run after adding an icon to docs/icons/

## Read this before touching anything

- **Several people and sessions edit this repo.** Stage specific files; never
  `git add -A` blindly. At handoff there is one untracked folder,
  `whiteboard/mockups/public/user-portal/` (five PNG screenshots of the current user
  portal, dropped 2026-09-25, not yet discussed): leave it alone.
- **She wordsmiths; the session does structure, deletion and code.** When her
  draft is wrong on a fact or a mechanic (contraction, typo, broken markup,
  indented code block, duplicate id), fix it and say so; otherwise leave her
  sentences. Every sentence the session or an agent writes is listed for her.
- **No contractions** in anything arXiv-facing. **Never narrate history** on a
  page (`check-policies.py` enforces). **One fact, one home.**
- **Ask before inventing** a class, a token or a colour. The docs use only
  the design system; docs-only scaffolding goes in `docs/docs.css`; no page
  carries a `<style>` block.
- Decisions she has made are in the git log; do not re-open them. The big
  ones since 2026-09-18: bare classes are the defaults (`.ds-btn` is the
  secondary tier, `.ds-alert` is info, `.ds-seg-btn` is neutral,
  `.ds-toc-bar` is always sticky); one card family for both surfaces
  (`.ds-card`, `.ds-card--data`, `.ds-card-grid`; internal colours come only
  from `.ds-internal` on a parent); two colour ramps (`--ds-grey-5/10/25/55/80`
  from Library Grey, `--ds-blue-20/50/70` from Open Blue; roles point at
  steps); the theme control is icon only (state in the accessible name);
  every link inside `.ds-page` is the link (`.ds-link` is gone); at most four
  top-level links in the arXiv header; `internal/`, `public/`, `outreach/`
  folded into `docs/`; metadata-panel, color-tokens and internal/buttons
  pages deleted.

## The page shape (every pattern page)

`<body class="ds-page">` → shared nav (copied verbatim from buttons.html) →
`.ds-container.ds-zone-secondary` holding `.ds-page-header` (h1 + lede),
the contents bar (`.ds-full.ds-toc-bar`, list generated), then one
`.ds-full.ds-zone-primary` band with one `<section>` per
buildable thing (an `h2` with an id as its first element, `p.ds-section-desc`, every example in a
`.ds-card` whose last child is a "Relevant code" accordion: markup first,
then a `<dl>` class key), then the Accessibility essentials note; after the
band, plain `<h2>` group headings (Modifiers / Rules / Spec) with
`<section>` elements opened by an `h3`, or nothing if there is nothing. Public and
internal examples share markup; the internal one sits in a wrapper with
`class="ds-internal"`. Scripts at the end: copy-code.js, anchors.js, toc.js
(deferred); theme.js in the head, not deferred.

## Open, in her hands

- Whether the two tables merge: tier 1 `.ds-table-framed` (docs spec
  tables) and tier 2 `.ds-table` (internal data table) are shown together
  on tables.html for the decision.
- tables.html is still built as an internal-only page (`.ds-internal` on
  `<html>`); showing both surfaces on it is a later pass.
- Which pages to mark finished for digests.

## Open, ours

- Tier 1 gaps the prose pages exposed: prose directly after a `.ds-card-grid`
  has no rhythm rule; `<figure>`/`<figcaption>` carry browser margins; no
  stat-number display (brand page). Promote only when a real page needs it.
- The paper mockup (`whiteboard/mockups/public/html-phase1.html`) still uses its own
  `.mg-toc-*` bar and `.ds-site-header--wrap`, which tier 1 no longer has;
  moving it onto the promoted zones and contents bar is queued for after the
  docs review. Leave mockups alone until then.
- Backlog from `whiteboard/planning/NEXT-STEPS.md` and `whiteboard/planning/DIGEST-PLAN.md`: the
  agent benchmark on digests once more pages are reviewed; the AGENTS.md
  spine rewrite; the in-progress button state (item 21); the page renderer
  from structured source.

## Conventions worth not rediscovering

- Modifiers take a double dash (`.ds-alert--error`), parts a single dash
  (`.ds-alert-title`); tokens are `--ds-<role>`, primitives `--ds-<colour>`
  or `--ds-<ramp>-<step>`.
- Type sizes are `rem`; a control's padding is `em` against its own label;
  controls clear a 24px target.
- Tier 2 (`docs/internal-tools.css`) holds only what internal tools alone
  have. Never copy a component into it to restyle: that is a token.
- Dark mode: media block, `[data-theme="dark"]` mirror, `[data-theme="light"]`
  restore; a fixed light value (the chrome bar, code blocks) is a fixed step,
  never a flipping token.
- Inline code and the disabled button fill are washes of the text colour
  (`color-mix`), so they show on every ground in both themes.
- The docs header wordmark is one shown span and one spoken span, so screen
  readers say "archive".
