---
page: messages.html
title: "Special messages"
summary: "When arXiv has something special to say on the platform itself, this is how we do it. We are starting with a small announcement band above the header. Other options will be added as our communications team finds the need."
stylesheet: design-system.css
components:
  - id: announcement-band
    title: "Announcement band"
    summary: "The announcement band is minimal but gets a lot of attention. Use sparingly to maintain its impact. If it is frequently deployed then our users will get used to it and tune it out. It sits above the site header as part of the header unit (full demo on [the header reference page](header.html)). The dismissal action persists across all repositories, but only for that particular banner. A new banner with a new message should display again for all users even if they dismissed the previous one."
    classes:
      - name: ".ds-announcement"
        does: "The band. Takes `role=\"region\"` and an `aria-label` so a screen reader user can find it and skip it. Goes directly above `.ds-site-header`."
      - name: ".ds-announcement-glyph"
        does: "The icon: an inline SVG from the [icon set](icons.html) with `aria-hidden=\"true\"`, or an `<img>` with an empty `alt` for one of the bones. Either way it is decoration; the sentence carries the meaning."
      - name: ".ds-announcement-text"
        does: "The one sentence."
      - name: ".ds-announcement-link"
        does: "The one link. An `<a>` with a real `href`."
      - name: ".ds-close"
        does: "The dismiss control, last inside the band; the band positions it at the right edge. Remembering the dismissal is the host’s job."
    notes:
      - "Alert vs announcement? An alert belongs to the page’s content and is specific to that user’s journey. The announcement belongs to the site and is for all users."
  - id: suggested-icons
    title: "Icon options"
    group: "Modifiers"
    summary: "Icons are important for conveying meaning quickly and effectively. The small smileybones are drawn for this small use case. Each carries its own colours, so it goes in as an image, not as a true svg icon. No alt text needed, the icon is purely decorative and the text carries the meaning."
  - id: color-variations
    title: "Color variations"
    group: "Modifiers"
    summary: "Open Blue is our default banner color, and should be overridden sparingly. For messages that call for a different treatment, two color variations are available: Black for maintenance and service notices, 'Smileybones yellow' for events."
    classes:
      - name: ".ds-announcement--maintenance"
        does: "For service notices: maintenance windows, outages, deadlines. The band takes the header’s dark ground in both themes, with light text and the light link blue."
      - name: ".ds-announcement--event"
        does: "For milestones and celebrations. The band takes the smileybones yellow in both themes, with fixed brown text; the link is the darker link blue, because the lighter one does not reach 4.5:1 on yellow."
rules:
  - "**Give the band a name.** Keep `role=\"region\"` and `aria-label=\"Announcement\"` on it. That is how a screen reader user finds the band in the page’s landmarks, and how they skip it once they have read it."
  - "**Do not make it a live region.** The band is part of the page as it loads, not a change that happens later. `role=\"alert\"` or `aria-live` would make every page announce it aloud, on every visit, before anything else."
  - "**The sentence carries the meaning.** The icon is hidden from assistive technology (`aria-hidden=\"true\"`, or an empty `alt`), and the band’s colour says nothing on its own. Read the sentence without the icon and the colour; it must still make sense."
  - "**The link is a real link.** An `<a>` with an `href`, so it works with JavaScript off and opens in a new tab if the reader wants. Never a button that navigates."
  - "**Name the dismiss control.** The `.ds-close` button needs its `<span class=\"is-sr-only\">Dismiss announcement</span>`. Do not use `title` or `aria-label` for this; page translation tools skip attributes."
  - "**After a dismiss, focus has somewhere to go.** Removing the band removes the focused button. Move focus to the site header’s first item, so a keyboard user is not dropped back to the top of the document."
  - "**Nothing the page needs lives in the band.** A dismissed band never comes back for that reader, so a link they must be able to find belongs in the page too."
---

# Special messages

When arXiv has something special to say on the platform itself, this is how we do it. We are starting with a small announcement band above the header. Other options will be added as our communications team finds the need.

Load `design-system.css`; internal tools also load `internal-tools.css` and put
`class="ds-internal"` on `<html>`. Every class below is in tier 1 unless it says otherwise.

## Announcement band

The announcement band is minimal but gets a lot of attention. Use sparingly to maintain its impact. If it is frequently deployed then our users will get used to it and tune it out. It sits above the site header as part of the header unit (full demo on [the header reference page](header.html)). The dismissal action persists across all repositories, but only for that particular banner. A new banner with a new message should display again for all users even if they dismissed the previous one.

