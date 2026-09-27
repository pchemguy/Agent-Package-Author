"""Pin the format boundaries used by offline validation."""

import json
from pathlib import Path
import unittest


class StandardsBaselineTests(unittest.TestCase):
    def test_format_fixture_pins_versions_and_discovery(self):
        fixture = json.loads((Path(__file__).parent / 'fixtures' / 'format-cases.json').read_text())
        self.assertEqual(fixture['plugin_schema'], 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json')
        self.assertEqual(fixture['mcp_schema'], 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json')
        self.assertIn('skills/example/SKILL.md', fixture['discovery']['included'])
        self.assertIn('skills/example/subskills/nested/SKILL.md', fixture['discovery']['excluded'])
        self.assertIn('.', fixture['plugin_name_alphabet'])
        self.assertNotIn('.', fixture['skill_name_alphabet'])


if __name__ == '__main__':
    unittest.main()
