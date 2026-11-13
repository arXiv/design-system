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
 * Write such a button hidden: it does nothing without this script, which shows
 * it. A Permalink is a link to its #id instead, <a href="#S2" data-copy-link="#S2">,
 * so without the script it still goes to the section; with it, a press copies
 * the link and the page stays where it is.
 *
 * The button holds its own icon and a tick, <svg class="ds-copy-done">. After a copy
 * the tick takes the icon's place and a status region says what was copied; both
 * clear after two seconds. Focus and the button's name stay as they were.
 *
 * If the copy fails, an alert takes the icon's place, the status region says so,
 * and a line under the control, .ds-copy-failed-message, says what to do instead.
 * Both stay until the button is pressed again. A link that could not be copied is
 * put in the address bar, where people already copy links from.
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

  // The error alert's icon. It is added the first time a copy fails, so no
  // button's markup has to carry it, and it carries its own stroke because
  // it can land in any button.
  var ALERT =
    '<svg class="ds-copy-failed" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      '<path d="M12 16h.01"/><path d="M12 8v4"/>' +
      '<path d="M15.312 2a2 2 0 0 1 1.414.586l4.688 4.688A2 2 0 0 1 22 8.688v6.624a2 2 0 0 1-.586 1.414l-4.688 4.688a2 2 0 0 1-1.414.586H8.688a2 2 0 0 1-1.414-.586l-4.688-4.688A2 2 0 0 1 2 15.312V8.688a2 2 0 0 1 .586-1.414l4.688-4.688A2 2 0 0 1 8.688 2z"/>' +
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

  // The line goes where a field's error goes, under the control's line: under
  // the code block, paper element, heading or paragraph that holds the button.
  // Where none does, or the one that does is wider than what the button links
  // to or copies from, it goes under that instead: a paragraph whose
  // Permalink sits in its margin. Failing both, it goes under the nearest
  // block in the text, past a row that floats on an element's edge. A button
  // in the margin, beside that block rather than over it, keeps the line
  // under itself, as wide as the margin allows.
  function place(btn, line) {
    var id = (btn.getAttribute('data-copy-link') || '').replace(/^#/, '') || btn.getAttribute('data-copy-from');
    var target = id && document.getElementById(id);
    var block = btn.closest('.ds-code, .ds-paper-element, h1, h2, h3, h4, h5, h6, p, li');
    if (target && target.contains(btn) && (!block || block.contains(target))) block = target;
    if (!block) {
      block = btn.parentElement;
      while (block && block !== document.body && /^(absolute|fixed)$/.test(window.getComputedStyle(block).position)) block = block.parentElement;
      if (block === document.body) block = null;
    }
    var after = btn;
    if (block) {
      var b = btn.getBoundingClientRect(), r = block.getBoundingClientRect();
      if (b.right <= r.left || b.left >= r.right) {
        line.style.width = 'min(12rem, ' + Math.floor(b.right <= r.left ? b.right - 16 : window.innerWidth - b.left - 16) + 'px)';
      } else if (block.matches('p, li')) {
        block.appendChild(line);
        return;
      } else {
        after = block;
        // Under a heading, the line takes over the heading's space below it,
        // so it sits against the heading rather than midway to what follows.
        if (/^H[1-6]$/.test(block.tagName)) {
          var below = parseFloat(window.getComputedStyle(block).marginBottom) || 0;
          line.style.margin = 'calc(var(--ds-space-1) - ' + below + 'px) 0 ' + below + 'px';
        }
      }
    }
    // After any line already there, so two lines keep the order of the presses.
    while (after.nextElementSibling && after.nextElementSibling.classList.contains('ds-copy-failed-message')) after = after.nextElementSibling;
    after.insertAdjacentElement('afterend', line);
  }

  // Pressing the button again takes down a failure, whatever happens next.
  function reset(btn) {
    btn.classList.remove('is-failed');
    var keep = (btn.getAttribute('aria-describedby') || '').split(' ').filter(function (id) {
      var line = id && document.getElementById(id);
      if (line && line.classList.contains('ds-copy-failed-message')) { line.remove(); return false; }
      return Boolean(id);
    });
    if (keep.length) btn.setAttribute('aria-describedby', keep.join(' '));
    else btn.removeAttribute('aria-describedby');
  }

  // A failure stays until the button is pressed again: the alert in the
  // icon's place, and the line, which also describes the button, so someone
  // who comes back to it with a screen reader hears what went wrong. A failure
  // takes down a tick still showing from the copy before.
  var lines = 0;
  function failed(btn, status, message) {
    clearTimeout(btn.dsCopyTimer);
    btn.classList.remove('is-done');
    status.textContent = message;
    if (!btn.querySelector('svg.ds-copy-failed')) {
      var tick = btn.querySelector('svg.ds-copy-done');
      if (tick) tick.insertAdjacentHTML('afterend', ALERT);
      else btn.insertAdjacentHTML('afterbegin', ALERT);
    }
    btn.classList.add('is-failed');
    var line = document.createElement('span');
    line.className = 'ds-copy-failed-message';
    line.id = 'ds-copy-failed-' + (++lines);
    line.textContent = message;
    place(btn, line);
    btn.setAttribute('aria-describedby', ((btn.getAttribute('aria-describedby') || '') + ' ' + line.id).trim());
  }

  // The tick for two seconds, and the words in a status region. A second copy
  // within the two seconds starts them again rather than stacking timers.
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
      reset(btn);
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
  document.querySelectorAll('button[hidden]:is([data-copy], [data-copy-link], [data-copy-from])').forEach(function (b) { b.hidden = false; });
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('[data-copy], [data-copy-link], [data-copy-from]');
    if (!btn) return;
    if (btn.tagName === 'A') e.preventDefault();   // a Permalink copies; without this script it goes to the section
    reset(btn);
    var text, otherwise, link = btn.hasAttribute('data-copy-link');
    if (link) {
      text = location.href.split('#')[0] + btn.getAttribute('data-copy-link');
      otherwise = 'Copy failed — copy the link from the address bar';
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
      function () {
        // The link goes in the address bar without moving the page or adding
        // a step to Back. Where the browser refuses that, as some do for a
        // file:// page, going to the fragment puts it there instead.
        if (link) {
          try { history.replaceState(history.state, '', text); } catch (e) { location.replace(text); }
        }
        failed(btn, page, otherwise);
      }
    );
  }, true);
})();
