/* Theme: the reader's choice, the system's, and the switch between them.
 *
 * Two parts, and they load differently on purpose.
 *
 *   <head>  <script src="theme.js"></script>          <!-- NOT defer -->
 *   <body>  ... <button class="ds-theme-toggle"></button> ...
 *
 * The attribute has to be on <html> before the first paint, or the page
 * renders light and then flips — the "flash of wrong theme", which is worst
 * for exactly the reader who chose dark because light hurts. So this file is
 * loaded WITHOUT defer in the head, does its one synchronous write, and wires
 * the button later on DOMContentLoaded.
 *
 * Three states, not two. "System" is a real state and the default, so a reader
 * who tries dark can get back to following their machine — a two-way switch
 * would lose that setting the first time it was touched.
 *
 * With no JavaScript there is no button and the page follows the OS, which is
 * the behaviour every page had before this existed. Nothing is lost.
 */
(function () {
  var KEY = 'arxiv-theme';
  var ORDER = ['system', 'light', 'dark'];
  var LABEL = {
    system: 'Theme: following the system',
    light: 'Theme: light',
    dark: 'Theme: dark'
  };
  var ANNOUNCE = {
    system: 'Theme now follows the system setting',
    light: 'Theme is now light',
    dark: 'Theme is now dark'
  };

  function read() {
    try {
      var v = localStorage.getItem(KEY);
      return ORDER.indexOf(v) > -1 ? v : 'system';
    } catch (e) {
      // Private windows and blocked site data throw on access, not on write.
      return 'system';
    }
  }

  function apply(choice) {
    var root = document.documentElement;
    if (choice === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', choice);
  }

  // ── Before first paint ──
  apply(read());

  // ── The control ──
  function paint(btn, choice) {
    btn.setAttribute('data-theme-choice', choice);
    // The label is the state, in words. An icon alone leaves the reader
    // guessing whether the moon means "it is dark" or "make it dark".
    btn.querySelector('.ds-theme-toggle-label').textContent =
      choice === 'system' ? 'System' : choice === 'light' ? 'Light' : 'Dark';
    btn.setAttribute('aria-label', LABEL[choice] + '. Activate to change.');
  }

  document.addEventListener('DOMContentLoaded', function () {
    var buttons = document.querySelectorAll('.ds-theme-toggle');
    if (!buttons.length) return;
    var choice = read();

    buttons.forEach(function (btn) {
      if (!btn.querySelector('.ds-theme-toggle-label')) {
        btn.insertAdjacentHTML('beforeend',
          '<svg class="ds-theme-icon-system" viewBox="0 0 24 24" aria-hidden="true">' +
            '<rect x="2" y="4" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 18v3"/></svg>' +
          '<svg class="ds-theme-icon-light" viewBox="0 0 24 24" aria-hidden="true">' +
            '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m5 5 1.5 1.5"/>' +
            '<path d="M17.5 17.5 19 19"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m5 19 1.5-1.5"/>' +
            '<path d="M17.5 6.5 19 5"/></svg>' +
          '<svg class="ds-theme-icon-dark" viewBox="0 0 24 24" aria-hidden="true">' +
            '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>' +
          '<span class="ds-theme-toggle-label"></span>');
      }
      paint(btn, choice);

      btn.addEventListener('click', function () {
        choice = ORDER[(ORDER.indexOf(choice) + 1) % ORDER.length];
        try { localStorage.setItem(KEY, choice); } catch (e) { /* choice holds for this page */ }
        apply(choice);
        document.querySelectorAll('.ds-theme-toggle').forEach(function (b) { paint(b, choice); });
        // Announce the result. The button's own name is what it does, and that
        // did not change — the same rule as the copy button.
        var status = document.getElementById('ds-theme-status');
        if (status) status.textContent = ANNOUNCE[choice];
      });
    });
  });

  // While the choice is "system", follow the machine if it changes underneath.
  try {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
      if (read() === 'system') apply('system');
    });
  } catch (e) { /* older engines: the initial read still applied */ }
})();
