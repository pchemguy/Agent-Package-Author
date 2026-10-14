"""Exercise strict plugin manifest and discovery validation."""

import importlib.util
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'agent-package-author/scripts'


def load():
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location('validate_plugin', SCRIPTS / 'validate_plugin.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class PluginValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'example-plugin'
        self.root.mkdir()

    def manifest(self, **changes):
        value = {'$schema':'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json', 'name':'example-plugin'}
        value.update(changes)
        (self.root / 'plugin.json').write_text(json.dumps(value))

    def sibling_skills(self):
        self.manifest()
        for name in ('alpha', 'beta'):
            skill = self.root / 'skills' / name
            (skill / 'references').mkdir(parents=True)
            (skill / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: Run {name}\n---\n\n# {name}\n')
        (self.root / 'skills/beta/references/shared.md').write_text('# Shared guidance\n')
        (self.root / 'skills/alpha/references/local.md').write_text('# Local guidance\n')
        return self.root / 'skills/alpha/SKILL.md'

    def test_sibling_entry_and_reference_are_warning_only(self):
        entry = self.sibling_skills()
        entry.write_text(entry.read_text() + '\n[Local](references/local.md)\n'
                         '[Handoff](../beta/SKILL.md)\n'
                         '[Shared](../beta/references/shared.md)\n')
        issues = load().validate_plugin(self.root)
        self.assertEqual([i for i in issues if i.severity == 'ERROR'], [])
        self.assertEqual([(i.severity, i.rule) for i in issues],
                         [('WARN', 'resource-cross-skill')] * 2)
        validator = subprocess.run([sys.executable, str(SCRIPTS / 'validate_plugin.py'), str(self.root)],
                                   capture_output=True, text=True)
        inspector = subprocess.run([sys.executable, str(SCRIPTS / 'inspect_package.py'), str(self.root)],
                                   capture_output=True, text=True)
        self.assertEqual(validator.returncode, 0, validator.stdout)
        self.assertEqual(inspector.returncode, 0, inspector.stdout)
        self.assertIn('warnings: 2', inspector.stdout)

    def test_missing_sibling_file_is_error(self):
        entry = self.sibling_skills()
        entry.write_text(entry.read_text() + '\n[Missing](../beta/references/absent.md)\n')
        issues = load().validate_plugin(self.root)
        self.assertTrue(any(i.severity == 'ERROR' and i.rule == 'resource-missing' for i in issues))

    def test_plugin_escape_and_symlink_escape_are_errors(self):
        entry = self.sibling_skills()
        outside = Path(self.temp.name) / 'outside.md'
        outside.write_text('# Outside\n')
        (self.root / 'skills/beta/references/external.md').symlink_to(outside)
        entry.write_text(entry.read_text() + '\n[Traversal](../../../outside.md)\n'
                         '[Symlink](../beta/references/external.md)\n')
        issues = load().validate_plugin(self.root)
        self.assertEqual(sum(i.severity == 'ERROR' and i.rule == 'resource-escape' for i in issues), 2)

    def test_presentation_generator_accepts_bundled_reference(self):
        entry = self.sibling_skills()
        entry.write_text(entry.read_text() + '\n[Shared](../beta/references/shared.md)\n')
        result = subprocess.run([sys.executable, str(SCRIPTS / 'create_openai_presentation.py'), str(self.root)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.root / 'skills/alpha/agents/openai.yaml').is_file())

    def test_minimal_manifest_and_dotted_name(self):
        self.manifest(name='example.plugin')
        self.assertEqual(load().validate_plugin(self.root), [])

    def test_unknown_field_and_invalid_metadata_type(self):
        self.manifest(commands=['not portable'])
        self.assertTrue(any(i.rule == 'manifest-unknown' for i in load().validate_plugin(self.root)))
        self.manifest(author={'name': 42})
        self.assertTrue(any(i.rule == 'manifest-author' for i in load().validate_plugin(self.root)))

    def test_schema_and_manifest_escape(self):
        self.manifest(**{'$schema':'https://agent-plugins.org/schemas/2.0.0/plugin.schema.json'})
        self.assertTrue(any(i.rule == 'manifest-schema' for i in load().validate_plugin(self.root)))
        (self.root / 'plugin.json').unlink()
        (self.root / 'plugin.json').symlink_to(Path(self.temp.name) / 'external.json')
        self.assertTrue(any(i.rule == 'manifest-containment' for i in load().validate_plugin(self.root)))

    def test_non_object_extensions_is_strict_error_with_client_note(self):
        self.manifest(extensions='bad')
        issues = load().validate_plugin(self.root)
        self.assertTrue(any(i.rule == 'extensions' and 'client' in i.message for i in issues))

    def test_extension_namespace_two_or_more_labels(self):
        for namespace in ('com.openai', 'com.example.product', 'co.ex-ample'):
            with self.subTest(namespace=namespace):
                self.manifest(extensions={namespace: {}})
                self.assertEqual(load().validate_plugin(self.root), [])

    def test_malformed_extension_namespace_and_nonobject_value(self):
        for namespace in ('com', 'com..openai', 'Com.openai', 'com.-openai', 'com.openai-'):
            with self.subTest(namespace=namespace):
                self.manifest(extensions={namespace: {}})
                issues = load().validate_plugin(self.root)
                self.assertTrue(any(i.rule == 'extensions' and 'namespace' in i.message for i in issues))
        self.manifest(extensions={'com.openai': []})
        issues = load().validate_plugin(self.root)
        self.assertTrue(any(i.rule == 'extensions' and 'object value' in i.message for i in issues))
        self.assertFalse(any('namespace' in i.message for i in issues))

    def test_immediate_skills_are_validated_independently(self):
        self.manifest()
        for name in ('alpha', 'beta'):
            skill = self.root / 'skills' / name
            skill.mkdir(parents=True)
            (skill / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: Run {name}\n---\n\n# {name}\n')
        self.assertEqual(load().validate_plugin(self.root), [])
        (self.root / 'skills/beta/SKILL.md').write_text('broken')
        self.assertTrue(any('beta' in i.path for i in load().validate_plugin(self.root)))

    def test_wrong_kind_skills_and_escaping_child(self):
        self.manifest()
        (self.root / 'skills').write_text('not a directory')
        self.assertTrue(any(i.rule == 'skills-kind' for i in load().validate_plugin(self.root)))
        (self.root / 'skills').unlink()
        (self.root / 'skills').mkdir()
        (self.root / 'skills/outer').symlink_to(Path(self.temp.name))
        self.assertTrue(any(i.rule == 'skill-containment' for i in load().validate_plugin(self.root)))

    def test_extension_directory_must_be_contained(self):
        self.manifest()
        for namespace in ('com.openai', 'com.example.client'):
            with self.subTest(namespace=namespace):
                link = self.root / namespace
                link.symlink_to(Path(self.temp.name), target_is_directory=True)
                self.assertTrue(any(i.rule == 'extension-containment' for i in load().validate_plugin(self.root)))
                link.unlink()

    def test_two_label_directory_and_unrelated_dotted_folder(self):
        self.manifest()
        (self.root / 'com.openai').mkdir()
        (self.root / 'docs.v2-').mkdir()
        self.assertEqual(load().validate_plugin(self.root), [])


if __name__ == '__main__':
    unittest.main()
