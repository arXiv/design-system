# Distractions audit

**Run 2026-08-12**

This test measures how much of an article page is not the article: third-party tracking,
advertising networks, cookies, and overlays that cover the content.

## Results

Measured on arrival, logged out, at 1280×800. One article per platform.

| Platform | Type | Third-party domains | Ad / tracking networks | Cookies set | Overlays covering content |
|---|---|---|---|---|---|
| **arXiv live** | Preprint server | **4** | **0** | 4 | **none** |
| **Quantum** | Overlay journal | **4** | **0** | **0** | none |
| ScienceDirect | Publisher | 15 | 3 | 9 | none *(its sticky outline is content)* |
| ResearchGate | Network | 15 | 6 | 20 | none at rest |
| Springer Link | Publisher | **31** | **15** | 17 | none |

Ad and tracking networks found, by platform:

| Platform | Networks |
|---|---|
| arXiv live | — |
| Quantum | — |
| ScienceDirect | DoubleClick, New Relic, OneTrust |
| ResearchGate | **DoubleClick, Criteo, AppNexus**, Google Analytics, Google Tag Manager |
| Springer Link | **DoubleClick ×2, Facebook, Twitter Ads, Bing Ads**, Segment, Google Tag Manager |

## Findings

**1. The split is commercial versus non-commercial, not old versus new.** arXiv and Quantum
each load four third-party domains and no tracking networks at all. Every commercial
platform measured loads between fifteen and thirty-one, with three to fifteen tracking
networks. There is no middle ground in this sample.

**2. Springer sets fifteen tracking networks on a page the reader cannot read.** The same
article is paywalled at USD 39.95. The advertising and analytics load is fully present
before any content is.

**3. ResearchGate runs real-time advertising auctions.** Criteo and AppNexus are retargeting
and ad-exchange services — this is not analytics for site improvement, it is inventory being
sold. Twenty cookies are set on arrival.

**4. arXiv's advantage here is structural and permanent.** It requires no ongoing
restraint, no design review, no policy enforcement: there is no commercial incentive
pushing in the other direction. Quantum, also non-commercial, lands in exactly the same
place. This is the clearest measured evidence for the brand claim that arXiv has no
attention to farm.

**5. Not everything sticky is a distraction.** ScienceDirect's fixed panel is the article
outline — navigation for the paper being read. Counted as content, not clutter.

## Methodology

**Measure on arrival**, logged out, before interacting with anything. Overlays that appear
only after scrolling or a delay are recorded separately if they appear.

**Third-party domains:** every distinct host contacted whose registrable domain differs
from the page's own, taken from the browser's resource timing.

**Ad / tracking networks:** the subset of those domains matching known advertising,
analytics, session-recording and consent-management services. Named individually in the
results, so the classification can be checked rather than trusted.

**Cookies:** count set and readable at arrival.

**Overlays:** fixed or sticky elements at least 80×40px, visible, intersecting the
viewport, measured as percentage of the viewport covered. Judgement applies — an element
holding navigation for the paper being read is content, not a distraction.

**"Cited by" and "Related articles" are related-content links, not distractions**
(Shamsi 2026-08-12). They are a service to the reader even when commercially motivated, and
counting them as clutter would make the headline number arguable.

### Additional methodology for automated agentic testing

Publisher sites refuse automated browsers — 403s, 429s and CAPTCHA pages that return HTTP
200, so a status code is not a reliable signal of access. These readings were taken in a
human's ordinary signed-in Chrome, driven by an agent, which is what made them possible.

Google Scholar's `gs-casa` overlay is injected on top of publisher pages by the reader's
Google session. It is not the platform's own design and is excluded everywhere.

### Pages used

| Platform | URL |
|---|---|
| arXiv live | `arxiv.org/abs/2301.08727` |
| Quantum | `quantum-journal.org/papers/q-2026-07-29-2178/` |
| ScienceDirect | `sciencedirect.com/science/article/pii/S037026931200857X` |
| ResearchGate | `researchgate.net/publication/411823724_Implicit_Computation_of_Filtered_Prime_Implicants` |
| Springer Link | `link.springer.com/article/10.1007/s00453-021-00817-8` |
