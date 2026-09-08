# Tier 1 as the trunk — stylesheet consolidation proposal

Status: **proposed**, and this version supersedes the earlier "extract a shared
`tokens.css`" framing. Shamsi's reading of the three-tier model (2026-09-08) is
the better one and the measurements below support it. Recorded because the two
framings lead to different work.

## The model

- **Tier 1 — `design-system.css`.** Nearly all of the CSS: tokens, foundation,
  and every component more than one surface could use. Loaded by everything.
- **Tier 2 — one per surface.** A thin file holding that surface's accent tokens,
  the handful of genuine overrides, and the components that exist only there.
  - staff tools: the `.btn-*` family, tables, metadata panels, segmented
    controls, toggles, type badges, info cards
  - the HTML papers reader: marginalia, the equation and figure regions, the
    contents bar
- **Tier 3 —** the mockup, for anything still moving.

A repo loads tier 1 plus at most one tier 2. The search pages load tier 1 alone.
The admin console loads tier 1 + the staff tier 2. The HTML papers repo loads
tier 1 + the reader tier 2. **No naming differences anywhere** — one class name
and one token name per thing, across all of it.

This is what the three-tier model in HANDOFF.md meant; the earlier proposal in
this file treated the two stylesheets as peers and only tried to share their
tokens, which is a smaller and less useful change.

## Does the code support it? Measured 2026-09-08

**Class inventory.** Public declares 96 classes, staff 84, and **25 names appear
in both** — `.ds-alert*`, `.ds-tag*`, `.ds-field`, `.ds-input`, `.ds-label`,
`.ds-hint`, `.ds-check`, `.is-invalid`, `.field-error`, `.is-sr-only`,
`.ds-close`. Those 25 are today maintained as two copies.

The 59 staff-only classes are the ones the model predicts: `.btn-*`, `.ds-table*`,
`.ds-meta-panel*`, `.seg-*`, `.toggle-*`, `.type-*`, `.info-card*`, `.ds-filter`,
`.sim-*`. Genuinely staff-surface components. Nothing there argues for a second
copy of anything shared.

**How different are the 25 duplicated components, really?** Comparing every
shared selector's declarations, then normalising the token *names* against the
synonym map (`--arxiv-surface` ↔ `--surface`, `--arxiv-error-bg` ↔ `--error-bg`,
and so on — pairs already verified to hold identical values):

> **Of 44 shared selectors, 36 are identical once the token names are
> normalised. 8 differ.**

And of those 8:

| Selector | Difference | Verdict |
|---|---|---|
| `a.ds-tag:hover` | public washes blue (`--arxiv-active-bg`), staff washes grey (`--grey-active-bg`) | **real** — per-surface accent |
| `.ds-tag--chrome` | public uses the popover tint tokens, staff uses the info tokens | **probably real**, worth a look |
| `.ds-alert` | `gap: 8px` vs `11px` | drift |
| `.ds-tag` | `gap: 8px` vs `5px` | drift |
| `.field-error` | staff sets `font-size` and `margin`, public does not | drift |
| `textarea.ds-input` | public sets `display: block`, staff does not | drift |
| `.ds-close` reduced-motion | equivalent rules written in different places | not a difference |

So the answer to "is this realistic" is: **yes, and by a wider margin than
expected.** One genuine per-surface difference, one likely second, six accidents.
The two files are not two designs. They are one design typed twice, and the
second copy has been quietly rotting.

**Evidence it is already rotting.** `--arxiv-grey-dis` is `#5a554f` in dark mode;
`--grey-dis` is `#484340`. Same concept, different value, nobody decided it. No
check could catch this: `check-drift.py` compares token *names*, and these are
two different names, so it sees two unrelated tokens rather than one that
disagrees with itself.

## The one decision left, and it is smaller than the last version of this file said

Class names need no decision — both stylesheets already say `.ds-*` for
everything shared.

Token names do. Under this model the staff sheet stops declaring
`--surface` / `--text` / `--canvas` at all and uses tier 1's names. The question
is only which prefix convention tier 1 keeps:

- **Keep `--arxiv-*`** (recommended). These names are already quoted in
  `color-mapping.md`, in both mockups, and in the blog theme, which lives in
  another repo. Renaming them has a blast radius outside this repo that we cannot
  see. Cost: the staff-only tokens either get the prefix too — `--arxiv-lime`,
  `--arxiv-danger` — or the file ends up mixing conventions. Recommend prefixing
  everything, for one rule with no exceptions.
- **Drop the prefix.** Shorter and reads better, and there is only one system, so
  a prefix earns less than it used to. But it breaks external references.

## Two things to know before starting

**Tier 1 gets loaded whole.** A staff tool would pull in the public site header,
footer, announcement band and skip link. At roughly 120KB uncompressed that is not
a performance problem, but it does mean a staff tool *could* render the public
black bar by accident. That is a governance question — a note in tier 2 and in
AGENTS.md, not a technical obstacle.

**The button system is where the payoff shows.** The staff `.btn-icon` is the same
shape as the new `.ds-btn-icon` with a rest-state border and colour variants baked
in. That border is not part of being icon-only; it is what the staff quiet tier
looks like, since `.btn-tertiary` drops the fill and keeps a border where public
`.ds-btn-text` drops the border. Under this model that control is *tertiary + the
icon shape*, and stops being a separate component. The same collapse is available
for `.ds-alert`, `.ds-tag`, `.ds-field` and the rest of the 25.

## Agreed sequence (Shamsi, 2026-09-08)

**Do this after the token rename, not before.** The two stylesheets use different
names for the same colours, so merging them means picking one set anyway; doing
both in one pass produces a diff nobody can review, in a repo with several
concurrent editors. Rename first, then this.

## Suggested order

1. **Agree the token-name convention.** The only step needing Shamsi. Reversible,
   costs nothing, and blocks everything else.
2. **Fix the six drifts** listed above, in place, before moving anything. Moving
   code and changing it in the same step makes the diff unreviewable.
3. **Move the 25 shared components** into tier 1; delete the staff copies; leave
   the two real differences behind as tier 2 overrides.
4. **Re-point the accent.** Staff tier 2 redeclares the accent tokens at `:root`
   and wins by source order — the mechanism `.ds-site-header--light` already
   proves. Access Lime as primary becomes a token decision, not a stylesheet one.
5. **Then the button system**, which is the largest single block and the one with
   the most to gain.

Steps 3–5 want the modal and the toggle to exist first: they are the next two
components that must work on both surfaces, and they are the real test of whether
the token layer carries the load.

## Not in scope

The blog theme's bundled copy. Separate project, translated deliberately;
`check-drift.py` reports its differences as a NOTE and that list is an agenda, not
a defect.
