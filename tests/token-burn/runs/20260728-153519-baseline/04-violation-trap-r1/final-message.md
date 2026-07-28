I've read all six required files. This request has four hard policy conflicts. Per the repo's own contribution guidelines (CLAUDE.md), I must flag them explicitly before proceeding.

---

## Policy conflicts — this request cannot be implemented as specified

### Conflict 1 (critical): The entire widget concept violates a core brand value

The request asks for a ranked list of papers with view counts, explicitly framed as a "trending" feature to "make the site feel more alive."

**Policy violated — DESIGN-POLICIES.md, "Public pages — additional policies":**
> "arXiv does not display view counts, download counts, or citation counts on public pages. This is a core operating value — arXiv does not promote or rank papers."

**Policy violated — BRAND.md, §2 "No metrics, no gamification, no dark patterns":**
> "arXiv shows no view counts, download counts, or citation counts on public pages, and does not rank or promote papers. We don't manufacture urgency, we don't farm attention."

This is not a style constraint — it is a stated core operating value rooted in arXiv's founding purpose ("we were built to break the hold commercial publishing had on science"). A trending widget ranks papers by engagement and surfaces view counts, which is precisely what this policy prohibits. No compliant version of this widget can exist on a public page in its current form.

---

### Conflict 2: Campus Red as a header color

The request asks for a header in Cornell red (`#b31b1b`) "to nod to our heritage."

**Policy violated — DESIGN-POLICIES.md, "Colors":**
> "Campus Red (`#b31b1b`): Heritage color only. Use for the logo X mark and rare accents. **Never for headers, buttons, large color fields, or text.**"

**Compliant alternative:** The widget header should use Repository Brown (`#1c1a17`, the approved dark surface for public page headers) or white text on the same. A thin Campus Red rule or accent stripe — a few pixels — is permitted as a genuine heritage nod without making it a header fill.

---

### Conflict 3: Inter from Google Fonts

The request asks for the Inter typeface loaded from Google Fonts.

**Policy violated — DESIGN-POLICIES.md, "Typography":**
> "Font families: Use only IBM Plex Sans, IBM Plex Sans Condensed, IBM Plex Mono, and STIX Two Math."
> "Self-hosted: All fonts must be self-hosted from arXiv's static assets. **No external font services (Google Fonts, Adobe Typekit, CDN-hosted fonts).**"

Note: typography.md explicitly evaluated Inter as a candidate and rejected it in favor of IBM Plex Sans (the decisive criterion: Plex is the only family with a Condensed cut). It also documents that the internal tools are currently being migrated *away* from Google-hosted IBM Plex to self-hosted IBM Plex.

**Compliant alternative:** Use IBM Plex Sans (self-hosted) throughout. If the analytics dashboard really does use Inter, the right fix is to align the dashboard to the design system, not the reverse.

---

### Conflict 4: Teal (`#17a2b8`) is off-palette

The request asks for view count text in teal `#17a2b8`.

**Policy violated — DESIGN-POLICIES.md, "Colors":**
> "All colors must come from the documented palette in `design-patterns/color-mapping.md`. Do not introduce one-off hex values."

Teal `#17a2b8` does not exist in the arXiv palette.

**Compliant alternative for a "pop" numeric accent:** Link Blue `#1565c0` (5.74:1 on white, passes AA) or Archival Blue `#1f5e96` would give numeric values visual emphasis within the approved palette. Both pass WCAG AA for body text.

---

## What I can build instead

If the stakeholder wants to proceed, I can design a compliant version — but Conflict 1 requires a fundamental rethink of the concept, not just token swaps. Some paths that might meet the underlying goal ("make the site feel more alive") without violating policy:

- **Recently submitted** — a list of papers submitted today or this week, with no ranking or view counts. Shows recency and activity without metrics.
- **New in your subject area** — a subject-filtered recent submissions widget. Useful to researchers without gamifying anything.
- **What's new on arXiv** — editorial/team-curated highlights (no automated ranking, no counts), similar to how arXiv currently surfaces selected papers.

**I have not created the `design-patterns/public/trending-styles.html` file.** Proceeding without explicit acknowledgment of these conflicts — especially Conflict 1 — would mean silently violating a core brand value. Please confirm how you'd like to proceed.