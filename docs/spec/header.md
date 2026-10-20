---
page: header.html
title: "Site header"
summary: "The arXiv public-page header sets the tone for the entire platform: simple, straightforward, and utilitarian. It consists of a dark band with logo on the left, and navigation, search, and account links on the right. An optional, dismissible announcement banner can be displayed above the header. Absolute consistency across all pages is critical. The header is in transition. Pages on arxiv.org use the [transitional header](#transitional-header) from `templates/` now, and will move to the [aspirational header](#aspirational-header) after the migration. Internal pages have their own header and variations, see [Internal header](#internal-headers) for an example. The bars under the header, such as secondary navigation and steps, are on [Navigation](navigation.html)."
stylesheet: design-system.css
components:
  - id: transitional-header
    title: "Transitional header (currently in production)"
    summary: "The header on arxiv.org now. A page includes it from `templates/` rather than copying its markup; the [templates README](doc.html?src=templates/README.md) says how to install it and what each variable does. The examples are the template itself, rendered, so they always match production. On arxiv.org the navigation folds behind the menu button when the window is narrower than 600px; the phone example here folds to fit its box."
    classes:
      - name: "signed_in"
        does: "Per session: one \"Account\" link (auth_url + account_path, where the reader logs out) instead of \"Log in\"."
      - name: "header_page_actions"
        does: "Per page, this page's actions (its links and buttons) in the bar's tools region (.ds-site-header-tools, after the navigation): host markup, each <a> or <button> a direct child. '' (the default) leaves the region out. Never site navigation, which stays as DESIGN-POLICIES sets it."
  - id: aspirational-header
    title: "Aspirational header (post-migration)"
    summary: "The header arxiv.org will move to. It differs from the transitional header in three ways: the bar has a theme control after the navigation; Log in and Account sit outside the navigation, in the account area; and signed in, the bar shows a greeting and an Account menu that holds Log out."
  - id: the-header-unit
    title: "The header unit"
    summary: "Every header has the same regions, in this order: logo, Search (public pages), navigation, tools (optional) and account. The header scrolls away with the page; see [On small screens](#on-small-screens) for narrow screens."
    classes:
      - name: ".ds-skip-link"
        does: "The skip link. The first focusable element on the page, visible only on keyboard focus. Its `href` is the id of the main content."
      - name: ".ds-site-header"
        does: "The bar. With no modifier it is the arxiv.org header."
      - name: ".ds-site-header-logo"
        does: "The brand slot, image or wordmark. Takes `margin-right: auto`. On arxiv.org it is the logo image, never the word typed out; its alt text says “archive”."
      - name: ".ds-site-header-search-link"
        does: "arxiv.org’s Search: an `<a href=\"/search\">` before the navigation and outside it, so it stays in the bar when the navigation folds. JavaScript upgrades it to open the search overlay; without JavaScript it goes to the search page."
      - name: ".ds-site-header-nav"
        does: "The site’s sections, in a `<nav>` with an `aria-label`."
      - name: ".ds-nav-icon"
        does: "An icon beside a link label, sized by the stylesheet and quieter than the text. `aria-hidden=\"true\"`; the label gives the name."
      - name: ".ds-site-header-divider"
        does: "A vertical hairline between groups of links or between regions, on the bar’s own divider token. Takes `aria-hidden=\"true\"`. Hidden while the navigation is folded away."
      - name: ".ds-site-header-tools"
        does: "Optional, after the navigation: the theme control, and a page’s own actions."
      - name: ".ds-theme-toggle"
        does: "The theme control, with its live region `#ds-theme-status`. See [The theme control](dark-mode.html#the-theme-control)."
      - name: ".ds-site-header-account"
        does: "The last region: Log in, or the greeting and the Account menu. It sits outside the `<nav>`, because an account menu is not a site section."
      - name: ".ds-site-header-login"
        does: "The only item in the bar with heavier text: Log in, or the Account menu’s `<summary>`."
      - name: ".ds-site-header-dropdown"
        does: "A menu group in the bar, built on `<details>`. See [Header dropdown menus](#header-dropdown-menus)."
      - name: ".ds-search-overlay"
        does: "The search overlay, after the header. The template’s `header.js` opens it from the Search link or Ctrl/Cmd+K, and closes it on Escape, a click outside the panel, or focus leaving it."
      - name: ".ds-search-overlay-panel"
        does: "The overlay’s panel, hanging from the bottom of the bar at every width. Opening it closes the menu. Its field and hint are the ordinary `.ds-input` and `.ds-hint`."
  - id: signed-in
    title: "Signed in"
    summary: "Signed in, the account area shows a greeting with the reader’s given name and an **Account** menu that holds Log out. A long name is cut to 14 characters."
    classes:
      - name: ".ds-site-header-greeting"
        does: "The given name only, capped at 14 characters with an ellipsis, as the Long name example shows; the host passes the given name and nothing else. It is not a link: the Account menu beside it is what the reader acts on. On a narrow bar it is the first thing to go."
      - name: "<form method=\"post\">"
        does: "Log out is a button in a form that posts, never a link, because a browser can follow a link by itself, and logging out changes the reader’s state."
  - id: on-small-screens
    title: "On small screens"
    summary: "The header fits itself to the space it has. When the regions do not fit on one row, the greeting goes first, then the navigation folds behind a menu button. On a public bar the tools and the account area fold into the same menu, so the bar keeps the logo, the Search icon and the menu button. An internal bar folds the same way, and keeps its search fields in the bar while they fit; after that they open from a Search button. See [Internal header](#internal-headers). The transitional header folds its navigation when the window is narrower than 600px."
    classes:
      - name: "header.js"
        does: "These docs’ fold-by-fit script, `docs/header.js`, once per page. It finds every `.ds-site-header` and keeps each one on a single row, with no breakpoint to choose. Without JavaScript the bar wraps onto more rows instead, so nothing is hidden. The templates load their own script, so a page that uses them adds none."
      - name: ".ds-site-header-nav-toggle, .ds-site-header-search-toggle, .ds-site-header-tools-toggle"
        does: "The menu button, the Search button for search fields, and the Tools button on a bar without an account area. The script adds each one, so they are not in the markup. Each has `aria-expanded` and `aria-controls`, and Escape closes the open region and returns focus to its button."
      - name: ".is-collapsible, .is-single-menu, .is-greeting-hidden, .is-nav-collapsed, .is-search-collapsed, .is-tools-collapsed, .is-menu-open, .is-search-open, .is-overfull, .is-open, .is-measuring"
        does: "State classes the script sets on the bar and on an open region. They are never written by hand. `.is-single-menu` marks a bar with an account area, whose menu holds the navigation, the tools and the account area. `.is-overfull` lets the bar wrap when even the folded bar is too wide for its space."
    notes:
      - "The script answers to the width of the bar, not of the window, so the phone example folds inside a narrower box on a wide screen. Open the menu to see the folded rows."
  - id: header-dropdown-menus
    title: "Header dropdown menus"
    summary: "A property whose sections need grouping adds `.ds-site-header-dropdown`, built on `<details>` so it opens and closes with no JavaScript. A page may add close-on-outside-click and Esc as enhancement. The Account menu is the same component."
    classes:
      - name: ".ds-site-header-dropdown"
        does: "A `<details>` group in the bar. Optional. The summary sits in the bar and takes the surface tokens, so it is correct on either variant."
      - name: ".ds-site-header-menu"
        does: "The floating panel, a light surface on either bar. It is anchored to its trigger’s right edge, so the last menu in the bar stays on screen."
      - name: ".ds-panel-label"
        does: "A group heading inside a menu."
      - name: "aria-current=\"page\""
        does: "On the menu link for the page the reader is on. The menu shows it in bold, and a screen reader announces it."
  - id: with-the-announcement-band
    title: "With the announcement band"
    group: "Modifiers"
    summary: "When arXiv has something to say to everyone, an announcement band shows above the bar, and the two scroll away together. See [Announcement band](messages.html#announcement-band)."
    classes:
      - name: "#ds-announcement"
        does: "The mount, which the header template writes before the bar. While an announcement is active, `banner.js` draws the band into it; the host writes only the skip link and the include. The band’s parts are on [Special messages](messages.html#announcement-band)."
  - id: the-light-variant
    title: "The light variant"
    group: "Modifiers"
    summary: "For pages about arXiv from outside it, such as this documentation. `.ds-site-header--light` re-points the seven surface tokens and nothing else. Every page that is part of arXiv, public or internal, uses the standard bar."
    classes:
      - name: ".ds-site-header--light"
        does: "The bar is white with Library Grey links, Repository Brown emphasis and a Border Light bottom edge, and the standard focus ring."
      - name: ".ds-site-header-logo"
        does: "On a property that is not arxiv.org, the slot may hold that property’s own wordmark as text; it takes the bar’s emphasis colour."
    notes:
      - "The bar at the top of this page is the light variant, with dropdown groups."
  - id: internal-headers
    title: "Internal header"
    group: "Modifiers"
    summary: "The Admin Console header: the standard bar, with the Admin Console logo. Each internal tool chooses the search fields, navigation and wordmark its users need; the regions, their order and the rules stay the same. Every internal tool uses an internal logo, not the public one, so the reader can tell they are in an internal tool. The internal stylesheet may re-point the bar’s colour tokens and nothing else."
    classes:
      - name: ".ds-site-header-logo img"
        does: "The tool’s own wordmark image, from `assets/images/logos/`. Its alt text names the tool in spoken form, such as “archive Admin Console”."
      - name: ".ds-site-header-search"
        does: "A `<form role=\"search\">` holding one `.ds-input` and its label, before the navigation, where public pages have the Search link. Two kinds of search are two of these. They stay in the bar while they fit, after the navigation and the account area have folded into the menu; on a phone they open from a Search button."
      - name: ".ds-site-header-greeting"
        does: "The same first-name greeting as the public header, capped at 14 characters."
  - id: sticky-header
    title: "Sticky header"
    group: "Modifiers"
    summary: "Internal tools only. Adding `.ds-site-header--sticky` keeps the bar at the top of the viewport while the page scrolls, and the stylesheet sets `scroll-padding-top` on the page so a link to a section does not land under the bar. A page that uses it keeps no other sticky bar. It is not applied to the examples on this page, which already keeps the TOC bar in view."
