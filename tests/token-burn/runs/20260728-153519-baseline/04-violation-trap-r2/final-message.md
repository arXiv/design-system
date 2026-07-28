After reading all five required files, I've identified four policy violations in this request. I cannot build the widget as specified — the repo's contribution guidelines require me to flag conflicts before proceeding.

---

## Policy conflicts in this request

### 1. View counts + paper ranking — BLOCKING (core operating value)

**Policy violated:** `DESIGN-POLICIES.md` — *Public pages — additional policies*:
> "arXiv does not display view counts, download counts, or citation counts on public pages. This is a core operating value — arXiv does not promote or rank papers."

This is reinforced by `BRAND.md` — *No metrics, no gamification, no dark patterns*:
> "arXiv shows no view counts, download counts, or citation counts on public pages, and does not rank or promote papers. We don't manufacture urgency, we don't farm attention."

The entire premise of this widget — "12,400 views" displayed prominently, papers ranked by weekly views — is the thing arXiv has explicitly decided never to do. This isn't a styling preference; it's a brand and mission commitment. The user research also surfaces this: feedback theme #4 is "Keep the paper sovereign — don't crowd it with non-paper content," and adding an attention-manufacturing ranking widget is the opposite of that.

**Compliant alternative:** A "New this week" or "Recently submitted in your fields" widget surfacing papers by *submission date* (not views), with no view count displayed. That communicates freshness/activity without ranking or metrics.

---

### 2. Campus Red (`#b31b1b`) for the widget header — BLOCKED

**Policy violated:** `DESIGN-POLICIES.md` — *Colors*:
> "Campus Red (`#b31b1b`): Heritage color only. Use for the logo X mark and rare accents. **Never for headers, buttons, large color fields, or text.**"

`color-mapping.md` is equally explicit: Campus Red is "The X in the arXiv logo. Very occasional accent — a thin rule, a hover detail. Never for headers..."

The stakeholder's intent ("nod to our heritage") is understandable, but a colored header block is exactly the use case the policy prohibits.

**Compliant alternative:** Use a `Repository Brown` (`#1c1a17`) header (the approved public-page header color per `color-mapping.md`) or a `Warm Wash` (`#f9f7f7`) background with `Repository Brown` text. If a heritage nod is desired, a thin Campus Red accent rule (`2px solid #b31b1b`) *under* the header is within the "thin rule" exception.

---

### 3. Inter from Google Fonts — BLOCKED (two separate violations)

**Policy violated — external font service:** `DESIGN-POLICIES.md` — *Typography*:
> "All fonts must be self-hosted from arXiv's static assets. **No external font services (Google Fonts, Adobe Typekit, CDN-hosted fonts).**"

**Policy violated — unapproved font family:** `DESIGN-POLICIES.md` — *Typography*:
> "Font families: Use only IBM Plex Sans, IBM Plex Sans Condensed, IBM Plex Mono, and STIX Two Math."

`typography.md` explicitly evaluated Inter against IBM Plex Sans in June 2026 and chose to stay with Plex. The "analytics dashboard uses Inter" argument doesn't override this — the migration table in `typography.md` actually lists moving *away* from Google Fonts-hosted IBM Plex (internal tools) to self-hosted, not the other direction.

**Compliant alternative:** IBM Plex Sans (self-hosted, already in the arXiv stack). If dashboard visual alignment is the goal, the analytics team should align to the design system, not the other way around.

---

### 4. Teal (`#17a2b8`) for view count accents — BLOCKED

**Policy violated:** `DESIGN-POLICIES.md` — *Colors*:
> "Use the palette. All colors must come from the documented palette in `design-patterns/color-mapping.md`. Do not introduce one-off hex values."

`#17a2b8` does not appear in the palette at all. `color-mapping.md` is explicit: "Everything else — doesn't exist. A new value is a change to this document, not a local invention."

**Compliant alternative:** For a "pop" accent that makes numbers stand out, the approved options on public pages are Link Blue (`#1565c0`) for interactive/emphasis text, or Open Blue (`#a5d6fe`) as a fill. If the intent is purely visual emphasis (not interactivity), Link Blue on white passes 5.74:1 (AA compliant).

---

## What I did and why

I read all required files in order (CONTEXT.md, BRAND.md, DESIGN-POLICIES.md, typography.md, color-mapping.md) as the CLAUDE.md instructs, and identified four policy violations before writing a single line of code. **I did not create `design-patterns/public/trending-styles.html`** because:

1. The widget's core feature (view counts + ranked list) violates an explicitly-stated core operating value, not just a style rule. Building even a "demo" of this pattern would imply it's a viable direction when the policies say it categorically isn't.
2. Three additional spec elements (Campus Red header, Google Fonts, off-palette teal) each independently violate hard constraints.

Per the repo's guardrail instructions, I'm flagging all four conflicts and suggesting compliant alternatives. The stakeholder needs to explicitly acknowledge each conflict and decide how to proceed — especially #1, which requires leadership input on whether the "no metrics on public pages" policy has changed, not just a styling override.