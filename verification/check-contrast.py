#!/usr/bin/env python3
"""Text-safe pairings: verify.

The pairings below are the ones the docs promise are safe (colors.html,
"Recommended pairings"): each text token on each surface it is allowed on,
in both themes, on both surfaces. This script measures every one against
the stylesheets and fails if any drops below WCAG AA for normal text
(4.5:1). Run with --emit to print the measured list, one pairing per
line, for a digest or a review.

Why this exists: three shipped bugs (the watermark, the skip link, the
nav group labels) were text elements borrowing tokens from non-text
roles. The list is the positive statement of which pairings are safe,
and this check keeps it true when tokens change.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "docs/design-system.css"
INT = ROOT / "docs/internal-tools.css"

def parse_block(text, start_marker):
    i = text.index(start_marker)
    j = text.index("{", i)
    depth, k = 1, j + 1
    while depth and k < len(text):
        depth += text[k] == "{"
        depth -= text[k] == "}"
        k += 1
    # Capture hex values AND var() references — since the primitive layer
    # landed, a semantic token usually points at a primitive rather than
    # carrying a hex of its own. resolve() flattens the chain.
    return dict(re.findall(r"(--[a-z0-9-]+)\s*:\s*(#[0-9a-fA-F]{3,6}|var\(--[a-z0-9-]+\))", text[j:k]))

def resolve(d):
    """Flatten var(--x) chains to the hex they end at."""
    out = dict(d)
    for _ in range(8):
        changed = False
        for key, val in list(out.items()):
            m = re.fullmatch(r"var\((--[a-z0-9-]+)\)", val.strip())
            if m and m.group(1) in out and out[m.group(1)] != val:
                out[key] = out[m.group(1)]; changed = True
        if not changed: break
    return {k: v for k, v in out.items() if v.startswith("#")}

def tokens(css_path, dark_marker, seed_light=None, seed_dark=None):
    """Parse one stylesheet's tokens, resolved.

    `seed_*` carries the tier below. Tier 2 declares only what differs and a
    page loads tier 1 first, so a tier 2 token may point at a primitive that
    only tier 1 declares — the Access Lime ramp does exactly that. Without the
    seed those chains cannot resolve and the parse raises on the first one.
    """
    s = css_path.read_text()
    raw_light = dict(seed_light or {})
    raw_light.update(parse_block(s, ":root {"))
    raw_dark = dict(seed_dark or seed_light or {})
    raw_dark.update(raw_light)
    raw_dark.update(parse_block(s, dark_marker))
    # Resolve within each mode: a dark semantic token may point at a
    # primitive declared in :root, so the light map seeds the dark one.
    return resolve(raw_light), resolve(raw_dark)

def lum(hexv):
    h = hexv.lstrip("#")
    if len(h) == 3: h = "".join(c*2 for c in h)
    r, g, b = (int(h[i:i+2], 16)/255 for i in (0, 2, 4))
    f = lambda v: v/12.92 if v <= 0.03928 else ((v+0.055)/1.055)**2.4
    r, g, b = f(r), f(g), f(b)
    return 0.2126*r + 0.7152*g + 0.0722*b

def ratio(fg, bg):
    l1, l2 = lum(fg), lum(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return round((hi + 0.05) / (lo + 0.05), 2)

# ── Curated pairing spec.  prefix, text rows, surface columns ──────────
# Both surfaces now share one token vocabulary, so the row and column names are
# the same for each; only the values behind them differ.
PUBLIC_TEXT = ["text", "text-muted", "link", "link-hover", "link-visited"]
PUBLIC_SURF = ["canvas", "surface", "surface-muted", "accent-surface", "accent-wash"]
PUBLIC_SPECIAL = [("text-on-accent", "accent"), ("text-on-accent", "accent-hover")]
PUBLIC_STATUS = [("info-fg", "info-bg"), ("success-fg", "success-bg"), ("warning-fg", "warning-bg"), ("error-fg", "error-bg")]
PUBLIC_NEVER = [("border-strong", "interactive borders, tracks, and arrows (3:1 non-text minimum)"),
                ("text-disabled", "disabled text only — exempt from AA, never for content"),
                ("border", "decorative hairlines"), ("border-muted", "component borders")]

INT_TEXT = ["text", "text-muted", "link", "link-hover", "link-visited"]
INT_SURF = ["canvas", "surface", "surface-muted", "surface-hover", "surface-hover-strong"]
INT_SPECIAL = [("text-on-accent", "accent"), ("text-on-accent", "accent-hover"), ("text-on-accent", "accent-active")]
INT_STATUS = [("info-fg", "info-bg"), ("success-fg", "success-bg"), ("warning-fg", "warning-bg"), ("error-fg", "error-bg")]
INT_NEVER = [("border-strong", "borders and arrows (3:1 non-text minimum)"),
             ("text-disabled", "disabled text only"), ("danger-disabled-fg", "disabled destructive icon buttons only")]

def palettes():
    pub_text = PUB.read_text()
    raw_pub_l = parse_block(pub_text, ":root {")
    raw_pub_d = parse_block(pub_text, '[data-theme="dark"] {')
    pub_l = resolve(raw_pub_l)
    pub_d = resolve({**raw_pub_l, **raw_pub_d})
    # The internal sheet is tier 2: it declares only what differs, and an
    # internal page loads tier 1 first. So the palette an internal page sees
    # is tier 1 with tier 2 layered over it, per theme, and then .ds-internal
    # (tier 1, on a parent) re-pointing the accent on top of both.
    int_text = INT.read_text()
    raw_int_l = parse_block(int_text, ":root {")
    raw_int_d = parse_block(int_text, "@media (prefers-color-scheme: dark)")
    ctx_l = parse_block(pub_text, "\n.ds-internal {")
    ctx_d = parse_block(pub_text, '[data-theme="dark"] .ds-internal {')
    int_l = resolve({**raw_pub_l, **raw_int_l, **ctx_l})
    int_d = resolve({**raw_pub_l, **raw_pub_d, **raw_int_d, **ctx_l, **ctx_d})
    return (pub_l, pub_d), (int_l, int_d)

def pairings():
    (pub_l, pub_d), (int_l, int_d) = palettes()
    rows = []
    for label, (light, dark), text, surf, special, status in (
        ("public", (pub_l, pub_d), PUBLIC_TEXT, PUBLIC_SURF, PUBLIC_SPECIAL, PUBLIC_STATUS),
        ("internal", (int_l, int_d), INT_TEXT, INT_SURF, INT_SPECIAL, INT_STATUS),
    ):
        pairs = [(t, sc) for t in text for sc in surf] + special + status
        for fg, bg in pairs:
            f, b = "--ds-" + fg, "--ds-" + bg
            rows.append((label, f, b, ratio(light[f], light[b]), ratio(dark[f], dark[b])))
    return rows

def main():
    rows = pairings()
    if "--emit" in sys.argv:
        for label, f, b, rl, rd in rows:
            print(f"{label:9} {f:26} on {b:26} {rl:5.2f} light  {rd:5.2f} dark")
        return 0
    bad = [r for r in rows if r[3] < 4.5 or r[4] < 4.5]
    if bad:
        print(f"FAIL  {len(bad)} promised text pairing(s) fall below 4.5:1")
        for label, f, b, rl, rd in bad:
            print(f"      {label}: {f} on {b} — {rl} light / {rd} dark")
        return 1
    print(f"PASS  {len(rows)} promised text pairings clear WCAG AA in both themes")
    return 0

if __name__ == "__main__":
    sys.exit(main())
