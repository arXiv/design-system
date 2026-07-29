# Component Audit — 2026-06-11

**Scope:** 9 pages — the 2 redesign mockups plus 7 live arXiv pages chosen as template-family representatives.
**Method:** Playwright captured viewport screenshots at 1440px with top/mid/bottom scroll positions where relevant. 15 captures total in `screenshots/components/`.
**Goal:** identify components (a) shared across pages and worth promoting to the design system first, (b) inconsistent across pages and in need of unification, (c) absent from the redesign but present on live (or vice versa).

## Headline

arXiv has **at least three distinct design eras coexisting on production today**:

| Era | Visible on | Distinctive traits |
|---|---|---|
| **Legacy** | homepage, abs page, browse listings, login | Cornell University banner, red ar5iv header, dense link blocks, fieldset+legend forms, sidebar widgets |
| **Modernized info site** | info.arxiv.org/help | Dark/light theme toggle, 3-column nav (left + content + right TOC), breadcrumbs, modern typography |
| **Modern HTML reader (ar5iv)** | /html/<id> | TOC left sidebar, red status bar with action links, ar5iv-rendered body |

**The redesign introduces a fourth design** (`abstract-redesign`, `html-redesign`) — a consistent light-Card-Grey / black two-tone family that's clearly related across the two mockups but distinct from any of the three live eras.

This is the strategic context for component-level promotion: **the design system isn't replacing one current style with another, it's introducing a single language to replace three.** The patterns we promote first should be the ones that recur across pages today, because those are the highest-leverage unification targets.

---

## Cross-page component inventory

### Components that appear on most/all pages

These are the **highest-priority promotion targets** — they're the bones of the site, and right now each page implements them slightly differently.

| Component | On legacy pages | On info-site | On redesign mockups | Promotion status |
|---|---|---|---|---|
| **Header** (logo + nav + chrome) | Cornell banner + arXiv red bar | red bar w/ theme toggle | black bar (abstract) / Card Grey bar (reader) | ❌ Not promoted. 4 distinct variants in the wild. |
| **Search bar** | Inline in red header | Bigger, rounded | Search icon-link in abstract nav; absent from reader chrome | ❌ Not promoted. |
| **Top-nav links** (Help / Login / About) | Inline white-on-red in legacy | Inline in dark bar | Top-row dark bar (abstract); icon-only nav (reader) | ❌ Not promoted. |
| **Footer** (warm grey w/ funder logos + nav links) | Present on most live pages | Same | Present on both new mockups | ⚠️ Used everywhere; not yet in the design system. |
| **Funder acknowledgment** (Simons / Schmidt / member institutions) | Top-right of dark bar OR in footer | In footer | In footer | ⚠️ Inconsistent placement. |
| **Buttons** (primary action) | Solid dark blue on legacy (login Submit) | Modern button family | Open Blue, V3 construction in mockups | ✅ Promoted (`.ds-btn-primary/secondary`). |
| **Inline links** | Browser default blue + underline | Custom styling | Link Blue + underline + hover/visited | ✅ Promoted (`.ds-link`). |
| **Form fieldset + legend + label + input** | Used on login, search-advanced | Possibly absent | Not yet in mockups | ❌ Not promoted. Legacy form pattern still pervasive. |
| **Alert / notice (info)** | Light-blue rounded notice on login | unknown | Not in mockups yet | ✅ Pattern promoted (`.ds-alert`), not applied to mockups. |
| **Alert / notice (warning)** | None obvious | unknown | Amber version-warning in abstract mockup | ✅ Pattern promoted (`.ds-alert.ds-alert-warning`). |

### Components specific to certain page types

