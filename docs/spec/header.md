---
page: header.html
title: "Site header"
summary: "The arXiv public-page header sets the tone for the entire platform: simple, straightforward, and utilitarian. It consists of a dark band with logo on the left, and navigation, search, and account links on the right. An optional, dismissible announcement banner can be displayed above the header. Absolute consistency across all pages is critical. Internal pages have their own header and variations, see [Internal header](#internal-headers) for an example."
stylesheet: design-system.css
components:
  - id: the-header-unit
    title: "The header unit"
    summary: "Rendered directly from `design-system.css`. Resize the window: at ≤599px the nav collapses behind the hamburger (the approved mobile treatment); **without JS it wraps to a second row instead** — every item stays visible, passing WCAG 1.4.10 reflow at 320px and keeping voice-control working. The header is static — it scrolls away with the page (on arxiv.org the site header is never the sticky bar — DESIGN-POLICIES.md). Every header has the same regions, in this order: logo, navigation, tools (optional), and account."
    classes:
      - name: ".ds-skip-link"
        does: "The skip link. The first focusable element on the page, visible only on keyboard focus. Its `href` is the id of the main content."
      - name: ".ds-site-header"
        does: "The bar. Bare, it is the arXiv header — arxiv.org cannot forget a class it never has to write."
      - name: ".ds-site-header-logo"
        does: "The brand slot, image or wordmark. Takes `margin-right: auto`. On arxiv.org it is the logo image, never the word typed out; its alt text says “archive”."
      - name: ".ds-site-header-nav"
        does: "The links, in a `<nav>` with an `aria-label`. The Search control is an `<a href=\"/search\">` that JS may upgrade to open a search overlay. Never a dead button — without JS it navigates to the search page."
      - name: ".ds-nav-icon"
        does: "An icon beside a link label, sized by the stylesheet and quieter than the text. `aria-hidden=\"true\"`; the label carries the name."
      - name: ".ds-site-header-divider"
        does: "A vertical hairline between groups of links or between regions, on the bar’s own divider token. Takes `aria-hidden=\"true\"`. Hidden below 600px."
      - name: ".ds-site-header-tools"
        does: "Optional. The controls one interface needs, after the navigation: search fields, icon buttons, the theme control. See [Internal header](#internal-headers)."
      - name: ".ds-site-header-account"
        does: "The last region: Log in, or the greeting and the Account menu. It sits outside the `<nav>`, because an account menu is not a site section. Below 600px it stays on the first row, beside the logo."
      - name: ".ds-site-header-login"
        does: "The emphasis slot, and the only item in the bar that takes weight. Signed out it is the *Log in* link. Signed in it is the *Account* menu, with the greeting beside it."
      - name: ".ds-site-header-nav-toggle, .is-collapsible, .is-open"
        does: "At ≤599px the nav collapses behind a hamburger **only after JS enables it**: the header script adds `.is-collapsible` to `.ds-site-header` and wires the toggle (`.is-open` on the nav, `aria-expanded` in sync) in the same call, so the hamburger appears only when it actually works. **The default — including no JS — is the wrap** (all items visible, WCAG 1.4.10 reflow)."
      - name: ".ds-site-header-dropdown"
        does: "A menu group in the bar, built on `<details>`. See [Header dropdown menus](#header-dropdown-menus)."
  - id: signed-out-and-signed-in
    title: "Signed out and signed in"
    summary: "Account-related items display to the right of the navigation and are the only items in a heavier text weight. Signed out it says **Log in**. Signed in it displays a greeting and name, and an **Account** menu that holds Log out. When names are long (and arXiv users have every type and structure of name) we truncate to a reasonable number of characters."
    classes:
      - name: ".ds-site-header-greeting"
        does: "The greeting takes the given name only — its first word — because the bar is chrome and a full legal name is more of it than the job needs. Even one word is user data of unbounded length in any script, so it is capped at 14 characters with an ellipsis, as the second example shows. A bar that reflows or overflows on a long name breaks for exactly the people whose names get tested least. The greeting is not a link. It is a statement; the thing you can act on is the Account menu beside it. Making the name itself the link would give that link the accessible name “Ada”, which says nothing about where it goes. It is the first thing dropped on a narrow bar: below 600px the greeting hides and Account stays — the menu is the useful half, and the reader already knows their own name."
      - name: ".ds-site-header-login"
        does: "The same emphasis slot as when signed out, now on the `<summary>` of an Account menu (`.ds-site-header-dropdown`). The slot is about rank in the bar, not about which of the two words is in it."
      - name: "<form method=\"post\">"
        does: "Log out is a button in a form that posts, never a link. A link can be followed by a browser prefetch or from another site, and logging someone out changes their state."
      - name: ".ds-site-header-greeting > b"
        does: "The name. The stylesheet caps it at 14 characters and ends it with an ellipsis; the host passes the given name and nothing else."
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
  - id: secondary-navigation
    title: "Secondary navigation"
    summary: "A row of section links directly under the header, for an area that has its own sections, such as the account pages. It wraps onto a second line rather than scrolling sideways, so every section stays visible on a phone and at high zoom."
    classes:
      - name: ".ds-subnav"
        does: "A `<nav>` directly after the header, with an `aria-label` that names the area, such as “Account sections”. Plain links; never `role=\"tab\"`, which would promise arrow-key behaviour that page links do not have. Hidden in print."
      - name: "aria-current=\"page\""
        does: "On the link for the current page. It shows in bold with an underline bar, so the current section never depends on colour alone, and a screen reader announces it."
      - name: ".ds-internal"
        does: "On a parent, it turns the underline bar Access Lime Deep. Nothing else changes."
  - id: with-the-announcement-band
    title: "With the announcement band"
    group: "Modifiers"
    summary: "When arXiv has something to say to everyone, an announcement band can be displayed above the header bar. Neither is fixed; the two scroll away together. See [Announcement band](messages.html#announcement-band) for the full documentation."
    classes:
      - name: ".ds-announcement"
        does: "The band, placed before `.ds-site-header` and after the skip link. See [Special messages](messages.html#announcement-band) for its parts."
  - id: the-light-variant
    title: "The light variant"
    group: "Modifiers"
    summary: "Adding `.ds-site-header--light` re-points seven surface tokens but declares no property of its own. The light variant is used in this documentation to clearly signal we are in a distinct space from the main arXiv site."
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
    summary: "The Admin Console header, built from the same component on the light variant. Each internal tool chooses the navigation, tools and wordmark its users need; the regions, their order and the rules stay the same. The internal stylesheet may re-point the bar’s colour tokens and nothing else."
    classes:
      - name: ".ds-site-header-logo img"
        does: "The tool’s own wordmark image, from `assets/images/logos/`. Its alt text names the tool in spoken form, such as “archive Admin Console”."
      - name: ".ds-site-header-search"
        does: "A `<form role=\"search\">` holding one `.ds-input` and its label. It stays visible in the bar, because internal tools search constantly. A tool with two kinds of search uses two of these; there is no double-search component. On public pages search stays the Search link in the navigation, which opens search only when the reader asks."
      - name: ".ds-site-header-tools > button"
        does: "An icon button that acts on the whole tool, such as Refresh or the sidebar toggle. Its name is `.is-sr-only` text. The sidebar toggle carries `aria-expanded`, and `aria-controls` naming the sidebar’s `id`."
      - name: ".ds-site-header-greeting"
        does: "The same first-name greeting as the public header, capped at 14 characters."
  - id: sticky-header
    title: "Sticky header"
    group: "Modifiers"
    summary: "Internal tools only. Adding `.ds-site-header--sticky` keeps the bar at the top of the viewport while the page scrolls, and the stylesheet sets `scroll-padding-top` on the page so a link to a section does not land under the bar. It is not applied to the examples on this page, which already keeps the TOC bar in view."
    classes:
      - name: ".ds-site-header--sticky"
        does: "Sticks the bar to the top of the viewport. A page that uses it keeps no other sticky bar."
