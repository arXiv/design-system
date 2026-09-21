# Canonical asset files

Official arXiv imagery consumed by docs pages, mockups, the blog theme, and
(by URL) other repos — the visual counterpart of the stylesheets and fonts.

```
images/logos/           arXiv wordmark colorways (SVG), favicons;
                        other-org-logos/ holds funder wordmarks (footer use)
images/bones/           the bones family (smiley/party/error/infinity/labsy/tooly)
                        SVG + PNG, plus giving seals
images/illustrations/   sketch illustration set (blog cards, empty states)
images/backgrounds/     social/OG + card background pairs (photo + solid)
images/photos/          photography (campus, conferences, community)
images/board-and-CEO-portraits/  official portraits; web/ = web-sized exports
```

UI icons are not assets in this sense: they live in `docs/icons/`, one SVG per
icon, beside the fonts, and `docs/icons.html` is generated from that folder.

Conventions: SVG is the source of truth where one exists; keep published paths
stable — other repos will link them. arXiv marks can be re-exported in any
size/color on request (Shamsi has the sources).
