// Both hosts paint the chrome and run its scripts without errors (React's under StrictMode,
// which runs them twice); the phone menu, the search overlay's focus and shortcut, a remount
// and printing work. The banner: the shared announcements file (served per test,
// so the tests do not depend on what the real file holds), its windows, the latest-start rule,
// dismissals (per message, across sites, focus kept), that the file is only data, and a
// landmark only while shown.
const { test, expect } = require("@playwright/test");

const ONE = "http://one.brand.test:5001";
const TWO = "http://two.brand.test:5001";
const FEED = "**/assets/json/announcements.json";
const COOKIE = "arxiv_banner_dismissed_";
const HOUR = 60 * 60 * 1000;
const DAY = 24 * HOUR;
const at = (offset) => new Date(Date.now() + offset).toISOString();
const banner = (page) => page.locator("#ds-announcement.ds-announcement");
const landmark = (page) => page.getByRole("region", { name: "Announcement" });

// What the file holds unless a test serves its own: one live announcement.
const SHARED = { id: "shared", text: "Shared news", link_text: "Read more",
                 url: "https://info.example.org/news", start: at(-HOUR), end: at(HOUR) };
const serve = (...announcements) => (route) => route.fulfill({ json: { announcements } });

test.beforeEach(async ({ context }) => {
  await context.route(FEED, serve(SHARED));
});

// Load a page and let banner.js fetch the file and draw (or not).
const open = (page, url) => page.goto(url, { waitUntil: "networkidle" });

// The band's text ("" for none) with the file answered by `answer`, a route handler.
async function bannerWith(page, answer, url = `${ONE}/jinja`) {
  await page.route(FEED, answer);
  await open(page, url);
  await expect(page.locator(".ds-site-header")).toBeVisible();
  const text = (await banner(page).count()) ? await banner(page).locator(".ds-announcement-text").innerText() : "";
  await page.unroute(FEED);
  return text;
}

function collectErrors(page) {
  const errors = [];
  page.on("console", (m) => m.type() === "error" && errors.push(m.text()));
  page.on("pageerror", (e) => errors.push(String(e)));
  return errors;
}

function feedRequests(page) {
  const seen = [];
  page.on("request", (r) => r.url().endsWith("/json/announcements.json") && seen.push(r.url()));
  return seen;
}

