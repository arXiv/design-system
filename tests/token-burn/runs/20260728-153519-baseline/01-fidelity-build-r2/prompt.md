You are a frontend developer contributing to the arXiv design-system repo (the current working directory). Follow the repo's own contribution guidance.

Build a new public-side pattern: a **"Dataset & code links" card** for the abstract page. Product context: papers increasingly ship with datasets and code repositories, and readers asked for one obvious place to find them. Requirements from the product owner:

- A card that lists a paper's external research artifacts (datasets, code repositories, supplementary material), each row showing: an artifact label (e.g. "Training data"), the destination (e.g. "Zenodo", "GitHub"), and the link itself.
- The card appears on public abstract pages. It must read as browsable supplementary material, not as a primary call to action.
- Rows must clearly signal they lead off-site.
- It must work with 1 artifact and with 12 artifacts without breaking the page (decide and document how many rows show before any overflow handling kicks in, and what that handling is).
- Include hover and keyboard-focus treatment for the rows.

Deliverables:
1. The component CSS added where this repo says shared public components belong, following the repo's conventions for naming, tokens, and documentation.
2. A demo/reference HTML page at `design-patterns/public/artifact-links-styles.html` showing the card's states and variants, following the structure of the existing reference pages.

Do not run git commands, do not start servers, and do not modify files unrelated to this task. When you are done, summarize what you built and every design-system rule you applied, as your final message.
