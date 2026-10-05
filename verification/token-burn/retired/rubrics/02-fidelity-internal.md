# Rubric — 02 fidelity internal (bulk-action bar)

**What this task measures:** correct surface identification (internal!) and reuse of existing internal components instead of reinvention.

Hard-constraint checks:
- [ ] Internal context: Access Lime primary action, NO Open Blue primary — this is the core context-crossing test
- [ ] "Remove selected" uses the danger treatment and is visually separated from Approve (destructive-confirmation rule at least acknowledged)
- [ ] Success/failure messages use the existing `.ds-alert` (internal stylesheet), not bespoke chrome
- [ ] Reuses internal `design-system.css` classes (buttons, alerts, table adjacency); page-local CSS limited to glue
- [ ] Selection count + Clear selection present; focus-visible on all interactive elements
- [ ] No external resources loaded

Judgment (designer pass):
- Does the bar read as connected to the table (visual adjacency)?
- State transitions plausible (nothing selected → active → result message)?
- Information density appropriate for a staff tool?

Reasoning quality: did the final message name the internal-vs-public rule and the destructive-action rule explicitly?
