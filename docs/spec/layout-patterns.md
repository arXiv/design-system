---
page: layout-patterns.html
title: "Layout patterns"
summary: "This section covers our primary patterns for differentiating and organizing content based on user needs. The organizing principle to follow throughout: Choose typographic and proximity-based organization patterns first, reach for visible containers only when called for."
stylesheet: design-system.css
components:
  - id: evaluating-user-needs
    title: "Evaluating user needs"
    summary: "What a user needs to learn determines the right organizational pattern to employ for any group of content. Use the four questions below as a starting point. Each question has a test and a set of patterns that answer it. Most content will fit under one of these questions. Have an edge case? Discuss it with the design team."
    notes:
      - "Where am I? (The address or the item changes): [Header](header.html) and [secondary navigation](header.html#secondary-navigation): sections of a site or tool; [Steps](header.html#steps): an ordered process; [Pager](pager.html): a queue, one item at a time; [Numbered pages](pager.html#numbered-pages): a long list split across pages; [TOC bar](progressive-disclosure.html#toc-bar): sections of one long page"
      - "What matters here? (Directing user attention): [Spacing](spacing.html) and [dividers](#dividers): separate content; [Page container](#the-page-container), [page zones](#page-zones) and [wide page](#wide-page): the page frame; [Sidebar](#sidebar) and [marginalia](#marginalia): supporting content; [Cards](cards.html) and [tables](tables.html): records"
      - "Which part do I need? (The content swaps in place): [Tabs](progressive-disclosure.html#tabs): one view at a time; [Filter bar](tables.html#filter-bar): narrowed data; [Sections of one page](typography.html#the-heading-scale): views to compare"
      - "Can I learn more? (Richer details are revealed upon request): [Tooltip](forms.html#tooltip) and [popover](progressive-disclosure.html#popover): detail on request; [Show more](progressive-disclosure.html#show-more) and [accordion](progressive-disclosure.html#accordion): more in the flow; [Modal](modals.html): a decision first; [Actions attached to content](buttons.html#small-actions-attached-to-content): act on one item"
  - id: the-page-container
    title: "The page container"
    summary: "Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Page zones](#page-zones)."
  - id: sidebar
    title: "Sidebar"
    summary: "A sidebar sits to the right of the main column and contains supplementary content. If the content is secondary, distinct from the main content, and it is important that it not be pushed far down the page, then a sidebar is appropriate."
    classes:
      - name: ".ds-sidebar"
        does: "On an `<aside>` with an `aria-label` that names what it holds: a complementary landmark. Its parent becomes the two-column layout, with the main content taking the spare width, the sidebar 17rem wide, and `--ds-space-section` between them. Blocks inside the sidebar are 24px apart (`--ds-space-6`). Nothing in it is sticky."
      - name: "<aside>"
        does: "The sidebar comes after the main content in the markup. When the two no longer fit side by side, the sidebar wraps below the content at full width, and a screen reader meets the article first."
      - name: ".ds-acc"
        does: "An accordion inside the sidebar drops its rules, goes single-column for the narrow measure, and turns its +/− marker Link Blue so a closed one still reads as interactive. No extra class."
  - id: dividers
    title: "Dividers"
    summary: "A rule between things. It belongs in the same conversation as the card, because both answer the same question and the answer is usually neither: this system groups with space first, and a line drawn where space would have done adds noise without adding meaning."
    classes:
      - name: "<hr>"
        does: "The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role=\"separator\"` for free."
      - name: ".ds-divider--tight"
        does: "Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning."
      - name: ".ds-divider--flush"
        does: "No margin at all; the caller owns the spacing."
      - name: ".ds-divider"
        does: "The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`."
      - name: ".ds-divider--vertical"
        does: "For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context."
  - id: marginalia
    title: "Marginalia and gutter space"
    summary: "At wide screen widths, our max content width leaves enough gutter space on the sides for marginalia. A short note beside the block it belongs to is appropriate for annotation-style content. At narrower widths, it is hidden in an info icon in the block’s top-right corner. Try it by widening and narrowing your screen."
    classes:
      - name: ".ds-marginalia"
        does: "The note, a `<details>`. Its first child in the block, so it is read before the thing it annotates. The block supplies `position: relative`; `.ds-card` already does."
      - name: ".ds-marginalia-body"
        does: "The text, with `.ds-annotation` for the voice. In the margin it has no chrome; folded, it opens as a small panel under the mark."
      - name: ".is-sr-only"
        does: "Required on the mark. The icon is `aria-hidden`, so without it the control announces as nothing."
    notes:
      - "A margin note is one or two sentences. Anything longer belongs in the main content."
  - id: page-zones
    title: "Page zones"
    group: "Modifiers"
    summary: "The page ground is white, and the thing the page is about sits directly on it. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material. The zone is named for its role, because the ground changes in dark mode."
    classes:
      - name: ".ds-zone-secondary"
        does: "Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode."
      - name: ".ds-full"
        does: "On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own."
  - id: wide-page
    title: "Wide page"
    group: "Modifiers"
    summary: "A dense internal tool can use a wider page: 1080px instead of 850px. Use it for tables and filters that do not fit the standard width, not for prose."
