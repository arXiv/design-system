# Linking the Abstract/HTML Paper mockup to user feedback
[Github-hosted Mockup](https://arxiv.github.io/design-system/mockups/merged-abstract-reader.html)

Working draft. 06/26/26. Shamsi Brinn.

## Description

The mockup of the combined abstract page and HTML papers page necessarily incorporates a lot of design decisions. This document links those decisions back to user research findings and points out gaps where more research and user testing is needed.

---

## Design decisions tied to feedback

| Mockup decision | Feedback it answers | Source | Strength |
|---|---|---|---|
| **HTML treated as a first-class destination**, merged into abstract page for immediate access | Strong user signals support HTML format: "HTML + MathML and you are done"; "I literally cheered."; Near-universal across AT interviews; #1 cross-dataset leverage item. Removing the 'experimental' banner was the largest single theme (~25 issues). | A11y §B1; UXDH §1; Overview #1; GH-closed §B1 | **Strong** (problem), **Designer-led** (solution space is untested) |
| **Show format and size for TeX Source** | "When you download source there isn't a file extension… you don't know what you've got or how to open it." Also requested by EUST.| A11y §B25 | **Moderate** |
| **Surface ancillary files** | Source download is buried ("must first go to formats link"); recurring across interviews + UXDH. Broader code/data-association demand (BPS #54; Firshman). Requested by EUST. | A11y §C-NEW9; UXDH §4/§8; BPS #54 | **Moderate** |
| **Display full category name** | An internal tester missed the category when only `[gr-qc]` showed; | Internal | **Moderate** |
| **Author lists should toggle** (first 8 shown) | >100-author lists cause "an enormous amount of scrolling" (#3395, #1180). *H to truncate is an open question.* | GH-open §A9; OpenQ Q5 | **Moderate** |
| **Show no paper metrics** | Heavy-user objection ("I do not want arXiv to endorse bibliometrics"), though a minority wants them. | UXDH §11; Overview #10 | **Strong** |
| **arXiv ID spelled phonetically for screen readers**; "arXiv" announced as "archive" | "The way your name is read is baffling… it reads it as a roman numeral." | A11y §B20 | **Strong** |
| **Make it easy to grab citation** | Bibliographic Explorer was the most-used, most-useful Lab but can be entirely internalized. Feedback over many years requestiong citation copy feature. Internal testing reworked placement and functionality. | Labs #1; AUXDH-1132 | **Strong** |
| **Dont let footnotes, citations, or reference links interrupt the flow** (especially relevant for AT users) | "Popups are a godsend… make reference a popout instead of jumping to the bottom."  ~9 independently-filed issues over 3 years. Click-not-hover and per-reference choice are both explicit responses. | A11y §B2 (ask #1); GH-open §A3; GH-open §A2; GH-closed §B2; A11y §B2 | **Strong** |
| **Footnotes use marginalia when space is available** | "When the mouse moves away from the footnote label to click the link in the overlay, the overlay is gone." ~9 issues. | GH-open §A3 | **Strong** |
| **Citation chips deemphasized, muted color by default** | "Please introduce a feature that hides all citations from the text — improves readability a lot"; AT corollary: "citation markings are a large auditory disturbance." Sighted + AT feedback converges. | GH-open §A7; A11y §C-NEW7 | **Strong** |
| **TOC always visible but keep it minimal** | TOC friction cluster — ~10 closed issues | GH-closed §B4 | **Strong** |
| **Maintain paper sovereignty.** Non-paper content (like Labs) must justify its presence and stay subordinate. | ""Keep it simple - I want to find the abstract, get PDF, ADS link, DOI, BiBTeX, citations and references and that's about it.""; "Integrating this stuff into the arXiv pages is an actively bad idea."; "Too much chrome… before I get to the abstract" | UXDH §3/§4; Overview #3/#8; UXDH-1138 | **Strong** (problem); **Designer-led** (layout choices) |
| **Labs have reduced priority** — Placement is below the paper (renamed "Related"), toggled on per tool | Split user feedback, but mostly negative. Resisters read Labs as a breach of arXiv's neutrality/minimality: "it just adds clutter, confusion and distraction… keep it simple and clean" (AUXDH-1101); "Leave arxiv UNMODIFIED… avoid social nonsense" (1117); "offensive" (1122). But there were positive comments too: "great improvements!" (1146); CORE Recommender "useful… nice that this is here" (1184); Requests for specifics (1102/1109/1111/1120). | UXDH §4/§11 | **Strong** |
| **Semantic structure and hierachy is sensitive to AT user needs** | "The site needs structure. It is very flat… you are all headings and lists"; "a heading 4 as the first heading — classic sign of using headings for styling." | A11y §B23/§C-NEW14 (ask #13) | **Strong** |
| **Surface useful AT features (or lack of them) to all readers** — Make alt text more visible; flag missing alt text with affordance for users to contribute; Surface header and image permalinks. | "Don't let the perfect be the enemy of the good — happy to have any alt text"; There is interest in community-contributed descriptions. | A11y §B5 (ask #4) | **Moderate** |
| **Access multiple formats in different ways and locations**. In addition to TeX download, added options to view TeX for each formula. | "Leave the LaTeX in there"; "I prefer to read the tex source"; | A11y §B3; GH-open §A9 | **Thin → Designer-led**, needs user testing|
| **"Listen" read-aloud** | Built a first attempt, only tested internally. | A11y §C-NEW8; OpenQ Q45 | **Thin / Designer-led**, needs testing |

---

## Gaps in the user research

### A. Top-leverage problems the mockup doesn't yet solve

1. **No upward path back to the listing.** "There seems to be no way to go back to the category." Possible regression. 
2. **Reader-controlled typography: Deferred.** ~8 issues requesting typography controls; Dyslexic font research invalidates that direction; The mockups lean on browser-level overrides and native zoom instead of UI controls. Are explicit reader controls warranted?

### B. Designer-led decisions that need usability testing

3. **Merged abstract and HTML paper page.**
4. **Equation marginalia chips (View TeX / Copy / Permalink / Listen).** —Validate with Deyan/Bruce first, then with users.
5. **"Listen" read-aloud feature.** —Target testing audience is sighted users with reading impairments (ADHD, dyslexia).
6. **Surfacing figure alt-text, user-contributed descriptions** —Explore usefulness *and* maintainability.

### C. Open accessibility questions

7. **Page semantics:** What page structure and elements will best support AT navigation? Should each section have its own `h2`? What `aria-label` should `<main>` carry?
8. **Math accessibility** MathML-4 + Intent path needs real AT testing, not inference.
9. **Author-list truncation semantics:** `<ul>` announces "list of 247 items" vs. comma-joined string? How does "show all" behave for AT?
10. **Reading order vs. visual order:** where does the sidebar land in the DOM relative to the abstract, and does that hurt AT users? Now that we lead with HTML (merged abs+html page) does it even matter anymore? Reaching the PDF download button quickly is not as important for AT users if they are already on the most readable version of the paper.
11. **Motion & forced-colors:** JS `scrollIntoView({behavior:'smooth'})` paths still bypass `prefers-reduced-motion`; Windows High Contrast Mode behavior of hard-coded colors is untested. Verify, don't assume.
12. **Keyboard model:** Need to test tab order vs. reading order, reader shortcuts, focus-ring contrast on the dark header, modal focus-trap + Esc + focus return.

### D. Needs more work and testing

13. **Mobile / responsiveness** 
15. **Whole-mockup usability testing.** 

### E. Populations we have insufficient data on

16. **Deaf/signing users (n=1).** "Getting spoken or signed information in print is a challenge." 
17. **Newcomers vs. experts.** New users feel arXiv looks dated, is hard to use. Long-term users value the heritage and non-commercial nature ("don't ruin this.")
---

## Tensions to resolve (feedback conflicts)

- **Additive features vs. paper sovereignty** Adding the Labs/tabs section drew a measured backlash (*"it just adds clutter, confusion and distraction"* AUXDH-1101; *"Leave arxiv UNMODIFIED… avoid social nonsense"* 1117; **and** a measured welcome (*"great improvements!"* 1146; CORE Recommender *"useful… nice that this is here"* 1184; The solution is not to freeze progress but to add new features in ways that don't disrupt the practicality, efficiency and speed that users want from arXiv.
- **Metrics:** a vocal minority wants views/downloads/citations; Heavy users object. Our design policy bars them on public pages and heavy users object. *Confirm this is official arXiv policy.*
- **Typography: Browser and user settings vs. UI controls:** Research proves dyslexia fonts don't improve reading; Some user requests for UI controls over font size, color, fonts; Browser controls like zooming in and out, or user settings, already provide excellent control; UI controls will add clutter to an already busy page.
- **arXiv PDF vs. VoR prominence** — Elsevier respondent wrote that arXiv PDF button is "too prominent relative to the journal version." Overlay Journals also want clear differentiation between arXiv and other versions. Unadressed in mockup because it lacks metadata support.
- **Math rendering: MathML vs. LaTeX-source vs. MathJax** — Ask Deyan and Bruce, formalize decision and why. Placeholder so I don't forget to ask.

---

## Sources

| Tag | Description | Details |
|---|---|---|
| **[BPS](https://docs.google.com/spreadsheets/d/1dut__Vh9lEARrVGkHw-2w1e-ptaKA4XUsNkIAixLDR8/edit?usp=sharing)** | Design/UX comments filtered from the BPS 2025 annual survey (open-ended) | 9,419 respondents, ~80 design comments |
| **[AUXDH](https://arxiv-org.atlassian.net/jira/software/c/projects/AUXDH/boards/80)** | UX Data Hub / Jira observations, ~2019→present | ~2,950 observations, 14 themes |
| **[A11Y Interviews](https://cornell.box.com/s/i388v9x90md4mqawuen1o601bm6bjxdu)** | Mediated interviews with AT users and experts | 42  interviews, Jul 2022–Jun 2023 |
| **[Reader Interviews](https://cornell.box.com/s/injxn6g4d5kkdfkprzkwd09mggak2ars)** | Mediated interviews with diverse arXiv readers | 11 interviews, Feb 2021 |
| **[Github issues](https://github.com/arXiv/html_feedback/issues)** | GitHub issues submitted by HTML paper readers | 107 relevant issues closed, 72 open |
| **[Labs](https://github.com/arXiv/design-system/blob/master/audits/audit-labs.md)** | Functional audit of 16 arXiv Labs integrations | Single report, Apr 2026  |
| **[Overlay Journals](https://docs.google.com/document/d/1FOFxM6pqDFMdMTGOoX65c47rieHPGOcqKxhl3gCMo0A/edit?usp=sharing)** | Interview-based report on Overlay Journals and arXiv | Jan 2025 |

> One caution: The A11y interviews **pre-date arXiv's HTML papers launch**. Many feature asks are now met, and the tech landscape has changed profoundly, so we need a new round of interviews.
