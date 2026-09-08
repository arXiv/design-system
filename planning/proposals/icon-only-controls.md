# Naming the icon-only controls — proposal

Status: **proposed**. Answers Shamsi's ask of 2026-09-08: name these the way the
established systems do rather than after the first place they appeared.

## The family

Zoom in, zoom out, reset/fit, and close. Today the first three exist only in the
figure viewer inside `mockups/public/html-phase1.html` as `.fig-lightbox-zoombtn`
and `.fig-lightbox-close`. Naming them "lightbox controls" would name a component
after its first host, which is the mistake `.ds-close` was just built to undo.

## What the three reference systems call it

| System | The shape | The quiet tier | Accessible name |
|---|---|---|---|
| **Primer** | `IconButton` — a distinct component. Sizes `small` / `medium` / `large`. | `variant="invisible"` | requires an `aria-label` prop; optional `description` renders a tooltip |
| **shadcn/ui** | `Button` with `size="icon"` (plus `icon-xs` / `icon-sm` / `icon-lg`) | `variant="ghost"` | left to the author |
| **Carbon** | `Button` with `hasIconOnly` | `kind="ghost"` | `iconDescription` — required |

Fetched and verified for Primer and shadcn on 2026-09-08. The Carbon row is from
memory: their docs site did not render for the fetch, so treat it as needing a
check before it is quoted anywhere.

The convergence is clear on two points and split on a third:

- **All three treat icon-only as a modifier on the button, not a new tier.** Only
  Primer gives it its own component name, and even there it takes the same
  variants as `Button`.
- **All three name the quiet tier something other than "text."** Two say *ghost*,
  one says *invisible*.
- **They split on whether the accessible name is enforced.** Carbon and Primer
  make it a required prop. shadcn does not, and shadcn is the one with the
  well-known accessibility gap here.

## Proposal

**`.ds-btn-icon`** — a shape modifier on `.ds-btn`, composing with whichever tier
the surface calls for:

```html
<button class="ds-btn ds-btn-text ds-btn-icon" type="button">
  <svg …  aria-hidden="true">…</svg>
  <span class="is-sr-only">Zoom in</span>
</button>
```

Reasons for this shape of answer:

- It matches shadcn's `size="icon"` and Carbon's `hasIconOnly` — a modifier, not
  a fourth tier. We already rejected adding a tier once, for the outline button,
  and for the same reason: a tier has to mean a rank in the hierarchy, and
  "happens to have no words" is not a rank.
- It does not rename `.ds-btn-text`. *Ghost* and *invisible* are the industry
  words, but our tier already has a name, a documented rationale for why it drops
  the border rather than the fill, and a matching internal `.btn-tertiary`.
  Renaming it would churn every page to land on a word that is more fashionable
  but not clearer. Recommend leaving it.
- The `.is-sr-only` span rather than `aria-label` follows the icon policy already
  in `DESIGN-POLICIES.md`, and takes the Carbon/Primer side of the split: the name
  is required, not optional. It also survives page translation, which `aria-label`
  does not.

### What it would specify

- 32×32, `min-width: 0`, no padding, `gap: 0` — against the 24×24 hard floor.
- `color: inherit`, for the same reason `.ds-close` takes it: an icon has no words
  to colour, and these controls sit on chrome that sets its own foreground.
- A required accessible name, documented as required.

### Relationship to `.ds-close`

`.ds-close` is standalone rather than a `.ds-btn` variant, because the staff
stylesheet names its buttons `.btn-*` and a close built on the public button base
could not be the same control on both surfaces. If `.ds-btn-icon` is approved,
the two overlap by about eight declarations and the honest options are:

- **(a)** leave both — `.ds-close` for the one control that must cross surfaces,
  `.ds-btn-icon` for icon-only buttons inside the public button system; or
- **(b)** make `.ds-btn-icon` standalone too, on the same reasoning, and let
  `.ds-close` be `.ds-btn-icon` plus the x recipe.

Recommend deciding this only when the second icon-only control actually needs to
exist. One instance is not enough evidence to choose, and the figure viewer is
still a mockup.

## Not proposed yet

Sizes. Primer and shadcn both offer three or four; we have one control and no
case for a second size. Add one when something asks for it.
