"""Validate Agent Plugins 1.0.0 package structure offline."""

import argparse
import json
from pathlib import Path
import re
import sys

from validate_skill import Issue, print_issues, validate_skill

PLUGIN_SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
MCP_SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json'
MANIFEST_KEYS = {'$schema', 'name', 'version', 'description', 'author', 'homepage', 'repository', 'license', 'keywords', 'extensions'}
PLUGIN_NAME = re.compile(r'[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?\Z')
NAMESPACE = re.compile(r'[a-z0-9]+(?:\.[a-z0-9-]+){2,}\Z')


def _json(path: Path) -> object:
    """Read a JSON file while rejecting duplicate object keys."""
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'duplicate JSON key: {key}')
            result[key] = value
        return result
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique)


def _manifest(root: Path) -> tuple[list[Issue], dict | None]:
    """Validate the plugin manifest under strict authoring rules."""
    path = root / 'plugin.json'
    issues = []
    if not path.resolve().is_relative_to(root.resolve()):
        return [Issue('ERROR', str(path), 'manifest-containment', 'manifest resolves outside plugin root')], None
    if not path.is_file():
        return [Issue('ERROR', str(path), 'manifest-entry', 'regular root plugin.json required')], None
    try:
        data = _json(path)
    except (ValueError, OSError, UnicodeError) as error:
        return [Issue('ERROR', str(path), 'manifest-json', str(error))], None
    if not isinstance(data, dict):
        return [Issue('ERROR', str(path), 'manifest-object', 'manifest must be an object')], None
    def error(rule, message):
        issues.append(Issue('ERROR', str(path), rule, message))
    if data.get('$schema') != PLUGIN_SCHEMA:
        error('manifest-schema', f'$schema must equal {PLUGIN_SCHEMA}')
    name = data.get('name')
    if not isinstance(name, str) or not PLUGIN_NAME.fullmatch(name) or '--' in name or '..' in name:
        error('manifest-name', 'name must be 1–64 lowercase alphanumeric, period, hyphen; alphanumeric at ends; no -- or ..')
    for key in sorted(data.keys() - MANIFEST_KEYS):
        error('manifest-unknown', f'unknown field {key!r}; clients report and ignore it, but strict authoring fails')
    for key in ('version', 'description', 'homepage', 'repository', 'license'):
        if key in data and not isinstance(data[key], str):
            error('manifest-type', f'{key} must be a string')
    if 'keywords' in data and (not isinstance(data['keywords'], list) or any(not isinstance(s, str) for s in data['keywords'])):
        error('manifest-keywords', 'keywords must be a string array')
    if 'author' in data:
        author = data['author']
        if not isinstance(author, dict) or set(author) - {'name','email','url'} or any(not isinstance(s, str) for s in author.values()):
            error('manifest-author', 'author must have only name/email/url string fields')
    if 'extensions' in data:
        ext = data['extensions']
        if not isinstance(ext, dict):
            error('extensions', 'extensions must be an object; clients report and ignore a non-object field')
        else:
            for namespace, value in sorted(ext.items()):
                if not NAMESPACE.fullmatch(namespace) or not isinstance(value, dict):
                    error('extensions', f'{namespace!r} must be a reverse-domain namespace with object value')
    return issues, data


def validate_plugin(path: Path) -> list[Issue]:
    """Return ordered strict findings for a plugin package.

    Args:
        path: Plugin root. Never launches bundled programs.

    Returns:
        All available structural findings, including independent components.
    """
    root = Path(path)
    if not root.is_dir():
        return [Issue('ERROR', str(root), 'plugin-root', 'plugin directory required')]
    issues, manifest = _manifest(root)
    return issues


def main() -> int:
    """Run the plugin structural validator CLI."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path, help='plugin directory')
    args = parser.parse_args()
    if not args.path.exists():
        parser.error(f'path does not exist: {args.path}')
    issues = validate_plugin(args.path)
    print_issues(issues)
    return 1 if any(i.severity == 'ERROR' for i in issues) else 0


if __name__ == '__main__':
    sys.exit(main())
