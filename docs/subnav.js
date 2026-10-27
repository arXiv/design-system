/* Secondary navigation that folds to fit — navigation.html, "Two levels of navigation".
 *
 * A row with a section menu (.ds-subnav-section) and its views as tabs keeps all of them
 * on one line while they fit, as header.js does for the header. Three layouts, tried in
 * order: the tabs beside the section menu; the views folded into a View menu beside it;
 * the section menu on a row of its own, with the View menu below. The script builds the
 * View menu from the row's own links, so the page writes them once. Without it the tabs
 * wrap, and every view is still a link.
 *
 * It also closes an open menu on Escape (focus returns to its summary) and on a click
 * outside it. The menus are <details>, so they open and close with no script.
 */
(function () {
  var ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M10 4v4"/><path d="M2 8h20"/><path d="M6 4v4"/></svg>';

  function setUp(row) {
    var section = row.querySelector(':scope > .ds-subnav-section');
    var views = Array.prototype.slice.call(row.querySelectorAll(':scope > a'));
    if (!section || !views.length || row.querySelector(':scope > .ds-subnav-views')) return;
    var current = row.querySelector(':scope > a[aria-current="page"]') || views[0];

    var menu = document.createElement('details');
    menu.className = 'ds-subnav-views';
    var summary = document.createElement('summary');
    summary.innerHTML = ICON + 'View: <b></b>';
    summary.querySelector('b').textContent = current.textContent;
    var list = document.createElement('div');
    list.className = 'ds-menu';
    views.forEach(function (a) {
      var link = a.cloneNode(true);
      list.appendChild(link);
    });
    menu.append(summary, list);
    row.append(menu);

    function top(el) { return el.getBoundingClientRect().top; }
    function fit() {
      row.classList.remove('is-views-folded', 'is-menu-row');
      if (top(views[views.length - 1]) - top(section) < 12) return;
      row.classList.add('is-views-folded');
      if (top(menu) - top(section) < 12) return;
      row.classList.add('is-menu-row');
    }
    new ResizeObserver(fit).observe(row);

    var menus = [section, menu];
    document.addEventListener('click', function (e) {
      menus.forEach(function (d) { if (d.open && !d.contains(e.target)) d.open = false; });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      menus.forEach(function (d) {
        if (!d.open) return;
        var inside = d.contains(document.activeElement);
        d.open = false;
        if (inside) d.querySelector('summary').focus();
      });
    });
  }

  function start() { document.querySelectorAll('.ds-subnav').forEach(setUp); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
