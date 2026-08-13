# Distractions audit

**Run 2026-08-12**

This test measures how much of an article page is not the article: advertising and tracking
networks, cookies, ad slots, and how far down the page the paper's title is pushed to make
room for them.

## Results

Measured on arrival, logged out, at 1280×800. One article per platform.

| Platform | Type | Third-party domains | Ad / tracking networks | Cookies | Ad slots | Title at | Pushed down by |
|---|---|---|---|---|---|---|---|
| **arXiv Phase 1 mockup** | Preprint server | **3** | **0** | **0** | **0** | 223px | **0px** |
| **arXiv live** | Preprint server | **4** | **0** | 4 | **0** | — | **0px** |
| **Quantum** | Overlay journal | **4** | **0** | **0** | **0** | — | **0px** |
| ScienceDirect | Publisher | 15 | 3 | 9 | 0 | — | 0px |
| ResearchGate | Network | 15 | 6 | 20 | 0 | — | 0px |
| APS | Publisher | 26 | 10 | 10 | 0 | **89px** | 0px |
| Springer Link | Publisher | 31 | 15 | 17 | 0 | — | 0px |
| IEEE Xplore | Publisher | 34 | 7 | **41** | 0 | 272px | 0px |
| **Nature** | Publisher | 41 | **22** | 22 | 5 | 351px | **528px** |
| **Wiley** | Publisher | **51** | 16 | 24 | 4 | **441px** | 120px |

Ad and tracking networks, named so the classification can be checked:

| Platform | Networks |
|---|---|
| arXiv (live and mockup), Quantum | — |
| ScienceDirect | DoubleClick, New Relic, OneTrust |
| ResearchGate | **DoubleClick, Criteo, AppNexus**, Google Analytics, Google Tag Manager |
| Springer Link | **DoubleClick ×2, Facebook, Twitter Ads, Bing Ads**, Segment, Google Tag Manager |
| Nature, Wiley, IEEE, APS | Google Publisher Tag / DoubleClick plus analytics and consent platforms |

## Findings

**1. Zero is achievable, and two platforms achieve it.** arXiv and Quantum load no
advertising or tracking networks at all, and Quantum sets no cookies. Every commercial
platform loads between fifteen and fifty-one third-party domains.

**2. Nature pushes its paper's title 528px down the page to fit two advertisements.** Both
sit above the title, at the very top of the document. On a 800px-tall window that is
two-thirds of the first screen spent before the paper is named. The arXiv Phase 1 mockup
pushes it 0px.

**3. Wiley loads fifty-one third-party domains and four Google ad slots**, and its title
lands at 441px — five times deeper than APS's 89px on the same class of content.

**4. Ads and tracking are separable, and society publishers show it.** APS carries no ad
slots and puts its title at 89px, the highest of any platform measured — but still loads
ten tracking networks. Not selling ad space does not mean not measuring readers. IEEE sets
41 cookies with no ad slots at all.

**5. Springer sets fifteen tracking networks on a page the reader cannot read.** The article
is paywalled at USD 39.95; the advertising and analytics load is fully present before any
content is.

**6. arXiv's advantage here is structural, not disciplinary.** It costs no ongoing restraint
and no design review, because no commercial incentive pushes the other way. Quantum, also
non-commercial, lands in the same place independently. This is the clearest measured
support for the brand claim that arXiv has no attention to farm.

**7. Not everything fixed to the viewport is a distraction.** ScienceDirect's sticky panel
is the article outline — navigation for the paper being read — and is counted as content.

## Methodology

**Measure on arrival**, logged out, at 1280×800, before interacting with anything.

**Third-party domains:** every distinct host contacted whose registrable domain differs from
the page's own, from the browser's resource timing.

**Ad / tracking networks:** the subset matching known advertising, analytics,
session-recording and consent-management services. Named individually in the results so the
classification can be checked rather than trusted.

**Ad slots:** elements that are an advertising iframe, carry an advertising class or id, or
are literally labelled "Advertisement". A deliberately strict test — promotional panels that
are merely commercial in tone are not counted.

**Pushed down by:** the summed height of ad slots positioned above the paper's title. This
is the cost in pixels of putting advertising ahead of the article.

**"Cited by" and "Related articles" are related-content links, not distractions**
(Shamsi 2026-08-12). They serve the reader even when commercially motivated, and counting
them as clutter would make the headline number arguable.

### Additional methodology for automated agentic testing

Publisher sites refuse automated browsers — 403s, 429s, and CAPTCHA pages that return HTTP
200, so a status code is not a reliable signal of access. These readings were taken in a
human's ordinary Chrome, driven by an agent.

Google Scholar's `gs-casa` overlay is injected on top of publisher pages by the reader's own
Google session. It is not the platform's design and is excluded everywhere.

Classifying page furniture by class name and text is approximate. The strict ad-slot test
above is reliable; a looser earlier pass produced false positives (author lists inside a
container whose text mentioned "Purchase"), and was discarded.

### Pages used

Same articles as the [clicks-to-content audit](audit-clicks-to-content.md).

Not yet measured for distractions: PLOS ONE, PubMed Central, ACM Digital Library,
Taylor & Francis, IOP Science, Open Journal of Astrophysics.
