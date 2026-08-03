# Typography Specification

**Status:** Draft
**Scope:** All arXiv platforms — public-facing pages, internal tools, and HTML paper rendering
**Last updated:** 2026-06-17

---

## Font families

arXiv uses the IBM Plex type family for all text, and STIX Two Math for mathematical notation. All fonts are self-hosted — no external font services (Google Fonts, Adobe Typekit, etc.).

### Why IBM Plex

- **Open source** — SIL Open Font License. No licensing cost, no vendor dependency.
- **Self-hostable** — woff2 files served from arXiv's own static assets. No external requests.
- **Complete family** — Sans, Sans Condensed, Mono, and Serif variants cover all use cases without mixing font families from different designers.
- **Language coverage** — supports Latin Extended, Cyrillic, Greek, Arabic, Hebrew, Devanagari, Thai, and more. Critical for an international research platform.
- **Math compatibility** — pairs well with STIX Two Math. Both are designed for technical/scientific contexts.

### Why not other fonts

- **Freight Sans/Text** (current brand font) — commercial, licensed through Cornell's Adobe Typekit account. Access will be lost with the Cornell spinout. Not self-hostable without a separate license purchase.
- **Rival Sans** (current HTML paper font) — commercial, also via Cornell's Typekit. Same dependency issue.
- **Google-hosted fonts** — internal objections to external font service dependencies. Self-hosting eliminates third-party requests, improves privacy, and ensures availability.

---

## Typeface re-evaluation — June 2026

**Decision: stay with IBM Plex Sans.** A deep review (cited below) scored Plex against the strongest open-source alternatives — Atkinson Hyperlegible Next, Source Sans 3, Inter, Public Sans. Plex is the *only* open-source family that bundles a competent text face, broad Latin + Greek + Cyrillic coverage, OFL self-hosting, **and** a true Condensed cut, in one coherent family. No alternative ships a real condensed/narrow width, so switching wholesale would forfeit the dense-table capability arXiv depends on — the same completeness that drove the original choice.

### Scored comparison

| Criterion | **IBM Plex Sans** | Atkinson Hyperlegible Next | Source Sans 3 | Inter | Public Sans |
|---|---|---|---|---|---|
| Evidence-based readability | ✓ competent | ~ design-intent, unproven | ✓ | ✓ | ✓ |
| OFL + self-host (woff2) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Global names (Latin+Greek+Cyrillic) | ✓ core | ~ Latin diacritics; Greek/Cyrillic unconfirmed | ✓ | ✓ | ~ Latin-only |
| **True Condensed cut** | **✓ (only one)** | ✗ | ✗ | ✗ | ✗ |
| Disambiguated 0/O · 1/l/I | ~ decent | ✓ best (explicit) | ~ | ~ (alts via cv) | ~ |
| Tabular figures | ✓ | likely | ✓ | ✓ | ✓ |
| Variable build | ✓ wght+wdth+ital | ✓ wght+ital | ✓ wght+ital | ✓ wght+ital | ✓ wght+ital |

✓ meets · ~ partial/unproven · ✗ missing. **The decisive cell is the Condensed cut** — a hard requirement for arXiv's dense tables that only Plex satisfies.

### What the readability evidence actually says

The marketing around "accessibility" typefaces does not survive scrutiny — and arXiv's honest voice (BRAND, Voice) shouldn't repeat claims it can't support:

- **Specialized dyslexia fonts give no measurable benefit.** Controlled studies — Wery & Diliberto (2017); Kuster et al. (2018, n≈170) — found OpenDyslexic and Dyslexie neither speed up nor improve reading accuracy versus standard fonts.
- **Atkinson Hyperlegible's low-vision readability is unproven.** Its reputation rests on design philosophy and a 2019 design award, not vision studies. Its *letter-disambiguation* design is real and useful — but "disambiguated" is a different, narrower claim than "more readable."
- **The proven lever is print size, not typeface.** Legge & Bigelow (2011, *Journal of Vision*) show reading speed is flat across a wide "fluent range" of sizes and drops only outside it. So the highest-leverage readability work is keeping body/UI x-height comfortably inside that range at typical reading distances — not swapping faces.

