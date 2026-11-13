# Next steps

Open items only. Finished items are removed; the git history keeps them. The current state of the work and the working rules are in `HANDOFF.md`.

## Decisions for Shamsi

- **The direction for the Papers rules:** three to five rules per section for people; the detail in each demo's class key; LaTeXML-specific rules moved to the renderer.
- **DESIGN-POLICIES duplicates:** `design-policies-audit-2026-10-13.md` proposes one or two sentences per rule, with a link to the page that holds the detail. It also lists errors to fix whatever is decided (button padding, `.btn-tertiary`, a doubled token name).
- **The spacing scale:** is it too sparse in the middle? Deferred 2026-09-16 by Shamsi: judge it in a real page, not from a frequency table.
- **The process trial** in `process-proposal.md`: what to keep. Since 2026-10-15 there are no new-prose lists; Shamsi reviews prose on the pages.
- **Brand metrics**, with leadership: the promise and proxy table is in `proposals/brand-metrics-brainstorm.md`.
- **One padding for every tinted band:** a band in the middle of a page would go from 48px to 32px, which removes two special rules. Show a before and after first.
- **The tokens with "grey" in their names** (`--ds-grey-*`, `--ds-library-grey`): rename them to American spelling or not. Builders already use them, and renames are free only until the first version is tagged.
- **The Smileybones description:** a serial comma in "ease of use, and brand fidelity", and a space after the ellipsis ("rules… or").
- **What an older version's page shows:** whether version 1's page shows a journal reference the paper gained later (round 12).
- **Citations on a paper's page** (round 12): a worked citation in the docs; which version an older version's citation names; whether a citation style may change the title's capitals, against "show the author's text as written".

## Docs

- **Pages not yet reviewed:** brand.html, outreach.html, index.html. papers.html and search.html were reviewed on 2026-10-06 but are not yet in `verification/reviewed-pages.txt`, so they have no digest.
- **When a sidebar beats the bottom of the page:** a docs example (from round 6).
- **A shared popover script,** like `tooltip.js`. Agents write their own opening code or avoid popovers.
- **references.html interactivity,** deferred until agents do the basics well: citation and footnote markers in the text, Jump to reference and Back to your place, from the behavior in `html-phase1.html` (comment block 9). Questions to settle then: ship `popover.js` and `references.js`; footnotes on a wide screen as a CSS margin note or the mockup's marker; whether LaTeXML's "Cited by" and "External Links" belong in a popover's copy; renaming Papers' "Citations and references". The mockup's CSS fades ignore reduced motion, its return wash is color only, its footnote popover needs Escape and scroll, and `.ds-paper-element:target` removes the outline.
- **From the V1 review, not needed for V1:** a "Not in this version" list in the release notes; patterns for an action in progress, an empty table and file upload; one set of breakpoints, in rem; prefixing the five form-message classes (`field-error` and the rest) before the first tag; "notice" or "alert"; the header divider class beside `.ds-divider--vertical`; one base focus ring; a check that a tagged version never loses a class.
- **Spacing outside a paper in a list:** the data list and the tag list space themselves only inside `.ds-paper`, so used anywhere else they touch (round 12).
- **Accordions in a sidebar:** Layouts puts several in a `.ds-acc-stack`; the sidebar on Papers puts them straight into the section (round 12).
- **Header:** at phone width the menu stays open behind the search overlay; step 3 of the centered space's fold (links fold into the menu) is not built in `docs/header.js`.
- **Two tokens kept for the mockups:** `--ds-accent-active` and `--ds-danger-active` are read only by two admin console mockups. Delete them when those mockups stop using them.
- **Applying dates to every view** ("use these dates for all tabs"), as the live site does: where the option lives.
- **A prominent card variant:** asked for in round 5. Shamsi prefers fewer variants.
- **Brand assets page:** logos, the X mark, the smileybones and friends, in the sizes and colours needed, SVG and PNG, with usage notes. Includes the Smileybones logo when Shamsi has made it; the header text then becomes the logo, with the alt text "Smileybones".
- **The category editor** (reorderable tags, primary first, inline remove, search to add) is styled in `internal-tools.css` but has no docs section.
- **The internal palette** on `colors.html`, documented as fully as the public palette.
- **Type:** finalize the weight set; decide whether headings get a display treatment; build and measure a subsetted variable font.
- **Patterns still to build:** the author list for the 100+ author case; the Labs opt-in section.
- **`docs/examples/`:** stable full-page examples built only from documented components, starting with form validation (approved in principle 2026-10-02).
- **The abstract heading in HTML papers** (decided 2026-11-03): an `<h2>`, hidden with `.is-sr-only`, as Papers now documents. LaTeXML outputs a visible `<h6>`; ask Deyan to promote it to `<h2>`, and the page hides it. See `live-html-markup-2026-10-06.md`.
- **Old links:** notes and the mockups README still point at files removed before the October reorganisation (`docs/public/`, `metadata-panel.html`, `BRAND.md`).

## Compact elements (its own session)

