// Distraction-load probe for verification/audits/audit-clicks-to-content.md
//
// Produces every machine-counted column in the "Distraction load" table:
// third-party domains, ad/tracking networks, cookies, ad slots, title
// placement, and pixel displacement.
//
// How to run: paste into the page context of an article's landing page, in an
// ordinary logged-out browser. Publisher sites refuse automated browsers, so
// this is driven through a real Chrome session rather than a headless one.
//
// Keep this file. The column is only comparable across platforms when every
// row is measured with the identical script in a single sitting. It was lost
// once, and the title-placement column had to be re-measured from scratch.

await new Promise(r => setTimeout(r, 4000)); // let the page settle; see METHODOLOGY

// --- third-party domains -----------------------------------------------
// Every distinct host contacted whose registrable domain differs from the
// page's own. Registrable domain = last two labels, or three for the
// two-part public suffixes below.
const MULTI = new Set(['co.uk','org.uk','ac.uk','gov.uk','com.au','org.au','net.au','co.jp','com.br','co.in','com.cn','co.nz','com.mx','co.za','com.sg']);
const reg = h => { const p = h.split('.'); if (p.length <= 2) return h; const l2 = p.slice(-2).join('.'); return MULTI.has(l2) ? p.slice(-3).join('.') : l2; };
const own = reg(location.hostname);
const hosts = new Set();
for (const e of performance.getEntriesByType('resource')) {
  try { const h = new URL(e.name).hostname; if (h && reg(h) !== own) hosts.add(reg(h)); } catch (_) {}
}
const domains = [...hosts].sort();

// --- ad and tracking networks ------------------------------------------
// Advertising, analytics, session-recording and consent-management services.
// Application performance monitoring (New Relic, Sentry, mPulse) and product
// analytics (Pendo) are deliberately NOT counted: they do not follow the
// reader between sites. Names are returned so the classification can be
// checked by hand.
const NET = /doubleclick|googlesyndication|googletagmanager|google-analytics|googleadservices|adservice|adsystem|adnxs|appnexus|criteo|taboola|outbrain|scorecardresearch|quantserve|quantcast|chartbeat|hotjar|fullstory|mouseflow|crazyegg|optimizely|segment\.|mixpanel|amplitude|onetrust|cookielaw|trustarc|cookiebot|adobedtm|omtrdc|demdex|everesttech|adsrvr|rubiconproject|pubmatic|openx|casalemedia|sharethrough|indexww|33across|bidswitch|smartadserver|teads|media\.net|adform|liveramp|bluekai|krxd|tiqcdn|ensighten|clarity\.ms|facebook\.net|facebook\.com|bat\.bing|moatads|doubleverify|adsafeprotected|serving-sys|flashtalking|yieldmo|gumgum|sovrn|triplelift|conversantmedia|adroll|pinterest|hubspot|marketo|pardot|drift\.com|intercom|qualtrics|cxense|parsely|permutive|piano\.io|tinypass|blueconic|lytics|treasuredata|statcounter|matomo|branch\.io|linkedin\.com|licdn|snapchat|tiktok|yandex|addthis|sharethis|gemius|nielsen|comscore|heap|kissmetric|inspectlet|smartlook|luckyorange|vwo|abtasty|dynamicyield|monetate|evergage|eloqua|sailthru|braze|iterable|appcues|walkme|usabilla|foresee|medallia|bazaarvoice/i;
const networks = domains.filter(d => NET.test(d));

// --- ad slots ----------------------------------------------------------
// A deliberately strict test: an advertising iframe, an advertising class or
// id, or an element literally labelled "Advertisement". Visible elements
// only, and nested matches collapse to their outermost ancestor.
//
// The "Advertisement" text test also matches the caption sitting BESIDE an ad,
// not just the ad itself, and the nesting filter only collapses ancestors, so
// a labelled ad was counted twice and its caption height added to the
// displacement sum. PLOS read 4 slots and 178px where the truth is 2 and 90px.
// A text-only match is therefore dropped when it sits against an element that
// matched on its class, id or iframe source — the ad is the thing with the
// markup, the caption is the thing with only the word. Captions abut their ad
// rather than overlapping it (PLOS puts one rotated down the left edge and one
// directly above), so the test allows a small margin instead of requiring
// intersection.
const visible = el => {
  const r = el.getBoundingClientRect(), s = getComputedStyle(el);
  return r.width > 0 && r.height > 0 && s.display !== 'none' && s.visibility !== 'hidden' && s.opacity !== '0';
};
const AD_CLASS = /(^|[-_ ])(ad|ads|advert|advertisement|advertising|adslot|ad-slot|ad-unit|adunit|ad-container|adcontainer|banner-ad|dfp|gpt|googlead|doubleclick)([-_ ]|$)/i;
const AD_SRC = /doubleclick|googlesyndication|adnxs|adform|criteo|amazon-adsystem|3lift|pubmatic|openx|rubicon|smartadserver|teads/i;
let slots = [], textOnly = new Set();
for (const el of document.querySelectorAll('div,section,aside,iframe,ins')) {
  if (!visible(el)) continue;
  const name = (typeof el.className === 'string' ? el.className : '') + ' ' + (el.id || '');
  const marked = (el.tagName === 'IFRAME' && AD_SRC.test(el.src || '')) || AD_CLASS.test(name);
  const labelled = /^advertisement$/i.test((el.textContent || '').trim());
  if (marked || labelled) { slots.push(el); if (labelled && !marked) textOnly.add(el); }
}
slots = slots.filter(el => !slots.some(o => o !== el && o.contains(el)));
const NEAR = 24; // px of slack; a caption abuts its ad, it does not overlap it
const adjacent = (a, b) => {
  const x = a.getBoundingClientRect(), y = b.getBoundingClientRect();
  return x.left - NEAR < y.right && x.right + NEAR > y.left
      && x.top - NEAR < y.bottom && x.bottom + NEAR > y.top;
};
slots = slots.filter(el => !textOnly.has(el) || !slots.some(o => o !== el && !textOnly.has(o) && adjacent(el, o)));

// --- title placement and pixel displacement ----------------------------
// Title placement is the paper title's distance from the top of the
// document. Every h1 is returned so the right one can be confirmed by eye
// rather than assumed. Pixel displacement is the summed height of ad slots
// sitting above the title.
const h1s = [...document.querySelectorAll('h1')].filter(visible).map(el => ({
  y: Math.round(el.getBoundingClientRect().top + scrollY),
  text: (el.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 60)
}));
const titleTop = h1s.length ? h1s[0].y : null;
let pushed = 0;
for (const el of slots) {
  const r = el.getBoundingClientRect();
  if (titleTop !== null && r.top + scrollY < titleTop) pushed += Math.round(r.height);
}

// --- cookies -----------------------------------------------------------
// Read through the prototype getter: the Claude in Chrome extension redacts
// document.cookie in returned values, so the count is computed in the page
// and only the integer leaves. Counts drift upward with repeat visits, so
// compare them within one sitting, never across days.
const jar = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie').get.call(document);

({
  url: location.href,
  viewport: innerWidth + 'x' + innerHeight, // record it; a wrong viewport invalidates title placement
  dpr: devicePixelRatio, // 2 is 100% zoom on this machine; anything else must be re-measured, not converted
  thirdParty: domains.length,
  domains,
  networks: networks.length,
  networkNames: networks,
  cookieCount: jar.split(';').filter(s => s.trim()).length,
  adSlots: slots.length,
  titleTop,
  h1s,
  pushedDownBy: pushed
})
