# We test the design system with AI agents — tear this apart

**Audience:** arXiv developers · **Ask:** ~10 minutes and your skepticism · **Contact:** Shamsi

## What this is

We test whether an AI coding agent, given only this repo, does frontend work correctly and cheaply. Five realistic tasks — build a component from a spec, reuse existing components, one deliberately under-specified design problem, one request that violates arXiv policy on purpose, one real backlog item — each run twice, headless. Deliberately a mid-tier model: developers here use Claude, Gemini, and Copilot, so the docs must carry the load; a frontier model bridging doc gaps by inference would hide exactly what we want to find.

Each run executes in a clean copy of the repo with the test definitions removed, so the agent can't find the answer key. We record tokens burned, files read and in what order, auto-scanned violations (external font/CDN loads, off-palette colors, planted traps), and Shamsi visually grades every output against the pattern pages.

## What it found so far

We ran it before and after restructuring the repo (same tasks, same model):

| | Before | After |
|---|---|---|
| Designer grade | 4/10 pass | 6/10 pass |
| Policy violations | 3 | 0 |
| Files read per battery | 106 | 83 |

The sharpest finding: failures tracked **documentation coverage, not model capability** — every remaining fail is a rule that was never written down or couldn't be found. One agent copied a policy violation verbatim from our own reference page: example code is training data. Details in [REORG-COMPARISON.md](REORG-COMPARISON.md) and [BASELINE-RESULTS.md](BASELINE-RESULTS.md).

## Where your perspective would genuinely help

1. **Task coverage** — are these the right kinds of work? What do you actually hand to an agent that we should be testing?
2. **Rigor** — two runs per task. Enough? How would you handle run-to-run variance without tripling cost?
3. **Metrics** — anything you'd add or drop? (e.g., diff-against-reference, time-to-first-correct)
4. **Cadence** — when should this run (on docs changes? scheduled?) so it stays useful without becoming maintenance for a very small team?
5. **Contamination** — does the clean-copy approach look airtight to you?
6. **Trust** — what would you need to see before treating `AGENTS.md` + `docs/` as the source of truth for agent-assisted frontend work?
7. **Your agents** — the runner drives Claude only. You also use Gemini and Copilot. Is cross-agent testing worth building, or is a mid-tier single-agent proxy good enough?

The harness lives in `verification/token-burn/` (one script, no dependencies). Answers, objections, and "you're measuring the wrong thing entirely" all welcome — that's the point of asking.
