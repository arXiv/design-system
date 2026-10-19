"""vendor.py: the marked copies in a site take a commit's generated files, and nothing else
changes. Stdlib only:

    python3 -m unittest discover -s templates/tests
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parents[1]
SITE = """<?php echo <<<'HTML'
<!-- design-system header: templates/adapters/vendored/header.html at 0 -->
stale
<!-- end design-system header -->
HTML;
[%# design-system footer: templates/adapters/templatetoolkit/footer.tt at 0 %]
[%# end design-system footer %]
"""


def vendor(path: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(TEMPLATES / "vendor.py"), str(path)],
                          capture_output=True, text=True)


def committed(name: str) -> str:
    return subprocess.run(["git", "-C", str(TEMPLATES), "show", f"HEAD:templates/adapters/{name}"],
                          capture_output=True, text=True, check=True).stdout


class TestVendor(unittest.TestCase):
    def test_each_block_becomes_its_file_at_the_commit(self):
        sha = subprocess.run(["git", "-C", str(TEMPLATES), "rev-parse", "--short=12", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp, "page.php")
            site.write_text(SITE)
            self.assertEqual(vendor(site).returncode, 0)
            self.assertEqual(site.read_text(), (
                "<?php echo <<<'HTML'\n"
                f"<!-- design-system header: templates/adapters/vendored/header.html at {sha} -->\n"
                + committed("vendored/header.html") +
                "<!-- end design-system header -->\nHTML;\n"
                f"[%# design-system footer: templates/adapters/templatetoolkit/footer.tt at {sha} %]\n"
                + committed("templatetoolkit/footer.tt") +
                "[%# end design-system footer %]\n"))

            site.write_text(SITE.replace("<!-- end design-system header -->\n", ""))
            self.assertNotEqual(vendor(site).returncode, 0)   # a block without its end line


if __name__ == "__main__":
    unittest.main()
