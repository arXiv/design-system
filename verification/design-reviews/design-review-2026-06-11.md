# Fresh-Look Review: Abstract Page + HTML Reader Mockups

**Reviewer:** Claude (independent design review)
**Date:** 2026-06-11
**Inputs:** Both mockups (code + rendered at 1440/1000/390/320px, interactions exercised), all five research syntheses, accessibility-priorities.md, DESIGN-POLICIES.md, labs-audit.md.

---

## Verdict

These are unusually research-honest mockups. Nearly every component traces to a named finding, and the hardest calls (capability advertisement vs. compliance score, HTML-first without demoting PDF, decisions-over-preferences) resolve real tensions in the data rather than ignoring them. Of the CSV synthesis's top-10 leverage items, eight are implemented or structurally addressed.

The gaps below are mostly in three categories: (1) concrete defects I verified by rendering; (2) places where the mockups stop short of their own research; (3) one place where the design contradicts the research.

---

## Verified defects (found by rendering, fix before promotion)

**1. Abstract page fails reflow at 320px (WCAG 1.4.10).**
At 320px viewport the header nav (Search / About / Submit / Donate / Log in) overflows to 469px scrollWidth — horizontal scrolling on the whole page. The header has no narrow-width collapse. The HTML reader passes the same test (0 overflow). accessibility-priorities.md lists 400% reflow as "needs verification on both mockups" — verified: reader passes, abstract fails.

**2. TOC dropdown leaks raw TeX (HTML reader).**
Dropdown entries render as "Evolution of Ψ\Psi and Φ\Phi", "Evolution of ℛ\mathcal{R}". The TOC-cloning script's `textContent` extraction picks up the MathML `<annotation>` TeX alongside the rendered symbol. Strip `annotation` elements when extracting titles.

**3. The citation-style switcher is a broken ARIA pattern (abstract page).**
`role="radiogroup"`/`role="radio"` is wired with click handlers only. The ARIA radio pattern requires roving tabindex + arrow-key navigation; without it, screen-reader users are told "radio button" and arrow keys do nothing. Either implement the full pattern or use plain buttons with `aria-pressed` (simpler, equally accessible). Same applies to the source switcher (preprint/journal).

**4. Smooth scrolling ignores `prefers-reduced-motion` (HTML reader).**
The CSS reduced-motion blocks kill CSS animations, but `scrollIntoView({behavior:'smooth'})` in the jump-to-reference and back-to-your-place JS bypasses CSS. Gate with `matchMedia('(prefers-reduced-motion: reduce)')` → `behavior:'auto'`. The abstract page has no reduced-motion handling at all (lower stakes — only micro-transitions — but the policy says honor it).

**5. px everywhere on the abstract page.**
accessibility-priorities.md (cognitive/dyslexia): "Use `rem` units. Avoid fixed line-heights… the user's own browser/OS choices should propagate." The abstract mockup is entirely px-based (body 15px, metadata 13px, fixed line-heights). Browser-level font-size overrides won't scale it. This is the design contradicting its own priorities doc; the production spec should be rem-based. (Reader chrome is px too, but ar5iv's content layer is rem — the part that matters most already complies.)

---

## Abstract page — where it stops short of the research

