# Clicks-to-content audit

Date: 08/12/2026

This test measured how much work it takes to do common tasks on article pages, and how arXiv stacks against others in the publishing ecosystem. We measured seventeen competitors against the arXiv live abstract page and phase 1 HTML papers mockup.

We looked at how easy it is to do three common tasks: Download the PDF, access the full text, and grab a citation. In addition we measured the level of "distraction load," how much unrelated content each platform puts on their pages, and separately what each platform does behind the page: who it contacts and what it stores on the reader's machine. We are also necessarily checking for gated vs open content.

## Click-to-content results

| Platform | Access | Full text | PDF | Citation |
|---|---|---|---|---|
| arXiv live | open | **1 click — separate page** | 1 click | 1 click → manually select |
| arXiv Phase 1 mockup | open | 0 clicks | 1 click, + sticky bar while reading | **1 click** |
| APS, Physical Review Letters | open | 0 clicks | 1 click | 1 click → manually select or file export |
| ScienceDirect, Annals of Physics | paywalled | intro and snippets shown, rest gated | gated | 2 click → file export |
| ScienceDirect, Physics Letters B | open | 0 clicks | 1 click | 2 click → file export |
| IOP Science | open | 0 clicks | 1 click | 1 click → file export  |
| Springer Nature, Algorithmica | paywalled | gated | 1 click | 2 clicks → file export |
| Springer Nature, Nature Communications | open | not available | 1 click | 2 clicks → file export |
| NIH, PubMed Central | open | 0 clicks | 1 click | 2 clicks |
| PLOS ONE | open | 0 clicks | 1 click | 1 click → file export (hard to find buried in a dropdown) |
| Wiley, Advanced Materials | paywalled | gated | gated | 2+ clicks |
| Wiley, Advanced Science | open | 0 clicks | 1 click | 2+ clicks |
| ACM DL | open | not available | 1 click | 2 clicks |
| IEEE Xplore | paywalled | section titles listed, body gated | gated | 2+ clicks |
| Taylor & Francis, Journal of Psychology | paywalled | gated | gated | 2+ clicks |
| Taylor & Francis, Research in Mathematics | open | 0 clicks | 1 click | 2+ clicks |
| ResearchGate | open | 0 clicks, *PDF reader only* | 1 click | 2 clicks → file export |
| Quantum (Overlay) | open | 1 click (via ar5iv) | 1 click | 1 click → manually select |
| Open Journal of Astrophysics (Overlay) | open | 2 clicks (via arXiv)  | 2 clicks (via arXiv) | 2 clicks → file export |

### Distraction load results

We measured how much distracting content each platform displays to readers (ads, popups or other unrelated content). The first number is the result of a human visual scan. The rest are machine counts.

| Platform | Visual count | Ad slots | Title placement | Pixel displacement |
|---|---|---|---|---|
| arXiv live | 0 | 0 | 108px | 0px |
| arXiv Phase 1 mockup | 0 | 0 | 223px | 0px |
| APS, Physical Review Letters | 2 | 0 | 298px | 0px |
| ScienceDirect, Annals of Physics | 3 | 0 | 268px | 0px |
| ScienceDirect, Physics Letters B | 3 | 0 | 112px | 0px |
| IOP Science | 1 | 0 | 174px | 0px |
| Springer Nature, Algorithmica | 3 | 1 | 209px | 0px |
| Springer Nature, Nature Communications | 4 | 2 | 351px | 137px |
| NIH, PubMed Central | 1 | 0 | 614px | 0px |
| PLOS ONE | 2 | 2 | 385px | 90px |
| Wiley, Advanced Materials | 6 | 3 | 431px | 90px |
| Wiley, Advanced Science | 6 | 3 | 441px | 90px |
| ACM DL | 4 | 0 | 287px | 0px |
| IEEE Xplore | 4 | 1 | 272px | 0px |
| Taylor & Francis, Journal of Psychology | 3 | 0 | 351px | 0px |
| Taylor & Francis, Research in Mathematics | 2 | 0 | 368px | 0px |
| ResearchGate | 5 (including a sticky, prominent banner ad) | 2 | 264px | 122px |
| Quantum (Overlay) | 0 (not counting the sponsor links because they land far below all content) | 0 | 129px | 0px |
| Open Journal of Astrophysics (Overlay) | 1 | 0 | 422px | 0px |

Four publishers appear twice to test their open access vs subscription journals. Interestingly, the numbers barely move within a
publisher. Distraction load appears to be a property of the platform, not of the journal.

### Privacy results

These numbers are not about what the reader sees. They are what the page does out of sight: who else it contacts while the paper loads, and what it stores on the reader's machine. Content counted here can load without ever appearing on screen.

