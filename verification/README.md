# Verification harness

Automated regression checks for the page mockups in `../mockups/`. Every check maps to a defect class found in user research, the html_feedback issue queues, or rendering audits — the script prints the research basis next to any failure.

## Run

```
pip install playwright
playwright install chromium
python3 verification/verify-mockups.py
```

Exit code 0 means all checks pass.

## What it checks

**Reflow / overflow** — no horizontal scrollable overflow on either mockup at 320 / 390 / 768 / 1440px. Covers WCAG 1.4.10 (400% zoom) and the middle-click-autoscroll bug class (any horizontal overflow breaks vertical autoscroll in Firefox — five independent html_feedback filings).

**ARIA hygiene** — no `role="radio"` without arrow-key support; switchers use `aria-pressed`; abstract-page type sizes are rem so browser font-size overrides propagate.

**Progressive enhancement (no-JS)** — with JavaScript disabled: all authors render, the search control degrades to a link, and reader footnotes are readable inline. Scripts add conveniences; they never carry content.

**Reader interactions** — TOC dropdown titles contain no raw TeX (MathML annotation leakage); citation chips are aurally compact at rest and carry contextual accessible names ("Reference 12: …"); the figure lightbox opens, paints (transformed-`<svg>` rasterization regression), keeps its zoom after pointer release, and closes on Esc.

## When to extend

Add a check whenever a fix lands for a reproducible defect — the check is what stops the bug class from regenerating. Keep each check annotated with its research basis so future maintainers know what breaks for whom if it fails.

Known gaps (manual testing still required): real screen-reader passes (NVDA/JAWS/VoiceOver), Windows High Contrast Mode, `prefers-reduced-motion` behavior, touch gestures on real devices, iOS Safari.
