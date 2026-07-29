# Repo reorganization — plan of record (2026-07-29)

Approved by Shamsi 2026-07-29 after the token-burn baseline (see
[../verification/token-burn/BASELINE-RESULTS.md](../verification/token-burn/BASELINE-RESULTS.md)).
This file records what changed, why, and what's deliberately deferred.

## The four categories

| Category | Directory | Rule |
|---|---|---|
| Documentation | `docs/` | the only build reference; one fact, one home |
| Verification | `verification/` | evidence — audits, design reviews, agent test runs |
| Planning | `planning/` | backlog, proposals, decision logs — meta, not rules |
| Work in progress | `mockups/` | never referenced for building; patterns promote *into* docs/ |

## What moved (2026-07-29)

- `design-patterns/` → `docs/` (flagship pages + `typography.md` / `color-mapping.md` at top level = the universal foundations; `public/` and `internal/` = the surface overlays). `BRAND.md` and `DESIGN-POLICIES.md` moved in from root.
- `audits/`, `docs/design-reviews/`, `tests/token-burn/` → `verification/`.
- `NEXT-STEPS.md`, `PROPOSED-GUIDELINES.md`, both dark-mode docs, `proposals/` → `planning/`.
- `CONTEXT.md` dissolved into the rewritten `README.md` (one overview, human-first).
- **`AGENTS.md` created** — canonical agent entry: directory contract, routing table ("building X → read Y, reuse Z"), the hard rules agents break (from baseline evidence), guardrails, writing rules with budgets. `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` are now three-line pointers to it (agent-agnostic entry points).
- Root keeps only: README, AGENTS + pointers, LICENSE (MIT — root by GitHub convention), `index.html` (Pages landing, must be root), `doc.html` + `docs-assets/` (the md viewer stays at root so it can reach all four categories; its `src` guard blocks `..`).
- Redirect stubs left at `design-patterns/*.html` for the seven flagship pages (shared URLs don't break).

## Why this shape (the baseline evidence)

1. Reading order stopped before the pattern pages → agents invented what was already
   defined. Fix: AGENTS.md routing table.
2. Only Claude read the entry file. Fix: AGENTS.md + per-tool pointers.
3. Reference pages are training data (CDN link copied verbatim). Fix: mockups/docs
   contract + example hygiene (cleanup queued).
4. Dark tokens misused on light pages. Fix: rule surfaced in AGENTS.md; point-of-use
   note lands with dark-mode Phase 0/1.

## Sequencing — and the measurement rule

**Structure first (done above) → re-run the battery → rewrite pages incrementally.**

The battery re-run must isolate the structure variable, so task prompts are **frozen**
except for mechanical path updates (`design-patterns/` → `docs/`). The harness UX
changes Shamsi requested (monospace lab-report review chrome, side-by-side canonical
comparison, agent-does-the-text-pass, scope-framing in task specs, final-message caps)
are all approved but **land after the comparison re-run** — changing prompts and
structure at once would confound the before/after.

## Deferred to next stages (approved, not yet built)

- **Page-template rewrite** — every pattern page inverted-pyramid (example + spec table
  above the fold; prose below). Incremental, evidence-driven, after the re-run.
- **Harness v2** — the four review changes above + neutral-shell task framing.
- **Dev explainer** — 1–2 pages on the testing format for arXiv developers, shared
  after the re-run shows a before/after.
- **Docs gaps list** (from the context session): type-size ramp, breakpoints,
  grid/layout vocabulary, Wombat user-page patterns, universal-vs-internal table split,
  disable-don't-disappear rule, logo/brand assets.

## Writing rules (the "less content" contract)

Recorded in AGENTS.md §Writing rules: minimal diffs; one fact one home; example-first
pages; numeric budgets (rationale ≤ 3 sentences/rule); prose added only against
observed failures. These exist to keep the docs human-pleasant, self-consistent, and
safe from wholesale agent rewrites.
