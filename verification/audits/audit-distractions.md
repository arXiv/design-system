# Distractions audit

**Run 2026-08-12**

This test measures how much of an article page is not the article: advertising and tracking
networks, cookies, ad slots, and how far down the page the paper's title is pushed to make
room for them.

## Results

Sorted by third-party domains contacted. Measured on arrival, logged out, at 1280×800,
three seconds after load.

| Platform | Type | Third-party domains | Ad / tracking networks | Cookies | Ad slots | Title at | Pushed down by |
|---|---|---|---|---|---|---|---|
| **arXiv Phase 1 mockup** | Preprint server | **3** | **0** | **0** | **0** | 244px | **0px** |
| PubMed Central | Repository | **3** | 2 | 8 | 1 | 614px | 75px |
| **arXiv live** | Preprint server | **4** | **0** | 4 | **0** | **56px** | **0px** |
| **Quantum** | Overlay journal | **4** | **0** | **0** | **0** | 0px | **0px** |
| **Open Journal of Astrophysics** | Overlay journal | **4** | **0** | 4 | 1 | 436px | 55px |
| ScienceDirect | Publisher | 15 | 3 | 9 | 0 | 112px | 0px |
| ACM Digital Library | Publisher | 16 | 5 | 7 | 8 | 437px | **544px** |
| ResearchGate | Network | 17 | 7 | 20 | 4 | 264px | 213px |
| IEEE Xplore | Publisher | 19 | 4 | **41** | **17** | 272px | 0px |
| IOP Science | Publisher | 23 | 8 | 25 | 0 | 174px | 0px |
| PLOS ONE | Publisher | 25 | 7 | 8 | 4 | 385px | 180px |
| APS | Publisher | 26 | 10 | 10 | 0 | 89px | 0px |
| Springer Link | Publisher | 31 | 15 | 17 | 3 | 209px | 0px |
| Nature | Publisher | 36 | 19 | 22 | 8 | 351px | **528px** |
| Wiley | Publisher | 42 | 15 | 23 | 4 | **441px** | 120px |
| Taylor & Francis | Publisher | **46** | 16 | **30** | 1 | 352px | 80px |

Ad and tracking networks named, so the classification can be checked rather than trusted:

| Platform | Networks |
|---|---|
| arXiv (live and mockup), Quantum, Open Journal of Astrophysics | **none** |
| PubMed Central | Google Analytics, Google Tag Manager |
| ScienceDirect | DoubleClick, New Relic, OneTrust |
| ResearchGate | **DoubleClick, Criteo, AppNexus**, Google Analytics, Google Tag Manager |
| Springer Link | **DoubleClick ×2, Facebook, Twitter Ads, Bing Ads**, Segment, Google Tag Manager |
| Nature, Wiley, Taylor & Francis, ACM, IEEE, IOP, APS, PLOS | Google Publisher Tag / DoubleClick plus analytics and consent platforms |

## Findings

**1. The split is commercial versus non-commercial, and it is absolute.** The five
non-commercial platforms — arXiv live, the Phase 1 mockup, Quantum, the Open Journal of
Astrophysics and PubMed Central — load three or four third-party domains. Every commercial
platform loads between fifteen and forty-six. Nothing sits in between.

**2. Four platforms carry zero advertising or tracking networks: arXiv twice, Quantum, and
the Open Journal of Astrophysics.** All four are non-commercial. Quantum sets no cookies at
all.

**3. ACM pushes its paper's title 544px down the page, Nature 528px.** On an 800px-tall
window that is roughly two-thirds of the first screen spent before the paper is named. The
arXiv Phase 1 mockup pushes it 0px, and arXiv live puts its title at 56px — the highest of
any platform measured.

**4. IEEE loads seventeen ad slots and sets forty-one cookies** on an article whose body it
will not show without a subscription.

**5. Ads and tracking are separable, and society publishers prove it.** APS and IOP carry
no ad slots at all and place their titles high — 89px and 174px — but still load ten and
eight tracking networks. Not selling ad space is not the same as not measuring readers.
arXiv does neither.

**6. arXiv's advantage here is structural, not disciplinary.** It costs no ongoing
restraint and no design review, because no commercial incentive pushes the other way. Three
other non-commercial platforms land in the same place independently. This is the clearest
measured support for the brand claim that arXiv has no attention to farm.

**7. Not everything fixed to the viewport is a distraction.** ScienceDirect's sticky panel
is the article outline — navigation for the paper being read — and is counted as content.

## Methodology

**Measure on arrival**, logged out, at 1280×800, three seconds after load and before
interacting with anything. The delay matters: probed immediately, APS reports 3 third-party
domains; after three seconds it reports 26. Any reading taken without a settling delay is
wrong.

**Third-party domains:** every distinct host contacted whose registrable domain differs from
the page's own, from the browser's resource timing.

**Ad / tracking networks:** the subset matching known advertising, analytics,
session-recording and consent-management services, named individually in the results.

**Ad slots:** elements that are an advertising iframe, carry an advertising class or id, or
are literally labelled "Advertisement". A deliberately strict test — panels that are merely
commercial in tone are not counted.

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
above is reliable; a looser earlier pass produced false positives — author lists inside a
container whose text mentioned "Purchase" — and was discarded.

### Pages used

Same articles as the [clicks-to-content audit](audit-clicks-to-content.md).
