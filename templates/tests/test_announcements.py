"""The shared announcements file (json/announcements.json) and the check that guards its
publication (upload_static_assets.check_announcements). Stdlib only."""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import upload_static_assets as u  # noqa: E402

ROOT = Path(u.ROOT)
GOOD = {"id": "maint", "text": "Maintenance tonight", "start": "2026-08-03T00:00-04:00",
        "end": "2026-08-06T00:00Z"}
LINK = dict(GOOD, link_text="Status", url="https://status.arxiv.org")


def problems(*entries):
    return u.check_announcements({"announcements": list(entries)})


class TestAnnouncements(unittest.TestCase):
    def test_the_published_file_and_the_documented_example_pass(self):
        doc = (ROOT / "templates/BANNER_ANNOUNCEMENTS.md").read_text(encoding="utf-8")
        for data in (json.loads((ROOT / u.ANNOUNCEMENTS).read_text(encoding="utf-8")),
                     json.loads(doc.split("```json")[1].split("```")[0])):
            self.assertEqual(u.check_announcements(data), [])
        self.assertEqual(problems(GOOD), [])  # the link is optional

    def test_each_rule(self):
        older = dict(GOOD, id="older", start="2026-07-01T00:00Z", end="2026-07-02T00:00Z")
        cases = [
            ("unknown key 'icon'", dict(GOOD, icon="wrench")),
            ("id is required", dict(GOOD, id="")),
            ("start is required", {k: v for k, v in GOOD.items() if k != "start"}),
            ("not an object of strings", dict(GOOD, text=["a"])),
            ("not an object of strings", "text"),
            ("link_text and url go together", dict(LINK, link_text="")),
            ("end is not after start", dict(GOOD, end="2026-08-02T00:00-04:00")),
            ("newest first", older, GOOD),
            ("duplicate id", GOOD, GOOD),
        ]
        cases += [("not an absolute https URL", dict(LINK, url=url)) for url in (
            "http://bit.ly/x", "https://https://status.arxiv.org", "https://logout",
            "javascript:alert(1)", "/about", "https://[broken")]
        cases += [("not an ISO 8601 time with its offset", dict(GOOD, start=t)) for t in (
            "2026-08-03T00:00", "2026-13-01T00:00Z", "2026-08-03 00:00-04:00",
            "20260803T0000-0400", "tomorrow")]
        for expected, *entries in cases:
            found = problems(*entries)
            self.assertTrue(any(expected in p for p in found), f"{expected!r} not in {found}")

    def test_the_file_is_an_object_holding_a_list(self):
        for data in ([GOOD], {"announcements": GOOD}):
            self.assertEqual(u.check_announcements(data), ['expected {"announcements": [...]}'])


if __name__ == "__main__":
    unittest.main()
