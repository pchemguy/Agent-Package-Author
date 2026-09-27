"""Check the creator's usable routing and design contracts."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CREATOR = ROOT / 'agent-package-author'


class AuthoringTests(unittest.TestCase):
    def test_entry_routes_both_modes_and_optional_mcp(self):
        body = (CREATOR / 'SKILL.md').read_text()
        self.assertIn('name: agent-package-author', body)
        self.assertIn('standalone', body)
        self.assertIn('plugin', body.lower())
        self.assertIn('references/mcp-packaging.md', body)
        self.assertIn('only if', body.lower())
        self.assertIn('references/hello-world-example.md', body)

    def test_shared_workflow_guards_collisions(self):
        body = (CREATOR / 'references/authoring-workflow.md').read_text()
        self.assertIn('collision', body.lower())
        self.assertIn('before', body.lower())
        self.assertIn('acceptance', body.lower())


if __name__ == '__main__':
    unittest.main()
