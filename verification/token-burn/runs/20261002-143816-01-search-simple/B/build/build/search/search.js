/* Search page behaviour. Loaded in the head, NOT deferred: the first line puts
   `js` on <html> before first paint, so the abstract excerpt never flashes in
   the wrong state. Everything else waits for the document.
   Without this file the page is complete: each result shows its full abstract,
   and the category names are in the tooltips' text, reachable by keyboard focus. */
document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', function () {
  // Abstract: excerpt <-> full abstract. Follows the show-more pattern
  // (progressive-disclosure.html): flip aria-expanded, toggle the `hidden`
  // ATTRIBUTE on every region named in aria-controls, swap the label.
  document.querySelectorAll('.search-abstract').forEach(function (box) {
    var excerpt = box.querySelector('.search-abstract-excerpt');
    var full = box.querySelector('.search-abstract-full');
    if (!excerpt || !full) return;
    full.hidden = true;

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'ds-show-more';
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-controls', excerpt.id + ' ' + full.id);
    button.setAttribute('data-open-label', 'hide full abstract');
    var closedLabel = 'show full abstract';
    button.textContent = closedLabel;
    box.appendChild(button);

    button.addEventListener('click', function () {
      var open = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', open ? 'false' : 'true');
      excerpt.hidden = !open;
      full.hidden = open;
      button.textContent = open ? closedLabel : button.getAttribute('data-open-label');
    });
  });

  // Tooltips: CSS shows them on hover and focus; only dismissal needs script
  // (WCAG 1.4.13). Reference implementation: forms.html.
  document.querySelectorAll('.ds-tooltip-host').forEach(function (host) {
    var tip = host.querySelector('.ds-tooltip');
    host.addEventListener('mouseenter', function () { tip.hidden = false; });
    host.addEventListener('focusin',    function () { tip.hidden = false; });
    host.addEventListener('mouseleave', function () { tip.hidden = false; });
    host.addEventListener('focusout', function (e) {
      if (!host.contains(e.relatedTarget)) tip.hidden = false;
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.ds-tooltip-host').forEach(function (host) {
      if (host.contains(document.activeElement) || host.matches(':hover')) {
        host.querySelector('.ds-tooltip').hidden = true;   // focus does not move
      }
    });
  });
});