test("Jinja host: the chrome paints and header.js opens the search overlay", async ({ page }) => {
  const errors = collectErrors(page);
  await open(page, `${ONE}/jinja`);
  await expect(page.locator(".ds-site-header")).toBeVisible();
  await expect(page.getByRole("link", { name: "Log in" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Accessibility" })).toBeVisible();
  await expect(banner(page)).toContainText("Shared news");
  await page.locator("#ds-search-toggle").click();
  await expect(page.locator("#ds-search-overlay")).toBeVisible();
  expect(errors).toEqual([]);
});

test("React host: the components paint, and StrictMode runs each script once", async ({ page }) => {
  const errors = collectErrors(page);
  const requests = feedRequests(page);
  await open(page, `${ONE}/react`);
  expect(requests).toHaveLength(1);                            // StrictMode ran banner.js twice
  await expect(page.locator(".ack-member-inline strong")).toHaveText("RWTH Aachen");
  await expect(banner(page)).toContainText("Shared news");
  expect(errors).toEqual([]);
});

test("the phone menu opens and closes on each click, on both hosts", async ({ page }) => {
  await page.setViewportSize({ width: 400, height: 800 });
  for (const host of ["jinja", "react"]) {
    await open(page, `${ONE}/${host}`);
    for (const expanded of ["true", "false"]) {
      await page.locator("#ds-nav-toggle").click();
      await expect(page.locator("#ds-nav-toggle"), host).toHaveAttribute("aria-expanded", expanded);
    }
  }
});

test("the search overlay closes when focus leaves it; Ctrl/Cmd+K is the host's in a field", async ({ page }) => {
  await open(page, `${ONE}/jinja`);
  const overlay = page.locator("#ds-search-overlay");
  const toggle = page.locator("#ds-search-toggle");
  await toggle.click();
  await expect(page.locator("#ds-search-input")).toBeFocused();
  await page.keyboard.press("Tab");                            // Advanced search
  await expect(overlay).toBeVisible();
  await page.keyboard.press("Tab");                            // behind the scrim: closed
  await expect(overlay).toBeHidden();
  await expect(toggle).toHaveAttribute("aria-expanded", "false");

  await page.keyboard.press("ControlOrMeta+k");
  await expect(overlay).toBeVisible();
  await page.keyboard.press("Escape");
  await expect(overlay).toBeHidden();
  await expect(toggle).toBeFocused();                          // Escape returns focus

  await page.setViewportSize({ width: 400, height: 800 });      // the phone menu hides Search:
  await page.keyboard.press("ControlOrMeta+k");
  await page.keyboard.press("Escape");
  await expect(page.locator("#ds-nav-toggle")).toBeFocused();  // focus goes to the hamburger
  await page.setViewportSize({ width: 1280, height: 720 });

  await page.locator("main").evaluate((m) => m.insertAdjacentHTML("beforeend", "<textarea></textarea>"));
  await page.locator("main textarea").focus();
  await page.keyboard.press("ControlOrMeta+k");
  await expect(overlay).toBeHidden();
});

test("a remounted header is wired again, and the old one stands down", async ({ page }) => {
  await open(page, `${ONE}/jinja`);
  // What a React remount does: new header and overlay nodes, and header.js run for them.
  await page.evaluate(() => {
    for (const old of [document.querySelector(".ds-site-header"), document.getElementById("ds-search-overlay")]) {
      const fresh = old.cloneNode(true);
      fresh.removeAttribute("data-ds-wired");
      old.replaceWith(fresh);
    }
    const again = document.createElement("script");
    again.src = document.querySelector('script[src$="chrome/header.js"]').src;
    document.body.appendChild(again);
  });
  await expect(page.locator(".ds-site-header")).toHaveAttribute("data-ds-wired", "");
  await page.keyboard.press("ControlOrMeta+k");                // the old handler would swallow it
  await expect(page.locator("#ds-search-overlay")).toBeVisible();
  await page.keyboard.press("Escape");
  await expect(page.locator("#ds-search-overlay")).toBeHidden();
});

test("printing keeps the logo, small, and hides the rest of the chrome", async ({ page }) => {
  await open(page, `${ONE}/jinja`);
  await expect(banner(page)).toBeVisible();
  await page.emulateMedia({ media: "print" });
  for (const part of [".ds-announcement", ".ds-site-header-nav", ".ds-site-header-nav-toggle", ".ds-site-footer"]) {
    await expect(page.locator(part), part).toBeHidden();
  }
  const logo = page.locator(".ds-site-header-logo img");
  await expect(logo).toBeVisible();
  expect((await logo.boundingBox()).height).toBe(28);
});

test("banner: the shared announcement, a landmark with its link and the default glyph", async ({ page }) => {
  await open(page, `${ONE}/jinja`);
  await expect(landmark(page)).toContainText("Shared news");
  const link = banner(page).locator("a.ds-announcement-link");
  await expect(link).toHaveText("Read more");
  await expect(link).toHaveAttribute("href", "https://info.example.org/news");
  const glyph = banner(page).locator("img.ds-announcement-glyph");
  await expect.poll(() => glyph.evaluate((img) => img.complete && img.naturalWidth)).toBeGreaterThan(0);
  await landmark(page).getByRole("button", { name: "Dismiss announcement" }).press("Enter");
  await expect(landmark(page)).toHaveCount(0);
  await expect(page.locator(".ds-site-header-logo")).toBeFocused();  // not the page's top
});

test("banner: an entry shows only inside its window", async ({ page }) => {
  const cases = [
    [{ start: at(-HOUR), end: at(HOUR) }, "Windowed"],
    [{ start: at(HOUR), end: at(2 * HOUR) }, ""],            // scheduled
    [{ start: at(-2 * HOUR), end: at(-HOUR) }, ""],          // over
    [{ start: "not-a-date", end: at(HOUR) }, ""],
    [{ start: at(-HOUR) }, ""],                              // no end: the end is mandatory
  ];
  for (const [window, shown] of cases) {
    expect(await bannerWith(page, serve({ id: "w", text: "Windowed", ...window })), JSON.stringify(window)).toBe(shown);
  }
});

test("banner: of the live entries the latest start wins, and every dismissal holds", async ({ page }) => {
  const campaign = { id: "campaign", text: "Long campaign", start: at(-48 * HOUR), end: at(48 * HOUR) };
  const urgent = { id: "urgent", text: "Maintenance now", start: at(-HOUR), end: at(HOUR) };
  const scheduled = { id: "next", text: "Next week", start: at(HOUR), end: at(2 * HOUR) };
  await page.route(FEED, serve(campaign, urgent, scheduled));
  await open(page, `${ONE}/jinja`);
  await expect(banner(page)).toContainText("Maintenance now");
  await banner(page).locator(".ds-close").click();
  await expect(banner(page)).toHaveCount(0);

  await open(page, `${ONE}/jinja`);
  await expect(banner(page)).toContainText("Long campaign");   // the next live entry
  await banner(page).locator(".ds-close").click();
  await open(page, `${ONE}/jinja`);
  await expect(page.locator(".ds-site-header")).toBeVisible();
  await expect(banner(page)).toHaveCount(0);                   // both dismissals kept
});

test("banner: the file is data: text stays text, links only https", async ({ page }) => {
  const markup = '<img src=x onerror="window.pwned = 1">News';
  for (const url of ["javascript:window.pwned = 1", "http://info.example.org/", "data:text/html,x",
                     "/relative", "https://https://info.example.org"]) {
    expect(await bannerWith(page, serve({ ...SHARED, text: markup, url })), url).toBe(markup);
    await expect(banner(page).locator(".ds-announcement-text *, a")).toHaveCount(0);
  }
  expect(await page.evaluate(() => window.pwned)).toBeUndefined();
});

test("banner: a missing or broken file shows nothing and throws nothing", async ({ page }) => {
  const errors = [];
  page.on("pageerror", (e) => errors.push(String(e)));
  for (const answer of [
    (route) => route.fulfill({ status: 404, body: "" }),
    (route) => route.fulfill({ contentType: "application/json", body: "{not json" }),
    (route) => route.fulfill({ json: [SHARED] }),
    (route) => route.fulfill({ json: { announcements: "none" } }),
    (route) => route.fulfill({ json: { announcements: [null, 3, "x", { id: "no-text" }] } }),
    (route) => route.abort(),
  ]) {
    expect(await bannerWith(page, answer)).toBe("");
  }
  await expect(landmark(page)).toHaveCount(0);                 // no empty landmark
  expect(errors).toEqual([]);
});

test("banner: hide_announcement drops the mount and fetches nothing", async ({ page }) => {
  const requests = feedRequests(page);
  for (const host of ["jinja", "react"]) {
    await open(page, `${ONE}/${host}?hide_announcement`);
    await expect(page.locator(".ds-site-header")).toBeVisible();
    await expect(page.locator("#ds-announcement")).toHaveCount(0);
  }
  expect(requests).toEqual([]);
});

test("banner: a dismissal holds for that message, on every site, until 30 days after its end", async ({ page, context }) => {
  await open(page, `${ONE}/jinja`);
  await banner(page).locator(".ds-close").click();
  await expect(landmark(page)).toHaveCount(0);
  const [cookie] = await context.cookies(ONE);
  expect(cookie.name).toMatch(new RegExp(`^${COOKIE}[0-9a-z]+$`));    // one cookie per message
  expect(cookie.domain).toBe(".brand.test");                            // the parent domain
  expect(Math.abs(cookie.expires - (Date.parse(SHARED.end) + 30 * DAY) / 1000)).toBeLessThan(2);

  expect(await bannerWith(page, serve(SHARED), `${TWO}/react`)).toBe(""); // another site
  for (const [change, shown] of [
    [{ end: at(24 * HOUR) }, ""],                                        // a new window: still dismissed
    [{ text: "Shared news, updated" }, "Shared news, updated"],         // an edited message shows
    [{ link_text: "Details" }, "Shared news"],
    [{ url: "https://info.example.org/other" }, "Shared news"],
  ]) {
    expect(await bannerWith(page, serve({ ...SHARED, ...change })), JSON.stringify(change)).toBe(shown);
  }
});

test("banner: on an IP host the dismissal falls back to that host", async ({ page }) => {
  await open(page, "http://127.0.0.1:5001/jinja");
  await banner(page).locator(".ds-close").click();
  await open(page, "http://127.0.0.1:5001/jinja");
  await expect(page.locator(".ds-site-header")).toBeVisible();
  await expect(banner(page)).toHaveCount(0);
});
