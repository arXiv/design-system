# Token naming — recommendation

Status: **recommendation**, needs Shamsi's yes. Answers her question of
2026-09-08: keep the `--arxiv-` prefix or not, and what modern practice is.

**The recommendation in one paragraph.** One canonical token name per thing,
used exactly as written in every codebase — no per-repo prefixes and no mapping
tables. Keep `--arxiv-` on all of them, because arXiv does not own the page in
the HTML reader and a custom-property collision there fails silently. Spend the
readability on the part after the prefix: name the role (`--arxiv-text`), not the
colour (`--arxiv-repository-brown`), because the colour names go false in dark
mode. Keep brand colour names, but one layer down, where components never touch
them.

This replaces the current rule in `DESIGN-POLICIES.md`, which says canonical
names are unprefixed and each consuming codebase adds its own. Section 0 explains
why that rule should go — briefly, it asks a four-person team to maintain
translation layers nothing can check, its premise stops being true under the
tier-1 model, and the code already ignores it.

## 0. The existing policy, and why it needs replacing

`DESIGN-POLICIES.md` *Design tokens* currently says:

> "**Canonical names.** The design system defines tokens by their semantic name
> (e.g., `--lime`, `--grey`, `--link`)."
>
> "**Namespace in production.** Each codebase should add a prefix appropriate to
> its context to avoid collisions with framework variables (e.g., `--arxiv-lime`
> in a React/MUI app, `$arxiv-lime` in Sass). The prefixed names should map 1:1
> to the canonical names."

Canonical unprefixed; every consuming codebase adds its own prefix and keeps a
1:1 mapping. Three problems with it, in order of weight.

**It is maintenance nobody has time for.** arXiv is a very small team, and this
rule asks every consuming repository to maintain a private translation layer
between our names and theirs. Nothing verifies those layers. Nothing can:
a mapping that lives in another repo is invisible to `check-drift.py` and to
anyone reading this one. For a team this size that is the wrong kind of rule —
it creates work that is never done and never checked.

**Its premise stops being true under tier 1.** The rule assumes consumers
*re-declare* our tokens inside their own framework, where they control the names.
Under the tier-1 model consumers re-declare nothing: the dashboards repo, the
search pages and the HTML papers repo all `<link>` our actual stylesheet. There
is no per-codebase prefixing step, because there is no per-codebase token
declaration. Whatever tier 1 names its tokens is what lands in their cascade.

**The code already ignores it.** The public stylesheet uses `--arxiv-*` as its
canonical names. The staff stylesheet complies with the policy and uses bare
names. So the two files disagree with each other, and one disagrees with the
written rule. That is not a policy being followed.

## 1. What the decision actually trades off

The three goals pull in different directions only if you treat the token name as
one thing. It is two.

| Half of the name | What it is for | What makes it good |
|---|---|---|
| `--arxiv-` | telling ours apart from everyone else's | being **unique**; nobody reads it for meaning |
| `text-muted` | telling a developer which token to reach for | being **honest and obvious**; read every time |

So the prefix should be optimised purely for specificity and the suffix purely
for usability. There is no trade between them — they are not competing for the
same characters. The apparent tension ("shorter names are friendlier") is really
about the suffix, and the suffix is where our names are currently worst.

## 2. Prefix: keep `--arxiv-`, and make it canonical

Checked against the reference systems, 2026-09-08:

| System | Prefix | Example |
|---|---|---|
| **Primer** | none | `--fgColor-accent`, `--bgColor-default`, `--borderColor-muted` |
| **shadcn/ui** | none | `--background`, `--foreground`, `--border`, `--ring` |
| **Carbon** | `--cds-` | `--cds-text-primary` *(from memory — their docs would not render for a fetch; verify before quoting)* |

The W3C Design Tokens Community Group spec reached its first stable version
(2025.10), but it governs the JSON exchange format, not CSS custom property
names. There is no standard to comply with — only convention, and convention is
split.

Two of the three drop the namespace. Both of those systems assume they own the
page: Primer assumes GitHub does, shadcn assumes your app does. **arXiv does not
own the page in the HTML reader.** A production paper page loads our stylesheet
alongside ar5iv's and the HTML-papers theme, which between them declare **62
custom properties in the same cascade**, unprefixed — `--text-color`,
`--background-color`, `--border-color`, `--link-text-color`,
`--header-text-color`, plus a full Bootstrap `--bs-*` set.

**Stated honestly: there are zero literal collisions today.** Checked both
stylesheets against all 62. This is not a live bug. It is a risk, and the reason
to spend seven characters on it is the shape of the failure rather than its
odds — a custom-property collision fails **silently**. The wrong value wins,
nothing errors, and the bug surfaces as "the reader looks slightly wrong on some
pages". Six of the staff stylesheet's bare names already sit next to a foreign
property naming the same concept (`--text` / `--text-color`, `--border` /
`--border-color`, `--canvas` and `--surface` / `--background-color`), so it would
take one upstream ar5iv change or one Bootstrap upgrade to land it. Cheap
insurance against a silent, slow-to-diagnose failure is a good trade even at low
probability. Bootstrap's own `--bs-` prefix exists because they learned this.