rules:
  - "A page includes the header from `templates/` and writes the skip link before it, pointing at its own main content. The [templates README](doc.html?src=templates/README.md) says how to install the header, which variables a host sets, and how the stylesheet, scripts and logo are published and cached. [Banner announcements](doc.html?src=templates/BANNER_ANNOUNCEMENTS.md) says how to put up an announcement."
  - "**Regions, in one order.** Logo, search (the Search link on public pages, search fields on internal tools), navigation, tools (optional), account. In the transitional header, Log in or Account is the last link in the navigation, and page actions come after it."
  - "**Navigation sits on the right.** The space after the logo stays empty."
  - "**No more than four links in arxiv.org’s navigation.** The logo and Log in do not count (DESIGN-POLICIES). A host does not change the template’s navigation."
  - "**Tools hold the theme control and a page’s own actions.** The transitional header has page actions only. A control that acts on the page’s data, such as Refresh, goes beside the page heading, with the time the data was last updated."
  - "**Public search opens on request; internal search stays in view.** On arxiv.org, Search is a link before the navigation. Internal tools keep their search fields in the bar while they fit."
  - "**Log out.** Today a signed-in reader logs out on the account page. In the aspirational header, Log out is in the Account menu, one menu away on every page."
  - "**The greeting is the first name.** The aspirational header shows the given name only, capped at 14 characters, on public and internal headers."
  - "**Sticky on internal tools only.** arxiv.org’s public header scrolls away (DESIGN-POLICIES)."
  - "**No breadcrumbs.** arXiv’s sitemap is wide and shallow, so the header navigation and the [secondary navigation](navigation.html#secondary-navigation) show the reader’s place."
  - "**Type sizes are rem**, so a reader’s browser font size applies. In print the header keeps only its logo, 28px tall."
  - "**The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content."
  - "**Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page."
  - "**The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish)."
  - "**The account area is not navigation.** In the aspirational header it sits outside the `<nav>`, so a screen reader user who lists landmarks finds only site sections there."
  - "**Name every search field.** A search field in the bar is a `<form role=\"search\">` with a `<label>`, hidden with `.is-sr-only` if needed, that says what it searches. The placeholder is not the name: it disappears as soon as someone types."
  - "**Mark the current page in the markup.** Put `aria-current=\"page\"` on the current link in the secondary navigation and in header menus."
