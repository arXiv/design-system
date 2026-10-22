# Next steps

Open items only. Finished items are removed; the git history keeps them. The current state of the work and the working rules are in `HANDOFF.md`.

## Decisions for Shamsi

- **The abstract heading level**, from Deyan's answers in `live-html-markup-2026-10-06.md`.
- **The direction for the Papers rules:** three to five rules per section for people; the detail in each demo's class key; LaTeXML-specific rules moved to the renderer.
- **DESIGN-POLICIES duplicates:** `design-policies-audit-2026-10-13.md` proposes one or two sentences per rule, with a link to the page that holds the detail. It also lists errors to fix whatever is decided (button padding, `.btn-tertiary`, a doubled token name).
- **The spacing scale:** is it too sparse in the middle? Deferred 2026-09-16 by Shamsi: judge it in a real page, not from a frequency table.
- **The process trial** in `process-proposal.md`: what to keep. Since 2026-10-15 there are no new-prose lists; Shamsi reviews prose on the pages.
- **Brand metrics**, with leadership: the promise and proxy table is in `proposals/brand-metrics-brainstorm.md`.

## Docs

- **Pages not yet reviewed:** brand.html, outreach.html, index.html. papers.html and search.html were reviewed on 2026-10-06 but are not yet in `verification/reviewed-pages.txt`, so they have no digest.
- **When a sidebar beats the bottom of the page:** a docs example (from round 6).
- **A shared popover script,** like `tooltip.js`. Agents write their own opening code or avoid popovers.
- **Applying dates to every view** ("use these dates for all tabs"), as the live site does: where the option lives.
- **A prominent card variant:** asked for in round 5. Shamsi prefers fewer variants.
- **Brand assets page:** logos, the X mark, the smileybones and friends, in the sizes and colours needed, SVG and PNG, with usage notes. Includes the Smileybones logo when Shamsi has made it; the header text then becomes the logo, with the alt text "Smileybones".
- **The category editor** (reorderable tags, primary first, inline remove, search to add) is styled in `internal-tools.css` but has no docs section.
- **The internal palette** on `colors.html` and in `color-mapping.md`, documented as fully as the public palette.
- **Type:** finalize the weight set; decide whether headings get a display treatment; build and measure a subsetted variable font.
- **Patterns still to build:** the author list for the 100+ author case; the Labs opt-in section.
- **`docs/examples/`:** stable full-page examples built only from documented components, starting with form validation (approved in principle 2026-10-02).
- **Old links:** notes and the mockups README still point at files removed before the October reorganisation (`docs/public/`, `metadata-panel.html`, `BRAND.md`).

## Compact elements (its own session)

- The secondary navigation at phone width wraps to two lines and is hard to read.
- The joined sort bar wraps badly at phone width.
- Other wide elements at phone width: filter bars, tables, button groups.
- **Small forms and the compact button** (added 2026-10-22): review forms; do we need a small form variant? What is the use case for the compact button (`.ds-btn-compact`, branch `compact-buttons`)? Review the activity dashboard filter bar: is that a small form, and does it use a compact button?

## Testing

- **V1, internal page:** round 9 gave the best builds yet (best D, worst B). Build D, with parts of C, is the starting point for the reference pages in `whiteboard/mockups/internal/activity-dashboard/`. V1 is not yet declared done; see `HANDOFF.md`.
- **Agents try the alternatives:** build two arrangements of the hardest placement choice and compare them, as a designer would. Test as a before-and-after pair, as in round 6, and weigh the extra tokens.
- **A footer check:** a build in round 8 or 9 left out the footer, and nobody noticed. The evaluation could flag a page without the standard footer.
- **arXiv Check, in React.** Shamsi takes screenshots first. See `TESTING-PLAN.md`.
- **The build and audit skills:** thin routers into the docs, never a second copy of the system. Not needed for V1.
- **User testing of the paper mockups** (`abstract-phase2.html`, `html-phase1.html`): script, tasks, recruitment (working researchers first). Parked questions are in `docs/accessibility-research-questions.md`.

## Mockups

- **Rebuild the paper mockup's structure** (`html-phase1.html`) so the layout is ours rather than what ar5iv emits. This also fixes a known failure: at 1280px the mockup fails text-only zoom, because ar5iv's body grid is sized by its content (noted in `verify-mockups.py`).
- **Reconcile the mockups with the docs** (`html-phase1.html`; the abstract page mockup is out of date): the Permalink pill, line height, the figure viewer caption, removing "Who cites this", and the author list from arXiv's metadata (LaTeXML's author blocks are not one per person).
- **Admin console mockups:** px font sizes still to convert to rem, with the internal tools work (noted by `check-policies.py`).

## Accessibility

- **Is a closed accordion "visible"?** The Accessibility accordion in the paper sidebar stays closed for now.
- **One general set of accessibility rules** in the design system, informed by the HTML papers work, with paper-specific decisions living with the renderer. Shamsi is unsure about `accessibility-priorities.md` being about the abstract and HTML paper pages only.

## Later, against real content

- Data visualisation: charts, meters, legends.
- User portal and Admin Console mockups.
- An agent pointer file other arXiv repos could include, naming the design system docs as the reference for look and feel, so agents stop copying sibling services.
