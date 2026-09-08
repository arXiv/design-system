# A staff-only control on a public page — needs a decision

Status: **settled 2026-09-08.** Shamsi agreed with the recommendation below; the
rule is now recorded in `DESIGN-POLICIES.md` *Contexts*. Raised by a developer
building arXiv's user dashboards:

> "I have a button that only shows up for logged in users with admin status. The
> page uses the public style for most elements but I need to be able to apply an
> 'admin' class style to a specific button. I don't want to override the style
> for all the other buttons on the page."

Two separate questions are tangled here. The mechanical one has a clean answer.
The design one is explicitly reserved to a person by `DESIGN-POLICIES.md`, so it
is not being built until Shamsi settles it.

## The design question — policy said ask, so this was the ask

`DESIGN-POLICIES.md` *Contexts*:

> "the accent tells the person which context they are working in, so the two must
> never be crossed. A lime primary button on a public page … is a violation
> regardless of how well it reads. When the context is genuinely ambiguous (a
> shared component or an embedded widget), ask and settle which one the user is
> in before building, then record the answer in a code comment."

This is that case, named almost exactly. It needs settling, not interpreting.

**Recommendation: the user is in the public context, and the button stays Open
Blue.** The page is a public dashboard; an admin viewing it is using the public
product with one extra power, not visiting a staff tool. The accent answers
"where am I", and the answer is still "on arxiv.org". Recolouring one button
lime would make the accent answer "what can I do", which is a different question
and the one the accent is specifically not for.

**Signal "staff only" some other way**, since the developer's real need — make it
obvious this is a privileged action — is legitimate:

1. **Label it.** A `.ds-tag--chrome` reading "Staff" beside the button, or the
   button's own words carrying it ("Approve as moderator"). This is the
   recommendation: it is the signal that survives greyscale, dark mode, and the
   reader who has never seen the other accent to contrast it with.
2. **Use the tier, if the action warrants it.** A moderation action that removes
   or withdraws something is destructive, and the destructive tier is a hierarchy
   signal available on any surface. That is a stronger and more accurate warning
   than an accent swap, and it needs no policy decision.
3. **Group them.** If more than one staff control appears, they belong in one
   labelled region rather than scattered among the public ones — which also makes
   the "one button" problem stop being a one-button problem.

**If Shamsi decides the opposite** — that a staff control keeps the staff accent
wherever it appears — then the mechanism below is what implements it, and the
decision needs recording in `DESIGN-POLICIES.md`, because the current text calls
it a violation in so many words.

## The mechanical question — how to scope a style to one control

The developer's instinct is right and the pattern already exists in the system.
A **scope class that re-points tokens and declares no properties of its own**:

```css
.ds-staff {
  --arxiv-open-blue: …;
  --arxiv-link-blue: …;
}
```

```html
<button class="ds-btn ds-btn-primary ds-staff">Approve</button>
```

Custom properties inherit, so this reaches that button's subtree and nothing else.
There is no specificity fight, because the scope declares no property that could
lose one. This is exactly how `.ds-site-header--light` works — it re-points seven
surface tokens and nothing more — so it is a pattern the system already proves
rather than a new invention.

### The blocker: it does not work on the buttons that matter, yet

Tested against the live stylesheet, 2026-09-08:

| Tier | Re-pointing its accent token | Why |
|---|---|---|
| `.ds-btn-text` | **works** | reads `var(--arxiv-link-blue)` |
| `.ds-btn-secondary` | **no effect** | fill and border are literal values |
| `.ds-btn-primary` | **no effect** | both gradients are literal hexes — `#a5d6fe`, `#b0d5ed`, `#6ba8da` |

So a scoped re-point currently reaches only the quiet tier. This is a defect in
the buttons rather than in the approach, and it contradicts a rule the same
policy file states: *"Palette and type stack only. No one-off hex values."* Those
gradient stops are one-off hex values.

**Tokenising the primary and secondary fills is worth doing regardless of how the
design question lands.** It is a prerequisite for any scoped re-point, it is what
would let the staff and public button systems share one construction under the
tier-1 consolidation (`token-unification.md`), and it is what the no-hex rule
already asks for. It is also the reason dark mode needs three separate
`.ds-btn-primary` overrides today instead of none.

## Answer to give the developer now

1. Keep the public accent on that button; it is a public page.
2. Mark the action as privileged with a `.ds-tag--chrome` "Staff" label, or with
   wording, or with the destructive tier if it destroys something.
3. The scope-class pattern is the right tool if we later decide he needs it, but
   it cannot recolour a primary button until those fills are tokenised. Do not
   hand-write the lime hex in the dashboard repo as a workaround — that is the
   one-off-hex rule, and it puts a value in a place nothing can check.

## Why this is worth more than one button

The case generalises: any public page that grows a privileged control hits it —
moderation on an abstract page, an editor's action on a listing, "edit this
paper" for an owner. Deciding it once, here, is cheaper than deciding it per
page, and the answer belongs in `DESIGN-POLICIES.md` *Contexts* next to the rule
that raised the question.
