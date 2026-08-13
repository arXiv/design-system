# Platform testing — consolidated report

**2026-08-12. Sixteen platforms, three tests.**

Everything we agreed to measure, with what each result is worth. Detail lives in
[clicks-to-content](audit-clicks-to-content.md), [distractions](audit-distractions.md) and
[accessibility](audit-accessibility.md).

## Confidence

Read this first. Two findings were retracted during this work after Shamsi caught them, and
the difference between the reliable and unreliable measures is *how* they were obtained.

| Confidence | Measures | Why |
|---|---|---|
| **Solid** | Third-party domains, tracking networks, cookies, ad slots, title position, push-down pixels, page weight, load time | Read from the browser — network requests and element geometry. Nature's 528px push was re-measured independently and matched exactly. |
| **Solid** | `<h1>` counts, heading skips, missing alt, `<main>`, skip links, tab stops | Counts of attributes that exist in the DOM. |
| **Solid where exercised** | Clicks to PDF, full text, citation — where the control was actually clicked | Every cell not marked otherwise was clicked and watched. |
| **Corrected** | Visible links with no accessible name | First count included hidden links and ignored `aria-labelledby` / `title`. Four platforms recounted; the rest marked *recount pending*. |
| **Not measurable by an agent** | Citation round trip | See below. |

## The headline results

**1. arXiv is one click behind on the most common task.** Every open-access publisher
measured except ACM serves the full paper on the landing page. arXiv alone sends the reader
to a separate `/html/` page. The Phase 1 mockup closes this, and is the only page measured
where the full text costs nothing *and* the PDF stays reachable while reading.

**2. The distraction split is commercial versus non-commercial, and it is absolute.** The
five non-commercial platforms load 3–4 third-party domains. Every commercial platform loads
15–46. Nothing sits in between. Four carry zero advertising or tracking networks: arXiv
twice, Quantum, and the Open Journal of Astrophysics.

**3. ACM pushes its paper's title 544px down the page, Nature 528px** — roughly two-thirds
of the first screen on an 800px window, spent before the paper is named. arXiv live puts its
title at 56px, the highest of anything measured. Both arXiv pages push it 0px.

**4. IEEE loads 17 ad slots and sets 41 cookies** on an article body it will not show
without a subscription. Springer runs 15 tracking networks on a page that costs USD 39.95 to
read.

**5. Ads and tracking are separable.** APS and IOP carry no ad slots and place their titles
high, but still load ten and eight tracking networks. Not selling ad space is not the same
as not measuring readers. arXiv does neither.

**6. Overlay journals delegate the reading experience to arXiv.** Neither Quantum nor the
Open Journal of Astrophysics hosts the full text. OJAp links out with "Read article at
ArXiv". For these journals arXiv's article page *is* their reading experience, so Phase 1
improves their product too.

**7. arXiv's distraction advantage is structural, not disciplinary.** It costs no ongoing
restraint, because no commercial incentive pushes the other way. Three other non-commercial
platforms land in the same place independently.

## What arXiv should fix

| Where | Fix | Evidence |
|---|---|---|
| **Live site** | Seven `<h1>` elements on the abstract page — heading navigation is meaningless for screen reader users | Direct count; mockup already has exactly one |
| **Live site** | No copy button on the BibTeX modal | ACM and Wiley both have one; the mockup has one |
| **Live site** | Full text is a separate page | Every open-access publisher measured serves it inline |

Nothing outstanding on the Phase 1 mockup. Its citation popover, single `<h1>`, sticky PDF
control, zero trackers and zero push-down are all confirmed.

## What could not be measured, and why

**The citation round trip — whether following a reference strands the reader — needs a
human.** This was the test Shamsi most wanted, and two automated approaches both failed.

Counting return links by their text produced false failures: a popover needs no return link
because it never moves the reader, so the platforms handling this *best* scored worst. That
error was published and retracted.

Clicking citations programmatically is also unreliable. Synthetic mouse events do not always
trigger real handlers, hover-triggered panels never fire, and "nothing visibly happened"
cannot be told apart from "the handler did not run".

Two platforms gave a clear enough answer to keep: the **arXiv Phase 1 mockup** and **Wiley**
both show the reference in a popover and do not move the reader. The other fourteen need a
person clicking a citation and reporting what they see. It is perhaps twenty minutes of work
and it is the highest-value remaining item in this whole exercise.

**Also outstanding:** ACM's "PDF/eReader" control was never clicked, so "full text not
available" for ACM is unconfirmed; IOP's citation control was described from its link text
rather than exercised; and eleven platforms need the unnamed-links recount.

## What this exercise taught about method

Recorded because it will happen again to whoever runs the next audit.

**Exercise every control. Never infer behaviour from markup.** Both retracted findings came
from building a detector and running it across sixteen platforms without once validating it
against a page whose behaviour was already known.

**Coverage is not evidence.** Getting to "all sixteen measured" was the wrong goal when the
instrument was wrong. A smaller set of verified results is worth more.

**HTTP 200 does not mean access.** Springer, IOP, Frontiers and IEEE all serve challenge or
CAPTCHA pages with a 200 status.

**Let the page settle.** Probed immediately, APS reports 3 third-party domains; after three
seconds, 26.

**Count what is visible.** Hidden links, hidden elements and rail placement all distort
counts that look objective.