```html
<div class="ds-announcement" role="region" aria-label="Announcement">
  <svg class="ds-announcement-glyph" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="M3 11h3l9-7v16l-9-7H3z"/>
    <path d="M19 8a5 5 0 0 1 0 8"/>
  </svg>
  <span class="ds-announcement-text">arXiv is now an independent nonprofit.</span>
  <a class="ds-announcement-link" href="#">Learn more</a>
  <button type="button" class="ds-close">
    <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M18 6 6 18"/>
      <path d="m6 6 12 12"/>
    </svg>
    <span class="is-sr-only">Dismiss announcement</span>
  </button>
</div>
```

- `.ds-announcement` — The band. Takes `role="region"` and an `aria-label` so a screen reader user can find it and skip it. Goes directly above `.ds-site-header`.
- `.ds-announcement-glyph` — The icon: an inline SVG from the [icon set](icons.html) with `aria-hidden="true"`, or an `<img>` with an empty `alt` for one of the bones. Either way it is decoration; the sentence carries the meaning.
- `.ds-announcement-text` — The one sentence.
- `.ds-announcement-link` — The one link. An `<a>` with a real `href`.
- `.ds-close` — The dismiss control, last inside the band; the band positions it at the right edge. Remembering the dismissal is the host’s job.

> Alert vs announcement? An alert belongs to the page’s content and is specific to that user’s journey. The announcement belongs to the site and is for all users.

## Icon options  (Modifiers)

Icons are important for conveying meaning quickly and effectively. The small smileybones are drawn for this small use case. Each carries its own colours, so it goes in as an image, not as a true svg icon. No alt text needed, the icon is purely decorative and the text carries the meaning.

```html
<img class="ds-announcement-glyph" src="assets/images/bones/icon_small-smileybones.svg" alt="">
```

```html
<img class="ds-announcement-glyph" src="assets/images/bones/icon_small-infinitybones.svg" alt="">
```

```html
<img class="ds-announcement-glyph" src="assets/images/bones/icon_small-errorbones.svg" alt="">
```

## Color variations  (Modifiers)

Open Blue is our default banner color, and should be overridden sparingly. For messages that call for a different treatment, two color variations are available: Black for maintenance and service notices, 'Smileybones yellow' for events.

```html
<div class="ds-announcement ds-announcement--maintenance" role="region" aria-label="Announcement">
  <img class="ds-announcement-glyph" src="assets/images/bones/icon_small-errorbones.svg" alt="">
  <span class="ds-announcement-text">arXiv will be closed for maintenance on January 1st</span>
  <a class="ds-announcement-link" href="#">Learn more</a>
  <button type="button" class="ds-close">
    <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M18 6 6 18"/>
      <path d="m6 6 12 12"/>
    </svg>
    <span class="is-sr-only">Dismiss announcement</span>
  </button>
</div>
```

```html
<div class="ds-announcement ds-announcement--event" role="region" aria-label="Announcement">
  <img class="ds-announcement-glyph" src="assets/images/bones/icon_small-smileybones.svg" alt="">
  <span class="ds-announcement-text">We are celebrating 35 years of open science!</span>
  <a class="ds-announcement-link" href="#">Join the party</a>
  <button type="button" class="ds-close">
    <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M18 6 6 18"/>
      <path d="m6 6 12 12"/>
    </svg>
    <span class="is-sr-only">Dismiss announcement</span>
  </button>
</div>
```

- `.ds-announcement--maintenance` — For service notices: maintenance windows, outages, deadlines. The band takes the header’s dark ground in both themes, with light text and the light link blue.
- `.ds-announcement--event` — For milestones and celebrations. The band takes the smileybones yellow in both themes, with fixed brown text; the link is the darker link blue, because the lighter one does not reach 4.5:1 on yellow.

## Rules

- **Give the band a name.** Keep `role="region"` and `aria-label="Announcement"` on it. That is how a screen reader user finds the band in the page’s landmarks, and how they skip it once they have read it.
- **Do not make it a live region.** The band is part of the page as it loads, not a change that happens later. `role="alert"` or `aria-live` would make every page announce it aloud, on every visit, before anything else.
- **The sentence carries the meaning.** The icon is hidden from assistive technology (`aria-hidden="true"`, or an empty `alt`), and the band’s colour says nothing on its own. Read the sentence without the icon and the colour; it must still make sense.
- **The link is a real link.** An `<a>` with an `href`, so it works with JavaScript off and opens in a new tab if the reader wants. Never a button that navigates.
- **Name the dismiss control.** The `.ds-close` button needs its `<span class="is-sr-only">Dismiss announcement</span>`. Do not use `title` or `aria-label` for this; page translation tools skip attributes.
- **After a dismiss, focus has somewhere to go.** Removing the band removes the focused button. Move focus to the site header’s first item, so a keyboard user is not dropped back to the top of the document.
- **Nothing the page needs lives in the band.** A dismissed band never comes back for that reader, so a link they must be able to find belongs in the page too.
