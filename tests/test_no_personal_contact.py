"""No notebook may send a personal email address to an external service.

User-Agent strings and ``mailto=`` parameters carry a contact address. Use
``noreply@example.org``; this fails if a personal address appears anywhere in
a notebook, a script or a test.

Run with: python3 -m unittest discover -s tests
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Assembled so this file does not match its own scan.
PERSONAL = re.compile(r"[A-Za-z0-9._%+-]+@" + "mattartz" + r"\.me", re.IGNORECASE)
SUFFIXES = {".ipynb", ".py", ".sh"}


def personal_hits(paths, root=ROOT):
    hits = []
    for p in paths:
        for n, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
            if PERSONAL.search(line):
                hits.append(f"{p.relative_to(root)}:{n}")
    return hits


def code_files(root=ROOT):
    return sorted(p for p in root.rglob("*")
                  if p.is_file() and p.suffix in SUFFIXES and ".git" not in p.parts)


class NoPersonalContact(unittest.TestCase):
    def test_no_personal_address_in_notebooks_or_scripts(self):
        self.assertEqual(personal_hits(code_files()), [])

    def test_the_scan_covers_the_notebooks(self):
        self.assertGreater(len([p for p in code_files() if p.suffix == ".ipynb"]), 10)

    def test_the_scan_catches_a_planted_address(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            nb = Path(d) / "planted.ipynb"
            nb.write_text('{"source": ["UA = \\"x/1.0 (someone@' + "mattartz" + '.me)\\""]}\n')
            self.assertEqual(personal_hits(code_files(Path(d)), Path(d)), ["planted.ipynb:1"])

    def test_the_contact_address_and_the_website_are_allowed(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            ok = Path(d) / "ok.py"
            ok.write_text("UA = 'x/1.0 (noreply@example.org)'  # https://www.mattartz.me/\n")
            self.assertEqual(personal_hits([ok], Path(d)), [])


if __name__ == "__main__":
    unittest.main()
