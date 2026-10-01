"""Behavioral tests of offline Agent Skill validation."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'agent-package-author/scripts/validate_skill.py'


def load():
    import sys
    spec = importlib.util.spec_from_file_location('validate_skill', SOURCE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'example-skill'
        self.root.mkdir()

    def write(self, metadata='name: example-skill\ndescription: "Handles files: when requested"'):
        (self.root / 'SKILL.md').write_text('---\n' + metadata + '\n---\n\n# Example\n')

    def test_valid_minimal_and_quoted_description(self):
        self.write()
        self.assertEqual(load().validate_skill(self.root), [])

    def test_missing_frontmatter_and_mismatched_directory(self):
        self.write('name: wrong\ndescription: Valid description')
        self.assertTrue(any(i.rule == 'name-directory' for i in load().validate_skill(self.root)))
        (self.root / 'SKILL.md').write_text('# No frontmatter')
        self.assertTrue(any(i.rule == 'frontmatter' for i in load().validate_skill(self.root)))

    def test_duplicate_and_unsupported_yaml_does_not_pass(self):
        self.write('name: example-skill\nname: example-skill\ndescription: test')
        self.assertTrue(any(i.rule == 'frontmatter' for i in load().validate_skill(self.root)))
        self.write('name: example-skill\ndescription: [flow, syntax]')
        self.assertTrue(any(i.rule == 'frontmatter-unverified' for i in load().validate_skill(self.root)))

    def test_optional_metadata_and_length(self):
        self.write('name: example-skill\ndescription: Valid\nmetadata:\n  author: Example')
        self.assertEqual(load().validate_skill(self.root), [])
        self.write('name: example-skill\ndescription: Valid\ncompatibility: ' + 'x'*501)
        self.assertTrue(any(i.rule == 'compatibility' for i in load().validate_skill(self.root)))

    def test_reference_links_are_contained_and_exist(self):
        self.write()
        (self.root / 'SKILL.md').write_text((self.root / 'SKILL.md').read_text() + '\nSee [guide](references/guide.md).\n')
        issues = load().validate_skill(self.root)
        self.assertTrue(any(i.rule == 'resource-missing' for i in issues))
        (self.root / 'references').mkdir()
        (self.root / 'references/guide.md').write_text('Guidance')
        self.assertEqual(load().validate_skill(self.root), [])
        (self.root / 'references/guide.md').unlink()
        (self.root / 'references/guide.md').symlink_to(Path(self.temp.name) / 'external.md')
        self.assertTrue(any(i.rule == 'resource-escape' for i in load().validate_skill(self.root)))

    def test_parent_traversal_is_rejected(self):
        self.write()
        (self.root / 'SKILL.md').write_text((self.root / 'SKILL.md').read_text() + '\n[bad](../other/SKILL.md)\n')
        self.assertTrue(any(i.rule == 'resource-escape' for i in load().validate_skill(self.root)))

    def test_invalid_yaml_scalars_do_not_pass_and_quoted_comment_works(self):
        self.write('name: example-skill\ndescription: Use when key: value')
        self.assertTrue(any(i.rule == 'frontmatter-unverified' for i in load().validate_skill(self.root)))
        self.write('name: example-skill\ndescription: "bad\\q"')
        self.assertTrue(any(i.rule == 'frontmatter-unverified' for i in load().validate_skill(self.root)))
        self.write('name: example-skill\ndescription: "Valid: quoted" # comment')
        self.assertEqual(load().validate_skill(self.root), [])


if __name__ == '__main__':
    unittest.main()
