# Typography Specification

**Status:** Draft
**Scope:** All arXiv platforms — public-facing pages, internal tools, and HTML paper rendering
**Last updated:** 2026-04-28

---

## Font families

arXiv uses the IBM Plex type family for all text, and STIX Two Math for mathematical notation. All fonts are self-hosted — no external font services (Google Fonts, Adobe Typekit, etc.).

### Why IBM Plex

- **Open source** — SIL Open Font License. No licensing cost, no vendor dependency.
- **Self-hostable** — woff2 files served from arXiv's own static assets. No external requests.
- **Complete family** — Sans, Sans Condensed, and Mono variants cover all use cases without mixing font families from different designers.
- **Language coverage** — supports Latin Extended, Cyrillic, Greek, Arabic, Hebrew, Devanagari, Thai, and more. Critical for an international research platform.
- **Math compatibility** — pairs well with STIX Two Math. Both are designed for technical/scientific contexts.

### Why not other fonts

- **Freight Sans/Text** (current brand font) — commercial, licensed through Cornell's Adobe Typekit account. Access will be lost with the Cornell spinout. Not self-hostable without a separate license purchase.
- **Rival Sans** (current HTML paper font) — commercial, also via Cornell's Typekit. Same dependency issue.
- **Google-hosted fonts** — internal objections to external font service dependencies. Self-hosting eliminates third-party requests, improves privacy, and ensures availability.

---

## The font stack

| Role | Font | Weights | Usage |
|---|---|---|---|
| **Body text** | IBM Plex Sans | 400 (regular), 500 (medium), 600 (semibold) | All body copy, paragraphs, author names, abstracts |
| **Labels & captions** | IBM Plex Sans Condensed | 500 (medium), 600 (semibold) | Section labels, metadata labels, table headers, uppercase captions |
| **Code & identifiers** | IBM Plex Mono | 400 (regular), 500 (medium) | arXiv IDs, DOIs, BibTeX, code blocks, monospace content |
| **Math notation** | STIX Two Math | 400 (regular) | Inline and display math in HTML paper pages |

### CSS custom properties

```css
:root {
  --font-body: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-condensed: "IBM Plex Sans Condensed", "IBM Plex Sans", sans-serif;
  --font-mono: "IBM Plex Mono", "SF Mono", "Fira Code", "Consolas", monospace;
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
  STIXTwoMath-Regular.woff2       ← already self-hosted
```

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
- **Total download:** ~120KB for all 7 Plex woff2 files + ~300KB for STIX Two Math. STIX is large but only needed on HTML paper pages, not abstract pages.
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
| Code / identifiers | 12–13px | 400 | Plex Mono |
| Nav links | 13px | 500 | Plex Sans |

---

## Open questions

- [ ] **Italic weights** — do we need italic variants of Plex Sans? Currently not loaded. Abstracts sometimes contain italic terms. MathJax handles math italics separately.
- [ ] **Bold weight (700)** — currently using 600 (semibold) as the heaviest weight. Do any contexts need true bold?
- [ ] **CJK support** — IBM Plex has CJK variants (Plex Sans JP, KR, TC, SC). Should these be loaded for author names and abstracts in those languages, or fall back to system fonts?
- [ ] **Info site migration** — timeline for replacing Freight with Plex on info.arxiv.org?
