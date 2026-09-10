# Token-burn baseline — results (2026-07-28)

Run: `runs/20260728-153519-baseline/` (plus one preflight cell, `runs/20260728-151508-preflight/`).
Worker: `claude-sonnet-4-6`, pinned. 10/10 cells completed, no run errors.
**Cost: $11.28 · 76 min of agent time · designer grading: Shamsi Brinn (grades.json).**

## Scoreboard

| Cell | Machine flags | Designer grade | Distilled notes |
|---|---|---|---|
| 01 fidelity build r1 | — | **fail** | table styling, not the card register; link style correct |
| 01 fidelity build r2 | — | **fail** | same; focus outline color correct |
| 02 fidelity internal r1 | Google Fonts | **fail** | base table correct; feedback alerts not the `.ds-alert` construction; header-area tint wrong |
| 02 fidelity internal r2 | bootstrap-icons CDN | **fail** | black selected-row background wrong |
| 03 extrapolation r1 | — | **fail** | mixes light/dark values; hand-built header + fabricated text logo; versions display ignores documented method |
| 03 extrapolation r2 | — | **fail** | mixed light/dark alert; white alert nested in dark-toned alert |
| 04 violation trap r1 | none (refused) | **pass** | flagged all violations with policy citations, built nothing |
| 04 violation trap r2 | none (refused) | **pass** | same |
| 05 real type badges r1 | — | **pass** | badges and host tables correct |
| 05 real type badges r2 | Google Fonts | **pass** | visually correct (font load is still a policy miss) |

**4 pass / 6 fail.** (Preflight cell 02-r1′ also failed on the same alert-construction grounds.)

## The headline: grades track documentation coverage, not model capability

The same model, same day, same repo aced some tasks and failed others — and the split is
clean:

- **Passed:** the violation trap (the guardrail instructions live in CLAUDE.md, directly in
  the reading path) and type badges (colors named in DESIGN-POLICIES, working examples in
  `internal/tables.html` — found and reused by both reps).
- **Failed:** every task whose correct answer lives in places the reading path never
  routes to, or that isn't written down at all.

Sonnet is not the bottleneck; **findability and coverage are.** This also answers the
"should we test with a stronger model" question with data: a stronger model might infer
its way past some gaps, but per the agent-agnostic principle that would only mask them.

## Finding 1 — the reading order stops before the pattern pages

`CLAUDE.md` routes agents through CONTEXT → BRAND → DESIGN-POLICIES → typography →
color-mapping → DESIGN-PROGRESS → stylesheets. **No flagship pattern page is in the
path.** Consequences observed in the reading logs:

- Neither 01 rep ever opened `organizing-content.html` — the page that defines the public
  card and the dl row grammar. Both invented a table-flavored row structure; both failed
  on exactly that.
- The 02 reps used `.ds-alert` tokens but not the component construction — neither opened
  `alerts.html`. Nothing maps "I need a status message" to the alert
  reference.
- 03-r1 hand-built a site header with a fabricated text logo instead of using
  `.ds-site-header` (`header.html`, never read) and ignored the documented
  versions treatment (`version-display.html`, never read).

**Reorg implication:** the entry point needs a routing layer — "building X? read Y" —
and the flagship pages must be reachable from it. (Also: agent-agnostic entry points;
today only Claude reads `CLAUDE.md`.)

## Finding 2 — reference pages are training data

02-r2 copied the bootstrap-icons CDN link **verbatim** from the repo's own
`internal/buttons.html`. The one policy violation shipped inside a reference page
propagated straight into new work. Corollary: example quality outranks rule wording.
(Cleanup of that CDN link is already queued as a task chip.)

## Finding 3 — external-resource loading is the dominant violation class

Google Fonts twice + the CDN icon font once, across 8 build cells (plus preflight).
The self-hosting rule exists in DESIGN-POLICIES and CLAUDE.md, yet agents "helpfully"
add font loads the reference pages themselves don't carry. Candidate fixes: a
point-of-use warning where fonts are documented (typography.md), and pattern-page
skeletons that show the correct (no-load) head.

## Finding 4 — dark-mode tokens without usage guidance get misused

Both 03 reps (and the 02 feedback bars) hand-mixed dark-mode token values into
light-mode pages. The dark values exist in the stylesheets; the *rule about when to use
them* lives in `dark-mode-decision.md`, which is outside the reading path. Nothing tells
an agent "new pages are light-only until the dark program resumes; never hand-pick dark
values; lock demo pages with `data-theme="light"`." Cheap fix queued for the dark-mode
Phase 0/1 work: a status note at the dark block in both stylesheets + one line in
DESIGN-POLICIES.

## Finding 5 — grading surfaced undocumented patterns (new backlog)

Shamsi's notes identified layouts the system never absorbed: the **Wombat user-page
mockup** (`~/arxiv/design/arXiv-mockups/Wombat mockups/user-page/index.html`) — the
"owned references" table treatment and the "owned papers" accordion — as the correct
reference for the 02 task's selected-rows/data-organization problems. Those styles were
never promoted into the internal design system, and the universal-vs-internal-only table
styles were never differentiated. Added to NEXT-STEPS (internal pattern queue).
Undocumented conventions agents also can't know, observed in grading: actions disable
rather than disappear (bulk bars); official logo assets only, never text-drawn logos
(feeds the Phase 3 brand-assets page).

## Burn shape (the efficiency half)

- Fidelity builds: $1.35–1.85 and 8–12 min per page; extrapolation $0.90–1.76;
  refusals $0.25 / ~1 min. Full-context onboarding costs ~450k–2.1M cache-read tokens
  per cell — the whole context re-fed every turn is the structural burn.
- Reading paths were disciplined (mostly the documented order, near-zero wasted
  detours, ≤6 re-reads) — the cost is **what the order contains**, not wandering.
- Efficiency and correctness point at the same lever: better routing means agents read
  *less* (targeted references instead of everything) and produce *more correct* work.

## Checker notes (for future runs)

False positives fixed during this run and now structural: palette derives from the
stylesheets themselves; view-count regex requires a digit; documented logo-X Campus Red
use exempted. Both 03 reps used Campus Red **correctly** (logo X only, citing the
heritage rule) — worth noting as a genuine rationale-following success.

## What this feeds

1. **The reorg context session** — Findings 1–4 are the evidence base: routing layer,
   agent-agnostic entry points, example hygiene, point-of-use rules.
2. **Post-reorg re-run** — same battery, same pinned model; success = fewer designer
   fails on 01/02/03, zero external-resource flags, lower per-cell burn.
3. **New documentation work** — Wombat user-page promotion; disable-don't-disappear
   rule; brand-assets/logo discoverability; dark-mode status note.
