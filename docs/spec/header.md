---
page: header.html
title: "Site header"
summary: "The arXiv public-page header sets the tone for the entire platform: simple, straightforward, and utilitarian. It consists of a dark band with logo on the left, and navigation, search, and account links on the right. An optional, dismissible announcement banner can be displayed above the header. Absolute consistency across all pages is critical. Internal pages have their own header and variations, see [Modifiers](#modifiers) for examples."
stylesheet: design-system.css
components:
  - id: the-header-unit
    title: "The header unit"
    summary: "Rendered directly from `design-system.css`. Resize the window: at ≤599px the nav collapses behind the hamburger (the approved mobile treatment); **without JS it wraps to a second row instead** — every item stays visible, passing WCAG 1.4.10 reflow at 320px and keeping voice-control working. The header is static — it scrolls away with the page (the site header is never the sticky bar — DESIGN-POLICIES.md)."
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
        does: "A vertical hairline between groups of links, on the bar’s own divider token. Takes `aria-hidden=\"true\"`."
      - name: ".ds-site-header-login"
        does: "The emphasis slot: the last item in the bar, and the only nav item that takes weight. Signed out it is the *Log in* link. Signed in it is the *Account* menu, with the greeting beside it."
      - name: ".ds-site-header-nav-toggle, .is-collapsible, .is-open"
        does: "At ≤599px the nav collapses behind a hamburger **only after JS enables it**: the header script adds `.is-collapsible` to `.ds-site-header` and wires the toggle (`.is-open` on the nav, `aria-expanded` in sync) in the same call, so the hamburger appears only when it actually works. **The default — including no JS — is the wrap** (all items visible, WCAG 1.4.10 reflow)."
      - name: ".ds-site-header-dropdown"
        does: "A menu group in the bar, built on `<details>`; it is documented with the other disclosures on [Progressive disclosure](progressive-disclosure.html#header-dropdown-menus)."
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
  - id: with-the-announcement-band
    title: "With the announcement band"
    summary: "When arXiv has something to say to everyone, an announcement band can be displayed above the header bar. Neither is fixed; the two scroll away together. See [Announcement band](messages.html#announcement-band) for the full documentation."
    classes:
      - name: ".ds-announcement"
        does: "The band, placed before `.ds-site-header` and after the skip link. See [Special messages](messages.html#announcement-band) for its parts."
  - id: the-light-variant
    title: "The light variant"
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
    summary: ""
rules:
  - "**The announcement is temporal.** Render only while active, persist dismissal in production, and never attach page-critical function to it."
  - "**No more than four top-level links.** The logo and Log in do not count. More than four causes cognitive overload and reduces comprehension; resist link-creep permanently (DESIGN-POLICIES)."
  - "**Log out is in the Account menu.** Signed in, Account opens a menu holding the account page and Log out. Logging out is then one menu away on every page, which matters on shared computers, and still takes two deliberate actions."
  - "**Type sizes are rem** so browser font-size overrides propagate; both bands are hidden in print."
  - "**The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content."
  - "**Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page."
  - "**The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish)."
  - "**Nothing in this unit is sticky.** The whole header scrolls away with the page (the one bar a page may keep in view is the contents bar — DESIGN-POLICIES). No `scroll-padding` duty applies."
---

# Site header

