/* Copy button on every code block.
 *
 * Include it once per page and write code blocks the way you already do:
 *
 *   <pre><code>...</code></pre>
 *   <script src="copy-code.js" defer></script>
 *
 * No wrapper, no button, no per-block markup — which is the point. A block
 * that needs remembering is a block someone forgets. This walks every <pre>
 * on the page, so one that gets added later is covered without being touched.
 *
 * With no JavaScript there is no button and the code is still selectable, so
 * nothing is lost; the button is an enhancement, never the only way to copy.
 *
 * Opt a block out with <pre data-no-copy>.
 */
(function () {
  // Two overlapping sheets, then a tick. aria-hidden on both: the button's
  // name comes from aria-label and never changes, because its action never
  // changes — what changed is the result, and that goes to the live region.
  var ICONS =
    '<svg class="ds-code-copy-idle" viewBox="0 0 24 24" aria-hidden="true">' +
      '<rect x="9" y="9" width="12" height="12" rx="2"/>' +
      '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>' +
    '</svg>' +
    '<svg class="ds-code-copy-done" viewBox="0 0 24 24" aria-hidden="true">' +
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
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
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
    btn.setAttribute('aria-label', 'Copy code');
    btn.title = 'Copy';       // the pointer affordance; assistive technology
                              // takes aria-label and ignores this

    // The button's own label changing is not reliably announced, so the
    // result goes to a live region that exists only for that.
    var status = document.createElement('span');
    status.className = 'is-sr-only';
    status.setAttribute('role', 'status');

    wrap.appendChild(btn);
    wrap.appendChild(status);

    var timer;
    btn.addEventListener('click', function () {
      write(pre.querySelector('code') ? pre.querySelector('code').innerText : pre.innerText)
        .then(function () {
          btn.classList.add('is-done');
          status.textContent = 'Copied to clipboard';
          clearTimeout(timer);
          timer = setTimeout(function () {
            btn.classList.remove('is-done');
            status.textContent = '';
          }, 2000);
        })
        .catch(function () {
          status.textContent = 'Copy failed — select the code and copy it manually';
        });
    });
  });
})();
