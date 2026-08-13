# Clicks-to-content audit

**Run 2026-08-12**

This test measures how much work it takes to do common tasks that researchers do on article pages, and measure how arXiv stacks against others in the publishing ecosystem.

## Results

| Platform | Type | Access | Full text | PDF | Citation |
|---|---|---|---|---|---|
| **arXiv live** | Preprint server | open | **1 click — separate page** | 1 click | modal, **no copy button** |
| **arXiv Phase 1 mockup** | Preprint server | open | **0 clicks — on the page** | 1 click, + sticky bar while reading | 1 click → **Copy** |
| APS | Publisher | open | 0 clicks | 1 click | modal, no copy button |
| ScienceDirect | Publisher | open | 0 clicks | 1 click | 2 clicks → file export only |
| IOP Science | Publisher | open | 0 clicks | 1 click | BibTeX/RIS file only |
| Nature | Publisher | open | 0 clicks | 1 click | 1 click *(not exercised)* |
| PubMed Central | Repository | open | 0 clicks | *not exercised* | *not exercised* |
| PLOS ONE | Publisher | open | *not exercised* | *not exercised* | *not exercised* |
| Wiley | Publisher | open | 0 clicks | 1 click | 1 click → **COPY TEXT** |
| ACM DL | Publisher | open | **not available — PDF only** | 1 click | 1 click → **Copy citation** |
| Springer Link | Publisher | **paywalled** | not available | Buy PDF, USD 39.95 | 1 click |
| IEEE Xplore | Publisher | **paywalled** | not available — section titles listed, body gated | gated | 1 click |
| Taylor & Francis | Publisher | **paywalled** | not available | USD 56 / USD 136 | 1 click |
| ResearchGate | Network | open | 1 click — *page images, not text* | 1 click | 1 click → file only; *Copy link* copies the URL |
| Quantum | Overlay journal | open | 1 click — *PDF, hosted by the journal* | 1 click | 1 click → BibTeX shown inline, select by hand |
| Open Journal of Astrophysics | Overlay journal | open | 1 click — *offsite, to arXiv* | via arXiv | 2 clicks → BibTeX file |


## Findings

