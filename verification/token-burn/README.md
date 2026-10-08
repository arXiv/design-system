# Agent build tests

These tests answer one question: given only this repository, does an AI coding agent build an arXiv page that Shamsi accepts visually and that conforms to the design system technically?

The plan (which tests, in what order, and what finishing means) is in `whiteboard/planning/TESTING-PLAN.md`. This file describes how one test works.

## One test, five steps

1. **Spec.** Claude writes `tests/<name>/spec.md` in product words. It names no classes or components. Shamsi reviews it before anything is built. Sample content goes in `content.md`, and the notes on what to look for go in `scoring.md`, written before the builds.
2. **Build.** Each build runs a fresh headless agent in a clean copy of the repository. The copy leaves out `verification/` and `whiteboard/`, so the builder cannot see the scoring notes, earlier results, or the mockups. By default there are four builds: two with Sonnet and two with Opus.
3. **Technical evaluation.** Claude does this. Computed checks run first, then Claude reads each builder's reasoning.
4. **Visual review.** Shamsi sees one build at a time, labelled A to D in shuffled order, without knowing which model made it. For each she answers "What is off?" and gives a verdict: accept, accept with changes, or reject. After the last one she sees them together and can add notes.
5. **Summary.** One short page with thumbnails, both verdicts for each build, which model made which, what the builds had in common, and what changed in the design system as a result.

## Commands

    python3 verification/token-burn/round.py build tests/01-search-simple
    python3 verification/token-burn/round.py evaluate runs/<run>
    python3 verification/token-burn/round.py review runs/<run>      # then open http://127.0.0.1:8765/
    python3 verification/token-burn/round.py summary runs/<run>
    python3 verification/token-burn/round.py report runs/<run>      # the one-page report for the team

Run them from `verification/token-burn/`. `evaluate` needs Playwright (`pip install playwright`, `playwright install chromium`). `build` accepts `--models`, `--reps`, and `--budget`. `summary` writes the detailed report; `report` writes the short one for the team, graded as described in [GRADING.md](GRADING.md).

## Usage and billing

Builds run on the Claude subscription that the `claude` command is signed in to. `build` refuses to start if an API key is configured, runs one build at a time, and starts no further builds once a build reports usage beyond what the plan includes. `--budget` (10 by default) stops a single build that runs away; the figure is the estimated cost of the tokens, and on a subscription nothing is charged for it. Whether usage beyond the plan is allowed at all is an account setting at claude.ai (Settings, Usage, extra usage), and the runner cannot change it.

## What the computed checks cover

For every page of every build: CSS written outside the one permitted file, classes that are defined nowhere, classes the builder invented, colours that are not in the design system, changes to existing files, anything loaded from another host, broken file paths, horizontal overflow at 768px and 320px, axe-core accessibility rules in light mode, contrast in dark mode, the tab order and whether each stop shows focus, and how much text is left with JavaScript off. It also takes screenshots at desktop width, at phone width, in dark mode, and with JavaScript off.

The results are in `runs/<run>/<label>/evaluation.json`. Claude writes its conclusions in `runs/<run>/technical.json`:

    {"result": "...", "builds": {"A": {"verdict": "...", "notes": "..."}}, "patterns": ["..."], "changes": ["..."]}

## What is recorded

Committed for each run: the spec, the built files, the screenshots, the measurements, Shamsi's review, and the summary. Not committed: transcripts and error logs.

Each run keeps a copy of the stylesheets and scripts as they were when it was built (`snapshot/`), and the review server uses that copy. Later changes to the design system do not change how an old build looks. Fonts, icons, and images come from the current repository. `run.json` records the commit.

## The July battery

`retired/` holds the five tasks, rubrics, and scripts used in July 2026. Most of those tasks asked for things the design system now documents. Their results are in `BASELINE-RESULTS.md`, `REORG-COMPARISON.md`, and the older folders in `runs/`.
