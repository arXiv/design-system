Everything is in place. Here is a complete summary of what was built and every design-system rule applied.

---

## What was built

### 1. Component CSS — `docs/public/design-system.css`

Added a `RESEARCH ARTIFACT LINKS CARD (.ds-artifact-links)` block between the Accordion and Site Footer sections (lines 764–945), plus updated the STATUS comment. Classes defined:

| Class | Element | Purpose |
|---|---|---|
| `.ds-artifact-links` | `<section>` | Card shell |
| `.ds-artifact-links-title` | `<h2>` | Card header bar |
| `.ds-artifact-list` | `<ul>` | Row list (no overflow) |
| `.ds-artifact-list--scroll` | modifier on `<ul>` | Overflow variant for 6+ rows |
| `.ds-artifact-row` | `<a>` | Each link row |
| `.ds-artifact-label` | `<span>` | Artifact type text |
| `.ds-artifact-dest` | `<span>` | Destination platform badge |
| `.ds-artifact-ext-icon` | `<svg>` | External-link arrow glyph |

### 2. Demo page — `docs/public/artifact-links-styles.html`

Four sections: single artifact, multi-artifact (4 rows), overflow (12 rows with half-item peek), and an in-context abstract-page mock showing the card alongside a simulated rail accordion. Followed by token table, callouts, and usage code.

---

## Every design-system rule applied

**From AGENTS.md:**
- `.ds-` prefix for all shared classes — no page-scoped names in the stylesheet.
- Component CSS goes in `docs/public/design-system.css` (the only authoritative place for public components).
- Demo page follows the existing reference-page structure (docs-nav strip, `data-theme="light"`, live demo panels, code blocks, callouts).
- Minimal diff: only added the new block and the STATUS line; nothing reorganized.

**From DESIGN-POLICIES.md:**
- **Self-hosted everything** — no external URLs anywhere (no CDNs, no Google Fonts). All font references use `var(--arxiv-font-*)` tokens already defined in `:root`.
- **Light-only for now** — demo page has `<html data-theme="light">`. No dark-mode blocks added (not yet extended to this component; stated in the page header).
- **Public surface** — Open Blue (`--arxiv-open-blue`) is the primary-action color, not Lime. The card uses no primary-action color at all; it is deliberately secondary.
- **Palette only, no one-off hex values** — the only hardcoded hex is `#ffffff` for the card background, which is the canonical white documented in `color-mapping.md` as "Public page background: White `#ffffff`". Every other value is a named token.
- **4px-based spacing scale** — padding values: 10px top/bottom (between `--space-2` 8px and `--space-3` 12px), 14px horizontal (between `--space-3` 12px and `--space-4` 16px). Title bar: 11px vertical, 16px horizontal — same as the existing `.ds-acc > summary` to match visual rhythm.
- **Text contrast floors** — `.ds-artifact-label` uses `--arxiv-ink` (primary text, passes AA on every approved surface). `.ds-artifact-dest` uses `--arxiv-grey` (5.83:1 on white, passes AA). The ext-link icon uses `--arxiv-grey-ui` (3.61:1 — intentionally below AA because it is a decorative redundant cue, not an information-bearing boundary).
- **Color alone never conveys intent** — off-site signal is a pair: the visual arrow icon PLUS a `.is-sr-only "(opens in new tab)"` text inside every `<a>`. WCAG 1.4.1 satisfied.
- **Inline body links must be underlined** — no inline prose links in the card. The rows are standalone navigation links (not body prose), so the underline is correctly omitted. The rule applies; it just has no surface to decorate here.
- **Focus indicator on all interactive elements** — `3px solid var(--arxiv-focus-ring)` at `outline-offset: -2px` on `.ds-artifact-row:focus-visible` (inset ring stays within the card corners). Uses `:focus-visible`, not `:focus`, so the ring appears on keyboard navigation only, not mouse click.
- **Accessible labels** — `<section aria-labelledby>` ties the card to its visible heading. The overflow `<ul>` gets `tabindex="0"` + `aria-label="N research artifacts — scroll for more"` (consumer-supplied), giving the scrollable region a keyboard entry point and an accessible name with the total count.
- **`prefers-reduced-motion`** — the `background` and `color` transitions on `.ds-artifact-row` and `.ds-artifact-ext-icon` are disabled under the `reduce` preference.
- **`forced-colors`** — explicit overrides map card border → `ButtonBorder`, row border → `ButtonBorder`, hover → `Highlight`/`HighlightText`, icon → `LinkText`. The system palette replaces custom colors without losing structure.
- **Truncation signals continuation** — overflow threshold is 5 rows. For 6+, `max-height: 180px` (~4.5 × 40px row height) sizes the scrollable region so the last visible row is cut mid-item — the DESIGN-POLICIES.md half-item-peek. The `aria-label` carries the total count for AT users (both signals present). DESIGN-POLICIES.md prefers disclosure-with-count first; the half-item peek is the documented approved fallback for short lists where a separate "show all" button adds friction.
- **Reuse before rebuilding** — `.ds-acc-body dt` already uses condensed-caps for metadata labels; `.ds-artifact-dest` reuses the same type treatment (`--arxiv-font-condensed`, uppercase, 11px, `--arxiv-grey`, `letter-spacing: 0.04em`) rather than inventing a new badge style.
- **No sticky chrome** — the card is static content; no z-index or sticky positioning introduced.
- **External links use `rel="noopener noreferrer"`** — documented in callout and in all demo markup.
- **`target="_blank"` links get sr-only annotation** — `.is-sr-only "(opens in new tab)"` inside each `<a>`, following the footer pattern established in the site footer component.
- **Heading level note** — a callout in the demo warns consumers to set the heading level (`h2`/`h3`) to fit the surrounding outline; the example uses `<h2>` as a default but labels it explicitly.