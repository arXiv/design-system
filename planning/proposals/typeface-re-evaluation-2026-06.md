# Typeface re-evaluation — June 2026

Moved out of `docs/typography.md` on 2026-09-09 when that file was merged into
`docs/typography.html`. It is a decision record: the comparison that led to
keeping IBM Plex. The outcome is stated on the typography page; this is the
working behind it, kept because the question will be asked again.

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

The marketing around "accessibility" typefaces does not survive scrutiny — and arXiv's honest voice (BRAND, Voice) should not repeat claims it cannot support:

- **Specialized dyslexia fonts give no measurable benefit.** Controlled studies — Wery & Diliberto (2017); Kuster et al. (2018, n≈170) — found OpenDyslexic and Dyslexie neither speed up nor improve reading accuracy versus standard fonts.
- **Atkinson Hyperlegible's low-vision readability is unproven.** Its reputation rests on design philosophy and a 2019 design award, not vision studies. Its *letter-disambiguation* design is real and useful — but "disambiguated" is a different, narrower claim than "more readable."
- **The proven lever is print size, not typeface.** Legge & Bigelow (2011, *Journal of Vision*) show reading speed is flat across a wide "fluent range" of sizes and drops only outside it. So the highest-leverage readability work is keeping body/UI x-height comfortably inside that range at typical reading distances — not swapping faces.

**Takeaway:** once a competent text face is in use, typeface choice is a low-leverage readability variable. Plex is competent; effort is better spent on size, spacing, and contrast.

### Two real gaps to handle

1. **IBM Plex Sans Condensed lacks Cyrillic.** A Cyrillic author name in a *condensed* table has no native glyphs. Mitigation already in place: the condensed stack falls through to non-condensed Plex Sans (`--font-condensed: "IBM Plex Sans Condensed", "IBM Plex Sans", …`), so missing glyphs render in regular-width Plex Sans automatically — correct, if slightly mixed-width within one name. Acceptable; revisit only if it reads wrong in practice. The variable build's width axis may close this entirely — verify glyph coverage before relying on it.
2. **Identifier disambiguation is already covered.** arXiv IDs, DOIs, and version strings render in **IBM Plex Mono** — monospaced and tabular, so confusable characters are already well separated. We are **not** adding a second sans family (e.g. Atkinson) for this: the benefit is unproven, its Greek/Cyrillic coverage is unconfirmed, and a second family cuts against low-maintenance (BRAND #7) and the speed pillar. Atkinson Hyperlegible Next is noted as a future fallback *only if* identifier confusability is ever shown to be a real user problem.

### Numerals — use tabular figures in tables *(plain English)*

"Tabular figures" means every digit is the same width, so numbers stack into tidy columns and do not shift sideways when a value changes. "Proportional figures" (the default) look better mid-sentence but misalign in a column. IBM Plex Sans ships both — turn tabular on for any aligned numeric context (version numbers, file sizes, dates, counts):

```css
.ds-table td.numeric, .metadata-value { font-variant-numeric: tabular-nums; }
```

Proportional for running prose; tabular for tables and aligned metadata. (Plex Mono is already tabular by nature.)

### Variable fonts — fewer, smaller files *(plain English)*

A "static" font is one file per weight (Regular + Medium + SemiBold = three downloads). A "variable" font packs the whole weight range — and for Plex Sans, a width and an italic axis — into a single file the browser interpolates. The wins for arXiv: fewer requests, usually fewer total bytes once you use ~3+ weights, and finer weight control. The catch: one variable file is larger than one static weight, so it only pays off above ~3 weights, and you must **subset to the scripts you actually serve** (Latin + Greek + Cyrillic) to keep it lean. The Plex Sans variable build exposes wght 100–700, wdth 75–100, ital 0–1 — so one subsetted file could potentially replace the separate Sans + Condensed static loads. **Next step:** prototype a subsetted variable Plex Sans woff2, measure its bytes against today's static set (~135KB for 8 files), keep `font-display: swap`, and confirm Cyrillic coverage across the width axis.

### Sources

Recommendation grounded in a verified deep-research pass (25/25 claims confirmed): [IBM/plex](https://github.com/IBM/plex) · [IBM Plex (Wikipedia)](https://en.wikipedia.org/wiki/IBM_Plex) · [Atkinson Hyperlegible (Braille Institute)](https://www.brailleinstitute.org/freefont/) · Wery & Diliberto 2017 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/26993270/)) · Kuster et al. 2018 ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5934461/)) · Legge & Bigelow 2011 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/21828237/)) · [Source Sans 3](https://github.com/adobe-fonts/source-sans) · [Inter](https://github.com/rsms/inter).

---
