# Handoff — 2026-10-02

Written for the next session. Everything below is committed and pushed to the branch
`docs-review-2026-09-28`, which is open as a pull request into `master` (master is PR-only).
Commit to that branch until Shamsi says otherwise. Fetch before every push: others push to it,
and it was rebased onto master once (after Deyan's brand-templates PR #6).

## Where the work is

The docs review is nearly finished. Shamsi reviews a page, sends notes, the session acts on them,
and she rewrites the prose herself. 21 pages are marked finished in
`verification/reviewed-pages.txt` and have agent digests in `docs/spec/`.

Not finished:
- **brand.html and outreach.html:** deliberately left for later ("a different type of thinking").

## Repo layout (changed 2026-10-02)

- `docs/` — the design system. Planned: `docs/examples/` for stable full-page examples.
- `templates/` — Deyan's production brand package (header, footer, banner chrome; the stats
  site uses it). It consumes `docs/design-system.css`, so stylesheet changes reach real pages.
- `verification/` — the checks, digests support, audits.
- `whiteboard/` — Shamsi's working files: `whiteboard/mockups/`, `whiteboard/planning/`
  (proposals, specs, this file). Non-canonical. Never link in-progress whole-page mockups from
  `docs/`; the one approved exception is forms.html linking the submission metadata mockup,
  to be replaced by a `docs/examples/` form page.

## Checks (run all before pushing)

    python3 verification/check-policies.py      page shape, docs menu identical on every page, plain words, classes documented
    python3 verification/check-drift.py         dark mirror = media block
    python3 verification/check-contrast.py      promised text pairings clear AA
    python3 verification/check-components.py
    python3 verification/gen-anchors.py         after editing any heading
    python3 verification/gen-digest.py          after editing a reviewed page
    /opt/homebrew/bin/python3.11 verification/check-template-compat.py   Deyan's; needs Python 3.10+
    /opt/homebrew/bin/python3.11 verification/check-generated.py        Deyan's; needs Python 3.10+

The system `python3` is 3.9 and fails on Deyan's two scripts.

## Working rules (do not rediscover)

- **She wordsmiths; the session does structure, deletion and code.** Fix facts and mechanics in
  her drafts (typos, contractions, broken links, wrong anchors) and say so. List every sentence
  you or an agent write.
- **Plain words** (STYLE.md "Say what it is, and stop"): state what a thing is; a reason only
  when a builder would otherwise get it wrong. Never "carries / rail / walk / track"
  (check-policies fails on them; "tracking" as surveillance is allowed). No contractions.
- **Ask before inventing** a class, token or colour. New fill colours: discuss with the design
  team first, never add without that step.
- **One fact, one home.** No history narration on pages.
- **Page shape:** plain `<section>` starting with `<h2 id>` (or `<h3 id>` under the plain
  Modifiers / Rules / Spec group headings); `.ds-section-desc`; demos in a `.ds-card` with a
  Relevant code accordion and a `dl` class key. No `class="section"` / `section-title` any more —
  scripts find section headings by structure. No page `<style>`, no inline styles; docs-only
  scaffolding goes in `docs/docs.css`.
- **Headings vs labels:** a heading names something a reader would want to find (own description
  or several examples); a panel label names the one example below it, a few words, never a
  sentence; state labels name cells in a row of variants; card titles stay h3.
- **Shared docs menu** is identical on every page (checked). New page → add it to the menu on all
  24 pages with one script.
- **Parallel agents:** give each its own files; on shared files (design-system.css, docs.css)
  Edit tool only, small replacements. Commit after they finish; never let agents commit.

## Decisions made this round (2026-09-28 to 2026-10-02)

Colour: two tints only, `--ds-tint-warm` (Card Grey; dark `#221f1b`) and `--ds-tint-accent`
(Tint Light; Access Lime wash inside `.ds-internal`). Fills use a tint or a status colour.
Popovers and tooltips use the accent tint. Notes keep their colours on every surface (essential
note = info status colours).

