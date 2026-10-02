/* Search pages: the two behaviours the stylesheet cannot supply.
 *
 * The HTML is complete without this file (DESIGN-POLICIES, Progressive
 * enhancement): every abstract is rendered whole and the show-more control is
 * hidden. This script folds each abstract to its excerpt and reveals the control.
 */
(function () {
  // Show more, after the reference implementation in docs/progressive-disclosure.html:
  // flip aria-expanded, hide with the `hidden` attribute, swap the label.
  // One abstract can have a hidden part before the excerpt and one after it,
  // so aria-controls is a list of ids.
  document.querySelectorAll('.ds-show-more[aria-controls]').forEach(function (toggle) {
    var folds = toggle.getAttribute('aria-controls').split(/\s+/)
      .map(function (id) { return document.getElementById(id); })
      .filter(Boolean);
    if (!folds.length) return;
    var paragraph = toggle.parentNode;
    var ellipses = paragraph.querySelectorAll('[data-ellipsis]');
    var label = toggle.querySelector('[data-label]');
    var closedLabel = toggle.getAttribute('data-closed-label');
    var openLabel = toggle.getAttribute('data-open-label');

    function set(expanded) {
      toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      folds.forEach(function (el) { el.hidden = !expanded; });
      ellipses.forEach(function (el) { el.hidden = expanded; });
      label.textContent = expanded ? openLabel : closedLabel;
    }
    toggle.addEventListener('click', function () {
      set(toggle.getAttribute('aria-expanded') !== 'true');
    });
    set(false);
    toggle.hidden = false;
  });

  // Tooltips, after the reference implementation in docs/forms.html: CSS shows
  // them on hover and focus; Escape closes one without moving focus (WCAG 1.4.13).
  document.querySelectorAll('.ds-tooltip-host').forEach(function (host) {
    var tip = host.querySelector('.ds-tooltip');
    host.addEventListener('mouseenter', function () { tip.hidden = false; });
    host.addEventListener('focusin',    function () { tip.hidden = false; });
    host.addEventListener('mouseleave', function () { tip.hidden = false; });
    host.addEventListener('focusout', function (e) {
      if (!host.contains(e.relatedTarget)) tip.hidden = false;
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.ds-tooltip-host').forEach(function (host) {
      if (host.contains(document.activeElement) || host.matches(':hover')) {
        host.querySelector('.ds-tooltip').hidden = true;
      }
    });
  });
})();
