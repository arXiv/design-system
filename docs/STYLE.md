# Writing style

Rules for anyone — person or agent — writing text that ships: interface copy, error messages, instructions, and the docs in this repo.

[BRAND.md](BRAND.md) sets arXiv's voice. [DESIGN-POLICIES.md](DESIGN-POLICIES.md) states the hard rules. This file carries the rules in full, with the reasoning behind them.

---

## Two tiers

**Load-bearing text** — error messages, validation messages, form labels and help text, submission and upload instructions, empty states that block a task, and agent-facing docs in this repo. Every rule below is a requirement here.

**Everything else** — pattern page prose, rationale, planning and brand documents, announcements. BRAND.md's voice applies in full, dry wit included. The load-bearing rules are useful defaults here, not requirements.

BRAND.md already implies this split: the mischief belongs in "small, optional places … never in anything load-bearing or anything a stressed researcher has to parse." This file makes the strict half concrete.

---

## Rules that apply everywhere

### No contractions

Write "do not," not "don't." Write "it is," not "it's."

This is long-standing arXiv policy, not a preference. arXiv's readers are spread across every country and many of them read English as a second or third language. A contraction compresses two words into one and hides a word boundary, which costs a reader who is translating as they go. Possessives are unaffected: "arXiv's palette" is correct.

It applies to everything with words — interface copy, error messages, documentation, alt text, commit messages.

### Same word for the same thing, every time

An alert is an alert everywhere — never a notification, toast, banner, or message. Synonyms read as meaningful distinctions and send people looking for a difference that is not there. Component names in prose must match the names in the stylesheet.

---

### Category names are copied, never restyled

Show a category exactly as arXiv publishes it, capitalization included, and always with `.ds-tag--keep-case` when it is a tag. `cs.AI`, `physics.optics` and `cond-mat.str-el` are all correct as written. Uppercasing the lowercase ones produces strings that are not real categories: every `physics.*` and `cond-mat.*` subcategory is lowercase.

---

## Rules for load-bearing text

### One instruction per sentence, imperative and active

Write "Enter your email address," not "Your email address should be entered." A reader working under pressure loses their place when one sentence carries two actions.

### No idiom or metaphor in text someone reads while something is going wrong

Errors, warnings, and validation messages state what happened and what to do next. Figurative language adds a translation step that a frustrated or non-native reader should not have to pay for.

### Use articles; no telegraphic style

Write "The file is too large," not "File too large." Dropped articles and clipped fragments save a few characters and cost clarity, most of all for readers translating as they go.

---

## Where these came from

The no-contractions rule is arXiv's own, and it predates this document.

The rest are adapted from [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/) (Issue 9, 2025), a controlled-language standard written for aerospace maintenance documentation and for readers with limited English. STE happens to ban contractions as well, which is some outside confirmation that arXiv's rule earns its keep.

We took the rules that fit and left the rest. STE also caps sentence length, bans all figurative language, and restricts writers to an approved dictionary of roughly 900 words — which would remove the voice BRAND.md commits to, and would need a word list maintained by hand. The parts kept here are the ones that help non-native readers without costing anything to maintain.
