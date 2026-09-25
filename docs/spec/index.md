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

## Not yet digested

These pages have not had their review pass. Read the page itself, and expect the shape to differ.

- brand.html
- colors.html
- dark-mode.html
- forms.html
- internal/cards.html
- internal/color-tokens.html
- internal/metadata-panel.html
- internal/tables.html
- links.html
- modals.html
- organizing-content.html
- progressive-disclosure.html
- public/footer.html
- public/header.html
- spacing.html
- typography.html
- version-display.html
