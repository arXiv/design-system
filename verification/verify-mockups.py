#!/usr/bin/env python3
"""
Mockup verification harness — arXiv design system

Automated regression checks for the abstract-page and HTML-reader
mockups. Run after any mockup change; every check here corresponds to
a defect class found in user research, the html_feedback issue queues,
or direct rendering audits (see mockups/design-review-2026-06-11.md
and references/github-open-ux-issues-synthesis.md).

Usage:
    pip install playwright && playwright install chromium
    python3 verification/verify-mockups.py

Exit code 0 = all checks pass. Each failure prints a FAIL line with
the research basis for the check.
"""

import asyncio
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ABS = (REPO / "mockups" / "abstract-redesign.html").as_uri()
READER = (REPO / "mockups" / "html-redesign.html").as_uri()

PASSES = []
FAILS = []


def check(name, ok, why):
    (PASSES if ok else FAILS).append(name)
    print(("PASS  " if ok else "FAIL  ") + name + ("" if ok else "\n      basis: " + why))


async def run():
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        b = await p.chromium.launch()

        # ── 1. Reflow at 320px (WCAG 1.4.10; 400% zoom equivalent) ──
        # Also the root cause of the middle-click horizontal-autoscroll
        # bug class (html_feedback #474 #3689 #4792 #5233 #6036): any
        # horizontal scrollable overflow breaks vertical autoscroll.
        for name, url in [("abstract", ABS), ("reader", READER)]:
            for width in (320, 390, 768, 1440):
                pg = await b.new_page(viewport={"width": width, "height": 800})
                await pg.goto(url)
                await pg.wait_for_timeout(1200)
                ov = await pg.evaluate(
                    "document.documentElement.scrollWidth - document.documentElement.clientWidth"
                )
                check(
                    f"no horizontal overflow: {name} @ {width}px",
                    ov <= 0,
                    "WCAG 1.4.10 reflow; middle-click autoscroll bug class",
                )
                await pg.close()

        # ── 2. ARIA hygiene (abstract) ──
        pg = await b.new_page(viewport={"width": 1440, "height": 900})
        await pg.goto(ABS)
        await pg.wait_for_timeout(800)
        radios = await pg.evaluate("document.querySelectorAll('[role=radio]').length")
        check(
            "no role=radio without arrow-key support (abstract)",
            radios == 0,
            "ARIA radio pattern promises arrow keys; use aria-pressed buttons",
        )
        pressed = await pg.evaluate("document.querySelectorAll('[aria-pressed]').length")
        check("citation switchers use aria-pressed", pressed >= 5, "switcher accessibility")
        px_fonts = await pg.evaluate(
            """Array.from(document.styleSheets).flatMap(s => {
                 try { return Array.from(s.cssRules); } catch(e) { return []; }
               }).filter(r => r.style && r.style.fontSize && r.style.fontSize.endsWith('px')).length"""
        )
        check(
            "abstract type sizes are rem, not px",
            px_fonts == 0,
            "accessibility-priorities.md: user font-size overrides must propagate",
        )
        await pg.close()

        # ── 3. No-JS readability (progressive enhancement) ──
        pg = await b.new_page(viewport={"width": 1440, "height": 900}, java_script_enabled=False)
        await pg.goto(ABS)
        await pg.wait_for_timeout(800)
        vis_authors = await pg.eval_on_selector_all(
            ".abs-authors a", "els => els.filter(e => e.offsetParent !== null).length"
        )
        check("no-JS: all authors visible (abstract)", vis_authors >= 22, "content never JS-gated")
        search = await pg.eval_on_selector("#search-toggle", "e => e.tagName")
        check("no-JS: search degrades to a link", search == "A", "no dead controls without JS")
        await pg.close()

        pg = await b.new_page(viewport={"width": 1440, "height": 900}, java_script_enabled=False)
        await pg.goto(READER)
        await pg.wait_for_timeout(1000)
        fn = await pg.eval_on_selector_all(
            ".footnote", "els => els.filter(e => e.offsetParent !== null).length"
        )
        check(
            "no-JS: footnotes readable inline (reader)",
            fn > 0,
            "hover-only footnotes were filed 9x in html_feedback (#805 et al.)",
        )
        await pg.close()

        # ── 4. Reader interactions ──
        pg = await b.new_page(viewport={"width": 1440, "height": 900})
        await pg.goto(READER)
        await pg.wait_for_timeout(1500)

        # TOC titles contain no raw TeX (annotation leakage)
        await pg.click("#toc-trigger")
        await pg.wait_for_timeout(400)
        leaked = await pg.evaluate(
            "Array.from(document.querySelectorAll('#toc-dropdown-list li')).some(li => li.textContent.includes('\\\\'))"
        )
        check("TOC titles free of raw TeX", not leaked, "MathML annotation leakage")
        await pg.keyboard.press("Escape")

        # Citation chips: compact at rest, contextual label, expanded-only-while-open
        chip = await pg.query_selector(".ltx_cite a.ltx_ref")
        rest = await chip.evaluate(
            "a => ({role: a.getAttribute('role'), exp: a.hasAttribute('aria-expanded'), label: a.getAttribute('aria-label')})"
        )
        check(
            "citation chips aurally compact at rest",
            rest["role"] is None and not rest["exp"],
            "push list: Dan Miner's 'auditory disturbance you cannot skip'",
        )
        check(
            "citation chips carry contextual accessible names",
            bool(rest["label"]) and rest["label"].startswith("Reference"),
            "push list: Tigwell's 'what is reference 10?'",
        )

        # Figure lightbox: opens, paints, zoom persists, closes, restores focus
        await pg.evaluate("document.querySelector('#fig-evolution').scrollIntoView()")
        await pg.wait_for_timeout(300)
        await pg.evaluate("document.querySelector('.fig-chip-expand').click()")
        await pg.wait_for_timeout(500)
        opened = await pg.evaluate("!!document.querySelector('dialog.fig-lightbox') && document.querySelector('dialog.fig-lightbox').open")
        check("lightbox opens", opened, "open-queue theme A1 (~15 issues)")
        painted = await pg.evaluate(
            "(() => { const c = document.querySelector('.fig-lightbox-content'); return c && c.getBoundingClientRect().width > 100; })()"
        )
        check("lightbox content lays out", painted, "transformed-svg rasterization regression")
        await pg.click(".fig-lightbox-zoombtn[data-zoom='in']")
        await pg.mouse.move(700, 500)
        await pg.mouse.down()
        await pg.mouse.move(760, 540)
        await pg.mouse.up()
        await pg.wait_for_timeout(300)
        level = await pg.eval_on_selector(".fig-lightbox-zoomlevel", "e => e.textContent")
        check(
            "lightbox zoom persists after pointer release",
            level != "100%",
            "the #1 figure complaint: zoom released on mouse-up (#4669 et al.)",
        )
        await pg.keyboard.press("Escape")
        await pg.wait_for_timeout(300)
        closed = await pg.evaluate("!document.querySelector('dialog.fig-lightbox').open")
        check("lightbox closes on Esc", closed, "dialog semantics")
        await pg.close()

        await b.close()

    print(f"\n{len(PASSES)} passed, {len(FAILS)} failed")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(run()))
