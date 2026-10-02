# A fifth option: the self-verifying living spec

*Draft for discussion — companion to [the four-option workflow comparison](dev-workflow-comparison.html). Argues that the four options share a blind spot, adds five evaluation criteria, proposes a fifth option, and grounds it in how future-focused orgs are building front-end today (June 2026).*

---

## The short version

The four options in the comparison all answer one question: **how should a dev repo *consume* the design system?** (Copy it by hand, prototype it in a tool, link it as a package, or split it.) None of them answer the two questions that actually decide whether brand fidelity survives across many repos with a team of one designer:

1. **How does anyone *know* the output is compliant** — without the designer reviewing every PR?
2. **How does a fix discovered during implementation get *back* into the source of truth** — without routing through the designer as a manual gate?

A fifth option falls out of taking those two questions seriously. Call it the **self-verifying living spec**: the design-system repo ships not just tokens and guidance but the **checks** that prove conformance, and a **contribution loop** that lets implementation feed the spec. The repo stops being a document devs read and becomes **infrastructure an agent both builds from and is verified against** — with the designer owning the spec and the checks, not the pixels.

This is not a speculative bet. It's roughly where Anthropic, Google, GitHub, Indeed, Spotify, and New York State have already converged (see [What the field is doing](#what-the-field-is-doing-june-2026)). And arXiv is unusually well-positioned for it, because the guardrails in `CLAUDE.md` are already written as checkable assertions.

---

## Five criteria the four options don't test

The original goals (designer-not-a-bottleneck, agentic adaptation, dev empowerment, git as home, "make it so," cross-repo brand fidelity) are about *capability and ownership*. These five are about *whether the system holds up in practice*:

| # | Criterion | The question it asks | Why the four options miss it |
|---|---|---|---|
| C1 | **Conformance / verification** | How is compliant output *proven*, not hoped for? | All four leave correctness to human review. For a one-designer team, review *is* the relocated bottleneck. |
| C2 | **Two-way contribution + governance** | How does an implementation-time fix flow back to the source of truth and out to every repo — and who arbitrates? | All four are one-directional (system → repo). Goal #3 (devs improve the system) has no described mechanism. |
| C3 | **Resilience / no lock-in** | Does the source of truth stay useful if the model, vendor, or tool changes? | Option 2 needs Claude specifically; "lives in git" can quietly become "only one agent can use it." Matters for a 30-year institution becoming an independent nonprofit. |
| C4 | **Authored for agents, at scale** | Is the guidance structured so an agent reliably loads and applies it as it grows? | "Pack in lots of context" only works if the context is machine-readable and token-efficient. Prose docs degrade fast (see Indeed's benchmark below). |
| C5 | **Incremental, per-repo adoption** | Can a repo adopt partially and coexist with un-migrated legacy? | arXiv spans Flask/Jinja + React, PHP, Perl/CGI, static HTML. No big-bang rewrite is viable. |

C1 and C2 are the heart of the fifth option. C3–C5 are framing that keeps it honest for arXiv specifically.

---

## What the field is doing (June 2026)

A clear pattern has formed across teams that build front-end with agents. Three moves recur, and together they describe the fifth option.

**1. The design system is treated as infrastructure, not a document.** The framing from the AI Design Systems Conference 2026 is blunt: *"I see the design system as infrastructure, the same way you see your CI/CD pipeline or database — an API that allows AI to build your product safely"* (Romina Kavcic). *"AI generates code; design systems generate understanding. Without a strong system, AI collapses toward the average of the internet."* The corollary: *"AI is a new user, and as a new user our design system needs to be in a format the AI can understand"* (Diana Wolosin, Indeed). ([Into Design Systems: Agentic Design Systems](https://www.intodesignsystems.com/agentic-design-systems))

**2. Conformance is built into the generation loop — the system checks the agent's output.** This is the missing piece in all four options, and it's now table stakes:

- **Anthropic's Claude Design** imports a design system from a GitHub repo, then *"builds with those components, checks its output against the design system, and makes corrections before users see the result."* It added admin governance to *"approve one standard design system and lock down edits."* ([TechRepublic, Jun 18 2026](https://www.techrepublic.com/article/news-anthropic-claude-design-overhaul-enterprise-teams/); [Anthropic](https://www.anthropic.com/news/claude-design-anthropic-labs))
- **Google's DESIGN.md** (open-sourced, Apache 2.0, early 2026) ships a CLI linter — `npx @google/design.md lint` — that checks **WCAG AA contrast (4.5:1)**, broken token references, orphaned tokens, section order, and missing typography, and a `diff` command that exits non-zero on regressions. ([designmd.app](https://designmd.app/what-is-design-md/); [spec on GitHub](https://github.com/google-labs-code/design.md))
- **GitHub Primer** runs agentic daily QA with sub-agents (e.g. an accessibility reviewer) under "safe outputs" — an agent can only *open an issue*, never merge unreviewed. **Indeed** ran 1,056 prompts to benchmark formats before committing. **Spotify Encore** built a custom MCP evaluation framework comparing generated components against the system both in code and visually. ([Into Design Systems](https://www.intodesignsystems.com/agentic-design-systems))

**3. The spec is two-layer: machine-readable tokens + human-readable intent, in one git file, plus a governed contribution loop.** This is the convergent format:

- **DESIGN.md** = YAML token front-matter (exact values for machines) + Markdown prose (the *why*, plus an explicit **Do's and Don'ts** section, because *"LLMs respond well to negative instructions"*). Framework-agnostic, no build step, `export` to Tailwind or W3C DTCG tokens when needed. *"DESIGN.md is to design what AGENTS.md is to code conventions."*
- **The W3C Design Tokens spec reached its first stable version (2025.10)** in October 2025 — a vendor-neutral `tokens.json` format now supported by Figma, Style Dictionary, Penpot, Tokens Studio, and others. Tokens are finally portable across tools and stacks. ([Design Tokens Community Group](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/))
- **AGENTS.md** became the cross-tool instruction standard (OpenAI, Google, Sourcegraph, Cursor, Factory; donated to the Linux Foundation, Dec 2025) — plain Markdown any agent reads. ([AGENTS.md guide](https://www.morphllm.com/agents-md-guide))
- **Indeed's benchmark** is the cost argument for structuring it this way: feeding Markdown prose to an MCP burned ~30,000 tokens/query at 82% accuracy with hallucinations; **JSON metadata hit higher accuracy with ~80% fewer tokens and 5× lower annual cost** ($300 vs $1,500). Rule of thumb: *JSON for the contract (tokens, props, states), Markdown for the rules an LLM reasons over.* ([Into Design Systems](https://www.intodesignsystems.com/agentic-design-systems))
- **Governance is by trust level, not full autonomy** (a MAPE-K "observe → detect → suggest → fix → learn" loop): mechanical, high-confidence fixes can auto-merge; anything touching the canonical spec is suggest-only and human-reviewed. *"You don't want agents running in the wild."*

**How Anthropic itself works** rounds out the picture: the majority of code is now written by Claude Code, and engineers *"focus on architecture, product thinking, and continuous orchestration… giving direction and making the decisions that shape what gets built"* rather than typing implementation. ([How Anthropic teams use Claude Code](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)) That is exactly the role shift the fifth option asks of arXiv's designer.

---

## Option 5 — the self-verifying living spec

The design-system repo stays the single source of truth and ships **three layers**, all in git, all plain text:

**Layer 1 — Invariants as a portable artifact (the part that needs no agent).**
The tokens you already keep in `design-system.css` `:root`, exported once to a W3C DTCG `tokens.json`, plus the plain-CSS custom-properties file you already have. Any stack links the CSS with no build step (covers Perl/CGI, PHP, static HTML); React/Jinja can consume the tokens directly. This is Option 3's strength, kept.

**Layer 2 — Context + intent as an agent-readable spec (the part that lets agents adapt).**
Your `CLAUDE.md` + `BRAND.md` + `color-mapping.md` + `typography.md`, plus a sibling `AGENTS.md` so non-Claude agents work too. Structured the DESIGN.md way: machine-readable values in token form, human prose for rationale, and your guardrails restated as an explicit **Do's and Don'ts** block. This is what lets an agent handle a situation the spec never anticipated — it reasons from encoded intent, not just literal rules (Goal #2).

**Layer 3 — Conformance as code (the missing piece).**
The repo ships the **checks** themselves, runnable in any consuming repo via one CI action. Almost every arXiv guardrail is mechanically checkable already:

| Guardrail (from `CLAUDE.md` / policies) | Becomes a check |
|---|---|
| Palette is closed (`color-mapping.md`) | Lint: flag any hex not in the token set |
| Type stack is closed (`typography.md`) | Lint: flag `font-family` outside the stack |
| No Google Fonts / external font loading | Lint: flag `fonts.googleapis.com`, `@import` of external fonts |
| WCAG AA contrast (4.5:1 text / 3:1 UI) | Contrast check on token pairs (the DESIGN.md linter already does this) |
| `:focus-visible`, never bare `:focus` | Lint: flag `:focus {` without `-visible` |
| Cornell/Campus Red is heritage-only | Lint: flag Campus Red as a primary/action color |
| Access Lime is internal-only; Open Blue is public-only | Lint: flag lime in public pages, Open Blue in internal |
| No paper metrics (views/downloads/citations) on public pages | Lint: flag metric components in public templates |

The point: **your policies are already a lint spec in prose.** Layer 3 is mostly transcription, not invention — and it can lean on existing tools (the DESIGN.md linter, custom ESLint/stylelint rules, a contrast checker) rather than a bespoke build.

### The loop

A dev runs Claude Code (or any agent), points it at new content and the design-system repo, and says *"make it so."* The agent:

1. **Generates** code using Layer 1 tokens and Layer 2 intent.
2. **Verifies** it against Layer 3 checks and self-corrects — the same build-then-check move Claude Design already does internally.
3. **Surfaces gaps**: where the spec gave no guidance, or a check had to be overridden, the agent opens a **structured contribution** back to the design-system repo (a proposed token, a flagged ambiguity, a suggested rule). Per trust levels, mechanical changes can auto-merge; anything touching the canonical spec is a suggest-only PR **you** review.

The designer's job moves from *implement-and-review-everything* to **own the spec and the checks**. You review changes to the source of truth — not every downstream PR in every repo. The checks do the cross-repo policing that one person never could. That is how Goal #1 (not a bottleneck) and cross-repo fidelity become true at the same time, instead of trading off.

### Why this is genuinely a fifth option, not "Hybrid plus"

Option 4 still describes *consumption* — it splits the system into a package for invariants and an agent path for flexible parts. Option 5's new ingredients are **the verification layer (C1)**, **the contribution loop and trust-level governance (C2)**, and **treating the repo as agent-consumable infrastructure (C4)**. The first four options have no feedback mechanism at all; drift can only be caught by a human looking. Option 5 closes the loop. It also tends to *collapse* the fidelity-vs-flexibility tradeoff the other options pick a point on: the checks guarantee fidelity, which is precisely what makes it safe to let the agent be flexible.

---

## Scorecard

Option 5 on the comparison's original axes, plus the five new criteria (out of 4):

| Axis | Opt 1 Manual | Opt 2 Claude Design | Opt 3 Package | Opt 4 Hybrid | **Opt 5 Self-verifying spec** |
|---|---|---|---|---|---|
| Design fidelity | 1 | 2 | 3 | 4 | **4** |
| Easy to use | 1 | 3 | 4 | 3 | **3** |
| Simplicity | 4 | 3 | 2 | 1 | **2** |
| Stack agnostic | 4 | 3 | 1 | 3 | **4** |
| Agent agnostic | 4 | 1 | 4 | 3 | **4** |
| C1 Conformance | 1 | 3 | 2 | 2 | **4** |
| C2 Two-way contribution | 1 | 1 | 1 | 2 | **4** |
| C3 Resilience / no lock-in | 3 | 1 | 4 | 3 | **4** |
| C4 Authored for agents | 1 | 2 | 3 | 3 | **4** |
| C5 Incremental adoption | 3 | 2 | 2 | 3 | **4** |

The honest weak spot is **Simplicity (2/4)**: setting up Layers 2–3 is real work. The mitigations: arXiv's guardrails are already check-shaped; the field now offers off-the-shelf pieces (DESIGN.md linter, stable DTCG export, AGENTS.md) so little is bespoke; and keeping Layer 1 as no-build plain CSS avoids the per-framework component matrix that made Option 4 heavy — which also respects the "no manual maintenance" guardrail for a tiny team.

---

## What this would take, concretely

1. **Export `:root` tokens to `tokens.json`** (W3C DTCG 2025.10). Keep the CSS file as the no-build artifact. *(Small.)*
2. **Add `AGENTS.md`** beside `CLAUDE.md`, and restate the guardrails as an explicit Do's/Don'ts block. *(Small — mostly reorganizing what exists.)*
3. **Stand up Layer 3 checks** as a CI action: start with the cheapest, highest-value rules (palette allowlist, font allowlist, `:focus-visible`, external-font ban, paper-metrics-on-public ban), then add contrast. Reuse existing linters. *(Medium — the real investment, but transcribed from policy.)*
4. **Pilot on one repo** (the abstract page is the obvious candidate — highest traffic, redesign in flight) before rolling the CI action to others. Proves incremental adoption (C5).
5. **Define trust levels**: which agent contributions auto-merge vs. land as suggest-only PRs to the spec. *(Small — a policy decision.)*

---

## Honest counter-arguments

- **The simplest option that works is Option 3 (package).** If brand fidelity could be fully captured in versioned tokens + component classes, a package alone removes most drift with far less machinery. Option 5 earns its complexity only because a meaningful share of arXiv's intent is *judgment* (newcomer signposting, context-dependent labels) that an agent must adapt — not values a class can pin. Be sure that's true before building Layer 3.
- **Conformance checks give false confidence.** A linter proves tokens and contrast, not that a layout is *good*. Visual regression and human spot-checks still matter; the checks shrink the review surface, they don't eliminate review.
- **Over-automation risk.** The field is unanimous that fully autonomous agents touching the canonical spec is a mistake. Trust levels and human review of spec changes are load-bearing, not optional.
- **Build cost lands on the one person it's meant to free.** Layer 3 is upfront work for the designer before it pays back. Sequencing (pilot first, cheapest rules first) is what keeps that from stalling.

---

## Sources

- [Into Design Systems — Agentic Design Systems: The Complete Guide](https://www.intodesignsystems.com/agentic-design-systems) (AI Design Systems Conference 2026: Kavcic, Wolosin/Indeed, Gardner/NY State, Six/GitHub, Frost; Spotify Encore)
- [Anthropic — Introducing Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs)
- [TechRepublic — Anthropic Adds Brand Controls, Code Sync to Claude Design](https://www.techrepublic.com/article/news-anthropic-claude-design-overhaul-enterprise-teams/) (Jun 18 2026)
- [Anthropic frontend-design skill (SKILL.md)](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md)
- [How Anthropic teams use Claude Code (PDF)](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)
- [designmd.app — What is DESIGN.md](https://designmd.app/what-is-design-md/) · [DESIGN.md spec (Google Labs, GitHub)](https://github.com/google-labs-code/design.md)
- [W3C Design Tokens Community Group — first stable spec (2025.10)](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [AGENTS.md spec guide](https://www.morphllm.com/agents-md-guide)
