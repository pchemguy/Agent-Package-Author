"""Validate an Agent Skill's portable structure without executing its contents.

The offline parser supports common scalar YAML and a string mapping for metadata.
It reports unhandled YAML syntax as unverified rather than declaring conformance.
"""

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
import re
import sys

NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*\Z')
OPTIONAL = {'license', 'compatibility', 'metadata', 'allowed-tools'}


@dataclass(frozen=True)
class Issue:
    """One deterministic, path-specific validation finding."""

    severity: str
    path: str
    rule: str
    message: str


def _scalar(value: str) -> str:
    """Parse a deliberately bounded string scalar without guessing YAML semantics."""
    value = value.strip()
    if value.startswith(('"', "'")):
        if value[-1:] != value[0]:
            raise ValueError('unterminated quoted scalar')
        parsed = ast.literal_eval(value)
        if not isinstance(parsed, str):
            raise ValueError('expected string')
        return parsed
    if not value or value[0] in '[{>|&*!' or value in {'null', '~', 'true', 'false'}:
        raise ValueError('unsupported YAML scalar syntax')
    return value


def _frontmatter(content: str) -> dict[str, object]:
    """Read supported frontmatter fields, rejecting ambiguous constructs."""
    lines = content.splitlines()
    if not lines or lines[0] != '---':
        raise ValueError('missing opening ---')
    try:
        end = lines.index('---', 1)
    except ValueError as error:
        raise ValueError('missing closing ---') from error
    data: dict[str, object] = {}
    current = None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line.startswith('  ') and current == 'metadata':
            match = re.fullmatch(r'  ([A-Za-z][\w-]*):\s*(.+)', line)
            if not match or match[1] in data['metadata']:
                raise ValueError('unsupported or duplicate metadata entry')
            data['metadata'][match[1]] = _scalar(match[2])
            continue
        match = re.fullmatch(r'([A-Za-z][\w-]*):\s*(.*)', line)
        if not match:
            raise ValueError('unsupported YAML frontmatter syntax')
        if match[1] in data:
            raise ValueError('duplicate frontmatter key')
        key, value = match.groups()
        if key == 'metadata' and not value:
            data[key] = {}
            current = key
        else:
            data[key] = _scalar(value)
            current = None
    if not '\n'.join(lines[end+1:]).strip():
        raise ValueError('missing Markdown body')
    return data


def validate_skill(path: Path) -> list[Issue]:
    """Return structural findings for a skill directory.

    Args:
        path: Skill root. No included scripts are executed.

    Returns:
        Ordered issues; an empty list means the supported checks passed.
    """
    path = Path(path)
    issues: list[Issue] = []
    entry = path / 'SKILL.md'
    if not path.is_dir() or not entry.is_file():
        return [Issue('ERROR', str(entry), 'entry', 'skill directory and regular SKILL.md required')]
    try:
        content = entry.read_text(encoding='utf-8')
        metadata = _frontmatter(content)
    except (OSError, UnicodeError) as error:
        return [Issue('ERROR', str(entry), 'read', str(error))]
    except (ValueError, SyntaxError) as error:
        rule = 'frontmatter-unverified' if 'unsupported' in str(error) else 'frontmatter'
        return [Issue('ERROR', str(entry), rule, str(error))]
    name = metadata.get('name')
    if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name):
        issues.append(Issue('ERROR', str(entry), 'name', 'name must be 1–64 lowercase letters, digits or single hyphens'))
    elif name != path.name:
        issues.append(Issue('ERROR', str(entry), 'name-directory', f'name {name!r} differs from {path.name!r}'))
    description = metadata.get('description')
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        issues.append(Issue('ERROR', str(entry), 'description', 'description must be 1–1024 nonblank characters'))
    compatibility = metadata.get('compatibility')
    if compatibility is not None and (not isinstance(compatibility, str) or not 1 <= len(compatibility) <= 500):
        issues.append(Issue('ERROR', str(entry), 'compatibility', 'compatibility must be 1–500 characters'))
    if 'metadata' in metadata and not isinstance(metadata['metadata'], dict):
        issues.append(Issue('ERROR', str(entry), 'metadata', 'metadata must be a string mapping'))
    for key in sorted(metadata.keys() - ({'name', 'description'} | OPTIONAL)):
        issues.append(Issue('ERROR', str(entry), 'field', f'unknown frontmatter field {key!r}'))
    if 'allowed-tools' in metadata:
        issues.append(Issue('WARN', str(entry), 'experimental', 'allowed-tools is experimental; client support varies'))
    return issues


def print_issues(issues: list[Issue]) -> None:
    """Print findings in stable input order with actionable rule labels."""
    for item in issues:
        print(f'{item.severity}: {item.path}: {item.rule}: {item.message}')


def main() -> int:
    """Run the standalone structural validator CLI."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path, help='skill directory')
    args = parser.parse_args()
    if not args.path.exists():
        parser.error(f'path does not exist: {args.path}')
    issues = validate_skill(args.path)
    print_issues(issues)
    return 1 if any(i.severity == 'ERROR' for i in issues) else 0


if __name__ == '__main__':
    sys.exit(main())
