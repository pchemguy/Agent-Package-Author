"""Tests for the deterministic welcome-pack renderer."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RENDER = ROOT / "scripts" / "render.py"
EXAMPLES = ROOT / "examples"


class RenderTests(unittest.TestCase):
    def run_render(self, fixture: str, output: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(RENDER), "--input", str(EXAMPLES / fixture), "--output", str(output)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_contributor_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            result = self.run_render("contributor.json", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            markdown = (output / "WELCOME.md").read_text(encoding="utf-8")
            manifest = json.loads((output / "welcome.json").read_text(encoding="utf-8"))
            self.assertIn("## First tiny change", markdown)
            self.assertNotIn("## Where to get help", markdown)
            self.assertEqual(manifest["audience"], "contributor")

    def test_user_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            result = self.run_render("user.json", output)
            self.assertEqual(result.returncode, 0, result.stderr)
            markdown = (output / "WELCOME.md").read_text(encoding="utf-8")
            manifest = json.loads((output / "welcome.json").read_text(encoding="utf-8"))
            self.assertIn("## Where to get help", markdown)
            self.assertNotIn("## First tiny change", markdown)
            self.assertEqual(manifest["audience"], "user")

    def test_invalid_input_returns_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = self.run_render("invalid.json", Path(tmp) / "out")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("audience", result.stderr)

    def test_rendering_is_byte_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = root / "first"
            second = root / "second"
            r1 = self.run_render("contributor.json", first)
            r2 = self.run_render("contributor.json", second)
            self.assertEqual(r1.returncode, 0, r1.stderr)
            self.assertEqual(r2.returncode, 0, r2.stderr)
            for name in ("WELCOME.md", "welcome.json"):
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())


if __name__ == "__main__":
    unittest.main()
