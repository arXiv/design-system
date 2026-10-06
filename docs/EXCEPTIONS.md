# Deliberate exceptions

Places where a page departs from a rule in the docs on purpose. Each was confirmed by the design lead. An agent that finds one of these is not looking at an error and does not change it. In the code, each one has a comment beside it: `<!-- exception: <name>, see docs/EXCEPTIONS.md -->`.

When an exception ends, remove its entry and the code that goes with it.

## back-to-abstract

- **What:** a Back to abstract link above the identity line on an HTML paper.
- **Rule it departs from:** papers.html, Full papers: "The identity line comes first."
- **Why:** readers are used to arriving at the abstract page first. The link helps them make the change to the HTML paper.
- **Ends:** after phase 1 of the HTML papers.
- **Form:** `.ds-btn.ds-btn-text` with `arrow-left.svg` and the words "Back to abstract".
