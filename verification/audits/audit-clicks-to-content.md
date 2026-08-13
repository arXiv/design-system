# Clicks-to-content audit

Date: 08/12/2026

This test measured how much work it takes to do common tasks on article pages, and how arXiv stacks against others in the publishing ecosystem.

## Results

Across platforms, measure how easy it is to do three common tasks: Download the PDF, access the full text, and grab a citation. We are also necessarily checking for gated vs open content.

| Platform | Access | Full text | PDF | Citation |
|---|---|---|---|---|
| arXiv live | open | **1 click — separate page** | 1 click | 1 click → manually select |
| arXiv Phase 1 mockup | open | 0 clicks | 1 click, + sticky bar while reading | **1 click** |
| APS, Physical Review Letters | open | 0 clicks | 1 click | 1 click → manually select or file export |
| Elsevier, Physics Letters B | open | 0 clicks | 1 click | 1 click → file export |
| IOP Science | open | 0 clicks | 1 click | 1 click → file export  |
| Springer Nature, Algorithmica | paywalled | gated | 1 click | 2 clicks → file export |
| Springer Nature, Nature Communications | open | not available | 1 click | 2 clicks → file export |
| NIH, PubMed Central | open | 0 clicks | 1 click | 2 clicks |
| PLOS ONE | open | 0 clicks | *not exercised* | 1 click → file export (hard to find) |
| Wiley, Advanced Materials | paywalled | gated | gated | 2+ clicks |
| Wiley, Advanced Science | open | 0 clicks | 1 click | 2+ clicks |
| ACM DL | open | not available | 1 click | 2 clicks |
| IEEE Xplore | paywalled | section titles listed, body gated | gated | 2+ clicks |
| Taylor & Francis, Journal of Psychology | paywalled | gated | gated | 2+ clicks |
| Taylor & Francis, Research in Mathematics | open | 0 clicks | 1 click | 2+ clicks |
| ResearchGate | open | 0 clicks, *PDF reader only* | 1 click | 2 clicks → file export |
| Quantum (Overlay) | open | 1 click (via ar5iv) | 1 click | 1 click → manually select |
| Open Journal of Astrophysics (Overlay) | open | 2 clicks (via arXiv)  | 2 clicks (via arXiv) | 2 clicks → file export |

### Distraction vs Focus

We measured how well each platform supports reading focus by eliminating distractions (ads, popups or other unrelated content).

| Platform | Third-party domains | Ad or tracking networks | Cookies | Ad slots | Title placement | Pixel displacement |
|---|---|---|---|---|---|---|
| arXiv Phase 1 mockup | **3** | **0** | **0** | **0** | 244px | **0px** |
| PubMed Central | **3** | 2 | 8 | 1 | 614px | 75px |
| arXiv live | **4** | **0** | 4 | **0** | **56px** | **0px** |
| Quantum | **4** | **0** | **0** | **0** | 0px | **0px** |
| Open Journal of Astrophysics | **4** | **0** | 4 | 1 | 436px | 55px |
| ScienceDirect | 15 | 3 | 9 | 0 | 112px | 0px |
| ACM DL | 16 | 5 | 7 | 8 | 437px | **544px** |
| ResearchGate | 17 | 7 | 20 | 4 | 264px | 213px |
| IEEE Xplore | 19 | 4 | **41** | **17** | 272px | 0px |
| IOP Science | 23 | 8 | 25 | 0 | 174px | 0px |
| PLOS ONE | 25 | 7 | 8 | 4 | 385px | 180px |
| APS | 26 | 10 | 10 | 0 | **89px** | 0px |
| Springer Link | 31 | 15 | 17 | 3 | 209px | 0px |
| Nature | 36 | 19 | 22 | 8 | 351px | **528px** |
| Wiley | 42 | 15 | 23 | 4 | **441px** | 120px |
| Taylor & Francis | **46** | 16 | **30** | 1 | 352px | 80px |

## Findings

**1. arXiv is one click behind on full text access.** Every open-access platform measured,
except ACM and ResearchGate, serves the full paper on the landing page. arXiv sends the
reader to a separate `/html/` page. The arXiv Phase 1 mockup serves the full text and metadata on the same page, with additional improvements to usability and accessibility.

**2. Copy-to-clipboard for citations is uncommon but not unique.** ACM, Wiley, and more have a 2-click process (open a modal, copy contents). Only the arXiv phase 1 mockup reduces it to 1-click by displaying the citation area on the main page instead of in a modal; Some have copy buttons in their modal, others generate a file for download or require manually selecting, including arXiv's abstract page. *Adding a copy button to arXiv's existing BibTeX modal is a small win, independent of the Phase 1 HTML papers work.*

**3. Distraction levels are split between commercial versus non-commercial platforms.** Only arXiv and the two overlay journals have zero advertising or tracking networks. The five non-commercial platforms load 3–4 third-party domains. Every commercial platform loads 15–46. Some are egregious: IEEE loads 17 ad slots and sets 41 cookies on an article body it will not show without a subscription. Springer runs 15 tracking networks on a page that costs USD 39.95 to read.

The presence of ads and unrelated content displaces useful content. ACM pushes its paper's title 544px down the page, and Nature 528px. That is roughly two-thirds of the load screen on an 800px window. arXiv's live site puts its title at 56px, the highest of any platform measured. *The mockup puts it lower because of the prominent "back to abstract" button, which can be retired if the merged abstract and full paper page becomes the default.* That button exists to ease user confusion caused by the existence of two pages.

Ads and tracking are not the same. APS and IOP carry no ad slots and place their titles
high, but still load up to ten tracking networks. Not selling ad space is not the same as
not measuring readers. arXiv does neither.