1. **arXiv is one click behind on the most common task**
Of the open-access articles
measured, every publisher except ACM serves the full text on the landing page — APS,
ScienceDirect, IOP, Nature, PMC, Wiley. arXiv alone sends the reader to a separate `/html/`
page. The [Phase 1 mockup](https://arxiv.github.io/design-system/mockups/public/html-phase1.html) of the new HTML Papers page serves up the full article as well as metadata and the PDF, and catches arXiv up to other publishers.
1. **Copy-to-clipboard for citations is uncommon but not unique**
ACM (`Copy citation`) and Wiley
(`COPY TEXT`) both do. arXiv live and APS show text to select by hand; ScienceDirect and
IOP create a file. The [Phase 1 mockup](https://arxiv.github.io/design-system/mockups/public/html-phase1.html) adds a user-friendly citation feature which will group arXiv with the more user-friendly half of the
field. *Live arXiv adding a copy button to its existing BibTeX modal is a small, obvious win, independent of Phase 1.*
1. **The shift to Open Access means less gatekeeping**
Three of thirteen — Springer, IEEE, Taylor &
Francis — provide neither the HTML nor the PDF. The other publishers match arXiv in providing the full text of the paper to readers at no cost.
1. **arXiv's interface has fewer distractions**
Most of the publisher sites
1. **arXiv's Phase 1 Mockup is the most accessible and least disrupted experience**
Due to optimizations like [help me write this section on what accessibility improvements we have brought into the Phase 1 mockup].
1. **arXiv's true impact is not visible**
Our core benefit to the scientific community is faster access to the latest research, and it cannot be inferred from the UI. Our platform design can support this key benefit by reducing frictions for all our users, including those who use assistive tech; We can make it as easy as possible to submit, read, or download artifacts; And we can optimize for secondary tasks like copying a citation or sharing a specific formula with a colleague. UI work can never replace or supercede our core benefit, only enhance it. 

### Live arXiv vs the Phase 1 mockup

The two differ in an interesting way:

| | arXiv live | HTML Phase 1 mockup |
|---|---|---|
| Sample | `arxiv.org/abs/2301.08727` | [html-phase1.html](https://arxiv.github.io/design-system/mockups/public/html-phase1.html) |
| Load time | 650 ms | 743 ms |
| Page weight | 42 KB | 143 KB |
| **View full HTML** | 1 click, 112px | **0 clicks — the paper is already on the page** |
| **Download PDF** | 1 click, 93px | 1 click, 496px — *and* permanently in the sticky bar while reading |
| **Copy a citation** | 1 click, 420px → modal, then **select and copy by hand — there is no copy button** | **1 click, 661px — a `Copy` button does it** |

**What the mockup wins.** It removes a whole navigation step: the full text is the page, so
the most common reader task costs nothing. Copying citations in one click is better than about half of the fiels, and equals the other half. 

**4. Overlay journals delegate the reading experience to arXiv.** Neither Quantum nor the
Open Journal of Astrophysics hosts the full text as a page of its own — Quantum serves the
PDF, OJAp links straight out to arXiv with "Read article at ArXiv". For these journals,
arXiv's article page *is* the reading experience they hand their readers. Improving it
improves their product too.

## Methodology

Setup:
- Start at the paper's own landing page, not a homepage or a Google Scholar result.
- Measure logged out, without institutional access to paywalled content.

The three tasks measured:
1. Downloading the PDF
1. Viewing the full paper as HTML
1. Copying a citation

**Record per task:** 
- clicks; **whether the control is visible on arrival without
scrolling**, and the smallest window height at which that stays true.
- whether it remains
reachable while reading a long paper (a sticky bar counts)
- whether the task can be
completed at all (gated articles are unreachable)
- and whether login is required. 

Note the control's position as *column* or
*rail* — a rail control is found by scanning sideways.
Raw pixel depth is worth recording but is a supporting number, not the headline. 

A paywalled PDF is a different and more damning result than a long click path, and
collapsing it into a click count hides the biggest blocker for scientists.

### Additional methodology for automated agentic testing
**Exercise every control; never infer behaviour from the markup.** Click it, watch what happens, and record
what the reader ends up holding. 

**Fix the viewport at 1280×800 and check it before every reading.** Any number taken at an unrecorded window size is worthless.

**Record per page:** load time, page weight, and whether a cookie or consent dialog
appears before the task can start. Those dialogs are real friction and belong in the count.

**Run in Chrome using the Claude Plugin.** Initial attempts were refused by
most publishers — APS and ScienceDirect returned 403, bioRxiv 429, and Springer, IOP,
Frontiers and IEEE served challenge or CAPTCHA pages that returned HTTP 200. Working in the user's own Chrome every platform served normally.

### Measuring time-on-task

True time-on-task testing needs to be done manually by humans with a stopwatch, and preferably not by staff who have a pro-arXiv bias. Until we have such results, these automated testing measures give a similar intuitive comparison:

- **Load time as a percentage of arXiv's** — machine-measured, mode-independent, and a useful proxy for speed.
- **Clicks as a ratio** — "three times the clicks" reads plainly as a comparison to arXiv.
- **Scroll depth to the control** — a real proxy for human search effort, in pixels.

We will include these measures when we conduct real usability testing on the Phase 1 HTML Papers page. Numbers for non-arXiv publishers would require seperate usability testing, possibly paid, if genuine human time-on-task number is wanted later. 

### Papers used

| Platform | URL |
|---|---|
| arXiv live | `arxiv.org/abs/2301.08727` |
| arXiv Phase 1 mockup | `arxiv.github.io/design-system/mockups/public/html-phase1.html` |
| APS — Phys Rev Lett | `journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102` |
| ScienceDirect | `sciencedirect.com/science/article/pii/S037026931200857X` |
| IOP Science | `iopscience.iop.org/article/10.3847/1538-4357/ae8190` |
| Nature | `nature.com/articles/s41586-021-03819-2` |
| PubMed Central | `pmc.ncbi.nlm.nih.gov/articles/PMC8371605/` |
| PLOS ONE | `journals.plos.org/plosone/article?id=10.1371/journal.pone.0173664` |
| Wiley | `advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202004433` |
| ACM Digital Library | `dl.acm.org/doi/10.1145/3292500.3330701` |
| Springer Link | `link.springer.com/article/10.1007/s00453-021-00817-8` |
| IEEE Xplore | `ieeexplore.ieee.org/document/9156697` |
| Taylor & Francis | `tandfonline.com/doi/full/10.1080/00223980.2019.1590298` |
| ResearchGate | `researchgate.net/publication/411823724_Implicit_Computation_of_Filtered_Prime_Implicants` |
| Quantum | `quantum-journal.org/papers/q-2026-07-29-2178/` |
| Open Journal of Astrophysics | `astro.theoj.org/article/166984-dust-and-grain-size-evolution-in-galaxy-simulations-what-matters-and-what-does-not` |
