# blog.arxiv.org theme — release artifact

`arxiv-blog-theme.zip` is the packaged WordPress theme for blog.arxiv.org
("arXiv News"). It is stored here so theme releases live somewhere besides
Shamsi's machine — this directory is an artifact shelf, nothing more.

**Current version: 0.8.6** (see `Version:` in the zip's `style.css`).
Each release replaces the zip in place; older versions live in git history.

## This is not design-system source

The theme is a *consumer* of the design system, and its CSS carries
deliberate, documented blog-only departures (Open Blue header field, a
temporary verbatim copy of the dark palette pending promotion, a
Material-icons continuity exception). Never read the zip's CSS as a style
reference — `docs/` is the only build reference in this repo.

## Source of truth

The theme's git repo (full history, one tag per release) lives at
`~/arxiv/repos/arxiv-blog-theme` on Shamsi's machine. Change the theme
there; this zip is regenerated from a tag via `git archive`.

## Installing on WordPress.com

wp-admin → Appearance → Themes → Add New Theme → Upload Theme → choose the
zip → **"Replace current with uploaded"**. Do not use the Calypso theme
installer (it auto-activates). The zip's `EDITOR-GUIDE.md` covers editor
workflows and one-time Jetpack settings.
