# Clicks-to-content audit

**Run 2026-08-12**

This test measures how much work it takes to do common tasks that researchers do on article pages, and measure how arXiv stacks against others in the publishing ecosystem.

## Results

### Doing the task

| Platform | Type | Access | Full text | PDF | Citation |
|---|---|---|---|---|---|
| **arXiv live** | Preprint server | open | **1 click — separate page** | 1 click | modal, **no copy button** |
| **arXiv Phase 1 mockup** | Preprint server | open | **0 clicks — on the page** | 1 click, + sticky bar while reading | 1 click → **Copy** |
| APS | Publisher | open | 0 clicks | 1 click | modal, no copy button |
| ScienceDirect | Publisher | open | 0 clicks | 1 click | 2 clicks → file export only |
| IOP Science | Publisher | open | 0 clicks | 1 click | BibTeX/RIS file *(not exercised)* |
| Nature | Publisher | open | 0 clicks | 1 click | 1 click *(not exercised)* |
| PubMed Central | Repository | open | 0 clicks | *not exercised* | *not exercised* |
| PLOS ONE | Publisher | open | 0 clicks | *not exercised* | *not exercised* |
| Wiley | Publisher | open | 0 clicks | 1 click | 1 click → **COPY TEXT** |
| ACM DL | Publisher | open | PDF only *(reader view not exercised)* | 1 click | 1 click → **Copy citation** |
| Springer Link | Publisher | **paywalled** | not available | Buy PDF, USD 39.95 | 1 click |
| IEEE Xplore | Publisher | **paywalled** | not available — section titles listed, body gated | gated | 1 click |
| Taylor & Francis | Publisher | **paywalled** | not available | USD 56 / USD 136 | 1 click |
| ResearchGate | Network | open | 1 click — *page images, not text* | 1 click | 1 click → file only; *Copy link* copies the URL |
| Quantum | Overlay journal | open | 1 click — *PDF, hosted by the journal* | 1 click | 1 click → BibTeX shown inline, select by hand |
| Open Journal of Astrophysics | Overlay journal | open | 1 click — *offsite, to arXiv* | via arXiv | 2 clicks → BibTeX file |

### What is in the way

Measured on arrival, logged out, at 1280×800, three seconds after load. Sorted by
third-party domains.

| Platform | Third-party domains | Ad / tracking networks | Cookies | Ad slots | Title at | Pushed down by | `<h1>` | Images no alt | Skip link |
|---|---|---|---|---|---|---|---|---|---|
| **arXiv Phase 1 mockup** | **3** | **0** | **0** | **0** | 244px | **0px** | **1** | 0/8 | yes |
| PubMed Central | **3** | 2 | 8 | 1 | 614px | 75px | 1 | 4/40 | yes |
| **arXiv live** | **4** | **0** | 4 | **0** | **56px** | **0px** | **7** | 0/7 | yes |
| **Quantum** | **4** | **0** | **0** | **0** | 0px | **0px** | 2 | 0/16 | yes |
| **Open Journal of Astrophysics** | **4** | **0** | 4 | 1 | 436px | 55px | 1 | 0/1 | **no** |
| ScienceDirect | 15 | 3 | 9 | 0 | 112px | 0px | 1 | 0/27 | **no** |
| ACM DL | 16 | 5 | 7 | 8 | 437px | **544px** | 1 | **13/25** | yes |
| ResearchGate | 17 | 7 | 20 | 4 | 264px | 213px | 1 | 0/33 | **no** |
| IEEE Xplore | 19 | 4 | **41** | **17** | 272px | 0px | 3 | 1/4 | yes |
| IOP Science | 23 | 8 | 25 | 0 | 174px | 0px | 1 | 0/61 | **no** |
| PLOS ONE | 25 | 7 | 8 | 4 | 385px | 180px | 2 | 0/35 | yes |
| APS | 26 | 10 | 10 | 0 | **89px** | 0px | 5 | 0/20 | yes |
| Springer Link | 31 | 15 | 17 | 3 | 209px | 0px | 1 | 2/18 | yes |
| Nature | 36 | 19 | 22 | 8 | 351px | **528px** | 1 | 6/24 | yes |
| Wiley | 42 | 15 | 23 | 4 | **441px** | 120px | 1 | 0/35 | yes |
| Taylor & Francis | **46** | 16 | **30** | 1 | 352px | 80px | 1 | 0/8 | yes |

