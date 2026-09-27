"""Create context-aware OpenAI skill metadata and a self-contained SVG icon.

This optional client presentation layer is separate from the portable skill format.
The program does not execute package code or access the network.
"""

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import sys

from validate_skill import _frontmatter, validate_skill


FIELDS = {'display_name', 'short_description', 'default_prompt', 'brand_color',
          'icon_label', 'icon_motif', 'allow_implicit_invocation'}
PALETTE = ('#315F91', '#6954A1', '#176C68', '#9B4B62', '#92602B')


def title(name):
    return ' '.join(part.capitalize() for part in name.split('-'))


def render(skill, context):
    if not isinstance(context, dict) or set(context) - FIELDS:
        raise ValueError(f'{skill}: context must be an object with only {sorted(FIELDS)}')
    # A skill can mention its future presentation icon before generation.
    issues = [issue for issue in validate_skill(skill) if issue.severity == 'ERROR'
              and not (issue.rule == 'resource-missing' and issue.message.endswith('assets/icon.svg'))]
    if issues:
        raise ValueError(f'{skill}: invalid SKILL.md: {issues[0].message}')
    front = _frontmatter((skill / 'SKILL.md').read_text(encoding='utf-8'))
    name, description = front['name'], front['description']
    display = context.get('display_name', title(name))
    summary = ' '.join(description.split())
    if len(summary) > 64:
        summary = summary[:64].rsplit(' ', 1)[0] or summary[:64]
    if len(summary) < 25:
        summary = f'Use {name[:25]} for its documented workflow'
    short = context.get('short_description', summary)
    prompt = context.get('default_prompt', f'Use ${name} for this task: {summary.rstrip(".")}.')
    color = context.get('brand_color', PALETTE[int(hashlib.sha256(name.encode()).hexdigest(), 16) % len(PALETTE)])
    label = context.get('icon_label', ''.join(part[0].upper() for part in name.split('-'))[:3])
    motif = context.get('icon_motif', 'package')
    implicit = context.get('allow_implicit_invocation', True)
    if not isinstance(display, str) or not 1 <= len(display.strip()) <= 64 or re.search(r'[\x00-\x1f]', display):
        raise ValueError(f'{skill}: display_name must have 1–64 printable characters')
    if not isinstance(short, str) or not 25 <= len(short) <= 64 or re.search(r'[\x00-\x1f]', short):
        raise ValueError(f'{skill}: short_description must have 25–64 printable characters')
    if not isinstance(prompt, str) or f'${name}' not in prompt or re.search(r'[\x00-\x1f]', prompt):
        raise ValueError(f'{skill}: default_prompt must contain ${name} and no control characters')
    if not isinstance(color, str) or not re.fullmatch(r'#[0-9A-Fa-f]{6}', color):
        raise ValueError(f'{skill}: brand_color must be #RRGGBB')
    if not isinstance(label, str) or not re.fullmatch(r'[A-Z0-9]{1,3}', label):
        raise ValueError(f'{skill}: icon_label must be 1–3 uppercase letters or digits')
    if motif not in {'package', 'document', 'check', 'spark'}:
        raise ValueError(f'{skill}: icon_motif must be package, document, check, or spark')
    if not isinstance(implicit, bool):
        raise ValueError(f'{skill}: allow_implicit_invocation must be boolean')
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    metadata = ('interface:\n'
                f'  display_name: {quote(display)}\n'
                f'  short_description: {quote(short)}\n'
                '  icon_small: "./assets/icon.svg"\n'
                '  icon_large: "./assets/icon.svg"\n'
                f'  brand_color: {quote(color.upper())}\n'
                f'  default_prompt: {quote(prompt)}\n'
                'policy:\n'
                f'  allow_implicit_invocation: {str(implicit).lower()}\n')
    glyphs = {
        'package': '<path d="M39 37 64 24l25 13v34L64 84 39 71Z"/><path d="M39 37 64 51l25-14M64 51v33"/>',
        'document': '<path d="M44 23h28l15 15v45H44Z"/><path d="M72 23v15h15M53 51h25M53 61h25M53 71h17"/>',
        'check': '<circle cx="64" cy="53" r="29"/><path d="m49 53 10 10 21-23"/>',
        'spark': '<path d="m64 20 8 25 25 8-25 8-8 25-8-25-25-8 25-8Z"/>',
    }
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" '
           f'aria-label="{html.escape(display, quote=True)} icon">\n'
           f'  <rect x="4" y="4" width="120" height="120" rx="28" fill="{color.upper()}"/>\n'
           '  <g fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" '
           f'stroke-linejoin="round">{glyphs[motif]}</g>\n'
           '  <rect x="31" y="87" width="66" height="26" rx="13" fill="#FFFFFF" opacity="0.95"/>\n'
           f'  <text x="64" y="105" text-anchor="middle" font-family="sans-serif" font-size="15" '
           f'font-weight="700" fill="{color.upper()}">{label}</text>\n'
           '</svg>\n')
    return metadata, svg


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path, help='standalone skill or plugin root')
    parser.add_argument('--context', type=Path, help='JSON presentation context; plugin uses a skills mapping')
    parser.add_argument('--force', action='store_true', help='replace existing presentation files')
    args = parser.parse_args()
    try:
        base = args.path
        if not base.is_dir():
            raise ValueError(f'{base}: package directory does not exist')
        if base.is_symlink():
            raise ValueError(f'{base}: package root cannot be a symbolic link')
        context = json.loads(args.context.read_text(encoding='utf-8')) if args.context else {}
        if (base / 'SKILL.md').is_file() and not (base / 'plugin.json').exists():
            skills = [(base, context)]
        elif (base / 'plugin.json').is_file():
            if not isinstance(context, dict) or set(context) - {'skills'} or not isinstance(context.get('skills', {}), dict):
                raise ValueError('plugin context must contain only a skills object')
            children = base / 'skills'
            if children.is_symlink():
                raise ValueError(f'{children}: skill container cannot be a symbolic link')
            skills = [(p, context.get('skills', {}).get(p.name, {})) for p in sorted(children.iterdir()) if p.is_dir()] if children.is_dir() else []
            if not skills:
                raise ValueError(f'{base}: plugin has no immediate-child skills')
            extra = set(context.get('skills', {})) - {p.name for p, _ in skills}
            if extra:
                raise ValueError(f'{base}: unknown skill context: {sorted(extra)}')
        else:
            raise ValueError(f'{base}: expected SKILL.md or plugin.json')
        writes = []
        for skill, options in skills:
            yaml, svg = render(skill, options)
            for relative, content in [('agents/openai.yaml', yaml), ('assets/icon.svg', svg)]:
                destination = skill / relative
                if skill.is_symlink() or destination.parent.is_symlink() or destination.is_symlink():
                    raise ValueError(f'{destination}: symbolic link is not an owned output')
                if destination.exists() and not args.force:
                    raise ValueError(f'{destination}: already exists; use --force to replace owned presentation files')
                writes.append((destination, content))
        for destination, content in writes:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(content, encoding='utf-8')
            print(destination)
        return 0
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