| Platform | Third-party | Ads/tracking networks | Cookies |
|---|---|---|---|
| arXiv live | 2 | 0 | 1 |
| arXiv Phase 1 mockup | 2 | 0 | 0 |
| APS, Physical Review Letters | 16 | 7 | 8 |
| ScienceDirect, Annals of Physics | 17 | 6 | 10 |
| ScienceDirect, Physics Letters B | 15 | 4 | 10 |
| IOP Science | 17 | 4 | 22 |
| Springer Nature, Algorithmica | 24 | 10 | 14 |
| Springer Nature, Nature Communications | 27 | 13 | 18 |
| NIH, PubMed Central | 4 | 3 | 8 |
| PLOS ONE | 22 | 8 | 8 |
| Wiley, Advanced Materials | 38 | 9 | 20 |
| Wiley, Advanced Science | 38 | 9 | 20 |
| ACM DL | 11 | 4 | 7 |
| IEEE Xplore | 15 | 3 | 28 |
| Taylor & Francis, Journal of Psychology | 31 | 9 | 25 |
| Taylor & Francis, Research in Mathematics | 21 | 6 | 25 |
| ResearchGate | 13 | 6 | 13 |
| Quantum (Overlay) | 4 | 0 | 0 |
| Open Journal of Astrophysics (Overlay) | 5 | 0 | 4 |

A third-party domain is not automatically a tracker. Both of arXiv's are code libraries served
from a CDN, and neither follows the reader anywhere. The middle column is the one that counts
services built to do that.

These are the numbers for a reader arriving with no history on the site, who then accepts the
cookie banner if one appears. Two things follow from that. Connected Papers does not appear in
arXiv's count, because it is only contacted once a reader turns on arXiv Labs. And the
publisher numbers would be far lower for someone who never accepts: Springer loads 6
third-party domains and 2 tracking networks before consent against the 24 and 10 recorded
here.

## Findings

**1. arXiv is one click behind on full text access.** Most open-access platforms measured (all except ACM and ResearchGate) serve the full paper on the landing page. arXiv's landing page (abs) sends the reader to a separate `/html/` page. The arXiv Phase 1 mockup serves the full text and metadata on the same page, with additional improvements to usability and accessibility.

**2. Copy-to-clipboard for citations is uncommon but not unique.** ACM, Wiley, and more have a 2-click process (open a modal, copy contents). Only the arXiv phase 1 mockup reduces it to 1-click by displaying the citation area on the main page instead of in a modal; Some have copy buttons in their modal, others generate a file for download or require manually selecting, including arXiv's current option on the abstract page. *Adding a copy button to arXiv's existing BibTeX modal is a small win, independent of the Phase 1 HTML papers work.*

**3. Distraction levels are split between commercial versus non-commercial platforms.** Only arXiv and the two overlay journals have zero advertising or tracking networks. The five non-commercial platforms load 2–5 third-party domains. Every commercial platform loads 11–38. Some are egregious: IEEE sets 28 cookies on an article body it will not show without a subscription. Springer runs 10 tracking networks on a page that costs USD 39.95 to read.

The presence of ads and unrelated content displaces useful content. Nature pushes its paper's title down 137px with a leaderboard ad, ResearchGate 122px, and Wiley and PLOS 90px each. Ads are not the only thing that displaces: PubMed Central carries no ad above its title and still starts the paper 614px down, and a cookie banner moves ACM's title 150px while it is on screen. arXiv's live site puts its title at 108px, the highest of any platform measured. *The mockup puts it lower because of the prominent "back to abstract" button, which can be retired if the merged abstract and full paper page becomes the default.* That button exists to ease user confusion caused by the existence of two pages.

Ads and tracking are not the same. APS and IOP carry no ad slots and place their titles
high, but still load seven and four tracking networks. Not selling ad space is not the same as
not measuring readers. arXiv does neither.

Being free from commercial incentive really shows. arXiv does best on this metric, followed by the overlay journals, and then other open access platforms like ACM. On commercial publishing platforms, the financial incentive is right in your face and actively degrades the reading experience.

**4. Access is the biggest separator.** Springer, IEEE and Taylor & Francis give a reader
with no subscription neither the HTML nor the PDF, at USD 39.95, gated, and USD 56. IEEE lists
the section titles above a body it will not show. Against no access at all, click counts don't matter.

**5. Overlay journals delegate the reading experience to arXiv.** Both overlay journals measured, Quantum and the Open
Journal of Astrophysics, link to us with "Read article at ArXiv". For these journals arXiv's article page *is* the reading experience they give their readers, so Phase 1 improves their product too.

**6. Accessibility is uneven.** The basics are covered on all sites (page language, basic landmarks), but there are many fails on other common features such as skip links, lack of structure, and missing alt text. arXiv's live abstract page has the sample's worst heading structure, with seven H1 elements where there should be one.

We will continue to struggle with challenges related to the uneven markup quality in the original TeX source, but we can improve in other ways as represented in the HTML phase 1 mockup. Round-trip citation navigation is a particular strong point compared to the other platforms tested. 

Consider how we can make the phase 1 mockup our default abstract and full text page.

End of report. Testing methodology follows.

---

