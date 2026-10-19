# Banner announcements

The banner is the band above the header on every arXiv page built from these templates. What it
says comes from one shared file, [`assets/json/announcements.json`](assets/json/announcements.json):
an entry there shows on every one of those sites at once, from its start to its end, until a
reader dismisses it. How the band looks, and how to word an announcement:
[Special messages](https://arxiv.github.io/design-system/docs/messages.html#announcement-band).

## Put up an announcement

1. **Write it:** one sentence that says what is happening and when, and a short link or two to
   where the reader finds the rest. The band is seen by everyone, so use it sparingly.
2. **Add an entry** at the top of `announcements.json` on a branch, and check the file:
   `python3 -m unittest discover -s templates/tests`.
3. **Preview it:** `python3 templates/tests/integration/app.py` (needs Flask) serves a page with
   the band from your copy of the file at <http://127.0.0.1:5001/jinja>. Like every page, it
   shows only an entry whose window includes now.
4. **Open a pull request.** CI refuses a file that breaks the rules below.
5. **Merge it to `master`.** The dev asset route publishes at once, prod on the manual run, and
   readers see the change within five minutes.

To change an announcement or end it early, edit or delete its entry the same way.

## The entry

```json
{
  "announcements": [
    {
      "id": "2026-08-maintenance",
      "text": "System maintenance August 4th and 5th",
      "links": [{ "text": "Learn more", "url": "https://status.arxiv.org" }],
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
| `links` | optional | One link, or two, each `{ "text": …, "url": … }`; `url` is an absolute `https://` URL, any host. |

- **Order:** newest first, so add a new entry at the top. When entries overlap, the latest
  `start` shows (a short notice over a long campaign). Expired entries never show and may stay.
- **Dismissal** holds on every arXiv site (a cookie on the parent domain), for that `id` and
  message, until 30 days after `end`, so an extended `end` stays dismissed. Editing `text` or a
  link shows the entry again to everyone.
- **Day-of reminder:** to show a notice again on its day to readers who dismissed it, end the
  entry the midnight before and add a copy above it, with its own `id`, starting at that
  midnight (DESIGN-POLICIES, Banner).
- **Times:** write a range with "to", not a dash ("7:00 to 12:00 EDT"): screen readers skip or
  misread a dash between times. Join the range with no-break spaces, ` ` in the file
  (`7:00 to 12:00 EDT`), so a narrow screen never splits it.
- **Checks:** CI refuses a file that breaks these rules; run
  `python3 -m unittest discover -s templates/tests` to check locally.

## Why it works this way

- **Data, not page markup.** `chrome/banner.js` fetches the file from the asset route (cached
  five minutes). An announcement therefore changes no page, and pages cached for a year
  (browse's abs pages) need no purge.
- **The script draws the band.** This is the one recorded exception to "scripts never carry
  content" (DESIGN-POLICIES, Banner): an announcement is temporal and never page-critical, so a
  reader without JavaScript sees none.
- **Plain text and links:**
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
