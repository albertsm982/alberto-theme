import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
COLOR_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?$")


def load_json(path):
    with path.open(encoding="utf-8") as file:
        return json.load(file)


class ThemeTests(unittest.TestCase):
    def test_manifest_declares_existing_theme_files(self):
        package = load_json(ROOT / "package.json")
        themes = package.get("contributes", {}).get("themes", [])

        self.assertTrue(themes, "package.json no declara ningún tema")

        for entry in themes:
            with self.subTest(theme=entry.get("label")):
                self.assertIn("label", entry)
                self.assertIn("path", entry)
                self.assertIn(entry.get("uiTheme"), {"vs", "vs-dark", "hc-black", "hc-light"})

                theme_path = ROOT / entry["path"]
                self.assertTrue(theme_path.is_file(), f"No existe el tema: {theme_path}")
                theme = load_json(theme_path)
                self.assertEqual(theme.get("name"), entry["label"])

    def test_theme_colors_and_token_rules(self):
        package = load_json(ROOT / "package.json")
        themes = package.get("contributes", {}).get("themes", [])

        for entry in themes:
            theme = load_json(ROOT / entry["path"])
            with self.subTest(theme=entry["label"]):
                self.assertIsInstance(theme.get("colors"), dict)
                self.assertTrue(theme["colors"], "El tema no define colores de interfaz")
                self.assertIsInstance(theme.get("tokenColors"), list)
                self.assertTrue(theme["tokenColors"], "El tema no define colores de sintaxis")

                for name, color in theme["colors"].items():
                    with self.subTest(color_id=name):
                        self.assertIsInstance(color, str)
                        self.assertRegex(color, COLOR_PATTERN)

                for index, rule in enumerate(theme["tokenColors"]):
                    with self.subTest(token_rule=index):
                        self.assertIsInstance(rule, dict)
                        scopes = rule.get("scope")
                        self.assertTrue(scopes, "Cada regla debe declarar al menos un scope")
                        if isinstance(scopes, str):
                            scopes = [scopes]
                        self.assertIsInstance(scopes, list)
                        self.assertTrue(all(isinstance(scope, str) and scope for scope in scopes))

                        settings = rule.get("settings")
                        self.assertIsInstance(settings, dict)
                        for key in ("foreground", "background"):
                            if key in settings:
                                self.assertRegex(settings[key], COLOR_PATTERN)


if __name__ == "__main__":
    unittest.main(verbosity=2)