rules:
  - "**The announcement is temporal.** Render only while active, persist dismissal in production, and never attach page-critical function to it."
  - "**No more than four top-level links.** The logo and Log in do not count. More than four causes cognitive overload and reduces comprehension; resist link-creep permanently (DESIGN-POLICIES)."
  - "**Log out is in the Account menu.** Signed in, Account opens a menu holding the account page and Log out. Logging out is then one menu away on every page, which matters on shared computers, and still takes two deliberate actions."
  - "**Regions, in one order.** Logo, navigation, tools (optional), account. Every header on every surface keeps this order."
  - "**Navigation sits on the right.** On every header, the space after the logo stays empty and the navigation follows it."
  - "**Tools hold what one interface needs.** Search fields, icon buttons such as Refresh and the sidebar toggle, and the theme control go in the tools region."
  - "**Public search opens on request; internal search stays in view.** On arxiv.org, Search is a link in the navigation. Internal tools keep their search fields in the tools region."
  - "**Sticky on internal tools only.** `.ds-site-header--sticky` is for internal tools; arxiv.org’s public header scrolls away (DESIGN-POLICIES)."
  - "**The greeting is the first name, everywhere.** Public and internal headers show the given name only, capped at 14 characters."
  - "**Breadcrumbs only on pages without secondary navigation.** arXiv’s sitemap is wide and shallow, so almost no page needs a breadcrumb. Where the secondary navigation shows the reader’s place, a breadcrumb would repeat it."
  - "**Type sizes are rem** so browser font-size overrides propagate; the header, the announcement band and the secondary navigation are hidden in print."
  - "**The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content."
  - "**Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page."
  - "**The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish)."
  - "**On arxiv.org nothing in this unit is sticky.** The whole header scrolls away with the page (the one bar a public page may keep in view is the TOC bar — DESIGN-POLICIES). An internal tool that adds `.ds-site-header--sticky` gets `scroll-padding-top` from the stylesheet, so a link to a section does not land under the bar."
  - "**The account area is not navigation.** It sits outside the `<nav>`, so a screen reader user who lists landmarks finds only site sections there."
  - "**Name every search field.** A search field in the bar is a `<form role=\"search\">` with a `<label>`, hidden with `.is-sr-only` if needed, that says what it searches. The placeholder is not the name: it disappears as soon as someone types."
  - "**Mark the current page in the markup.** Put `aria-current=\"page\"` on the current link in the secondary navigation and in header menus."
