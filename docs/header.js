/* Site header: collapse by fit. Load it on any page with a .ds-site-header:

     <script src="header.js" defer></script>

   Nothing else is needed. When the bar's regions do not fit on one row, the
   greeting goes first, then the navigation collapses behind a menu button.
   On a public bar with an account area, the tools and the account area go
   into the same menu, so the bar keeps only the logo, Search and the menu
   button. An internal bar (inside .ds-internal) keeps its tools and account
   area while they fit; at its last fold its search fields go behind a Search
   button and everything else into the menu. On a bar with no navigation the
   tools collapse behind a second button. The script adds the buttons itself,
   and it answers to the width of the bar, not of the window, so a bar in a narrow
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
  var SEARCH_ICON = ICON + '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>';
  var count = 0;

  function setUp(header) {
    var nav = header.querySelector(':scope > .ds-site-header-nav');
    var tools = header.querySelector(':scope > .ds-site-header-tools');
    var account = header.querySelector(':scope > .ds-site-header-account');
    if (!nav && !tools) return;
    count += 1;

    // A public bar with an account area has one menu from its first fold: it
    // holds the navigation, then the tools, then the account area, each region
    // keeping its own element. An internal bar gets the same menu at its last
    // fold, with its search fields behind a Search button of their own.
    var internal = !!header.closest('.ds-internal');
    var single = !!(nav && account) && !internal;
    var foldsAll = !!nav && internal;
    var fields = tools && tools.querySelector(':scope > .ds-site-header-search');

    function name(region, suffix) {
      if (region && !region.id) region.id = 'ds-site-header-' + suffix + '-' + count;
    }
    name(nav, 'nav');
    name(tools, 'tools');
    name(account, 'account');

    var entries = [];
    function addButton(regions, className, label, icon, before) {
      var button = header.querySelector(':scope > .' + className);
      if (!button) {
        button = document.createElement('button');
        button.type = 'button';
        button.className = className;
        button.innerHTML = icon + '<span class="is-sr-only">' + label + '</span>';
        header.insertBefore(button, before);
      }
      button.setAttribute('aria-expanded', 'false');
      var entry = { regions: regions, button: button };
      button.addEventListener('click', function () { toggle(entry); });
      entries.push(entry);
      return entry;
    }
    function inMenu() {
      return header.classList.contains('is-single-menu') ? [nav, tools, account].filter(Boolean) : [nav];
    }
    var menu = nav && addButton(inMenu, 'ds-site-header-nav-toggle', 'Menu', MENU_ICON, nav);
    var search = null;
    if (tools && !single) {
      if (!foldsAll) addButton(function () { return [tools]; }, 'ds-site-header-tools-toggle', 'Tools', MORE_ICON, tools);
      else if (fields) search = addButton(function () { return [tools]; }, 'ds-site-header-tools-toggle', 'Search', SEARCH_ICON, menu.button);
    }

    // Each level folds one more thing away: the greeting first, because the
    // reader already knows their own name, then the navigation (on a public
    // bar, with the tools and the account area), then the tools (on an
    // internal bar, with the account area).
    var greeting = header.querySelector('.ds-site-header-greeting');
    var steps = [];
    if (greeting) steps.push('is-greeting-hidden');
    if (nav) steps.push('is-nav-collapsed');
    if (tools && !single) steps.push('is-tools-collapsed');
    var all = [];
    for (var n = 0; n <= steps.length; n++) all.push(n);
    var levels = all;
    var state = 0;
    var need = {};

    function apply(level) {
      steps.forEach(function (cls, i) { header.classList.toggle(cls, i < level); });
      header.classList.toggle('is-single-menu', single || (foldsAll && level === steps.length));
      entries.forEach(function (entry) {
        entry.button.setAttribute('aria-controls', entry.regions().map(function (r) { return r.id; }).join(' '));
      });
    }
    function setOpen(entry, open) {
      entry.regions().forEach(function (r) { r.classList.toggle('is-open', open); });
      entry.button.setAttribute('aria-expanded', String(open));
      if (entry === menu) header.classList.toggle('is-menu-open', open && header.classList.contains('is-single-menu'));
      if (open && entry === search) setTimeout(function () { fields.querySelector('input').focus(); }, 0);
    }
    function closeAll() {
      entries.forEach(function (entry) { setOpen(entry, false); });
    }
    function toggle(entry) {
      var opening = entry.button.getAttribute('aria-expanded') !== 'true';
      closeAll();
      if (opening) setOpen(entry, true);
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
      entries.forEach(function (entry) {
        if (entry.button.getAttribute('aria-expanded') !== 'true') return;
        var inside = entry.button === document.activeElement ||
          entry.regions().some(function (r) { return r.contains(document.activeElement); });
        setOpen(entry, false);
        if (inside) entry.button.focus();
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