---

# Site header

The arXiv public-page header sets the tone for the entire platform: simple, straightforward, and utilitarian. It consists of a dark band with logo on the left, and navigation, search, and account links on the right. An optional, dismissible announcement banner can be displayed above the header. Absolute consistency across all pages is critical. The header is in transition. Pages on arxiv.org use the [transitional header](#transitional-header) from `templates/` now, and will move to the [aspirational header](#aspirational-header) after the migration. Internal pages have their own header and variations, see [Internal header](#internal-headers) for an example. The bars under the header, such as secondary navigation and steps, are on [Navigation](navigation.html).

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Transitional header (currently in production)

The header on arxiv.org now. A page includes it from `templates/` rather than copying its markup; the [templates README](doc.html?src=templates/README.md) says how to install it and what each variable does. The examples are the template itself, rendered, so they always match production. On arxiv.org the navigation folds behind the menu button when the window is narrower than 600px; the phone example here folds to fit its box.

```html
<div id="ds-announcement"></div>
<script src="https://static.arxiv.org/static/design-system/latest/chrome/banner.js" defer></script>
<script src="https://static.arxiv.org/static/design-system/latest/chrome/header.js" defer></script>
<header class="ds-site-header ">
  <a aria-hidden="true" tabindex="-1" href="https://arxiv.org/IgnoreMe" class="is-sr-only"></a>
  <a href="https://arxiv.org/" class="ds-site-header-logo" aria-label="archive home">
    <img src="https://static.arxiv.org/static/design-system/latest/logos/arxiv-logo.svg" alt="archive">
  </a>
  <a id="ds-search-toggle" class="ds-site-header-search-link" href="https://arxiv.org/search" aria-controls="ds-search-overlay" aria-expanded="false">
    <svg class="ds-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
      <circle cx="11" cy="11" r="8"/>
      <line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <span>Search</span>
  </a>
  <button type="button" id="ds-nav-toggle" class="ds-site-header-nav-toggle"
    aria-label="Open menu" aria-controls="ds-site-header-nav" aria-expanded="false">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
      <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>
    </svg>
  </button>
  <nav class="ds-site-header-nav" id="ds-site-header-nav" aria-label="Main navigation">
    <a href="https://arxiv.org/submit">Submit</a>
    <a href="https://info.arxiv.org/about/donate.html">Donate</a>
    <span class="ds-site-header-divider" aria-hidden="true"></span>
    <a href="https://arxiv.org/login" class="ds-site-header-login">Log in</a>
  </nav>
</header>
<div class="ds-search-overlay" id="ds-search-overlay" hidden>
  <div class="ds-search-overlay-panel" role="search">
    <form method="GET" action="https://arxiv.org/search">
      <label for="ds-search-input" class="is-sr-only">Search arXiv</label>
      <input type="text" name="query" id="ds-search-input" class="ds-input" autocomplete="off"
        placeholder="Search papers by title, author, abstract, or ID...">
      <input type="hidden" name="searchtype" value="all">
      <input type="hidden" name="source" value="header">
    </form>
    <p class="ds-hint">
      Press Enter to search · <a href="https://arxiv.org/search/advanced">Advanced search</a>
    </p>
  </div>
</div>
```

- `signed_in` — Per session: one "Account" link (auth_url + account_path, where the reader logs out) instead of "Log in".
- `header_page_actions` — Per page, this page's actions (its links and buttons) in the bar's tools region (.ds-site-header-tools, after the navigation): host markup, each <a> or <button> a direct child. '' (the default) leaves the region out. Never site navigation, which stays as DESIGN-POLICIES sets it.

## Aspirational header (post-migration)

The header arxiv.org will move to. It differs from the transitional header in three ways: the bar has a theme control after the navigation; Log in and Account sit outside the navigation, in the account area; and signed in, the bar shows a greeting and an Account menu that holds Log out.

## The header unit

Every header has the same regions, in this order: logo, Search (public pages), navigation, tools (optional) and account. The header scrolls away with the page; see [On small screens](#on-small-screens) for narrow screens.

```html
<!-- First focusable element on the page -->
<a class="ds-skip-link" href="#main">Skip to main content</a>

<header class="ds-site-header">
  <a href="/" class="ds-site-header-logo" aria-label="archive home">
    <img src="logo_arxiv-primary.svg" alt="archive">
  </a>
  <a id="ds-search-toggle" class="ds-site-header-search-link" href="/search" aria-controls="ds-search-overlay" aria-expanded="false">
    <svg class="ds-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
      <circle cx="11" cy="11" r="8"/>
      <line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <span>Search</span>
  </a>
  <nav class="ds-site-header-nav" id="ds-site-header-nav" aria-label="Main navigation">
    <a href="/submit">Submit</a>
    <a href="/about/donate">Donate</a>
  </nav>
  <div class="ds-site-header-tools">
    <button type="button" class="ds-theme-toggle"></button>
    <span id="ds-theme-status" class="is-sr-only" role="status"></span>
  </div>
  <span class="ds-site-header-divider" aria-hidden="true"></span>
  <div class="ds-site-header-account">
    <a href="/login" class="ds-site-header-login">Log in</a>
  </div>
</header>
```

- `.ds-skip-link` — The skip link. The first focusable element on the page, visible only on keyboard focus. Its `href` is the id of the main content.
- `.ds-site-header` — The bar. With no modifier it is the arxiv.org header.
- `.ds-site-header-logo` — The brand slot, image or wordmark. Takes `margin-right: auto`. On arxiv.org it is the logo image, never the word typed out; its alt text says “archive”.
- `.ds-site-header-search-link` — arxiv.org’s Search: an `<a href="/search">` before the navigation and outside it, so it stays in the bar when the navigation folds. JavaScript upgrades it to open the search overlay; without JavaScript it goes to the search page.
- `.ds-site-header-nav` — The site’s sections, in a `<nav>` with an `aria-label`.
- `.ds-nav-icon` — An icon beside a link label, sized by the stylesheet and quieter than the text. `aria-hidden="true"`; the label gives the name.
- `.ds-site-header-divider` — A vertical hairline between groups of links or between regions, on the bar’s own divider token. Takes `aria-hidden="true"`. Hidden while the navigation is folded away.
- `.ds-site-header-tools` — Optional, after the navigation: the theme control, and a page’s own actions.
- `.ds-theme-toggle` — The theme control, with its live region `#ds-theme-status`. See [The theme control](dark-mode.html#the-theme-control).
- `.ds-site-header-account` — The last region: Log in, or the greeting and the Account menu. It sits outside the `<nav>`, because an account menu is not a site section.
- `.ds-site-header-login` — The only item in the bar with heavier text: Log in, or the Account menu’s `<summary>`.
- `.ds-site-header-dropdown` — A menu group in the bar, built on `<details>`. See [Header dropdown menus](#header-dropdown-menus).
- `.ds-search-overlay` — The search overlay, after the header. The template’s `header.js` opens it from the Search link or Ctrl/Cmd+K, and closes it on Escape, a click outside the panel, or focus leaving it.
- `.ds-search-overlay-panel` — The overlay’s panel, hanging from the bottom of the bar at every width. Opening it closes the menu. Its field and hint are the ordinary `.ds-input` and `.ds-hint`.

## Signed in

Signed in, the account area shows a greeting with the reader’s given name and an **Account** menu that holds Log out. A long name is cut to 14 characters.

```html
<span class="ds-site-header-divider" aria-hidden="true"></span>
<div class="ds-site-header-account">
  <span class="ds-site-header-greeting">Welcome <b>Ada</b></span>
  <details class="ds-site-header-dropdown">
    <summary class="ds-site-header-login">Account</summary>
    <div class="ds-site-header-menu">
      <a href="/account">Your account</a>
      <form method="post" action="/logout">
        <button type="submit">Log out</button>
      </form>
    </div>
  </details>
</div>
```

- `.ds-site-header-greeting` — The given name only, capped at 14 characters with an ellipsis, as the Long name example shows; the host passes the given name and nothing else. It is not a link: the Account menu beside it is what the reader acts on. On a narrow bar it is the first thing to go.
- `<form method="post">` — Log out is a button in a form that posts, never a link, because a browser can follow a link by itself, and logging out changes the reader’s state.

## On small screens

The header fits itself to the space it has. When the regions do not fit on one row, the greeting goes first, then the navigation folds behind a menu button. On a public bar the tools and the account area fold into the same menu, so the bar keeps the logo, the Search icon and the menu button. An internal bar folds the same way, and keeps its search fields in the bar while they fit; after that they open from a Search button. See [Internal header](#internal-headers). The transitional header folds its navigation when the window is narrower than 600px.

```html
<!-- Once per page, after the header. Nothing else changes. -->
<script src="header.js" defer></script>
```

- `header.js` — These docs’ fold-by-fit script, `docs/header.js`, once per page. It finds every `.ds-site-header` and keeps each one on a single row, with no breakpoint to choose. Without JavaScript the bar wraps onto more rows instead, so nothing is hidden. The templates load their own script, so a page that uses them adds none.
- `.ds-site-header-nav-toggle, .ds-site-header-search-toggle, .ds-site-header-tools-toggle` — The menu button, the Search button for search fields, and the Tools button on a bar without an account area. The script adds each one, so they are not in the markup. Each has `aria-expanded` and `aria-controls`, and Escape closes the open region and returns focus to its button.
- `.is-collapsible, .is-single-menu, .is-greeting-hidden, .is-nav-collapsed, .is-search-collapsed, .is-tools-collapsed, .is-menu-open, .is-search-open, .is-overfull, .is-open, .is-measuring` — State classes the script sets on the bar and on an open region. They are never written by hand. `.is-single-menu` marks a bar with an account area, whose menu holds the navigation, the tools and the account area. `.is-overfull` lets the bar wrap when even the folded bar is too wide for its space.

> The script answers to the width of the bar, not of the window, so the phone example folds inside a narrower box on a wide screen. Open the menu to see the folded rows.

## Header dropdown menus

A property whose sections need grouping adds `.ds-site-header-dropdown`, built on `<details>` so it opens and closes with no JavaScript. A page may add close-on-outside-click and Esc as enhancement. The Account menu is the same component.

```html
<header class="ds-site-header ds-site-header--light">
  <a href="/" class="ds-site-header-logo">arXiv Design System</a>
  <nav class="ds-site-header-nav" aria-label="Design system">
    <details class="ds-site-header-dropdown">
      <summary>Design Patterns</summary>
      <div class="ds-site-header-menu">
        <span class="ds-panel-label">Components</span>
        <a href="colors.html">Colors</a>
        <a href="header.html" aria-current="page">Site header</a>
        <!-- … -->
      </div>
    </details>
    <details class="ds-site-header-dropdown">
      <summary>Docs</summary>
      <div class="ds-site-header-menu">
        <a href="using.html">Using the system</a>
        <!-- … -->
      </div>
    </details>
  </nav>
</header>
```

- `.ds-site-header-dropdown` — A `<details>` group in the bar. Optional. The summary sits in the bar and takes the surface tokens, so it is correct on either variant.
- `.ds-site-header-menu` — The floating panel, a light surface on either bar. It is anchored to its trigger’s right edge, so the last menu in the bar stays on screen.
- `.ds-panel-label` — A group heading inside a menu.
- `aria-current="page"` — On the menu link for the page the reader is on. The menu shows it in bold, and a screen reader announces it.

## With the announcement band  (Modifiers)

When arXiv has something to say to everyone, an announcement band shows above the bar, and the two scroll away together. See [Announcement band](messages.html#announcement-band).

```html
<a class="ds-skip-link" href="#main">Skip to main content</a>
<div id="ds-announcement"></div>
<header class="ds-site-header">…</header>
```

- `#ds-announcement` — The mount, which the header template writes before the bar. While an announcement is active, `banner.js` draws the band into it; the host writes only the skip link and the include. The band’s parts are on [Special messages](messages.html#announcement-band).

## The light variant  (Modifiers)

For pages about arXiv from outside it, such as this documentation. `.ds-site-header--light` re-points the seven surface tokens and nothing else. Every page that is part of arXiv, public or internal, uses the standard bar.

```html
<header class="ds-site-header ds-site-header--light">
  <a href="/" class="ds-site-header-logo">arXiv Design System</a>
  <nav class="ds-site-header-nav" aria-label="Site navigation">
    <a href="/patterns">Patterns</a>
    <a href="/mockups">Mockups</a>
    <a href="/docs">Docs</a>
  </nav>
</header>
```

- `.ds-site-header--light` — The bar is white with Library Grey links, Repository Brown emphasis and a Border Light bottom edge, and the standard focus ring.
- `.ds-site-header-logo` — On a property that is not arxiv.org, the slot may hold that property’s own wordmark as text; it takes the bar’s emphasis colour.

> The bar at the top of this page is the light variant, with dropdown groups.

## Internal header  (Modifiers)

The Admin Console header: the standard bar, with the Admin Console logo. Each internal tool chooses the search fields, navigation and wordmark its users need; the regions, their order and the rules stay the same. Every internal tool uses an internal logo, not the public one, so the reader can tell they are in an internal tool. The internal stylesheet may re-point the bar’s colour tokens and nothing else.

```html
<div class="ds-internal">
<header class="ds-site-header">
  <a href="/" class="ds-site-header-logo">
    <img src="logo_arxiv-admin-light.svg" alt="archive Admin Console">
  </a>
  <form class="ds-site-header-search" role="search" action="/users">
    <label class="is-sr-only" for="search-users">Search users</label>
    <input class="ds-input" type="search" id="search-users" name="q" placeholder="Search users">
  </form>
  <form class="ds-site-header-search" role="search" action="/documents">
    <label class="is-sr-only" for="search-docs">Search submissions and documents</label>
    <input class="ds-input" type="search" id="search-docs" name="q" placeholder="Search submissions">
  </form>
  <nav class="ds-site-header-nav" aria-label="Admin Console">
    <a href="/resources">Resources</a>
    <a href="/submission">Submission</a>
    <a href="/support">User Support</a>
    <a href="/students">Students</a>
  </nav>
  <span class="ds-site-header-divider" aria-hidden="true"></span>
  <div class="ds-site-header-account">
    <span class="ds-site-header-greeting">Welcome <b>Shamsi</b></span>
    <details class="ds-site-header-dropdown">…</details>
  </div>
</header>
</div>
```

- `.ds-site-header-logo img` — The tool’s own wordmark image, from `assets/images/logos/`. Its alt text names the tool in spoken form, such as “archive Admin Console”.
- `.ds-site-header-search` — A `<form role="search">` holding one `.ds-input` and its label, before the navigation, where public pages have the Search link. Two kinds of search are two of these. They stay in the bar while they fit, after the navigation and the account area have folded into the menu; on a phone they open from a Search button.
- `.ds-site-header-greeting` — The same first-name greeting as the public header, capped at 14 characters.

## Sticky header  (Modifiers)

Internal tools only. Adding `.ds-site-header--sticky` keeps the bar at the top of the viewport while the page scrolls, and the stylesheet sets `scroll-padding-top` on the page so a link to a section does not land under the bar. A page that uses it keeps no other sticky bar. It is not applied to the examples on this page, which already keeps the TOC bar in view.

## Rules

- A page includes the header from `templates/` and writes the skip link before it, pointing at its own main content. The [templates README](doc.html?src=templates/README.md) says how to install the header, which variables a host sets, and how the stylesheet, scripts and logo are published and cached. [Banner announcements](doc.html?src=templates/BANNER_ANNOUNCEMENTS.md) says how to put up an announcement.
- **Regions, in one order.** Logo, search (the Search link on public pages, search fields on internal tools), navigation, tools (optional), account. In the transitional header, Log in or Account is the last link in the navigation, and page actions come after it.
- **Navigation sits on the right.** The space after the logo stays empty.
- **No more than four links in arxiv.org’s navigation.** The logo and Log in do not count (DESIGN-POLICIES). A host does not change the template’s navigation.
- **Tools hold the theme control and a page’s own actions.** The transitional header has page actions only. A control that acts on the page’s data, such as Refresh, goes beside the page heading, with the time the data was last updated.
- **Public search opens on request; internal search stays in view.** On arxiv.org, Search is a link before the navigation. Internal tools keep their search fields in the bar while they fit.
- **Log out.** Today a signed-in reader logs out on the account page. In the aspirational header, Log out is in the Account menu, one menu away on every page.
- **The greeting is the first name.** The aspirational header shows the given name only, capped at 14 characters, on public and internal headers.
- **Sticky on internal tools only.** arxiv.org’s public header scrolls away (DESIGN-POLICIES).
- **No breadcrumbs.** arXiv’s sitemap is wide and shallow, so the header navigation and the [secondary navigation](navigation.html#secondary-navigation) show the reader’s place.
- **Type sizes are rem**, so a reader’s browser font size applies. In print the header keeps only its logo, 28px tall.
- **The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content.
- **Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page.
- **The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish).
- **The account area is not navigation.** In the aspirational header it sits outside the `<nav>`, so a screen reader user who lists landmarks finds only site sections there.
- **Name every search field.** A search field in the bar is a `<form role="search">` with a `<label>`, hidden with `.is-sr-only` if needed, that says what it searches. The placeholder is not the name: it disappears as soon as someone types.
- **Mark the current page in the markup.** Put `aria-current="page"` on the current link in the secondary navigation and in header menus.