**6. The upward path (top-10 item #7) — partially resolved by decision.**
*Updated 2026-06-11 after discussion with Shamsi:* prev/next links are broken on production, 2020 analytics showed they were rarely clicked, and the team is deliberately retiring them — their removal from the mockup is intentional, not an oversight. The remaining open question is the narrower one: "no way to go back to the category" (AUXDH-950/951). The Subjects links in the metadata band do reach the category listings; whether that satisfies the upward-path need, or whether a more visible "gr-qc › recent" affordance is warranted, is a (small) open design question — note the complaint data is from 2019 mobile users and may itself be stale.

**7. Ancillary files (data/code) are not surfaced.**
Validated priority ("Joseph Smith, Ben Firshman, DOE OSTI — ancillary files visible from the abstract page, not hidden under formats"). The mockup has no slot for them. The Accessibility Notes block or a fourth row in the actions column ("Data & code") would close it. This is also the capability with the strongest cross-audience payoff — Smith: "well-written code… I would prefer that to reading the paper."

**8. Accessibility Notes: the partial-coverage case is undesigned.**
The mockup hardcodes the happy path ("Alt text on all figures"). What renders at 8-of-12 figures? Present-only framing makes "alt text on 8 of 12 figures" (the priorities doc's own example) awkward — and pure silence at 0/12 means AT users can't distinguish "no alt text" from "block not implemented." Suggest: counts are honest and still non-punitive ("Alt text on 8 of 12 figures" is *present-framing* with information). Also: each capability should link to a short help page — "Structured math" is insider vocabulary to the very newcomers and AT users the block serves.

**9. Newcomer signposting isn't there yet.**
Priorities doc: "a subtle 'What is arXiv?' affordance" (Miner: "I have no clue what I am walking into"). The header's "About" link doesn't do this work — newcomers landing from Google don't scan headers. Also no `<abbr>`/glossing of arXiv-specific vocabulary on the page: "Comments" field opens with "v3: 18 pages…", "cross-listed" categories, version pills — all unglossed (research question #31).

**10. Download honesty details.**
- TeX Source button gives no format hint. Robin Williams: "there isn't a file extension… not obvious if it is a zip or a tar." A small "(.tar.gz)" under or in the button closes a named, validated ask.
- Filename-as-title (top-10 item #6) is server-side, invisible in a mockup — but nothing in the mockup's comments carries the requirement. Add it to the component comment so it survives implementation.
- BibTeX uses `author={Palomares, Adrian and Shapiro, Ilya L. and others}` — real arXiv BibTeX lists all authors; "and others" in copied BibTeX is the kind of subtle wrongness researchers notice. Citation text is arXiv's highest-trust copy surface; mockup data should be exact.

**11. Author links: decide what happens before identity work lands.**
Each author name links to "#". In production today, that link does the *harmful* thing (surname-initial collision — Parampreet Singh: "Till this problem is fixed, I can't find arxiv useful any more"). If author-identity records aren't ready at launch, linking to the current broken search reproduces the #4 leverage complaint inside the new design. Options: link to search with an honest disambiguation note, or don't link names until records exist. Worth an explicit decision in the mockup comments.

**12. Metadata font sizes flirt with the #2 complaint theme.**
"Fonts too small" (metadata, DOI, citation links) is a ~20-observation theme. The redesign sets metadata values, labs labels, a11y items, and footer at 13px — larger than legacy but still the smallest text on the page, on the elements users specifically named. Cheap insurance: 14px floor for interactive text. (Also helps the 24×24 target-size exception margins on mobile.)

**13. DOM order: downloads before abstract.**
`nav.abs-actions` precedes the abstract in source order, so screen readers hit HTML/PDF/TeX before any content. That's defensible (button findability was a top complaint) but it's exactly research question #4, still open — flag for AT testing rather than assuming.

**14. Labs placement vs. your own audit.**
DESIGN-POLICIES: "Labs that require login should be deprioritized in placement." The mockup gives alphaXiv (login-walled, per labs-audit.md) equal placement with frictionless tools, and includes ScienceCast, which the audit called a poor-affordance integration. Suggest the toggle list order encode the audit: frictionless first, login-walled last (or behind a "more" group).

---

## HTML reader — where it stops short of the research

**15. Justified body text works against the dyslexia track.**
The override justifies body text "to match the print/PDF convention readers expect." Justified text creates uneven word spacing ("rivers") and is consistently advised against for dyslexia (your own audience: Joseph Smith — "I basically can't read a paper"; reading-mode-by-default principle). This is tension E7 (print culture vs. browser-native) resolved in favor of print *for the surface where the cognitive-accessibility users live*. Recommend left-aligned (ragged right) as the reader default — it's also what every reader-mode product ships. If justification stays, it must at minimum not fight user stylesheet overrides.

**16. The citation chips add AT noise instead of reducing it.**
The push list's citation experience has three AT commitments: full context in each citation's accessible name ("Reference 12: Smith et al., 2024"), aurally compact announcement, and skim suppression (Miner's "auditory disturbance you cannot skip" — named feature ask #2). The mockup's implementation gives each chip `role="button"` + `aria-expanded` and no contextual label — so a cluster like [15, 44, 45, 26, 31, 3] now announces as *six expandable buttons*, which is more disturbance than the plain links it replaces. The popover work is good for sighted/keyboard users; the AT layer of the push list is simply not wired yet. The skim-suppression toggle is also absent — and note it genuinely collides with "decisions over preferences." My read: it's a content-layer reading control (like the TeX/math toggle you already ship per-equation), not a preference center — but that's a call to make explicitly, not silently drop.

**17. Popovers close on 50px scroll — hostile at high zoom.**
Low-vision users at 200–400% zoom scroll *to read the popover itself*. Closing on scroll yanks it away mid-read. Close on outside-interaction/Esc/source-leaving-viewport instead, or anchor the popover to the document rather than the viewport. This interacts with the flagged low-vision research gap — test with magnification users before promoting the pattern.

**18. The disabled "Listen" chip should go.**
It advertises capability that doesn't exist (honesty-of-affordance), it will age badly ("coming soon" + small-team maintenance policy), and per-equation speech is arriving via MathML Intent + browser/AT (Deyan's track), where a play-button UI may never be the right shape. Remove it; add it back when real.

**19. Reading time will be wrong on math-heavy papers.**
words/200 with only the bibliography excluded counts every equation token as prose. On this very sample paper the estimate will be significantly off. Either exclude `<math>` content and figures/tables from the count, round aggressively ("~40 min"), or drop the feature. A precise-looking wrong number is worse than none.

**20. Verify the anchor-offset fix covers every jump path.**
Sticky-header-covers-anchor-target was the #2 GitHub theme (12 independent filings). The global `scroll-padding` handles native anchors; confirm it also holds for the JS `scrollIntoView` paths (jump-to-reference, back-to-your-place, TOC entries) in compact-header state, where header height differs. This bug class regenerates easily.

**21. Long-paper performance is unaddressed.**
Continuous scroll is the right decision, but Avneesh Singh's caveat ("10–20 page HTML is OK; longer might take too long") and GitHub #1773 ("too slow for low-performance PC") mean a 150-page paper with thousands of equations needs a plan (content-visibility, lazy MathML rendering) that doesn't break find-in-page or AT heading navigation. Flag for the engineering spec, not the mockup.

**22. Keyboard shortcuts (research Q24) — absent, fine, but reserve the keys.**
Next/prev section, jump-to-references, `?` overlay are push-list items. Don't need them in this mockup, but the citation popover and TOC already claim Esc behaviors — worth one inventory now so shortcuts don't collide later.

---

## On the research itself

**The 71 open GitHub issues are the most current signal you have, and they're unanalyzed.** The closed-issue synthesis is dominated by the banner era — a resolved problem class. The open set postdates it and reflects friction in the thing you're actually redesigning. I'd synthesize those before the reader mockup freezes.

**The interview corpus is 2022–23, pre-HTML-launch, and the priorities doc leans on it as if current.** Part F of the synthesis already lists 18 claims needing verification (MathML Core browser support, NVDA/JAWS+MathCAT behavior, crossref DOI display rec, MathJax v4…). Several directly shape mockup decisions (e.g., the no-MathJax posture). Worth a focused half-day verification pass against 2026 reality — the Ginev et al. paper (arXiv:2605.16562) probably settles the math-stack items.

**Author disambiguation has a provenance wrinkle.** It's ranked #4 leverage and accessibility-priorities.md marks it "validated" citing Singh, Sert, Arca Sedda, Dalla Bontà — but the interview synthesis itself marks it SILENT (Part B #22); the voices are all CSV/survey. The conclusion still stands (the CSV evidence is strong), but "validated" tags in the priorities doc silently mix datasets with very different characters. Suggest tagging each validation with its source dataset — it changes how much weight a future reader should give it.

**The mobile evidence is mostly 2019.** The big mobile cluster comes from the responsive-abs survey seven years ago, pre-HTML-reader. Phone reading of papers is now plausible in a way it wasn't ("it would make it more likely to read papers on my phone" was a *wish* in the data). Fresh mobile testing of the reader will tell you more than that cluster can.

**The BPS design comments have a sampling quirk worth remembering:** they emerged from an AI question, so they over-sample AI-anxious users. The themes that repeat across other datasets (search, author identity, filenames) are safe; the one-offs less so. Relatedly: multiple BPS voices ask for **AI-disclosure labeling on the abstract page**, and arXiv policy seems headed somewhere. The metadata `<dl>` is the natural slot — no design needed now, but confirm the block stays extensible (research Q19 already flags color-independence rules for any future badge).

**Silences to treat as gaps, not absence of need** (the syntheses say this; echoing the two that bear directly on these mockups): low-vision users at high zoom (marginalia, popovers, scroll-close behavior) and motor/dexterity users (hover-reveal chips, 44×44 targets). Both are recruit-before-promote for the reader's interaction layer specifically.

---

## If I had to pick five

1. Fix the verified defects (#1–5) — they're cheap and they're the difference between claiming the accessibility posture and having it.
2. Restore an upward path + prev/next on the abstract page (#6) — the only top-10 item with no answer in the mockup, and a heavy-user regression risk.
3. Wire the citation chips' AT layer to the push list (#16) and decide the skim-toggle tension explicitly.
4. Un-justify the reader's body text (#15).
5. Synthesize the 71 open GitHub issues before freezing the reader.
