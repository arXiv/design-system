# One name per thing, at the token layer — proposal

Status: **proposed**. Answers Shamsi's question of 2026-09-08 — *what are the
two stylesheets, and what exactly would be unified?*

## The two stylesheets

| File | Serves | Names its tokens | Names its buttons |
|---|---|---|---|
| `docs/public/design-system.css` | arxiv.org and every public page; outreach sites inherit it | `--arxiv-*` prefix | `.ds-btn*` |
| `docs/internal/design-system.css` | staff tools — the admin console, arXiv Check, moderation screens | no prefix | `.btn-*` |

Both are authoritative for their surface. Neither imports the other. There is
no third file and no shared base.

They exist as two files for a real reason: the accent differs, and the accent is
how a person can tell at a glance which system they are in. Internal is Access
Lime, public is Open Blue, and the two are never crossed. That decision is not in
question here.

## What is actually duplicated

They share **7 token names out of about 60 each** — the `--space-*` scale, and
nothing else.

That understates the overlap badly. Twenty-five more tokens are **the same value
under a different name**:

| The thing | Public | Internal | Same value? |
|---|---|---|---|
| Page canvas | `--arxiv-warm-wash` | `--canvas` | `#f9f7f7` both |
| Primary text | `--arxiv-repository-brown` | `--text` | `#1c1a17` both |
| Component fill | `--arxiv-surface` | `--surface` | `#ffffff` both |
| Hairline border | `--arxiv-border-light` | `--border` | `#ddd8d2` both |
| UI boundary grey | `--arxiv-grey-ui` | `--grey-ui` | `#8b8680` both |
| Muted body text | `--arxiv-library-grey` | `--grey` | `#6b6459` both |
| Raised band | `--arxiv-card-grey` | `--surface-header` | `#f0eeec` both |
| Link / hover / visited | `--arxiv-link-blue` etc. | `--link` etc. | identical, all three |
| Focus ring | `--arxiv-focus-ring` | `--focus-ring` | `#1565c0` both |
| Status families | `--arxiv-success-*`, `-info-*`, `-warning-*`, `-error-*` | `--success-*`, `--info-*`, `--warning-*`, `--error-*` | identical, all twelve |

So the picture is not "two palettes." It is **one palette, written down twice,
plus each surface's own accent**.

## What is genuinely different, and must stay so

- **Public only:** `--arxiv-open-blue`, `--arxiv-archival-blue`, `--arxiv-tint-*`
  (popover surfaces), `--arxiv-pill-border`, `--arxiv-header-bar`,
  `--arxiv-smileybones-yellow`.
- **Internal only:** the whole `--lime*` and `--sec-*` families, `--danger*`,
  `--text-on-lime`, `--icon-border`, `--grey-hover-*`, `--surface-hover`.

Roughly a third of each file. This is the part that earns two files.

## The drift this is already causing

Two same-concept tokens have **different dark-mode values**:
`--arxiv-grey-dis` is `#5a554f` dark; `--grey-dis` is `#484340` dark. Nobody
decided that. One of them was adjusted and the other was not, and no check could
have caught it, because a checker comparing token *names* sees two unrelated
tokens.

That is the argument for doing this. Not tidiness — the duplication is invisible
to every tool we have, so it can only be found by a person reading both files
side by side, which is exactly what nobody does.

## What "unify" would mean, concretely

Not merging the stylesheets. Three steps, each independently landable:

1. **Agree one name per concept** for the 25 shared tokens. The internal names
   are shorter and read better (`--canvas`, `--text`, `--surface`); the public
   names carry the brand and are the ones quoted in `color-mapping.md` and in
   every mockup. Recommend keeping the **public** names, because they are the
   ones already written into content outside this repo, and renaming those has a
   blast radius we cannot see. Cost: internal gets more verbose.
2. **Extract the agreed set into one file** both stylesheets `@import` or that
   is concatenated at publish time — a single `tokens.css`. Each stylesheet then
   holds only its own accent and its own component rules.
3. **Re-point the 22 internal-only classes** that are the same component in a
   different palette — `.ds-alert*`, `.ds-tag*`, `.ds-field`, `.ds-input`,
   `.ds-label`, `.ds-check`. These do not need to be re-declared at all once the
   tokens are shared; they need the accent tokens to resolve differently, which
   is what `.ds-site-header--light` already does for the header. **Access Lime as
   primary becomes a token decision, not a stylesheet one** — which is the real
   prize here, because it is what would let a staff tool and a public page share
   a component instead of each owning a copy.

Step 3 is where the payoff is; steps 1 and 2 are what make it possible.

## Recommended sequence

Do **step 1 only** first, as a decision, and write it down here. It costs nothing
to reverse and it is the only step that needs Shamsi. Steps 2 and 3 are mechanical
once the names are agreed, and step 3 should wait until the modal and the toggle
exist, because those are the first two components that will have to work on both
surfaces and will test whether the token layer actually carries the load.

## Not in scope

The blog theme's bundled copy. It is a separate project that translates
deliberately; `check-drift.py` already reports its differences as a NOTE and that
list is an agenda, not a defect.
