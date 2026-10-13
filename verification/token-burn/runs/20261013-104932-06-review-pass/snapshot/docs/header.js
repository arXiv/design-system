/* Site header: collapse by fit. Load it on any page with a .ds-site-header:

     <script src="header.js" defer></script>

   Nothing else is needed. When the bar's regions do not fit on one row, the
   navigation collapses behind a menu button; if the bar still does not fit,
   the tools region collapses behind a second button. The logo and the account
   area always stay in the bar. The script adds both buttons itself, and it
   answers to the width of the bar, not of the window, so a bar in a narrow
   column collapses too. Without the script the bar wraps onto more rows and
   nothing is hidden.

   The width each state needs is measured when the bar is set up and again
   when its content, its fonts or the small-screen breakpoint change. A resize
   only compares the bar's width against those numbers, so resizing never
   moves anything back and forth. */
(function () {
  'use strict';

  // Room a collapsed bar needs beyond the exact fit before it expands again,
  // so a scrollbar appearing or disappearing cannot flip it back.
  var SLACK = 16;
  var ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">';
  var MENU_ICON = ICON + '<path d="M4 12h16"/><path d="M4 18h16"/><path d="M4 6h16"/></svg>';
  var MORE_ICON = ICON + '<circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>' +
    '<circle cx="5" cy="12" r="1"/></svg>';
  var count = 0;

  function setUp(header) {
    var nav = header.querySelector(':scope > .ds-site-header-nav');
    var tools = header.querySelector(':scope > .ds-site-header-tools');
    if (!nav && !tools) return;
    count += 1;

    var panels = [];
    function addButton(panel, className, label, icon, suffix) {
      if (!panel.id) panel.id = 'ds-site-header-' + suffix + '-' + count;
      var button = header.querySelector(':scope > .' + className);
      if (!button) {
        button = document.createElement('button');
        button.type = 'button';
        button.className = className;
        button.innerHTML = icon + '<span class="is-sr-only">' + label + '</span>';
        header.insertBefore(button, panel);
      }
      button.setAttribute('aria-controls', panel.id);
      button.setAttribute('aria-expanded', 'false');
      var entry = { panel: panel, button: button };
      button.addEventListener('click', function () { toggle(entry); });
      panels.push(entry);
    }
    if (nav) addButton(nav, 'ds-site-header-nav-toggle', 'Menu', MENU_ICON, 'nav');
    if (tools) addButton(tools, 'ds-site-header-tools-toggle', 'Tools', MORE_ICON, 'tools');

    // Each level folds one more thing away: the greeting first, because the
    // reader already knows their own name, then the navigation, then the tools.
    var greeting = header.querySelector('.ds-site-header-greeting');
    var steps = [];
    if (greeting) steps.push('is-greeting-hidden');
    if (nav) steps.push('is-nav-collapsed');
    if (tools) steps.push('is-tools-collapsed');
    var all = [];
    for (var n = 0; n <= steps.length; n++) all.push(n);
    var levels = all;
    var state = 0;
    var need = {};

    function apply(level) {
      steps.forEach(function (cls, i) { header.classList.toggle(cls, i < level); });
    }
    function closeAll() {
      panels.forEach(function (p) {
        p.panel.classList.remove('is-open');
        p.button.setAttribute('aria-expanded', 'false');
      });
    }
    function toggle(entry) {
      var opening = !entry.panel.classList.contains('is-open');
      closeAll();
      if (opening) {
        entry.panel.classList.add('is-open');
        entry.button.setAttribute('aria-expanded', 'true');
      }
    }
    function measure() {
      header.classList.add('is-measuring');
      all.forEach(function (level) {
        apply(level);
        need[level] = Math.ceil(header.getBoundingClientRect().width);
      });
      header.classList.remove('is-measuring');
      // A step that saves no room is skipped: folding a region smaller than
      // its button away would only make the bar wider.
      levels = all.filter(function (level, i) {
        return i === 0 || need[level] < need[all[i - 1]];
      });
      if (levels.indexOf(state) < 0) state = levels[levels.length - 1];
      apply(state);
    }
    function update() {
      var room = header.getBoundingClientRect().width;
      var last = levels[levels.length - 1];
      var next = last;
      for (var i = 0; i < levels.length; i++) {
        var slack = levels[i] < state ? SLACK : 0;
        if (need[levels[i]] + slack <= room) { next = levels[i]; break; }
      }
      // Too narrow even with everything folded away: let the bar wrap.
      header.classList.toggle('is-overfull', need[last] > room);
      if (next !== state) {
        closeAll();
        state = next;
        apply(state);
      }
    }
    function refresh() { measure(); update(); }

    header.classList.add('is-collapsible');
    refresh();

    // Folding changes the bar's height, so the change waits until the observer
    // has finished; changing it inside the callback is a resize loop.
    var queued = false;
    new ResizeObserver(function () {
      if (queued) return;
      queued = true;
      setTimeout(function () { queued = false; update(); }, 0);
    }).observe(header);
    new MutationObserver(refresh).observe(header, { childList: true, subtree: true, characterData: true });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(refresh);
    window.addEventListener('load', refresh);
    var narrow = window.matchMedia('(max-width: 599px)');
    if (narrow.addEventListener) narrow.addEventListener('change', refresh);

    // Escape closes an open region. Focus goes back to its button only when it
    // was inside the region, so Escape elsewhere on the page never moves it.
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      panels.forEach(function (p) {
        if (!p.panel.classList.contains('is-open')) return;
        var inside = p.panel.contains(document.activeElement) || p.button === document.activeElement;
        p.panel.classList.remove('is-open');
        p.button.setAttribute('aria-expanded', 'false');
        if (inside) p.button.focus();
      });
    });
    document.addEventListener('click', function (e) {
      if (!header.contains(e.target)) closeAll();
    });
  }

  function start() {
    document.querySelectorAll('.ds-site-header').forEach(setUp);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
