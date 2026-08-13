# Accessibility audit

**Run 2026-08-12**

This test measures the structural accessibility of article pages, and specifically how
disruptive it is to follow a citation or footnote and get back — the movement that costs
screen reader and keyboard users the most.

## Results

Measured logged out at 1280×800.

| Platform | Lang | `<h1>` | Heading skips | Images no alt | Links no name | `<main>` | Tabs to content | Skip link | Refs in | Ways back |
|---|---|---|---|---|---|---|---|---|---|---|
| **arXiv Phase 1 mockup** | en | **1** | 1 | 0/8 | 1 | yes | 8 | yes | **393** | **1** |
| arXiv live | en | **7** | 1 | 0/7 | 1 | yes | 7 | yes | — | — |
| APS | en | **5** | 0 | 0/20 | 0 | yes | 20 | yes | 18 | **0** |
| ScienceDirect | en-US | 1 | 0 | 0/27 | 0 | yes | **6** | **no** | 50 | **0** |
| IOP Science | en | 1 | 0 | 0/61 | 0 | yes | 9 | **no** | **353** | 1 |
| Nature | en | 1 | 0 | **6/24** | 0 | yes | 14 | yes | 24 | **0** |
| PubMed Central | en | 1 | 1 | 4/40 | 0 | yes | 12 | yes | 6 | **0** |
| PLOS ONE | en | 2 | 0 | 0/35 | 3 | yes | 11 | yes | 55 | **0** |
| Wiley | en | 1 | 1 | 0/35 | **18** | yes | 9 | yes | **454** | **0** |
| ACM Digital Library | en | 1 | 1 | **13/25** | 11 | yes | 24 | yes | 3 | **0** |
| Springer Link | en | 1 | 0 | 2/18 | 0 | yes | 16 | yes | 4 | **0** |
| IEEE Xplore | en-US | 3 | 0 | 1/4 | 2 | yes | 21 | yes | — | — |
| Taylor & Francis | en | 1 | 1 | 0/8 | 1 | yes | 15 | yes | — | 1 |
| ResearchGate | en | 1 | 0 | 0/33 | **144** | yes | **1** | **no** | — | — |
| Quantum | en-GB | 2 | 1 | 0/16 | 0 | yes | 19 | yes | — | — |
| Open Journal of Astrophysics | en | 1 | 1 | 0/1 | 0 | yes | 26 | **no** | — | — |

Dashes mean the page has no article body to link into — an abstract-only landing page, a
gated page, or an overlay journal that sends the reader to arXiv.

## Findings

**1. Following a citation is a one-way trip on every platform measured.** Of the eight
pages with reference links, **six offer no marked route back at all**, and the two that do
offer exactly one link between them. Wiley has 454 links into references and zero back. IOP
has 353 and one. The Phase 1 mockup has 393 and one.

A sighted mouse user presses Back or scrolls. A screen reader or keyboard user who follows
a citation has landed in a reference list with no announced way to return to the sentence
they were reading. This is the single most consistent accessibility failure in the sample,
it is industry-wide, and **arXiv's own mockup shares it**.

**2. arXiv live has seven `<h1>` elements.** A page should have one. For someone navigating
by heading — the normal way through a long document — seven top-level headings means seven
competing titles and an outline that says nothing. APS has five, IEEE three. The Phase 1
mockup has exactly one, so this is already fixed in the redesign.

**3. ResearchGate has 144 links with no accessible name.** A screen reader announces these
as "link" with nothing else. It also has no skip link and only one focusable element before
its main content, so the page offers almost no structural navigation at all.

**4. ACM leaves 13 of 25 images without an alt attribute** — over half. Nature leaves 6 of
24. On a research paper, unlabelled images are usually figures, which is where the evidence
is.

**5. Four platforms have no skip link:** ScienceDirect, IOP, ResearchGate and the Open
Journal of Astrophysics. Both arXiv pages have one.

**6. The basics are otherwise sound.** Every platform declares a page language and provides
a `<main>` landmark. Nobody fails at that level.

## Findings for arXiv

- **Fix on the live site:** seven `<h1>` elements on the abstract page.
- **Fix in the Phase 1 mockup:** add a return link to every reference and footnote. The
  mockup already carries the sticky reader bar and a single correct `<h1>`; the return path
  is the remaining gap, and closing it would make arXiv the only platform in this sample
  where following a citation is a round trip rather than a one-way jump.

## Methodology

**Measure logged out** at 1280×800, on arrival, before interacting.

**Structure:** language attribute present; count of `<h1>` elements, which should be one;
heading levels skipped (h2 → h4); images lacking an `alt` attribute; links with no
accessible name from text, `aria-label`, or an image alt.

**Navigation cost:** presence of a `<main>` landmark; the number of focusable elements
before it, which is how many Tab presses a keyboard user spends to reach the paper; whether
the first focusable element is a skip link.

**Reference and footnote round trip:** in-page links pointing into references, citations,
footnotes or numbered sections, counted against links that return — a back-reference arrow,
"back to text", or similar. A large gap means following a citation strands the reader.

### What this test cannot tell you

This measures structure, not experience. It cannot hear a screen reader, so it cannot judge
whether announcements make sense in sequence, whether reading order is confusing, or how
disorienting a jump feels in practice. Those need a person running VoiceOver, NVDA or JAWS.
What is measured here is the part a machine checks reliably, and it is the part that should
be right before a human test is worth anyone's time.

### Additional methodology for automated agentic testing

Reference links are identified by an in-page `href` matching reference, bibliography,
citation, footnote, note or numbered-section patterns. Return links are identified by their
visible text — an arrow, "back to", "return to". A platform using an unlabelled icon for its
return link would be undercounted, so any zero is worth a spot-check by hand before it is
quoted.

### Pages used

Same articles as the [clicks-to-content audit](audit-clicks-to-content.md).
