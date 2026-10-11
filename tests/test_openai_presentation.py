"""Exercise contextual OpenAI presentation generation for skills and plugins."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'agent-package-author/scripts/create_openai_presentation.py'


class PresentationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)

    def run_generator(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], capture_output=True, text=True)

    @staticmethod
    def clear_presentation(skill):
        (skill / 'agents/openai.yaml').unlink(missing_ok=True)
        (skill / 'assets/icon.svg').unlink(missing_ok=True)

    def test_standalone_derives_metadata_and_icon_from_skill(self):
        skill = self.path / 'word-count'
        shutil.copytree(ROOT / 'examples/standalone/word-count', skill)
        self.clear_presentation(skill)
        result = self.run_generator(skill)
        self.assertEqual(result.returncode, 0, result.stderr)
        metadata = (skill / 'agents/openai.yaml').read_text()
        self.assertIn('display_name: "Word Count"', metadata)
        self.assertIn('icon_small: "./assets/icon.svg"', metadata)
        self.assertIn('icon_large: "./assets/icon.svg"', metadata)
        self.assertIn('$word-count', metadata)
        self.assertTrue(25 <= len(json.loads(next(line.split(': ', 1)[1] for line in metadata.splitlines() if 'short_description:' in line))) <= 64)
        root = ElementTree.parse(skill / 'assets/icon.svg').getroot()
        self.assertEqual(root.attrib['viewBox'], '0 0 128 128')
        self.assertIn('WC', (skill / 'assets/icon.svg').read_text())

    def test_plugin_generates_distinct_contextual_files_per_child(self):
        plugin = self.path / 'notes-tools'
        shutil.copytree(ROOT / 'examples/multi-skill/notes-tools', plugin)
        for child in (plugin / 'skills').iterdir():
            self.clear_presentation(child)
        context = self.path / 'context.json'
        context.write_text(json.dumps({'skills': {
            'outline-notes': {'display_name': 'Note Outliner', 'short_description': 'Outline headings from Markdown notes', 'default_prompt': 'Use $outline-notes to outline this note.', 'brand_color': '#315F91', 'icon_label': 'NO', 'icon_motif': 'document'},
            'check-note-links': {'display_name': 'Note Link Checker', 'short_description': 'Find broken links in local Markdown notes', 'default_prompt': 'Use $check-note-links to check these links.', 'brand_color': '#8155AA', 'icon_label': 'LC', 'icon_motif': 'check'}
        }}))
        result = self.run_generator(plugin, '--context', context)
        self.assertEqual(result.returncode, 0, result.stderr)
        for name, label in [('outline-notes', 'NO'), ('check-note-links', 'LC')]:
            child = plugin / 'skills' / name
            self.assertIn(f'${name}', (child / 'agents/openai.yaml').read_text())
            self.assertIn(label, (child / 'assets/icon.svg').read_text())
            ElementTree.parse(child / 'assets/icon.svg')
        self.assertFalse((plugin / 'agents/openai.yaml').exists())

    def test_existing_output_refused_without_force_then_stable_on_regeneration(self):
        skill = self.path / 'word-count'
        shutil.copytree(ROOT / 'examples/standalone/word-count', skill)
        self.clear_presentation(skill)
        self.assertEqual(self.run_generator(skill).returncode, 0)
        yaml = (skill / 'agents/openai.yaml').read_bytes()
        svg = (skill / 'assets/icon.svg').read_bytes()
        self.assertNotEqual(self.run_generator(skill).returncode, 0)
        self.assertEqual(self.run_generator(skill, '--force').returncode, 0)
        self.assertEqual((skill / 'agents/openai.yaml').read_bytes(), yaml)
        self.assertEqual((skill / 'assets/icon.svg').read_bytes(), svg)

    def test_bad_context_fails_before_writing(self):
        skill = self.path / 'word-count'
        shutil.copytree(ROOT / 'examples/standalone/word-count', skill)
        self.clear_presentation(skill)
        context = self.path / 'bad.json'
        context.write_text(json.dumps({'default_prompt': 'Missing invocation', 'brand_color': '#abc'}))
        result = self.run_generator(skill, '--context', context)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((skill / 'agents/openai.yaml').exists())

    def test_long_skill_name_and_description_derive_valid_defaults(self):
        name = 'a' * 64
        skill = self.path / name
        skill.mkdir()
        (skill / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: ' +
                                        'Review Markdown documents and generate a detailed, consistent outline for every requested section.\n---\n\n# Review\n')
        result = self.run_generator(skill)
        self.assertEqual(result.returncode, 0, result.stderr)
        metadata = (skill / 'agents/openai.yaml').read_text()
        short = json.loads(next(line.split(': ', 1)[1] for line in metadata.splitlines() if 'short_description:' in line))
        self.assertTrue(25 <= len(short) <= 64)
        self.assertIn(f'${name}', metadata)

    def test_invalid_second_plugin_child_never_writes_first(self):
        plugin = self.path / 'notes-tools'
        shutil.copytree(ROOT / 'examples/multi-skill/notes-tools', plugin)
        for child in (plugin / 'skills').iterdir():
            self.clear_presentation(child)
        context = self.path / 'bad-plugin.json'
        context.write_text(json.dumps({'skills': {'outline-notes': {'brand_color': 'not-a-color'}}}))
        result = self.run_generator(plugin, '--context', context)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((plugin / 'skills/check-note-links/agents/openai.yaml').exists())
        self.assertFalse((plugin / 'skills/outline-notes/agents/openai.yaml').exists())

    def test_plugin_skills_symlink_cannot_write_outside_package(self):
        plugin = self.path / 'linked-plugin'
        plugin.mkdir()
        (plugin / 'plugin.json').write_text('{}')
        external = self.path / 'external'
        shutil.copytree(ROOT / 'examples/multi-skill/notes-tools/skills', external)
        for child in external.iterdir():
            self.clear_presentation(child)
        (plugin / 'skills').symlink_to(external, target_is_directory=True)
        result = self.run_generator(plugin)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((external / 'outline-notes/agents/openai.yaml').exists())


if __name__ == '__main__':
    unittest.main()
