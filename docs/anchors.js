/* A link to every section, added to the page rather than written into it.
 *
 *   <script src="anchors.js" defer></script>
 *
 * The ids themselves are NOT this script's job — they are written into the
 * HTML by verification/gen-anchors.py, so a fragment works with JavaScript
 * off, works for a link arriving from another page, and is resolved by the
 * browser on first load. This adds only the affordance: a control beside each
 * heading that copies the link to it.
 *
 * It is a button, not an anchor. An <a href="#section"> in a heading is a
 * second tab stop that goes nowhere a reader wanted to go — they are already
 * looking at the section. What they want is the address, so the control
 * copies it and says so.
 */
(function () {
  var LINK_ICON =
    '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/>' +
      '<path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>';

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

    document.querySelectorAll('.section-title[id]').forEach(function (h) {
      if (h.querySelector('.ds-anchor')) return;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'ds-anchor';
      btn.innerHTML = LINK_ICON;
      // The name carries the section, so a screen-reader user hearing a list
      // of buttons is not given twelve identical "Copy link to section".
      btn.setAttribute('aria-label', 'Copy link to ' + h.textContent.trim());
      btn.title = 'Copy link to this section';
      btn.addEventListener('click', function () {
        var url = location.href.split('#')[0] + '#' + h.id;
        write(url).then(
          function () { status.textContent = 'Link to ' + h.textContent.trim() + ' copied'; },
          function () { status.textContent = 'Copy failed — the address is ' + url; }
        );
      });
      h.appendChild(btn);
    });
  });
})();
