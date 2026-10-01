# Banner announcements

[`assets/json/announcements.json`](assets/json/announcements.json) is the banner above the
header on every arXiv page. Edit it and merge to `master`: the dev route publishes at once,
prod on the manual run, and readers see the change within five minutes.

```json
{
  "announcements": [
    {
      "id": "2026-08-maintenance",
      "text": "System maintenance August 4th and 5th",
      "link_text": "Learn more",
      "url": "https://status.arxiv.org",
      "start": "2026-08-03T00:00-04:00",
      "end": "2026-08-06T00:00-04:00"
    }
  ]
}
```

| Field | | |
|---|---|---|
| `id` | required | Names the entry for dismissal (below). |
| `text` | required | One short sentence, plain text (markup shows as typed). |
| `start`, `end` | required | ISO 8601 with the offset (`-04:00`, `Z`); shown from `start` to `end`. |
| `link_text`, `url` | optional, together | One link; `url` is an absolute `https://` URL, any host. |

- **Order:** newest first, so add a new entry at the top. When entries overlap, the latest
  `start` shows (a short notice over a long campaign). Expired entries never show and may stay.
- **Dismissal** holds on every arXiv site (a cookie on the parent domain), for that `id` and
  message, until 30 days after `end`, so an extended `end` stays dismissed. Editing `text`,
  `link_text` or `url` shows the entry again to everyone.
- **Checks:** CI refuses a file that breaks these rules; run
  `python3 -m unittest discover -s templates/tests` to check locally.

## Why it works this way

- **Data, not page markup.** `chrome/banner.js` fetches the file from the asset route (cached
  five minutes). An announcement therefore changes no page, and pages cached for a year
  (browse's abs pages) need no purge.
- **The script draws the band.** This is the one recorded exception to "scripts never carry
  content" (DESIGN-POLICIES, Banner): an announcement is temporal and never page-critical, so a
  reader without JavaScript sees none.
- **Plain text and one link:**
  - no HTML, which would need a sanitizer on every page for markup the Banner policy excludes;
  - no images: acknowledgements belong in the footer, and an off-site image would let a third
    party observe every page view.

  Nearly all of browse's banners since 2018 fit this form as one sentence. The exceptions
  were an interactive consent form and a per-reader link.
- **One shared file.** A per-host announcement would live in the page, so every change would
  mean purging cached pages. Per-app banner macros retire as their apps move to the templates.
- **No iframe.** Without a script, a frame can neither fit its text nor collapse when nothing
  is live. Dismissal and the time window need a script anyway, and screen readers would get a
  nested document.
- **The file lives here for now,** not in its own repository. The URL is `banner.js`'s, so
  the file can move without a page changing.
