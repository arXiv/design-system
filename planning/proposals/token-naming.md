# Token naming — recommendation

Status: **recommendation**, needs Shamsi's yes. Answers her question of
2026-09-08: keep the `--arxiv-` prefix or not, and what modern practice is.

Short version: **keep the prefix, and change the half that comes after it.**
The prefix is where the length is; the second half is where the usability is,
and that is the half currently causing trouble.

There is a wrinkle: `DESIGN-POLICIES.md` already rules on this and rules the
other way. Section 0 covers that first, because it changes what the decision
actually is.

## 0. There is already a policy, and it says the opposite

`DESIGN-POLICIES.md` *Design tokens* currently states:

> "**Canonical names.** The design system defines tokens by their semantic name
> (e.g., `--lime`, `--grey`, `--link`). These are the authoritative reference
> names used in `design-system.css`."
>
> "**Namespace in production.** Each codebase should add a prefix appropriate to
> its context to avoid collisions with framework variables (e.g., `--arxiv-lime`
> in a React/MUI app, `$arxiv-lime` in Sass). The prefixed names should map 1:1
> to the canonical names."

So the standing rule is: **canonical is unprefixed; the consumer adds the
prefix.** Flagging that before recommending anything, per the guardrail — this
is a hard-constraints file.

Two things follow.

**The public stylesheet already does not comply.** It uses `--arxiv-*` as its
canonical names. The staff stylesheet does comply (`--lime`, `--grey`, `--link`).
So the two files disagree with each other *and* one of them disagrees with the
policy, which is part of why this question feels unsettled.

**The tier-1 model changes the premise the policy was written on.** That rule
assumes a consumer *re-declares* our tokens inside their own framework — a React
or MUI app, a Sass build — where they control the names and can add a prefix at
that point. Under the tier-1 model consumers do not re-declare anything: the
dashboards repo, the search pages and the HTML papers repo all `<link>` our
actual stylesheet. There is no per-codebase prefixing step, because there is no
per-codebase token declaration. Whatever tier 1 names its tokens is what lands in
their cascade.

**So adopting tier 1 requires revisiting this policy.** Not working around it —
its premise stops being true. That is the decision to make, and the rest of this
file is the recommendation for what to replace it with.

## 1. Recommendation: prefix the canonical names

The reference systems, checked 2026-09-08:

| System | Prefix | Example |
|---|---|---|
| **Primer** | none | `--fgColor-accent`, `--bgColor-default`, `--borderColor-muted` |
| **shadcn/ui** | none | `--background`, `--foreground`, `--border`, `--ring` |
| **Carbon** | `--cds-` | `--cds-text-primary` *(from memory — their docs would not render for a fetch; verify before quoting)* |

Two of the three drop the namespace, so on convention alone the answer would be
to drop it. The W3C Design Tokens Community Group spec reached its first stable
version (2025.10), but it governs the JSON exchange format, not CSS custom
property names — there is no standard to comply with here, only convention.

**arXiv's situation differs in a way that can be checked rather than argued.**
Primer assumes GitHub owns the page; shadcn assumes your app owns the page. arXiv
does not own the page in the HTML reader. A production paper page loads our
stylesheet alongside ar5iv's and the HTML-papers theme, which between them declare
108 custom properties, unprefixed, in the same cascade — including:

`--text-color` · `--background-color` · `--border-color` · `--link-text-color`
· `--header-text-color` · `--secondary-text-color` · `--form-border-color` ·
plus a full Bootstrap `--bs-*` set

Bare names of the shadcn kind — `--background`, `--foreground`, `--border`,
`--text` — would sit one careless addition away from a silent collision, and
collisions in custom properties fail quietly: the wrong value wins and nothing
errors.

This is not hypothetical. The staff stylesheet uses exactly those bare names
today, and under tier 1 they are the names that would be loaded into the reader
repo, next to `--text-color` and `--border-color`.

**Recommend `--arxiv-` as the canonical prefix**, and amending the policy to say
so. Self-documenting, already referenced outside this repo, and the cost is
characters rather than comprehension. A shorter namespace (`--ax-`) would work
identically if the length ever bites; not worth the churn now.

## 2. Change the second half: name the role, not the colour

This is where the real gain is, and where modern practice has clearly moved —
Primer's rename from `--color-text-primary` to `--fgColor-default` is the
reference case, and the reason is exactly our problem.

Twelve public tokens are named for what they look like rather than what they do.
In dark mode those names become false:

| Token | Light | Dark |
|---|---|---|
| `--arxiv-repository-brown` | `#1c1a17` | **`#f0eeec`** — not brown |
| `--arxiv-library-grey` | `#6b6459` | `#b0aba6` |
| `--arxiv-card-grey` | `#f0eeec` | **`#2b2723`** — a dark fill called grey |
| `--arxiv-warm-wash` | `#f9f7f7` | **`#1c1a17`** — nothing warm or washed about it |
| `--arxiv-link-blue` | `#1565c0` | `#64b5f6` |

`--arxiv-repository-brown` holding `#f0eeec` is a token whose name is wrong half
the time the site is running. That is not a tidiness complaint: it is why an
agent writing dark-mode CSS reaches for the wrong token, which the token-burn
baseline already observed happening.

Recommended shape — role, then modifier:

```
--arxiv-text            --arxiv-text-muted        --arxiv-text-disabled
--arxiv-surface         --arxiv-surface-raised    --arxiv-canvas
--arxiv-border          --arxiv-border-strong
--arxiv-link            --arxiv-link-hover        --arxiv-link-visited
--arxiv-accent          --arxiv-accent-bright
```

Brand names do not disappear — they move down a layer (below).

## 3. Two layers: primitives, then semantic

Every system in the table does this, and it is the fix for a maintenance problem
this repo already has.

- **Primitives** name the colour: `--arxiv-brown-90`, `--arxiv-blue-60`,
  `--arxiv-lime-50`. They never change between themes and components never use
  them.
- **Semantic** tokens name the job and point at a primitive:
  `--arxiv-text: var(--arxiv-brown-90)`. **Only these appear in component rules.**

The payoff is dark mode. Today the dark palette is a mirrored block of about 40
hand-maintained values, and `verification/check-drift.py` exists specifically to
catch the two copies disagreeing — which it cannot do across the two stylesheets,
where `--arxiv-grey-dis` and `--grey-dis` have already drifted apart in dark. With
two layers, a theme re-points semantic tokens at different primitives and there is
no second copy of anything to keep in sync.

It also gives the accent re-point a place to stand: the staff surface sets
`--arxiv-accent: var(--arxiv-lime-50)` and every component follows, which is what
would make Access Lime a token decision rather than a stylesheet one.

## 4. Sequence

1. **Tier-1 consolidation first, names unchanged** (`token-unification.md`). Move
   the code, fix the six drifts, delete the staff copies.
2. **Then the semantic rename**, as its own pass, mechanical and scriptable.
3. **Then the primitive layer**, which is only worth introducing once there is
   one file to introduce it into.

Not both at once. A diff that moves code and renames it in the same commit cannot
be reviewed, and this repo has several concurrent editors.

## What this does not change

`.ds-` class names. Both stylesheets already agree on those, and nothing above
touches them.
