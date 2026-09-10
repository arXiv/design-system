# What the HTML paper mockup asks of the design system

Audit of `mockups/public/html-phase1.html` against `docs/design-system.css`,
2026-09-10. Item 20 in the v1 plan.

Shamsi asked for this to be read **both ways**: where the page fails to use the
design system, and where the design system fails to support what the page needs.
The second half is first, because it changes what we build.

The page is 9,587 lines with 568 local CSS rules over 3,658 lines of `<style>`.
It links tier 1 and then declares 31 rules that touch a `.ds-` selector — 13
that override tier 1 and 16 that extend it. Those 29 rules are the audit: each
one is a place where a person building a real page found tier 1 insufficient and
wrote around it. None of them is arbitrary.

---

## Part one — where the design system does not support the page

### 1. Every control ignores the reader's text size

**The most serious finding, and it is not about the mockup.** Tier 1 declares 17
font sizes in `px`. Set the browser's font size to 32px — the single most common
assistive setting there is — and measure:

| | at root 16px | at root 32px |
|---|---|---|
| `.ds-btn` label | 14px | **14px** |
| `.ds-input` | 14px | **14px** |
| `.ds-label` | 13px | **13px** |
| `.ds-hint` | 12px | **12px** |
| `.ds-alert` | 13px | **13px** |
| `.ds-seg-btn` | 12px | **12px** |
| `.ds-switch-label` | 11px | **11px** |
| body text, headings, `.ds-section-desc` | scale correctly | scale correctly |

The button does not overflow. It does not change at all — 120×37px before and
after. A reader who doubled their text gets prose at 32px and a form they cannot
read while typing into it.

The pattern is exactly backwards: **prose scales, controls freeze.** Prose is the
part a reader can already fix with a user stylesheet or reader mode. A form field
is not.

`typography.html` states the rule — *"Sizes are rem, never px. Browser font-size
overrides must propagate to arXiv content… The verification harness enforces this
on the mockups."* It is enforced on the mockups and unenforced on the stylesheet,
which is the one file every page inherits.

The rule's second sentence is also part of the cause: *"Layout dimensions stay px
— only type scales."* That licensed `min-width: 120px` and `padding: 10px 20px` on
`.ds-btn`, and once the box was px the type followed. A control that holds text
needs its box to scale with the text; 88 size declarations in tier 1 are px today.

The mockup already knows: it overrides `.ds-nav-icon` from tier 1's `16px` to
`1.23em`, and `.ds-site-footer-main` from `720px` to `48rem`. Both are the same
fix, applied locally because tier 1 would not do it.

**This is item 7, and it is bigger than "write the magnification docs".**

### 2. The popover cannot hold content of unknown length

The page builds three popovers by hand — citation, footnote, table of contents.
All three take the same material as `.ds-popover`: same surface token, same
border token, same radius, same shadow. They differ in exactly three things
tier 1 does not offer:

```
width: 360px / 320px / 380px          .ds-popover has no width at all
max-height: 60vh / 50vh / calc(...)   .ds-popover has no max-height
overflow-y: auto;                     .ds-popover cannot scroll
overscroll-behavior: contain;         so scrolling it scrolls the page beneath
```

A popover holding a bibliography entry, a footnote, or a table of contents holds
content nobody has measured. Tier 1's popover assumes short content and gives a
caller no way to say otherwise, so three callers wrote their own. That is not
three components; it is one component missing two properties.

### 3. The documented z-layer scale puts popovers behind sticky headers

DESIGN-POLICIES sets: *content chrome < 50 · popovers 50 · header-attached
dropdowns 60 · sticky headers 100 · skip link/overlays 200. Do not introduce
ad-hoc z-index values.*

All three of the page's popovers use **110**, which is not on the scale. They
have to: a citation popover opened from a paragraph must clear the sticky
contents bar, and the scale puts the bar 50 above it. The mockup did not break
the rule out of carelessness — it followed the rule and got a popover hidden
behind a bar.

`.ds-popover` has the same defect at `z-index: 50`. Any page with sticky chrome
and a popover has it.