| Component | Found on | Variants worth standardizing? |
|---|---|---|
| **Breadcrumbs** ("Home › Help") | info-site only | Yes — if other pages get breadcrumbs (browse, listings, search results), they need a shared component. |
| **Left sidebar navigation** | info-site (hierarchical), html-current (TOC) | Two different uses; could share a base "side nav" component with use-specific modifiers. |
| **Right sidebar / in-page TOC** | info-site (TOC of headings), abs-current (action panel) | Conceptually different. The info-site's in-page TOC is the most reusable pattern. |
| **TOC dropdown menu** | New html-redesign | Net-new component — worth promoting as a generalization even though no other current page uses it yet. |
| **Dark/light theme toggle** | info-site only | Worth standardizing the toggle UX **when** dark mode is taken up (currently deferred per `dark-mode-decision.md`). |
| **Citation export panel** (BibTeX / APA / Chicago / MLA) | abs-current sidebar | Listed `[ ]` in design-system roadmap — confirmed as missing pattern. |
| **Bibliography back-links / "Cited by"** | abs-current "Bibliographic and Citation Tools" | Worth surfacing into the design system once the format settles. |
| **Version pills** (v1 / v2 / v3) | abs-current + abstract-redesign | Listed `[ ]` in roadmap. Both versions use the same conceptual pattern. |
| **Listing item** (paper + abstract + authors + tags) | browse-listing-current | Frequent pattern, no current design-system equivalent. Worth a future promotion. |
| **Subject browse grid / dense link cluster** | homepage | Highly arXiv-specific, awkward to "componentize." May not belong in a shared system. |
| **Search filter sidebar** (Subject / Date / Term type) | search-advanced | Form-heavy pattern, could share the form components. |
| **Search "Tips" sidebar** | search-advanced | Similar to a contextual help panel. |
| **Login form** (fieldset, password, register CTA) | login | Form-heavy; could be composed from form atoms once those exist. |
| **Equation chrome / hover pill** | New html-redesign only | Net-new. Promoted as `.ds-element-pill`. |
| **Citation popover** | New html-redesign only | Net-new. Promoted as `.ds-popover`. |
| **Marginalia (right margin notes)** | New html-redesign only | Net-new. Promoted typography (`.ds-annotation`). |
| **Reading-progress bar** | New html-redesign only | Net-new in the chrome. Not yet codified. |
| **Labs toggles** ("Hugging Face Spaces") | New abstract-redesign | Listed `[ ]` in roadmap. |

---

## Inconsistencies worth naming

These are the cases where the same conceptual thing has different implementations across pages:

1. **The site has at least 4 different headers** (legacy red, info-site red+toggle, current ar5iv reader, new redesign tan/black). Each requires its own CSS, separately maintained. **Codifying a "header" pattern is probably the highest-leverage promotion next.**

2. **The "Login" affordance** appears in at least 3 styles — orange Login text-link in legacy, blue link in modernized, embedded in nav in info-site, dark-bar link in redesign abstract.

3. **Search inputs** vary by page — mini-search in header, full search field on homepage, faceted search on advanced. None share a base style today.

4. **The footer** is similar but not identical across legacy pages, info-site, and the new redesign. Codifying the footer as a single shared component would prevent future drift.

