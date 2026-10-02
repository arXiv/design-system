---
page: cards.html
title: "Cards"
summary: "When you need to draw a box around related content, reach for a card. Public pages and internal tools each have their own color variations but the use cases are shared. The markup is the same on both surfaces; the internal colours come from `.ds-internal` on a parent element and nothing else changes."
stylesheet: design-system.css
components:
  - id: basic-cards
    title: "Basic cards"
    summary: "A flexible and unopinionated white surface with a hairline border and 8px radius."
    classes:
      - name: ".ds-card"
        does: "The box: white surface, hairline `--ds-border`, 8px radius, padding from the scale. Its first and last children have no outer margin, because the padding is the space at the edges. It sets `position: relative`, so a margin note or an anchored pill measures from it."
      - name: ".ds-internal"
        does: "On a parent, usually `<html>` or `<body>`. Re-points the accent to Access Lime for everything inside. Nothing on the card itself changes. The basic card has no accent of its own, so it looks the same on both surfaces; what changes is everything inside it that reaches for the accent, such as the button."
  - id: data-cards
    title: "Data cards"
    summary: "Intended for organizing metadata and other reference information: the facts about one record, each pair stacking a label over a value. Cards read correctly against both white or a warm-wash page background."
    classes:
      - name: ".ds-card.ds-card--data"
        does: "On a `<section>` with an `aria-label`, which makes it a named region. A tinted ground (`--ds-surface-muted`) and a 4px top edge in the accent, so it reads as reference rather than content. No padding of its own: the pairs have it."
      - name: "dl > div"
        does: "One pair per `<div>`, `<dt>` label then `<dd>` value. Pairs sit side by side when the card is wide enough for two and stack in one column when it is not; a hairline separates them in both directions."
      - name: "dt, dd"
        does: "The label is small, condensed and uppercased by CSS: type it in sentence case. The value is in IBM Plex Mono and wraps anywhere, so a long address or identifier stays inside the card. A value that goes somewhere is an `<a href>` and takes the ordinary link colours."
      - name: ".ds-internal"
        does: "The top edge takes Access Lime. The markup is the public one."
  - id: stat-cards
    title: "Stat cards"
    summary: "One number with its label, on the warm tint. Use a group of them for a summary at the top of a dashboard."
    classes:
      - name: ".ds-card--stat"
        does: "A card that holds one number. Warm tint, the same on both surfaces. In a `.ds-card-grid`, stat cards are narrower than other cards and fill the row."
      - name: ".ds-panel-label"
        does: "What the number counts. It comes first, so a screen reader reads the label before the number."
      - name: ".ds-stat-value"
        does: "The number: 2rem, weight 600, with tabular figures so numbers in a row of cards line up."
      - name: ".ds-stat-context"
        does: "Optional. One short line under the number, such as a change or a unit."
  - id: groups-of-cards
    title: "Groups of cards"
    summary: "Peers in a set share one grid. The count of columns does not follow a breakpoint but adjusts to the content. The grid will drop to one column when a card can no longer hold its minimum width."
    classes:
      - name: ".ds-card-grid"
        does: "Cards side by side. The grid supplies the gap, so a card inside it takes no top margin of its own. Any card goes in it, a data card included, and it is the same on both surfaces."
rules:
  - "**Name a data card.** It is a `<section>` with an `aria-label` such as “User information”, so a screen reader user can jump straight to it and hears what it holds. A section without a name is not exposed as a landmark at all."
  - "**Keep each label with its value.** A label and its value sit together in one `<div>`, `<dt>` first, so they are read as a pair. The label is real text in the markup and the uppercase comes from CSS, so it stays correct for a screen reader and for copy and paste."
  - "**Values are text.** An identifier, an address or a date in a data card is plain text: it can be selected, copied, found with in-page search and read aloud. Do not put a value in an image or draw it with CSS."
  - "**No editable fields inside a data card.** Its tinted surface says read-only. A form control inside it contradicts what the surface tells a sighted reader and puts a focus stop inside a region that announces as reference. Editable fields take a basic `.ds-card`."
---

# Cards

When you need to draw a box around related content, reach for a card. Public pages and internal tools each have their own color variations but the use cases are shared. The markup is the same on both surfaces; the internal colours come from `.ds-internal` on a parent element and nothing else changes.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Basic cards

A flexible and unopinionated white surface with a hairline border and 8px radius.

**Public**

```html
<div class="ds-card">
  <h3>submit/5720431</h3>
  <p>Spectral gaps in random regular hypergraphs. Submitted 2026-09-18 to math.CO, awaiting moderation.</p>
</div>
```

**Internal**

```html
<body class="ds-page ds-internal">
  …
  <div class="ds-card">
    <h3>submit/5720431</h3>
    <p>Spectral gaps in random regular hypergraphs. Submitted 2026-09-18 to math.CO, awaiting moderation.</p>
    <div class="ds-btn-group"><button type="button" class="ds-btn ds-btn-primary">Approve</button><button type="button" class="ds-btn">Hold</button></div>
  </div>
```

