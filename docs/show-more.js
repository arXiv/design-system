/* Show more: the rest of a list or a text, behind a button — progressive-disclosure.html.
 *
 *   <script src="show-more.js" defer></script>
 *
 * Include it once per page. It works on every .ds-show-more that names what it
 * reveals in aria-controls, so a page writes no script of its own.
 *
 * Write the whole text into the HTML: the tail in a .ds-show-more-tail, and the
 * button after it, with hidden on it.
 *
 *   …, L. Cheng<span id="authors-tail" class="ds-show-more-tail">, T. Okonkwo, …</span>
 *   <button type="button" class="ds-show-more" aria-expanded="false"
 *           aria-controls="authors-tail" data-open-label="show fewer" hidden>show all 22 authors</button>
 *
 * Without JavaScript the tail shows and the button does not, so nothing is lost.
 * With it, this hides the tail with the hidden attribute and shows the button.
 * The stylesheet keeps the tail closed from the first paint, under html.js,
 * which theme.js sets in the head, so a long author list does not show in full
 * and then collapse.
 *
 * Each press flips aria-expanded, swaps the label, and flips hidden on every
 * region that aria-controls names. Several ids, separated by spaces, open and
 * close together: a version list hides its ellipsis as it shows the versions
 * behind it. A region that is not a .ds-show-more-tail, such as that ellipsis,
 * shows only while the tail is closed: write it hidden, so without JavaScript
 * it does not show, and this shows it. Every region has .is-open while the
 * button is expanded.
 *
 *   data-open-label="…"     the label while open; "show fewer" if absent
 *   data-closed-label="…"   the label while closed, for a button that starts
 *                           open (aria-expanded="true"); otherwise the
 *                           button's own text
 *
 * Focus stays on the button, and its name is its label, so a screen reader
 * hears the new label with the new state.
 *
 * A Show more inside a Cite, .ds-paper-cite, belongs to cite.js: there the
 * citation is cut to its first two lines, not hidden.
 */
(function () {
  document.querySelectorAll('.ds-show-more[aria-controls]').forEach(function (toggle) {
    if (toggle.closest('.ds-paper-cite')) return;
    var regions = toggle.getAttribute('aria-controls').split(/\s+/).map(function (id) {
      return document.getElementById(id);
    }).filter(Boolean);
    if (!regions.length) return;

    var open = toggle.getAttribute('aria-expanded') === 'true';
    var closedLabel = toggle.getAttribute('data-closed-label') || toggle.textContent;
    var openLabel = toggle.getAttribute('data-open-label') || 'show fewer';

    // The tail is hidden here, not in the HTML, so without JavaScript it shows.
    regions.forEach(function (r) {
      r.hidden = r.classList.contains('ds-show-more-tail') ? !open : open;
      r.classList.toggle('is-open', open);
    });
    toggle.hidden = false;

    toggle.addEventListener('click', function () {
      open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      regions.forEach(function (r) {
        // The attribute, not a class: while hidden, the tail is out of the tab
        // order and out of find-in-page, with or without the stylesheet.
        r.hidden = !r.hidden;
        r.classList.toggle('is-open', open);
      });
      toggle.textContent = open ? openLabel : closedLabel;
    });
  });
})();
