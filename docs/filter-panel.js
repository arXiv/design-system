/* Filter panel placement — filters.html, "Multiple-choice filters".
 *
 * A filter button's panel is a popover (popovertarget), so it opens and closes with no
 * script, and Escape closes it. A panel opens from the row its button sits in, such as the
 * site header or a card's header bar: this script hangs it from that row's bottom edge,
 * lined up with the button's left edge, or its right edge where there is no room, and
 * gives it the row's background (--ds-menu-bg). From the dark header it also gets dark
 * mode, so its text and fields read on that background. A button in no row hangs the
 * panel from its own bottom edge. The script keeps aria-expanded on the button current.
 * Without it the browser centers the panel on the page's own surface.
 */
(function () {
  var ROWS = '.ds-site-header, .ds-card-bar';

  function setUp(button) {
    var panel = document.getElementById(button.getAttribute('popovertarget'));
    if (!panel || panel.dataset.placed) return;
    panel.dataset.placed = 'true';
    var row = button.closest(ROWS);
    if (row && row.matches('.ds-site-header:not(.ds-site-header--light)')) {
      panel.setAttribute('data-theme', 'dark');
      if (button.closest('.ds-internal')) panel.classList.add('ds-internal');
    }
    function place() {
      var own = button.getBoundingClientRect();
      var width = panel.getBoundingClientRect().width;
      var left = own.left + width > window.innerWidth - 16 ? own.right - width : own.left;
      var top = row ? row.getBoundingClientRect().bottom : own.bottom;
      var ground = getComputedStyle(button).getPropertyValue('--ds-menu-bg').trim();
      if (ground) panel.style.setProperty('--ds-menu-bg', ground);
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
