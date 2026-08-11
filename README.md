# arXiv Design System

arXiv's DNA for product design and frontend development: design tokens, component specs, typography and color decisions, accessibility requirements, and interactive pattern references. These define the visual language production code should follow — they are not production code themselves.

Browse it rendered: **https://arxiv.github.io/design-system/**

## Three contexts, shared foundations

- **Public pages** (arxiv.org, abstract pages, HTML papers) — clean, fast, brown-and-blue. Primary action color: **Open Blue**.
- **Internal tools** (arXiv Check, Admin Console) — warm, utilitarian. Primary action color: **Access Lime**.
- **Outreach sites** (the news blog, event and campaign mini-sites) — the public design as-is, plus a short list of agreed differences.
- The accent signals which context you're in; public and internal are never mixed.

## Directory guide

```
docs/           THE documentation — rules, tokens, pattern pages, stylesheets
                (docs/public/, docs/internal/, docs/outreach/ hold per-context patterns + CSS)
mockups/        work-in-progress page explorations — never a build reference
verification/   evidence — audits, design reviews, agent test results
planning/       backlog (NEXT-STEPS.md), proposals, decision logs
index.html      the GitHub Pages landing page (docs/doc.html renders .md files on the site)
```

## Start here

- **Designers / product owners** — open the pattern pages in `docs/` in a browser (no build step); read `docs/BRAND.md` for the why.
- **Developers** — `docs/DESIGN-POLICIES.md` holds the hard constraints; `docs/public/design-system.css` and `docs/internal/design-system.css` hold the authoritative tokens and component CSS (plain CSS custom properties — consumable from Flask/Jinja, React, PHP, or static HTML).
- **AI coding agents** — read [`AGENTS.md`](AGENTS.md). It has the reading order, a routing table, and the guardrails. CLAUDE.md / GEMINI.md / copilot-instructions are pointers to it.

## Key decisions (short version)

- **Typography:** IBM Plex family, self-hosted. No external font services, ever.
- **Color:** Repository Brown + warm greys as neutrals; Link Blue / Archival Blue / Open Blue; Access Lime is staff-only. Campus Red (`#b31b1b`) is heritage — logo X only.
- **Accessibility:** WCAG 2.1 AA is the legal floor; 2.2 AA is the working target. Ongoing accessibility gains is a key arXiv value, not a checkbox.
- **No metrics on public pages:** no view counts, downloads, or citation counts — arXiv does not rank or promote papers.
- **Cornell spinout:** Cornell branding is being removed; the black single-bar header (phase 1) transitions to Repository Brown (phase 2).
- **Small team:** nothing that needs manual upkeep survives review.

Design decisions are grounded in user research — the 2025 annual survey (9,419 respondents), ~180 UX-labeled GitHub issues, 42 accessibility interviews, and the Labs audit. The recurring themes: HTML papers are first-class; the interface gets out of the way; core tasks stay obvious; the paper stays sovereign; accessibility is a floor. See `docs/BRAND.md` for how these became design principles.

## Mockups vs. canonical

Patterns are explored in `mockups/`, and **promoted into `docs/`** when they stabilize — only then are they canonical and fair game for production. Both are visible on the published site (deliberate — stakeholders see demos and mockups in one place); the folder READMEs mark the difference.

## License

MIT — see [LICENSE](LICENSE).
