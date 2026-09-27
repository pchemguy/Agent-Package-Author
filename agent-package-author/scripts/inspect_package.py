"""Inventory a skill or Agent Plugin without executing package content."""

import argparse
from pathlib import Path
import sys

from validate_skill import validate_skill
from validate_plugin import _json, validate_plugin


def inspect(path: Path) -> tuple[list[str], int]:
    """Return deterministic inventory lines and a bounded status code.

    Args:
        path: Existing skill or plugin directory.

    Returns:
        Inventory lines and exit status (zero, invalid package, unknown path).
    """
    root = Path(path)
    if not root.is_dir():
        return ['UNKNOWN: directory required'], 2
    if (root / 'plugin.json').exists() or (root / 'plugin.json').is_symlink():
        lines = ['PACKAGE: plugin', 'STANDARD: Agent Plugins 1.0.0']
        skills = root / 'skills'
        if skills.is_dir() and skills.resolve().is_relative_to(root.resolve()):
            for child in sorted(skills.iterdir(), key=lambda p: p.name):
                if child.is_dir() and (child / 'SKILL.md').exists():
                    lines.append(f'  skill: {child.name}')
        mcp = root / 'mcp.json'
        if mcp.is_file() and mcp.resolve().is_relative_to(root.resolve()):
            try:
                config = _json(mcp)
                entries = config.get('mcpServers', {}) if isinstance(config, dict) else {}
                if isinstance(entries, dict):
                    for name, item in sorted(entries.items()):
                        kind = item.get('type', '?') if isinstance(item, dict) else '?'
                        lines.append(f'  mcp: {name} ({kind})')
            except (OSError, ValueError):
                lines.append('  mcp: unreadable')
        try:
            manifest = _json(root / 'plugin.json')
            if isinstance(manifest, dict) and isinstance(manifest.get('extensions'), dict):
                lines.extend(f'  extension: {name}' for name in sorted(manifest['extensions']))
        except (OSError, ValueError):
            pass
        issues = validate_plugin(root)
    elif (root / 'SKILL.md').is_file():
        lines = ['PACKAGE: skill']
        for name in ('references', 'scripts', 'assets'):
            directory = root / name
            if directory.is_dir() and directory.resolve().is_relative_to(root.resolve()):
                lines.append(f'  {name}: {sum(p.is_file() for p in directory.iterdir())}')
        issues = validate_skill(root)
    else:
        return ['UNKNOWN: no root SKILL.md or plugin.json'], 2
    errors = sum(i.severity == 'ERROR' for i in issues)
    warnings = sum(i.severity == 'WARN' for i in issues)
    lines.append(f'VALIDATION: errors: {errors}, warnings: {warnings}')
    lines.append('RUNTIME: not verified by inventory')
    return lines, 1 if errors else 0


def main() -> int:
    """Run the read-only inventory CLI."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path, help='skill or plugin directory')
    args = parser.parse_args()
    lines, status = inspect(args.path)
    print('\n'.join(lines))
    return status


if __name__ == '__main__':
    sys.exit(main())
