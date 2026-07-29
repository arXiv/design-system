The file is complete and correct. The demo page is at `docs/public/withdrawn-notice-styles.html`.

---

## Design rationale

Here is a summary of the decisions made and the guidance they trace to:

**1. Warning alert (`ds-alert-warning`), not error**
`alerts.html` defines warning as "advisory amber — 'worth knowing, nothing broke.'" Withdrawal is not misconduct, and the vast majority are honest scholarly corrections. Using error-red (`.ds-alert-error`) would mislabel both the paper and its authors. Using info-blue would undersell the notice for a reader arriving cold from a citation. Amber is precisely calibrated: immediately visible, clearly significant, free of accusation.

**2. Placed in the main column, between the version row and the abstract**
`alerts.html` placement rule: "Time-critical messages live in the main reading column where every reader meets them — the older-version warning sits under the title; don't tuck a warning into a rail the reader may never open." A reader following a citation has no context; they read title → then abstract. The notice intercepts that path before they process a word of the abstract. `organizing-content.html` reinforces: never put must-see information only inside a closed accordion.

**3. `role="alert"` (assertive)**
Per the alerts semantics table: `role="alert"` is for warning/error states — announced immediately by screen readers. A screen-reader user deserves to hear "Withdrawn" before the abstract is read to them.

**4. Tone: factual, attributed, non-accusatory**
`BRAND.md` Voice: "Honest, plainspoken, no marketing gloss." The copy says "The authors withdrew this submission" — active voice, attributed to them, no arXiv editorializing. The reason is labeled "Authors' stated reason" to keep their voice distinct from arXiv's. No exclamation marks, no alarm, no hedging.

**5. Author reason inside the alert, in an attributed sub-block**
The reason is short and exactly what a citing reader needs. Hiding it behind a disclosure adds a click without benefit. The `.wdr-reason` sub-block uses `currentColor` for its left border — inheriting the ambient warning amber with no new hex value, no new token, entirely derived from documented values. The condensed-caps label follows the metadata-label grammar already established throughout the system.

**6. Downloads remain enabled and unmodified**
The content is still downloadable (the scholarly record is preserved). `AGENTS.md`: "Actions disable, they don't disappear." Scholars verifying a citation need the PDF. The alert alone communicates the paper's status — no redundant markers on the buttons.

**7. No additional withdrawal signal on the title or download buttons**
`BRAND.md` §1: "The interface gets out of the way." The alert, placed precisely between the version row and the abstract, carries the full weight of the signal. Decorating the title heading or each download button would produce anxious, defensive UI — the dark-pattern register arXiv specifically rejects.