Networks named, so the classification can be checked rather than trusted:

| Platform | Ad / tracking networks |
|---|---|
| arXiv (live and mockup), Quantum, Open Journal of Astrophysics | **none** |
| PubMed Central | Google Analytics, Google Tag Manager |
| ScienceDirect | DoubleClick, New Relic, OneTrust |
| ResearchGate | **DoubleClick, Criteo, AppNexus**, Google Analytics, Google Tag Manager |
| Springer Link | **DoubleClick ×2, Facebook, Twitter Ads, Bing Ads**, Segment, Google Tag Manager |
| Nature, Wiley, Taylor & Francis, ACM, IEEE, IOP, APS, PLOS | Google Publisher Tag / DoubleClick plus analytics and consent platforms |

## Findings

**1. arXiv is one click behind on the most common task.** Every open-access platform measured
except ACM and ResearchGate serves the full paper on the landing page. arXiv alone sends the
reader to a separate `/html/` page. The Phase 1 mockup closes this, and is the only page
measured where the full text costs nothing *and* the PDF stays reachable while reading.

**2. Copy-to-clipboard for citations is uncommon but not unique.** ACM and Wiley have one.
arXiv live and APS show text to select by hand; ScienceDirect and IOP hand over a file. The
Phase 1 mockup has one. **Adding a copy button to arXiv's existing BibTeX modal is a small win
available today, independent of Phase 1.**

**3. The distraction split is commercial versus non-commercial, and it is absolute.** The five
non-commercial platforms load 3–4 third-party domains. Every commercial platform loads 15–46.
Nothing sits in between. Four carry zero advertising or tracking networks: arXiv twice,
Quantum, and the Open Journal of Astrophysics.

**4. ACM pushes its paper's title 544px down the page, Nature 528px** — roughly two-thirds of
the first screen on an 800px window, spent before the paper is named. arXiv live puts its title
at 56px, the highest of anything measured. Both arXiv pages push it 0px.

**5. IEEE loads 17 ad slots and sets 41 cookies** on an article body it will not show without a
subscription. Springer runs 15 tracking networks on a page that costs USD 39.95 to read.

**6. Ads and tracking are separable.** APS and IOP carry no ad slots and place their titles
high, but still load ten and eight tracking networks. Not selling ad space is not the same as
not measuring readers. arXiv does neither.

**7. The real gap is access, not clicks.** Springer, IEEE and Taylor & Francis give a reader
with no subscription neither the HTML nor the PDF, at USD 39.95, gated, and USD 56. IEEE lists
the section titles above a body it will not show. Against that, click counts are a rounding
error.

**8. Overlay journals delegate the reading experience to arXiv.** Neither Quantum nor the Open
Journal of Astrophysics hosts the full text — OJAp links out with "Read article at ArXiv". For
these journals arXiv's article page *is* the reading experience they give their readers, so
Phase 1 improves their product too.

**9. arXiv's distraction advantage is structural, not disciplinary.** It costs no ongoing
restraint, because no commercial incentive pushes the other way. Three other non-commercial
platforms land in the same place independently.

## What arXiv should fix

| Where | Fix | Evidence |
|---|---|---|
| Live site | Seven `<h1>` elements on the abstract page — heading navigation is meaningless for screen reader users | Direct count; the mockup has exactly one |
| Live site | No copy button on the BibTeX modal | ACM and Wiley have one; the mockup has one |
| Live site | Full text is a separate page | Every open-access publisher measured serves it inline |

