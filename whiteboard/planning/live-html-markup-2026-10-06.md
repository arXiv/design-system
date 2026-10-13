# What live arXiv HTML papers output

2026-10-06. Checked on five live papers: 2604.22725v1 (the mockup's sample), 2605.16562v1, 2310.06825v1, 2401.04088v1, 2312.11805v1.

## Math in the contents list

LaTeXML's own contents list (`nav.ltx_page_navbar > nav.ltx_TOC`) holds each heading with its MathML, including the `<annotation encoding="application/x-tex">`. A browser never displays the annotation, so the live list shows the math rendered. The TeX shows up only when a script reads `textContent`. `toc.js` and `anchors.js` now leave out `annotation` elements when they read a heading's words.

## Footnotes

```html
<span id="footnote1" class="ltx_note ltx_role_footnote">
  <sup class="ltx_note_mark">1</sup>
  <span class="ltx_note_outer"><span class="ltx_note_content">
    <sup class="ltx_note_mark">1</sup><span class="ltx_tag ltx_tag_note">1</span>
    The note, with its own math and citations.
  </span></span>
</span>
```

The note sits inline, straight after its marker. There is no separate note elsewhere and the marker is not a link. So the note can be shown in the margin with CSS, without copying or moving it. The mockup's footnote markup (a marker linking to a note elsewhere) is not what LaTeXML outputs.

## Authors

```html
<div class="ltx_authors">
  <span class="ltx_creator ltx_role_author">
    <span class="ltx_personname">Adrian Palomares</span>
    <span class="ltx_author_notes"><span class="ltx_author_notes_content">
      <span class="ltx_contact ltx_role_affiliation"><span class="ltx_contact_name">Affiliation: </span>…</span>
      <span class="ltx_contact ltx_role_email"><span class="ltx_contact_name">Email: </span><a href="mailto:…">…</a></span>
    </span></span>
  </span>
  <span class="ltx_author_before"> </span>
  <span class="ltx_creator ltx_role_author">…</span>
</div>
```

Each `ltx_creator` is one author block as the author wrote it in LaTeX, not always one person:
- 2401.04088v1 puts many names in one block;
- 2312.11805v1 has one block, "Gemini Team, Google";
- 2605.16562v1 adds an ORCID link inside the name.

A design that needs one element per person (for example "show all 22 authors" after eight) cannot count on this markup. arXiv's own metadata has the author list.

## Other

None of the five has a `<main>` element or `role="main"`.

## Deyan's answers, 2026-10-06

The questions are in `questions-for-deyan.html`; he answered in Slack.

**Display equations.** LaTeXML's `<table>` markup for display equations is due to change: Vincenzo has a proposal for new markup, probably CSS grid, because the tables are bad for accessibility and do not reflow on phones. Reflow on phones needs a line-breaking script until browsers support MathML line-breaking. The `role="presentation"` question waits for the new markup. Deyan agrees a wide equation should never scroll the page, because that would also move the margin notes on wide screens.

**TeX for View TeX and Copy.** LaTeXML cannot keep the author's original string. It expands the author's macros into standard TeX (`\myNat` becomes `\mathbb{N}`) so the TeX works outside the paper. papers.html says so.

**Permalink ids.** LaTeXML's ids follow the document's structure and are meant to become stable, but they are not guaranteed yet. When a rendering fix restores a missing section or paragraph, regenerating the paper renumbers everything after it at the same level, even within one version. No doc should promise that a permalink is permanent.

**Stylesheets.** The early-2026 scaffold refactor puts arXiv's theme on top of ar5iv's base styling, and any arXiv rule already wins. The theme needs updating to the current design system, and ar5iv's theme switcher can go. To check with Deyan: whether the scaffold uses cascade layers as the papers.html code sample shows. Also for that conversation: the theme's page grid gives each side column a 14rem minimum (`--nav-width: minmax(14rem, 25rem)`), which fits the live 832px article in a 1280px window exactly. A wider article, such as the mockup's 850px, makes the page scroll sideways from 1280 to 1297px unless that minimum goes; the mockup sets it to 0, since LaTeXML's sidebar is not shown.

**`<main>`.** Workable: the scaffold can wrap LaTeXML's `<article>`. Shamsi has answered him.

**Abstract heading.** LaTeXML already outputs a visible `<h6>` "Abstract", so a second, hidden heading is not needed. Deyan has an open question about promoting it to a higher level. When the author did not use `{abstract}`, there is no abstract to mark. The mockup still hides LaTeXML's heading and adds its own `<h2>` (`html-phase1.html`, the `ltx_abstract` block); that waits on Shamsi's decision about the level.

**Table scroll regions.** Deyan wants to discuss with Bruce and asked what `role="region"` solves; Shamsi sent the reasons. `.ltx_table` and `.ltx_tabular` are the classes to anchor on. Overflow scrolling needs a wrapper or `display: block` on the table, which raises the same semantics question as the equations.

**Bibliography position.** LaTeXML cannot move the bibliography out of the narrative flow: a document can have several, for example one per chapter. Deyan suggested drawing the band with CSS instead. Tested in `html-phase1.html`: the bibliography stays where LaTeXML puts it, at the body width, and a `box-shadow` clipped by `clip-path` paints the tint to the window edges. A shadow is not part of the page width, so it cannot cause sideways scroll. Measured at 375, 768, 1280 and 1920px: the band is continuous for the main bibliography, a chapter-level bibliography nested in a section, and an appendix after the references; the references line up with the body text; print shows no tint. The earlier version, with negative margins measured from the viewport, fell short of the edges for a nested bibliography at tablet widths and left an appendix after the references as a tinted box at the body width.
