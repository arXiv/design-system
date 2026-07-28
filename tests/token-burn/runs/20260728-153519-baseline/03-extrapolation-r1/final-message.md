The file is written. Here is the design rationale, restated from the final document:

---

## Design rationale: withdrawn paper notice

### 1. Warning, not error (`color-mapping.md › Status & alert colors`)

The notice uses `.ds-alert-warning` (amber), not `.ds-alert-error` (red). `color-mapping.md` reserves Error/failure for "destructive actions, error states" — system failures and unrecoverable problems. A withdrawal is neither. Most withdrawals are honest scientific corrections. Using the error variant would falsely imply misconduct. Warning is the right register: "proceed with awareness." This also follows a precedent `CONTEXT.md` sets explicitly: "An older-version notice uses the `.ds-alert` warning variant." Withdrawal is a more consequential instance of the same semantic.

`role="alert"` (assertive, not polite) is used, matching `design-system.css`'s own convention for warning and error states — a screen reader user hears the notice immediately without navigating to it.

### 2. After authors, before the abstract (`BRAND.md › #1 Interface gets out of the way`)

Two constraints pull in opposite directions. The title and authors are the paper's permanent scholarly identity — they stay valid and unchanged after withdrawal. A notice above them would suggest the paper's identity is suspect, which is false. A notice below the abstract would let readers absorb potentially invalidated claims before seeing the warning. The slot after authors and before the abstract is the only position that satisfies both. The notice is in-flow and not sticky — consistent with BRAND.md's "interface gets out of the way" and with `DESIGN-POLICIES.md`'s rule that sticky chrome is exceptional.

### 3. Factual, non-judgmental tone (`BRAND.md › Voice`)

BRAND.md Voice: "Honest — we say what's true. Plainspoken — short words, direct sentences." The notice leads with "Withdrawn" (the bare fact), states the date and the author's reason verbatim in italics, and closes with a reassurance about the scholarly record. Showing the author's own reason is the most transparent thing arXiv can do. The reassurance ("All versions remain available for download") directly addresses the anxiety a researcher who has already cited this paper might feel.

### 4. Persistent, not dismissible (`DESIGN-POLICIES.md`)

The `.ds-alert` component supports a dismiss button; the withdrawn notice does not use it. Withdrawal is permanent. A dismissed notice could be closed on one visit and forgotten on a return visit, defeating the purpose of the warning entirely.

### 5. Downloads unchanged (`CONTEXT.md › Versions`)

arXiv's explicit policy is that the scholarly record is never deleted. The download buttons appear at their standard weight and styling — no modification needed. Because the withdrawn notice is positioned before the abstract, no reader reaches the downloads without first seeing the withdrawn status. Page flow handles the ordering.

### 6. WCAG 1.4.1 — color never the sole signal (`DESIGN-POLICIES.md › Accessibility`)

The notice pairs the amber background with a warning-triangle SVG icon (`aria-hidden="true"`) and the bold leading keyword "Withdrawn" in `.ds-alert-title`. In forced-colors mode the amber collapses but the icon shape and the word "Withdrawn" persist. Warning fg `#7a5c00` on warning bg `#fff8e1` = 5.9:1, clearing AA.

### 7. Version row: current version labeled WDR (`CONTEXT.md › Versions; DESIGN-POLICIES.md › Submission type badges`)

The withdrawn version inherits the existing "current version" treatment — bold Repository Brown, `aria-current`, not a link — and adds the `.type-wdr` badge alongside it. `DESIGN-POLICIES.md` names `.type-wdr` as "dark" in the submission-type palette; Repository Brown background with white text is used, matching how that badge appears in internal tooling. Prior versions remain available as standard Link Blue underlined links. No new tokens are introduced; all styling comes from existing `design-system.css` and palette values documented in `color-mapping.md`.