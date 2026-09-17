# Handoff — 2026-09-17

Written for the next session. The previous one ended mid-conversation when
Shamsi restarted to switch models.

## Where the programme is

The v1 plan is `planning/NEXT-STEPS.md`, active list at the top. **Phases 0–5
and 6b are closed.** What remains:

| Item | Phase | Whose |
|---|---|---|
| 9 — build and audit skills | 6 | mine |
| 17 — the exit test | 6 | mine, after her buttons/alerts pass |
| 35 — rebuild the paper mockup's structure | 7 | mine, after v1 |
| 37 — the spacing scale | deferred | hers, judged in a real page |

Everything is committed and pushed to `master`. Verification state:

    python3 verification/check-policies.py    10 checks, 1 FAILING (see below)
    python3 verification/check-drift.py       clean (1 expected NOTE: blog theme)
    python3 verification/check-contrast.py    PASS
    python3 verification/verify-mockups.py    42 passed, 0 failed   (needs playwright)
    python3 verification/gen-anchors.py       run after editing any heading

## Read this before touching anything

- **Several people and sessions edit this repo at once.** The last session
  committed Shamsi's in-progress `buttons.html` and someone else's deletions by
  using `git add -A`. Nothing was lost, but the commit message was wrong and a
  correction had to be pushed (`1df553e`). **Stage specific files.**
- **Shamsi is doing a prose pass** over every page, starting with `buttons.html`
  and `alerts.html`. She wordsmiths; we do structure, deletion and code. She has
  said `buttons.html` is free to take over right now.
- **The system is new and in use nowhere**, so the docs never narrate their own
  history. `check-policies.py` enforces this.

## The immediate queue: 24 items of feedback on buttons.html

### State at the end of the 2026-09-17 afternoon session — NOTHING COMMITTED

Shamsi answered the three questions. Decisions and what is built:

- **(8) One button family.** `.ds-internal` is a context class in tier 1; it
  goes on a parent (`<html>` for an internal page, a wrapper on a mixed page)
  and re-points the accent plus new `--ds-btn-*` construction tokens to lime.
  Tier 2 no longer sets the accent. All five `docs/internal/*.html` pages carry
  the class. `buttons.html` internal demo and `internal/tables.html` are on
  `.ds-btn*`; `.ibtn-*` and `.ctx-internal` are deleted. Internal secondary
  keeps its lime wash. `.btn-tertiary` is replaced by `.ds-btn-text`.
- **Done:** (4) (7) (9) (10) (12) (14) (19) (20) (23), and `.ds-btn-destructive`
  is documented again, so `check-policies.py` passes.
- **(3)** `outreach/html-papers.html` moved to `docs/sharing/`. The "Outreach
  sites" link is out of the nav on every page, by her decision; the rules page
  stays, reachable from DESIGN-POLICIES and AGENTS.md.
- **Still to do for (8):** `docs/internal/buttons.html` still writes `.btn-*`
  (135 uses) and tier 2 still defines the family for it. That page needs a
  rebuild, not a rename: most of it repeats `buttons.html` in lime. Waiting on
  two decisions from her — `.btn-link` and the internal icon-button variants.
