# Reorg before/after — battery comparison (2026-07-29)

Same battery, same pinned model (`claude-sonnet-4-6`), prompts frozen except
mechanical path updates. Baseline: `runs/20260728-153519-baseline/` ·
Post-reorg: `runs/20260729-105246-post-reorg/` (structure + AGENTS.md routing;
page content **unchanged** — the page-template rewrite hasn't happened yet).

## Machine axis

| Measure | Baseline | Post-reorg |
|---|---|---|
| Policy-violation auto-flags | **3** (Google Fonts ×2, CDN icon font ×1) | **0** |
| Off-palette hexes (true) | 5 | 3 (all page-chrome greys/tints) |
| Total cost | $11.28 | $10.46 |
| File reads (10 cells) | 106 | 83 |
| Guardrail trap | pass ×2 | pass ×2 (now refusing after 3–4 reads, was 5) |

## The routing evidence (the reorg's actual job)

Every post-reorg cell opened `AGENTS.md` first, then went **straight to the
pages whose absence caused its baseline failure**:

- 01 (card): read `docs/organizing-content.html` — the card definition neither
  baseline rep ever found.
- 02 (bulk bar): read `docs/internal/alert-styles.html` — the alert
  construction both baseline reps missed (that miss was the core of the fail).
- 03 (withdrawn notice): read `docs/version-display.html` + `docs/alerts.html`
  — the versions treatment it ignored in baseline.
- External-resource violations went **3 → 0**: the AGENTS.md "rules agents
  break most" section (written from baseline evidence) eliminated the class.

## New finding: the page-composition gap

03-r1 read `mockups/public/abstract-redesign.html` **seven times** — despite the
mockup contract — because the task needs "a realistic abstract-page fragment"
and `docs/` documents components, not page assembly. The only place an
abstract page *exists* is a mockup. Routing can't point at what doesn't exist:
**docs/ needs a page-composition/layout reference** (ties into the known gaps:
layouts, grids, breakpoints, type ramp). Until then, agents will keep falling
through to mockups for page context.

Also recurring: fabricated text logos in simulated headers (Campus Red applied
*correctly* to the X — but there's still no official logo asset in docs/ to
use; the Phase 3 brand-assets page closes this).

## Anomaly note

02-r1 ran 35 min (baseline 11) with normal cost/turns — ~18 min was non-API
stall time (rate-limit backoff while other sessions ran). Infrastructure, not
structure; excluded from conclusions.

## Designer axis (graded 2026-07-29)

**Baseline 4/10 pass → post-reorg 6/10 pass.** The extrapolation task flipped from
fail×2 to pass×2 — the reasoning-from-rationale task improved most, consistent with
agents now reading the routed guidance (version-display, alerts tone) instead of
missing it. Trap and type badges held at pass×2.

The four remaining fails are all rules that exist **nowhere in the docs**:

- 01 (card ×2): hairline row dividers on a card + missing background-tint rules —
  both decided 2026-07-29 (cards: spacing not dividers; tint signals editability),
  neither written into docs/ yet.
- 02 (bulk bar ×2): tinted action-button bar; the preferred action-bar layout
  (buttons + descriptive text left, filter dropdown right) exists only in the
  **unpublished local Wombat user-page mockup**. An agent cannot match a reference
  it cannot reach — direct evidence for the mockup migration.

One decision flowed backward from an agent output: Shamsi prefers the agent's
**green tint on selected rows** over her own mockup's untinted rows ("aids
usability") — adopted into the Wombat promotion item. The harness is now feeding
design decisions, not just catching errors.

Recurring: 03-r2 hand-built header/sidebar and a fabricated logo (rep-inconsistent;
the brand-assets and page-composition gaps again).

## Caveats

- Same-day, n=2/task: directional, not statistical.
- Designer grading of post-reorg artifacts pending — the visual axis decides
  whether correctness *as graded* actually improved (baseline was 4/10 pass).
- Costs barely moved because page *content* hasn't changed — the burn is in
  what each page costs to read. That's the page-template rewrite's job, with
  this run as its baseline.

## Next

1. Shamsi grades `runs/20260729-105246-post-reorg/review.html`.
2. Harness v2 (approved, was deferred for comparability): monospace lab-report
   review chrome, side-by-side canonical-reference comparison, agent text-pass
   before designer pass, neutral-shell task framing, final-message caps.
3. Page-composition reference + brand-assets enter the docs-gap queue with
   teeth (both caused observed failures now).
