# How Claude reports back: a proposal

2026-10-07. For the process conversation Shamsi asked for. Nothing here is in use yet.

## The problem

After a work session, Claude sends back more than Shamsi can take in: long messages, many questions at once, and lists of every change. This week that also led to mistakes in what was said, for example deleting the search prototype she still needed, and calling a docs disagreement a "conflict" when it was not one.

## The proposal

**1. The end-of-session message has three parts and fits on one screen.**
- *What changed:* at most three lines.
- *What needs you:* at most three items, each one decision, each with Claude's recommendation.
- *Links:* full `file:///` links to what to look at.

Anything longer goes in a file, and the message links to it.

**2. One decision at a time.** Claude asks only what it cannot decide from the docs or a sensible default. Questions that can wait, wait, and are listed in `HANDOFF.md` instead of in the message.

**3. New prose goes in a file, not the message.** Every sentence Claude writes for the docs is still listed, so Shamsi can wordsmith, but in one file per session, linked from the message.

**4. Check before saying it is done.** Claude renders the page and looks at it before reporting a visual change, and runs the checks before reporting that they pass. Anything it did not check, it says it did not check.

**5. Look before deleting.** Before deleting a file, Claude checks whether anything links to it and whether Shamsi is still using it. If unsure, Claude asks, or moves it rather than deleting it.

**6. Long runs end with one page.** After an overnight or long run, a single page in `whiteboard/planning/` holds what was done and what needs Shamsi. The message only links to it.

## For Shamsi to decide

Which of these to keep, and whether "fits on one screen" is the right limit.