Being free from commercial incentive really shows. arXiv does best on this metric, followed by the overlay journals, and then other open access platforms like ACM. On commercial publishing platforms, the financial incentive is right in your face and actively degrades the reading experience.

**4. Access is the biggest seperator.** Springer, IEEE and Taylor & Francis give a reader
with no subscription neither the HTML nor the PDF, at USD 39.95, gated, and USD 56. IEEE lists
the section titles above a body it will not show. Against no access at all, click counts don't matter.

**5. Overlay journals delegate the reading experience to arXiv.** Both overlay journals measured, Quantum and the Open
Journal of Astrophysics, link to us with "Read article at ArXiv". For these journals arXiv's article page *is* the reading experience they give their readers, so Phase 1 improves their product too.

**6. Accessibility is uneven.** The basics are covered on all sites (page language, basic landmarks), but there are many fails on other common features such as skip links, lack of structure, and missing alt text. arXiv's live abstract page has the sample's worst heading structure, with seven H1 elements where there should be one. 

We will continue to struggle with challenges related to the uneven markup quality in the TeX source, but we can improve in many other ways, and have done so in the HTML phase 1 mockup. Round-trip citation navigation is a particular strong point compared to the other platforms tested. 

## What arXiv can fix

1. On the live abs page, reduce to one `<h1>` element instead of seven
1. Also on the live abs page, add a button to the BibTeX modal
1. Full text is currently on a seperate page. Consider how we can make the phase 1 mockup our default abstract and full text page.

End of report. Testing methodology follows.

---

## URLs checked
1. `https://www.tandfonline.com/doi/full/10.1080/00223980.2019.1590298` (Taylor and Francis, The Journal of Psychology, paywalled)
2. `https://www.tandfonline.com/doi/full/10.1080/27684830.2026.2711512` (Taylor and Francis, Research in Mathematics, open access)
3. `https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202004433` (Wiley, Advanced Science, open access)
4. `https://advanced.onlinelibrary.wiley.com/doi/epdf/10.1002/adma.74176` (Wiley, Advanced Materials, paywalled)
5. `https://dl.acm.org/doi/10.1145/3292500.3330701` (ACM)
6. `https://ieeexplore.ieee.org/document/9156697` (IEEE)
7. `https://link.springer.com/article/10.1007/s00453-021-00817-8` (Nature, Algorithmica, paywalled)
8. `https://www.nature.com/articles/s41467-026-76467-7` (Nature, Nature Communications, open access)
9. `https://www.nature.com/articles/s41586-021-03819-2` (Nature, open access)
10. `https://iopscience.iop.org/article/10.3847/1538-4357/ae8190` (IOP, The Astrophysical Journal)
11. `https://www.sciencedirect.com/science/article/pii/S037026931200857X?via%3Dihub` (Elsevier, Physics Letters B, open access)
12. `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102` (APS, Physical Review Letters, open access)
13. `https://pmc.ncbi.nlm.nih.gov/articles/PMC8371605/` (NIH, PMC, also linked to Nature article)
14. `https://www.researchgate.net/publication/411823724_Implicit_Computation_of_Filtered_Prime_Implicants` (ResearchGate)
15. `https://arxiv.org/abs/2604.22725` (arXiv live)
16. `https://arxiv.github.io/design-system/mockups/public/html-phase1.html` (arXiv mockup)
17. `journals.plos.org/plosone/article?id=10.1371/journal.pone.0173664` (PLOS One, open access)
18. astro.theoj.org/article/166984-dust-and-grain-size-evolution-in-galaxy-simulations-what-matters-and-what-does-not` (Open Journal of Astrophysics, open access overlay)

## Methodology

Process:
- Start at the paper's own landing page, not a homepage or a Google Scholar result.
- Measure logged out, without institutional access to paywalled content.
- Measure at 1280×800 screen dimentions, and wait several seconds for all content to load.

The three tasks:
1. download the PDF
1. view the full paper as HTML
1. copy a citation

Gated content is scored as "paywalled".

Record per task:
clicks; whether the control is visible on arrival without scrolling;
whether it remains reachable while reading a long paper (a sticky bar counts); whether the task
can be completed at all; and whether login is required. 

Distraction measurements:
- Third-party domains: every distinct host contacted whose registrable
domain differs from the page's own. 
- Ad and tracking networks: the subset matching known
advertising, analytics, session-recording and consent-management services, named individually
so the classification can be checked. 
- Ad slots: elements that are an advertising iframe, carry
an advertising class or id, or are literally labelled "Advertisement" — a deliberately strict
test. 
- Pushed down by: the summed height of ad slots positioned above the paper's title.

"Cited by" and "Related articles" are related-content links, not distractions.

### Possible future usability tests

These tests would complement the existing audit but require manual human asessment, preferably by non-staff.

**Citation round-trip journey.** Whether following a citation strands the reader. Two automated approaches were tried and
both failed.

**Screen reader experience.** Automated measures can detect what a machine checks reliably.
But other measurements would need a person running VoiceOver, NVDA, or JAWS (and ideally some testing on all three). They include wether announcements make sense in sequence, whether reading order is confusing, and how
disorienting a jump feels.

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

**Note content position** and whether the control sits in the
reading *column* or a side *rail* — a rail control is found by scanning sideways, so its
vertical depth means little. A paywalled PDF is a different and more damning result than a long
click path, and collapsing it into a click count hides the worst finding.

Google Scholar's `gs-casa` overlay is injected on top of publisher pages by the reader's own
Google session. It is not the platform's design and is excluded everywhere.
