# Accessibility audit

**Run 2026-08-12**

This test measures the structural accessibility of article pages, and specifically how
disruptive it is to follow a citation or footnote and get back — the movement that costs
screen reader and keyboard users the most.

## Results

Measured logged out at 1280×800.

| Platform | Lang | `<h1>` | Heading skips | Images no alt | Links no name (visible) | `<main>` | Tabs to content | Skip link | Citation round trip |
|---|---|---|---|---|---|---|---|---|---|
| **arXiv Phase 1 mockup** | en | **1** | 1 | 0/8 | 1 | yes | 8 | yes | **popover — reader is not moved** |
| arXiv live | en | **7** | 1 | 0/7 | 1 | yes | 7 | yes | *needs human test* |
| APS | en | **5** | 0 | 0/20 |  *recount pending* | yes | 20 | yes | *needs human test* |
| ScienceDirect | en-US | 1 | 0 | 0/27 |  *recount pending* | yes | **6** | **no** | *needs human test* |
| IOP Science | en | 1 | 0 | 0/61 |  *recount pending* | yes | 9 | **no** | *needs human test* |
| Nature | en | 1 | 0 | **6/24** |  *recount pending* | yes | 14 | yes | *needs human test* |
| PubMed Central | en | 1 | 1 | 4/40 |  *recount pending* | yes | 12 | yes | *needs human test* |
| PLOS ONE | en | 2 | 0 | 0/35 |  *recount pending* | yes | 11 | yes | *needs human test* |
| Wiley | en | 1 | 1 | 0/35 | **12** | yes | 9 | yes | **popover — reader is not moved** |
| ACM Digital Library | en | 1 | 1 | **13/25** | 0 | yes | 24 | yes | *needs human test* |
| Springer Link | en | 1 | 0 | 2/18 |  *recount pending* | yes | 16 | yes | *needs human test* |
| IEEE Xplore | en-US | 3 | 0 | 1/4 |  *recount pending* | yes | 21 | yes | *needs human test* |
| Taylor & Francis | en | 1 | 1 | 0/8 |  *recount pending* | yes | 15 | yes | *needs human test* |
| ResearchGate | en | 1 | 0 | 0/33 | **0** | yes | **1** | **no** | *needs human test* |
| Quantum | en-GB | 2 | 1 | 0/16 |  *recount pending* | yes | 19 | yes | *needs human test* |
| Open Journal of Astrophysics | en | 1 | 1 | 0/1 |  *recount pending* | yes | 26 | **no** | *needs human test* |

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

**3. RETRACTED — the unnamed-links count was inflated.** An earlier version reported
ResearchGate with 144 links lacking an accessible name. Recounted correctly, ResearchGate
has **zero visible links** without a name, and ACM has zero rather than eleven. The original
check counted links hidden from view, and ignored `aria-labelledby` and `title`, both of
which are valid ways to name a link.

Wiley does have **12** visible unnamed links and arXiv live has 1 — those hold. The
remaining platforms are marked *recount pending*.

What still stands about ResearchGate: it has no skip link, and only one focusable element
before its main content.

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
heading levels skipped (h2 → h4); images lacking an `alt` attribute; **visible** links with
no accessible name, where a name may come from text, `aria-label`, `aria-labelledby`,
`title`, an image alt, or an SVG title. Count visible links only — a link hidden from view
is not announced either, and including hidden links inflates the number several-fold.

**Navigation cost:** presence of a `<main>` landmark; the number of focusable elements
before it, which is how many Tab presses a keyboard user spends to reach the paper; whether
the first focusable element is a skip link.

**Reference and footnote round trip: this one needs a human.** Two automated approaches
were tried and both failed. Counting return links by text produced false failures, because a
popover needs no return link. Clicking citations programmatically is also unreliable:
synthetic mouse events do not always trigger the real handlers, hover-triggered panels do not
fire at all, and "nothing visibly happened" cannot be distinguished from "the handler did not
run". Two platforms gave a clear enough answer to record — the arXiv mockup and Wiley both
show a popover and do not move the reader. The rest need a person clicking a citation and
saying what they see.

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
