/* One tab stop per element pill; the arrow keys move between its actions.
 *
 *   <div class="ds-element-pill" role="toolbar" aria-label="Equation 2.14">…</div>
 *   <script src="element-pill.js" defer></script>
 *
 * Without this script every action is its own tab stop, which still works.
 */
(function () {
  function actions(pill) {
    return Array.prototype.slice.call(pill.querySelectorAll(':scope > button, :scope > a[href]'))
      .filter(function (el) { return !el.disabled; });
  }

  document.querySelectorAll('.ds-element-pill').forEach(function (pill) {
    var items = actions(pill);
    if (items.length < 2) return;
    // The action last used keeps the tab stop, so Tab returns the reader to it.
    items.forEach(function (el, i) { el.tabIndex = i === 0 ? 0 : -1; });

    pill.addEventListener('keydown', function (e) {
      var items = actions(pill);
      var i = items.indexOf(document.activeElement);
      if (i < 0) return;
      var next = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') next = items[(i + 1) % items.length];
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') next = items[(i - 1 + items.length) % items.length];
      else if (e.key === 'Home') next = items[0];
      else if (e.key === 'End') next = items[items.length - 1];
      if (!next) return;
      e.preventDefault();
      items[i].tabIndex = -1;
      next.tabIndex = 0;
      next.focus();
    });
  });
})();
