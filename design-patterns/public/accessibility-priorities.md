# Accessibility Priorities — Public Pages

Decisions for accessibility on the public abstract page and HTML paper reader. Companion to `../../DESIGN-POLICIES.md`. The "why" lines name supporting research voices; the underlying research syntheses live in the mockups working folder (`~/Desktop/arxiv-mockups/arxiv-public/references/`). Open research questions and recruit-before-design flags live there too — this document is decisions only.

## Mission

arXiv builds accessibility into the product by default. Users do not need an account, a preference center, or a setting toggle to get an accessible experience. Decisions about reading-mode, motion, font size, theme, and chrome density are made here — not punted to user preferences. The exceptions are OS/browser-level accessibility signals (`prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast`, `forced-colors`), which we honor as defaults coming from the user's existing system.

## Headline commitment

HTML + MathML + alt text is arXiv's accessible-by-default substrate. PDF remains available for the legacy corpus and for users who prefer it, but is not what we optimize new accessibility work against. Validated unanimously across screen-reader, magnification, braille, and dyslexia-track research voices.

## Priorities

### Information architecture

**Semantic HTML structure on the abstract page.** Heading hierarchy starts at `<h1>` (paper title) and descends logically. No heading levels used for styling. Landmarks (`<main>`, `<nav>`, sections) labeled meaningfully. DOM reading order matches visual prominence on desktop and mobile.
*Status: needs verification.* *Why: Dan Miner (2023-02-28) reported the current page returns h4 as the first heading; Coornaert noted arXiv search results have "almost no headings." WCAG 1.3.1.*

**arXiv ID and DOI announce correctly to screen readers.** Wrap inline arXiv identifiers and DOIs with `aria-label` so they announce as "archive paper, I D 2 6 0 4 dot 2 2 7 2 5, primary category gr-qc" — not as a Roman numeral or run-together gibberish. Follow crossref's 2022 DOI display recommendation.
*Status: validated. Why: Dan Miner (2023-02-28) — "the way your name is read is baffling, it reads it as a roman numeral most times but not always"; Bill Kasdorf (2022-11-02).*

**The word "arXiv" announces as "archive" site-wide.** Ginsparg picked the spelling because the X is Greek chi and the wordmark reads "archive" visually — that intention is invisible to TTS, so screen readers produce "ar-zhiv" / "ark-iv" / "arks-fourteen" (Roman numeral parsing of XIV) / similar. The canonical fix is a dual-span pattern:

```html
<span class="arxiv-word"><span aria-hidden="true">arXiv</span><span class="is-sr-only">archive</span></span>
```

Visible content is hidden from AT; the spoken substitute "archive" is shown only to AT. Works reliably across NVDA, JAWS, VoiceOver, TalkBack. Prefer this over `aria-label` on a wrapping `<span>` (which has inconsistent AT support on non-interactive inline elements).

Where to apply:
- Header logo: `<img alt="archive">` and `<a aria-label="archive home">` (replace "arXiv home" / `alt="arXiv"`).
- Page chrome containing "arXiv" as body text ("What are arXiv Labs?", "arXiv identifier", "arXiv preprint" toggle labels).
- Identifier patterns ("arXiv:2604.22725 [gr-qc]") get a full announcement label, not just the dual-span: `aria-label="archive paper, I D 2 6 0 4 dot 2 2 7 2 5, primary category gr-qc"`.

Where NOT to apply:
- **Copy-out content** (BibTeX, formatted citation text). The sr-only pattern is included in some browsers' selection copy; readers selecting the BibTeX would copy "archivearXiv2604.22725" — broken. Leave citation text strings alone.
- **Plain identifiers in metadata that are already inside `aria-label` wrappers** — don't double-wrap.

Operationalize as a template helper (Jinja/PHP/Smarty macro) emitting the dual-span on every "arXiv" instance in site-controlled chrome. For user-uploaded content that mentions arXiv (paper titles, comments), a small once-on-DOMContentLoaded script can walk text nodes and apply the same wrapping.

*Status: validated; rollout in progress. Why: Dan Miner (2023-02-28) "the way your name is read is baffling, I've gone there several times over the years and it's gibberish." Same source as the arXiv ID announcement.*

**Primary download/HTML/source buttons carry the paper title in their accessible name.** Use `aria-describedby` pointing to the title element on the primary action; buttons further from the title use `aria-label` with the title included.
*Status: validated. Why: Sam Hartman (2022-08-02), Robin Williams (2022-09-14).*

