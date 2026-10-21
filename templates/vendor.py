#!/usr/bin/env python3
"""Update a site's copies of the generated templates, for a site that cannot install the
package (submit, tapir, status, lib). Needs Python 3 and git, nothing else.

Set up, once per copy: where the copy goes in the site's file, write two marker lines in
that file's own comment syntax, naming a file from templates/adapters/ (vendored/ for static
HTML, templatetoolkit/ for TemplateToolkit), then run the update below to fill the block in:

    <!-- design-system header: templates/adapters/vendored/header.html at 0 -->
    <!-- end design-system header -->

The name ("header") pairs the two lines; the commit after "at" is written by the update. In
Perl or PHP, put the markers inside a literal that does not interpolate (a <<'EOT' heredoc,
a <<<'EOT' nowdoc), so the block prints as written.

Update, from a design-system clone:

    git fetch origin
    python3 templates/vendor.py --ref origin/master SITE_FILE...

Each block becomes its file at that commit (default: this clone's HEAD), and its opening line
records the commit. Review the site's diff and commit it there. Edit around the blocks, never
inside them: the next update replaces what is inside. A file without a block, or a block
without its end line, stops the run before that file is written.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BLOCK_RE = re.compile(
    r"^(?P<open>[^\n]*design-system (?P<name>[\w-]+): (?P<path>templates/adapters/\S+) at )"
    r"[0-9a-f]+(?P<rest>[^\n]*\n)(?:[^\n]*\n)*?(?P<close>[^\n]*end design-system (?P=name)\b)",
    re.M)
OPEN_RE = re.compile(r"design-system [\w-]+: templates/adapters/")


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True,
                          check=True).stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ref", default="HEAD", help="the design-system commit to copy from")
    parser.add_argument("files", nargs="+", type=Path, metavar="SITE_FILE",
                        help="a site file holding marked blocks")
    args = parser.parse_args()
    # Copies come from the commit, never the working tree, so a marker names what it holds.
    sha = git("rev-parse", "--short=12", args.ref + "^{commit}").strip()
    for path in args.files:
        old = path.read_text(encoding="utf-8")
        text, count = BLOCK_RE.subn(
            lambda m: m["open"] + sha + m["rest"] + git("show", f"{sha}:{m['path']}") + m["close"],
            old)
        opened = len(OPEN_RE.findall(old))
        if not opened or count != opened:
            sys.exit(f"{path}: {opened} design-system block(s), {count} with an end line")
        path.write_text(text, encoding="utf-8")
        print(f"{path}: {count} block(s) at design-system {sha}")


if __name__ == "__main__":
    main()
