# Submission metadata — form UX/UI and validation

A proposal for form UX/UI and validation on the "Add or Edit Metadata" page. This is a work in progress, and a reference, **not production code**.

## Demo
**Open `index.html`.** The dark bar at the top switches between five states. The Process button runs the flow so you can see the mocked-up errors and user messaging. If I left out any useful error states or messages we can easily add them in.

| File | What it is |
|---|---|
| `index.html` | The mockup described above |
| `mockup-validation.css` | All stylesheet changes proposed in the mockup. Eleven sections with reasoning behind each decision in comments written by Claude |
| `mockup-validation.js` | All user feedback proposals from the mockup: rendering, gating, tooltip, and in-progress. Comments for each written by Claude |
| `arxivstyle.css` · `submit.css` · `base_edit.css` · `submit_overrides.css` | CSS used to recreate this snapshot of the Submission 2.0. **Not using the design system.** |

The mockup loads the submission system's own stylesheets rather than the design system's and new stylesheet work is confined to `mockup-validation.css`. I used design-system class names though, for easier porting and sharing of patterns.

## The validation model

Two dispositions matching QA's vocabulary, plus a third signal for neutral 'info'.

| Tier | Meaning | Continue? | Colour |
|---|---|---|---|
| **Error** | Rejection. The value is not acceptable | No | Red `#c62828` |
| **Warning** | Accepted, but the submission may be held for moderator review | Yes | Amber `#e8b800` |
| **Note** | arXiv changed a value automatically. Not an error, just info for the user | Yes | Blue `#5a82c8` |

A **note** example: Whitespace normalisation and sanitisation are two types of edits to author-submitted content that you mentioned, Carly. Per your philosophy of transparency and user confirmation we point out the changes, but they are distinguishable from error reporting. 

---

## Components

| Component | Class | Where it goes | Appears |
|---|---|---|---|
| Optional marker | `<span class="label-optional">` | Inside the label | On optional fields only. Required fields carry no marker, they are the default |
| Hint | `.help.has-text-grey` | Between label and input | Always |
| Hint example | `.hint-example-label` + one `<code>` | Inside the hint | As needed |
| Field message | `.field-error` / `.field-warning` / `.field-note` | **After** the input | One per problem |
| Multiple field messages | `<ol class="field-messages">` | After the input | When a field has 2+ problems |
| Field state | `.is-invalid` / `.is-warning` / `.is-note` | On the control | Worst tier present |
| Validation summary | `#form-summary` › `.form-summary.form-summary-{tier}` | Above the first field | After processing, one alert per severity |
| In-field highlight | `.field-highlight` wrapper, `mark.mark-{tier}` | Wraps the control | When a problem names a substring |
| Match chip · Show me | `.field-match` · `.field-locate` | Inside the field message | Same |
| Process action row | `.form-actions` + `<hr class="form-rule top">` | Above the first field, and below the last | Always |
| Continue gating | `aria-disabled="true"` | Sidebar nav | Until processed with no errors |
| Disabled reason tooltip | `.ds-tooltip-host` › `.ds-tooltip` + `.is-sr-only` description | Wraps Continue | On hover, focus or tap, while unavailable |
| In-progress | `.spinner` inside the button | Process button | During the request |
| Buttons | `.ds-btn` + `-primary` / `-secondary` | Process, Go Back, Continue. Note that 'Disabled' is a state, not a class | Always |

**A few other rules in the mockup:**

