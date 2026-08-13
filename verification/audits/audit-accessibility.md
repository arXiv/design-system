# Accessibility audit

**Run 2026-08-12**

This test measures the structural accessibility of article pages, and specifically how
disruptive it is to follow a citation or footnote and get back — the movement that costs
screen reader and keyboard users the most.

## Results

Measured logged out at 1280×800.

| Platform | Lang | `<h1>` | Heading skips | Images no alt | Links no name | `<main>` | Tabs to content | Skip link | Citation round trip |
|---|---|---|---|---|---|---|---|---|---|
| **arXiv Phase 1 mockup** | en | **1** | 1 | 0/8 | 1 | yes | 8 | yes | **popover — reader is not moved** |
| arXiv live | en | **7** | 1 | 0/7 | 1 | yes | 7 | yes | *not yet click-tested* |
| APS | en | **5** | 0 | 0/20 | 0 | yes | 20 | yes | *not yet click-tested* |
| ScienceDirect | en-US | 1 | 0 | 0/27 | 0 | yes | **6** | **no** | *not yet click-tested* |
| IOP Science | en | 1 | 0 | 0/61 | 0 | yes | 9 | **no** | *not yet click-tested* |
| Nature | en | 1 | 0 | **6/24** | 0 | yes | 14 | yes | *not yet click-tested* |
| PubMed Central | en | 1 | 1 | 4/40 | 0 | yes | 12 | yes | *not yet click-tested* |
| PLOS ONE | en | 2 | 0 | 0/35 | 3 | yes | 11 | yes | *not yet click-tested* |
| Wiley | en | 1 | 1 | 0/35 | **18** | yes | 9 | yes | **popover — reader is not moved** |
| ACM Digital Library | en | 1 | 1 | **13/25** | 11 | yes | 24 | yes | *not yet click-tested* |
| Springer Link | en | 1 | 0 | 2/18 | 0 | yes | 16 | yes | *not yet click-tested* |
| IEEE Xplore | en-US | 3 | 0 | 1/4 | 2 | yes | 21 | yes | *not yet click-tested* |
| Taylor & Francis | en | 1 | 1 | 0/8 | 1 | yes | 15 | yes | *not yet click-tested* |
| ResearchGate | en | 1 | 0 | 0/33 | **144** | yes | **1** | **no** | *not yet click-tested* |
| Quantum | en-GB | 2 | 1 | 0/16 | 0 | yes | 19 | yes | *not yet click-tested* |
| Open Journal of Astrophysics | en | 1 | 1 | 0/1 | 0 | yes | 26 | **no** | *not yet click-tested* |

Dashes mean the page has no article body to link into — an abstract-only landing page, a
gated page, or an overlay journal that sends the reader to arXiv.

## Findings

**1. RETRACTED — the citation round-trip finding was wrong.** An earlier version of this
file reported that following a citation strands the reader on nearly every platform,
including arXiv's own mockup. That was a measurement error, caught by Shamsi.

The test looked for a *return link* by matching visible text — an arrow, "back to". It never
clicked a citation. Platforms that solve the problem better, by showing the reference in a
popover so the reader is never moved at all, scored zero and were reported as failures.

Re-tested by clicking: the **arXiv Phase 1 mockup** opens a `cite-popover` with the full
reference and the scroll position does not change — there is nothing to return from.
**Wiley** does the same across 415 inline citations. Both were wrongly marked as failing.

The rest of the sample has not been click-tested yet and is marked as such. No conclusion
about citation navigation should be drawn from this audit until that is done.

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
- **No fix needed for citations in the Phase 1 mockup.** It already solves this better than
  a return link would: the reference appears in a popover and the reader is never displaced.

## Methodology

**Measure logged out** at 1280×800, on arrival, before interacting.

**Structure:** language attribute present; count of `<h1>` elements, which should be one;
heading levels skipped (h2 → h4); images lacking an `alt` attribute; links with no
accessible name from text, `aria-label`, or an image alt.

**Navigation cost:** presence of a `<main>` landmark; the number of focusable elements
before it, which is how many Tab presses a keyboard user spends to reach the paper; whether
the first focusable element is a skip link.

**Reference and footnote round trip:** *click an inline citation and observe what happens.*
Record whether a popover appears, whether the scroll position moves, and — only if the
reader is actually displaced — whether a return affordance exists. Counting return links
without clicking produces false failures: a popover needs no return link, because it never
takes the reader anywhere.

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