rules:
  - "**Use only the questions the content raises.** When a page uses more than one layer, they stack in this order: navigation, then tabs, then filters."
  - "**One control of each kind per view.** Never two rows of tabs, and never two filter bars."
  - "**No tabs inside a tab panel.**"
  - "**Filters apply to everything below them.**"
  - "**One Apply button per filter bar.**"
  - "**A number that changes a calculation is a setting, not a filter.**"
  - "**No breadcrumbs.** In complex tools, the secondary navigation fills this role already. It shows the user's place as well as being functional navigation. arXiv has a wide but shallow site and does not need traditional breadcrumbs."
  - "**One main landmark.** Put the page's content in a single `<main>`. A page with two, or with none, gives a screen-reader user nothing to jump to."
  - "**Label every aside.** A sidebar is an `<aside>` with an `aria-label` that says what it holds, so it announces as a complementary landmark with a name, not as part of the article."
  - "**Headings continue the outline inside a card.** A heading inside a container takes the next level down from the section it sits in. Do not skip a level because the content is in a card."
  - "**Use native disclosure.** Build accordions, margin notes and the TOC bar on `<details>` and `<summary>`: the summary is focusable and toggles with Enter and Space for free. Do not rebuild them from `<div>` elements and click handlers."
  - "**Nothing required lives only in a collapsed panel.** Anything legally or practically required, such as a warning or a licence, must also exist in always-visible flow. A closed accordion, a folded margin note and a popover are all places a reader may never open."
---

# Layout patterns

This section covers our primary patterns for differentiating and organizing content based on user needs. The organizing principle to follow throughout: Choose typographic and proximity-based organization patterns first, reach for visible containers only when called for.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Evaluating user needs

What a user needs to learn determines the right organizational pattern to employ for any group of content. Use the four questions below as a starting point. Each question has a test and a set of patterns that answer it. Most content will fit under one of these questions. Have an edge case? Discuss it with the design team.