1. **Messages go after the input.** The current page renders them above the hint and above the input. It is too far away from what they describe, and causes the input to jump down the page.
2. **Every message needs `id` + `aria-describedby`** on its input, and for errors they need `aria-invalid="true"`. Without it a screen reader announces the field and nothing else.
3. **One alert per severity; don't mix them.** Red alerts always mean "you cannot proceed". Mixing together a non-blocking item inside a red alert confuses the message. Multiple alert boxes for each color are OK. See an example in the mockup tab for "Errors + warnings"
4. **The alert heading includes a count.** This is a 'very nice to have' if it is technically feasible. A heading label like "2 blocking errors" or "3 warnings" conveys the amount of work and the urgency very efficiently. If it is not possible to include the count just let me know, we'll figure out something else.
5. **Continue uses `aria-disabled`, not `disabled`.** A disabled button leaves the tab order and screen readers skip it, so a user who cannot proceed finds nothing there and no explanation. `aria-disabled` keeps it reachable and lets it carry the tooltip. A screen reader then announces all three parts: the name, the state, and the reason ("Process and resolve any errors before continuing"). The reason lives in a visually hidden `<span>` that `aria-describedby` points at, not in the tooltip itself. That detail is important because the tooltip is toggled with `hidden`, which takes it out of the accessibility tree while it is closed, so pointing `aria-describedby` straight at the tooltip would leave the button undescribed most of the time. Both the span and the tooltip get their text from one variable in the JS, so the two cannot drift apart.
6. **Red always means error.** Nothing else should use red, including the `<code>` elements used in examples above the fields. The mockup has changed their color.
7. **Label optional fields in text; leave required fields unmarked.** We only indicate optional fields because, on five of six submission pages, we only have required fields to display. Required fields still carry `required` and `aria-required="true"`, which is the part a screen reader announces. For optional field labeling, nothing is as universally understood as a text label, so we use a word rather than a symbol.
8. **Disable "Continue" button until processing reveals no blocking errors**. Per our discussion, the review step is what currently provides the user with the opportunity to review and confirm changes. In later iterations of Submission we may be able to replace the review step with more instant JS-powered user messaging, but for now this step is needed, so Continue stays unavailable until processing comes back clean (using `aria-disabled`, per rule 5).
9. **Sidebar CSS cleanup**. The sidebar CSS had gotten quite messy and harder for users to quickly grok what is going on. Applying these styles cleanly to this page can provide a good template for other pages too.

---

## What to port

### CSS
`mockup-validation.css` sections 1–10. Section 11 is the scenario switcher; delete it. This css file should load after the existing four stylesheets and will override them, so no existing css files need to change.

### HTML
1. Move the message block to **after** the input.
2. Add `<span class="label-optional">(optional)</span>` to the six optional
   labels, Comments included. Leave the three required fields unmarked, and
   keep `required` and `aria-required="true"` on their controls.
3. Add the `#form-summary` container above the form.
4. Add the `.form-actions` row with the Process button, above the first field
   and below the last, with `<hr class="form-rule top">` under the first.
5. Swap `class="button …"` for `class="ds-btn ds-btn-primary"` /
   `ds-btn-secondary`; leave the sidebar as Go Back / Continue.
6. Wrap Continue in `.ds-tooltip-host` with its tooltip and `aria-describedby`.
7. Give each message an `id` and point its input at it.
8. Replace the help-bubble anchors with visible hint text plus a plain text link
   named for its field ("See title formatting help").
9. Wrap examples in one `<code>` with an `Example:` label.

### JS
| Part | Port? |
|---|---|
| `SCENARIOS`, `[data-scenario]` handlers | **No.** Scaffolding |
| `renderField()`, `renderSummary()` | **As a reference**. Server-rendered today, so these specify what the template should produce |
| `setContinue()`, the Continue handler, the tooltip | **Yes.** Small, and adds useful explanations for users about button state |
| Process in-progress state | **Yes**, if processing is async. On a full page POST the browser's own loading indicator covers it |
| `applyHighlights()`, `selectNextMatch()` | **Possibly later** because it needs client-side JS. Up to you. |

### Server
The response needs, per field: tier, message, and optionally the offending substring. The tier drives everything else — class, glyph, gating, and the summary's own tier.

---

## Things Claude noticed while building

Goes beyond design feedback, but I recorded them in case any of it is useful (all verified against `develop`, which perhaps is not the right branch?).

- **`add_metadata.html:60`** — `class=[class, "is-danger"]|join` uses Jinja's
  `join` with no separator, producing `textareais-danger` and `inputis-danger`.
  The error styling has never applied to any field on the page. `|join(" ")`.
- **`aria-required="True"`** with a capital T. ARIA values are lowercase, so
  assistive technology may not parse it.
- **Comments is passed without `required=False`**, so it is announced as
  required and marked as such when it is optional. (Also check for capitals)
- **Multiple errors on one field** are looped into a single `<div>` with no
  separator, so two errors concatenate into one run-on line.
- **The help-bubble link has no accessible name** at rest — it contains only an
  SVG plus `.bubble-text`, which is `visibility: hidden` and therefore out of
  the accessibility tree until focused.
