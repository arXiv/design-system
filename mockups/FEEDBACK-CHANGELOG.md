# You said, we changed it

Changes to the redesign mockups made in direct response to internal feedback, June 2026. Thank you — every item below started as one of your comments. View the results: [abstract page](public/abstract-phase2.html) · [HTML paper](public/html-phase1.html) · [design-system home](../index.html).

## On the HTML paper page

- **DOI added** to the identity line at the top — you were right that many readers land here directly without passing the abstract page. The DOI and License links now also share the standard arXiv link style.
- **Full category name shown** ("[gr-qc] General Relativity and Quantum Cosmology"), not just the code.
- **Read-aloud is real — and now it reads the math.** The "Listen" button speaks the paper using the browser's built-in text-to-speech: it starts from wherever you've scrolled to, highlights the paragraph being read, and skips citation brackets and the bibliography. After your testing feedback ("Equation 2.3 is not what a blind user needs"), equations are now genuinely spoken — "d s squared equals minus d t squared plus a squared…" — using literal (MathSpeak) rules chosen on expert advice: verbose but correct, never guessing at structure. Self-hosted, loaded only when Listen is used. Skip buttons and media-player keys (←/→ skip, Space pause, Esc stop) included. Try it!
- **Mobile table-of-contents bug fixed** — the list's end was unreachable on iPhones because of how Safari measures screen height behind the collapsing URL bar.
- **Gray references background now continues** through any appendix or acknowledgments that follow the bibliography — no jarring snap back to white (works in pure CSS, robust to varied TeX).
- **"View TeX" cleaned up** — no more code-block box, and the `\displaystyle` clutter is stripped from both the display and what Copy gives you.

## On the abstract page

- **File sizes on the download buttons** — PDF (1.2 MB) inline on one line; TeX Source shows format and size.
- **Ancillary files got their own download button** with file count and size, alongside the filename list in Paper Information.
- **Cite section reworked per your testing:** the version toggle now sits right after the "Cite this paper" heading where it gets noticed, and reads "This arXiv version." All copyable text is in real, visibly styled code blocks. BibTeX wraps with a vertical scrollbar instead of running off sideways (the formatted column too, for long author lists). The arXiv DOI now appears in every arXiv-version citation format.
- **Banner icon restored to full-color yellow.**
- **Breadcrumbs removed** — too shallow to justify the real estate, and those links live elsewhere on the page.

## Answered, and open for discussion

- The cite section's data is **hardcoded in the mockup** (it's a design prototype). Production note: the `doi.org` BibTeX route covers BibTeX only — APA/Chicago/MLA need a formatter fed from metadata.
- **"Journal article" vs "Related DOI"** label: real tension between honest metadata and a meaningful citation label — needs a team decision (options: keep "Journal article," use "Published version," or suppress the toggle when the DOI type is unknown).
- **Should the arXiv DOI replace the arXiv ID in citations?** Currently both are included — the ID is still the community's everyday identifier (ADS, INSPIRE, reviewer vernacular); the DOI adds persistence. Open to discussion.

*Every change above was verified by an automated check suite (29 browser-based tests covering reflow, accessibility, and past bug classes) before landing. Feedback always welcome — it visibly moves the work.*