Nothing outstanding on the Phase 1 mockup. Its citation popover, single `<h1>`, sticky PDF
control, zero trackers and zero push-down are all confirmed.

## Methodology

**Start at the paper's own landing page.** Not a homepage or a Google Scholar result.

**Measure logged out**, without institutional access to paywalled content, at 1280×800, three
seconds after load.

**The three tasks:** download the PDF, view the full paper as HTML, copy a citation.

**Record per task:** clicks; whether the control is visible on arrival without scrolling;
whether it remains reachable while reading a long paper (a sticky bar counts); whether the task
can be completed at all; and whether login is required. Note whether the control sits in the
reading *column* or a side *rail* — a rail control is found by scanning sideways, so its
vertical depth means little. A paywalled PDF is a different and more damning result than a long
click path, and collapsing it into a click count hides the worst finding.

**Distraction measures.** Third-party domains: every distinct host contacted whose registrable
domain differs from the page's own. Ad and tracking networks: the subset matching known
advertising, analytics, session-recording and consent-management services, named individually
so the classification can be checked. Ad slots: elements that are an advertising iframe, carry
an advertising class or id, or are literally labelled "Advertisement" — a deliberately strict
test. Pushed down by: the summed height of ad slots positioned above the paper's title.

**"Cited by" and "Related articles" are related-content links, not distractions.** They serve
the reader even when commercially motivated, and counting them as clutter would make the
headline number arguable. Likewise a sticky panel holding the article outline is content.

**Structure measures.** Count of `<h1>` elements, which should be one; images lacking an `alt`
attribute; whether the first focusable element is a skip link. Count **visible** elements only
— a link hidden from view is not announced either, and including hidden ones inflates counts
several-fold.

### What needs a human

**Whether following a citation strands the reader.** Two automated approaches were tried and
both failed. Counting return links by their text produced false failures, because a popover
needs no return link — the platforms handling this best scored worst. Clicking citations
programmatically is also unreliable: synthetic mouse events do not always trigger real
handlers, hover-triggered panels never fire, and "nothing visibly happened" cannot be told
apart from "the handler did not run".

Two platforms gave a clear enough answer to record: the **arXiv Phase 1 mockup** and **Wiley**
both show the reference in a popover and do not move the reader. The other fourteen need a
person clicking a citation and reporting what they see — roughly twenty minutes, and the
highest-value remaining item in this audit.

**Screen reader experience.** The structure measures above are what a machine checks reliably.
Whether announcements make sense in sequence, whether reading order is confusing, how
disorienting a jump feels — those need a person running VoiceOver, NVDA or JAWS.

**Also unexercised:** ACM's reader view, IOP's citation control, and the PDF and citation
controls on PubMed Central and PLOS ONE. Marked in the table rather than guessed at.

### Additional methodology for automated agentic testing

**Exercise every control; never infer behaviour from the markup.** Every mistake this audit
made came from reading elements instead of clicking them: a `Copy` button beside the one a
probe found first, a modal misread as a page navigation, and a citation popover scored as a
missing return link.

**HTTP 200 does not mean access.** Springer, IOP, Frontiers and IEEE all serve challenge or
CAPTCHA pages with a 200 status. Publisher sites refuse automated browsers generally — these
readings were taken in a human's ordinary Chrome, driven by an agent.

**Let the page settle.** Probed immediately after load, APS reports 3 third-party domains;
after three seconds, 26. A reading taken without a delay is wrong.

**Fix the viewport and check it.** In a collapsed browser pane the arXiv mockup put its PDF
control at 6,104px; at 1280×800 the same control sits at 496px.

Google Scholar's `gs-casa` overlay is injected on top of publisher pages by the reader's own
Google session. It is not the platform's design and is excluded everywhere.

### Pages used

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
