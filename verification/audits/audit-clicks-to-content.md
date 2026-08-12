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

**Record per task:** clicks; **whether the control is visible on arrival without
scrolling**, and the smallest window height at which that stays true; whether it remains
reachable while reading a long paper (a sticky bar counts); whether the task can be
completed at all; and whether login is required. Note the control's position as *column* or
*rail* — a rail control is found by scanning sideways, so its vertical depth means little.

Raw pixel depth is worth recording but is a supporting number, not the headline. The two
questions that matter are binary: **can I see it when I land, and can I still get it while
I read.**
A paywalled PDF is a different and more damning result than a long click path, and
collapsing it into a click count hides the worst finding.

**Fix the viewport at 1280×800 and check it before every reading.** This is not a detail.
Measured in a collapsed browser pane, the arXiv mockup put its PDF control 6,104px down the
page; at 1280×800 the same control sits at 496px. A twelve-fold difference, purely from
reflow. Any number taken at an unrecorded window size is worthless.

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

## arXiv today vs the Phase 1 mockup

Both measured at 1280×800 on 2026-08-12. This is the comparison the audit exists to
support, and the two differ in an interesting way rather than a simple one.

| | arXiv live | HTML Phase 1 mockup |
|---|---|---|
| Sample | `arxiv.org/abs/2301.08727` | [html-phase1.html](https://arxiv.github.io/design-system/mockups/public/html-phase1.html) |
| Load time | 650 ms | 743 ms |
| Page weight | 42 KB | 143 KB |
| **View full HTML** | 1 click, 112px | **0 clicks — the paper is already on the page** |
| **Download PDF** | 1 click, 93px | 1 click, 496px — *and* permanently in the sticky bar while reading |
| **Copy a citation** | 1 click, 420px — *navigates to a separate citation page* | **1 click, 661px — a `Copy` button in the rail, no navigation** |

**What the mockup wins.** It removes a whole navigation step: the full text is the page, so
the most common task costs nothing. And its sticky reader bar carries the PDF control at the
top of the viewport for the entire length of the paper — on the live site, once you have
clicked through to `/html/`, getting the PDF means going back.

**What "moves down" actually means — a correction.** The raw depth numbers (PDF 93px →
496px, citation 420px → 661px) read as a loss, and they are not. Both controls sit in a
right-hand actions rail at x=798, *beside* the abstract rather than below it — the abstract
column runs x=224–745. The eye reaches them by scanning right, not by scrolling. They are
visible without scrolling at every common window height tested, down to a 600px-tall
window.

**Vertical depth is the wrong measure for a rail.** It is a good proxy for a control in a
single reading column and a bad one for a control placed in a side region. Recorded here
because the metric, taken at face value, would have argued for pushing a download button
above the paper's own title — making the design worse to make the number better.

**Citation is a second win, not a gap (corrected 2026-08-12).** The rail pairs
`Display BibTeX` with a `Copy` button at the same height, so copying a citation is one
click and no navigation. On the live site, `export BibTeX citation` takes you to a separate
page, where you then select and copy by hand. The mockup is ahead here, and an earlier
version of this file undersold it.

**The narrow gap that remains.** The rail is `position: static`, so it scrolls away, and
the sticky bar carries Contents, the section list, Abstract, PDF and TeX Source — but no
citation. At 4,000px into the paper, neither citation control is on screen. This only
affects someone deep in a long paper who wants to cite it, and the fix is one more item in
a bar that already exists. Small, but it is the same problem the bar was built to solve for
PDF.

## Results so far — other platforms

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
