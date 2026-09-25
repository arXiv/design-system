"""Publish the design system's static assets to the rolling route
<bucket>/static/design-system/latest/ that every consumer's static_base points at:
PUBLISHED below, plus the derived design-system-components.css (build_components_css.py)
and fonts.css. There are no versioned snapshots, so an asset change must keep serving every
template version (verification/check-template-compat.py). The shared announcements,
json/announcements.json, are checked before anything is staged (check_announcements).

    python3 upload_static_assets.py --bucket gs://arxiv-dev-web-static [--dry-run] [--yes]

Buckets: gs://arxiv-dev-web-static (static.dev.arxiv.org), gs://arxiv-web-static
(static.arxiv.org). Stdlib only; the tests and checks reuse stage(dir).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

from datetime import datetime
from urllib.parse import urlsplit

import build_components_css

ROOT = os.path.dirname(os.path.abspath(__file__))

# (source relative to the repository root, published path); a directory is copied whole.
PUBLISHED = [
    ("docs/design-system.css", "design-system.css"),
    ("docs/internal/internal-tools.css", "internal-tools.css"),
    ("docs/theme.js", "theme.js"),
    ("docs/assets/images/logos/logo_arxiv-primary.svg", "logos/arxiv-logo.svg"),
    ("docs/assets/images/bones/icon_small-smileybones.svg", "logos/smileybones.svg"),  # banner glyph
    # The footer's funder marks, at the size it shows them (the folder also holds the sources).
    ("docs/assets/images/logos/other-org-logos/simons-foundation.png", "funders/simons-foundation.png"),
    ("docs/assets/images/logos/other-org-logos/simons-foundation-international.png",
     "funders/simons-foundation-international.png"),
    ("docs/assets/images/logos/other-org-logos/schmidt-sciences.png", "funders/schmidt-sciences.png"),
    ("templates/assets", "."),
]
# Cache-Control by top-level directory ("" is the rest). `latest` is updated in place, so it
# must propagate promptly (GCS's default is an hour); an announcement is edited while it runs
# (an incident), so a correction reaches readers in minutes.
CACHE_CONTROL = {"": "public, max-age=60, must-revalidate", "json": "public, max-age=300"}

ANNOUNCEMENTS = "templates/assets/json/announcements.json"
ANNOUNCEMENT_KEYS = ("id", "text", "link_text", "url", "start", "end")
# The ISO 8601 forms every browser's Date.parse reads, with the offset (never local time).
TIME_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2}(\.\d{1,3})?)?(Z|[+-]\d{2}:\d{2})")


def check_announcements(data: object) -> list[str]:
    """What is wrong with an announcements file (templates/BANNER_ANNOUNCEMENTS.md)."""
    entries = data.get("announcements") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        return ['expected {"announcements": [...]}']
    problems, ids, previous = [], set(), None
    for i, a in enumerate(entries):
        if not isinstance(a, dict) or not all(isinstance(v, str) for v in a.values()):
            problems.append(f"entry {i}: not an object of strings")
            continue
        at = f"entry {i} ({a.get('id')!r})"
        problems += [f"{at}: unknown key {k!r}" for k in a if k not in ANNOUNCEMENT_KEYS]
        problems += [f"{at}: {k} is required" for k in ("id", "text", "start", "end") if not a.get(k)]
        if bool(a.get("link_text")) != bool(a.get("url")):
            problems.append(f"{at}: link_text and url go together")
        if a.get("url") and not _https_url(a["url"]):
            problems.append(f"{at}: url is not an absolute https URL on a named host")
        start, end = _time(a.get("start", "")), _time(a.get("end", ""))
        problems += [f"{at}: {k} is not an ISO 8601 time with its offset"
                     for k, t in (("start", start), ("end", end)) if a.get(k) and not t]
        if start and end and end <= start:
            problems.append(f"{at}: end is not after start")
        if start and previous and start > previous:
            problems.append(f"{at}: starts after the entry above it (newest first)")
        if a.get("id") in ids:
            problems.append(f"{at}: duplicate id")
        ids.add(a.get("id"))
        previous = start or previous
    return problems


def _https_url(value: str) -> bool:
    """An absolute https URL on a named host, the only link chrome/banner.js draws."""
    try:
        url = urlsplit(value)
    except ValueError:
        return False
    return url.scheme == "https" and (url.hostname or "").find(".") > 0


def _time(value: str) -> datetime | None:
    if not TIME_RE.fullmatch(value):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def stage(staging: str) -> None:
    """Assemble the exact tree to publish, so --dry-run shows exactly what would change. A
    bad announcements file stops it (ValueError)."""
    with open(os.path.join(ROOT, ANNOUNCEMENTS), encoding="utf-8") as f:
        problems = check_announcements(json.load(f))
    if problems:
        raise ValueError(f"{ANNOUNCEMENTS}: " + "; ".join(problems))
    for src, rel in PUBLISHED:
        src, dest = os.path.join(ROOT, src), os.path.join(staging, rel)
        if os.path.isdir(src):
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copyfile(src, dest)
    with open(os.path.join(ROOT, "docs", "design-system.css"), encoding="utf-8") as f:
        components = build_components_css.generate(f.read())
    with open(os.path.join(staging, "design-system-components.css"), "w", encoding="utf-8") as f:
        f.write(components)
    _stage_fonts(staging)


def _stage_fonts(staging: str) -> None:
    """fonts.css: the faces docs/fonts.css declares, with their woff2 files and licences
    under fonts/. Page-level state, so never part of the component stylesheet."""
    with open(os.path.join(ROOT, "docs", "fonts.css"), encoding="utf-8") as f:
        declared = re.sub(r"/\*.*?\*/", "", f.read(), flags=re.S)
    faces = re.findall(r"@font-face\s*\{.*?\}", declared, re.S)
    files = [u for face in faces for u in re.findall(r'url\("(fonts/[^"]+)"\)', face)]
    files += ["fonts/" + p for p in os.listdir(os.path.join(ROOT, "docs", "fonts")) if p.endswith(".txt")]
    os.makedirs(os.path.join(staging, "fonts"), exist_ok=True)
    for rel in files:
        shutil.copyfile(os.path.join(ROOT, "docs", rel), os.path.join(staging, rel))
    with open(os.path.join(staging, "fonts.css"), "w", encoding="utf-8") as f:
        f.write("/* Self-hosted IBM Plex / STIX faces the design system declares (from docs/fonts.css).\n"
                "   Page-level, separate from design-system-components.css by design. */\n"
                + "\n".join(faces) + "\n")


def publish(staging: str, dest: str, dry_run: bool) -> None:
    """Upload what changed, its Cache-Control set in the same request: set afterwards, GCS's
    one-hour default would be served, and cached, in between."""
    for sub, value in CACHE_CONTROL.items():
        exclude = [] if sub else [f"--exclude=^{d}/" for d in CACHE_CONTROL if d]
        subprocess.run(["gcloud", "storage", "rsync", "--recursive", f"--cache-control={value}", *exclude,
                        os.path.join(staging, sub), f"{dest}/{sub}".rstrip("/")]
                       + (["--dry-run"] if dry_run else []), check=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--bucket", required=True,
                        help="gs://arxiv-dev-web-static (dev) or gs://arxiv-web-static (prod)")
    parser.add_argument("--dry-run", action="store_true", help="show what would change; upload nothing")
    parser.add_argument("--yes", action="store_true", help="skip the confirmation prompt (CI)")
    args = parser.parse_args(argv)

    dest = f"{args.bucket.rstrip('/')}/static/design-system/latest"
    for src, rel in PUBLISHED:
        print(f"  {src} -> {rel}")
    print(f"dest: {dest}")
    if not (args.dry_run or args.yes) and input("Publish there? [y/N] ").strip().lower() != "y":
        print("Aborted.")
        return 1
    with tempfile.TemporaryDirectory() as staging:
        stage(staging)
        publish(staging, dest, args.dry_run)
    print(f"Done. Verify: gcloud storage ls --recursive {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
