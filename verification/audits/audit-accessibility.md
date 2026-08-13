# Accessibility audit

**Started 2026-08-12**

This test measures the structural accessibility of article pages, and specifically how
disruptive it is to follow a citation or footnote and get back — the movement that costs
screen reader and keyboard users the most.

## Results

Measured logged out at 1280×800.

| Platform | Lang | `<h1>` count | Heading skips | Images without alt | Links with no name | `<main>` | Tab stops before content | Skip link | Links into references | Links back out |
|---|---|---|---|---|---|---|---|---|---|---|
| **arXiv Phase 1 mockup** | en | **1** | 1 | 0 / 8 | 1 | yes | 8 | yes | **393** | **1** |
| arXiv live | en | **7** | 1 | 0 / 7 | 1 | yes | 7 | yes | 0 *(abstract page)* | — |
| PLOS ONE | en | 2 | 0 | 0 / 35 | 3 | yes | 11 | yes | **55** | **0** |

## Findings so far

**1. Following a citation is a one-way trip almost everywhere — including our mockup.** The
Phase 1 mockup has 393 in-page links into references and sections, and one link back. PLOS
ONE has 55 in and none back. A sighted mouse user presses Back or scrolls; a screen reader
user who follows a citation has landed somewhere with no marked route to where they were
reading. This is the disruption the audit was built to find, and arXiv's own design has it.

**2. arXiv live has seven `<h1>` elements.** A page should have one. For a screen reader
user navigating by heading — the normal way to move through a long document — seven top-level
headings means the page announces seven competing "titles" and the document outline is
meaningless. The Phase 1 mockup fixes this: it has exactly one.

**3. The basics are in decent shape everywhere measured.** Every page declares a language,
provides a `<main>` landmark, offers a skip link as the first focusable element, and gives
alt attributes to all images. None of the three has a systematic failure at that level.

## Methodology

**Measure logged out** at 1280×800, on arrival, before interacting.

**Structure:** language attribute present; count of `<h1>` elements (should be one); heading
levels skipped (h2 → h4); images lacking an `alt` attribute; links with no accessible name
from text, `aria-label`, or an image alt.

**Navigation cost:** presence of a `<main>` landmark; number of focusable elements before it,
which is how many Tab presses a keyboard user spends to reach the paper; whether the first
focusable element is a skip link.

**Reference and footnote round trip:** count of in-page links pointing into references,
citations, footnotes or sections, against the count of links that return — a back-reference
arrow, "back to text", or similar. A large gap means following a citation strands the reader.

### What this test cannot tell you

This measures structure, not experience. It cannot hear a screen reader, so it cannot judge
whether announcements make sense in sequence, whether a reading order is confusing, or how
disorienting a jump feels. Those need a human running VoiceOver, NVDA or JAWS. What is
measured here is the part a machine can check reliably, and it is the part that must be
right before a human test is worth running.

### Additional methodology for automated agentic testing

Reference links are identified by an in-page `href` matching reference, bibliography,
citation, footnote, note or section patterns. Return links are identified by their visible
text — an arrow, "back to", "return to". A platform using an unlabelled icon for its return
link would be undercounted; check by hand before quoting a zero.

### Pages used

Same articles as the [clicks-to-content audit](audit-clicks-to-content.md).

Remaining to measure: APS, ScienceDirect, IOP, Nature, PubMed Central, Wiley, ACM,
Springer, IEEE, Taylor & Francis, ResearchGate, Quantum, Open Journal of Astrophysics.
