# Handoff — 2026-10-05

Written for the next session. PR #7 (`docs-review-2026-09-28`) merged into `master` on
2026-10-05. Shamsi wants to commit to `master` directly, but GitHub rulesets still require a pull
request and status checks there, and she is asking the team to change them. Until then, work goes
on the branch `search-results-2026-10` and reaches `master` through a pull request she opens.
Fetch before every push: others push too.

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

0. **State on 2026-10-05 (overnight run).** Branch `search-results-2026-10` holds: search
   version D (`search.html`), the Papers page (`papers.html`: hierarchy, a paper in a list,
   versions, categories, full papers, sidebar, contents bar, section permalinks, equations,
   figures and references, citations and footnotes, rules incl. paper body and printing), and the
   inventory promotions from the paper decisions inventory (sections 1 to 8; deleted after promotion, in git history). The
   promotion rule (Shamsi): promote everything unless it directly breaks a docs guideline;
   conflicts are listed for her, not promoted. `abstract-phase2.html` is ignored (stale).
   Waiting on Shamsi: the conflicts list in the morning summary; her second pass on papers.html
   and search.html; the new prose (she wordsmiths).
000. **Dark mode tints:** audit `dark-mode-tints-audit.html`, proposal `dark-mode-proposal.html`.
   Shamsi likes nearly every proposed value; she asked for a stronger selected-row tint, now 1.20
   against the page. Nothing is in design-system.css yet: adopt the proposal only after she
   approves it, then run check-contrast and check-drift.
0000. **Questions for Deyan** (answered 2026-10-06): his answers and what follows from them are in
   `live-html-markup-2026-10-06.md`. Still open: the abstract heading level (Shamsi decides);
   table scroll regions (Deyan and Bruce; Shamsi sent the reasons for `role="region"`); the
   stylesheet reconciliation and theme switcher removal (a later conversation with Deyan).
00000. **Shamsi's answers, 2026-10-06** (done): papers.html has an optional area above the identity line for temporary content (Back to abstract); no exceptions file;
   the missing-alt-text note is shown, to teach;
   references are shown as the author wrote them and arXiv has no reference format; one
   `.ds-permalink` pill everywhere (replaces `.ds-anchor`); element pill is one tab stop with arrow
   keys (`element-pill.js`); PDF from a paper opens a new tab; external links print their address;
   captions are Plex Sans small. Visual choices waiting on her: `paper-type-choices.html` (section
   number weight, hyphenation, TeX glyph draft).
00000a. **To do later:** an accessibility-visibility discussion (the Accessibility accordion stays
   closed for now; does a closed accordion count as "visible"?).
00000b. **Next plan candidate: reconcile the mockups with the docs.** `abstract-phase2.html` and
   `html-phase1.html` should follow the docs: Permalink pill, body line-height from typography,
   figure viewer caption unchanged, remove "Who cites this", and every other refinement since. Treat
   it as an early test: the mockups are real future uses of the system.
00. **Testing** — plan in `TESTING-PLAN.md`, protocol in `verification/token-burn/README.md`,
   team report in `verification/token-burn/reports/2026-10-search/`. Tests 1 and 2 are done.
   Test 3 rebuilds search results once Papers settles; then arXiv Check as the non-paper search.
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

Cleaned up on 2026-10-06: implemented and superseded proposals were deleted (they are in git
history before that date). What remains is still open or is linked from the docs:
brand-metrics-brainstorm (parked; linked from brand.html), dev-workflow-comparison with
fifth-option-self-verifying-spec and options-3-and-5-on-browse-and-search (how dev repos adopt the
DS; linked from index.html and templates/README.md), icon-only-controls (figure viewer zoom
controls, still proposed), typeface-re-evaluation-2026-06 (decision record; linked from
typography.html).
