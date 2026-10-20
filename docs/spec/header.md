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
    summary: "Rendered directly from `design-system.css`. On a narrow screen the bar folds itself to fit; see [On small screens](#on-small-screens). The header is static — it scrolls away with the page (on arxiv.org the site header is never the sticky bar — DESIGN-POLICIES.md). Every header has the same regions, in this order: logo, Search (public pages), navigation, tools (optional), and account."
    classes:
      - name: ".ds-skip-link"
        does: "The skip link. The first focusable element on the page, visible only on keyboard focus. Its `href` is the id of the main content."
      - name: ".ds-site-header"
        does: "The bar. Bare, it is the arXiv header — arxiv.org cannot forget a class it never has to write."
      - name: ".ds-site-header-logo"
        does: "The brand slot, image or wordmark. Takes `margin-right: auto`. On arxiv.org it is the logo image, never the word typed out; its alt text says “archive”."
      - name: ".ds-site-header-search-link"
        does: "arxiv.org’s Search: an `<a href=\"/search\">` just before the navigation and outside it, so it stays in the bar when the navigation folds, and search opens from the same place at every width. JS may upgrade it to open the search overlay. Never a dead button — without JS it navigates to the search page. Folded, it shows its icon alone, at the menu button’s size; the word in its `<span>` stays for screen readers."
      - name: ".ds-site-header-nav"
        does: "The site’s sections, in a `<nav>` with an `aria-label`."
      - name: ".ds-nav-icon"
        does: "An icon beside a link label, sized by the stylesheet and quieter than the text. `aria-hidden=\"true\"`; the label gives the name."
      - name: ".ds-site-header-divider"
        does: "A vertical hairline between groups of links or between regions, on the bar’s own divider token. Takes `aria-hidden=\"true\"`. Hidden while the navigation is folded away."
      - name: ".ds-site-header-tools"
        does: "Optional. The controls one interface needs, after the navigation. On public pages it holds the theme control; internal tools add search fields and icon buttons. See [Internal header](#internal-headers)."
      - name: ".ds-theme-toggle"
        does: "The theme control, with its live region `#ds-theme-status`. See [The theme control](dark-mode.html#the-theme-control)."
      - name: ".ds-site-header-account"
        does: "The last region: Log in, or the greeting and the Account menu. It sits outside the `<nav>`, because an account menu is not a site section. On a phone it folds into the menu with the navigation, as the last rows."
      - name: ".ds-site-header-login"
        does: "The emphasis slot, and the only item in the bar that takes weight. Signed out it is the *Log in* link. Signed in it is the *Account* menu, with the greeting beside it."
      - name: ".ds-site-header-dropdown"
        does: "A menu group in the bar, built on `<details>`. See [Header dropdown menus](#header-dropdown-menus)."
      - name: ".ds-search-overlay"
        does: "The search overlay: a `hidden` scrim after the header that the shared chrome’s `header.js` opens from the Search link (or Ctrl/Cmd+K), and closes on Escape, a click on the scrim, or focus moving out of it. Without JS the Search link goes to the search page. Its markup is the transitional header’s."
      - name: ".ds-search-overlay-panel"
        does: "The overlay’s panel, hanging from the bottom of the bar at every width. Opening it closes the menu. Its field and hint are the ordinary `.ds-input` and `.ds-hint`."
  - id: signed-in
    title: "Signed in"
    summary: "Account-related items display at the right end of the bar and are the only items in a heavier text weight. Signed out it says **Log in**. Signed in it displays a greeting and name, and an **Account** menu that holds Log out. When names are long (and arXiv users have every type and structure of name) we truncate to a reasonable number of characters."
    classes:
      - name: ".ds-site-header-greeting"
        does: "The greeting takes the given name only — its first word — because the bar is chrome and a full legal name is more of it than the job needs. Even one word is user data of unbounded length in any script, so it is capped at 14 characters with an ellipsis, as the Long name example shows. A bar that reflows or overflows on a long name breaks for exactly the people whose names get tested least. The greeting is not a link. It is a statement; the thing you can act on is the Account menu beside it. Making the name itself the link would give that link the accessible name “Ada”, which says nothing about where it goes. It is the first thing dropped on a narrow bar: when the bar runs out of room the greeting hides and Account stays — the menu is the useful half, and the reader already knows their own name."
      - name: ".ds-site-header-greeting > b"
        does: "The name. The stylesheet caps it at 14 characters and ends it with an ellipsis; the host passes the given name and nothing else."
      - name: ".ds-site-header-login"
        does: "The same emphasis slot as when signed out, now on the `<summary>` of an Account menu (`.ds-site-header-dropdown`). The slot is about rank in the bar, not about which of the two words is in it."
      - name: "<form method=\"post\">"
        does: "Log out is a button in a form that posts, never a link. A link can be followed by a browser prefetch or from another site, and logging someone out changes their state."
  - id: on-small-screens
    title: "On small screens"
    summary: "The header fits itself to the space it has. When the regions do not fit on one row, the greeting goes first, then the navigation folds behind a menu button. On a public bar the tools and the account area fold into the same menu, so the bar keeps the logo, the Search icon and the menu button. An internal bar folds the same way at its last step, with its search fields behind a Search button of their own; see [Internal header](#internal-headers). The transitional header folds its navigation when the window is narrower than 600px."
    classes:
      - name: "header.js"
        does: "These docs’ fold-by-fit script, `docs/header.js`, once per page. It finds every `.ds-site-header` and keeps each one on a single row, with no breakpoint to choose. Without JavaScript the bar wraps onto more rows instead, so nothing is hidden. The templates load their own script, so a page that uses them adds none."
      - name: ".ds-site-header-nav-toggle, .ds-site-header-tools-toggle"
        does: "The menu button, and a second button: Search on a folded internal bar, or Tools on a bar that has tools and no navigation. The script adds each one, so they are not in the markup. Each has `aria-expanded` and `aria-controls`, and Escape closes the open region and returns focus to its button."
      - name: ".is-collapsible, .is-single-menu, .is-greeting-hidden, .is-nav-collapsed, .is-tools-collapsed, .is-menu-open, .is-overfull, .is-open, .is-measuring"
        does: "State classes the script sets on the bar and on an open region. They are never written by hand. `.is-single-menu` marks a bar whose menu holds the navigation, the tools and the account area: a public bar once folded, an internal bar at its last fold. `.is-overfull` lets the bar wrap when even the folded bar is too wide for its space."
    notes:
      - "The script answers to the width of the bar, not of the window, so the phone example folds inside a narrower box on a wide screen. Open the menu to see the folded rows."
  - id: header-dropdown-menus
    title: "Header dropdown menus"
    summary: "A property whose sections need grouping adds `.ds-site-header-dropdown`, built on `<details>` so it opens and closes with no JavaScript. A page may add close-on-outside-click and Esc as enhancement. The Account menu is the same component."
    classes:
      - name: ".ds-site-header-dropdown"
        does: "A `<details>` group in the bar. Optional. The summary sits in the bar and takes the surface tokens, so it is correct on either variant."
      - name: ".ds-site-header-menu"
        does: "The floating panel. Right-anchored, capped to the viewport. A floating panel is a light surface whichever bar summoned it, the same way a popover is. The menu anchors to its trigger’s **right** edge: the nav always sits at the right of the bar, and a left-anchored menu runs off the viewport on the last item — which is every bar’s last item, not an edge case."
      - name: ".ds-panel-label"
        does: "Group headings inside a menu use the system-wide label, not a bespoke class."
      - name: "aria-current=\"page\""
        does: "On the menu link for the page the reader is on. The menu shows it in bold, and a screen reader announces it."
  - id: with-the-announcement-band
    title: "With the announcement band"
    group: "Modifiers"
    summary: "When arXiv has something to say to everyone, an announcement band can be displayed above the header bar. Neither is fixed; the two scroll away together. See [Announcement band](messages.html#announcement-band) for the full documentation."
    classes:
      - name: "#ds-announcement"
        does: "The mount, which the header template writes before the bar. While an announcement is active, `banner.js` draws the band into it; the host writes only the skip link and the include. The band’s parts are on [Special messages](messages.html#announcement-band)."
  - id: the-light-variant
    title: "The light variant"
    group: "Modifiers"
    summary: "Adding `.ds-site-header--light` re-points seven surface tokens but declares no property of its own. It is for pages that comment on arXiv from outside it, such as this documentation. Every page that is part of arXiv, public or internal, uses the standard bar."
    classes:
      - name: ".ds-site-header--light"
        does: "Seven token values. No property overrides. The bar is white (`--ds-surface`) with Library Grey links, Repository Brown emphasis, and a Border Light bottom edge; the standard focus ring replaces the on-dark one."
      - name: ".ds-site-header-logo"
        does: "On a property that is not arxiv.org, the slot may hold that property’s own wordmark as text; it takes the bar’s emphasis colour."
    notes:
      - "The bar at the top of this page is the light variant, with dropdown groups."
  - id: internal-headers
    title: "Internal header"
    group: "Modifiers"
    summary: "The Admin Console header: the standard bar, with the Admin Console logo. Each internal tool chooses the navigation, tools and wordmark its users need; the regions, their order and the rules stay the same. Every internal tool uses an internal logo, not the public one, so the reader can tell they are in an internal tool. The internal stylesheet may re-point the bar’s colour tokens and nothing else."
    classes:
      - name: ".ds-site-header-logo img"
        does: "The tool’s own wordmark image, from `assets/images/logos/`. Its alt text names the tool in spoken form, such as “archive Admin Console”."
      - name: ".ds-site-header-search"
        does: "A `<form role=\"search\">` holding one `.ds-input` and its label. It stays visible in the bar, because internal tools search constantly. A tool with two kinds of search uses two of these; there is no double-search component. On public pages search stays the Search link beside the navigation, which opens search only when the reader asks."
      - name: ".ds-site-header-tools > button"
        does: "An icon button that acts on the whole tool, such as Refresh or the sidebar toggle. Its name is `.is-sr-only` text. The sidebar toggle has `aria-expanded`, and `aria-controls` naming the sidebar’s `id`."
      - name: ".ds-site-header-greeting"
        does: "The same first-name greeting as the public header, capped at 14 characters."
    notes:
      - "The phone example folds inside a narrower box, as [On small screens](#on-small-screens) describes. Open the menu or the Search button to see the folded rows."
  - id: sticky-header
    title: "Sticky header"
    group: "Modifiers"
    summary: "Internal tools only. Adding `.ds-site-header--sticky` keeps the bar at the top of the viewport while the page scrolls, and the stylesheet sets `scroll-padding-top` on the page so a link to a section does not land under the bar. A page that uses it keeps no other sticky bar. It is not applied to the examples on this page, which already keeps the TOC bar in view."
