# arXiv Brand

The brand is the *why* behind the design system. Colors, type, and components are downstream of it. When a design decision is genuinely ambiguous, this document — not taste — should settle it.

---

## Brand statement

> **arXiv is the light side of the internet.** We were built in 1991 to break the hold commercial publishing had on science. It was too slow, too expensive, too much gatekeeping. We aim to be the opposite and offer the most useful website on the internet, best-in-class for speed, readability, accessibility, and efficiency. The rebellion succeeded, but we still play by its rules: always free, answerable only to researchers, zero ego, and no dark patterns. The light side, indeed.

### In brief

- **Positioning** — The light side of the internet.
- **Origin** — Broke the hold of commercial publishing.
- **Operating values** — Free, best-in-class, no dark patterns.
- **Quality bar** — The most useful website on the internet.
- **Personality** — No ego, but we push boundaries in service of science.
- **Who we serve** — Researchers. When a tradeoff pits the casual visitor against the researcher who uses arXiv every day, the researcher wins.

---

## Voice

**Honest, plainspoken, accessible, and slightly mischievous.**

- **Honest** — We say what's true, including the unflattering parts (open issues, known limitations, "this is a prototype"). No marketing gloss, no overclaiming.
- **Plainspoken** — Short words, direct sentences, no jargon-as-decoration. If a researcher would say it plainly at a whiteboard, we write it that way.
- **Accessible** — Literally (WCAG, screen readers, low bandwidth, JS off) and tonally. Nobody should feel they need a secret handshake to use arXiv.
- **Slightly mischievous** — A dry wit, a wink, the smileybones. Never cute for its own sake, never at the reader's expense — just enough to signal there are humans here who enjoy this.

The voice applies to *everything that has words*: UI copy, empty states, error messages, docs, alt text, even commit messages. When in doubt, read it aloud — if it sounds like a brochure or a legal notice, rewrite it.

---

## What this means for design

The brand is not decoration — it has already decided real constraints. Each principle below names the policy or pattern it drives, so the line from brand to pixel is traceable.

### 1. The interface gets out of the way
Zero ego means the design never competes with the science. Chrome recedes as the reader goes deeper ([PROPOSED-GUIDELINES G2](design-patterns/PROPOSED-GUIDELINES.md)); navigation stays permanently short and resists link-creep ([DESIGN-POLICIES, nav cap](DESIGN-POLICIES.md)). The most useful website is the one you stop noticing.

### 2. No metrics, no gamification, no dark patterns
"Answering only to researchers" is literal: arXiv shows **no view counts, download counts, or citation counts** on public pages, and does not rank or promote papers ([DESIGN-POLICIES, public pages](DESIGN-POLICIES.md)). We don't manufacture urgency, we don't farm attention, and we keep toasts/notifications near zero ([z-layer values note](DESIGN-POLICIES.md)). If a feature's job is to drive engagement rather than serve a research task, it doesn't belong.

### 3. Lighter than the establishment
The light-side metaphor is built into the palette: warm Repository Brown and light tints where commercial publishers go navy-and-corporate. Open Blue (public) and Access Lime (internal) are bright, not somber. The visual lightness *is* the positioning — see [color-mapping.md](design-patterns/color-mapping.md).

### 4. Readable by people and machines, equally
"Best-in-class for readability" includes machines: clean semantic HTML, real headings and landmarks, content present before JavaScript runs ([progressive enhancement policy](DESIGN-POLICIES.md)). Co-equal HTML and PDF formats serve the same goal. *(Open strategic question: whether to move from co-equal to HTML-first — see G2. A brand decision waiting on leadership, not a design-system one.)*

### 5. Accessibility is a brand value, not a checkbox
"The light side" and "open to all" mean WCAG 2.2 AA is a floor, not a target — spoken math, keyboard-reachable everything, forced-colors and reduced-motion support, JS-off usability. The accessibility rules in [DESIGN-POLICIES.md](DESIGN-POLICIES.md) are the brand made concrete.

### 6. Honest, plainspoken copy — with a wink
UI text is direct and never overclaims (the [feedback changelog](mockups/FEEDBACK-CHANGELOG.md) is a good model: "this is a prototype," "open for discussion"). The mischief lives in small, optional places — the smileybones, a dry empty state — never in anything load-bearing or anything a stressed researcher has to parse.

### 7. Built to last by a small team
arXiv is daily infrastructure maintained by a very small team. Designs must be **low-maintenance**: no patterns that require manual upkeep, no per-paper hand-tuning, citation formats generated from metadata ([DESIGN-POLICIES](DESIGN-POLICIES.md)). Durable and boring-where-it-counts beats clever-and-fragile. This too is "zero ego."

### 8. Speed and efficiency are different promises
For arXiv these are two distinct pillars, not synonyms. **Speed** is how fast a paper moves from submission to published and announced: a throughput commitment. **Efficiency** is how few clicks it takes a researcher to get what they came for, whether that's the DOI, the PDF, the source, or the right version. Publisher sites bury those behind many clicks; arXiv surfaces them. The design directive that follows: count the clicks to every core task (download, cite, find the DOI, switch version) and minimize them. The common cases belong on the surface, not in menus.
