# Test protocol description - I want your feedback!
Shamsi Brinn
07/30/26

## What this is

I want to test whether an AI coding agent, given only this repo, does frontend work correctly and cheaply. I've used Claude to set up five testing tasks: 
1. build a new component from the design system guidelines (a component that doesn't exist in the design system yet)
2. reuse existing components in the design system
3. complete a deliberately under-specified design problem
4. test if it completes one request that violates arXiv policy on purpose (it should not do it, but flag it to the user instead)
5. complete one real backlog item (a pattern our docs mention but never demo — note the agent can't see the backlog itself; test workspaces exclude /planning/ along with the answer keys)

I used Fable to build the tests but I'm conducting them with Sonnet so that frontier models don't become a crutch for poor documentation. (if the design system doesn't answer a question I don't want the model to hack into Hugging Face looking for an answer :-D :-D )

Each test gets run twice, headless. Each run executes in a clean copy of the repo with the test definitions removed, so the agent can't find the answer key. Per Claude's advice I'm recording: 
- tokens burned
- files read and in what order
- auto-scanned violations (external font/CDN loads, off-palette colors, planted traps)
- I also visually scan the output and compare with official pattern pages (ie: https://arxiv.github.io/design-system/docs/buttons.html)

## What it found so far

I've just restructured the repo and ran the tests before and after to see if it made a difference. There is a long ways to go but the testing did help:

| | Before | After |
|---|---|---|
| Visual review | 4/10 pass | 6/10 pass |
| Policy violations | 3 | 0 |
| Files read per battery | 106 | 83 |

The biggest finding: Sonnet mostly worked exactly as expected and a frontier model does not appear to be necessary. The problem that the tests uncovered was significant **documentation coverage gaps**. There were many questions the agent needed to answer that I had never written down. Details are in [REORG-COMPARISON.md](REORG-COMPARISON.md) and [BASELINE-RESULTS.md](BASELINE-RESULTS.md).

## Your help
I'd love your technical perspective on these aspects of the tests so I can improve them.
1. **Task coverage** — are these the right kinds of work? What do you actually hand to an agent that we should be testing?
2. **Rigor** — two runs per task. Is that sufficient? How would you handle run-to-run variance without tripling our costs?
3. **Metrics** — anything you'd add or drop? (e.g., diff-against-reference, time-to-first-correct)
4. **Cadence** — when should we run these tests so it stays useful without becoming too much maintenance? Manually by devs? On merging?
5. **Trust** — what would you need to see in test results to trust `AGENTS.md` and `docs/` as your source of truth for frontend work?
6. **Agent agnostic** — I'm testing with Claude (sonnet). Some people use Gemini and Copilot. Is cross-agent testing worth building?

The harness lives in `verification/token-burn/` (two small scripts, no dependencies). All thoughts are welcome! I'll feed them to Fable for improvement.
