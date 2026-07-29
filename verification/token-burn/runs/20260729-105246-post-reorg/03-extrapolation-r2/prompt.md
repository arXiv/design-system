You are a frontend developer contributing to the arXiv design-system repo (the current working directory). Follow the repo's own contribution guidance.

arXiv is adding support for **author-initiated withdrawal**: authors can mark their own paper as withdrawn, with a short reason. The abstract page of a withdrawn paper needs a treatment. **No pattern for this exists in the design system** — this is a new situation, and you must design it by reasoning from what the system documents about how arXiv communicates.

Facts you can rely on:
- A withdrawn paper's abstract page remains online forever (the scholarly record is never deleted); the paper content stays downloadable.
- Readers arriving from a citation may have no idea the paper was withdrawn.
- The withdrawal reason is author-written, usually one or two sentences (e.g. "an error in Section 3 invalidates the main result").
- Withdrawal is not misconduct — most withdrawals are honest corrections. Some withdrawn papers remain heavily cited.

Design questions you must answer (there is no spec — decide and justify):
- What does the reader see, where on the page, and how loud is it?
- What tone does the messaging take toward the paper and its authors?
- How does the treatment interact with the page's other elements (title, download actions, version information)?

Deliverable: a demo HTML page at `docs/public/withdrawn-notice-styles.html` showing your treatment in context (a realistic abstract-page fragment), plus — as the top section of that page — a short written rationale connecting each major decision you made to the specific guidance in this repo that motivated it.

Do not run git commands, do not start servers, and do not modify files unrelated to this task. When you are done, restate your design rationale as your final message.
