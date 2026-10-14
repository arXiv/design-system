# Decisions: repo housekeeping, October 2026

Branch `repo-housekeeping`. One pull request for the whole set, so peers review it once.

## Changes reach master through a pull request (2026-10-14)

arXiv's GitHub manager decided that nobody commits directly to master. Work goes on a branch named for what it changes and reaches master through a pull request. `AGENTS.md` said "commit direct to master"; it now says this.

## Colours come from tokens, and a check enforces it (2026-10-14)

`check-policies.py` now fails any colour written straight into a rule in the two stylesheets, except white, black and the component-internal constants listed in `docs/color-mapping.md`, which the check reads. The destructive button's colours and the close button's wash joined that list. The field halos (invalid, warning, info) are now made from their status border tokens, so in dark mode they match their borders; light mode is unchanged. The tinted-band button's hover edge keeps `#c8c4be`, already on the list, because the nearest token changes in dark mode and on internal tools.
