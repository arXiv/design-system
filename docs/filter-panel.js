/* Filter panel placement — filters.html, "Multiple-choice filters".
 *
 * A filter button's panel is a popover (popovertarget), so it opens and closes with no
 * script, and Escape closes it. This script places it at the button's bottom edge, lined
 * up with the button's left edge, or its right edge where there is no room, and keeps
 * aria-expanded on the button current. In the site header the panel hangs from the
 * header's bottom edge, as the header's menus do. Without the script the browser centres
 * the panel.
 */
(function () {
  function setUp(button) {
    var panel = document.getElementById(button.getAttribute('popovertarget'));
    if (!panel || panel.dataset.placed) return;
    panel.dataset.placed = 'true';
    var header = button.closest('.ds-site-header');
    function place() {
      var own = button.getBoundingClientRect();
      var width = panel.getBoundingClientRect().width;
      var left = own.left + width > window.innerWidth - 16 ? own.right - width : own.left;
      var top = header ? header.getBoundingClientRect().bottom : own.bottom;
      panel.style.setProperty('--ds-panel-top', Math.round(top + window.scrollY) + 'px');
      panel.style.setProperty('--ds-panel-left', Math.round(Math.max(16, left) + window.scrollX) + 'px');
    }
    panel.addEventListener('toggle', function (e) {
      var open = e.newState === 'open';
      button.setAttribute('aria-expanded', String(open));
      if (open) place();
    });
    window.addEventListener('resize', function () { if (panel.matches(':popover-open')) place(); });
  }

  function start() { document.querySelectorAll('.ds-filter-button[popovertarget]').forEach(setUp); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
