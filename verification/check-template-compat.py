#!/usr/bin/env python3
"""The assets on the rolling `latest` route must serve every template version.

Consumers track master and their lock files pin a SHA, but every SHA loads its assets from
the one route, so an asset change must stay compatible with every template version a lock
may hold: each commit in this history that changed a template (after SINCE), plus the
working tree. Against the current assets it checks that
  1. every `{{ static_base }}<path>` the templates load is still published
     (upload_static_assets.stage);
  2. every `ds-*` / `is-sr-only` class they use is still in design-system.css.
It proves nothing was removed or renamed, not behaviour. Needs full history (fetch-depth: 0).
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "templates"))
import upload_static_assets  # noqa: E402
from generate import SECTIONS  # noqa: E402

TEMPLATES = [f"templates/arxiv_brand/{s}.html" for s in SECTIONS]
# Versions up to this commit are no longer checked. Raise it, to the oldest SHA any
# consumer's lock still holds, to retire them; None checks every version. Never retire a
# version younger than the longest page cache (about a year, browse's abs pages): cached
# pages keep the markup they were rendered with.
SINCE = None

ASSET_RE = re.compile(r"\{\{\s*static_base\s*\}\}([^\"'\s>]+)")
CLASS_RE = re.compile(r'class="([^"]*)"')
COMMENT_RE = re.compile(r"\{#.*?#\}", re.S)


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True, check=True).stdout


def versions():
    """Every commit in this history that changed a template, newest first."""
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        sys.exit("FAIL  shallow clone: the template history is incomplete (fetch-depth: 0)")
    return git("log", "--format=%H", f"{SINCE}..HEAD" if SINCE else "HEAD", "--", *TEMPLATES).split()


def template_source(sha, section):
    """The section's source at `sha`, or in the working tree when `sha` is None; empty in a
    version older than the section."""
    path = f"templates/arxiv_brand/{section}.html"
    if sha is None:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            return f.read()
    if not git("ls-tree", "--name-only", sha, path).strip():
        return ""
    return git("show", f"{sha}:{path}")


def main():
    with open(os.path.join(ROOT, "docs", "design-system.css"), encoding="utf-8") as f:
        css = re.sub(r"/\*.*?\*/", "", f.read(), flags=re.S)   # a class named in a comment is not defined
        defined = set(re.findall(r"\.((?:ds-|is-sr-only)[\w-]*)", css))
    with tempfile.TemporaryDirectory(prefix="ds-route-") as staging:
        upload_static_assets.stage(staging)
        published = {os.path.relpath(os.path.join(d, f), staging)
                     for d, _, files in os.walk(staging) for f in files}

    problems = []
    targets = [(sha, sha[:10]) for sha in versions()] + [(None, "working tree")]
    for sha, label in targets:
        src = COMMENT_RE.sub("", "".join(template_source(sha, s) for s in SECTIONS))
        for path in sorted(set(ASSET_RE.findall(src))):
            if path not in published:
                problems.append(f"{label}: loads {path}, which is no longer published")
        for attr in CLASS_RE.findall(src):
            for cls in attr.split():
                if (cls.startswith("ds-") or cls == "is-sr-only") and "{{" not in cls \
                        and cls not in defined:
                    problems.append(f"{label}: uses .{cls}, no longer defined in design-system.css")

    if problems:
        print("FAIL  current assets break a template version (rolling `latest` contract):")
        for p in problems:
            print("  - " + p)
        return 1
    print(f"PASS  current assets serve all {len(targets)} template versions "
          f"({len(targets) - 1} in the history + the working tree)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