> Where am I? (The address or the item changes): [Header](header.html) and [secondary navigation](header.html#secondary-navigation): sections of a site or tool; [Steps](header.html#steps): an ordered process; [Pager](pager.html): a queue, one item at a time; [Numbered pages](pager.html#numbered-pages): a long list split across pages; [TOC bar](progressive-disclosure.html#toc-bar): sections of one long page

> What matters here? (Directing user attention): [Spacing](spacing.html) and [dividers](#dividers): separate content; [Page container](#the-page-container), [page zones](#page-zones) and [wide page](#wide-page): the page frame; [Sidebar](#sidebar) and [marginalia](#marginalia): supporting content; [Cards](cards.html) and [tables](tables.html): records

> Which part do I need? (The content swaps in place): [Tabs](progressive-disclosure.html#tabs): one view at a time; [Filter bar](tables.html#filter-bar): narrowed data; [Sections of one page](typography.html#the-heading-scale): views to compare

> Can I learn more? (Richer details are revealed upon request): [Tooltip](forms.html#tooltip) and [popover](progressive-disclosure.html#popover): detail on request; [Show more](progressive-disclosure.html#show-more) and [accordion](progressive-disclosure.html#accordion): more in the flow; [Modal](modals.html): a decision first; [Actions attached to content](buttons.html#small-actions-attached-to-content): act on one item

## The page container

Every page sits in `.ds-container`. It centres the content in a column at the standard reading width, 850px at most, with a margin of at least 24px on each side. For a band that runs edge to edge, see [Page zones](#page-zones).

## Sidebar

A sidebar sits to the right of the main column and contains supplementary content. If the content is secondary, distinct from the main content, and it is important that it not be pushed far down the page, then a sidebar is appropriate.

```html
<div>
<article>…</article>
<aside class="ds-sidebar" aria-label="Paper details">
  <details class="ds-acc" open>
    <summary>Versions</summary>
    <div class="ds-acc-body">
      <dl>
        <dt>v3 · current</dt><dd>24 Apr 2026</dd>
        <dt>v2</dt><dd><a href="#">2 Mar 2026</a></dd>
      </dl>
    </div>
  </details>
  <details class="ds-acc">
    <summary>Paper information</summary>
    <div class="ds-acc-body">…</div>
  </details>
</aside>
</div>
```

- `.ds-sidebar` — On an `<aside>` with an `aria-label` that names what it holds: a complementary landmark. Its parent becomes the two-column layout, with the main content taking the spare width, the sidebar 17rem wide, and `--ds-space-section` between them. Blocks inside the sidebar are 24px apart (`--ds-space-6`). Nothing in it is sticky.
- `<aside>` — The sidebar comes after the main content in the markup. When the two no longer fit side by side, the sidebar wraps below the content at full width, and a screen reader meets the article first.
- `.ds-acc` — An accordion inside the sidebar drops its rules, goes single-column for the narrow measure, and turns its +/− marker Link Blue so a closed one still reads as interactive. No extra class.

## Dividers

A rule between things. It belongs in the same conversation as the card, because both answer the same question and the answer is usually neither: this system groups with space first, and a line drawn where space would have done adds noise without adding meaning.

```html
<p>A section of content.</p>
<hr>
<p>The next section.</p>
<hr>
<p>And the one after it.</p>
```

```html
<p>An item in a group.</p>
<hr class="ds-divider ds-divider--tight">
<p>The next item in the same group.</p>
<hr class="ds-divider ds-divider--tight">
<p>And the one after it.</p>
```

```html
<div class="ds-btn-group">
<span>Search</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Submit</span>
<span class="ds-divider ds-divider--vertical" aria-hidden="true"></span>
<span>Donate</span>
</div>
```

- `<hr>` — The preferred form. Styled by the foundation with 32px above and below (`--ds-space-8`), no class needed, and it includes `role="separator"` for free.
- `.ds-divider--tight` — Between items in a group rather than between sections: 16px above and below (`--ds-space-block`). It works on an `<hr>`, which keeps the separator meaning.
- `.ds-divider--flush` — No margin at all; the caller owns the spacing.
- `.ds-divider` — The class form, for where an `<hr>` will not fit: inside a flex row, or on an element that is already there. It is decorative, so mark it `aria-hidden` — a real separator should be an `<hr>`.
- `.ds-divider--vertical` — For a row of controls. Height is in `em`, so it follows the row's own text instead of needing a value per context.

## Marginalia and gutter space

At wide screen widths, our max content width leaves enough gutter space on the sides for marginalia. A short note beside the block it belongs to is appropriate for annotation-style content. At narrower widths, it is hidden in an info icon in the block’s top-right corner. Try it by widening and narrowing your screen.

```html
<div class="ds-card">
<details class="ds-marginalia">
  <summary><svg aria-hidden="true">…</svg><span class="is-sr-only">Note</span></summary>
  <p class="ds-marginalia-body ds-annotation">The note.</p>
</details>
…
</div>
```

- `.ds-marginalia` — The note, a `<details>`. Its first child in the block, so it is read before the thing it annotates. The block supplies `position: relative`; `.ds-card` already does.
- `.ds-marginalia-body` — The text, with `.ds-annotation` for the voice. In the margin it has no chrome; folded, it opens as a small panel under the mark.
- `.is-sr-only` — Required on the mark. The icon is `aria-hidden`, so without it the control announces as nothing.

> A margin note is one or two sentences. Anything longer belongs in the main content.

## Page zones  (Modifiers)

The page ground is white, and the thing the page is about sits directly on it. The **secondary** zone is a tinted band for what introduces or supports that content: the opening of the page, and any closing material. The zone is named for its role, because the ground changes in dark mode.

```html
<div class="ds-container">
  <div class="ds-full ds-zone-secondary">               <!-- tinted: introduces -->
    <header class="ds-page-header">…</header>
  </div>
  <section>…</section>                                  <!-- page ground: the thing itself -->
  <div class="ds-full ds-zone-secondary">               <!-- tinted: supports -->
    <section>…</section>
  </div>
</div>
```

- `.ds-zone-secondary` — Goes on a `.ds-full` band and gives it the tinted ground and its own top and bottom padding. A band that opens or closes the page runs to the container’s edge. The colour is the token `--ds-zone-secondary-bg`: the class is what you write, and the token is the colour the class applies, which changes in dark mode.
- `.ds-full` — On a direct child of `.ds-container`. The child runs across all three columns, from edge to edge, and its padding brings its own content back in line with the centre column. It has no background of its own.

## Wide page  (Modifiers)

A dense internal tool can use a wider page: 1080px instead of 850px. Use it for tables and filters that do not fit the standard width, not for prose.

## Rules

- **Use only the questions the content raises.** When a page uses more than one layer, they stack in this order: navigation, then tabs, then filters.
- **One control of each kind per view.** Never two rows of tabs, and never two filter bars.
- **No tabs inside a tab panel.**
- **Filters apply to everything below them.**
- **One Apply button per filter bar.**
- **A number that changes a calculation is a setting, not a filter.**
- **No breadcrumbs.** In complex tools, the secondary navigation fills this role already. It shows the user's place as well as being functional navigation. arXiv has a wide but shallow site and does not need traditional breadcrumbs.
- **One main landmark.** Put the page's content in a single `<main>`. A page with two, or with none, gives a screen-reader user nothing to jump to.
- **Label every aside.** A sidebar is an `<aside>` with an `aria-label` that says what it holds, so it announces as a complementary landmark with a name, not as part of the article.
- **Headings continue the outline inside a card.** A heading inside a container takes the next level down from the section it sits in. Do not skip a level because the content is in a card.
- **Use native disclosure.** Build accordions, margin notes and the TOC bar on `<details>` and `<summary>`: the summary is focusable and toggles with Enter and Space for free. Do not rebuild them from `<div>` elements and click handlers.
- **Nothing required lives only in a collapsed panel.** Anything legally or practically required, such as a warning or a licence, must also exist in always-visible flow. A closed accordion, a folded margin note and a popover are all places a reader may never open.
