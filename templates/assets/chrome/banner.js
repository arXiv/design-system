/* The announcement band (DESIGN-POLICIES, Banner; templates/BANNER_ANNOUNCEMENTS.md): the live
 * entry of json/announcements.json on this asset route with the latest start. Content is
 * data: text as text, a link only as an absolute https URL; anything unreadable shows
 * nothing. A dismissal is a cookie on the parent domain, keyed on the message, until 30 days
 * after its end (so an extended end does not bring it back).
 */
(function () {
  "use strict";

  var COOKIE = "arxiv_banner_dismissed_"; // + the message's key: one cookie per dismissal
  var GRACE = 30 * 24 * 60 * 60 * 1000; // a dismissal outlives its end by this

  // The asset route, from this script's own URL (…/chrome/banner.js -> …/).
  var here = document.currentScript && document.currentScript.src;
  var base = here ? here.replace(/chrome\/banner\.js.*$/, "") : "";

  function str(v) { return typeof v === "string" ? v : ""; }

  // The dismissal key: the id and the message the reader sees, hashed (FNV-1a, base 36). Any
  // edit to the text or the link is a new key; a new window is not.
  function key(a) {
    var s = [str(a.id), str(a.text), str(a.link_text), str(a.url)].join("\n");
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 0x01000193) >>> 0;
    return h.toString(36);
  }

  // Dismissed: this message's cookie, the parent domain's or, where the browser refused that,
  // this host's.
  function isDismissed(k) { return document.cookie.split("; ").indexOf(COOKIE + k + "=1") !== -1; }

  // The parent domain of this host (a.b.arxiv.org -> arxiv.org), or "" for an IP or a
  // single-label host such as localhost.
  function parentDomain() {
    var labels = location.hostname.split(".");
    if (labels.length < 2 || /^\d+$/.test(labels[labels.length - 1])) return "";
    return labels.slice(-2).join(".");
  }

  // Remember a dismissal past the message's end, in case the end is extended.
  function remember(a) {
    var k = key(a);
    var cookie = COOKIE + k + "=1; path=/; expires=" + new Date(time(a.end) + GRACE).toUTCString() +
      "; SameSite=Lax" + (location.protocol === "https:" ? "; Secure" : "");
    var domain = parentDomain();
    if (domain) document.cookie = cookie + "; domain=" + domain;
    // A browser refuses a parent domain that is a public suffix (github.io); then this host.
    if (!isDismissed(k)) document.cookie = cookie;
  }

  // A time as milliseconds, or NaN (which compares false) for anything unreadable. The
  // publish refuses a time without its offset (upload_static_assets.check_announcements).
  function time(v) { return Date.parse(str(v)); }

  // Shown: text, inside the window and not dismissed.
  function live(a, now) {
    return Boolean(a && str(a.text)) && !isDismissed(key(a)) && time(a.start) <= now && now < time(a.end);
  }

  // Of the live entries the latest start wins (an urgent notice over a long campaign); on a
  // tie, the earlier entry.
  function pick(list, now) {
    var best = null;
    for (var i = 0; i < list.length; i++) {
      if (live(list[i], now) && (!best || time(list[i].start) > time(best.start))) {
        best = list[i];
      }
    }
    return best;
  }

  // An absolute https URL on a named host, else "" (no javascript:, no relative links).
  function httpsUrl(v) {
    try {
      var url = new URL(str(v));
      return url.protocol === "https:" && url.hostname.indexOf(".") > 0 ? url.href : "";
    } catch (e) {
      return "";
    }
  }

  // The band (docs/messages.html), a landmark only while it shows (an empty one would be on
  // every page).
  function render(mount, a) {
    mount.className = "ds-announcement";
    mount.setAttribute("role", "region");
    mount.setAttribute("aria-label", "Announcement");
    mount.innerHTML =
      '<img class="ds-announcement-glyph" src="' + base + 'logos/smileybones.svg" alt="">' +
      '<span class="ds-announcement-text"></span>' +
      '<a class="ds-announcement-link"></a>' +
      '<button type="button" class="ds-close">' +
        '<svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
          '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>' +
        '</svg><span class="is-sr-only">Dismiss announcement</span></button>';

    mount.querySelector(".ds-announcement-text").textContent = str(a.text);
    var link = mount.querySelector(".ds-announcement-link");
    var href = httpsUrl(a.url);
    if (str(a.link_text) && href) {
      link.textContent = str(a.link_text);
      link.setAttribute("href", href);
    } else {
      link.remove();
    }

    mount.querySelector(".ds-close").addEventListener("click", function () {
      remember(a);
      mount.removeAttribute("role");
      mount.removeAttribute("aria-label");
      mount.className = "";
      mount.textContent = "";
      // The focused button is gone: focus goes to the header's first item, not the page's top.
      var first = document.querySelector(".ds-site-header-logo");
      if (first) first.focus();
    });
  }

  // Once per mount, as header.js: React's StrictMode runs this twice over the same markup.
  var mount = document.getElementById("ds-announcement");
  if (!mount || mount.hasAttribute("data-ds-wired") || !base || !window.fetch) return;
  mount.setAttribute("data-ds-wired", "");
  fetch(base + "json/announcements.json", { credentials: "omit" })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (feed) {
      var a = pick(feed && Array.isArray(feed.announcements) ? feed.announcements : [], Date.now());
      if (a) render(mount, a);
    })
    .catch(function () {});
})();
