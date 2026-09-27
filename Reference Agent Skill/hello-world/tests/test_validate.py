"""Tests for independent welcome-pack artifact validation."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RENDER = ROOT / "scripts" / "render.py"
VALIDATE = ROOT / "scripts" / "validate.py"
EXAMPLES = ROOT / "examples"


class ValidateTests(unittest.TestCase):
    def render(self, fixture: str, output: Path) -> None:
        result = subprocess.run(
            [sys.executable, str(RENDER), "--input", str(EXAMPLES / fixture), "--output", str(output)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def validate(self, output: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATE), str(output)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_contributor_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            self.render("contributor.json", output)
            result = self.validate(output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("audience=contributor", result.stdout)

    def test_valid_user_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            self.render("user.json", output)
            result = self.validate(output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("audience=user", result.stdout)

    def test_corrupted_markdown_returns_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            self.render("contributor.json", output)
            path = output / "WELCOME.md"
            path.write_text(
                path.read_text(encoding="utf-8").replace("## First tiny change", "## Removed section"),
                encoding="utf-8",
                newline="\n",
            )
            result = self.validate(output)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("section", result.stderr.lower())

    def test_missing_artifact_returns_nonzero(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out"
            output.mkdir()
            result = self.validate(output)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("WELCOME.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
