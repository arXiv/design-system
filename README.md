# Smileybones

The arXiv design system.

arXiv's approved patterns for front-end interfaces, built around accessibility, usability, and the arXiv brand: design tokens, component specs, typography, color, accessibility requirements, and interactive pattern references. These define the visual language production code should follow. They are not production code themselves.

Browse it rendered: **https://arxiv.github.io/design-system/**. The site's home page (`index.html`) covers the same ground for people browsing, with a card for each pattern page.

**AI coding agents:** read [`AGENTS.md`](AGENTS.md) first. It has the reading order, a routing table, and the guardrails. CLAUDE.md, GEMINI.md and copilot-instructions point to it.

## How the repository is organized

Build only from the canonical folders. Everything else is for exploring ideas, planning, or testing.

| Folder | Status | What it holds |
|---|---|---|
| `docs/` | Canonical | The documentation: rules, pattern pages, and the stylesheets. Every pattern page shows both surfaces; `docs/sharing/` holds audience-specific pages. |
| `docs/assets/` | Canonical, for images | arXiv's official image library: logos, illustrations, backgrounds, and photos. Other repositories link to these files by URL, so keep every file and path. |
| `templates/` | Canonical, for markup | The shared head, header, and footer that other arXiv apps install (`templates/README.md`), and the announcement banner's file (`templates/BANNER_ANNOUNCEMENTS.md`). Their styles come from `docs/`. |
| `verification/` | Testing | The automated checks, audits, design reviews, and agent tests. |
| `whiteboard/mockups/` | Exploration | Whole-page explorations in progress. Never a build reference: a pattern moves into `docs/` when it is stable. |
| `whiteboard/planning/` | Exploration | The backlog (`NEXT-STEPS.md`), proposals, and decision logs. |
| `blog-theme/` | Separate project | A packaged copy of the blog.arxiv.org theme, a separate project that extends the design system. Never read its CSS as the rule. |

At the top level, `index.html` is the home page of the published site, and `docs/doc.html` renders the Markdown files there.

Mockups and canonical pages are both visible on the published site, so that stakeholders see demos and mockups in one place. Only `docs/` and `templates/` are fair game for production.

## Three contexts, shared foundations

- **Public pages** (arxiv.org, abstract pages, HTML papers): clean, fast, brown and blue. Primary action color: **Open Blue**.
- **Internal tools** (arXiv Check, Admin Console): warm, utilitarian. Primary action color: **Access Lime**.
- **Outreach sites** (the news blog, event and campaign mini-sites): the public design as-is, plus a short list of agreed differences.
- The accent signals which context a reader is in; public and internal are never mixed.

## Start here

- **Designers and product owners:** open the pattern pages in `docs/` in a browser (no build step), and read `docs/brand.html` for the why.
- **Developers:** read `docs/using.html` first. `docs/DESIGN-POLICIES.md` holds the hard constraints. Stylesheets are tiered: `docs/design-system.css` is tier 1 and everything loads it; `docs/internal-tools.css` is tier 2 for internal tools and is loaded *after* it, never alone. Plain CSS custom properties, consumable from Flask/Jinja, React, PHP, or static HTML.
- **AI coding agents:** [`AGENTS.md`](AGENTS.md).

## Key decisions (short version)

The full list is in `docs/DESIGN-POLICIES.md`, which wins wherever this summary falls short.

- **Typography:** IBM Plex family, self-hosted. No external font services, ever.
- **Color:** Repository Brown and warm greys as neutrals; Link Blue, Archival Blue and Open Blue; Access Lime is internal-only. Campus Red (`#b31b1b`) is heritage, used only in the logo's X.
- **Accessibility:** WCAG 2.1 AA is the legal floor; 2.2 AA is the working target. Ongoing accessibility gains are a key arXiv value, not a checkbox.
- **No metrics on public pages:** no view counts, downloads, or citation counts. arXiv does not rank or promote papers.
- **Header:** a single bar, with no Cornell branding after the spinout.
- **Small team:** nothing that needs manual upkeep survives review.

Design decisions are grounded in user research: the 2025 annual survey (9,419 respondents), about 180 UX-labeled GitHub issues, 42 accessibility interviews, and the Labs audit. The recurring themes: HTML papers are first-class; the interface gets out of the way; core tasks stay obvious; the paper stays sovereign; accessibility is a floor. See `docs/brand.html` for how these became design principles.

## License

MIT — see [LICENSE](LICENSE).
