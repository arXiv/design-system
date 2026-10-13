# How the report grades a build

For Shamsi and Claude. The team report shows only the grades; this file says what they mean.

## Visual fidelity

Shamsi's verdict in the blind review:

| Review verdict | Report grade |
|---|---|
| Accept | Pass |
| Accept with changes | Pass with changes |
| Reject | Fail |

## Programmatic fidelity

Claude's grade from the automated checks and a read of the code. It is written to `technical.json` as `programmatic`, with the reasons in `notes`, which appear in the detailed report.

- **Pass:** every automated check passes, and the code uses only design-system classes and tokens. The checks are accessibility (axe), contrast in light and dark, no sideways scrolling on a phone, a visible keyboard focus, the page working without JavaScript, and nothing loaded from another site.
- **Pass with changes:** the checks pass, but the code departs from the design system in small ways: a few page-only styles, the wrong component for a job, or a component rebuilt by hand instead of reused.
- **Fail:** any accessibility failure, or the page ignores the design system's components.

## Tokens

The total the agent used: input, output, and cache reads and writes. Most of it is cache reads, so the total is much larger than the text the agent wrote. There is no dollar figure, because the builds run on a Claude plan.

## What the review found

Up to three gaps in the design system that the review showed, written to `technical.json` as `findings`, and one line on what comes next as `next`.
