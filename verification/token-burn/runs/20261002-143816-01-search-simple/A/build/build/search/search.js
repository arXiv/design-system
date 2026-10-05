/* Search pages: the two behaviours the stylesheet cannot supply.
 * Both are enhancements. Without this file every abstract shows in full
 * and the tooltips still open on hover and on focus.
 */
(function () {
  // Abstracts. The page is served with the whole abstract showing, the
  // excerpt hidden and the control hidden. Collapse each one here, as
  // docs/progressive-disclosure.html requires of a show-more control:
  // flip aria-expanded, use the `hidden` ATTRIBUTE, and swap the label.
  document.querySelectorAll('.ds-show-more[aria-controls][data-excerpt]').forEach(function (toggle) {
    var full = document.getElementById(toggle.getAttribute('aria-controls'));
    var excerpt = document.getElementById(toggle.getAttribute('data-excerpt'));
    if (!full || !excerpt) return;
    var closedLabel = toggle.textContent;
    var openLabel = toggle.getAttribute('data-open-label') || 'show less';
    function set(expanded) {
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      full.hidden = !expanded;
      excerpt.hidden = expanded;
      toggle.textContent = expanded ? openLabel : closedLabel;
    }
    set(false);
    toggle.hidden = false;
    toggle.addEventListener('click', function () {
      set(toggle.getAttribute('aria-expanded') !== 'true');
    });
  });

  // Tooltips. Escape closes an open tooltip without moving focus
  // (docs/forms.html, Tooltip); the pointer or focus arriving again clears it.
  var hosts = document.querySelectorAll('.ds-tooltip-host');
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    hosts.forEach(function (host) {
      if (host.matches(':hover, :focus-within')) {
        var tip = host.querySelector('.ds-tooltip');
        if (tip) tip.hidden = true;
      }
    });
  });
  hosts.forEach(function (host) {
    function show() {
      var tip = host.querySelector('.ds-tooltip');
      if (tip) tip.hidden = false;
    }
    host.addEventListener('mouseenter', show);
    host.addEventListener('focusin', show);
  });
})();
