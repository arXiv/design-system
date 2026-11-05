/* Copying, with the same feedback everywhere — action-feedback.html.
 *
 *   <script src="copy.js" defer></script>
 *
 * Include it once per page. It does two things.
 *
 * Every code block gets a copy button. Write code blocks the way you already do,
 * <pre><code>...</code></pre>: no wrapper, no button, no per-block markup — which is
 * the point. A block that needs remembering is a block someone forgets. This walks
 * every <pre> on the page, so one that gets added later is covered without being
 * touched. Opt a block out with <pre data-no-copy>.
 *
 * Any other button copies with one attribute and gets the same feedback:
 *
 *   data-copy="text"          copies that text
 *   data-copy-link="#id"      copies this page's address with that fragment
 *   data-copy-from="id"       copies that element's text; an equation's MathML
 *   data-copied="…"           what a screen reader hears, such as "Link to
 *                             equation 2.14 copied"; "Copied to clipboard" if absent
 *   data-copy-failed="…"      what to do instead if the copy fails
 *
 * The button holds its own icon and a tick, <svg class="ds-copy-done">. After a copy
 * the tick takes the icon's place and a status region says what was copied; both
 * clear after two seconds. Focus and the button's name stay as they were.
 *
 * With no JavaScript there is no copy button on a code block and the code is still
 * selectable, so nothing is lost; the button is an enhancement, never the only way
 * to copy.
 *
 * A block wider than its box scrolls sideways, and a keyboard can only scroll
 * what it can focus. So every block that overflows, opted out or not, joins
 * the tab order, and leaves it again when the window is wide enough to show it.
 */
(function () {
  function reachable(pre) {
    if (pre.hasAttribute('tabindex') && !pre.hasAttribute('data-ds-scroll')) return;   // the author's own
    if (pre.scrollWidth > pre.clientWidth) {
      pre.setAttribute('tabindex', '0');
      pre.setAttribute('data-ds-scroll', '');
    } else {
      pre.removeAttribute('tabindex');
      pre.removeAttribute('data-ds-scroll');
    }
  }
  var blocks = document.querySelectorAll('pre');
  if ('ResizeObserver' in window) {
    var watcher = new ResizeObserver(function (entries) {
      entries.forEach(function (entry) { reachable(entry.target); });
    });
    blocks.forEach(function (pre) { watcher.observe(pre); });
  } else {
    blocks.forEach(reachable);
  }

  // Two overlapping sheets, then a tick. aria-hidden on both: the button's
  // name comes from aria-label and never changes, because its action never
  // changes — what changed is the result, and that goes to the live region.
  var ICONS =
    '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<rect x="9" y="9" width="12" height="12" rx="2"/>' +
      '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>' +
    '</svg>' +
    '<svg class="ds-copy-done" viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="m20 6-11 11-5-5"/>' +
    '</svg>';

  // The async clipboard is the right API and the wrong one to rely on alone:
  // it needs a secure context, which file:// is not, and it rejects when the
  // document is not focused. So it is tried first and execCommand catches
  // every way it can fail, rather than only the one where it is missing.
  function legacyWrite(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:-1000px;opacity:0';
    document.body.appendChild(ta);
    var back = document.activeElement;   // select() moves focus; it goes back to the button
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    if (back && back.focus) back.focus();
    return ok ? Promise.resolve() : Promise.reject();
  }

  function write(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).catch(function () {
        return legacyWrite(text);
      });
    }
    return legacyWrite(text);
  }

  // The tick for two seconds, and the words in a status region. A second copy
  // within the two seconds starts them again rather than stacking timers; a
  // failure takes down a tick still showing from the copy before.
  function failed(btn, status, message) {
    clearTimeout(btn.dsCopyTimer);
    btn.classList.remove('is-done');
    status.textContent = message;
  }
  function done(btn, status, message) {
    btn.classList.add('is-done');
    status.textContent = message;
    clearTimeout(btn.dsCopyTimer);
    btn.dsCopyTimer = setTimeout(function () {
      btn.classList.remove('is-done');
      if (status.textContent === message) status.textContent = '';
    }, 2000);
  }

  // The button's own label changing is not reliably announced, so the result
  // goes to a live region that exists only for that. It is in the page before
  // anything is written to it, or the first message can go unheard.
  function region() {
    var status = document.createElement('span');
    status.className = 'is-sr-only';
    status.setAttribute('role', 'status');
    return status;
  }

  document.querySelectorAll('pre').forEach(function (pre) {
    if (pre.hasAttribute('data-no-copy') || pre.closest('.ds-code')) return;

    var wrap = document.createElement('div');
    wrap.className = 'ds-code';
    pre.parentNode.insertBefore(wrap, pre);
    wrap.appendChild(pre);

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'ds-code-copy';
    btn.innerHTML = ICONS;
    // A block in a figure is named by its caption: "Copy BibTeX", not "Copy code".
    var caption = pre.closest('figure') && pre.closest('figure').querySelector('figcaption');
    btn.setAttribute('aria-label', caption ? 'Copy ' + caption.textContent.trim() : 'Copy code');
    btn.title = 'Copy';       // the pointer affordance; assistive technology
                              // takes aria-label and ignores this
    var status = region();
    wrap.appendChild(btn);
    wrap.appendChild(status);

    btn.addEventListener('click', function () {
      var code = pre.querySelector('code') || pre;
      write(code.innerText || code.textContent).then(   // innerText keeps the line breaks as shown
        function () { done(btn, status, 'Copied to clipboard'); },
        function () { failed(btn, status, 'Copy failed — select the code and copy it manually'); }
      );
    });
  });

  // Every other copy button. One listener on the document, in the capture
  // phase, so a button another script adds later is covered, and a script that
  // stops the click from bubbling, as anchors.js does, cannot stop the copy.
  var page = region();
  document.body.appendChild(page);
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('[data-copy], [data-copy-link], [data-copy-from]');
    if (!btn) return;
    var text, otherwise;
    if (btn.hasAttribute('data-copy-link')) {
      text = location.href.split('#')[0] + btn.getAttribute('data-copy-link');
      otherwise = 'Copy failed — the address is ' + text;
    } else if (btn.hasAttribute('data-copy-from')) {
      var from = document.getElementById(btn.getAttribute('data-copy-from'));
      if (!from) return;
      var math = from.matches('math') ? from : from.querySelector('math');
      text = math ? math.outerHTML : from.innerText;
    } else {
      text = btn.getAttribute('data-copy');
    }
    otherwise = btn.getAttribute('data-copy-failed') || otherwise || 'Copy failed — select the text and copy it manually';
    write(text).then(
      function () { done(btn, page, btn.getAttribute('data-copied') || 'Copied to clipboard'); },
      function () { failed(btn, page, otherwise); }
    );
  }, true);
})();
