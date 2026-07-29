# Options 3 & 5 on arxiv-browse and arxiv-search — a current-state review

*Draft for discussion. Reviews the real state of `arxiv-browse`, `arxiv-search`, and their shared `arxiv-base` (June 2026), then walks through exactly how [Option 3 (package)](dev-workflow-comparison.html) and [Option 5 (self-verifying spec)](fifth-option-self-verifying-spec.md) would land on each. Ends with a constraints inventory for the dev-team vision.*

---

## The one-paragraph picture

The premise "design is shared via `arxiv-base`" is **already only half true**. `arxiv-search` still inherits its entire look from `arxiv-base` (`{% extends "base/base.html" %}` → Bulma 0.7.2, Open Sans from Google Fonts, Campus Red as `$primary`). But `arxiv-browse` has **left**: its `base.html` no longer extends base — it writes its own HTML shell and only *imports* base's macros, ships ~20 hand-written CSS files with no framework and no build step, and has already reimplemented the new spinout design by hand (self-hosted IBM Plex, Repository Brown `#1c1a17`, Link Blue `#1565c0`, a `:root` custom property). So today there are **three** design states, not one: the old design (in base, still driving search), the new design (hand-coded in browse), and the canonical new design (this repo's tokens), which isn't wired into any of them yet. That divergence is the thing the dev-team vision has to resolve, and it's what makes Options 3 and 5 land so differently on each repo.

---

## Current state, side by side

| | **arxiv-base** | **arxiv-browse** | **arxiv-search** |
|---|---|---|---|
| Role | Shared design + templates package | Abstract/listing app | Search UI + API |
| base dependency | — | git **`branch=master`**, 1-min freshness (rolling) | git **`rev=1.0.1`** (but `Pipfile` pins commit `ed3feece`, `poetry.lock` resolved `1.0.0a5`) |
| Uses base's layout? | n/a | **No** — own `base.html`, imports macros only | **Yes** — `extends "base/base.html"` |
| CSS approach | SASS + **Bulma 0.7.2**, manual `sass` compile | ~20 **hand-written CSS** files, **no build, no framework** | tiny `search.sass` (144 ln) + base's Bulma |
| Design tokens | SASS vars (`$red-dark`, `$primary`) | hardcoded hex + **one** `:root` var (`--arxiv-font-sans`) | hardcoded hex |
| Fonts | **Open Sans via Google Fonts** ⚠ | self-hosted **IBM Plex** woff2 ✓ | inherits Open Sans ⚠ |
| Palette vs policy | **`$primary = #b31b1b` (Campus Red)** ⚠ | new palette, hand-coded ✓ (values match this repo) | inherits old palette ⚠ |
| Asset delivery | versioned static path `/static/base/{VERSION}/` + Flask-S3/CDN | `?v=YYYYMMDD` query params, Flask-S3 | `url_for('static')`, Flask-S3 |
| Runtime | — | Flask 3, Python 3.11 | **Flask 2.2, Python 3.10** (older) |
| Front-end gates | ruff + type + selenium; **no CSS/a11y lint** | ruff + pytest 80%; **no CSS/a11y lint**; has `ACCESSIBILITY_REMEDIATION_PLAN.md` (16 WCAG 2.2 issues) | flake8 **disabled**, pylint/mypy; **no CSS/a11y lint** |

⚠ = live conflict with a `DESIGN-POLICIES.md` guardrail (no external fonts; Campus Red is heritage-only).

Two structural facts drive everything below:

1. **The version contract is broken.** Browse rolls on `master`; search is pinned three different ways across three files. Neither Option 3 nor Option 5 works without a single deterministic version pin — this is the #1 blocker, independent of which option you pick.
2. **base itself is the old design**, and ships two of the policy violations (Google Fonts, Campus-Red-primary) to every app that still inherits from it (i.e. search).

---

## Option 3 (package) — exactly how it lands

*Shared idea:* this repo publishes a **framework-agnostic artifact** — a DTCG `tokens.json` plus a plain-CSS `design-system.css` (the `--arxiv-*` custom properties + component classes you already maintain), versioned and shipped over the static/CDN path base already has. Per-framework builds are optional extras. Then:

