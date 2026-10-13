/* Tooltips: CSS shows .ds-tooltip on hover and on focus. This script does the
   two things CSS cannot.
   1. Escape closes the tooltip without moving focus (WCAG 1.4.13). Arriving
      at or leaving the host clears the dismissal, so the next visit shows it.
   2. A bubble that would run off either edge of the screen slides back onto
      it, so a host whose position cannot be known in advance (a tag in a row
      that wraps) never makes the page scroll sideways.
   Without the script the tooltip still shows, opening toward the inline end. */
(function () {
  var MARGIN = 8;
  // Measured from where the bubble opens, then slid back just far enough to
  // stay on screen, never past the opposite edge.
  function place(tip) {
    tip.style.removeProperty('--ds-tooltip-shift');
    var r = (tip.querySelector('.ds-tooltip-body') || tip).getBoundingClientRect();
    var vw = document.documentElement.clientWidth;
    var shift = 0;
    if (r.right > vw - MARGIN) shift = -Math.min(r.right - (vw - MARGIN), r.left - MARGIN);
    else if (r.left < MARGIN) shift = Math.min(MARGIN - r.left, (vw - MARGIN) - r.right);
    if (shift) tip.style.setProperty('--ds-tooltip-shift', Math.round(shift) + 'px');
  }
  document.querySelectorAll('.ds-tooltip-host').forEach(function (host) {
    var tip = host.querySelector('.ds-tooltip');
    if (!tip) return;
    function show() { tip.hidden = false; place(tip); }
    host.addEventListener('mouseenter', show);
    host.addEventListener('focusin', show);
    host.addEventListener('mouseleave', function () { tip.hidden = false; });
    host.addEventListener('focusout', function (e) {
      if (!host.contains(e.relatedTarget)) tip.hidden = false;
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.ds-tooltip-host').forEach(function (host) {
      if (host.contains(document.activeElement) || host.matches(':hover')) {
        host.querySelector('.ds-tooltip').hidden = true;   // focus does NOT move
      }
    });
  });
})();
