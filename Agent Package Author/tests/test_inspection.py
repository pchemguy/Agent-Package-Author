"""Read-only package inventory acceptance tests."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'agent-package-author/scripts/inspect_package.py'


class InspectionTests(unittest.TestCase):
    def test_plugin_inventory_and_invalid_child_without_execution(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'sample-plugin'
            root.mkdir()
            (root / 'plugin.json').write_text(json.dumps({'$schema':'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json','name':'sample-plugin'}))
            child = root / 'skills' / 'alpha'
            child.mkdir(parents=True)
            (child / 'SKILL.md').write_text('broken')
            marker = root / 'side-effect'
            (root / 'run.py').write_text(f'from pathlib import Path\nPath({str(marker)!r}).touch()')
            result = subprocess.run([sys.executable, str(SCRIPT), str(root)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('skill: alpha', result.stdout)
            self.assertIn('errors:', result.stdout)
            self.assertFalse(marker.exists())

    def test_standalone_inventory(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'standalone'
            root.mkdir()
            (root / 'SKILL.md').write_text('---\nname: standalone\ndescription: Use for standalone examples\n---\n\n# Standalone')
            result = subprocess.run([sys.executable, str(SCRIPT), str(root)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertIn('PACKAGE: skill', result.stdout)


if __name__ == '__main__':
    unittest.main()