**Filenames include paper title and file extension.** `Author_Title_2401.12345.tar.gz` not `2401.12345`. Applies to PDF, HTML, and source-bundle downloads.
*Status: validated. Why: Ewin Tang (UXDH), Robin Williams (2022-09-14), repeated in CSV.*

**Source download surfaced on the abstract page**, not buried under "formats."
*Status: validated. Why: Michel Coornaert (2022-11-14), TV Raman (2022-08-05).*

**Author-link disambiguation.** Clicking an author's name finds *that* author's papers, not a surname-initial collision. Critical for Chinese, Korean, multi-part Latin names, and any common surname. (Depends on author identity work upstream of this design.)
*Status: validated. Why: Parampreet Singh, Cagri Sert, Manuel Arca Sedda, Elena Dalla Bontà — multiple voices.*

### Math accessibility

**MathML 4 (with `intent` semantics) is the primary math substrate; LaTeX source preserved alongside.** Ship MathML for AT consumption, MathJax for visual rendering, LaTeX source for download. We do not replace LaTeX with MathML-only output. arXiv contributes to the W3C Math Working Group via Deyan Ginev.
*Status: validated. Why: Neil Soiffer (2022-08-10) "HTML + MathML and you are pretty much done"; Avneesh Singh (2022-09-26); Volker Sorge (2022-09-02) — Sorge's caution that "MathML throws away information that LaTeX has" is addressed by keeping both.*

**Math serializes cleanly to braille displays.** Nemeth and UEB both supported via the screen reader's braille translator. Test using NVDA's Braille Viewer (engineering regression) and with real braille-display users (Nadolskis, Williams, Hartman).
*Status: needs verification. Why: Lucas Gil Nadolskis (2023-03-07) — "If its good for screen reader but not good for braille that is a problem"; Volker Sorge (2022-09-02) flagged Nemeth-yes / UEB-no in SRE at that time — verify current state.*

### Figures and tables

**Alt text on figures.** Authors are expected to provide alt text. Figure caption serves as fallback where missing. Author-facing tooling at submission to surface gaps is a separate track (submission-pipeline-as-lever).
*Status: validated. Why: every screen-reader-user voice in the research; Volker Sorge framing of submission-time as the lever.*

**Tables marked up semantically.** `<th scope>`, `<caption>`, row/column headers explicit. Where possible, also available as ancillary CSV.
*Status: validated. Why: Joseph Smith, Tony Malykh, Frank Elavsky, Bill Kasdorf.*

**Ancillary files (data, code) surfaced on the abstract page.** Where authors upload data or code as ancillary, those files are visible from the abstract page, not hidden under "other formats."
*Status: validated. Why: Joseph Smith (2022-08-22), Ben Firshman (2022-08-23), DOE OSTI request (CSV).*

### Visual and low-vision

**Reflow at 400% zoom.** No horizontal scrolling at 400% on any breakpoint. WCAG 1.4.10.
*Status: needs verification on both mockups.*

**Respect OS-level visual signals.** `prefers-color-scheme`, `prefers-contrast`, `forced-colors`, `prefers-reduced-motion` are honored as defaults. Design works in both light and dark; design works in Windows High Contrast Mode; animations are reduced when the user has requested it. **No arXiv-internal dark-mode toggle, font picker, or motion toggle.**
*Status: needs verification on the mockups.*

**Color independence on all status badges, version pills, type markers.** Color is never the sole carrier of meaning. Each marker has text or icon redundancy. (WCAG 1.4.1.)
*Status: design-side validation needed.*

**Low vision is its own track.** Wayne Dick's principle: low-vision users have distinct needs from screen-reader users — magnification, line length at zoom, independent equation enlargement, custom stylesheet support. Optimizing for blind users does not solve low-vision needs.
*Status: ongoing. Why: Wayne Dick (2023-06-06) — "It is not 'once you fix it for the blind, you fix it for everyone.'"*

### Cognitive and dyslexia

**Respect user-applied stylesheets and browser overrides.** Use `rem` units. Avoid fixed line-heights and letter-spacings. Don't pin font-family with `!important`. The user's own browser/extension/OS choices should propagate to arXiv content.
*Status: needs verification on the mockups. Why: Joseph Smith (2022-08-22) — "HTML gives you a lot more freedom — you can use software to change colors or typefaces."*

**HTML reader is reading-mode by default.** Minimal chrome, content-first, no decorative density. We pick the right defaults rather than offering a "focus mode" toggle.
*Status: design-side. Why: decisions-over-preferences principle plus the cognitive-load research voices.*

