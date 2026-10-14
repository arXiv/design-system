# Decision: the light block is checked, 2026-10-14

Branch `light-block-check`, from master.

## What was wrong

The `[data-theme="light"]` block keeps an area light inside a dark page, as the demos on the dark mode page do. No check compared it with the default values in `:root`:

- In `design-system.css` it typed out seven colours that `:root` takes from the named palette (Link Blue, Repository Brown and others). A change to a palette colour would not have reached readers who chose Light, and every check would still have passed.
- It did not reset three values that dark mode changes: `--ds-scrim`, `--ds-note-mark-fg` and `--ds-note-mark-internal`.
- `internal-tools.css` had no light block, so its three dark values (`--ds-surface-hover-strong`, `--ds-surface-active`, `--ds-text-strong`) stayed dark in a light area.

## What was decided

Shamsi chose to check the light block and to point it at the named palette.

- `check-drift.py` now fails when a light block misses a value that dark mode changes, or when one of its values differs from `:root`. It checks both stylesheets.
- The seven colours in the tier 1 light block now use the palette tokens.
- The three missing values are reset in tier 1, and tier 2 has a light block.

Not rendered in a browser. The seven token changes cannot change how a page looks; the resets only affect a light area inside a dark page.
