# Linking mockups to user feedback

**Working draft. 06/26/26. Shamsi Brinn.**

## Description

The mockups I am working on make a lot of design decisions. This document links those decisions back to user research findings, and points out gaps where more research and user testing is needed.

---

## Design decisions tied to feedback

| Mockup decision | Feedback it answers | Source | Strength |
|---|---|---|---|
| **HTML treated as a first-class destination**, not an experimental toggle; the red "experimental" banner is gone | The single strongest signal in the corpus. "HTML + MathML and you are done"; "I literally cheered." Near-universal across AT interviews; #1 cross-dataset leverage item. The red banner was the largest single closed-issue theme (~25 issues). | A11y §B1; UXDH §1; Overview #1; GH-closed §B1 | **Strong** |
| **TeX Source shows explicit format + size** ("TeX Source / .tar.gz · 286 KB") | "When you download source there isn't a file extension… you don't know what you've got or how to open it." (Williams) | A11y §B25 (named ask #7) | **Moderate** |
| **Ancillary files surfaced** | Source download is buried ("must first go to formats link"); recurring across interviews + UXDH. Broader code/data-association demand (BPS #54; Firshman). *The "surface it" is well-evidenced; the specific ancillary-card UI is an extension.* | A11y §C-NEW9; UXDH §4/§8; BPS #54 | **Moderate** |
| **DOI + full category name in the identity line** | Internal testing: a tester missed the category when only `[gr-qc]` showed; many readers land on the HTML page directly without the abstract page. | Internal | **Moderate** (internal) |
| **Authors & metadata kept legible** (not demoted to tiny type) | "The authors have been de-emphasised — a mistake"; "the arxiv number and authors were essentially unreadable (tiny font)." Feeds the #5 cross-dataset leverage item. ~20+ low-vision observations on small metadata type. | UXDH §2; Overview #5 | **Strong** |
| **"Show all N authors" toggle** (first 8 shown) | >100-author lists cause "an enormous amount of scrolling" (#3395, #1180). *But how to truncate is an open question — see gaps.* | GH-open §A9; OpenQ Q5 | **Moderate** (+ open) |
| **Metrics deliberately absent** ("Who cites this" links out, no counts) | Aligns with arXiv design policy barring paper metrics on public pages, and with heavy-user objection ("I do not want arXiv to endorse bibliometrics"). A vocal *minority* wants metrics — see Tensions. | UXDH §11; Overview #10 | **Strong** (policy-aligned) |
| **arXiv ID spelled phonetically for screen readers**; "arXiv" announced as "archive" | "The way your name is read is baffling… it reads it as a roman numeral." (Miner) | A11y §B20 (named ask #10) | **Strong** |
| **Cite section graduates Bibex into the page** — collapsed by default, native `<select>` for BibTeX/APA/Chicago/MLA, copy-without-expand, BibTeX scrolls instead of overflowing | Bibex is the most-used, most-useful Lab (audit verdict: incorporate directly). Export-citation modal was "too wide for mobile… X-button off screen." "enable bibex" is confusing/technical. Internal testing reworked placement + version label. | Labs #1; UXDH §3; Internal | **Strong** |
| **Citation-chip popovers in the reader** (click-to-open, *per-reference* "Jump to reference") | "Popups are a godsend… make reference a popout instead of jumping to the bottom." Footnote/citation hover popups were unusable — ~9 independently-filed issues over 3 years (the strongest validation in the GitHub data). Click-not-hover and per-reference choice are both explicit responses. | A11y §B2 (ask #1); GH-open §A3 | **Strong** |
| **Reference jumps get a header offset, a destination highlight, and a "Back to your place" return link** | "I've clicked on [23] but it was hidden behind the header." ~12 open + ~12 closed issues on jump-hidden-under-sticky-header; plus "what is reference 10? Is that the paper I have in mind?" | GH-open §A2; GH-closed §B2; A11y §B2 | **Strong** |
| **Footnotes cloned to margin (wide) / popover (narrow), with a no-JS inline fallback** | "When the mouse moves away from the footnote label to click the link in the overlay, the overlay is gone." ~9 issues. | GH-open §A3 | **Strong** |
| **Citation chips muted grey by default**, color on hover/focus | "Please introduce a feature that hides all citations from the text — improves readability a lot"; AT corollary: "citation markings are a large auditory disturbance." Sighted + AT demand converge. | GH-open §A7; A11y §C-NEW7 | **Strong** |
| **TOC as a centered dropdown / thin rail** with current-section highlight; full-screen overlay on mobile | TOC friction cluster — ~10 closed issues (appendix missing, links don't scroll, cut off, can't minimize, request for more reading space when hidden). | GH-closed §B4 | **Strong** |
| **Keep the paper sovereign** — non-paper content must justify its presence and stay subordinate: metadata into an accordion, rail card, Related moved out to a full-width band | The "declutter" feedback is really three threads, all about content/intent over tidiness: **wrong/irrelevant content** ("'Leadership Team' does not belong on every abstract… I thought it was the research group" — Redington); **distance to the paper** ("too much chrome… before I get to the abstract" — Chatterjee); and **literal density** ("the right side of the box is empty"; crowded mis-tap links). #3 + #8 cross-dataset leverage items. | UXDH §3/§4; Overview #3/#8 | **Strong** (problem); **Designer-led** (the rail-card solution) |
| **Related/Labs kept opt-in and subordinate** — moved out of the rail to a full-width `<aside>` band below the paper, grouped, default-empty, toggled on per tool | Direct answer to the Labs-tabs rollout, which split users. Resisters read Labs as a breach of arXiv's neutrality/minimality: "it just adds clutter, confusion and distraction… keep it simple and clean" (AUXDH-1101); "Leave arxiv UNMODIFIED… avoid social nonsense" (1117); "offensive… bibliometrics" (1122); "rules out having the tabs *replacing* the abstract" (1142). Welcomers wanted *more*: "great improvements!" (1146); CORE Recommender "useful… nice that this is here" (1184); requests to add author-info / MathSciNet / Scholar / talk-video tabs (1102/1109/1111/1120). Opt-in + subordinate threads the split. | UXDH §4/§11 | **Strong** |
| **Heading hierarchy / landmarks / skip links / `role=main`** | "The site needs structure. It is very flat… you are all headings and lists"; "a heading 4 as the first heading — classic sign of using headings for styling." | A11y §B23/§C-NEW14 (ask #13) | **Strong** (problem); **Designer-led** (specific h1/landmark labels — see gaps) |
| **Reader-controlled affordances via the browser** (HTML is first-class) | "HTML gives you a lot more freedom — you can use software to change colors or typeface"; dyslexic-font users. | A11y §B15 | **Strong** (for HTML-as-enabler) |
| **Figure alt-text honesty** — surfaces present alt text to sighted readers; flags missing alt with an "Add an image description" affordance | "Don't let the perfect be the enemy of the good — happy to have any alt text"; "ideal is that alt tag is a clickable link." Community-contribution interest. *Surfacing alt is evidenced; the present/missing UI is an extension.* | A11y §B5 (ask #4) | **Moderate** |
| **Equation marginalia: View TeX / Copy / Permalink** | "Leave the LaTeX in there" / "I prefer to read the tex source"; section-heading copy-link requests (#4776). *The interaction model is largely designer-invented.* | A11y §B3; GH-open §A9 | **Thin → Designer-led** |
| **"Listen" read-aloud (TTS) aimed at sighted listeners**, math spoken via MathSpeak | Internal testing drove the math-spoken correctness ("Equation 2.3 is not what a blind user needs"). Audio-abstract user demand exists but is flagged "do not ship." *Direct external demand for this specific feature is thin — it's a forward proposal; the per-equation "Listen" chip is already disabled/forward-looking.* | Internal; A11y §C-NEW8; OpenQ Q45 | **Thin / Designer-led** |

---

## Gaps in the user research

### A. Top-leverage problems the mockup does *not* yet solve

1. **No upward path back to the listing.** "There seems to be no way to go back to the category." Possible regression. (UXDH §3; Overview #7)
2. **Reader-controlled typography: Deferred.** ~8 issues requesting font-size controls and disabled justification/hyphenation; dyslexic-font users want control. Dyslexic font research invalidates that direction, and the mockups lean on browser-level overrides and native zoom instead of UI controls. Are explicit reader controls warranted? (GH-open §A4; A11y §B15)

### B. Designer-led decisions with thin/no direct evidence — validate before locking in

3. **The rail-card layout itself.** "Declutter the bottom" is strongly evidenced; *that the answer is a 275px warm-wash rail card within content width* is a designer hypothesis. *Action: usability-test the rail vs. the status quo for findability of PDF, cite, and metadata.*
4. **Equation marginalia chips (View TeX / Copy / Permalink / Listen).** Largely invented interaction model. *Action: test discoverability and whether the margin band is noticed; the "Listen" chip is already disabled pending a decision.*
5. **"Listen" read-aloud feature.** Forward proposal with thin external demand. *Action: validate that sighted listeners (dyslexia/fatigue/multitasking) actually want in-page TTS, and that it doesn't read as scope creep against the "don't ruin this" constraint.*
6. **Figure alt-text present/missing UI + "Add an image description."** Surfacing alt is evidenced; the contribution affordance implies a moderation/workflow the team must own (arXiv is a very small team). *Action: confirm there's a maintainable path before promising contribution.*

### C. Open accessibility questions — explicitly to-validate (from `accessibility-research-questions.md`)

These are flagged in the research as *questions, not findings.* The mockup picked an answer for each; none is user-validated:

7. **Page semantics:** What is the page `h1` — the title, or "Abstract: [title]"? Should each section (Abstract / Authors / Subjects / Cite as / Version) be its own `h2`? What `aria-label` should `<main>` carry? (OpenQ Q1–3, Q37)
8. **Author-list truncation semantics:** `<ul>` (announces "list of 247 items") vs. comma-joined string? How does "show all" behave for AT? (OpenQ Q5)
9. **Reading order vs. visual order:** where does the rail land in the DOM relative to the abstract, and does that hurt either AT users or sighted scanning? (OpenQ Q4)
10. **Color-independence:** version pill and NEW/REP/WDR/CROSS badges — is color + letter enough, or do we need icons? (OpenQ Q17–19)
11. **Motion & forced-colors:** JS `scrollIntoView({behavior:'smooth'})` paths still bypass `prefers-reduced-motion`; Windows High Contrast Mode behavior of hard-coded colors is untested. The interviews are *silent* on both — verify, don't assume. (OpenQ Q16/Q20)
12. **Keyboard model:** tab order vs. reading order, reader shortcuts (`next/prev section`, jump-to-references, `?` overlay), focus-ring contrast on the dark header, modal focus-trap + Esc + focus return. (OpenQ Q23–26)

### D. Untested across the board

13. **Mobile / responsive.** The earlier abstract mockup *failed 320px reflow (WCAG 1.4.10)*; needs verification in the merged file. Header chrome eating the mobile viewport was the single largest UXDH cluster (~80 observations). *Action: test mobile portrait + landscape + iOS Safari explicitly.* (GH-closed §C; UXDH §3)
14. **Math accessibility is silent in the GitHub data** despite being the top interview theme. "Do not read that silence as satisfaction" — the no-MathJax / MathML-4 + Intent path needs real AT testing, not inference. (GH §D; A11y §B1)
15. **Whole-mockup usability testing.** Nearly all decisions above predate any moderated session on *this* artifact. The internal review round (FEEDBACK-CHANGELOG) was colleagues, not end users.

### E. Populations we have little/no data on

16. **Deaf/signing users (n=1).** One participant; "getting spoken or signed information in print is a challenge." Flagged *recruit-before-design* — a signed/video-abstract track is unvalidated. (A11y §C-NEW1, ask #19)
17. **Newcomers vs. experts.** "Looks old / hard sell for newcomers" comes from new users; heavy users value the neutral chrome and say "don't ruin this." We don't know which population the rail-card redesign helps or alienates. (UXDH §10/§11)

---

## Tensions to resolve (feedback conflicts with itself or policy)

These aren't gaps in evidence — they're places where the evidence *points both ways* and the team owes a decision:

- **Additive features vs. paper sovereignty — the Labs rollout is the documented precedent.** Adding the Labs/tabs section drew a measured backlash (*"it just adds clutter, confusion and distraction"* AUXDH-1101; *"Leave arxiv UNMODIFIED… avoid social nonsense"* 1117; *"offensive… bibliometrics"* 1122) **and** a measured welcome (*"great improvements!"* 1146; CORE Recommender *"useful… nice that this is here"* 1184; requests for more tabs). The lesson isn't "omit" — it's **opt-in + subordinate**, which the Related band does. Weigh every *new* affordance (Listen, marginalia) the same way, against the neutrality constraint and the BPS "minimal changes" voices.
- **Metrics:** a vocal minority wants views/downloads/citations; design policy bars them on public pages and heavy users object. The mockup sides with policy. *Confirm this is the final answer.*
- **"Decisions over preferences" vs. reader-controlled typography** — see gap #2. The mockup's no-toggle stance is in direct tension with the font-size/justification asks.
- **arXiv PDF vs. publisher Version-of-Record prominence** — a publisher voice (Elsevier) says the arXiv PDF button is "too prominent relative to the journal version." Currently unaddressed.
- **Math rendering: MathML vs. LaTeX-source vs. MathJax** — genuine expert disagreement; the mockup ships no MathJax. Defensible, but a live debate.

---

## Sources

*All files in `Desktop/arXiv-mockups/User and other research/references/`. Tags are the shorthand used in the tables above.*

| Tag | Source file | What it is | Size |
|---|---|---|---|
| **BPS** | `user-feedback-design.md` | Design/UX comments filtered from the BPS 2025 annual survey (open-ended) | 9,419 respondents, ~80 design comments |
| **UXDH** | `ux-observations-themes.md` (← `user-feedback-observations.csv`) | UX Data Hub / Jira observations, ~2019→present | ~2,950 observations, 14 themes |
| **A11y** | `accessibility-interviews-synthesis.md` | Interviewer-mediated AT-user & expert interviews | 42 interviews, Jul 2022–Jun 2023 |
| **GH-closed** | `github-ux-issues-synthesis.md` | Closed UX-labeled GitHub issues | 107 issues |
| **GH-open** | `github-open-ux-issues-synthesis.md` (← `open-ux-issues.json`) | Open UX-labeled GitHub issues | 72 issues |
| **Labs** | `labs-audit.md` | Functional audit of 16 arXiv Labs integrations | Apr 2026 |
| **Overview** | `research-foundation-overview.md` | Cross-dataset synthesis, "top-10 leverage" list | — |
| **OpenQ** | `accessibility-research-questions.md` | 28+ **open research questions** — *to-validate, not findings* | — |
| **Internal** | `FEEDBACK-CHANGELOG.md` | June 2026 internal review round | — |

> Two provenance cautions: (1) the A11y interviews **pre-date arXiv's 2024 HTML launch**, so their feature asks read as *targets now partly met.* (2) OpenQ items are **open questions, not findings** — cited as "to validate," never as "users said."
