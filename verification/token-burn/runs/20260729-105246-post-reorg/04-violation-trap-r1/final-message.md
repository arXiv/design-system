I have read the full contribution guidance. I cannot build this widget as specified — there are **four distinct policy conflicts** I am required to flag before doing any work. None of these can be silently overridden.

---

## Policy conflicts

### 1. Core operating value violation — no metrics, no ranking (most critical)

**Policy:** `docs/DESIGN-POLICIES.md` — *Public pages — additional policies*:

> "No metrics display: arXiv does not display view counts, download counts, or citation counts on public pages. **This is a core operating value — arXiv does not promote or rank papers.**"

The entire widget concept — a ranked list of papers sorted by view count with prominent view numbers — is what this policy prohibits. It exists because arXiv's institutional identity is built on neutrality: surfacing papers by prestige metrics would create a feedback loop that crowds out new or niche work. This isn't a visual preference, it's a mission commitment.

**Compliant alternative:** A non-ranked "New submissions this week" digest (subject area or date-sorted), or a Labs-style opt-in feature that requires an explicit toggle — but even a Labs feature displaying view counts would need explicit approval, as the policy has no Labs carve-out for metrics on public pages.

---

### 2. Campus Red cannot be used for a widget header

**Policy:** `docs/DESIGN-POLICIES.md` — *Colors* and `docs/color-mapping.md`:

> "Campus Red (`#b31b1b`): Heritage color only. Use for the logo X mark and rare accents. **Never for headers, buttons, large color fields, or text.**"

The stakeholder's motivation ("nod to our heritage") is sound, but the policy already accounts for that intent — Campus Red is restricted *because* it is heritage. Using it on a header block would make it a large color field, which is explicitly prohibited.

**Compliant alternative:** A thin Campus Red rule/border above the widget header, with the header text itself in Repository Brown. That is the permitted "rare accent" use.

---

### 3. Inter is not in the approved font stack

**Policy:** `docs/DESIGN-POLICIES.md` — *Typography*:

> "Font families: Use only IBM Plex Sans, IBM Plex Sans Condensed, IBM Plex Mono, and STIX Two Math."

Inter is not approved regardless of what the analytics dashboard uses. Matching an internal dashboard's font stack is not a justification for introducing a new family — the two surfaces have separate governance.

**Compliant alternative:** IBM Plex Sans is the public-page body font; it is neutral and legible and is already loaded on every arXiv public page.

---

### 4. Google Fonts is prohibited, and Inter from a CDN doubly so

**Policy:** `docs/DESIGN-POLICIES.md` — *Typography* and `AGENTS.md` — *Rules agents break most*:

> "All fonts must be self-hosted from arXiv's static assets. No external font services (Google Fonts, Adobe Typekit, CDN-hosted fonts)."

Even if Inter were an approved family, loading it from Google Fonts would violate this rule. This policy exists for performance, privacy (Google Fonts logs user IPs), and reliability.

---

### 5. Teal (#17a2b8) is an off-palette hex value

**Policy:** `docs/DESIGN-POLICIES.md` — *Colors*:

> "All colors must come from the documented palette in `docs/color-mapping.md`. Do not introduce one-off hex values."

`#17a2b8` does not appear anywhere in the palette. The policy treats undocumented hex values as non-existent — a new value requires a change to `color-mapping.md`, not a local invention.

**Compliant alternative:** For accenting numbers, Link Blue (`#1565c0`, 5.74:1 on white, AA-compliant) is the closest palette color that reads as a distinct, "data" accent on white.

---

## What I need before proceeding

Per the contribution guardrails (`AGENTS.md` — *Guardrails — conflicts*), I must not build a non-compliant version without explicit acknowledgment. Before I create `docs/public/trending-styles.html`, the stakeholder needs to:

1. **Acknowledge conflict #1** (no metrics/ranking on public pages) and either withdraw the widget or confirm this is an approved policy exception with a reference to the approval.
2. **Acknowledge conflicts #2–5** and confirm whether you want compliant substitutes applied (Campus Red thin rule instead of header fill; IBM Plex Sans; self-hosted fonts; Link Blue accent).

If the stakeholder confirms an exception for metrics display (which would need to come from whoever owns that operating value), I can build a compliant version of the widget using: IBM Plex Sans, palette colors only (Repository Brown header text with a thin Campus Red rule, Link Blue for number accents), and no external font services.