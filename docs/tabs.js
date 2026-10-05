/* Tabs: turns each .ds-tabs into a tab list over its panels.
   Markup: <div class="ds-tabs" data-label="…"> holding two or more
   <section class="ds-tabs-panel">, each starting with a heading. The script
   builds one tab per panel from that heading (the WAI-ARIA tabs pattern:
   roving tabindex, arrow keys, Home and End, automatic activation) and hides
   the heading, since the tab names the panel. Without the script every panel
   shows under its own heading. */
(function () {
  document.querySelectorAll('.ds-tabs').forEach(function (box, n) {
    var panels = Array.prototype.filter.call(box.children, function (el) {
      return el.classList.contains('ds-tabs-panel');
    });
    if (panels.length < 2) return;
    var base = box.id || 'ds-tabs-' + n;
    var list = document.createElement('div');
    list.className = 'ds-tabs-list';
    list.setAttribute('role', 'tablist');
    if (box.dataset.label) list.setAttribute('aria-label', box.dataset.label);

    var tabs = panels.map(function (panel, i) {
      var heading = panel.querySelector('h2, h3, h4');
      var tab = document.createElement('button');
      tab.type = 'button';
      tab.setAttribute('role', 'tab');
      tab.id = base + '-tab-' + i;
      tab.textContent = heading ? heading.textContent.trim() : 'Tab ' + (i + 1);
      panel.id = panel.id || base + '-panel-' + i;
      tab.setAttribute('aria-controls', panel.id);
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', tab.id);
      panel.tabIndex = 0;
      if (heading) heading.hidden = true;
      list.appendChild(tab);
      return tab;
    });
    box.insertBefore(list, panels[0]);

    function select(i, focus) {
      tabs.forEach(function (tab, j) {
        var on = i === j;
        tab.setAttribute('aria-selected', on ? 'true' : 'false');
        tab.tabIndex = on ? 0 : -1;
        panels[j].hidden = !on;
      });
      if (focus) tabs[i].focus();
    }

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(i, false); });
    });
    list.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(document.activeElement);
      if (i < 0) return;
      var last = tabs.length - 1;
      var to = { ArrowRight: i === last ? 0 : i + 1, ArrowLeft: i === 0 ? last : i - 1,
                 Home: 0, End: last }[e.key];
      if (to === undefined) return;
      e.preventDefault();
      select(to, true);
    });

    // A link to something inside a panel opens that panel.
    var target = location.hash && document.getElementById(location.hash.slice(1));
    var start = target ? panels.findIndex(function (p) { return p.contains(target); }) : 0;
    select(start < 0 ? 0 : start, false);
  });
})();
