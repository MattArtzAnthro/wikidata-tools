"""No notebook may use a personal email address as an API contact.

User-Agent strings and ``mailto=`` parameters carry a contact address. Use
``noreply@example.org``. Citing the address (an author line in a notebook) is
fine; this fails if one is used as a request contact.

Run with: python3 -m unittest discover -s tests
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Assembled so this file does not match its own scan.
PERSONAL = re.compile(r"[A-Za-z0-9._%+-]+@" + "mattartz" + r"\.me", re.IGNORECASE)
SUFFIXES = {".ipynb", ".py", ".sh"}

# A personal address is allowed as a citation (README, LICENSE, author metadata) and
# refused as an API contact: a request marker on the line or the two lines before it.
LINKS = re.compile(r"\]\(mailto:[^)\s]*\)|<mailto:[^>\s]*>|href=[\"']mailto:[^\"']*[\"']",
                   re.IGNORECASE)
MARK_ANYCASE = re.compile(r"mailto|user[-_ ]?agent|polite|contact_email|user_agent_contact"
                          r"|--contact|headers\s*=|params\s*=", re.IGNORECASE)
MARK_CONST = re.compile(r"\bUA\b|\b[A-Z_]*(?:EMAIL|MAILTO|CONTACT)[A-Z_]*\s*[:=]")


def contact_lines(lines):
    """1-based numbers of lines that use a personal address as a request contact."""
    hits = []
    for i, line in enumerate(lines):
        if PERSONAL.search(LINKS.sub("", line)):
            context = LINKS.sub("", "\n".join(lines[max(0, i - 2):i + 1]))
            if MARK_ANYCASE.search(context) or MARK_CONST.search(context):
                hits.append(i + 1)
    return hits


def personal_hits(paths, root=ROOT):
    hits = []
    for p in paths:
        lines = p.read_text(errors="ignore").splitlines()
        hits += [f"{p.relative_to(root)}:{n}" for n in contact_lines(lines)]
    return hits


def code_files(root=ROOT):
    return sorted(p for p in root.rglob("*")
                  if p.is_file() and p.suffix in SUFFIXES and ".git" not in p.parts)


class NoPersonalContact(unittest.TestCase):
    def test_no_personal_address_used_as_a_contact(self):
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

    def test_an_author_line_in_a_notebook_is_allowed(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            nb = Path(d) / "a.ipynb"
            nb.write_text('{"source": ["Created by Matt Artz, research@' + "mattartz" + '.me"]}\n')
            self.assertEqual(personal_hits([nb], Path(d)), [])


if __name__ == "__main__":
    unittest.main()