There is a second benefit that does not depend on collisions at all: **ownership
is legible**. Open devtools on a paper page and 62 foreign properties are
interleaved with ours. `--arxiv-text` says whose it is without looking anything
up — which matters for a small team and for the agents doing much of this work.

`--ax-` would be equally unique and shorter. Recommend against it: the seven
characters buy self-documentation, and nothing in the codebase is currently
suffering from name length.

## 3. Simplicity: one name, used verbatim, everywhere

This is the change that actually simplifies things, and it is the opposite of the
current rule.

**One canonical name per thing. Every codebase uses it exactly as written. No
per-repo prefixes, no mapping tables, no translation layer.** If a page wants
arXiv's text colour it writes `var(--arxiv-text)`, in this repo, in the
dashboards repo, in the reader, in a Sass build, in devtools, in a bug report.

This is where usability, simplicity and specificity stop competing: one
unambiguous name is simultaneously the most specific option, the least work, and
the easiest to talk about. The only thing it costs is the flexibility for each
repo to pick its own names, which was never a benefit — it was a requirement
imposed by the old assumption that consumers re-declare tokens.

## 4. Usability: name the role, not the colour

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

## 5. Two layers: primitives, then semantic

Every system in the table does this, and it is the fix for a maintenance problem
this repo already has.

- **Primitives** name the colour: `--arxiv-brown-90`, `--arxiv-blue-60`,
  `--arxiv-lime-50`. They never change between themes and components never use
  them.
- **Semantic** tokens name the job and point at a primitive:
  `--arxiv-text: var(--arxiv-brown-90)`. **Only these appear in component rules.**

**What this does and does not buy — stated carefully, because the first version
of this file oversold it.** It does *not* shrink the dark block: a theme still
re-points every semantic token, so the line count is the same. What it buys is
that the palette is stated once, so two tokens that should hold the same colour
provably do. Today `--arxiv-card-grey` in light and `--arxiv-repository-brown` in
dark are both `#f0eeec`, and nothing shows that they are meant to be the same
value rather than a coincidence. It also means retuning a brand colour is one
edit instead of a search, and it gives the brand names a legitimate home instead
of leaving them attached to roles they stop describing.

The mirrored dark block itself wants a different fix — the `light-dark()` CSS
function, or generating the mirror rather than hand-writing it. Worth looking at
separately; not solved by layering.

It also gives the accent re-point a place to stand: the staff surface sets
`--arxiv-accent: var(--arxiv-lime-50)` and every component follows, which is what
would make Access Lime a token decision rather than a stylesheet one.

## 6. Sequence

1. **Tier-1 consolidation first, names unchanged** (`token-unification.md`). Move
   the code, fix the six drifts, delete the staff copies.
2. **Then the semantic rename**, as its own pass, mechanical and scriptable.
3. **Then the primitive layer**, which is only worth introducing once there is
   one file to introduce it into.

Not both at once. A diff that moves code and renames it in the same commit cannot
be reviewed, and this repo has several concurrent editors.


## The proposed policy text

To replace the *Design tokens* section of `DESIGN-POLICIES.md` if this is
accepted:

> ## Design tokens
>
> - **One name, used everywhere.** Each token has exactly one name, and every
>   codebase uses it exactly as written — this repo, the dashboards, the search
>   pages, the HTML papers reader, a Sass build, a bug report. No per-repository
>   prefixes and no mapping tables: a mapping that lives in another repo is
>   invisible to everyone here and to every check we run.
> - **Every token is prefixed `--arxiv-`.** arXiv does not own the page in the
>   HTML reader, where our stylesheet loads beside ar5iv's and the papers theme
>   and their 62 unprefixed custom properties. A collision between custom
>   properties fails silently — the wrong value wins and nothing errors — so the
>   prefix is cheap insurance against a slow, quiet failure. It also makes
>   ownership legible in devtools.
> - **Name the role, not the colour.** `--arxiv-text`, not
>   `--arxiv-repository-brown`. Colour names stop being true the moment the theme
>   flips, and a token whose name is wrong half the time the site is running is a
>   trap for whoever reads it next.
> - **Two layers.** Primitives name the colour (`--arxiv-brown-90`) and never
>   change between themes. Semantic tokens name the job and point at a primitive
>   (`--arxiv-text: var(--arxiv-brown-90)`). **Components only ever use semantic
>   tokens** — a primitive in a component rule is the same mistake as a raw hex.
> - **Values are the source of truth.** The values in `design-system.css` are
>   authoritative. If a framework's token disagrees, the design system wins.

## What it would cost

Honest accounting, since none of this is free:

- **A rename pass over both stylesheets and every docs page.** Mechanical and
  scriptable, but it is the whole repo, and several people and agent sessions
  edit here concurrently. Wants to be one commit, landed quickly, not left
  half-done.
- **External references go stale.** `color-mapping.md`, both mockups, and the
  blog theme in another repo quote the current names. The blog theme is
  translated deliberately anyway, so it absorbs this on its next pass, but it
  needs to be on that agenda rather than discovered.
- **One concept more to learn** — the primitive/semantic split. Worth it because
  it is the thing that stops brand names from being attached to roles they no
  longer describe, but it is a real addition to what a newcomer must hold.

## What it does not change

`.ds-` class names. Both stylesheets already agree on those, and nothing above
touches them.