**The policy is wrong, not the page.** A popover summoned *from content* is not
in the same layer as one attached to a header.

### 4. Components break inside the paper renderer

`ar5iv.0.8.5.css` line 1692 sets, globally:

```css
svg { z-index: -1; }   /* "require svg content is underneath the main page" */
```

That is upstream and reasonable in its own terms — it keeps LaTeXML's generated
figures below the text. But every `.ds-` component with an inline SVG icon is a
casualty: inside an inline-flex button the icon is a flex item, so the z-index
applies without positioning and the icon paints **behind the button's own fill**,
invisible on anything opaque. The mockup carries eight separate countermeasures
for it, one of which is on `.ds-btn` itself.

Tier 1 does not mention `ar5iv`, LaTeXML or a host stylesheet anywhere. But the
HTML paper page is arXiv's own page and a first-class consumer of the design
system, and it is served inside a stylesheet arXiv did not write. A component
that only works when nothing else is on the page is not finished.

### 5. The site header cannot wrap on a paper page

Tier 1 builds `.ds-site-header` with `display: flex`. The page replaces it with
`display: grid; grid-template-columns: auto auto; row-gap: 4px`, plus
`justify-self` on the logo and the nav.

The reason is in the mockup's own comment: the nav items each carry
`white-space: nowrap`, and on a paper page the bar has to fold to a second row
rather than collapse behind a hamburger, because the paper's own chrome is
already using that gesture. Tier 1 offers one responsive behaviour and the page
needed the other.

### 6. There is nothing for the shape of a reading page

62 distinct `.mg-*` classes carry the paper's layout: the shell, the marginalia
rail, the sticky contents bar, the reading-mode toggle, the anchor band. The
design system has no primitive for a main column with a rail beside it, which is
the defining shape of the thing arXiv publishes. This is on the July backlog as
"Reader chrome" and has never been built.

---

## Part two — where the page does not use the design system

Smaller, and mostly follows from part one.

- **Five tier-1 components have zero uses on the page** while the page rebuilds
  their job: `.ds-card`, `.ds-popover`, `.ds-tag`, `.ds-divider`, `.ds-badge`.
- **Hardcoded values that have tokens.** `.ds-site-header-nav a` uses `#b0aba6`
  where `--ds-hdr-fg` says the same thing; `:hover` uses `#302c28` and `#f0eeec`
  for `--ds-hdr-hover` and `--ds-hdr-fg-strong`; `.ds-site-header-divider` uses
  `#4a433d` for `--ds-hdr-divider`. Four rules, all pure duplication.
- **Stale copies.** `.ds-site-footer-main` pins `min-width: 280px` where tier 1
  now has `min(280px, 100%)` — the mockup holds the version tier 1 fixed. The
  whole `footer.ds-site-footer` block is a local re-declaration.
- **A token that no longer exists under that name.** `.ds-skip-link:focus-visible`
  uses `--ds-focus-ring-on-dark`; tier 1 uses `--ds-hdr-ring`.
- **41 pixel font sizes across 9 sizes, 205 raw pixel spacing values, and 58
  distinct one-off hex values** in the page's own CSS.
- **Dead CSS is small** — four classes (`html-header-nav`, `html-header-logo`,
  `new-html-divider`, `mg-a11y-fix`). An automated pass suggested 30, but 26 of
  those are built at runtime in script; they were checked individually.

## Already named, and confirmed here

- `.mg-btn-quiet` **already exists in the mockup** under that name. The promotion
  question raised in item 8d — whether the paper's quiet action chips become
  `.ds-btn-quiet` — is answered by the page having independently arrived at the
  name.
- `.fig-chip` and `.eqn-chip` still lack `white-space: nowrap`; a two-word label
  such as "Alt text" wraps and makes the pill lopsided. Fixed in the docs demo in
  item 8d, still open here.

## Not caused by this work

`verify-mockups.py` reports 27 passed, 2 failed: `no horizontal overflow: reader
@ 320px` and `@ 390px`. Both fail identically at the revision before the
2026-09-10 changes, checked by running the harness against that revision in a
separate worktree. They are pre-existing and belong to Phase 4.
