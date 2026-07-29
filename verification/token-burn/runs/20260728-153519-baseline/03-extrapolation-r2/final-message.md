748 lines, 4 `</section>` tags (rationale, demo, usage, open questions), file closes cleanly with `</body></html>`.

---

Here is the design rationale, restated as requested:

---

## Design rationale — withdrawn-paper notice

**Warning variant, not error.** The notice uses `.ds-alert-warning` (amber) rather than `.ds-alert-error`. `color-mapping.md` reserves the error/failure variant (Danger Red `#c62828`) for "destructive actions and error states." Withdrawal is neither. `BRAND.md` demands "honest — no overclaiming": the amber warning register communicates *pay attention, something changed* without implying misconduct. The precedent already exists in the system — `mockups/abstract-redesign.html` uses the same amber tokens for the older-version banner, establishing that amber = advisory paper-status message.

**Position: between the date/version row and the author list.** `CONTEXT.md` states readers arriving from citations "may have no idea the paper was withdrawn," so the notice must appear before the abstract without requiring scrolling. This is the same slot the version-warning banner occupies — consistent with the system's established convention for advisory version-level messages. Placing it here lets the reader first establish the paper's identity (title, date, versions), then learn its status, then engage with the content. `BRAND.md` principle 1: "the design never competes with the science."

**Factual, attributed tone.** The copy says "The authors have withdrawn this paper" — not "This paper contains errors." The withdrawal reason appears in a clearly attributed block ("Authors' statement:") so it reads as the authors' own words, not an arXiv editorial verdict. `BRAND.md`: "Honest — We say what's true… Plainspoken — Short words, direct sentences."

**Downloads unchanged.** `CONTEXT.md` confirms the scholarly record is never deleted and content stays downloadable. `BRAND.md` principle 8 says to minimize clicks to every core task. Hiding or de-emphasizing downloads on a withdrawn paper adds friction with no benefit.

**Non-color secondary cue on the version pill.** A small `(withdrawn)` text label appears next to the version number. `DESIGN-POLICIES.md` (WCAG 1.4.1): "Never use color as the sole means of conveying information." The `aria-label` on the pill also includes "withdrawn" for screen-reader users who navigate directly to the version row. Label color is Library Grey `#6b6459` (5.83:1 on white — passes AA).

**Author-quoted reason in a nested block.** The left-border callout shape is already used in this codebase's doc pages. `currentColor` inherits the warning foreground so the border stays in-palette without a new token. The condensed-caps "Authors' statement:" label follows the established metadata-label convention throughout the abstract page.

**No new design tokens.** The entire treatment reuses `.ds-alert.ds-alert-warning` from `design-system.css`. `BRAND.md` principle 7: "arXiv is daily infrastructure maintained by a very small team. Designs must be low-maintenance." New tokens propagate through public CSS, dark-mode overrides, and forced-colors blocks — every reuse of an existing component is one less thing to maintain.