- **Open, hers:** the olive text button (`--ds-access-lime-deep` #6b7a10) is
  4.75:1 on white but 4.46 on the canvas and 4.11 on its own hover wash, under
  the 4.5:1 floor. Proposed a darker olive (#5e6b0e is 5.06 worst case).
- **Page zones adopted (Shamsi, 2026-09-17).** `.ds-zone-secondary` on the
  container + one `.ds-full.ds-zone-primary` band; named for role, not colour.
  Secondary ground is the token `--ds-zone-secondary-bg` (Card Grey in light,
  canvas in dark, because Card Grey equals the surface in dark). Documented on
  `organizing-content.html`. Only `buttons.html` is zoned so far. Its shape:
  intro on the secondary ground; in the primary band one H2 per thing you can
  build, each example a `.ds-card` with its "Relevant CSS" accordion inside;
  the internal variant is a `.ds-note--internal`; accessibility essentials sit
  beside the core component.
- **The documentation header (`.ds-site-header--light`) is white now.** The
  arXiv header (the bare class) is unchanged, by her instruction.
- **Her principle for docs pages:** they use the DS and override or invent
  nothing; a style must become a documented DS piece first. Agreed next steps,
  in order: promote the TOC bar from `mockups/public/html-phase1.html` into
  tier 1 (it has JS, and an open question on how it sits under the site
  header); move the paper mockup onto the promoted zones and TOC; clear the
  ~70 page-local rules in `buttons.html` (state grid, forced states, token
  tables) by promoting or deleting each. The AGENTS.md page spine must be
  rewritten when the new page shape is settled — not done yet, because 22
  pages still have the old shape.
- **Contents bar promoted to tier 1** from `mockups/public/html-phase1.html`:
  `.ds-toc` (a `<details>`, works with JS off), `.ds-toc-bar`, optional
  `.ds-toc-bar--sticky`, plus `docs/toc.js`. `verification/gen-anchors.py`
  now fills the bar's `<ol>` from the page's h2 headings and `--check` fails
  when it is stale. Documented on `organizing-content.html` with a live demo.
  On `buttons.html` the bar is STATIC: DESIGN-POLICIES allows sticky chrome on
  the HTML paper reader only, and the policy change (Shamsi proposed "one
  sticky header at a time") is waiting on her approval of the wording. The
  paper mockup still uses its own `.mg-toc-*` copy; moving it over is next.
- `~/.claude/skills/promote-pattern/SKILL.md` is stale: old stylesheet path,
  `--arxiv-*` token names, `-styles.html` demo pages, a STATUS list and README
  index that no longer exist.
- **The admin-console mockups do not load the design-system stylesheets.** They
  carry local `.btn-*` copies, so nothing in tier 2 reaches them. They were
  left untouched.

Shamsi reviewed `docs/buttons.html` and left 24 numbered items. They are the
next work. Grouped by what they need.

### She asked a question — answer before building

- **(8) Do internal buttons need their own class family at all?** Today it is
  `.ibtn-*` on that page and `.btn-*` in `internal-tools.css`, against
  `.ds-btn*` for public. Her instinct is a **parent class that establishes
  context**, so one set of classes serves both surfaces and only colour
  changes. She is right that this gets easier after (4). My view: agree, and it
  is the same mechanism the switch already uses — tier 2 re-points
  `--ds-accent` and the shared component follows. Worth confirming the scope
  (does `.btn-*` disappear entirely?) before starting, because it touches the
  admin mockups.
- **(12) Rename "Relevant classes" to "Relevant CSS"?** Appears on ~10 pages.
- **(3) The `outreach/` directory should not be in the nav** — those are links
  she prepared for sharing. She suggested renaming the directory, maybe "For
  sharing", and was unsure. Needs a decision, then a rename + nav sweep.

### Bugs, confirmed by measurement

- **(23) The accordion at ~line 563 rendered empty — FIXED, not yet committed.**
  The cause was not unbalanced tags (the page had one unclosed `<p>`, nothing
  more). Its `<dl>` had two `<dd>`s under one `<dt>`; the second fell into the
  `max-content` term column, and its unbroken `<pre>` line made that column
  wider than the page. `.ds-acc-body dd` in tier 1 now sets `grid-column: 2`
  and `min-width: 0`.
- **`.ds-btn-destructive` is now documented nowhere**, so `check-policies.py`
  fails. Her deletion of the "Buttons in forms" section (15) took the only
  mention. It needs a home on the page.
- **(19) The disabled icon-only button needs a grey fill** — currently only
  distinguishable on hover.

### Things the design system lacks and must gain

- **(18) A caption class.** For text under a demo — smaller, italic, tied to
  the card above. No `.ds-caption` exists.
- **(16) An on-page nav.** She added a row of text links near the top; there is
  no component for it. Nothing in the stylesheet matches.
- **(21) An in-progress button state** — grey with a spinner. Designed already
  in `mockups/public/submission-metadata/`; port it.
- **(10) A text-only internal button** to replace the tertiary tier, in a dark
  or olive green already in the palette (`--ds-access-lime-deep` is `#6b7a10`).
- **(6) Styling for the two grouping `<span>`s** she added to the Design
  Patterns dropdown.
- **(24) An icons page**, to hold the "why a Lucide icon and not ×" note she
  quoted. That note currently lives on `buttons.html`.

### Corrections to content

- **(4) Internal buttons should match public construction** — shadows and all;
  only colour differs. This is the one that unblocks (8), (9) and (20).
- **(7) "four tiers" is wrong** — there are three.
- **(9) Disabled styling should be identical** across both surfaces.
- **(20) Drop the "internal stylesheet has its own icon button" alert.** If the
  only difference is colour, showing both repeatedly is noise.
- **(14) "Card Grey section fill"** — replace with the class name if one exists.
- **(22)** `<!-- MISSING RELEVANT CLASSES ACCORDION HERE -->` at line 547 needs
  its accordion.

### Cross-cutting, and bigger than one page

- **(1) Why is there a `<style>` block?** Her understanding is that docs pages
  link only `design-system.css`. **She is right in principle and this is worth
  raising properly**: `buttons.html` still has **74 local rules over 170
  lines**, and the biggest family is `.ibtn-*` (20 rules) — which item (8)
  would delete outright. The rest is demo scaffolding (state grids, token
  tables). Some of that is legitimately page-local; some should be promoted.
  Recommend: do (8) first, then re-measure, then decide what is left.
- **(11) Every example in a card.** She added `.ds-card` to two divs — check
  the usage is right, then apply to the rest.
- **(13) Code blocks are single unbroken lines.** They need real line breaks
  and indentation. Related to (17).
- **(17) Remove HTML entities.** `&mdash;`, `&gt;`, `&nbsp;` and the rest.
  **There are 1,277 across the docs** — 348 `&lt;`, 347 `&gt;`, 209 `&mdash;`,
  94 `&amp;`, 77 `&nbsp;`. The `&lt;`/`&gt;`/`&amp;` inside `<pre>` blocks are
  **load-bearing and must stay** — that is how code shows as code. The rest can
  become real characters. Do this as a scripted pass with the `<pre>` contents
  excluded, and verify nothing renders as raw markup afterwards.
- **(2) `design-patterns/` is deleted** — she removed it, the pages live in
  `docs/` now. Already committed. Nothing links to it.

## Suggested order

1. Answer (8), (12), (3) — they change what the rest of the work is.
2. Fix the unbalanced markup in `buttons.html` (23) and the failing check.
3. Do (4): make internal buttons share public construction. Then (7), (9),
   (10), (20) fall out of it, and (8) becomes mechanical.
4. Then the new components: (18) caption, (16) on-page nav, (21) in-progress.
5. Then the page-level passes: (11) cards, (13) code formatting, (17) entities.
6. Then (24) the icons page, and (1) re-measure what the `<style>` block still
   needs to hold.

## Conventions worth not rediscovering

- Page spine, checked: page header, Demo, Spec, Usage, Rules, Accessibility.
  A page may omit one but may not rename it. In `AGENTS.md`.
- Every page: `<title>Name — arXiv Design System</title>`, sentence-case
  section headings, `theme.js` in the head **undeferred**, `.ds-theme-toggle`
  plus `#ds-theme-status` in the header.
- Type sizes are `rem`; a control's padding and min-width are `em` against its
  own label. Controls clear a 24px target floor, with two exemptions recorded
  by name in `verify-mockups.py`.
- Tier 2 (`docs/internal/internal-tools.css`) holds only what differs. Never
  copy a component into it to restyle — that is a token.
