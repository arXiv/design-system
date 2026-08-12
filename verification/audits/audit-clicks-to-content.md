# Clicks-to-content audit

**Started 2026-08-12. Partial — see *Status* before quoting any number.**

Measures how much work it takes to do the three things a researcher actually came to do,
on arXiv and on the platforms researchers move between. Exists to turn one of arXiv's
functional brand claims — that publisher sites bury core tasks and arXiv surfaces them —
from an assertion into a table.

## Protocol

**Start at the paper's own landing page.** Not a homepage, not a Google Scholar result.
That is how researchers actually arrive (search result, citation link, a colleague's
message), it is the only starting point every platform shares, and it isolates the part
arXiv controls.

**Measure logged out**, in a clean profile. That is the state someone meeting a paper for
the first time is in, and it is the state that reveals gates.

**The three tasks:**

1. Download the PDF
2. View the full paper as HTML
3. Copy a citation

**Record per task:** clicks, whether the control is visible without scrolling, how far down
the page it sits, whether the task can be completed at all, and whether login is required.
A paywalled PDF is a different and more damning result than a long click path, and
collapsing it into a click count hides the worst finding.

**Record per page:** load time, page weight, and whether a cookie or consent dialog
appears before the task can start. Those dialogs are real friction and belong in the count.

### On measuring time-on-task

The original idea was to time each task and express other platforms as a percentage of
arXiv. Attractive, but an agent's clock cannot stand in for a human's: an agent reads the
page structure directly instead of scanning it visually, so its elapsed time is dominated
by network and tooling rather than by *finding* anything. A slow site with an obvious
button would score worse than a fast site with a buried one — backwards from what this
audit is for.

Three measures give the same intuitive comparison honestly:

- **Load time as a percentage of arXiv's** — machine-measured, mode-independent, and it is
  already arXiv's own Speed proxy.
- **Clicks as a ratio** — "three times the clicks" reads as plainly as any percentage.
- **Scroll depth to the control** — a real proxy for human search effort, in pixels.

If a genuine human time-on-task number is wanted later, it needs humans: a handful of
researchers, the same three tasks, a stopwatch. That is a usability test, and it would be
worth doing on its own terms rather than simulated here.

## Status — why this is unfinished

**Most publisher platforms block automated clients.** Verified 2026-08-12 with a normal
desktop browser user-agent:

| Platform | Result |
|---|---|
| arXiv | 200 — measured |
| Nature | 303 → page loads — measured |
| Zenodo | loads — measured, but see note |
| PubMed Central | 200 to `curl`; the in-app browser refused the navigation — retry by hand |
| bioRxiv | **429** rate-limited |
| APS (Physical Review) | **403** forbidden |
| ScienceDirect (Elsevier) | **403** forbidden |
| IEEE Xplore | bot-check page, "unusual traffic detected" |

So the automatable sample is small and biased toward platforms that permit bots — which is
not a random subset. **This audit needs a person with an ordinary browser to finish**,
maybe an hour of work. The protocol above and the table below are the instrument; the rows
just need filling.

No attempt was made to work around any of these blocks.

## Results so far

Reference viewport 1280×720. One paper per platform, so treat every number as indicative
rather than settled.

| | arXiv | Nature | Zenodo |
|---|---|---|---|
| Sample | `2301.08727` | `s41586-021-03819-2` | `records/3723939` |
| **Load time** | **650 ms** | 3,332 ms | 6,728 ms |
| vs arXiv | — | **+413%** | **+935%** |
| Page weight | 42 KB | 147 KB | 30 KB |
| **PDF** | 1 click, 93px | 1 click, 390px | 1 click, 3,076px |
| **HTML full text** | 1 click, 112px | 0 clicks — landing page *is* the full text | not applicable |
| **Citation** | 1 click, 420px | 1 click, 1,908px | 1 click, 7,673px |
| Citation scroll depth vs arXiv | — | 4.5× deeper | 18× deeper |
| Paywall / login | none | none (open access sample) | none |

**Zenodo caveat:** the record sampled is a dataset, not a paper, so "download the PDF" and
"view HTML" do not really apply. It is in the table for load time only. A paper record
would be a fairer comparison.

**Nature caveat:** an open-access article was sampled. A paywalled one would change the
paywall row completely, and picking only open articles would flatter every publisher in
this table. Whoever finishes this should sample both.

## What the three measured rows suggest

Nothing conclusive from three samples, but the shape is visible and worth confirming: arXiv
loads in a fifth of Nature's time and a tenth of Zenodo's, and puts all three tasks within
the first screen. The clearest gap is not clicks — every platform here reached the PDF in
one click — but **depth**: arXiv's citation control sits 420px down, Nature's at 1,908px,
Zenodo's at 7,673px. If the finished audit holds this pattern, the honest claim is narrower
and stronger than the one BRAND.md currently makes. Not *"publishers bury tasks behind many
clicks"* — they mostly do not — but *"arXiv puts them where you are already looking."*