**Takeaway:** once a competent text face is in use, typeface choice is a low-leverage readability variable. Plex is competent; effort is better spent on size, spacing, and contrast.

### Two real gaps to handle

1. **IBM Plex Sans Condensed lacks Cyrillic.** A Cyrillic author name in a *condensed* table has no native glyphs. Mitigation already in place: the condensed stack falls through to non-condensed Plex Sans (`--font-condensed: "IBM Plex Sans Condensed", "IBM Plex Sans", …`), so missing glyphs render in regular-width Plex Sans automatically — correct, if slightly mixed-width within one name. Acceptable; revisit only if it reads wrong in practice. The variable build's width axis may close this entirely — verify glyph coverage before relying on it.
2. **Identifier disambiguation is already covered.** arXiv IDs, DOIs, and version strings render in **IBM Plex Mono** — monospaced and tabular, so confusable characters are already well separated. We are **not** adding a second sans family (e.g. Atkinson) for this: the benefit is unproven, its Greek/Cyrillic coverage is unconfirmed, and a second family cuts against low-maintenance (BRAND #7) and the speed pillar. Atkinson Hyperlegible Next is noted as a future fallback *only if* identifier confusability is ever shown to be a real user problem.

### Numerals — use tabular figures in tables *(plain English)*

"Tabular figures" means every digit is the same width, so numbers stack into tidy columns and don't shift sideways when a value changes. "Proportional figures" (the default) look better mid-sentence but misalign in a column. IBM Plex Sans ships both — turn tabular on for any aligned numeric context (version numbers, file sizes, dates, counts):

```css
.ds-table td.numeric, .metadata-value { font-variant-numeric: tabular-nums; }
```

Proportional for running prose; tabular for tables and aligned metadata. (Plex Mono is already tabular by nature.)

### Variable fonts — fewer, smaller files *(plain English)*

A "static" font is one file per weight (Regular + Medium + SemiBold = three downloads). A "variable" font packs the whole weight range — and for Plex Sans, a width and an italic axis — into a single file the browser interpolates. The wins for arXiv: fewer requests, usually fewer total bytes once you use ~3+ weights, and finer weight control. The catch: one variable file is larger than one static weight, so it only pays off above ~3 weights, and you must **subset to the scripts you actually serve** (Latin + Greek + Cyrillic) to keep it lean. The Plex Sans variable build exposes wght 100–700, wdth 75–100, ital 0–1 — so one subsetted file could potentially replace the separate Sans + Condensed static loads. **Next step:** prototype a subsetted variable Plex Sans woff2, measure its bytes against today's static set (~135KB for 8 files), keep `font-display: swap`, and confirm Cyrillic coverage across the width axis.

### Sources

Recommendation grounded in a verified deep-research pass (25/25 claims confirmed): [IBM/plex](https://github.com/IBM/plex) · [IBM Plex (Wikipedia)](https://en.wikipedia.org/wiki/IBM_Plex) · [Atkinson Hyperlegible (Braille Institute)](https://www.brailleinstitute.org/freefont/) · Wery & Diliberto 2017 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/26993270/)) · Kuster et al. 2018 ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5934461/)) · Legge & Bigelow 2011 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/21828237/)) · [Source Sans 3](https://github.com/adobe-fonts/source-sans) · [Inter](https://github.com/rsms/inter).

---

## The font stack

| Role | Font | Weights | Usage |
|---|---|---|---|
| **Body text** | IBM Plex Sans | 400 (regular), 500 (medium), 600 (semibold) | All body copy, paragraphs, author names, abstracts |
| **Labels & captions** | IBM Plex Sans Condensed | 500 (medium), 600 (semibold) | Section labels, metadata labels, table headers, uppercase captions |
| **Code & identifiers** | IBM Plex Mono | 400 (regular), 500 (medium) | arXiv IDs, DOIs, BibTeX, code blocks, monospace content |
| **Annotation** | IBM Plex Serif | 400 italic | Secondary editorial commentary — footnote text in margin, figure alt-text in margin (see `.ds-annotation`) |
| **Math notation** | STIX Two Math | 400 (regular) | Inline and display math in HTML paper pages |

### CSS custom properties

```css
:root {
  --font-body: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-condensed: "IBM Plex Sans Condensed", "IBM Plex Sans", sans-serif;
  --font-mono: "IBM Plex Mono", "SF Mono", "Fira Code", "Consolas", monospace;
  --font-serif: "IBM Plex Serif", Georgia, "STIX Two Text", "Times New Roman", serif;
  --font-math: "STIX Two Math", "Cambria Math", math;
}
```

### Fallback strategy

Each font stack includes system fallbacks so content remains readable if web fonts fail to load:
- Sans: falls back to the OS system font (-apple-system on Mac, Segoe UI on Windows)
- Mono: falls back to platform monospace (SF Mono on Mac, Consolas on Windows)
- Math: falls back to Cambria Math (bundled with Windows/Office) and then the CSS `math` generic family

---

## Hosting

All font files are self-hosted as woff2 from arXiv's static assets directory. No external font service dependencies.

```
/static/fonts/
  IBMPlexSans-Regular.woff2
  IBMPlexSans-Medium.woff2
  IBMPlexSans-SemiBold.woff2
  IBMPlexSansCondensed-Medium.woff2
  IBMPlexSansCondensed-SemiBold.woff2
  IBMPlexMono-Regular.woff2
  IBMPlexMono-Medium.woff2
  IBMPlexSerif-Italic.woff2
  STIXTwoMath-Regular.woff2       ← already self-hosted
```

**This repo's docs pages** serve the same files (minus STIX — no math on pattern pages) from `docs/fonts/`, declared in [`docs/fonts.css`](fonts.css), which every pattern page links ahead of its design-system.css. The @font-face rules live in that separate stylesheet — not in the two design-system.css files — because consumers bundle those with their own font paths. Files copied from [IBM/plex](https://github.com/IBM/plex) (OFL).

### @font-face declarations

```css
@font-face {
  font-family: "IBM Plex Sans";
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexSans-Regular.woff2") format("woff2");
}
@font-face {
  font-family: "IBM Plex Sans";
  font-weight: 500;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexSans-Medium.woff2") format("woff2");
}
@font-face {
  font-family: "IBM Plex Sans";
  font-weight: 600;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexSans-SemiBold.woff2") format("woff2");
}

@font-face {
  font-family: "IBM Plex Sans Condensed";
  font-weight: 500;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexSansCondensed-Medium.woff2") format("woff2");
}
@font-face {
  font-family: "IBM Plex Sans Condensed";
  font-weight: 600;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexSansCondensed-SemiBold.woff2") format("woff2");
}

@font-face {
  font-family: "IBM Plex Mono";
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexMono-Regular.woff2") format("woff2");
}
@font-face {
  font-family: "IBM Plex Mono";
  font-weight: 500;
  font-style: normal;
  font-display: swap;
  src: url("/static/fonts/IBMPlexMono-Medium.woff2") format("woff2");
}

@font-face {
  font-family: "IBM Plex Serif";
  font-weight: 400;
  font-style: italic;
  font-display: swap;
  src: url("/static/fonts/IBMPlexSerif-Italic.woff2") format("woff2");
}

@font-face {
  font-family: "STIX Two Math";
  font-weight: 400;
  font-style: normal;
  font-display: auto;
  src: local("STIXTwoMath-Regular"),
       url("/static/fonts/STIXTwoMath-Regular.woff2") format("woff2");
}
```

### Performance notes

- **`font-display: swap`** for text fonts — shows fallback immediately, swaps when loaded. Prioritizes readability over visual stability.
- **`font-display: auto`** for STIX Two Math — math rendering can look wrong in fallback fonts, so it's better to wait briefly for the correct font.
- **Total download:** ~135KB for all 8 Plex woff2 files (Serif Italic adds ~15KB) + ~300KB for STIX Two Math. STIX is large but only needed on HTML paper pages, not abstract pages.
- **`local()` check** for STIX Two Math — skips download if the user already has it installed.

---

## Usage by platform

| Platform | Body | Labels | Code | Math |
|---|---|---|---|---|
| **Abstract pages** | Plex Sans | Plex Sans Condensed | Plex Mono | — (MathJax handles math) |
| **HTML paper pages** | Plex Sans | Plex Sans Condensed | Plex Mono | STIX Two Math |
| **Internal tools** (arXiv Check, Admin Console) | Plex Sans | Plex Sans Condensed | Plex Mono | — |
| **Homepage, listings, search** | Plex Sans | Plex Sans Condensed | Plex Mono | — |

### Migration from current fonts

| Current | Replacement | Affected pages |
|---|---|---|
| Rival Sans (Typekit) | IBM Plex Sans | HTML paper pages |
| IBM Plex Mono (Typekit) | IBM Plex Mono (self-hosted) | HTML paper pages |
| Freight Sans/Text (Typekit) | IBM Plex Sans | Info site |
| IBM Plex Sans (Google Fonts) | IBM Plex Sans (self-hosted) | Internal tools |
| STIX Two Math (self-hosted) | No change | HTML paper pages |

---

## Type scale

Not yet formalized. The following sizes are used consistently across mockups and should be documented as the scale is refined:

| Use | Size | Weight | Font |
|---|---|---|---|
| Paper title (abstract page) | 24px | 600 | Plex Sans |
| Section heading | 15–16px | 600 | Plex Sans |
| Body text | 15px | 400 | Plex Sans |
| Metadata labels | 11px uppercase | 600 | Plex Sans Condensed |
| Table headers | 11px uppercase | 600 | Plex Sans Condensed |
| Secondary text / captions | 13px | 400–500 | Plex Sans |
| Annotation (footnote, alt-text in margin) | 13px italic | 400 | Plex Serif |
| Code / identifiers | 12–13px | 400 | Plex Mono |
| Nav links | 13px | 500 | Plex Sans |

---

## Open questions

- [ ] **Plex Serif weights** — currently loading Italic only (for `.ds-annotation`). Roman/regular weight could be added later if a non-italic serif use case appears, but italic is the only validated use today.
- [ ] **Italic weights** — do we need italic variants of Plex Sans? Currently not loaded. Abstracts sometimes contain italic terms. MathJax handles math italics separately.
- [ ] **Bold weight (700)** — currently using 600 (semibold) as the heaviest weight. Do any contexts need true bold?
- [x] **CJK support** — *Decided (2026-06-17): fall back to system fonts for CJK.* IBM Plex's CJK siblings (Plex Sans JP/KR/TC/SC) are separate multi-megabyte families; loading them for author names and abstracts is against the speed pillar and small-team maintenance (BRAND #7, #8). CJK text falls back to the OS system CJK font via the sans stack. Revisit only if CJK rendering proves a real problem in testing.
- [x] **Tabular figures & variable build** — *Direction set (2026-06-17)* in "Typeface re-evaluation" above: enable `tabular-nums` for aligned numeric tables; prototype a subsetted variable Plex Sans woff2 and measure before adopting.
- [x] **Re-evaluate IBM Plex vs. alternatives** — *Done (2026-06-17): stay with Plex.* See "Typeface re-evaluation — June 2026" above for the scored comparison, the readability evidence, and the two gaps (Condensed-Cyrillic, identifier disambiguation).
- [ ] **Info site migration** — timeline for replacing Freight with Plex on info.arxiv.org?
