# arXiv design system — digests for agents

One file per pattern page, generated from the page by `verification/gen-digest.py`.
Each holds the classes, what they do and require, the markup to copy, and the rules.
Nothing else. A digest exists only for a page that has had its review pass.

| Component | Digest | Summary |
|---|---|---|
| Buttons | [buttons.md](buttons.md) | Each arXiv button family shares the same mechanical spec, with color used to differentiate by context: Open Blue for public pages and Access Lime for internal t |
| Alerts | [alerts.md](alerts.md) | Alerts are a critical component of successful user journeys. They go hand in hand with [form validation](forms.html) but have many uses beyond forms as well. Al |
| Tags | [tags.md](tags.md) | A small rounded element used for categories, search filters, states, and other small multiples. Tags remain the same across public and internal pages. |
| Special messages | [messages.md](messages.md) | When arXiv has something special to say on the platform itself, this is how we do it. We are starting with a small announcement band above the header. Other opt |
| Site footer | [footer.md](footer.md) | The universal arXiv public-page footer (`.ds-site-footer`). Note that the footer is still changing post-spinout as we figure out the best way to acknowledge maj |
| Forms & validation | [forms.md](forms.md) | The design system supports highly accessible forms with robust validation display options. Explore validation examples in action in this [submission metadata mo |
| Site header | [header.md](header.md) | The arXiv public-page header sets the tone for the entire platform: simple, straightforward, and utilitarian. It consists of a dark band with logo on the left,  |
| Icons | [icons.md](icons.md) | The design system uses the Lucide icon set which is open source, community supported, and available for both commercial and non-commercial use under the ISC lic |
| Using the design system | [using.md](using.md) | This page shares how to get started with the arXiv Design System: basic markup, which files to link to, in what order, and a handful of things to avoid. If you  |
| Links | [links.md](links.md) | Text links are simple but important to get right. Every link inside a `.ds-page` is the inline text link, with no class to add, and appears in Link Blue, a spec |
| Cards | [cards.md](cards.md) | When you need to draw a box around related content, reach for a card. Public pages and internal tools each have their own color variations but the use cases are |
| Colors | [colors.md](colors.md) | The full arXiv palette, rendered. Written spec and rationale: [color-mapping.md](doc.html?src=docs/color-mapping.md) (source of truth — if this page and the spe |
| Dark mode | [dark-mode.md](dark-mode.md) | In the design system, every colour comes from a token and the tokens flip in each mode. A page or component built from the color tokens follows the mode without |
| Modal dialogs | [modals.md](modals.md) | A window that overlays the background page until it is answered or dismissed. There are many ways to build a modal wrong. The design system starts with a native |
| Tables | [tables.md](tables.md) | The table and what can be built on it: sortable columns, a filter toolbar, row selection and bulk actions. All of it is shared by the public site and internal t |
| Progressive disclosure | [progressive-disclosure.md](progressive-disclosure.md) | Options to toggle open additional content. HTML paper pages, for example, hold far more than a reader wants to see all at once, so they use every progressive di |
| Spacing | [spacing.md](spacing.md) | Every gap on arXiv pages comes from the scale defined below. The scale is a 4px-based / 8-point scale, with no off-scale values permitted. More details in [DESI |
| Pager | [pager.md](pager.md) | Previous and Next controls with a position counter for going through a set, one item at a time. |
| Typography | [typography.md](typography.md) | arXiv sets all text in the IBM Plex family with STIX Two Math for notation. All fonts are self-hosted and open source with no external font services. |
| Versions | [version-display.md](version-display.md) | How a paper shows its submission date, the timestamp it was announced at, its current revision date, and its version history. arXiv displays this info over and  |

## Not yet digested

These pages have not had their review pass. Read the page itself, and expect the shape to differ.

- brand.html
- layout-patterns.html
- outreach.html
