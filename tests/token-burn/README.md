# Token-burn test harness

Measures whether this repo is structured so an AI agent can do frontend work
in it **efficiently** (token burn, reading path) and **correctly** (rules
followed, violations flagged, good judgment where no rule exists). Built
2026-07-28 for Phase 1 of NEXT-STEPS.md: run a baseline, reorganize the repo,
re-run, compare.

## How it works

Each test cell copies the repo (minus `tests/` and `.git`) into a clean temp
workspace and runs a headless Claude agent (`claude -p`, Sonnet) on one task
prompt inside it. The agent never sees the tasks, rubrics, or previous
results — so the battery stays honest. The runner captures the full
transcript, diffs the workspace to collect what the agent built, computes
metrics, and generates a review page.

## The battery (5 tasks × 2 reps by default)

| Task | Family | What it measures |
|---|---|---|
| 01 fidelity build | specced, public | finds + applies documented rules (card, links, truncation) |
| 02 fidelity internal | specced, internal | surface identification (lime vs blue), component reuse |
| 03 extrapolation | underspecified | reasoning from the *why* prose where no spec exists |
| 04 violation trap | adversarial spec | guardrails: flag + compliant alternative, not silent compliance |
| 05 real type badges | real backlog item | completing a partially-documented real pattern (retires once the real page is built) |

## Running

```bash
bash tests/token-burn/run.sh              # full battery (≈10 agent runs)
bash tests/token-burn/run.sh --smoke      # cheap plumbing check
bash tests/token-burn/run.sh --task 03    # one task
bash tests/token-burn/run.sh --variant digest --repo-dir /path/to/alt-repo
```

The `--variant/--repo-dir` form tests an alternate repo structure (e.g. a
specs-only digest) with the same battery — that comparison is the controlled
experiment for whether the rationale prose earns its token cost.

## Reviewing

Open `runs/<stamp>-<variant>/review.html` (or `runs/index.html`). Each cell
shows metrics, auto-check flags (external resources, planted trap markers,
non-palette hexes), the agent's final message, its reading path, and the
built page in an iframe. Grade each cell (pass / minor / fail + notes —
stored in your browser), then **Export grades** and paste the JSON back to
Claude for the results write-up. Score against `rubrics/`.

Committed per run: metrics, prompts, artifacts, review page. Not committed:
raw transcripts and stderr logs (bulky; see `.gitignore`).

## Interpreting the metrics

- **Tokens / cost** — the headline burn per task; compare across variants.
- **Files read (calls · unique · re-reads)** — the reading path. High
  re-reads or many unique files for a small task suggest structure problems;
  the ordered list shows *where* an agent wandered.
- **Auto-check flags** — hard tells (external fonts/CDNs, planted trap
  values, off-palette hexes). Any flag on tasks 01–03/05 is a correctness
  miss; flags on 04 mean the trap was reproduced instead of refused.
- **Designer grades** — the half the machine can't do. "Efficient but
  fails the visual pass" means the structure is optimizing the wrong thing.