### Multimedia and international

**Deaf/HoH accessibility is a designed-for-but-unverified bet.** Design hooks for video/ASL ancillary content (LaTeX package + HTML-reader rendering hooks), but do not commit to the reader-facing experience until further research. **No author-uploaded audio abstract field** — adoption would be too low, abstracts rarely contain complex math (where author intent matters most), and the HTML reader serves the same use case better. Video/ASL is a different question and is preserved as a research-gap item.
*Status: research gap on deaf experience; decision on audio abstracts is "do not ship." Why: Raja Kushalnagar n=1; resource constraint and adoption-prediction on audio abstracts.*

**`lang` attribute on paper-language content.** Non-English papers tag `lang` correctly at the title/abstract/body level for screen-reader pronunciation and hyphenation.
*Status: validated.*

**Non-ASCII author names render and announce correctly.** Müller, López, Chéreau, Dalla Bontà render visually with diacritics and serialize through screen readers and braille displays.
*Status: needs verification. Why: Lucas Gil Nadolskis (2023-03-07), Jonathan Godfrey (2022-10-10).*

### Page mechanics

**Declutter the abstract page bottom.** The dense block of Download, Browse context, References & Citations, Bibex toggle, Submission history is consolidated and re-prioritized. Each section has a clear semantic landmark and a clear visual hierarchy.
*Status: validated. Why: many CSV voices + Coornaert (2022-11-14) + Miner (2023-02-28) — "You are all headings and lists."*

**Newcomer signposting.** A subtle "What is arXiv?" affordance for first-time visitors. arXiv-specific vocabulary ("cross-listed", "v2", "endorsement", "comments") is glossed or `<abbr>`-wrapped.
*Status: design-side.*

**Capability advertisement on the abstract page.** A small, honest, visible block per paper showing what's accessible: HTML version available / MathML / alt text on N of M figures / data download present / etc. Not a single compliance score. Visible to all readers; informs AT users about what to expect; gives authors social-proof feedback. **Next design move on the abstract-page mockup.**
*Status: to design. Why: tension resolution between Charles+Arvind's "grade visible publicly" and Avneesh Singh's "score will mislead users" — per-capability is the synthesis.*

**HTML reader is the primary destination from the abstract page**, not an experimental toggle. PDF remains a first-class download but stops being demoted.
*Status: validated. Why: the strongest emotional response in the entire research dataset is the 2024 HTML launch — "I literally cheered!" / "HTML is truly an order of magnitude better."*

### Continuous scroll, not pagination

**HTML papers render as one continuous document.** No reader-imposed pagination. Browser-native scroll, with section heading landmarks for AT users who navigate by headings. Page numbers from the source LaTeX are preserved as inline markers for cross-reference and citation practice, not as actual page breaks.
*Status: decision. Why: Jonathan Godfrey (2022-10-10) — page numbers preserved as "necessary evil" for citation; Avneesh Singh (2022-09-26) — "10-20 page HTML is OK" implies continuous works. No reader has asked for arXiv to paginate.*

## HTML reader push list

Beyond-baseline features specifically for the HTML reader, to push accessibility as far as we can — well beyond WCAG compliance. These are aspirations to design toward as the HTML reader matures.

### Citation experience for screen readers and beyond

Six independent voices in the research described distinct problems with the same inline-citation surface. The combined design moves:

- **Every inline citation carries full context in its accessible name.** `<a class="citation-ref" href="#ref12" aria-label="Reference 12: Smith et al., Title, 2024">[12]</a>` — visible "[12]" stays compact for sighted readers; the `aria-label` gives AT users the same context a sighted reader gets from author-year style citations. Addresses Tigwell's *"what is reference 10? Is that the paper I have in mind?"* without requiring a UI toggle.
- **Citation marks are aurally compact by default.** Wrap each inline mark so the announcement is "Smith 2024, reference 12" or similar — not "open bracket twelve close bracket." Sighted readers see "[12]"; listening readers experience low-noise prose flow. Addresses Dan Miner's *"auditory disturbance you cannot skip."*
- **References open as popups, not jumps.** On hover (sighted) or focus (keyboard/AT), a small popover shows the full reference inline. On explicit click, the user jumps to the references section and browser-back returns focus to the citation. Closes Godfrey's *"why jump around?"* + Firshman's arXiv Vanity precedent + Branham's TAPS jump-back pattern.
- **Reference list is structured for navigation.** `<ol>` with each `<li id="ref12">` carrying bibliographic info in semantically distinguishable spans (`<cite>`, author span, venue span, year span). Screen-reader users can list-navigate and jump.
- **"Cited by" affordance in each reference.** Each entry in the references section has a small icon-link back to the in-text citation(s) that use it — orientation aid for AT users who jumped to the bib and want to find context.
- **External link targets are scoped within each reference.** DOI / arXiv-ID / publisher URL within a reference is its own link, not the whole reference entry. Avoids "open bracket twelve close bracket open new tab" announcements.

