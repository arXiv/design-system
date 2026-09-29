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

## Not yet digested

These pages have not had their review pass. Read the page itself, and expect the shape to differ.

- brand.html
- cards.html
- colors.html
- dark-mode.html
- header.html
- links.html
- modals.html
- organizing-content.html
- outreach.html
- progressive-disclosure.html
- spacing.html
- tables.html
- typography.html
- version-display.html