- The secondary navigation at phone width wraps to two lines and is hard to read.
- The joined sort bar wraps badly at phone width.
- Other wide elements at phone width: filter bars, tables, button groups.
- **Small forms and the compact button** (added 2026-10-22): review forms; do we need a small form variant? What is the use case for the compact button (`.ds-btn-compact`, branch `compact-buttons`)? Review the activity dashboard filter bar: is that a small form, and does it use a compact button?

## Testing

- **V1, internal page:** round 9 gave the best builds yet (best D, worst B). Build D, with parts of C, is the starting point for the reference pages in `whiteboard/mockups/internal/activity-dashboard/`. V1 is not yet declared done; see `HANDOFF.md`.
- **Agents try the alternatives:** build two arrangements of the hardest placement choice and compare them, as a designer would. Test as a before-and-after pair, as in round 6, and weigh the extra tokens.
- **Cheap checks for `round.py evaluate`:** one `<main>`, a skip link pointing at it, and the standard footer (a build in round 8 or 9 left out the footer, and nobody noticed); an element written `hidden` that still shows; an inline icon wider than 48px outside a figure; every `<dialog>` opened and checked with axe again.
- **Run round 13's brief again** on the fixed docs, unchanged, as the after measure. Mark predictions 9 and 10 (selection) and the count sentence as changed by the docs, so they do not count as an improvement.
- **The test tooling** (`round.py` and its review and report pages) is on local commits only: a PR once Shamsi is happy with it.
- **arXiv Check, in React.** Shamsi takes screenshots first. See `TESTING-PLAN.md`.
- **The build and audit skills:** thin routers into the docs, never a second copy of the system. Not needed for V1.
- **User testing of the paper mockups** (`abstract-phase2.html`, `html-phase1.html`): script, tasks, recruitment (working researchers first). Parked questions are in `whiteboard/planning/accessibility-research-questions.md`.

## Mockups

- **Rebuild the paper mockup's structure** (`html-phase1.html`) so the layout is ours rather than what ar5iv emits. This also fixes a known failure: at 1280px the mockup fails text-only zoom, because ar5iv's body grid is sized by its content (noted in `verify-mockups.py`).
- **Reconcile the mockups with the docs** (`html-phase1.html`; the abstract page mockup is out of date): the Permalink pill, line height, the figure viewer caption, removing "Who cites this", and the author list from arXiv's metadata (LaTeXML's author blocks are not one per person).
- **Admin console mockups:** px font sizes still to convert to rem, with the internal tools work (noted by `check-policies.py`).

## Accessibility

- **Is a closed accordion "visible"?** The Accessibility accordion in the paper sidebar stays closed for now.
- **One general set of accessibility rules** in the design system, informed by the HTML papers work, with paper-specific decisions living with the renderer. `accessibility-priorities.md` (paper-page decisions) moved here from docs/ in November 2026, out of the general docs menu.

## For Deyan

From the V1 review, 12 November 2026.

- **Publish by rule:** every `docs/*.css` except docs.css, every `docs/*.js` except marked.js, and the logos. Today the static route has only design-system-components.css, the fonts and the chrome scripts, so design-system.css, internal-tools.css, theme.js, the shared scripts and the internal logos return 404. Then using.html names the route once and the two stylesheets by role.
- **`latest` is behind and unmarked:** it was built on 21 October. The next publish removes classes and tokens, while `templates/README.md` promises additive changes only.
- **Publishing is manual:** every CI publish run is skipped (no credentials), but the docs say merges publish at once, and `BANNER_ANNOUNCEMENTS.md` promises five minutes.
- **The GitHub Pages docs site** has been stuck since 9 November, after two build errors.
- **CI is not a gate:** there are no required status checks. `upload_static_assets.py` cannot import on Python 3.9, so two checks cannot run on Shamsi's Mac.
- **Licensing:** MIT appears to cover the photos, portraits, funder logos and campus photos; the IBM Plex OFL text is missing; `tex.svg` is Font Awesome, not Lucide, and is not credited.
- **Header scripts:** `docs/header.js` disables the template's hamburger when both load; `chrome/header.js` wires the page's first header, not its own; Ctrl+K leaves the phone menu open; the fold depends on when the fonts load; without JavaScript the Search link is still announced as a collapsed disclosure.
- **Shared scripts:** they break when loaded twice and ignore content added later; they start in three different ways; `copy.js` throws when not deferred; `tooltip.js` throws on Escape on a host with no bubble.
- **Versioning:** a git tag names a reviewed state of the docs, classes and tokens, with a `version.txt` on the route and release notes from merged PR titles; a check fails if anything a tag shipped is removed. Make every deletion and rename before the first tag.
- **Repo weight:** 52 of 65 woff2 files are never declared, the June audit screenshots are 11 MB, and an npm git install downloads 60 MB.
- **The announcements file** needs a field to choose the band's color variation (maintenance, event). Messages says it does not exist yet.
- **The abstract heading in HTML papers:** promote LaTeXML's `<h6>` to `<h2>` (see Docs above).

## Later, against real content

- Data visualisation: charts, meters, legends.
- User portal and Admin Console mockups.
- An agent pointer file other arXiv repos could include, naming the design system docs as the reference for look and feel, so agents stop copying sibling services.