*Status: design-side; user-testing recommended once HTML reader exposes a draft. Why: Dan Miner (2023-02-28), Garreth Tigwell (2022-08-10), Jonathan Godfrey (2022-10-10), Ben Firshman (2022-08-23), Sam Hartman (2022-08-02), Stacey Branham (2023-03-02).*

### Other push-list items

- **Alt-text-as-expandable.** For figures with long descriptions, short alt is the affordance that opens the longer description in-place. (Godfrey, Rothberg.)
- **Headings navigation everywhere.** Section headings (Abstract, Introduction, Methods, Results, References) are properly nested and labelled so AT users can jump-by-heading.
- **Per-equation read-aloud control.** When a screen-reader user lands on an equation, they can step through the expression tree (numerator, denominator, sub-expression) with cursor keys. (Volker Sorge, TV Raman.)
- **List of figures / list of tables** as navigable landmarks for AT users skipping to visual content.
- **Reader-contributed alt-text via Labs** (opt-in). Reader-supplied or reader-AI-drafted suggestions go into a queue with provenance labels; author reviews before they appear on the canonical paper.

## Productive tensions and resolutions

- **MathML vs LaTeX as math substrate.** Resolution: both. MathML for AT consumption; LaTeX preserved as source download and authoring trust.
- **PDF: keep tagging vs abandon.** Resolution: HTML is the priority substrate. Tagged PDF is best-effort for legacy corpus; not feature parity.
- **Accessibility grade public vs author-only.** Resolution: per-capability advertisement to readers (not a single grade); author-facing detailed report at submission (separate track).
- **Crowd alt-text trustworthy vs not.** Resolution: differentiate roles. Authors canonical; community suggests; author reviews before publication. Reader-contributed alt text goes through Labs-style opt-in with provenance labeling.
- **arXiv full-stack vs focused publisher.** Resolution: core arXiv ships HTML, math, alt-text, ID announcements, declutter, capability advertisement. Labs hosts opt-in experiments. arXiv never recommends third-party AI/audio/AT tools by name.

## Standards posture

- **WCAG 2.2 AA** on the abstract page and HTML reader. Audit date and methodology stated publicly when reached.
- **MathML 4** (with `intent`) for math. arXiv contributes to the W3C Math Working Group via Deyan Ginev.
- **Speech Rule Engine / MathCAT** for math read-aloud where the AT toolchain supports it.
- **EPUB Accessibility 1.1** principles applied to HTML reader where they translate (structured navigation, alt text, language tagging).
- **W3C Personalization / Adapt:** track but don't build to until stable.

## Brand-level positions

- **Decisions over preferences.** arXiv does not build internal preference centers for accessibility (font picker, theme toggle, motion toggle, font-size selector, reading-mode toggle). OS/browser-level accessibility signals are respected as defaults. We pick the right defaults once, courageously, rather than punting to user configuration.
- **No third-party tool recommendations.** arXiv does not maintain or publish lists of external AI tools, audio-summary services, or AT software. Such lists age poorly. arXiv provides high-quality metadata so external tools can do their work well.
- **No author-uploaded audio/video abstract field.** Adoption would be too low; abstracts rarely contain the complex math where author intent matters most; HTML reader serves the same use case better. Video/ASL for deaf accessibility remains an open research question — distinct from this decision.
- **Capability advertisement, not compliance claim.** Every paper shows what it actually supports, honestly. No single grade. First-pass surface (visible to readers, above the metadata block on the abstract page): present-only — no "missing" indicators. arXiv is not here to punish hard-working researchers who managed to finish their paper; only to help all researchers as much as we can.
- **No paid retainer experts; no annual a11y forum committed.** Reader goodwill leveraged for occasional testing. Revisit as conditions change.

## Pointers

- Research syntheses, raw data, and open research questions: `~/Desktop/arxiv-mockups/arxiv-public/references/`
- Submission-pipeline-as-accessibility-lever work: separate track (not in this document; the submission flow is where most author-side accessibility behavior change can happen)
- Brand updates (post-spinout): separate track
