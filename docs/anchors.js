/* A Permalink in every section heading, added to the page rather than written into it.
 *
 *   <script src="anchors.js" defer></script>
 *
 * The ids themselves are NOT this script's job — they are written into the
 * HTML by verification/gen-anchors.py, so a fragment works with JavaScript
 * off, works for a link arriving from another page, and is resolved by the
 * browser on first load. This adds only the control that copies the link.
 */
(function () {
  var LINK_ICON =
    '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>' +
      '<path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>';

  function write(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).catch(function () { return legacy(text); });
    }
    return legacy(text);
  }
  function legacy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:-1000px;opacity:0';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    return ok ? Promise.resolve() : Promise.reject();
  }

  document.addEventListener('DOMContentLoaded', function () {
    var status = document.getElementById('ds-anchor-status');
    if (!status) {
      status = document.createElement('span');
      status.id = 'ds-anchor-status';
      status.className = 'is-sr-only';
      status.setAttribute('role', 'status');
      document.body.appendChild(status);
    }

    document.querySelectorAll('section > :is(h2, h3):first-child[id]').forEach(function (h) {
      if (h.querySelector('.ds-permalink')) return;
      var name = h.textContent.replace(/\s+/g, ' ').trim();
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'ds-permalink';
      // The visible word starts the name; the hidden part says which section.
      btn.innerHTML = LINK_ICON + 'Permalink<span class="is-sr-only"> to ' + name.replace(/[&<>]/g, function (c) { return '&#' + c.charCodeAt(0) + ';'; }) + '</span>';
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var url = location.href.split('#')[0] + '#' + h.id;
        write(url).then(
          function () { status.textContent = 'Link to ' + name + ' copied'; },
          function () { status.textContent = 'Copy failed — the address is ' + url; }
        );
      });
      h.appendChild(btn);
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
