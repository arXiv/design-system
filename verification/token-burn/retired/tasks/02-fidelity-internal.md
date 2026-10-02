You are a frontend developer contributing to the arXiv design-system repo (the current working directory). Follow the repo's own contribution guidance.

The arXiv Check moderation team needs a **bulk-action bar** for the moderation queue: when a moderator selects one or more submissions in the queue table, a bar appears offering actions on the selection. Requirements from the tool's product owner:

- Shows the selection count ("3 submissions selected") and a "Clear selection" affordance.
- Three actions: **Approve selected** (the common, safe action), **Put on hold** (neutral), and **Remove selected** (destructive — moderators occasionally fat-finger this, so treat it accordingly).
- The bar sits directly above the queue table and must be visually connected to it.
- Must include a message state for when an action completes ("3 submissions approved") and one for when an action fails.

Deliverable: a single demo HTML page at `docs/internal/bulk-action-styles.html` that renders the bar in its states (nothing selected / selection active / success / failure), reusing this repo's existing components and styles wherever they already exist rather than inventing new ones. Page-specific glue CSS may live in the page's own style block per repo convention.

Do not run git commands, do not start servers, and do not modify files unrelated to this task. When you are done, summarize what you built and every design-system rule you applied, as your final message.

---
Scope and output rules (battery v2):
- Render ONLY what this task asks for. Stage it inside a plain neutral shell (a simple grey placeholder frame is fine); do NOT build site chrome — headers, footers, sidebars, logos — unless the task explicitly asks for them.
- Your final message: at most 10 short bullet lines.
