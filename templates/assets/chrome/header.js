/* The brand header's behaviour (templates/README.md, Template rules). Vanilla JS.
 *  - Search: the Search link opens the in-page overlay (without JS it navigates); Escape,
 *    a click on the scrim or focus moving out of it closes it; Ctrl/Cmd+K opens it, except
 *    while typing in a field.
 *  - Phone nav: adds .is-collapsible and wires the hamburger, so it shows only when it
 *    works (without JS the nav wraps). A host that drives the toggle itself marks it
 *    data-host-nav before this deferred script runs (arxiv-docs).
 *  - Member acknowledgement: fills an empty, hidden .ack-member-inline from the
 *    same-origin /institutional_banner, cached for 30 days (an hour after a failure).
 */
(function () {
  "use strict";

  // Once per header: a host may run this again over the same markup (React's StrictMode runs
  // effects twice), and a second set of handlers would undo every click. A host that renders
  // a new header (a React remount) runs it again for the new one, and the page-level handlers
  // of the old one stand down: it is no longer in the page.
  var header = document.querySelector(".ds-site-header");
  if (!header || header.hasAttribute("data-ds-wired")) return;
  header.setAttribute("data-ds-wired", "");
  function current() { return header.isConnected; }

  var toggle = document.getElementById("ds-search-toggle");
  var overlay = document.getElementById("ds-search-overlay");
  var input = document.getElementById("ds-search-input");
  var navToggle = document.getElementById("ds-nav-toggle");
  var nav = document.getElementById("ds-site-header-nav");
  var ownsNav = navToggle && nav && !navToggle.hasAttribute("data-host-nav");

  function shown(el) { return Boolean(el && el.getClientRects().length); }

  // Closing returns focus to the Search link (to the hamburger while the phone menu hides it),
  // unless focus is already going elsewhere.
  function setOverlay(open, refocus) {
    if (!overlay) return;
    overlay.hidden = !open;
    if (toggle) toggle.setAttribute("aria-expanded", String(open));
    if (open && input) setTimeout(function () { input.focus(); }, 50);
    if (!open && refocus !== false) {
      var back = shown(toggle) ? toggle : shown(navToggle) ? navToggle : null;
      if (back) back.focus();
    }
  }

  if (toggle && overlay) {
    toggle.addEventListener("click", function (e) { e.preventDefault(); setOverlay(true); });
    overlay.addEventListener("click", function (e) { if (e.target === overlay) setOverlay(false); });
    // Tab past its last link lands behind the scrim: close it, as a disclosure would.
    document.addEventListener("focusin", function (e) {
      if (current() && !overlay.hidden && !overlay.contains(e.target)) setOverlay(false, false);
    });
  }

  function setNav(open) {
    nav.classList.toggle("is-open", open);
    navToggle.setAttribute("aria-expanded", String(open));
    navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }

  if (ownsNav) {
    header.classList.add("is-collapsible");
    navToggle.addEventListener("click", function (e) {
      e.stopPropagation();
      setNav(!nav.classList.contains("is-open"));
    });
    document.addEventListener("click", function (e) {
      if (current() && nav.classList.contains("is-open") && !nav.contains(e.target)) setNav(false);
    });
  }

  // Ctrl/Cmd+K is the host's while the reader types (an editor's "insert link").
  function typing(el) {
    return el.isContentEditable || el.tagName === "TEXTAREA" || (el.tagName === "INPUT" &&
      !/^(checkbox|radio|button|submit|reset|range|color|file|image)$/.test(el.type));
  }

  document.addEventListener("keydown", function (e) {
    if (!current()) return;
    if (e.key === "Escape") {
      if (overlay && !overlay.hidden) setOverlay(false);
      else if (ownsNav && nav.classList.contains("is-open")) { setNav(false); navToggle.focus(); }
    } else if ((e.metaKey || e.ctrlKey) && !e.shiftKey && !e.altKey && (e.key === "k" || e.key === "K") &&
               overlay && !e.defaultPrevented && !typing(e.target)) {
      e.preventDefault();
      setOverlay(true);
    }
  });

  var ack = document.querySelector(".ack-member-inline[hidden]");
  var name = ack && ack.querySelector("strong");
  if (!name || name.textContent.trim() || !window.fetch) return;

  var KEY = "arxiv_member_label";
  var DAY = 24 * 60 * 60 * 1000;
  function remember(label, days) {
    try { localStorage.setItem(KEY, JSON.stringify({ label: label, expires: Date.now() + days * DAY })); } catch (e) {}
    return label;
  }
  var cached = null;
  try { cached = JSON.parse(localStorage.getItem(KEY)); } catch (e) {}

  (cached && Date.now() < cached.expires
    ? Promise.resolve(cached.label)
    : fetch("/institutional_banner")
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (j) { return j ? remember(j.label || null, 30) : remember(null, 1 / 24); })
        .catch(function () { return remember(null, 1 / 24); })
  ).then(function (label) {
    if (label) { name.textContent = label; ack.hidden = false; }
  });
})();
