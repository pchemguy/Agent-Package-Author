"""Validate Agent Plugins 1.0.0 package structure offline."""

import argparse
import ipaddress
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

from validate_skill import Issue, print_issues, validate_skill

PLUGIN_SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
MCP_SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/mcp.schema.json'
MANIFEST_KEYS = {'$schema', 'name', 'version', 'description', 'author', 'homepage', 'repository', 'license', 'keywords', 'extensions'}
PLUGIN_NAME = re.compile(r'[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?\Z')
NAMESPACE = re.compile(r'[a-z0-9]+(?:\.[a-z0-9-]+){2,}\Z')
HEADER = re.compile(r"[!#$%&'*+.^_`|~0-9A-Za-z-]+\Z")


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


def _mcp(root: Path) -> list[Issue]:
    """Check the fixed root MCP configuration and each server independently."""
    path = root / 'mcp.json'
    if not path.exists() and not path.is_symlink():
        return []
    if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
        return [Issue('ERROR', str(path), 'mcp-path', 'mcp.json must be a contained regular file')]
    try:
        data = _json(path)
    except (ValueError, OSError, UnicodeError) as error:
        return [Issue('ERROR', str(path), 'mcp-json', str(error))]
    if not isinstance(data, dict) or set(data) != {'$schema','mcpServers'} or not isinstance(data.get('mcpServers'), dict):
        return [Issue('ERROR', str(path), 'mcp-root', 'root must contain only $schema and mcpServers object')]
    if data['$schema'] != MCP_SCHEMA:
        return [Issue('ERROR', str(path), 'mcp-schema', f'$schema must match plugin version: {MCP_SCHEMA}')]
    issues = []
    for name, config in sorted(data['mcpServers'].items()):
        label = f'{path}#mcpServers/{name}'
        def error(rule, message):
            issues.append(Issue('ERROR', label, rule, message))
        if not isinstance(config, dict):
            error('mcp-server', 'server configuration must be an object')
            continue
        kind = config.get('type')
        if kind == 'stdio':
            allowed = {'type','command','args','env','cwd'}
            command = config.get('command')
            if not isinstance(command, str) or not command or command.startswith(('/', '../')) or (not command.startswith('./') and (any(c.isspace() for c in command) or '/' in command or '\\' in command)):
                error('mcp-command', 'command must be a bare executable token or contained ./ path')
            elif command.startswith('./') and not (root / command).resolve().is_relative_to(root.resolve()):
                error('mcp-path', 'command escapes plugin root')
            if 'args' in config and (not isinstance(config['args'], list) or any(not isinstance(s, str) for s in config['args'])):
                error('mcp-args', 'args must be a string array')
            env = config.get('env', {})
            if not isinstance(env, dict) or any(not isinstance(v, str) for v in env.values()) or {'PLUGIN_ROOT','PLUGIN_DATA'} & set(env):
                error('mcp-env', 'env must be a string mapping without reserved PLUGIN_ROOT/PLUGIN_DATA keys')
            elif any(re.search(r'(?:TOKEN|SECRET|PASSWORD|API_KEY)', k, re.I) and v and '${' not in v for k,v in env.items()):
                issues.append(Issue('WARN', label, 'mcp-secret-review', 'possible literal credential in env; review manually'))
            cwd = config.get('cwd')
            if cwd is not None:
                if not isinstance(cwd, str) or not (cwd.startswith('./') or cwd == '${PLUGIN_ROOT}' or cwd.startswith('${PLUGIN_ROOT}/') or cwd == '${PLUGIN_DATA}' or cwd.startswith('${PLUGIN_DATA}/')):
                    error('mcp-cwd', 'cwd must be ./, PLUGIN_ROOT, or PLUGIN_DATA rooted')
                else:
                    prefix = '${PLUGIN_DATA}'
                    if cwd.startswith(prefix):
                        base, suffix = root / '.plugin-data-placeholder', cwd[len(prefix):]
                    elif cwd.startswith('${PLUGIN_ROOT}'):
                        base, suffix = root, cwd[len('${PLUGIN_ROOT}'):]
                    else:
                        base, suffix = root, cwd[1:]
                    if not (base / suffix.lstrip('/')).resolve().is_relative_to(base.resolve()):
                        error('mcp-path', 'cwd escapes its declared root')
        elif kind in {'streamable-http','sse'}:
            allowed = {'type','url','headers'}
            url = config.get('url')
            try:
                parsed = urlsplit(url) if isinstance(url, str) else None
                host = parsed.hostname if parsed else None
                if parsed:
                    _ = parsed.port  # Force validation of malformed port text.
                loopback = host == 'localhost'
                if host and not loopback:
                    try:
                        loopback = ipaddress.ip_address(host).is_loopback
                    except ValueError:
                        pass
                if not parsed or any(c.isspace() for c in url) or parsed.scheme not in {'http','https'} or not host or parsed.username or parsed.password or parsed.fragment or (parsed.scheme == 'http' and not loopback):
                    error('mcp-url', 'absolute HTTPS URL required except HTTP loopback; no userinfo or fragment')
            except ValueError:
                error('mcp-url', 'invalid URL')
            headers = config.get('headers', {})
            if not isinstance(headers, dict) or any(not isinstance(v, str) or not HEADER.fullmatch(k) or '\r' in v or '\n' in v for k,v in headers.items()) or len({k.lower() for k in headers}) != len(headers):
                error('mcp-headers', 'headers must be valid strings with case-insensitively unique names')
            elif any(k.lower() in {'authorization','proxy-authorization','x-api-key'} and v for k,v in headers.items()):
                issues.append(Issue('WARN', label, 'mcp-secret-review', 'possible literal credential in headers; review manually'))
        else:
            allowed = {'type'}
            error('mcp-type', 'type must be stdio, streamable-http, or sse')
        for key in sorted(config.keys() - allowed):
            error('mcp-server-fields', f'unknown or cross-variant field {key!r}')
    return issues


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
    if manifest is None:
        return issues
    skills = root / 'skills'
    if skills.exists() or skills.is_symlink():
        if not skills.resolve().is_relative_to(root.resolve()) or not skills.is_dir():
            issues.append(Issue('ERROR', str(skills), 'skills-kind', 'skills must resolve to a contained directory'))
        else:
            for child in sorted(skills.iterdir(), key=lambda p: p.name):
                if not child.is_dir():
                    continue
                if not child.resolve().is_relative_to(root.resolve()):
                    issues.append(Issue('ERROR', str(child), 'skill-containment', 'discovered child escapes plugin root'))
                    continue
                entry = child / 'SKILL.md'
                if not entry.exists() and not entry.is_symlink():
                    continue
                if not entry.resolve().is_relative_to(root.resolve()):
                    issues.append(Issue('ERROR', str(entry), 'skill-containment', 'SKILL.md escapes plugin root'))
                else:
                    issues.extend(validate_skill(child))
    for child in sorted(root.iterdir(), key=lambda p: p.name):
        if child.is_dir() and child.name.startswith(('com.', 'org.', 'net.')) and not NAMESPACE.fullmatch(child.name):
            issues.append(Issue('ERROR', str(child), 'extension-directory', 'extension root must use a reverse-domain namespace'))
    issues.extend(_mcp(root))
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