## URLs checked
1. `https://arxiv.org/abs/2604.22725` (arXiv live)
1. `https://arxiv.github.io/design-system/mockups/public/html-phase1.html` (arXiv mockup)`https://www.tandfonline.com/doi/full/10.1080/00223980.2019.1590298` (Taylor and Francis, The Journal of Psychology, paywalled)
1. `https://www.tandfonline.com/doi/full/10.1080/27684830.2026.2711512` (Taylor and Francis, Research in Mathematics, open access)
1. `https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202004433` (Wiley, Advanced Science, open access)
1. `https://advanced.onlinelibrary.wiley.com/doi/epdf/10.1002/adma.74176` (Wiley, Advanced Materials, paywalled)
1. `https://dl.acm.org/doi/10.1145/3292500.3330701` (ACM)
1. `https://ieeexplore.ieee.org/document/9156697` (IEEE)
1. `https://link.springer.com/article/10.1007/s00453-021-00817-8` (Nature, Algorithmica, paywalled)
1. `https://www.nature.com/articles/s41467-026-76467-7` (Nature, Nature Communications, open access)
1. `https://www.nature.com/articles/s41586-021-03819-2` (Nature, open access)
1. `https://iopscience.iop.org/article/10.3847/1538-4357/ae8190` (IOP, The Astrophysical Journal)
1. `https://www.sciencedirect.com/science/article/pii/S037026931200857X?via%3Dihub` (Elsevier, Physics Letters B, open access)
1. `https://www.sciencedirect.com/science/article/abs/pii/S0003491626003180` (Elsevier, Annals of Physics, paywalled)
1. `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102` (APS, Physical Review Letters, open access)
1. `https://pmc.ncbi.nlm.nih.gov/articles/PMC8371605/` (NIH, PMC, also linked to Nature article)
1. `https://www.researchgate.net/publication/411823724_Implicit_Computation_of_Filtered_Prime_Implicants` (ResearchGate)
1. `journals.plos.org/plosone/article?id=10.1371/journal.pone.0173664` (PLOS One, open access)
1. `astro.theoj.org/article/166984-dust-and-grain-size-evolution-in-galaxy-simulations-what-matters-and-what-does-not` (Open Journal of Astrophysics, open access overlay)
1. `https://quantum-journal.org/papers/q-2026-08-13-2189/` (Quantum, overlay journal, open access)

## Methodology

Process:
- Start at the paper's own landing page, not a homepage or a Google Scholar result.
- Measure logged out, without institutional access to paywalled content.
- Measure at one fixed screen size, and wait several seconds for all content to load. The
current readings were taken at 1225×744, at 100% browser zoom.
- Accept the cookie banner where one appears, then measure. Most readers accept, and on many
platforms the trackers and ad slots do not load until they do. Measuring without accepting
makes publishers look far cleaner than a reader will ever see them.
- Start from a browser with no cookies for any platform in the sample, so that first-visit
state is the same everywhere.

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
- Ad slots: elements that are an advertising iframe, carry
an advertising class or id, or are literally labelled "Advertisement" — a deliberately strict
test. 
- Pushed down by: the summed height of ad slots positioned above the paper's title.

Privacy measurements:
- Third-party domains: every distinct host contacted whose registrable
domain differs from the page's own. 
- Ad and tracking networks: the subset matching known
advertising, analytics, session-recording and consent-management services, named individually
so the classification can be checked. 
- Cookies: how many the page has set in the reader's browser.

"Cited by" and "Related articles" are related-content links, not distractions.

The script that produces these numbers is [verification/probe-distraction.js](../probe-distraction.js).
Use it rather than writing a new one: the column only means anything when every row is
measured the same way, and four rules make the difference between a real reading and a
plausible one.

- **Measure the paper's title, not the first heading.** arXiv puts the subject category in a
heading above the title, and APS puts the journal name there. Taking the topmost heading
scores arXiv at 108px instead of 56px and APS at 298px instead of 89px.
- **Check the browser zoom.** Chrome stores zoom per site, so one platform can be measured at
80% and the next at 100% without anything looking wrong. Zoom reflows the page rather than
scaling it, so the numbers cannot be converted afterwards — they have to be re-measured.
- **Measure every platform in one sitting, from the same cookie state.** Repeat loads of the
same page return identical numbers — three consecutive loads matched exactly on every platform
in the sample. What moves the numbers is browser state, not chance, so a reading is only
comparable to another taken in the same state. An earlier round of these figures varied
wildly for exactly this reason, and re-measuring with medians turned out to fix nothing.
- **Consent state changes almost everything.** Before accepting Springer's cookie banner the
page loads 6 third-party domains and 2 tracking networks; after accepting, 24 and 10. Nature
goes from 7 and 2 to 27 and 13. A cookie banner also displaces content while it is on screen:
ACM's title sits at 437px with the banner up and 287px once it is dismissed.

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

**A redirect can hide a paywall.** Wiley's `/doi/full/` URL silently lands on `/doi/abs/`,
which looks like a successful load and prints no paywall wording — the wall only appears on
clicking through to the PDF or EPUB. Compare the final URL against the requested one, and
check whether the article body is actually present, rather than searching the page for words
like "purchase".

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
