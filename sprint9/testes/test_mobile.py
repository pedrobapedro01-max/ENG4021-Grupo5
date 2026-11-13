"""Testes independentes e executáveis do protótipo mobile da Sprint 9.
Executar da raiz do repositório: python -m unittest discover -s sprint9/testes -v
Não depende do backend e não valida funcionalidades do site principal.
"""
from pathlib import Path
from html.parser import HTMLParser
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "mobile" / "index.html"

class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = set()
        self.buttons = []
        self.viewport = False
        self.nav = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "section" and "id" in a:
            self.sections.add(a["id"])
        if tag == "button" and "data-go" in a:
            self.buttons.append(a["data-go"])
        if tag == "meta" and a.get("name") == "viewport":
            self.viewport = True
        if tag == "nav" and a.get("aria-label"):
            self.nav = True

class MobilePrototypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML.read_text(encoding="utf-8")
        cls.parser = Structure()
        cls.parser.feed(cls.html)
    def test_responsive_viewport(self):
        self.assertTrue(self.parser.viewport)
        self.assertIn("@media", self.html)
    def test_three_sections(self):
        self.assertEqual(self.parser.sections, {"inicio", "treinos", "alimentacao"})
    def test_navigation_targets_exist(self):
        self.assertTrue(self.parser.nav)
        self.assertTrue(set(self.parser.buttons) <= self.parser.sections)
        self.assertTrue(self.parser.sections <= set(self.parser.buttons))
    def test_basic_accessibility(self):
        self.assertIn('lang="pt-BR"', self.html)
        self.assertIn("focus-visible", self.html)
        self.assertIn("aria-current", self.html)

if __name__ == "__main__":
    unittest.main()
