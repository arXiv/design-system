# Digests for agents — the plan

Decided with Shamsi, 2026-09-22. Follows the agent-ingestion review of
2026-09-19 (option A first, then E; C later; D only on demand).

## What a digest is

One Markdown file per pattern page, holding only what an agent needs in order
to build with the component: the classes and what each does, the parts a
class requires (an `.is-sr-only` span in an icon-only button, a script tag
for a contents bar), the markup to copy, and the rules. No nav, no demo
scaffolding, no page prose about why the thing looks the way it does. Plus
one index listing every component with a sentence each.

They are generated, never written. `verification/gen-digest.py` reads the
pattern pages and writes `docs/spec/<page>.md` and `docs/spec/index.md`;
`--check` fails when a digest is stale, like the anchors, the contents lists
and the icons page. GitHub Pages publishes them beside the pages, so any
agent reaches them by URL with nothing installed.

## Why

An agent that wants one class today reads a whole HTML page: the nav, the
demo markup, the styles that stage the demo. A compact contract it can fetch
directly is cheaper to read and harder to misread. The measured result on a
comparable system (edl.dk, 2026): about a third fewer tokens for a strong
model, and almost no invented classes for a weaker one.

## The rule that governs which pages get one

**A digest is only ever generated for a page that has had its review pass.**
A digest copies the page's contract faithfully, so a digest of a wrong page
is wrong with the same confidence, and an agent acts on it. The reviewed
pages are listed in `verification/reviewed-pages.txt`; the index names the
components that have no digest yet, and that list is the review checklist.

A page's review pass ends the same way every time: its styles move to
`docs/docs.css` (no `<style>` block left), its section titles carry the
generated anchors and its contents list is generated, and its name goes on
the reviewed list so its digest switches on.

## What the extractor reads

It is written against `buttons.html`, the first reviewed page, whose shape
every other page is being brought to:

| On the page | In the digest |
|---|---|
| `<h1>` and the header paragraph | The page's summary |
| Each `<h2 class="section-title">` / `<h3 class="section-title">` and its `.ds-section-desc` | A component, with its one-line summary |
| A "Relevant code" accordion: each `<dt>` / `<dd>` pair | The class key: name, what it does, what it requires |
| A `<pre><code>` inside that accordion | The markup to copy |
| The accessibility essentials list | Rules |
| A margin note (`.ds-marginalia`) | A note on the component it sits in |
| Everything else (demos, cards, alerts, prose about construction) | Left out |

Run on a page that has not had its pass, the extractor is a diagnostic: it
reports what the page lacks in that shape (no class key, one-line code
blocks, a section with no description). That is most of what the review
finds, found before the page is opened.

## The direction this is heading

The extractor's output format is the future structured source. The files
are Markdown with a short YAML header for the contract, so that a renderer
can later read the same file and produce the human page. When a page
round-trips (render the extracted source, diff against the hand-written page,
no meaningful difference) the hand-written HTML can be retired and the
structured file becomes the source of truth for both views. That is done
page by page; nothing is converted wholesale.

## Order

1. Extractor, against `buttons.html`. Digest published for that page only.
2. The review pass continues page by page; each finished page adds a digest.
3. When several pages are through: the benchmark (option E) on the digests,
   using the token-burn harness and its `--variant` switch, with the edl.dk
   metrics added (invented classes, missing required parts, inlined markup
   instead of the component).
4. Then `AGENTS.md` sends agents to the digests before the pages.
5. The renderer, starting from `buttons.html`, once the page shape is settled.

## Not in scope here

The `ds` CLI (search / get / check) and an MCP wrapper. They read the same
files and are added when consumers ask for them.
