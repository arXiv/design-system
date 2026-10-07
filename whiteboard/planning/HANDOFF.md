# Handoff — 2026-10-07

Written for the next session. **PR #8** (`search-results-2026-10` into `master`) is open and
waiting for a reviewer; Shamsi merges it. Work started after PR #8 goes on a new branch
(`overnight-2026-10-07` from 2026-10-07) so the PR under review does not change. `master` still
requires a pull request and status checks. Fetch before every push: others push too, and a second
Claude session sometimes works in the same repo (stage files by name).

## Where the work is

Shamsi reviews a page, sends notes, the session acts on them, and she rewrites the prose herself.
Pages with a finished review are listed in `verification/reviewed-pages.txt` and have agent
digests in `docs/spec/`. papers.html and search.html have had her review (2026-10-06) and are not
yet in that list. brand.html and outreach.html are deliberately left for later.

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

- **Links are full `file:///` URLs** (and `http://127.0.0.1:8765/` for the review page), never
  bare paths: Shamsi clicks them to review.
- **Blind review:** Claude does not look at a test's builds before Shamsi has reviewed them.
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

## V1 (agreed 2026-10-06)

**V1 is done when an agent with no help beyond the docs builds a public page and an internal page
that both pass visual and programmatic fidelity, and Shamsi has reviewed every docs page those
builds depend on.** This replaces the 2026-09-09 exit test (the membership dashboard spec in
`specs/`, which described a different page). Not needed for V1: the agent skills (#9), the old
dashboard spec, the Papers scope work (Papers follows V1 as the first product built on it).

1. **Public page:** search. Done: test 3 passed programmatic fidelity in all four builds; its two
   gaps are fixed. Shamsi called search testing sufficient.
2. **Internal page:** test 4, moderation and staff reports. Built and evaluated
   (`verification/token-burn/runs/20261006-192823-04-staff-reports/`). Next: Shamsi's blind
   review, then Claude's programmatic grades, then `round.py report`. Do not look at the builds
   before her review.
3. **Docs pages the builds depend on:** reviewed, except any that test 4 shows are missing.
4. Then the next plan: Papers scope (what belongs to the renderer), simplifying the Papers rules,
   reconciling the mockups with the docs.

## Open, in Shamsi's hands

- Review test 4 (start the review page with `python3 round.py review runs/20261006-192823-04-staff-reports`).
- Merge PR #8 after the reviewer approves.
- Decide the abstract heading level (from Deyan's answers, `live-html-markup-2026-10-06.md`).
- Approve or change the direction for the Papers rules: three to five rules per section for
  people; the detail in each demo's class key; LaTeXML-specific rules moved to the renderer.
- Brand & vision and Outreach pages.

## To do later (agreed, not scheduled)

- **arXiv Check test, in React.** Shamsi takes screenshots first. See `TESTING-PLAN.md`.
- **Accessibility visibility discussion.** The Accessibility accordion in the paper sidebar stays
  closed for now; does a closed accordion count as "visible"?
- **The accessibility guidelines' direction.** Shamsi is unsure about
  `accessibility-priorities.md` being focused on the abstract and HTML paper pages. Proposed: one
  general set of accessibility rules in the design system, informed by the HTML papers work, with
  paper-specific decisions living with the renderer.
- **Reconcile the mockups with the docs** (`html-phase1.html`; the abstract page mockup is stale):
  Permalink pill, typography line-height, figure viewer caption unchanged, remove "Who cites
  this", author list from arXiv's metadata (LaTeXML's author blocks are not one per person).
- **Process.** Shamsi finds the amount of text after a session overwhelming. A proposal is in
  `process-proposal.md`.
- **`docs/examples/`**: stable full-page examples built only from documented components (approved
  in principle 2026-10-02); start with form validation.
- **Deferred, decide against real content:** data visualisation (charts, meters, legends); user
  portal and Admin Console mockups.
- **Cleanup:** links in older notes and the mockups README that point at files gone before the
  reorg (`docs/public/`, `metadata-panel.html`, `BRAND.md`).

## Decided 2026-10-06 (details in the commits)

Dark mode tints adopted (cards sit on the page with a border; every fill steps away by its
light-mode amount). One `.ds-permalink` pill on every heading. `.ds-element-pill` is one tab stop
with arrow keys. PDF from a paper opens a new tab; in a row of links that each have an icon, the
new-tab icon is left out. External links print their address. Captions are Plex Sans small.
Paper body text is hyphenated; section numbers stay at 600. TeX glyph from Font Awesome Free
(CC BY 4.0). The papers page: TOC bar (renamed from contents bar), framed sidebar matching the
mockup, references shown as the author wrote them, alt-text note shown to teach. Alerts go at the
top of the part of the page they are about. Pager: which page numbers to show; bars space
themselves from the list. Test report: one page for the team (`round.py report`), grades in
`verification/token-burn/GRADING.md`.

## Proposals (whiteboard/planning/proposals/)

Cleaned up on 2026-10-06: implemented and superseded proposals were deleted (they are in git
history before that date). What remains is still open or is linked from the docs:
brand-metrics-brainstorm (parked; linked from brand.html), dev-workflow-comparison with
fifth-option-self-verifying-spec and options-3-and-5-on-browse-and-search (how dev repos adopt the
DS; linked from index.html and templates/README.md), icon-only-controls (figure viewer zoom
controls, still proposed), typeface-re-evaluation-2026-06 (decision record; linked from
typography.html).
