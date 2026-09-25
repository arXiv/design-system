/* The contents bar's behaviour, added to a control that already works.
 *
 *   <script src="toc.js" defer></script>
 *
 * .ds-toc is a <details>, so it opens and closes with JavaScript off, and its
 * list is written into the HTML by verification/gen-anchors.py. This adds what
 * markup cannot: it closes on Escape, on a click outside, and when a link is
 * followed; it names the section the reader is in on the control itself; and
 * on a bar with .ds-toc-bar it marks the bar .is-stuck once it has
 * reached the top of the viewport.
 */
(function () {
  var toc = document.querySelector('.ds-toc');
  if (!toc) return;
  var trigger = toc.querySelector('.ds-toc-trigger');
  var text = toc.querySelector('.ds-toc-text');
  var links = Array.prototype.slice.call(toc.querySelectorAll('.ds-toc-menu a'));
  var bar = toc.closest('.ds-toc-bar');
  var PREFIX = text ? (text.querySelector('.ds-toc-prefix') || text).textContent.replace(/\s*·\s*$/, '') : 'Contents';

  function close(refocus) {
    if (!toc.open) return;
    toc.open = false;
    if (refocus) trigger.focus();
  }
  document.addEventListener('click', function (e) {
    if (!toc.contains(e.target)) close(false);
  });
  document.addEventListener('keydown', function (e) {
    // Focus goes back to the control only if it was inside the list we are
    // closing; otherwise Escape anywhere on the page would steal it.
    if (e.key === 'Escape') close(toc.contains(document.activeElement));
  });
  links.forEach(function (a) {
    a.addEventListener('click', function () { close(false); });
  });

  // The sections are whatever the list links to, in the order it lists them.
  var targets = links.map(function (a) {
    var el = document.getElementById((a.getAttribute('href') || '').slice(1));
    return el ? { el: el, link: a } : null;
  }).filter(Boolean);

  function label(name) {
    if (!text) return;
    text.textContent = '';
    var prefix = document.createElement('span');
    prefix.className = 'ds-toc-prefix';
    prefix.textContent = name ? PREFIX + ' ·' : PREFIX;
    text.appendChild(prefix);
    if (name) text.appendChild(document.createTextNode(' ' + (name.length > 64 ? name.slice(0, 61) + '…' : name)));
  }

  // Stuck or not is read from a 1px sentinel pinned to the bar's top edge,
  // outside the viewport exactly when the bar is held at the top. It is
  // independent of the bar's height, so the bar tightening when it sticks
  // cannot unstick it: measuring the bar itself did, and the bar flickered.
  if (bar && 'IntersectionObserver' in window) {
    var sentinel = document.createElement('span');
    sentinel.className = 'ds-toc-sentinel';
    bar.insertBefore(sentinel, bar.firstChild);
    new IntersectionObserver(function (entries) {
      bar.classList.toggle('is-stuck', !entries[0].isIntersecting && entries[0].boundingClientRect.top < 0);
    }, { threshold: 0 }).observe(sentinel);
  }

  function sync() {
    var line = window.pageYOffset + 120, current = null;
    targets.forEach(function (t) {
      if (t.el.getBoundingClientRect().top + window.pageYOffset <= line) current = t;
    });
    links.forEach(function (a) {
      a.classList.remove('is-current');
      a.removeAttribute('aria-current');
    });
    if (current) {
      current.link.classList.add('is-current');
      current.link.setAttribute('aria-current', 'location');
    }
    label(current ? current.link.textContent.replace(/\s+/g, ' ').trim() : '');
  }

  window.addEventListener('resize', sync);
  window.addEventListener('scroll', sync, { passive: true });
  sync();
})();