---

# Site header

The arXiv public-page header sets the tone for the entire platform: simple, straightforward, and utilitarian. It consists of a dark band with logo on the left, and navigation, search, and account links on the right. An optional, dismissible announcement banner can be displayed above the header. Absolute consistency across all pages is critical. Internal pages have their own header and variations, see [Internal header](#internal-headers) for an example.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The header unit

Rendered directly from `design-system.css`. Resize the window: at ≤599px the nav collapses behind the hamburger (the approved mobile treatment); **without JS it wraps to a second row instead** — every item stays visible, passing WCAG 1.4.10 reflow at 320px and keeping voice-control working. The header is static — it scrolls away with the page (on arxiv.org the site header is never the sticky bar — DESIGN-POLICIES.md). Every header has the same regions, in this order: logo, navigation, tools (optional), and account.

```html
<!-- First focusable element on the page -->
<a class="ds-skip-link" href="#main">Skip to main content</a>

<header class="ds-site-header">
  <a href="/" class="ds-site-header-logo" aria-label="archive home">
    <img src="logo_arxiv-primary.svg" alt="archive">
  </a>
  <button type="button" id="ds-nav-toggle" class="ds-site-header-nav-toggle" aria-label="Open menu" aria-controls="ds-site-header-nav" aria-expanded="false">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
      <line x1="3" y1="6" x2="21" y2="6"/>
      <line x1="3" y1="12" x2="21" y2="12"/>
      <line x1="3" y1="18" x2="21" y2="18"/>
    </svg>
  </button>
  <nav class="ds-site-header-nav" id="ds-site-header-nav" aria-label="Main navigation">
    <a href="/search">
      <svg class="ds-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
        <circle cx="11" cy="11" r="8"/>
        <line x1="21" y1="21" x2="16.65" y2="16.65"/>
      </svg>
      Search
    </a>
    <a href="/submit">Submit</a>
    <a href="/about/donate">Donate</a>
  </nav>
  <span class="ds-site-header-divider" aria-hidden="true"></span>
  <div class="ds-site-header-account">
    <a href="/login" class="ds-site-header-login">Log in</a>
  </div>
</header>
```

- `.ds-skip-link` — The skip link. The first focusable element on the page, visible only on keyboard focus. Its `href` is the id of the main content.
- `.ds-site-header` — The bar. Bare, it is the arXiv header — arxiv.org cannot forget a class it never has to write.
- `.ds-site-header-logo` — The brand slot, image or wordmark. Takes `margin-right: auto`. On arxiv.org it is the logo image, never the word typed out; its alt text says “archive”.
- `.ds-site-header-nav` — The links, in a `<nav>` with an `aria-label`. The Search control is an `<a href="/search">` that JS may upgrade to open a search overlay. Never a dead button — without JS it navigates to the search page.
- `.ds-nav-icon` — An icon beside a link label, sized by the stylesheet and quieter than the text. `aria-hidden="true"`; the label carries the name.
- `.ds-site-header-divider` — A vertical hairline between groups of links or between regions, on the bar’s own divider token. Takes `aria-hidden="true"`. Hidden below 600px.
- `.ds-site-header-tools` — Optional. The controls one interface needs, after the navigation: search fields, icon buttons, the theme control. See [Internal header](#internal-headers).
- `.ds-site-header-account` — The last region: Log in, or the greeting and the Account menu. It sits outside the `<nav>`, because an account menu is not a site section. Below 600px it stays on the first row, beside the logo.
- `.ds-site-header-login` — The emphasis slot, and the only item in the bar that takes weight. Signed out it is the *Log in* link. Signed in it is the *Account* menu, with the greeting beside it.
- `.ds-site-header-nav-toggle, .is-collapsible, .is-open` — At ≤599px the nav collapses behind a hamburger **only after JS enables it**: the header script adds `.is-collapsible` to `.ds-site-header` and wires the toggle (`.is-open` on the nav, `aria-expanded` in sync) in the same call, so the hamburger appears only when it actually works. **The default — including no JS — is the wrap** (all items visible, WCAG 1.4.10 reflow).
- `.ds-site-header-dropdown` — A menu group in the bar, built on `<details>`. See [Header dropdown menus](#header-dropdown-menus).

## Signed out and signed in

Account-related items display to the right of the navigation and are the only items in a heavier text weight. Signed out it says **Log in**. Signed in it displays a greeting and name, and an **Account** menu that holds Log out. When names are long (and arXiv users have every type and structure of name) we truncate to a reasonable number of characters.

```html
<nav class="ds-site-header-nav" aria-label="Main navigation">
  <a href="/search">
    <svg class="ds-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
      <circle cx="11" cy="11" r="8"/>
      <line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    Search
  </a>
  <a href="/submit">Submit</a>
</nav>
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

```html
<span class="ds-site-header-greeting">Welcome <b>Sivaramakrishnan</b></span>
```

- `.ds-site-header-greeting` — The greeting takes the given name only — its first word — because the bar is chrome and a full legal name is more of it than the job needs. Even one word is user data of unbounded length in any script, so it is capped at 14 characters with an ellipsis, as the second example shows. A bar that reflows or overflows on a long name breaks for exactly the people whose names get tested least. The greeting is not a link. It is a statement; the thing you can act on is the Account menu beside it. Making the name itself the link would give that link the accessible name “Ada”, which says nothing about where it goes. It is the first thing dropped on a narrow bar: below 600px the greeting hides and Account stays — the menu is the useful half, and the reader already knows their own name.
- `.ds-site-header-login` — The same emphasis slot as when signed out, now on the `<summary>` of an Account menu (`.ds-site-header-dropdown`). The slot is about rank in the bar, not about which of the two words is in it.
- `<form method="post">` — Log out is a button in a form that posts, never a link. A link can be followed by a browser prefetch or from another site, and logging someone out changes their state.
- `.ds-site-header-greeting > b` — The name. The stylesheet caps it at 14 characters and ends it with an ellipsis; the host passes the given name and nothing else.

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

## Secondary navigation

A row of section links directly under the header, for an area that has its own sections, such as the account pages. It wraps onto a second line rather than scrolling sideways, so every section stays visible on a phone and at high zoom.

```html
<header class="ds-site-header">…</header>
<nav class="ds-subnav" aria-label="Account sections">
  <a href="/account">Account home</a>
  <a href="/account/submissions">Submissions</a>
  <a href="/account/works" aria-current="page">Works you own</a>
  <a href="/account/endorse">Endorse</a>
</nav>
```

- `.ds-subnav` — A `<nav>` directly after the header, with an `aria-label` that names the area, such as “Account sections”. Plain links; never `role="tab"`, which would promise arrow-key behaviour that page links do not have. Hidden in print.
- `aria-current="page"` — On the link for the current page. It shows in bold with an underline bar, so the current section never depends on colour alone, and a screen reader announces it.
- `.ds-internal` — On a parent, it turns the underline bar Access Lime Deep. Nothing else changes.

## With the announcement band  (Modifiers)

When arXiv has something to say to everyone, an announcement band can be displayed above the header bar. Neither is fixed; the two scroll away together. See [Announcement band](messages.html#announcement-band) for the full documentation.

```html
<a class="ds-skip-link" href="#main">Skip to main content</a>

<div class="ds-announcement" role="region" aria-label="Announcement">
  <img class="ds-announcement-glyph" src="icon_small-smileybones.svg" alt="">
  <span class="ds-announcement-text">arXiv is now an independent nonprofit!</span>
  <a class="ds-announcement-link" href="/about">Learn more</a>
  <button type="button" class="ds-close">
    <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M18 6 6 18"/>
      <path d="m6 6 12 12"/>
    </svg>
    <span class="is-sr-only">Dismiss announcement</span>
  </button>
</div>

<header class="ds-site-header">…</header>
```

- `.ds-announcement` — The band, placed before `.ds-site-header` and after the skip link. See [Special messages](messages.html#announcement-band) for its parts.

## The light variant  (Modifiers)

Adding `.ds-site-header--light` re-points seven surface tokens but declares no property of its own. The light variant is used in this documentation to clearly signal we are in a distinct space from the main arXiv site.

```html
<nav class="ds-site-header ds-site-header--light" aria-label="Design system">
  <a href="/" class="ds-site-header-logo">arXiv Design System</a>
  <nav class="ds-site-header-nav" aria-label="Site navigation">
    <a href="/patterns">Patterns</a>
    <a href="/mockups">Mockups</a>
    <a href="/docs">Docs</a>
  </nav>
</nav>
```

- `.ds-site-header--light` — Seven token values. No property overrides. The bar is white (`--ds-surface`) with Library Grey links, Repository Brown emphasis, and a Border Light bottom edge; the standard focus ring replaces the on-dark one.
- `.ds-site-header-logo` — On a property that is not arxiv.org, the slot may hold that property’s own wordmark as text; it takes the bar’s emphasis colour.

> The bar at the top of this page is the light variant, with dropdown groups.

## Internal header  (Modifiers)

The Admin Console header, built from the same component on the light variant. Each internal tool chooses the navigation, tools and wordmark its users need; the regions, their order and the rules stay the same. The internal stylesheet may re-point the bar’s colour tokens and nothing else.

```html
<header class="ds-site-header ds-site-header--light">
  <a href="/" class="ds-site-header-logo">
    <img src="logo_arxiv-admin.png" alt="archive Admin Console">
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
- `.ds-site-header-search` — A `<form role="search">` holding one `.ds-input` and its label. It stays visible in the bar, because internal tools search constantly. A tool with two kinds of search uses two of these; there is no double-search component. On public pages search stays the Search link in the navigation, which opens search only when the reader asks.
- `.ds-site-header-tools > button` — An icon button that acts on the whole tool, such as Refresh or the sidebar toggle. Its name is `.is-sr-only` text. The sidebar toggle carries `aria-expanded`, and `aria-controls` naming the sidebar’s `id`.
- `.ds-site-header-greeting` — The same first-name greeting as the public header, capped at 14 characters.

## Sticky header  (Modifiers)

Internal tools only. Adding `.ds-site-header--sticky` keeps the bar at the top of the viewport while the page scrolls, and the stylesheet sets `scroll-padding-top` on the page so a link to a section does not land under the bar. It is not applied to the examples on this page, which already keeps the TOC bar in view.

```html
<header class="ds-site-header ds-site-header--light ds-site-header--sticky">…</header>
```

- `.ds-site-header--sticky` — Sticks the bar to the top of the viewport. A page that uses it keeps no other sticky bar.

## Rules

- **The announcement is temporal.** Render only while active, persist dismissal in production, and never attach page-critical function to it.
- **No more than four top-level links.** The logo and Log in do not count. More than four causes cognitive overload and reduces comprehension; resist link-creep permanently (DESIGN-POLICIES).
- **Log out is in the Account menu.** Signed in, Account opens a menu holding the account page and Log out. Logging out is then one menu away on every page, which matters on shared computers, and still takes two deliberate actions.
- **Regions, in one order.** Logo, navigation, tools (optional), account. Every header on every surface keeps this order.
- **Navigation sits on the right.** On every header, the space after the logo stays empty and the navigation follows it.
- **Tools hold what one interface needs.** Search fields, icon buttons such as Refresh and the sidebar toggle, and the theme control go in the tools region.
- **Public search opens on request; internal search stays in view.** On arxiv.org, Search is a link in the navigation. Internal tools keep their search fields in the tools region.
- **Sticky on internal tools only.** `.ds-site-header--sticky` is for internal tools; arxiv.org’s public header scrolls away (DESIGN-POLICIES).
- **The greeting is the first name, everywhere.** Public and internal headers show the given name only, capped at 14 characters.
- **Breadcrumbs only on pages without secondary navigation.** arXiv’s sitemap is wide and shallow, so almost no page needs a breadcrumb. Where the secondary navigation shows the reader’s place, a breadcrumb would repeat it.
- **Type sizes are rem** so browser font-size overrides propagate; the header, the announcement band and the secondary navigation are hidden in print.
- **The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content.
- **Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page.
- **The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish).
- **On arxiv.org nothing in this unit is sticky.** The whole header scrolls away with the page (the one bar a public page may keep in view is the TOC bar — DESIGN-POLICIES). An internal tool that adds `.ds-site-header--sticky` gets `scroll-padding-top` from the stylesheet, so a link to a section does not land under the bar.
- **The account area is not navigation.** It sits outside the `<nav>`, so a screen reader user who lists landmarks finds only site sections there.
- **Name every search field.** A search field in the bar is a `<form role="search">` with a `<label>`, hidden with `.is-sr-only` if needed, that says what it searches. The placeholder is not the name: it disappears as soon as someone types.
- **Mark the current page in the markup.** Put `aria-current="page"` on the current link in the secondary navigation and in header menus.