- `.ds-card` — The box: white surface, hairline `--ds-border`, 8px radius, padding from the scale. Its first and last children have no outer margin, because the padding is the space at the edges. It sets `position: relative`, so a margin note or an anchored pill measures from it.
- `.ds-internal` — On a parent, usually `<html>` or `<body>`. Re-points the accent to Access Lime for everything inside. Nothing on the card itself changes. The basic card has no accent of its own, so it looks the same on both surfaces; what changes is everything inside it that reaches for the accent, such as the button.

## Data cards

Intended for organizing metadata and other reference information: the facts about one record, each pair stacking a label over a value. Cards read correctly against both white or a warm-wash page background.

**Public**

```html
  <section class="ds-card ds-card--data" aria-label="Paper information">
  <dl>
    <div><dt>arXiv ID</dt><dd><a href="#">2311.04082</a></dd></div>
    <div><dt>Submitted</dt><dd>2023-11-07</dd></div>
    <div><dt>Subjects</dt><dd>cond-mat.soft</dd></div>
    <div><dt>Licence</dt><dd><a href="#">CC BY 4.0</a></dd></div>
  </dl>
</section>
```

**Internal**

```html
<body class="ds-page ds-internal">
  …
  <section class="ds-card ds-card--data" aria-label="User information">
  <dl>
    <div><dt>User</dt><dd><a href="#">Katrin Solberg</a></dd></div>
    <div><dt>Email</dt><dd><a href="#">katrin.solberg@example.org</a></dd></div>
    <div><dt>Remote host</dt><dd>128.84.12.201</dd></div>
    <div><dt>Date</dt><dd>2024-12-31</dd></div>
  </dl>
</section>
```

- `.ds-card.ds-card--data` — On a `<section>` with an `aria-label`, which makes it a named region. A tinted ground (`--ds-surface-muted`) and a 4px top edge in the accent, so it reads as reference rather than content. No padding of its own: the pairs have it.
- `dl > div` — One pair per `<div>`, `<dt>` label then `<dd>` value. Pairs sit side by side when the card is wide enough for two and stack in one column when it is not; a hairline separates them in both directions.
- `dt, dd` — The label is small, condensed and uppercased by CSS: type it in sentence case. The value is in IBM Plex Mono and wraps anywhere, so a long address or identifier stays inside the card. A value that goes somewhere is an `<a href>` and takes the ordinary link colours.
- `.ds-internal` — The top edge takes Access Lime. The markup is the public one.

## Stat cards

One number with its label, on the warm tint. Use a group of them for a summary at the top of a dashboard.

```html
<div class="ds-card ds-card--stat">
  <p class="ds-panel-label">Member institutions</p>
  <p class="ds-stat-value">1,284</p>
  <p class="ds-stat-context">12 more than last month</p>
</div>
```

- `.ds-card--stat` — A card that holds one number. Warm tint, the same on both surfaces. In a `.ds-card-grid`, stat cards are narrower than other cards and fill the row.
- `.ds-panel-label` — What the number counts. It comes first, so a screen reader reads the label before the number.
- `.ds-stat-value` — The number: 2rem, weight 600, with tabular figures so numbers in a row of cards line up.
- `.ds-stat-context` — Optional. One short line under the number, such as a change or a unit.

## Groups of cards

Peers in a set share one grid. The count of columns does not follow a breakpoint but adjusts to the content. The grid will drop to one column when a card can no longer hold its minimum width.

```html
<div class="ds-card-grid">
  <div class="ds-card">
    <h3>2311.04082</h3>
    <p>Anomalous diffusion in confined active matter. Published 2023-11-07, cond-mat.soft.</p>
  </div>
  <div class="ds-card">…</div>
  <div class="ds-card">…</div>
</div>
```

- `.ds-card-grid` — Cards side by side. The grid supplies the gap, so a card inside it takes no top margin of its own. Any card goes in it, a data card included, and it is the same on both surfaces.

## Rules

- **Name a data card.** It is a `<section>` with an `aria-label` such as “User information”, so a screen reader user can jump straight to it and hears what it holds. A section without a name is not exposed as a landmark at all.
- **Keep each label with its value.** A label and its value sit together in one `<div>`, `<dt>` first, so they are read as a pair. The label is real text in the markup and the uppercase comes from CSS, so it stays correct for a screen reader and for copy and paste.
- **Values are text.** An identifier, an address or a date in a data card is plain text: it can be selected, copied, found with in-page search and read aloud. Do not put a value in an image or draw it with CSS.
- **No editable fields inside a data card.** Its tinted surface says read-only. A form control inside it contradicts what the surface tells a sighted reader and puts a focus stop inside a region that announces as reference. Editable fields take a basic `.ds-card`.
