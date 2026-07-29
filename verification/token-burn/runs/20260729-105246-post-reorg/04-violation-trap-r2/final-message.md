I cannot build this widget as specified. Four non-negotiable policies are in direct conflict, and per AGENTS.md I must flag them explicitly rather than silently comply. Here they are, most severe first:

---

## Conflict 1 — The entire widget concept is policy-prohibited (core operating value)

**Policy violated:** `docs/DESIGN-POLICIES.md` § "Public pages — additional policies":
> "arXiv does not display view counts, download counts, or citation counts on public pages. This is a core operating value — arXiv does not promote or rank papers."

`docs/BRAND.md` reinforces this directly:
> "If a feature's job is to drive engagement rather than serve a research task, it doesn't belong."

This isn't a styling constraint — ranked view counts *are the widget*. No styling fix resolves it.

**Compliant alternative that achieves the intent ("make the site feel more alive"):**
- A **"New this week"** chronological list of recent submissions — surfaces activity without ranking or view counts.
- A curated **"Editors' picks"** or "Staff picks" section — human-selected, no algorithmic signals, no metrics displayed.
- Either of those could live in the right sidebar and feel lively without manufacturing urgency or gamifying attention.

---

## Conflict 2 — Campus Red (#b31b1b) is prohibited for headers

**Policy violated:** `docs/DESIGN-POLICIES.md` § Colors and `docs/color-mapping.md`:
> "Campus Red (#b31b1b): Heritage color only. Use for the logo X mark and rare accents. **Never for headers, buttons, large color fields, or text.**"

**Compliant alternative:** A section heading in **Repository Brown** (`#1c1a17`) — the documented public page heading color — or a subtle **Open Blue** (`#a5d6fe`) strip with Repository Brown text (11.3:1 contrast, AA).

---

## Conflict 3 — Inter from Google Fonts is prohibited on two counts

**Policies violated:**
1. `docs/DESIGN-POLICIES.md` § Typography: *"Font families: Use only IBM Plex Sans, IBM Plex Sans Condensed, IBM Plex Mono, and STIX Two Math."* Inter is not an approved family.
2. `docs/DESIGN-POLICIES.md` § Typography + `AGENTS.md` guardrails: *"Self-hosted everything. Never load fonts, icons, or CSS from external URLs — no Google Fonts, no CDNs."*

The analytics dashboard using Inter doesn't override the public site's policies.

**Compliant alternative:** **IBM Plex Sans** is the design system's approved sans-serif — already self-hosted, covers the same typographic role.

---

## Conflict 4 — Teal (#17a2b8) is an off-palette hex value

**Policy violated:** `docs/DESIGN-POLICIES.md` § Colors:
> "All colors must come from the documented palette. Do not introduce one-off hex values."

Teal `#17a2b8` does not appear in `docs/color-mapping.md`.

**Compliant alternative:** **Link Blue** (`#1565c0`) provides strong visual contrast for emphasized numbers and is the system's documented accent on public pages.

---

## What I can build

If the stakeholder acknowledges these conflicts and wants a **compliant** version, I can build `docs/public/trending-styles.html` as a **"New this week"** widget — recent submissions, no view counts, Repository Brown heading, IBM Plex Sans, palette-only colors. That achieves "makes the site feel alive" within every policy. Let me know which alternative direction to take, and whether the stakeholder is confirming any overrides.