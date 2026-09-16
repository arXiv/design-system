# Spec — the membership dashboard

Written from the two
screenshots in `mockups/public/membership-dashboard/`. This is the written
brief for **item 17, the v1 exit test**: an agent builds these two pages from
this text alone, without referencing the screenshots, using the design system and **no custom CSS**. 

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
3. Display an affordance for logged-in staff users only, that will take them to the Admin management page for members. 

### Structure

- The standard signed-in **site header**: wordmark on the left, standard header navigation, and standard account info on the right.
- **Page title** and one line of lede saying what the page is for.
- A **search field** below the title and intro, but above other content, labelled, that will filter the list as the reader types. It is the primary control on the page and should read that way.
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
- The display must be responsive and fluid.

---

## Page 2 — Admin view

**Route:** `/membership/admin` · **Title:** `Admin view`

### What it must do

1. Show **who currently has access**, searchable and filterable by institution.
2. Show member **invitations** in three states — open, expired, historical.
3. Let staff **remove someone's access**, and **mark someone as a manager**.
4. Let staff **export the current view** as CSV.

### Structure

- The same site header.
- **Page title.**
- An **invitation status filter**: all invitations, live invitations, expired invitations,
  historical invitations.
  - **Two more filters**: a text search for people names, and an institution
  chooser.
- An **export control** for the current view.
- A **table** of the current view. For all users, the columns are:
  user ID, family name, given name, email, institutions, ROR ID, is manager (binary status),
  and actions like edit or delete.
- **Row count and filter summary**, so the reader knows whether they are looking at 12 rows or 1,200, and whether a filter is applied. No pagination needed, just display all relevant rows each time.

### Miscellaneous Rules

- **Only sort by columns where sorting means something.** Sort controls on
  every column, including actions, is noise; each one is also a tab stop.
- **Removing access is destructive and irreversible from this screen.** It
  takes the destructive tier and a confirmation step naming the person and the
  institution.
- **A person's email is a link that mails them**; an institution's name links to
  its report; a ROR ID links to ROR. All three take the link treatment — none
  of them keeps the browser default.
- **Long institution names wrap inside their cell** rather than widening the
  table. 

---

## Sample data

Use these real values when building the pages:

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
