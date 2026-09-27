"""Exercise strict plugin manifest and discovery validation."""

import importlib.util
import json
from pathlib import Path
import sys
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


if __name__ == '__main__':
    unittest.main()
