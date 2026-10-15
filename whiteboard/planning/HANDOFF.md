# Handoff — 2026-10-15

Written for the next session. Open work is in `NEXT-STEPS.md`; this file holds the current state and the working rules.

## Branches and pull requests

- Every change goes on a branch named for its content and reaches master through a pull request that Shamsi opens. Nobody commits to master directly.
- One branch and one pull request per batch of related changes. Do not add commits to a pull request that is waiting for review.
- Open, local only: `DS-messaging` (the rename to Smileybones and the new home page). It waits for Deyan's PR 17, which edits `README.md` and `AGENTS.md` too. Squash-merge it: one commit adds a file that a later commit removes.
- Open, local only: `planning-cleanup` (this file, `NEXT-STEPS.md`, and removed planning notes).
- Deyan's drafts: PR 17 (banner) and PR 10 (header page actions).
- Fetch before every push. Others push too, and a second Claude session sometimes works in the same repo, so stage files by name.

## Where the work is

**V1 is done when an agent with no help beyond the docs builds a public page and an internal page that both pass visual and programmatic fidelity, and Shamsi has reviewed every docs page those builds depend on.**

1. Public page: search. Done.
2. Internal page: the moderation and staff reports. Rounds 4 to 9 have run; round 9 gave the best builds yet. The reference pages are in `whiteboard/mockups/internal/activity-dashboard/`. Not yet declared done.
3. Docs pages: reviewed pages are listed in `verification/reviewed-pages.txt` and have agent digests in `docs/spec/`.

After V1: the Papers scope (what belongs to the renderer), simpler Papers rules, and reconciling the mockups with the docs.

## Repo layout

- `docs/` — the design system.
- `templates/` — Deyan's production brand package (header, footer, banner). It uses `docs/design-system.css`, so stylesheet changes reach real pages.
- `verification/` — the checks, the digests, the audits, the agent test harness.
- `whiteboard/` — Shamsi's working files: `mockups/` and `planning/`. Not canonical. Never link an in-progress whole-page mockup from `docs/`.

## Checks (run all before pushing; GitHub runs the first six on every push)

    python3 verification/check-policies.py
    python3 verification/check-drift.py
    python3 verification/check-contrast.py
    python3 verification/check-components.py
    /opt/homebrew/bin/python3.11 verification/check-template-compat.py
    /opt/homebrew/bin/python3.11 verification/check-generated.py
    python3 verification/gen-anchors.py         after editing any heading
    python3 verification/gen-digest.py          after editing a reviewed page

The system `python3` is 3.9 and fails on the two template checks.

## Working rules (do not rediscover)

- **Links are full `file:///` URLs**, never bare paths: Shamsi clicks them to review.
- **Shamsi reviews changes on the pages themselves.** Do not write prose lists, proposals or long planning files for her to read. She rewrites prose in place.
- **She wordsmiths; the session does structure, deletion and code.** Fix facts and mechanics in her drafts (typos, contractions, broken links) and say so.
- **Blind review:** do not look at a test's builds before Shamsi has reviewed them.
- **Plain words** (STYLE.md): state what a thing is; a reason only when a builder would otherwise get it wrong. `check-policies.py` fails on a list of words to avoid. No contractions in anything written for arXiv.
- **Ask before inventing** a class, token or colour. New fill colours are discussed with the design team first.
- **One fact, one home.** No history on docs pages.
- **Page shape:** plain `<section>` starting with `<h2 id>`; `.ds-section-desc`; demos in a `.ds-card` with a Relevant code accordion and a `dl` class key. No page `<style>`, no inline styles; docs-only scaffolding goes in `docs/docs.css`. Page names follow `AGENTS.md`.
- **The shared docs menu** is the same on every docs page (checked). A new page goes into the menu on every page with one script.
- **Parallel agents:** give each its own files; on shared files (`design-system.css`, `docs.css`) use small Edit replacements. Commit after they finish; never let agents commit.
- **Look before deleting.** Check what links to a file and whether Shamsi still uses it.

## Proposals still open (`whiteboard/planning/proposals/`)

`brand-metrics-brainstorm.md` (linked from brand.html), `dev-workflow-comparison.html` (how developer repos adopt the design system; linked from `templates/README.md`), `icon-only-controls.md` (figure viewer zoom controls), `typeface-re-evaluation-2026-06.md` (decision record; linked from typography.html).
