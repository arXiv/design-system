/* Cite: a paper's citation, in the format the reader chooses — papers.html.
 *
 *   <script src="cite.js" defer></script>
 *   <script src="copy.js" defer></script>
 *
 * Include it once per page, with copy.js, which gives each format its copy
 * button. It works on every .ds-paper-cite, so a page writes no script of its own.
 *
 * Write every format into the HTML, each in a <figure data-format="…"> inside
 * .ds-paper-cite-code, with the format's name in its <figcaption> and the
 * citation in a plain <pre><code>. The select has one <option> for each
 * figure, its value the figure's data-format. After the code comes a
 * .ds-show-more that names .ds-paper-cite-code in aria-controls, with hidden
 * on it; its text is the label while the citation is closed.
 *
 * Without JavaScript every format is shown in full under its name, and the
 * stylesheet hides the select and the button. With it, only the format the
 * select names is shown; the others take the hidden attribute, so the one copy
 * button left in the Cite copies the citation the reader sees. copy.js names
 * that button from the figcaption, "Copy BibTeX", and the select keeps its own
 * label.
 *
 * The stylesheet shows the first two lines of the citation, under html.js,
 * which theme.js sets in the head. The button opens the rest: each press puts
 * .is-open on .ds-paper-cite-code or takes it off, flips aria-expanded, and
 * swaps the label between its own text and "Show less". The whole citation is
 * copied either way. Focus stays on the button.
 */
(function () {
  document.querySelectorAll('.ds-paper-cite').forEach(function (cite) {
    var select = cite.querySelector('select');
    var figures = cite.querySelectorAll('figure[data-format]');
    if (select && figures.length) {
      var show = function () {
        figures.forEach(function (f) { f.hidden = f.getAttribute('data-format') !== select.value; });
      };
      select.addEventListener('change', show);
      show();   // the browser may have restored an earlier choice on reload
    }

    var toggle = cite.querySelector('.ds-show-more');
    var code = cite.querySelector('.ds-paper-cite-code');
    if (!toggle || !code) return;
    var closedLabel = toggle.textContent;
    toggle.hidden = false;
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      code.classList.toggle('is-open', open);
      toggle.textContent = open ? 'Show less' : closedLabel;
    });
  });
})();
