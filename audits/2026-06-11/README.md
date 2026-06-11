# Audit — 2026-06-11

Two parallel audits of the redesign mockups and the current arXiv site, captured via Playwright.

**See also:** [`../../visual-audit/`](../../visual-audit/) — the platform-wide strategic visual audit from 2025-11-11 (the "11 visual languages" report). That's a stakeholder-facing narrative document; this folder is operational tool output. Different artifacts, both useful, kept separate on purpose.

## Files

- **`AUDIT-RESPONSIVENESS.md`** — viewport-by-viewport review of the two redesign mockups (`html-redesign.html`, `abstract-redesign.html`) at 320 / 375 / 414 / 768 / 1024 / 1440 px. Live arXiv pages were excluded from this pass — known to lack mobile responsiveness, no actionable signal.
- **`AUDIT-COMPONENTS.md`** — cross-page component inventory across 9 pages (2 redesign mockups + 7 live arXiv template-family representatives). Identifies high-leverage promotion targets, inconsistencies, and missing patterns for the design-system roadmap.
- **`scripts/audit-v2.mjs`** — the Playwright capture script. Reproducible: install dependencies (`npm install playwright && npx playwright install chromium`) and `node audit-v2.mjs`. Re-running regenerates all screenshots.
- **`screenshots/`** — 45 captures (~5 MB). Not committed to git (see `.gitignore`).

## How to re-run

```sh
cd /tmp && mkdir -p playwright-audit && cd playwright-audit
npm init -y
npm install playwright
npx playwright install chromium
node ~/Documents/arxiv-repos/design-system/audits/2026-06-11/scripts/audit-v2.mjs
```

Screenshots will land back at `audits/2026-06-11/screenshots/`. Total runtime ~3 minutes.

## What to do next

1. Skim both audit Markdown files (the headlines + "Issues found" / "Recommendations" sections).
2. Decide which findings translate into fixes (responsiveness) or roadmap re-priorities (components).
3. Treat this folder as a snapshot. The next audit gets its own dated folder; nothing here gets overwritten.