rules:
  - "A page includes the header from `templates/` and writes the skip link before it, pointing at its own main content. The [templates README](doc.html?src=templates/README.md) says how to install the header, which variables a host sets, and how the stylesheet, scripts and logo are published and cached. [Banner announcements](doc.html?src=templates/BANNER_ANNOUNCEMENTS.md) says how to put up an announcement."
  - "**Regions, in one order.** Logo, Search (public pages), navigation, tools (optional), account. In the transitional header, Log in or Account is the last link in the navigation, and page actions come after it."
  - "**Navigation sits on the right.** The space after the logo stays empty."
  - "**No more than four links in arxiv.org’s navigation.** The logo and Log in do not count (DESIGN-POLICIES). A host does not change the template’s navigation."
  - "**Tools hold what one page or tool needs.** On public pages: this page’s actions, and in the aspirational header the theme control. On internal tools: search fields and icon buttons such as Refresh and the sidebar toggle."
  - "**Public search opens on request; internal search stays in view.** On arxiv.org, Search is a link before the navigation. Internal tools keep their search fields in the tools region."
  - "**Log out.** Today a signed-in reader logs out on the account page. In the aspirational header, Log out is in the Account menu, one menu away on every page."
  - "**The greeting is the first name.** The aspirational header shows the given name only, capped at 14 characters, on public and internal headers."
  - "**Sticky on internal tools only.** arxiv.org’s public header scrolls away (DESIGN-POLICIES)."
  - "**No breadcrumbs.** arXiv’s sitemap is wide and shallow, so the header navigation and the [secondary navigation](navigation.html#secondary-navigation) show the reader’s place."
  - "**Type sizes are rem**, so a reader’s browser font size applies. In print the header keeps only its logo, 28px tall."
  - "**The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content."
  - "**Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page."
  - "**The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish)."
  - "**On arxiv.org nothing in this unit is sticky.** The whole header scrolls away with the page (the one bar a public page may keep in view is the TOC bar — DESIGN-POLICIES). An internal tool that adds `.ds-site-header--sticky` gets `scroll-padding-top` from the stylesheet, so a link to a section does not land under the bar."
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

