import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';

const OUT_DIR = '/Users/shamsibrinn/Documents/arxiv-repos/design-system/audits/2026-06-11';

// Responsiveness pass — viewport-only at top, plus mid-paper scroll for HTML reader
const RESPONSIVENESS_PAGES = [
  { name: 'html-redesign',      url: 'https://arxiv.github.io/design-system/mockups/html-redesign.html',     scrollPositions: ['top', 'mid', 'bottom'] },
  { name: 'abstract-redesign',  url: 'https://arxiv.github.io/design-system/mockups/abstract-redesign.html', scrollPositions: ['top', 'bottom'] },
];
const RESPONSIVENESS_VIEWPORTS = [320, 375, 414, 768, 1024, 1440];

// Component pass — first-screen + mid + bottom (or just first-screen for short pages)
const COMPONENT_PAGES = [
  { name: '01-html-redesign-NEW',       url: 'https://arxiv.github.io/design-system/mockups/html-redesign.html',     positions: ['top', 'mid'] },
  { name: '02-abstract-redesign-NEW',   url: 'https://arxiv.github.io/design-system/mockups/abstract-redesign.html', positions: ['top', 'bottom'] },
  { name: '03-abs-current',             url: 'https://arxiv.org/abs/2604.22725v1',                                   positions: ['top', 'bottom'] },
  { name: '04-html-current',            url: 'https://arxiv.org/html/2604.22725v1',                                  positions: ['top', 'mid'] },
  { name: '05-homepage-current',        url: 'https://arxiv.org/',                                                   positions: ['top', 'bottom'] },
  { name: '06-browse-listing-current',  url: 'https://arxiv.org/list/gr-qc/recent',                                  positions: ['top', 'mid'] },
  { name: '07-info-help-current',       url: 'https://info.arxiv.org/help/index.html',                               positions: ['top'] },
  { name: '08-search-advanced-current', url: 'https://arxiv.org/search/advanced',                                    positions: ['top'] },
  { name: '09-login-current',           url: 'https://arxiv.org/login',                                              positions: ['top'] },
];
const COMPONENT_VIEWPORT = 1440;

async function captureAt(page, position) {
  if (position === 'top') {
    await page.evaluate(() => window.scrollTo(0, 0));
  } else if (position === 'mid') {
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.4));
  } else if (position === 'bottom') {
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight - window.innerHeight));
  }
  await page.waitForTimeout(500);
}

async function loadPage(page, url) {
  await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 });
  await page.waitForTimeout(1500);
}

// Clean out previous screenshots before re-running
const shootDir = path.join(OUT_DIR, 'screenshots');
if (fs.existsSync(shootDir)) fs.rmSync(shootDir, { recursive: true });

(async () => {
  const browser = await chromium.launch();

  console.log('=== Responsiveness pass (viewport-only, multi-scroll) ===');
  for (const { name, url, scrollPositions } of RESPONSIVENESS_PAGES) {
    const dir = path.join(OUT_DIR, 'screenshots', 'responsiveness', name);
    fs.mkdirSync(dir, { recursive: true });
    for (const w of RESPONSIVENESS_VIEWPORTS) {
      const context = await browser.newContext({ viewport: { width: w, height: 700 } });
      const page = await context.newPage();
      try {
        await loadPage(page, url);
        for (const pos of scrollPositions) {
          await captureAt(page, pos);
          const out = path.join(dir, `${String(w).padStart(4, '0')}-${pos}.png`);
          await page.screenshot({ path: out, fullPage: false });
          const sz = fs.statSync(out).size;
          console.log(`  ${name} @ ${w} ${pos}: OK (${(sz / 1024).toFixed(0)}KB)`);
        }
      } catch (e) {
        console.log(`  ${name} @ ${w}: ERROR ${e.message.split('\n')[0]}`);
      }
      await context.close();
    }
  }

  console.log('\n=== Component pass (1440px, multi-scroll) ===');
  const compDir = path.join(OUT_DIR, 'screenshots', 'components');
  fs.mkdirSync(compDir, { recursive: true });
  for (const { name, url, positions } of COMPONENT_PAGES) {
    const context = await browser.newContext({ viewport: { width: COMPONENT_VIEWPORT, height: 900 } });
    const page = await context.newPage();
    try {
      await loadPage(page, url);
      for (const pos of positions) {
        await captureAt(page, pos);
        const out = path.join(compDir, `${name}-${pos}.png`);
        await page.screenshot({ path: out, fullPage: false });
        const sz = fs.statSync(out).size;
        console.log(`  ${name} ${pos}: OK (${(sz / 1024).toFixed(0)}KB)`);
      }
    } catch (e) {
      console.log(`  ${name}: ERROR ${e.message.split('\n')[0]}`);
    }
    await context.close();
  }

  await browser.close();
  console.log('\nDone.');
})();