Header: four regions — logo, navigation, tools (optional), account (outside the nav). Navigation
on the right. Account is a menu (account page + Log out, Log out is a POST form button). First-name
greeting, 14ch cap. `header.js` folds by fit: greeting, then nav, then tools; no fixed
breakpoint. `--sticky` modifier for internal tools only. Docs pages use the new structure.

Navigation and organisation: layout-patterns.html opens with four questions (Where am I? What
matters here? Which part do I need? Can I learn more?) as cards listing every option; rules under
"Rules". Secondary navigation `.ds-subnav` (horizontal bar, wraps). Steps `.ds-subnav--steps` for
ordered processes (the app owns which steps are available). Pager (renamed from Stepper,
`.ds-pagination`) for queues. Tabs `.ds-tabs` + tabs.js, one level only. Filter bar
`.ds-filter-bar`, a GET form; settings sit apart from filters. No breadcrumbs where secondary
navigation exists. Sidebar `.ds-sidebar` (was rail), separated by spacing. `.ds-container--wide`
(1080px) for dense internal tools. Full bands (`.ds-full`) are documented under Page zones.

Tables: one `.ds-table` for both surfaces; header from `<thead>` (body colour, 15:1); row headers
from `<th scope="row">`; visible UI Boundary Grey frame (border-collapse: separate); no frame
directly inside a card; `--striped`; `.ds-num`; bulk actions, `.ds-filter`, `.ds-table-scroll`
in tier 1.

Other: stat card `.ds-card--stat` (stat grids fill the row, 12rem minimum); `.ds-link-list`;
`.ds-label-row`; switch fill only changes; h3 has 32px above, proximity rule "at least 2×";
help text below fields with messages under it; disabled reasons in a tooltip or help text; modal
body scrolls automatically and becomes a tab stop only while it overflows.

## Open, in Shamsi's hands

- Share the membership dashboard mockup with Christopher
  (`whiteboard/mockups/internal/membership-dashboard/`). Placeholders to raise with him: the
  holds-ratio basis and the Recruitment statuses.
- Brand & vision and Outreach pages.

## Next, ours

0. **Testing** — plan in `TESTING-PLAN.md`, protocol in `verification/token-burn/README.md`.
   Test 1 (simple search) is built, reviewed and summarized; its 14 proposed changes are in the
   plan under "Test 1". Next: design the compact search form on a proposal page, decide the
   default page ground (white or tint), then rebuild with one page state.
   The pager changed on 2026-10-02: position or range at the start, controls at the end, and a
   numbered variant (`.ds-pagination-pages`). Open: its phone-width layout, the "Request 1–3 of
   15" wording against the two descriptions under it, the Settings label on tables.html.
1. **`docs/examples/`** — stable, generic full-page examples built only from documented
   components (approved in principle 2026-10-02). Start with form validation (states: empty,
   errors after submit, warnings, auto-corrected value, fixed); then a report page for
   layout-patterns. Once the form example exists, forms.html links to it instead of the
   submission mockup. Demo switchers are docs-only scaffolding. Add one AGENTS.md line.
2. **Deferred, decide against real content:** sidebar tint or border (after mockups move onto the
   DS); data visualisation (charts, gauges, meters, legends); user portal mockup (Moderation and
   Administration move to internal tools); Admin Console mockup (test the four questions; many
   destinations probably go in grouped header dropdowns).
3. **Mockups onto the DS:** the paper and abstract mockups still use their own TOC and header
   classes; move them after the review.
4. **Cleanup:** about 15 links in older notes and the mockups README point at files gone before
   the reorg (`docs/public/`, `metadata-panel.html`, `BRAND.md`).

## Proposals (whiteboard/planning/proposals/)

Decided and implemented: header-component, secondary-navigation (option B), bulk-action-bar
(option A), tints, headings-and-labels, membership-dashboard-audit and -structure,
navigation-layers. Their pages describe the options; the decisions above are what stands.
