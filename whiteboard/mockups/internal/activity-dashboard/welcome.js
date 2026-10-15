// Mockup only: the welcome dialog that asks for the reader's subject group.
// It cannot be closed without submitting, and it accepts whatever is chosen.
// It shows once per browser session, and again after a page refresh, so testers
// can see it as often as they need.
(function () {
  var dialog = document.getElementById('welcome');
  if (!dialog) return;
  var KEY = 'activity-dashboard-group';

  function read() { try { return sessionStorage.getItem(KEY); } catch (e) { return null; } }
  function write(v) { try { sessionStorage.setItem(KEY, v); } catch (e) {} }
  function forget() { try { sessionStorage.removeItem(KEY); } catch (e) {} }

  // Show the chosen group in the filter bar and in the page heading.
  function apply(group) {
    var select = document.getElementById('f-group');
    if (select) select.value = group;
    document.querySelectorAll('[data-group-name]').forEach(function (el) { el.textContent = group; });
  }

  var nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
  if (nav && nav.type === 'reload') forget();

  var chosen = read();
  if (chosen) { apply(chosen); return; }

  var submitted = false;
  dialog.addEventListener('cancel', function (e) { e.preventDefault(); });
  // Browsers let a second Escape close a dialog even when the first was refused; open it again.
  dialog.addEventListener('close', function () { if (!submitted) dialog.showModal(); });
  dialog.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();
    var group = dialog.querySelector('select').value;
    write(group);
    apply(group);
    submitted = true;
    dialog.close();
  });
  dialog.showModal();
})();
