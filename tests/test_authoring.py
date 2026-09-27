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

    def test_skill_resources_are_optional_and_example_is_not_mandatory(self):
        standard = (CREATOR / 'references/skill-standard.md').read_text()
        design = (CREATOR / 'references/skill-design.md').read_text()
        exemplar = (CREATOR / 'references/hello-world-example.md').read_text()
        self.assertIn('optional', standard.lower())
        self.assertIn('activation', design.lower())
        self.assertIn('not a mandatory', exemplar.lower())
        self.assertIn('description:', (CREATOR / 'assets/skill-entry-template.md').read_text())

    def test_plugin_templates_have_canonical_schemas(self):
        import json
        manifest = json.loads((CREATOR / 'assets/plugin-manifest-template.json').read_text())
        mcp = json.loads((CREATOR / 'assets/mcp-template.json').read_text())
        self.assertEqual(manifest['$schema'], 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json')
        self.assertEqual(mcp['$schema'], 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json')
        self.assertNotIn('mcpServers', manifest)
        self.assertIn('immediate', (CREATOR / 'references/plugin-standard.md').read_text())


if __name__ == '__main__':
    unittest.main()
