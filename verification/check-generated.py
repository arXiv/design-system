#!/usr/bin/env python3
"""Every concrete target of the brand templates is generated from the single source, and
current.

The source is templates/arxiv_brand/{head,header,footer}.html + schema.json (the Python
package ships them as they are). templates/generate.py writes everything else — the
TemplateToolkit, React (+ .d.ts) and vendored adapters and the repository-root
package.json. A hand-edited target is a second source of truth that drifts, so this fails
if a generated file is missing or stale, or if a tracked .jsx/.tsx/.d.ts/.tt under templates/,
or any file in templates/adapters/, is not one the generator writes.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "templates"))
import generate  # noqa: E402

TARGET_SUFFIXES = (".jsx", ".tsx", ".d.ts", ".tt")


def main() -> int:
    expected = generate.generated()
    tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files"],
                             capture_output=True, text=True, check=True).stdout.split()
    problems = []
    for rel, text in expected.items():
        f = ROOT / rel
        if not f.is_file():
            problems.append(f"{rel}: missing — run templates/generate.py")
        elif f.read_text(encoding="utf-8") != text:
            problems.append(f"{rel}: differs from the source — run templates/generate.py "
                            "(never edit a generated file)")
    for rel in tracked:
        if rel not in expected and rel.startswith("templates/") and (
                rel.endswith(TARGET_SUFFIXES) or rel.startswith("templates/adapters/")):
            problems.append(f"{rel}: hand-written target; generate it from templates/arxiv_brand instead")
    if problems:
        print("FAIL  brand-template targets must be generated from the single source:")
        for p in problems:
            print("  - " + p)
        return 1
    print(f"PASS  all {len(expected)} generated targets match templates/arxiv_brand")
    return 0


if __name__ == "__main__":
    sys.exit(main())