Rendered directly from `design-system.css`. On a narrow screen the bar folds itself to fit; see [On small screens](#on-small-screens). The header is static — it scrolls away with the page (on arxiv.org the site header is never the sticky bar — DESIGN-POLICIES.md). Every header has the same regions, in this order: logo, Search (public pages), navigation, tools (optional), and account.

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
- `.ds-site-header` — The bar. Bare, it is the arXiv header — arxiv.org cannot forget a class it never has to write.
- `.ds-site-header-logo` — The brand slot, image or wordmark. Takes `margin-right: auto`. On arxiv.org it is the logo image, never the word typed out; its alt text says “archive”.
- `.ds-site-header-search-link` — arxiv.org’s Search: an `<a href="/search">` just before the navigation and outside it, so it stays in the bar when the navigation folds, and search opens from the same place at every width. JS may upgrade it to open the search overlay. Never a dead button — without JS it navigates to the search page. Folded, it shows its icon alone, at the menu button’s size; the word in its `<span>` stays for screen readers.
- `.ds-site-header-nav` — The site’s sections, in a `<nav>` with an `aria-label`.
- `.ds-nav-icon` — An icon beside a link label, sized by the stylesheet and quieter than the text. `aria-hidden="true"`; the label gives the name.
- `.ds-site-header-divider` — A vertical hairline between groups of links or between regions, on the bar’s own divider token. Takes `aria-hidden="true"`. Hidden while the navigation is folded away.
- `.ds-site-header-tools` — Optional. The controls one interface needs, after the navigation. On public pages it holds the theme control; internal tools add search fields and icon buttons. See [Internal header](#internal-headers).
- `.ds-theme-toggle` — The theme control, with its live region `#ds-theme-status`. See [The theme control](dark-mode.html#the-theme-control).
- `.ds-site-header-account` — The last region: Log in, or the greeting and the Account menu. It sits outside the `<nav>`, because an account menu is not a site section. On a phone it folds into the menu with the navigation, as the last rows.
- `.ds-site-header-login` — The emphasis slot, and the only item in the bar that takes weight. Signed out it is the *Log in* link. Signed in it is the *Account* menu, with the greeting beside it.
- `.ds-site-header-dropdown` — A menu group in the bar, built on `<details>`. See [Header dropdown menus](#header-dropdown-menus).
- `.ds-search-overlay` — The search overlay: a `hidden` scrim after the header that the shared chrome’s `header.js` opens from the Search link (or Ctrl/Cmd+K), and closes on Escape, a click on the scrim, or focus moving out of it. Without JS the Search link goes to the search page. Its markup is the transitional header’s.
- `.ds-search-overlay-panel` — The overlay’s panel, hanging from the bottom of the bar at every width. Opening it closes the menu. Its field and hint are the ordinary `.ds-input` and `.ds-hint`.

## Signed in

Account-related items display at the right end of the bar and are the only items in a heavier text weight. Signed out it says **Log in**. Signed in it displays a greeting and name, and an **Account** menu that holds Log out. When names are long (and arXiv users have every type and structure of name) we truncate to a reasonable number of characters.

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

- `.ds-site-header-greeting` — The greeting takes the given name only — its first word — because the bar is chrome and a full legal name is more of it than the job needs. Even one word is user data of unbounded length in any script, so it is capped at 14 characters with an ellipsis, as the Long name example shows. A bar that reflows or overflows on a long name breaks for exactly the people whose names get tested least. The greeting is not a link. It is a statement; the thing you can act on is the Account menu beside it. Making the name itself the link would give that link the accessible name “Ada”, which says nothing about where it goes. It is the first thing dropped on a narrow bar: when the bar runs out of room the greeting hides and Account stays — the menu is the useful half, and the reader already knows their own name.
- `.ds-site-header-greeting > b` — The name. The stylesheet caps it at 14 characters and ends it with an ellipsis; the host passes the given name and nothing else.
- `.ds-site-header-login` — The same emphasis slot as when signed out, now on the `<summary>` of an Account menu (`.ds-site-header-dropdown`). The slot is about rank in the bar, not about which of the two words is in it.
- `<form method="post">` — Log out is a button in a form that posts, never a link. A link can be followed by a browser prefetch or from another site, and logging someone out changes their state.

## On small screens

The header fits itself to the space it has. When the regions do not fit on one row, the greeting goes first, then the navigation folds behind a menu button. On a public bar the tools and the account area fold into the same menu, so the bar keeps the logo, the Search icon and the menu button. An internal bar folds the same way at its last step, with its search fields behind a Search button of their own; see [Internal header](#internal-headers). The transitional header folds its navigation when the window is narrower than 600px.

```html
<!-- Once per page, after the header. Nothing else changes. -->
<script src="header.js" defer></script>
```

- `header.js` — These docs’ fold-by-fit script, `docs/header.js`, once per page. It finds every `.ds-site-header` and keeps each one on a single row, with no breakpoint to choose. Without JavaScript the bar wraps onto more rows instead, so nothing is hidden. The templates load their own script, so a page that uses them adds none.
- `.ds-site-header-nav-toggle, .ds-site-header-tools-toggle` — The menu button, and a second button: Search on a folded internal bar, or Tools on a bar that has tools and no navigation. The script adds each one, so they are not in the markup. Each has `aria-expanded` and `aria-controls`, and Escape closes the open region and returns focus to its button.
- `.is-collapsible, .is-single-menu, .is-greeting-hidden, .is-nav-collapsed, .is-tools-collapsed, .is-menu-open, .is-overfull, .is-open, .is-measuring` — State classes the script sets on the bar and on an open region. They are never written by hand. `.is-single-menu` marks a bar whose menu holds the navigation, the tools and the account area: a public bar once folded, an internal bar at its last fold. `.is-overfull` lets the bar wrap when even the folded bar is too wide for its space.

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
- `.ds-site-header-menu` — The floating panel. Right-anchored, capped to the viewport. A floating panel is a light surface whichever bar summoned it, the same way a popover is. The menu anchors to its trigger’s **right** edge: the nav always sits at the right of the bar, and a left-anchored menu runs off the viewport on the last item — which is every bar’s last item, not an edge case.
- `.ds-panel-label` — Group headings inside a menu use the system-wide label, not a bespoke class.
- `aria-current="page"` — On the menu link for the page the reader is on. The menu shows it in bold, and a screen reader announces it.

## With the announcement band  (Modifiers)

When arXiv has something to say to everyone, an announcement band can be displayed above the header bar. Neither is fixed; the two scroll away together. See [Announcement band](messages.html#announcement-band) for the full documentation.

```html
<a class="ds-skip-link" href="#main">Skip to main content</a>
<div id="ds-announcement"></div>
<header class="ds-site-header">…</header>
```

- `#ds-announcement` — The mount, which the header template writes before the bar. While an announcement is active, `banner.js` draws the band into it; the host writes only the skip link and the include. The band’s parts are on [Special messages](messages.html#announcement-band).

## The light variant  (Modifiers)

Adding `.ds-site-header--light` re-points seven surface tokens but declares no property of its own. It is for pages that comment on arXiv from outside it, such as this documentation. Every page that is part of arXiv, public or internal, uses the standard bar.

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

- `.ds-site-header--light` — Seven token values. No property overrides. The bar is white (`--ds-surface`) with Library Grey links, Repository Brown emphasis, and a Border Light bottom edge; the standard focus ring replaces the on-dark one.
- `.ds-site-header-logo` — On a property that is not arxiv.org, the slot may hold that property’s own wordmark as text; it takes the bar’s emphasis colour.

> The bar at the top of this page is the light variant, with dropdown groups.

## Internal header  (Modifiers)

The Admin Console header: the standard bar, with the Admin Console logo. Each internal tool chooses the navigation, tools and wordmark its users need; the regions, their order and the rules stay the same. Every internal tool uses an internal logo, not the public one, so the reader can tell they are in an internal tool. The internal stylesheet may re-point the bar’s colour tokens and nothing else.

```html
<header class="ds-site-header">
  <a href="/" class="ds-site-header-logo">
    <img src="logo_arxiv-admin-light.svg" alt="archive Admin Console">
  </a>
  <nav class="ds-site-header-nav" aria-label="Admin Console">
    <a href="/resources">Resources</a>
    <a href="/submission">Submission</a>
    <a href="/support">User Support</a>
    <a href="/students">Students</a>
  </nav>
  <span class="ds-site-header-divider" aria-hidden="true"></span>
  <div class="ds-site-header-tools">
    <form class="ds-site-header-search" role="search" action="/users">
      <label class="is-sr-only" for="search-users">Search users</label>
      <input class="ds-input" type="search" id="search-users" name="q" placeholder="Search users">
    </form>
    <form class="ds-site-header-search" role="search" action="/documents">
      <label class="is-sr-only" for="search-docs">Search submissions and documents</label>
      <input class="ds-input" type="search" id="search-docs" name="q" placeholder="Search submissions">
    </form>
    <button type="button">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
        <path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/>
        <path d="M21 3v5h-5"/>
      </svg>
      <span class="is-sr-only">Refresh</span>
    </button>
    <button type="button" aria-expanded="true" aria-controls="sidebar">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
        <rect width="18" height="18" x="3" y="3" rx="2"/>
        <path d="M15 3v18"/>
      </svg>
      <span class="is-sr-only">Sidebar</span>
    </button>
  </div>
  <span class="ds-site-header-divider" aria-hidden="true"></span>
  <div class="ds-site-header-account">
    <span class="ds-site-header-greeting">Welcome <b>Shamsi</b></span>
    <details class="ds-site-header-dropdown">…</details>
  </div>
</header>
```

- `.ds-site-header-logo img` — The tool’s own wordmark image, from `assets/images/logos/`. Its alt text names the tool in spoken form, such as “archive Admin Console”.
- `.ds-site-header-search` — A `<form role="search">` holding one `.ds-input` and its label. It stays visible in the bar, because internal tools search constantly. A tool with two kinds of search uses two of these; there is no double-search component. On public pages search stays the Search link beside the navigation, which opens search only when the reader asks.
- `.ds-site-header-tools > button` — An icon button that acts on the whole tool, such as Refresh or the sidebar toggle. Its name is `.is-sr-only` text. The sidebar toggle has `aria-expanded`, and `aria-controls` naming the sidebar’s `id`.
- `.ds-site-header-greeting` — The same first-name greeting as the public header, capped at 14 characters.

> The phone example folds inside a narrower box, as [On small screens](#on-small-screens) describes. Open the menu or the Search button to see the folded rows.

## Sticky header  (Modifiers)

Internal tools only. Adding `.ds-site-header--sticky` keeps the bar at the top of the viewport while the page scrolls, and the stylesheet sets `scroll-padding-top` on the page so a link to a section does not land under the bar. A page that uses it keeps no other sticky bar. It is not applied to the examples on this page, which already keeps the TOC bar in view.

## Rules

- A page includes the header from `templates/` and writes the skip link before it, pointing at its own main content. The [templates README](doc.html?src=templates/README.md) says how to install the header, which variables a host sets, and how the stylesheet, scripts and logo are published and cached. [Banner announcements](doc.html?src=templates/BANNER_ANNOUNCEMENTS.md) says how to put up an announcement.
- **Regions, in one order.** Logo, Search (public pages), navigation, tools (optional), account. In the transitional header, Log in or Account is the last link in the navigation, and page actions come after it.
- **Navigation sits on the right.** The space after the logo stays empty.
- **No more than four links in arxiv.org’s navigation.** The logo and Log in do not count (DESIGN-POLICIES). A host does not change the template’s navigation.
- **Tools hold what one page or tool needs.** On public pages: this page’s actions, and in the aspirational header the theme control. On internal tools: search fields and icon buttons such as Refresh and the sidebar toggle.
- **Public search opens on request; internal search stays in view.** On arxiv.org, Search is a link before the navigation. Internal tools keep their search fields in the tools region.
- **Log out.** Today a signed-in reader logs out on the account page. In the aspirational header, Log out is in the Account menu, one menu away on every page.
- **The greeting is the first name.** The aspirational header shows the given name only, capped at 14 characters, on public and internal headers.
- **Sticky on internal tools only.** arxiv.org’s public header scrolls away (DESIGN-POLICIES).
- **No breadcrumbs.** arXiv’s sitemap is wide and shallow, so the header navigation and the [secondary navigation](navigation.html#secondary-navigation) show the reader’s place.
- **Type sizes are rem**, so a reader’s browser font size applies. In print the header keeps only its logo, 28px tall.
- **The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content.
- **Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page.
- **The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish).
- **On arxiv.org nothing in this unit is sticky.** The whole header scrolls away with the page (the one bar a public page may keep in view is the TOC bar — DESIGN-POLICIES). An internal tool that adds `.ds-site-header--sticky` gets `scroll-padding-top` from the stylesheet, so a link to a section does not land under the bar.
- **The account area is not navigation.** In the aspirational header it sits outside the `<nav>`, so a screen reader user who lists landmarks finds only site sections there.
- **Name every search field.** A search field in the bar is a `<form role="search">` with a `<label>`, hidden with `.is-sr-only` if needed, that says what it searches. The placeholder is not the name: it disappears as soon as someone types.
- **Mark the current page in the markup.** Put `aria-current="page"` on the current link in the secondary navigation and in header menus.
