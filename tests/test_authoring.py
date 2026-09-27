"""Check the creator's usable routing and design contracts."""

from pathlib import Path
import subprocess
import sys
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

    def test_three_example_packages_validate_and_work(self):
        examples = ROOT / 'examples'
        script = CREATOR / 'scripts'
        for kind, path in [('validate_skill.py', examples/'standalone'/'word-count'),
                           ('validate_plugin.py', examples/'multi-skill'/'notes-tools'),
                           ('validate_plugin.py', examples/'with-mcp'/'notes-tools')]:
            result = subprocess.run([sys.executable, str(script/kind), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        counter = examples/'standalone'/'word-count'/'scripts'/'count_words.py'
        run = subprocess.run([sys.executable, str(counter), 'one two three'], capture_output=True, text=True)
        self.assertEqual((run.returncode, run.stdout.strip()), (0, '3'))
        for root in ('multi-skill', 'with-mcp'):
            base = examples/root/'notes-tools'/'skills'
            for skill, expected in [('outline-notes', '- First'), ('check-note-links', 'missing: absent.md')]:
                tool = next((base/skill/'scripts').glob('*.py'))
                result = subprocess.run([sys.executable, str(tool), str(examples/'standalone'/'sample.md')], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(expected, result.stdout)

    def test_invalid_package_and_bad_invocation_have_distinct_exit_codes(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'bad-skill'
            root.mkdir()
            (root / 'SKILL.md').write_text('bad')
            script = CREATOR / 'scripts/validate_skill.py'
            invalid = subprocess.run([sys.executable, str(script), str(root)], capture_output=True, text=True)
            missing = subprocess.run([sys.executable, str(script), str(root/'absent')], capture_output=True, text=True)
            self.assertEqual((invalid.returncode, missing.returncode), (1, 2))
            self.assertIn('frontmatter', invalid.stdout)

    def test_authoring_requires_collision_check_before_overwrite(self):
        body = (CREATOR / 'references/authoring-workflow.md').read_text()
        self.assertIn('Before writing into an existing target or installing', body)
        self.assertIn('never overwrite an unrelated item', body)

    def test_creator_skill_validates_itself(self):
        result = subprocess.run([sys.executable, str(CREATOR/'scripts/validate_skill.py'), str(CREATOR)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_external_entry_symlink_is_rejected_without_reading_it(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'sample'
            root.mkdir()
            outside = Path(temp) / 'outside.md'
            outside.write_text('---\nname: sample\ndescription: Outside\n---\n# Outside')
            (root / 'SKILL.md').symlink_to(outside)
            result = subprocess.run([sys.executable, str(CREATOR/'scripts/validate_skill.py'), str(root)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('entry-containment', result.stdout)

    def test_example_mcp_server_handles_initialize_and_tool_list(self):
        import json
        server = ROOT/'examples/with-mcp/notes-tools/bin/notes_server.py'
        requests = [{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2025-06-18','capabilities':{},'clientInfo':{'name':'test','version':'1'}}},
                    {'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}}]
        result = subprocess.run([sys.executable,str(server)],input='\n'.join(map(json.dumps,requests))+'\n',capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        responses=[json.loads(line) for line in result.stdout.splitlines()]
        self.assertEqual(responses[0]['result']['serverInfo']['name'],'note-heading-index')
        self.assertEqual(responses[1]['result']['tools'][0]['name'],'headings')


if __name__ == '__main__':
    unittest.main()