**arxiv-base** — *best structural fit, biggest semantic lift.*
base is *already* the shared package with versioned-static + S3 machinery, so it's the natural host. The work: regenerate base's SASS variables from `tokens.json` (Style Dictionary can export SASS), or replace `arxivstyle.sass`'s hardcoded `$primary`/`$red-dark`/Open Sans with token-derived values; ship `design-system.css` alongside base's templates. **But tokens alone don't deliver the redesign** — base's `header.html`/`footer.html`/Bulma chrome are the *old structure*. To actually modernize search-via-base you must also bring base's chrome up to the new header/footer (the work browse already did independently). Then a version bump flows the redesign to every consumer.
- *Wins:* search and any base-consumer get the redesign by a version bump, no agent required; reuses the CDN you already have.
- *Friction:* the package stays **Flask/Jinja+SASS+Bulma-specific** — not stack-agnostic (Option 3's known 1/4). Bulma 0.7.2 is ancient and coupled. Requires the version contract fixed first.

**arxiv-browse** — *cleanest drop-in for the CSS artifact.*
Browse already uses plain CSS + `:root` custom properties + the new palette — it just hardcodes the hex. Option 3 here = link the published `design-system.css` and mechanically replace literals (`#1c1a17`, `#1565c0`, …) with `var(--arxiv-*)`. Because browse has **no build step**, the plain-CSS artifact drops in with zero tooling — browse is the ideal home for the no-build CSS file. Browse keeps its own templates (it's effectively the reference implementation of the new chrome).
- *Wins:* converts hand-coded drift into referenced tokens; no build to set up; browse stops being a private fork of the design and becomes a versioned consumer of it.
- *Friction:* someone refactors ~20 CSS files (legacy `arXiv.css` from 2024 + new `arxiv-header-footer.css`); move from `?v=date` to a real version pin.

**arxiv-search** — *smallest surface, most coupled.*
Two paths: **(a)** if base adopts tokens + the new chrome (above), search inherits the redesign almost for free — it only has 4 templates and 144 lines of SASS; **(b)** if search wants the new look without waiting on base, it links `design-system.css` and stops extending the old base layout — a bigger change to its `base.html`. Cleanest is (a): let base own it, search version-bumps.
- *Wins:* least work; inherits via base.
- *Friction:* fully hostage to base's release cadence and the Bulma chrome; blocked by the messy pin **and** the old Flask 2.2/Python 3.10 runtime.

---

## Option 5 (self-verifying spec) — exactly how it lands

Option 5 **keeps Option 3's artifact as Layer 1** and adds Layer 2 (this repo's `CLAUDE.md`/`BRAND.md`/policies as agent-readable intent, plus an `AGENTS.md`) and Layer 3 (the **conformance checks**, runnable in each repo's CI). The workflow is: a dev runs Claude Code pointed at the repo + this spec, says "make it so," the agent builds against the tokens **and proves conformance against the checks**, and surfaces gaps back as PRs to this repo.

**arxiv-base** — *this is the killer demo.*
Point the checks at base **today** and they light up with exactly the violations we found by hand: the `fonts.googleapis.com` `@import`, `$primary = #b31b1b` (Campus Red as a primary, not heritage), missing `:focus-visible`, and any failing contrast pairs. An agent run — "migrate `arxivstyle.sass` and the chrome to the design system" — does the token migration + header/footer modernization, then the checks confirm the violations are gone before a human looks. Gaps ("Bulma component X has no token equivalent") become contributions back here. Option 5 turns "the designer must *remember* base still uses Campus Red" into a CI failure that blocks the merge.

**arxiv-browse** — *the obvious pilot.*
Highest traffic, redesign already in flight, no build tooling to fight, and an existing `ACCESSIBILITY_REMEDIATION_PLAN.md` with 16 WCAG 2.2 issues. One agent pass against the spec does the hardcoded-hex→token refactor *and* works the a11y backlog (keyboard traps, focus indicators, link-contrast); the contrast / `:focus-visible` / palette-allowlist checks then prove it. Crucially, Option 5 converts that one-time remediation plan into **standing checks** so the 16 issues can't silently regress — which is the whole point for a one-designer team. When the agent needs a color not in the palette, it proposes a token rather than hardcoding one.

**arxiv-search** — *fast follow.*
Small enough that an agent can migrate all 4 templates + `search.sass` off the old base chrome onto the tokens in one pass, with the checks catching any residual Bulma/Open Sans/old-palette inheritance. But the agent will immediately surface search's real blockers — the inconsistent base pin and the Flask 2.2/Python 3.10 runtime — because it can't cleanly "make it so" on an inconsistent dependency graph. That's a feature: Option 5 makes the hidden constraints visible.

---

## Constraints inventory (for the dev-team vision)

**Remove — actively blocking either option:**

- The **rolling `branch=master` pin** in browse and the **three-way-inconsistent** base pin in search. A single deterministic version contract is a hard prerequisite for *both* options. This is the first thing to fix regardless of direction.
- **Google Fonts `@import`** in `arxiv-base` (external dependency + policy violation).
- **Campus Red as `$primary`** in `arxiv-base`.

**Loosen — coupling that limits the ceiling:**

- **Bulma 0.7.2** in base — ancient and framework-coupling; it's why the base package can't be stack-agnostic. Move toward token-based plain CSS (the direction browse already proves works).
- **Manual SASS compile** in base — replace with token export (Style Dictionary / a DTCG pipeline) or drop SASS for plain `--arxiv-*` custom properties to match browse and this repo.
- The implicit rule that **"all shared design flows through base templates"** — it already doesn't (browse left). Make this a deliberate decision rather than an accident (see below).

**Keep / build on — these are assets, not debt:**

- base's **versioned static-path + Flask-S3/CDN** delivery — the ideal vehicle for a versioned `design-system.css`. Reuse it.
- browse's **plain-CSS, no-build, self-hosted-IBM-Plex, `:root`-token** approach — that *is* the target architecture; it only needs tokenizing.
- **git as source of truth + Poetry package-data** — keep.

---

## The strategic question to settle first

Where does the design actually live? Three coherent futures:

- **A — base stays the design home.** This repo feeds tokens into base; base ships them; consumers inherit. Simplest, but **browse already voted against it with its feet**, so you'd be re-merging browse back under base.
- **B — this repo becomes the published artifact.** base and browse both *consume* a versioned `design-system.css`; base stops being the design home and goes back to being "Flask utilities + templates." This is Option 3, done cleanly.
- **C — this repo is the spec + checks.** Each repo consumes the tokens *and* is verified against the policies in CI, with browse as the pilot and a contribution loop back here. This is Option 5.

B and C aren't exclusive — C is B plus the verification/contribution layer. The review suggests the honest sequence is: **fix the version contract → adopt the token artifact (B) → pilot the checks on browse (C) → roll checks to base (where they immediately pay off) → search last.**

## What I'd verify before committing

- Whether this repo's `design-system.css` token *values* already match browse's hand-coded hex (spot check suggests yes — same Repository Brown, same Link Blue). If so, browse's refactor is near-mechanical.
- Whether base's `header.html`/`footer.html` and browse's hand-built chrome can converge on one set of macros, so the redesign isn't maintained twice.
- The real cost of the search runtime bump (Flask 2.2 → 3, Python 3.10 → 3.11), since it gates search either way.
