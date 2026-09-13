# Spec — the membership dashboard

**Status: draft for Shamsi's correction, 2026-09-13.** Written from the two
screenshots in `mockups/public/membership-dashboard/`. This is the written
brief for **item 17, the v1 exit test**: an agent builds these two pages from
this text alone, using the design system and **no custom CSS**.

Because the test measures the design system rather than the builder, the brief
says what each page must *do*, not what the screenshots look like. Where the
screenshots depart from arXiv policy, this says so and says what to build
instead — copying a defect would test the wrong thing.

---

## What this is for

arXiv's institutional members pay for membership and want to know what they get
for it. The dashboard answers that: a member representative signs in, finds
their institution, and reads its report. A small number of arXiv staff also
need to see who has access and to grant or remove it.

Two pages, two audiences, and the difference matters more than it looks:

| | Institution reports | Admin view |
|---|---|---|
| Who | Member representatives — librarians, research office staff | arXiv staff and member managers |
| Surface | **Public.** Open Blue accent | **Internal tools.** Access Lime accent |
| Frequency | A few times a year | Daily, for some people |
| Failure mode | Cannot find their institution | Removes the wrong person's access |

---

## Page 1 — Institution reports

**Route:** `/membership/reports` · **Title:** `Institution reports`

### What it must do

1. Let a signed-in representative **find their institution** among roughly a
   thousand, by typing part of its name.
2. Let them **open its report**.
3. Show staff a way through to the admin view, without implying that everyone
   has one.

### Structure

- The standard signed-in **site header**: wordmark, and the account slot with
  the reader's given name and an account link.
- **Page title** and one line of lede saying what the page is for.
- A **search field**, labelled, filtering the list as the reader types. It is
  the primary control on the page and should read that way.
- A **grid of institution cards**, alphabetical. Each card carries:
  the institution's name, its country, and its ROR identifier.
  The whole card is the target that opens the report.
- **Empty state:** when the search matches nothing, say so in words and offer
  the way back (clear the search). Never an empty grid with no explanation.

### Rules

- **Cards in a row are the same height**, whatever the name length. Two of the
  names in the sample data run to four lines; the grid must not become ragged.
- **The ROR identifier is an identifier**, so it is set in mono and copied
  exactly — never re-cased, never truncated mid-string. If it must be shortened
  visually, the full value stays available.
- **One target per card, not three.** A card containing three separate links is
  three tab stops that all go to the same place.
- Sort alphabetically by the name as displayed, and say that it is alphabetical.

---

## Page 2 — Admin view

**Route:** `/membership/admin` · **Title:** `Admin view`

### What it must do

1. Show **who currently has access**, searchable and filterable by institution.
2. Show **invitations** in three states — open, expired, historical.
3. Let staff **remove someone's access**, and **mark someone a manager**.
4. Let staff **export the current view** as CSV.

### Structure

- The same site header.
- **Page title.**
- A **set of four views** — all users, all invitations, expired invitations,
  historical invitations. Only one is shown at a time.
- An **export control** for the current view.
- **Two filters side by side**: a text search over people, and an institution
  chooser.
- A **table** of the current view. For all users, the columns are:
  user ID, family name, given name, email, institutions, ROR ID, is manager,
  and actions.
- **Row count**, so the reader knows whether they are looking at 12 rows or
  1,200, and whether a filter is applied.

### Rules

- **Only sort by columns where sorting means something.** Sort controls on
  every column, including actions, is noise; each one is also a tab stop.
- **Removing access is destructive and irreversible from this screen.** It
  takes the destructive tier and a confirmation step naming the person and the
  institution. A red button repeated on every row of a long table is a mis-click
  waiting to happen, and it makes the whole table look like an alarm.
- **"Is manager" is either editable or it is not**, and it must look like
  whichever it is. If it can be changed here, it is a control with a label and
  it reports what changed. If it cannot, it is a yes/no value, not a checkbox.
- **A person's email is a link that mails them**; an institution's name links to
  its report; a ROR ID links to ROR. All three take the link treatment — none
  of them keeps the browser default.
- **Long institution names wrap inside their cell** rather than widening the
  table. The sample data contains a five-line name.
- **Empty state per view.** "No expired invitations" is a useful sentence; an
  empty table is not.

---

## Both pages

- **Responsive to 320px.** The table scrolls horizontally inside its own
  container; the page never does.
- **Dark mode**, following the OS and overridable by the reader's own choice.
- **200% text-only zoom** without clipping or overlap.
- **Keyboard-complete.** Every control reachable and visibly focused; the
  confirmation step traps focus and returns it on close.
- Every control's accessible name says what it does, not where it is:
  "Remove access for Marina Werbeloff", not "Remove access".

---

## Sample data

Use the real values from the screenshots — they are the good stress test.

**Institutions:** Aalto University (Finland, ror.org/020hwjq30) · Abo Akademi
University (Finland, 029pk6x14) · Adelaide University (Australia, 028g18b61) ·
Ames Laboratory (United States, 041m9xr71) · Argonne National Lab (United
States, 05gvnxz63) · Australian National University (Australia, 019wvm592) ·
Bibliothèque Diderot de Lyon (École Normale Supérieure de Lyon / ENS Lyon)
(France, 04zmssz18) · Big Ten Academic Alliance (United States, 02ntfsb56)

**Users:** 446345 Werbeloff, Marina · werbeloff@fas.harvard.edu · Harvard
University · ror.org/03vek6s52 · not a manager — 939007 Pan, Jianhao ·
1604134186@qq.com · DESY (HGF - Helmholtz Association, German Research Centers)
· ror.org/01js2sh04 · manager — 186092 Köhler, Martin · martin.koehler@desy.de ·
DESY · ror.org/01js2sh04 · not a manager

The sample is deliberately awkward and should stay that way: a five-line
institution name, a diacritic in a surname, and an email that is a string of
digits.

---

## What the screenshots do that the build must not

Recorded so the test is not scored against a copy of the current design.

1. **Access Lime on a public page.** Both the "Admin View" button on page 1 and
   "Export CSV" use the internal-tools accent. Page 1 is public, so its
   controls are Open Blue — and there is a rule for exactly this case: *a
   privileged control on a public page stays public* (DESIGN-POLICIES, settled
   2026-09-08). The accent answers "where am I", not "what may I do". Signal
   the privilege in the wording instead.
2. **Default browser link colours.** Emails and ROR links render in the
   browser's blue and purple, not arXiv's link tokens.
3. **A heading in link blue.** "All Users with Access" is a heading, and
   colouring it like a link says it is one.
4. **Title Case headings.** Sentence case, per the docs convention.
5. **A full-size destructive button on every row**, with no confirmation.
6. **Sort affordances on columns that do not sort**, actions included.
7. **Uneven card heights** in the institution grid.
8. **No visible page-level navigation back** from the admin view to the reports.

---

## Gaps this will find — predicted before the run

Recorded now so the test measures the system rather than our memory of it.

- **There is no tab component.** The four views on page 2 need one and
  `.ds-tabs` does not exist. Either the builder invents one — which is a
  finding — or the spec's "set of four views" is satisfied some other way,
  which is also a finding. **Do not build `.ds-tabs` before the run.**
- **There is no confirmation dialog pattern for a destructive row action**,
  though `.ds-modal` exists and should be enough.
- **There is no empty-state pattern** documented anywhere.
- **There is no row-count or result-count convention.**
- **Dark mode on internal tools** is being added now; if it is not finished
  before the run, page 2's dark requirement will fail and that is the honest
  result.

Run **page 1 before the build/audit skills exist**, so we see what the docs
alone produce. Then page 2 with the skills, and compare.
