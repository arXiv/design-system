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
    // The icon is the only visible part; the state is in the accessible name,
    // and the result of a press goes to the live region.
    btn.setAttribute('aria-label', LABEL[choice] + '. Activate to change.');
  }

  document.addEventListener('DOMContentLoaded', function () {
    var buttons = document.querySelectorAll('.ds-theme-toggle');
    if (!buttons.length) return;
    var choice = read();

    buttons.forEach(function (btn) {
      if (!btn.querySelector('svg')) {
        btn.insertAdjacentHTML('beforeend',
          '<svg class="ds-theme-icon-system" viewBox="0 0 24 24" aria-hidden="true">' +
            '<circle cx="12" cy="12" r="10"/><path d="m8.5 16 3.5-8 3.5 8"/><path d="M9.9 13h4.2"/></svg>' +
          '<svg class="ds-theme-icon-light" viewBox="0 0 24 24" aria-hidden="true">' +
            '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/><path d="M12 6.5v1.3"/><path d="M12 16.2v1.3"/><path d="M6.5 12h1.3"/><path d="M16.2 12h1.3"/><path d="m8.1 8.1.9.9"/><path d="m15 15 .9.9"/><path d="m8.1 15.9.9-.9"/><path d="m15 9 .9-.9"/></svg>' +
          '<svg class="ds-theme-icon-dark" viewBox="0 0 24 24" aria-hidden="true">' +
            '<circle cx="12" cy="12" r="10"/><path d="M16.5 12.4A4.5 4.5 0 1 1 11.6 7.5a3.5 3.5 0 0 0 4.9 4.9Z"/></svg>');
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