5. **Form patterns** (legacy uses `<fieldset><legend>`, modernized doesn't). Picking a single pattern and porting both old and new code to it is meaningful work but bounded.

6. **Action buttons** appear in at least 4 visual styles across pages (red header buttons, light-blue Search button, solid blue Submit, redesign V3 blue HTML/PDF). V3 is the codified pattern; everything else needs to adopt.

---

## Recommendations for the design-system roadmap

Re-prioritizing the existing roadmap (`docs/public/README.md`) based on this audit:

**High frequency × high drift — promote next:**
1. **Footer component** — **already approved** as part of the arxiv-browse "spinout-header-footer" Cloud Run deployment (see addendum below). The approved version is essentially identical to what's in the `abstract-redesign.html` mockup: warm-grey band, same acknowledgment text, same footer nav, same Simons + Schmidt funder logos on the right. This is the **lowest-friction promotion target** because it's already validated in three places — promotion is mostly a codification exercise.
2. **Header component (light + dark variants)** — used on every page, currently fragmented into 4 implementations.
3. **Search input** — multiple variants in use; standardize a shared base.
4. **Form atoms** (label + input + fieldset + validation) — bridges legacy and modern. Used on login, advanced search, submission portal.

**Net-new patterns in the mockups, worth promoting opportunistically:**
5. **TOC dropdown** (`.ds-toc-dropdown` or similar) — already validated in `html-redesign`, can be promoted via the `/promote-pattern` skill anytime.
6. **Reading progress bar** — small but novel.
7. **Equation hover chrome** (the pill + frame combination beyond just `.ds-element-pill`) — equation-specific composition.

**Roadmap items that are still genuinely needed (confirmed by this audit):**
8. **Citation export panel** (`[ ]` in roadmap, present on abs-current).
9. **Version display** (`[ ]` in roadmap, present on abs-current + abstract-redesign).
10. **Author list with truncation** (`[ ]` in roadmap, present on abstract pages — the 100+ author case is real).
11. **Labs toggle section** (`[ ]` in roadmap, present in abstract-redesign).
12. **Announcement / banner component** (`[ ]` in roadmap, present on homepage and many current pages).

**Roadmap items where the audit reveals a thinner case:**
13. **Tertiary / text-only button** — used inconsistently; lower urgency until a clear repeated use case emerges.

---

## Observations beyond components

A few things noticed during the audit that aren't strictly component-level but worth flagging:

- **The info site is unexpectedly modern.** It has a theme toggle, breadcrumbs, sidebar nav, in-page TOC — all things the rest of arXiv lacks. It might be the closest thing to a working reference for "what arXiv pages could be."
- **The "Cornell University" banner is universal on legacy pages but absent from the redesign mockups.** This is correct given the post-spinout context — but it means the redesign mockups are visually quite different from any current arXiv page, and stakeholder review will need to clearly frame this as intentional.
- **Donation appeals on the homepage take significant vertical space** above the fold (independence banner + donation appeal bar). The redesign mockups don't include either; whether to retain them and where is a strategic question, not a component-design question.
- **Multiple pages have multiple "Login" affordances** (top-right link + dedicated login flow + sometimes a third). Simplifying the login surface is a UX question that touches the design system.

---

## Addendum — approved footer in arxiv-browse Cloud Run

Captured 2026-06-11 from `https://arxiv-browse-spinout-header-footer-874717964009.us-central1.run.app/abs/2604.02161` — a deployment of the arxiv-browse repo with the approved post-spinout header and footer treatment. Screenshots: `screenshots/components/10-abs-spinout-footer-NEW-{top,bottom,full}.png`.

Two findings worth surfacing:

1. **The approved footer matches the `abstract-redesign.html` mockup almost exactly.** Warm-grey band with the "We gratefully acknowledge support from our major funders, member institutions, and all contributors" centered acknowledgment, the standard footer nav (About · Help · Contact · Subscribe · Copyright · Privacy · Accessibility · Operational Status), and Simons + Schmidt funder logos on the right. The visual treatment is functionally identical between the two — meaning the footer promotion is more "extract what already exists" than "design something new."

2. **The body of the abs page in this deployment is still the legacy page** (Cornell-era sidebar layout, dense link blocks, "Access Paper" panel, Bibliographic Tools tabs at the bottom). The spinout deployment updates the chrome (header + footer) but leaves the body of the abs page largely unchanged. This is a useful signal: arXiv's approach in arxiv-browse is **chrome-first**, with deeper-page redesigns deferred. The redesign mockups in this repo go further than the spinout deployment by also redesigning the body of the abs page.

**Implication for the design system:** the footer is **the most validated component on this list.** Three implementations (approved Cloud Run, `abstract-redesign.html`, `html-redesign.html`) all agree. Promotion is low-risk, high-leverage. Suggested next action: extract the footer CSS from one of the three and codify as `.ds-footer` (or similar) in `docs/public/design-system.css`, with a `footer-styles.html` demo page.

---

## What's NOT in this audit

This is a **single-viewport snapshot audit**. It does not cover:
- Hover, focus, or other interactive states
- Mobile rendering of live pages (skipped intentionally — known issue)
- Component states (loading, error, disabled, etc.)
- Accessibility (screen-reader announcement, focus order, contrast)
- Performance / page weight

A second pass with explicit interaction triggers (Playwright `.click()` + `.hover()`) before each screenshot would surface state-based components. Probably worth doing after the first round of stakeholder feedback.
