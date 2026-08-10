# Accessibility Research Questions — Public Pages

**Status:** Open — seeded 2026-07-24. Companion to `accessibility-priorities.md` (which is *decisions*); this file holds the open questions waiting on a user-testing round.

These are parked questions to put in front of assistive-technology users and researchers when the moderated-test round for `abstract-phase2.html` and `html-phase1.html` runs (see `../../planning/NEXT-STEPS.md`). Each notes where it came from. Add findings inline as rounds complete, and promote resolved ones into `accessibility-priorities.md`.

## Questions

### 1. Silent ambient orientation indicators (from PROPOSED-GUIDELINES G9)
Continuously-updating orientation chrome (current-section label, reading-progress bar, "N min left") is currently silent for AT — no `aria-live` on scroll-driven values, on the theory that AT users get equivalent orientation from headings/landmarks and can poll the progressbar on demand. **Question:** does that hold up for real screen-reader and low-vision users, or do some want an on-demand announcement of progress / current section? Test before promoting G9 from pattern convention to policy.

### 2. "Journal article vs Related DOI" label tension
The abstract page can surface both the arXiv-hosted item and a related published version. **Question:** what labels make the distinction unambiguous to AT users and newcomers without publisher jargon? Candidate labels to test, and whether the DOI should read as "published version" vs "related DOI."

### 3. Newcomer signposting after the announcement banner retires
Once the time-bound announcement banner is dismissed/retired, first-time visitors lose an obvious "what is arXiv?" entry point. **Question:** what subtle, persistent signpost orients newcomers (and glosses arXiv vocabulary — "cross-listed", "v2", "endorsement", "comments") without adding chrome for regulars? Ties to the abbr/glossing work in `accessibility-priorities.md`.

### 4. Justification & hyphenation (issues #6533, #5028)
Reconsider justified text / hyphenation settings in the HTML reader for low-vision and dyslexia-track readers. **Question:** do current defaults (and respecting user stylesheets) serve these readers, or is justified text actively harmful at zoom? Test against real user stylesheets and browser overrides.
**Dev corroboration (2026-08-07):** full justification + `hyphens: auto` flagged independently in dev review — browser hyphenation of specialized scientific vocabulary is weak (LaTeX-quality typesetting is exactly what browsers still lack), and submitters won't supply soft hyphens. Raises this question's priority.

### 4b. Permalink permanence (dev review, 2026-08-07)
The reader's anchor links to figures, equations, and sections are labeled "permalink" — a strong word for an archive. **Question:** what do they actually promise? Do they pin to a specific paper version, and do anchors survive re-renders of the same version? Decide the versioning semantics before the label ships; "permalink" must not overclaim.

## Pointers

- Decisions (not questions): `accessibility-priorities.md`
- Research syntheses and raw data: the UX research references folder (see `accessibility-priorities.md` Pointers)
- User-testing plan: `../../planning/NEXT-STEPS.md`
