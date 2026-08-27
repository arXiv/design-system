# Submission metadata — form validation patterns

A guide for implementing validation feedback on the Add or Edit Metadata page.

This is a design specification, not production code. The mockup demonstrates the
target behavior; the markup is written to be readable rather than to drop into a
Jinja template unchanged.

**Files**

| File | What it is | Ported? |
|---|---|---|
| `metadata-form-mockup.html` | The page, simplified to the form and the patterns under discussion | Reference only |
| `mockup-validation.css` | Every new style. Eleven numbered sections | **Yes — this is the deliverable** |
| `mockup-validation.js` | Rendering, gating, and the in-progress state | Partly — see [What to port](#what-to-port) |

Open `metadata-form-mockup.html` in a browser. The dark bar at the top switches
between five states. It is scaffolding, not a proposal — delete it when porting.
The Process button also runs the flow for real, including the in-progress state.

---

## 1. The validation model

Two dispositions, matching QA's existing vocabulary, plus a third signal that is
not a problem at all.

| Tier | Meaning | Can the user continue? | Color |
|---|---|---|---|
| **Error** | Rejection. The value is not acceptable. | No. Continue stays unavailable. | Danger Red `#c62828` |
| **Warning** | The value is accepted, but the submission may be held for moderator review. | Yes. | Amber `#e8b800` |
| **Note** | arXiv changed the value automatically. Nothing is wrong; the user is being told what happened. | Yes. | Info Blue `#5a82c8` |

The **note** tier is what carries your "automate what is not debatable, then
present it back" principle. Whitespace normalization and sanitization are edits
to author-submitted content, and what makes that legitimate is that the author
sees the change before it is committed. The review step is not a nicety that can
be optimized away later for obvious fixes — it is the thing that makes automatic
transformation acceptable in the first place. Worth stating in the code comment
so a future developer does not remove it.

Colors are the status tokens from `docs/public/design-system.css`, copied into
section 1 of `mockup-validation.css`. Contrast is already verified there. When
the submission app adopts the design system, delete that block and inherit.

---

## 2. Component inventory

### 2.1 Required and optional indicators

An asterisk on its own is not enough. It is small, it carries no meaning without
a legend, and the legend sits at the top of a form the reader has already
scrolled past by the time they reach the ninth field. The accepted practice is
to say the word.

**What the current page does is worth looking at first.** Five labels carry
`.optional`, and `submit.css:142` styles `.label.optional span` in italic — so
the template was written to emit `DOI <span>(optional)</span>`. That span is not
in the markup. **The word never renders.** All that survives is the label
turning grey, which is color alone and fails WCAG 1.4.1. Comments is optional
too and is not marked at all.

So mark both groups, in words:

| | Signal |
|---|---|
| **Required** | Red asterisk via `.field-required`, the legend above the form, plus `required` and `aria-required="true"` |
| **Optional** | The word `(optional)` in the label text, via `<span class="label-optional">` |

Marking both is usually over-marking, and the standard advice — mark only the
optional ones — assumes most fields are required. Here it is inverted: six of
nine are optional. Neither group is small enough to be the obvious exception, so
neither is left to inference.

The word goes in the **visible label text**, never in `aria-label` or `title`.
Inside the label it becomes part of the accessible name for free and needs no
ARIA of its own.

Only the qualifier is de-emphasized. The legacy rule greys the whole label to
`#767676` (4.54:1 — AA by a hair), which makes optional fields harder to read
than required ones. The label keeps full strength; the parenthetical steps back
to `#595959` (7.0:1).

### 2.2 Hints, examples, and inline code

- **Visual:** small grey text between the label and the input. `#757575` on
  white, 4.60:1 — passing AA with almost no margin, so do not lighten it.
- **Markup:** `<p class="help has-text-grey is-marginless">`
- Position is already right on the current page: above the input, where a hint
  can prevent the error instead of explaining it afterwards.

**Inline code loses its red.** The legacy stylesheet paints every `<code>`
element `#cd0200` (`arxivstyle.css` line 329). That is a Bulma default, not a
decision anyone made about this form, and it measures 5.8:1 on white against our
error red at 5.6:1. They are the same red to a reader. The author-format example
`GivenName(s) FamilyName(s)` therefore reads as a validation failure, on a page
whose whole job is to tell failures apart from everything else.

Red means one thing in this form: error. Nothing else may use it.

The replacement is the design system's inline-code treatment, used on every page
in `docs/`: monospace on a neutral grey chip (`#f0eeec`), inheriting the
surrounding text color, with no color of its own. The font stack is the design
system's own and falls through to the platform monospace until IBM Plex Mono is
loaded, so it upgrades by itself when the submission app adopts the DS fonts.

This is worth promoting into `design-system.css`. Today it exists only as a
local style repeated on each documentation page, which means it is a convention
rather than a component.

**Examples get a word, not just a chip.** Label them `Example:`
(`<span class="hint-example-label">`) so that being illustrative does not rest
on the chip styling alone. Keep the whole example inside one `<code>`,
separators included — the separator is part of what the user has to type, and
splitting `F.2.2; I.2.7` into two chips hides the semicolon that does the work.

**Link text is specific to its field.** "See title formatting help", "See author
name formatting help", "See abstract formatting help" — never three identical
"See formatting help" links. Someone pulling up a list of links on the page, or
tabbing between them, gets the destination from the link alone; three links with
the same text and different targets are indistinguishable out of context.

**The help bubbles are gone.** The bright blue question-mark icons
(`.filter-blue`, `#1c8bd6`) drew more attention than any label on the page, and
what they concealed was one short sentence per field. That sentence is now hint
text, visible without interaction. Where a link to the full help page is still
useful, it is a plain inline text link at the end of the hint.

This also disposes of an accessibility problem: the bubble appeared on hover,
vanished on mouse-out, could not be hovered into, and could not be dismissed
with Escape. WCAG 2.1 SC 1.4.13 requires content shown on hover to be hoverable,
dismissible, and persistent. Reserve tooltips for genuinely long explanations,
and if any come back, fix the dismiss behavior first.

### 2.3 Field message — error, warning, note

- **Visual:** small colored text below the input, with a leading glyph
  (`✕` error, `⚠` warning, `↻` note). The glyph is a CSS `::before` and is
  decorative; the message text carries the meaning.
- **Markup:** `<p class="field-error" id="{name}-msg">`, and correspondingly
  `field-warning` / `field-note`.
- **Position: after the input.** The current page renders the message *above*
  the hint and *above* the input, which is the furthest point from what it
  describes, and pushes the input down the page when it appears. Below the
  input it is adjacent to the problem and nothing moves.
- **Wiring:** the input needs `aria-describedby="{name}-msg"`, and
  `aria-invalid="true"` for the error tier only. Without `aria-describedby` a
  screen reader announces the field and nothing else, and the whole validation
  display is invisible to that user.
- Each message opens with visually-hidden text — `Error:`, `Warning:`,
  `Changed automatically:` — because the tier is otherwise carried only by
  color and a decorative glyph.

**Several problems in one field.** The abstract rules on
[info.arxiv.org/help/prep](https://info.arxiv.org/help/prep.html#abstracts) are
easy to break several at a time, so the abstract does exactly that across the
main scenarios: a leading "Abstract:", an HTML `<br>`, a `\em` font command, and
a URL run together with the full stop after it. *Errors and warnings* shows all
four at once — two blocking, two not — in a single field.

- **One problem renders as a `<p>`. Several render as an `<ol class="field-messages">`.**
  Numbered, because "the second one" has to be sayable while someone works
  through them, and because a run of loose paragraphs under one field stops
  looking like a set of separate problems.
- **Inside the list the glyph is dropped.** The marker already separates the
  rows, and a number plus an icon plus a color is one signal too many. Color and
  the visually-hidden prefix still carry the tier.
- **The control shows the worst tier present.** A field holding an error and a
  warning is a field you cannot proceed past, so its border reads as an error.
- **`aria-describedby` points at the list container**, so the whole set is read
  when the field takes focus.
- **The marks are tiered too.** One highlight color would say "something is
  wrong here" without saying which of these stops you continuing.
- All matches are painted in **one pass** over the value, sorted by position, so
  overlapping problems cannot double-wrap the same characters.

**Copy detail that bites.** The chip shows the match *trimmed*, while the search
uses it whole: `"Abstract: "` needs its trailing space to be the string we mean,
but a chip with a hanging space reads as a typo. And nothing appends a full stop
after the chip — half these matches already end in punctuation, and
`Remove <code>Abstract:</code>.` reads as a mistake.

### 2.4 Field state on the control

- **Visual:** border in the tier color plus a 3px translucent ring of the same
  hue. The ring is what makes the state legible at a glance without the border
  weight changing and reflowing the layout.
- **Markup:** `.is-invalid` or `.is-warning` on the `input` / `textarea`.
- **Note fields get a blue border and ring** (`.is-note`), so every alert tier
  has a matching field state and the changed field can be found from the summary
  without reading. It is distinct from focus, which is a 3px outline at 2px
  offset rather than a border.

  A first pass gave blue the border but no ring, reasoning that a non-problem
  should stay quiet. That was wrong — a bare border among ringed fields
  disappears, and a signal nobody notices fails at the only job it has. If blue
  does turn out to compete with red for attention, the fix is to reconsider
  whether every automatic change deserves a flag, not to draw the flag too
  faintly to read.
- `.is-empty-required` is visually identical to `.is-invalid`. It exists as a
  separate class only so the server can distinguish "left blank" from "filled
  in wrongly" in logs. Use whichever is more convenient.
- The border is never the only signal. Every state here is paired with a
  message, per DESIGN-POLICIES: color is never the sole means of conveying
  information.

### 2.5 Page-level summary

- **Visual:** a bordered, tinted panel above the first field. Thick left border
  in the tier color. Same construction as `.ds-alert` in the design system.
- **Markup:** `#form-summary` is a plain container. Inside it goes one
  `<div class="form-summary form-summary-{tier}">` per severity present.
- **The list items are links** to the fields they name. A summary that names
  problems without jumping to them makes the user hunt, and on a nine-field
  form that hunt is most of the cost of the error.
- `tabindex="-1"` and `aria-live="polite"` on the container, so focus can move
  here after processing and the result is announced.

**One alert per severity — never a mixed one.** Errors and warnings do not share
a box. Red has to mean "you cannot proceed", and the moment a non-blocking item
appears inside a red alert, red stops meaning that: the user has to read every
line to work out which kind each one is. Split, each alert gets a heading that
says what it is, instead of one heading hedging across both.

| Order | Alert | Heading | Body |
|---|---|---|---|
| 1 | Error (red) | **2 blocking errors** | Blocking errors must be corrected before you can continue. |
| 2 | Warning (amber) | **3 warnings** | You may continue with warnings, but your submission may experience delays in announcement. |
| 3 | Success (green) | **No problems found** | Select Continue to move on to the final preview. |
| 4 | Note (blue) | **1 automatic change** | arXiv corrected these for you. Please check that they read correctly. |

**The heading is the count.** "2 blocking errors" answers "how bad is this?" in
two words, which is the question someone scanning actually has, and it keeps all
three headings parallel: the number, then what the items are. The body then says
what the tier *means*, once, instead of restating the count in a longer sentence.
Each body ends with "Click on an item to jump to that field."

The blue heading is **"automatic changes"**, not "informational". The other
headings name what the items *are*, not which tier they belong to; naming the
tier would make this one the odd heading out, and would tell the reader less.

The verdict precedes the supporting detail: when nothing is blocking, "can I
proceed?" is the question the user actually has, so the green alert comes before
the blue one. Automatic changes are always reported and never folded into the
green alert, which would read as "no action needed" for something the author is
being explicitly asked to check.

**One row per problem, not per field**, and every row names its field even when
a field contributes several rows. Repeating "Abstract" three times is not noise:
without it the reader cannot tell whether three problems mean one field to visit
or three. When the two counts differ, the sentence says both — *"2 items in 1
field"* — so nobody has to work it out from the list.

Each row also carries the match, since a message written to lead into one
(*"… Remove"*) would otherwise end mid-sentence in the summary.

Every count and every list is derived from the field results, so a summary
cannot disagree with the fields it describes. Do not hand-write these strings in
the template.

### 2.6 Highlight within a field

**Never echo the field's contents back below it.** An abstract runs to 1920
characters, and reprinting it to point at five of them is absurd — it buries
every other message on the page. Mark the problem where it already is.

Three channels, because no one of them reaches everybody:

1. **The message names the offending string.** This is the channel that always
   works: screen readers, images off, high-contrast modes, print. The *match* is
   short even when the *field* is long, which is why quoting the match is safe
   where quoting the value is not. Multiple hits get a count —
   `Remove <tag> (3 instances).`
2. **The field highlights it**, for someone scanning visually.
3. **A "Show me" control selects it**, scrolling a long value to the right place
   and putting the caret there. This is what makes the pattern work at 1920
   characters, and it serves keyboard users, not only mouse users. Repeated
   presses cycle through every instance.

Highlight alone would fail WCAG 1.4.1 — it is a purely visual cue. Channel 1 is
what makes channels 2 and 3 enhancements rather than requirements. That is also
why the message says *"Remove `<tag>`"* and not *"see highlighted text"*: an
instruction that only makes sense if you can see the highlight is not an
instruction for everybody.

```html
<p class="field-error" id="abstract-msg">
  <span class="is-sr-only">Error: </span>The abstract contains HTML markup,
  which is not permitted. Remove <code class="field-match">&lt;tag&gt;</code>.
  <button type="button" class="field-locate">Show me</button>
</p>
```

**Mechanism.** A backdrop div sits behind a transparent-background control and
paints marks at the same coordinates as the real glyphs. The two must share
font, padding, border width, line height, and wrapping or the marks drift, which
is why `mockup-validation.css` sets all of it explicitly rather than inheriting
from the legacy stylesheet.

This works on textareas as well as inputs — the backdrop uses `pre-wrap` to
reproduce textarea wrapping, and syncs `scrollTop` on the control's scroll
event. The control stays in normal flow inside the wrapper while the backdrop is
absolutely positioned, so the wrapper's height follows the control and dragging
a textarea's resize handle keeps the marks aligned for free.

Two details that are easy to miss:

- **Build the backdrop with text nodes, never `innerHTML`.** The value is author
  input, on a page whose whole purpose is rejecting HTML in author input.
- **Drop the marks on first edit.** Offsets go stale the moment the user types.
  The message stays — it still names what to look for.

**Needs client-side JS**, so this is the "later" capability. Today the message
alone carries it, and that is already better than echoing the field.

### 2.7 Process step

- **Placement: the form column, right-aligned, above the first field and below
  the last.** Not the sidebar — the sidebar is where you go when you are *done*
  with the form, and Process is something you do *to* the form.
- **Both ends.** Someone who fills in only the required fields never reaches the
  foot of the form; someone who works straight down it should not have to travel
  back up. Right-aligned so it lands where the eye leaves the last field.
- **Anchored by a rule, not floating.** Right-aligned in open space, the button
  attached to nothing and read as adrift. A thin rule directly beneath the row
  ties it to the form, so the actions and the fields they act on read as one
  block. Same structure as the admin-console
  [paper-details mockup](https://arxiv.github.io/design-system/mockups/internal/admin-console/paper-details/),
  with public tokens rather than that page's internal palette.
- **Something on the left.** The required-fields legend shares the top row —
  "fields marked \* are required" is about the form the button acts on, so the
  two belong together, and the row stops being a lone button in a wide space.

```html
<div class="form-actions form-actions-split">
  <p class="required-legend">Fields marked <span class="req-star">*</span> are required.</p>
  <button type="button" class="ds-btn ds-btn-primary" data-process>Process metadata</button>
</div>
<hr class="form-rule top">
<form> … </form>
<div class="form-actions form-actions-end">
  <button type="button" class="ds-btn ds-btn-primary" data-process>Process metadata</button>
</div>
```

Two details that make it work:

- **The rule is an `<hr>`, not a border on the row.** It separates two parts of
  the page, which is what the element is for, and it keeps the spacing above and
  below independent of the row's own box.
- **The margins are asymmetric** — tight to the buttons, open to the form
  (`0.75rem` / `1.75rem`). That is what makes the rule read as belonging to the
  action row rather than as a free-standing divider stranded between two things.
- **Only the top row gets a rule.** At the top it separates the actions from the
  fields below them. At the bottom there is nothing underneath to separate from
  — the last field already ends the form — so the line would be drawing a
  boundary that is not there. Plain space does the job.

**No explanatory paragraph.** A button saying "Process metadata" above a form,
with Continue greyed out until it is used, states the sequence by its own
arrangement. Prose is what you add once the arrangement has failed — and if
people do not find it, the first fix to reach for is a clearer arrangement, not
a sentence.

**There is no separate status line either.** The alerts are the result; a
running commentary beside the button only repeated them. The one piece of text
that survives is the hint under Continue, five words explaining why it is
unavailable, and that is feedback rather than instruction.
- **The explanation is permanent, not conditional.** It tells the user the step
  exists *before* they go looking for Continue and find it unavailable.
- The status line is `role="status"` with `tabindex="-1"`. Focus moves to it
  when processing finishes; otherwise focus stays on the Process button and a
  screen reader user is not told that anything happened.

### 2.8 Buttons and Continue gating

**All three buttons are now the design-system component**: `.ds-btn` with
`.ds-btn-primary` (Process, Continue) and `.ds-btn-secondary` (Go Back), lifted
verbatim from `docs/public/design-system.css` into section 8 along with the
tokens they need. Copied, not adapted — if these ever diverge, the design system
is right.

Worth adopting on its own merits, separately from anything else here: it brings
a real focus ring (3px, offset 2px) and a genuine disabled construction to a
page that has neither today. The font stack falls back to the system sans until
IBM Plex Sans is served, so it degrades rather than breaking.

One construction note, so nobody "simplifies" it: a single `border-color` cannot
carry a vertical gradient, so the button paints **two** backgrounds — one
clipped to `padding-box` (the fill), one to `border-box` (the border gradient) —
behind a `1.5px solid transparent` border. Hover *brightens* rather than darkens.

Two consequences of that construction, both of which bit during this build:

- **An undefined custom property invalidates the whole shorthand.** Because the
  fill and the border ride in one `background` declaration, a single missing
  token makes the button paint *nothing* — no fill, no border. It does not
  degrade to a plain button; it degrades to invisible. Check every token
  resolves before assuming the CSS is wrong somewhere else.
- **`.ds-btn` sets `box-sizing: border-box` here**, which the design system does
  not need to: its own pages are border-box already. Dropped into a page whose
  box model it does not control, `min-width: 120px` has to mean the whole button
  or two of them stop fitting a 22em sidebar.

> **The disabled state is a proposal, not a port.** Worth being precise about
> what the design system actually has, because it is less than it looks:
>
> - `docs/internal/design-system.css` has `.btn-primary:disabled`,
>   `.btn-secondary:disabled`, `.btn-tertiary:disabled`, with dedicated
>   `--lime-dis-*` / `--sec-dis-*` / `--danger-dis-*` tokens. Those buttons are
>   flat fills — the internal stylesheet contains **zero** `linear-gradient`
>   declarations — so they say nothing about what to do with the public button's
>   gradient border, inset vignette, and drop shadow.
> - `DESIGN-POLICIES.md:80` says *"Disabled state: `cursor: not-allowed`,
>   reduced opacity."* The internal implementation does **not** follow this — it
>   uses explicit `-dis-` tokens, not opacity. **The policy line and the only
>   implementation of it already disagree.**
> - `docs/public/design-system.css` has nothing for filled buttons, only
>   `.ds-btn-text:disabled`. And `docs/public/button-styles.html` — the public
>   button documentation page — does not contain the word "disabled" at all.
>
> So there is no rule to inherit. What follows was designed for this page and is
> offered for promotion.
>
> **Plain and dead.** One flat grey fill, muted grey label, no border, no
> shadow, no gradient, nothing that moves.
>
> ```css
> background: var(--arxiv-card-grey);      /* #f0eeec — neutral surface band */
> color:      var(--arxiv-library-grey);   /* #6b6459 — the muted-text token  */
> border-color: transparent;
> box-shadow: none;
> transform:  none;
> cursor:     not-allowed;
> ```
>
> **The label clears AA at 5.05:1.** WCAG exempts disabled controls from
> contrast, but a label nobody can read is worse than one they can. This is the
> only pairing in the warm grey ladder that is both genuinely muted and
> genuinely legible — `--arxiv-grey-ui` manages 3.12:1 on the same fill, and
> `--arxiv-repository-brown` passes at 15:1 but looks entirely live.
>
> **Both tokens flip in dark mode** (`#2b2723` fill, `#b0aba6` label, 6.51:1),
> so it holds in both without a hand-picked dark value.
>
> **The fill is faint against white — 1.16:1** — so the shape is carried by the
> label rather than by an edge. That is the trade for having no border, and it
> is the right way round: a control you cannot use should not assert itself. The
> palette has nothing between Card Grey and Border Light, and Border Light as a
> fill would drop the label to 4.13:1 and fail.
>
> **The 1.5px transparent border stays.** It draws nothing, but removing it
> would shrink the button by 3px in each axis and the disabled state would stop
> matching the shape of the live one.
>
> One rule covers both variants: the treatment is neutral, so it does not depend
> on which button it replaces.

- **Placement:** Go Back at the left of the sidebar row, Continue at the right,
  on one line (`justify-content: space-between`). The row reads in the direction
  of travel, and Continue stays on the side it will always be on.
- **Markup:** `aria-disabled="true"` — **not** the `disabled` attribute.

This is the one recommendation I would push hardest. A `disabled` button is
removed from the tab order and skipped by screen readers, so a user who cannot
proceed finds nothing there and no explanation of why. `aria-disabled` keeps the
button focusable and announced, and the click handler explains what is missing.
The cost is that `aria-disabled` does not block activation on its own, so the
handler has to call `preventDefault()`.

**The reason lives in a tooltip on the button itself.** A note under the button
row read as belonging to Go Back and Continue equally, when it only ever
described Continue. Attaching it to the control it explains removes the
ambiguity, and it appears only when it applies.

> This works **only** because Continue uses `aria-disabled`. A truly `disabled`
> button is out of the tab order and does not fire pointer events in every
> browser, so a tooltip on one is unreachable by keyboard and unreliable by
> mouse. This is the concrete payoff of that choice.

The copy is deliberately generic:

> Process and resolve any errors before continuing

On a form nobody has filled in yet there is no way to know whether there *will*
be errors, so the message must not claim there are any. One string covers every
unavailable state, which also retires the second, error-specific hint.

**No tooltip exists in the design system.** `.ds-popover` is a heavier
click-triggered panel with a title and close button, for citation and footnote
context. This is a new component borrowing the popover's material — tint fill,
tint border, 6px radius, 13px text — so the two read as the same family.
Promotion candidate.

It satisfies WCAG 1.4.13, which the page's existing help bubbles fail:

| Requirement | How |
|---|---|
| Hoverable | The host wraps the button, and the visual gap is the tooltip's own `padding-bottom`, not margin — the pointer never crosses dead space |
| Dismissible | Escape closes it without moving focus; a flag stops the next pointer or focus event immediately reopening it |
| Persistent | Stays while hovered or focused. No timer |

**It opens downward.** Opening upward put it behind the sticky bar at the top of
the mockup, and raising `z-index` alone would only have papered over that: the
real arXiv header is sticky too, so a tooltip opening upward near the top of a
page collides there for the same reason. Downward has clear space under both
Continue buttons. The `z-index` is raised above the sticky bar anyway, so an
overlap anywhere else resolves in the tooltip's favour rather than hiding the
only explanation the user has.

Three more details that matter:

- **Focus is a trigger, not just hover.** A keyboard user has no hover, so
  without it the explanation would be mouse-only.
- **A visually-hidden span carries the same text and is always in the
  accessibility tree**, referenced by `aria-describedby`. A tooltip toggled with
  `hidden` leaves the tree when closed, so a description pointing at it can be
  missed. Both strings are written from one variable in JS and cannot drift.
- **A tap shows it too.** Touch has no hover, so the intercepted click surfaces
  the same tooltip. Focus stays put — the tooltip answers the question in
  place, and moving focus on top of that is motion the user did not ask for.

### 2.9 In-progress

- **Visual:** the button label is replaced with a spinner and "Processing…";
  the button gets `cursor: progress` and reduced opacity.
- **Placement: next to the button that started the work, not an overlay.** The
  work is scoped to one action, so the feedback belongs at that action. An
  overlay would imply the whole page is unusable.
- The text carries the state; the spinner is decoration. Under
  `prefers-reduced-motion: reduce` the animation stops and the ring goes
  static — per DESIGN-POLICIES, reduced motion covers everything, and a
  spinner is exactly what that rule is aimed at.

---

## 3. The flow

```
  Page loads
     │
     ▼
  NOT PROCESSED ──────────────► Continue unavailable
     │                          Hint: "Select Process metadata first."
     │  user selects Process
     ▼
  PROCESSING ─────────────────► Spinner in button, status "Checking…"
     │
     ▼
  Server: transform → validate
     │
     ├── any error? ──── yes ──► ERRORS
     │                           Summary: error, with links
     │                           Continue unavailable
     │                           Hint: "Correct the errors, then run Process again."
     │                              │
     │                              └── user edits, runs Process again ──┐
     │                                                                   │
     ├── warnings only? ─ yes ──► WARNINGS                               │
     │                            Summary: warning                       │
     │                            Continue AVAILABLE                     │
     │                                                                   │
     └── nothing? ────────────► ALL CLEAR                                │
                                 Summary: success                        │
                                 Continue AVAILABLE                      │
                                                                         │
  ◄────────────────────────────────────────────────────────────────────┘
```

Notes tier does not affect gating. Automatic corrections never block; they are
reported and the user continues.

Editing a field after processing does **not** re-enable Continue in this mockup.
See [Open questions](#6-open-questions).

---

## 4. What to port

### Page measure

`.layout-container` is capped at **1180px and centred**. This one is a proposal
rather than a port: a form field is a line of text you have to read back, and on
a wide display an uncapped column runs a title input past 1200px — unreadable in
exactly the way long body text is. Capping the layout also stops the sidebar
drifting further from the form as the window widens.

The horizontal padding in the same rule is only standing in for the header,
breadcrumb, and footer this mockup drops. The real page does not need it.

### Equal-height columns

The sidebar should be as tall as the form, so its left border runs the length of
the page. Flexbox does this by default — `align-items: stretch` — so it already
wanted to. Two rules stopped it:

```
arxivstyle.css:9489   body { display: flex; flex-direction: column; height: 100vh; }
base_edit.css:572     .layout-container { height: calc(100% - 130px); }
```

Because the body has a **fixed** height of one viewport, that `100%` resolves
against the viewport rather than against the content. The layout container is
therefore about a screenful tall no matter how long the form is; the form
overflows it, and the sidebar — which stretches correctly, to its parent — stops
where the parent stops. On a nine-field form the rail and its border end part
way down the page.

Nothing needs measuring or scripting. Let the body grow with its content, drop
the height off the container, and stretch does the rest:

```css
body              { height: auto; min-height: 100vh; }
.layout-container { height: auto; align-items: stretch; }
```

> **`height: 100vh` on the body is worth fixing independently of this.** It
> makes every percentage height in the document relative to the window instead
> of the page, and this is only the first place it shows. The standard form is
> `min-height`, which still fills a short viewport.

### The sidebar borders

Worth reading the history before changing anything here, because the current
state was not decided by anyone — it is what three passes of patching left
behind.

| Stylesheet | What it says about `.info-container` |
|---|---|
| `submit.css` | `border: 0`, transparent background, `border-left: 2px solid #a5d6fe`, soft shadow |
| `base_edit.css` | `border: 1px solid #ddd`, `background: #f9f9f9` |
| `submit_overrides.css` | `background: transparent !important`, `border-left: none !important`, `box-shadow: none !important` |

Read in order: the original design was a **single 2px Open Blue edge** — one
line, in the brand accent, doing one job. `base_edit.css` then boxed the rail on
all four sides and filled it grey. `submit_overrides.css` then removed the
background and the shadow, and removed the **left** border — the only one anyone
had designed — leaving the three nobody had.

So the rail today carries a top, right and bottom border it was never meant to
have, and is missing the one it was.

There is a second, smaller version of the same problem: `submit_overrides.css`
puts a `border-bottom` on `.info-container-top` while `submit.css` puts a
`border-top` on the `.message-body` directly beneath it, so **two lines are
drawn a few pixels apart** where one divider was intended.

Restored to the original intent:

- `.info-container` — one left edge, no box, no fill, no shadow
- `.info-container-top` — one `border-bottom`
- `.info-container-bottom` — one `border-top`
- `.info-container-middle .message-body` — no border at all
- Both dividers use `--arxiv-border-light`. The rail currently uses `#ddd`,
  `#d7d7d7` **and** `#d0d7de` — and that last one is a cool grey, which reads
  faintly blue against a warm palette.
- Everything in the rail aligns to one left edge. `submit_overrides.css` indents
  the centre copy by `1.25rem` with `!important`, setting it in from the buttons
  above and below it for no reason.

`mockup-validation.css` uses `!important` in exactly three declarations —
`border-left` on the container, `border-bottom` on the top block, and `padding`
on the centre block. All three are here, and all three exist only to beat
`submit_overrides.css`. When that override file loses its own `!important`
flags, delete these with them.

### CSS — port all of it

`mockup-validation.css`, sections 1 through 10. Section 11 is the scenario
switcher; delete it.

Section 8 (buttons) is separable from the rest and can ship on its own — it is
the "one small change" that gets the page accessible focus and disabled states
without adopting the design system wholesale. The file loads after the existing four stylesheets and
overrides them; nothing in the existing stylesheets needs to change.

### HTML — template changes

1. Move the message block from above the hint to **after** the input.
2. Add `field-required` to the labels of Title, Authors, and Abstract. On the
   other six, keep `.optional` and add the missing
   `<span class="label-optional">(optional)</span>` — including on Comments,
   which is optional and currently unmarked.
3. Add the required legend above the form.
4. Add the `#form-summary` container above the first field.
5. Add a right-aligned `.form-actions` block holding the Process button, above
   the first field and below the last. Leave the sidebar as Go Back / Continue
   only, plus the `data-continue` / `data-continue-hint` hooks.
6. Swap `class="button is-success"` and `class="button"` for
   `class="ds-btn ds-btn-primary"` and `class="ds-btn ds-btn-secondary"`.
7. Give each message an `id` and point the input at it with `aria-describedby`.
8. Remove the help-bubble anchors. Move each tooltip's sentence into the hint
   paragraph above the input, and add a plain text link to the help page where
   one is still warranted.
9. Wrap examples in a single `<code>` and prefix them with
   `<span class="hint-example-label">Example:</span>`.

### JS — port the gating, not the scenarios

| Part of `mockup-validation.js` | Port? |
|---|---|
| `SCENARIOS`, `[data-scenario]` handlers | **No.** Mockup scaffolding. |
| `renderField()`, `renderSummary()` | **As a reference.** Server-rendered today — these functions specify what the Jinja template must produce. |
| `setContinue()`, the Continue click handler | **Yes.** This is the gating, and it is small. |
| Process button in-progress state | **Yes**, if processing is asynchronous. If it is a full page POST, the in-progress state is the browser's own loading indicator and you can skip it. |
| `applyHighlight()` | **Later.** Needs client-side JS. |

### Server

The response needs to carry, per field: the tier, the message, and optionally
the offending substring. The tier drives everything else — class, glyph, whether
Continue is gated, and the summary's own tier.

---

## 5. Bugs found in the current page

Six, all worth fixing regardless of anything else in this proposal.

1. **`class="textareais-danger"`** on the abstract field, in
   `complete2_Add or Edit Metadata _ arXiv e-print repository.html` line 536.
   A missing space, so the error styling silently does not apply. The field
   shows an error message with no error state on the control.

2. **`aria-required="True"`** with a capital T, on every required field. ARIA
   values are lowercase. Assistive technology may not parse `True`, so the
   fields may not be announced as required.

3. **`aria-required="True"` on Comments**, which has no `required` attribute and
   is not marked required in the label. The field is announced as required and
   is not.

4. **The help-bubble links have no accessible name.** Each contains only an SVG
   with no title, so it is announced as an unlabeled link. Resolved by removing
   the bubbles — see §2.2.

5. **`<code>` is red**, and close enough to the error red to be
   indistinguishable. Covered in §2.2. A single line of CSS, and worth fixing on
   the live page immediately, ahead of everything else here.

6. **The word "(optional)" never renders.** `submit.css:142` styles
   `.label.optional span`, but no span is emitted. Only the grey label survives,
   which is color alone. Covered in §2.1.

### One implementation trap

`base_edit.css:595` sets `.info-container-top` and `.info-container-bottom` to
`display: flex` with the default row direction. Each block currently holds
exactly one child — the Go Back / Continue nav — so the direction never mattered
and nobody noticed. Putting four children in there (explanation, Process button,
status, hint) spreads them across the sidebar in a row.

`mockup-validation.css` fixes this with `flex-direction: column` and resets
`justify-content` from `flex-end`, which in a column would push the whole block
to the bottom. Expect to hit this the moment you add anything to the rail.

---

## 6. Open questions

**Does editing a field after processing invalidate the result?** Right now the
user could process, get a clean result, then change the title to something
invalid and continue. Options: re-gate Continue on any input event, or re-run
validation on submit and return them to the page. The second is more robust and
needs no JS. My recommendation is the second.

**Is the JS constraint architectural or a platform limit?** The notes imply
server-side validation, but the page already loads three scripts. If JS is
available, technique (b) and blur-time validation are much cheaper than assumed.

**Should the six non-core fields collapse into a disclosure?** DOI, journal
reference, report number, ACM, and MSC are exactly the fields the page's own
help text calls non-core, and they are all optional. The design system has
`.ds-acc` for this. Out of scope here, flagged as its own decision.

**Does the modal for upload-delete get built?** `.ds-alert` is an inline banner,
not a modal — it has no backdrop, no focus trap, no `z-index`. There is no modal
pattern in the design system at all. Confirming a destructive action does want a
real dialog, so that is a new component rather than a reuse.