The arXiv public-page header sets the tone for the entire platform: simple, straightforward, and utilitarian. It consists of a dark band with logo on the left, and navigation, search, and account links on the right. An optional, dismissible announcement banner can be displayed above the header. Absolute consistency across all pages is critical. Internal pages have their own header and variations, see [Modifiers](#modifiers) for examples.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## The header unit

Rendered directly from `design-system.css`. Resize the window: at ≤599px the nav collapses behind the hamburger (the approved mobile treatment); **without JS it wraps to a second row instead** — every item stays visible, passing WCAG 1.4.10 reflow at 320px and keeping voice-control working. The header is static — it scrolls away with the page (the site header is never the sticky bar — DESIGN-POLICIES.md).

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
    <span class="ds-site-header-divider" aria-hidden="true"></span>
    <a href="/login" class="ds-site-header-login">Log in</a>
  </nav>
</header>
```

- `.ds-skip-link` — The skip link. The first focusable element on the page, visible only on keyboard focus. Its `href` is the id of the main content.
- `.ds-site-header` — The bar. Bare, it is the arXiv header — arxiv.org cannot forget a class it never has to write.
- `.ds-site-header-logo` — The brand slot, image or wordmark. Takes `margin-right: auto`. On arxiv.org it is the logo image, never the word typed out; its alt text says “archive”.
- `.ds-site-header-nav` — The links, in a `<nav>` with an `aria-label`. The Search control is an `<a href="/search">` that JS may upgrade to open a search overlay. Never a dead button — without JS it navigates to the search page.
- `.ds-nav-icon` — An icon beside a link label, sized by the stylesheet and quieter than the text. `aria-hidden="true"`; the label carries the name.
- `.ds-site-header-divider` — A vertical hairline between groups of links, on the bar’s own divider token. Takes `aria-hidden="true"`.
- `.ds-site-header-login` — The emphasis slot: the last item in the bar, and the only nav item that takes weight. Signed out it is the *Log in* link. Signed in it is the *Account* menu, with the greeting beside it.
- `.ds-site-header-nav-toggle, .is-collapsible, .is-open` — At ≤599px the nav collapses behind a hamburger **only after JS enables it**: the header script adds `.is-collapsible` to `.ds-site-header` and wires the toggle (`.is-open` on the nav, `aria-expanded` in sync) in the same call, so the hamburger appears only when it actually works. **The default — including no JS — is the wrap** (all items visible, WCAG 1.4.10 reflow).
- `.ds-site-header-dropdown` — A menu group in the bar, built on `<details>`; it is documented with the other disclosures on [Progressive disclosure](progressive-disclosure.html#header-dropdown-menus).

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
  <span class="ds-site-header-divider" aria-hidden="true"></span>
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
</nav>
```

```html
<span class="ds-site-header-greeting">Welcome <b>Sivaramakrishnan</b></span>
```

- `.ds-site-header-greeting` — The greeting takes the given name only — its first word — because the bar is chrome and a full legal name is more of it than the job needs. Even one word is user data of unbounded length in any script, so it is capped at 14 characters with an ellipsis, as the second example shows. A bar that reflows or overflows on a long name breaks for exactly the people whose names get tested least. The greeting is not a link. It is a statement; the thing you can act on is the Account menu beside it. Making the name itself the link would give that link the accessible name “Ada”, which says nothing about where it goes. It is the first thing dropped on a narrow bar: below 600px the greeting hides and Account stays — the menu is the useful half, and the reader already knows their own name.
- `.ds-site-header-login` — The same emphasis slot as when signed out, now on the `<summary>` of an Account menu (`.ds-site-header-dropdown`). The slot is about rank in the bar, not about which of the two words is in it.
- `<form method="post">` — Log out is a button in a form that posts, never a link. A link can be followed by a browser prefetch or from another site, and logging someone out changes their state.
- `.ds-site-header-greeting > b` — The name. The stylesheet caps it at 14 characters and ends it with an ellipsis; the host passes the given name and nothing else.

## With the announcement band

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

## The light variant

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



## Rules

- **The announcement is temporal.** Render only while active, persist dismissal in production, and never attach page-critical function to it.
- **No more than four top-level links.** The logo and Log in do not count. More than four causes cognitive overload and reduces comprehension; resist link-creep permanently (DESIGN-POLICIES).
- **Log out is in the Account menu.** Signed in, Account opens a menu holding the account page and Log out. Logging out is then one menu away on every page, which matters on shared computers, and still takes two deliberate actions.
- **Type sizes are rem** so browser font-size overrides propagate; both bands are hidden in print.
- **The skip link comes first.** `.ds-skip-link` is the first focusable element on the page, visible only on keyboard focus, and it goes to the main content.
- **Name the navigation.** The bar’s links sit in a `<nav>` with an `aria-label`, such as “Main navigation”, so a screen reader user can tell it from the other landmarks on the page.
- **The wordmark is an image with alt text.** Logo alt text and aria-labels say “archive” — the spoken form of “arXiv” (screen readers otherwise produce “ar-zhiv” or Roman-numeral gibberish).
- **Nothing in this unit is sticky.** The whole header scrolls away with the page (the one bar a page may keep in view is the contents bar — DESIGN-POLICIES). No `scroll-padding` duty applies.
