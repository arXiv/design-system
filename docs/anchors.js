/* A Permalink in every section heading, added to the page rather than written into it.
 *
 *   <script src="copy.js" defer></script>
 *   <script src="anchors.js" defer></script>
 *
 * The ids themselves are NOT this script's job — they are written into the
 * HTML by verification/gen-anchors.py, so a fragment works with JavaScript
 * off, works for a link arriving from another page, and is resolved by the
 * browser on first load. This adds only the control; copy.js, on the same page,
 * copies the link and says so.
 */
(function () {
  // The words of a heading or link as shown: MathML's TeX annotation is never
  // displayed, so it is left out, as is the Permalink control.
  function plain(el) {
    var c = el.cloneNode(true);
    Array.prototype.forEach.call(c.querySelectorAll('annotation, annotation-xml, .ds-permalink'), function (n) { n.remove(); });
    return c.textContent.replace(/\s+/g, ' ').trim();
  }
  var LINK_ICON =
    '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>' +
      '<path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>' +
    '<svg class="ds-copy-done" viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="m20 6-11 11-5-5"/></svg>';

  // copy.js does the copying and says so; this says what to copy and what to say.
  // The click stops here, so a tap on the control is not also a tap on its heading.
  function wire(btn, h, name) {
    btn.setAttribute('data-copy-link', '#' + h.id);
    btn.setAttribute('data-copied', 'Link to ' + name + ' copied');
    btn.addEventListener('click', function (e) { e.stopPropagation(); });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('section > :is(h2, h3):first-child[id]').forEach(function (h) {
      // A label inside a demo or a sidebar names a block, not a section of the page.
      if (h.querySelector('.ds-permalink') || h.closest('aside, .ds-card')) return;
      var name = plain(h);
      var btn = document.createElement('a');
      btn.href = '#' + h.id;
      btn.className = 'ds-permalink';
      // The visible word starts the name; the hidden part says which section.
      btn.innerHTML = LINK_ICON + 'Permalink<span class="is-sr-only"> to ' + name.replace(/[&<>]/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; }) + '</span>';
      wire(btn, h, name);
      h.appendChild(btn);
    });

    // A demo that writes its control into a heading with an id gets the same behaviour.
    document.querySelectorAll('.ds-card :is(h2, h3, h4)[id] > .ds-permalink').forEach(function (btn) {
      wire(btn, btn.parentElement, btn.querySelector('.is-sr-only').textContent.replace(/^ to /, ''));
    });

    // Without hover, a tap on a heading shows its Permalink; a tap elsewhere hides it.
    if (window.matchMedia('(hover: none)').matches) {
      document.addEventListener('click', function (e) {
        var hit = e.target.closest('section > :is(h2, h3):first-child[id]');
        document.querySelectorAll('.is-active > .ds-permalink').forEach(function (b) {
          if (b.parentElement !== hit) b.parentElement.classList.remove('is-active');
        });
        if (hit) hit.classList.toggle('is-active');
      });
    }
  });
})();
