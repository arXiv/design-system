# Scoring notes — the membership dashboard exit test

**The builder never sees this file.** It holds the two things that belong to
the test rather than to the brief: what we already know is wrong with the
current design, and what we predict the run will expose. Both were in the spec
until 2026-09-16; Shamsi moved them out, which is right — a brief that tells a
builder what it expects them to fail is not measuring anything.

Pre-registered before the run so we cannot rationalise the result afterwards.

## What the screenshots do that a correct build must not

If the build reproduces any of these, it copied the screenshots rather than
reading the spec — which is why the spec now says to build without looking at
them.

1. **Access Lime on a public page.** The "Admin View" button on page 1 and
   "Export CSV" on page 2 use the internal-tools accent. Page 1 is public, so
   its controls are Open Blue. DESIGN-POLICIES has the rule for exactly this
   case: a privileged control on a public page stays public, because the accent
   answers *where am I*, not *what may I do*.
2. **Default browser link colours** on the emails and ROR links.
3. **A heading in link blue** — "All Users with Access" is a heading, and
   colouring it like a link says it is one.
4. **Title Case headings.**
5. **A full-size destructive button on every row**, with no confirmation.
6. **Sort affordances on columns that do not sort**, actions included.
7. **Uneven card heights** in the institution grid.
8. **No route back** from the admin view to the reports.

## Gaps we predict the run will find

- **There is no tab component.** Page 2's invitation-status filter is the
  natural place for one and `.ds-tabs` does not exist. Whatever the builder
  does instead is the finding. **Do not build `.ds-tabs` before the run.**
- **No confirmation-dialog pattern for a destructive row action**, though
  `.ds-modal` exists and should be enough to compose one.
- **No empty-state pattern** documented anywhere.
- **No row-count or filter-summary convention**, which page 2 asks for by name.
- **No documented "edit" action for a table row** — the spec asks for edit as
  well as delete, and only delete has a tier.

## What the spec deliberately does not say

Shamsi removed the cross-cutting requirements — responsive to 320px, dark mode,
200% text zoom, keyboard completeness, accessible names that say what a control
does. **That absence is itself the test.** Those are in DESIGN-POLICIES and on
the pattern pages; if a brief has to restate the accessibility floor for a
builder to meet it, the design system has failed to carry it. Score them as
requirements even though the spec does not list them.

## How to run it

1. **Page 1 first, with no build skill in place**, so the result measures the
   documentation alone.
2. Then item 9, the build and audit skills.
3. **Page 2 with the skills**, and compare — the difference is what the skills
   are worth.
4. Re-run the token-burn battery (item 31), which has not run since July. That
   harness measures regression against a known baseline; these pages measure
   coverage of things never tried.
