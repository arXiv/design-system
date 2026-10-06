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
