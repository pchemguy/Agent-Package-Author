"""Small standard-library MCP server for heading lookup in local notes.

This fixture demonstrates why the plugin adds MCP: a client can request a
heading index through a tool in addition to discovering the two skills.
The client supplies the note path; this script is not run by validators.
"""

import json
from pathlib import Path
import sys


def handle(request: dict) -> dict | None:
    """Answer initialize and heading-index tool requests over JSON-RPC."""
    method = request.get('method')
    if 'id' not in request:
        return None
    if method == 'initialize':
        result = {'protocolVersion': '2025-06-18', 'capabilities': {'tools': {}}, 'serverInfo': {'name': 'note-heading-index', 'version': '0.1.0'}}
    elif method == 'tools/list':
        result = {'tools': [{'name': 'headings', 'description': 'List Markdown headings in a local note', 'inputSchema': {'type': 'object', 'properties': {'path': {'type': 'string'}}, 'required': ['path']}}]}
    elif method == 'tools/call' and request.get('params', {}).get('name') == 'headings':
        try:
            path = Path(request['params']['arguments']['path'])
            headings = [line.lstrip('#').strip() for line in path.read_text(encoding='utf-8').splitlines() if line.startswith('#') and line.lstrip('#').startswith(' ')]
            result = {'content': [{'type': 'text', 'text': '\n'.join(headings)}]}
        except (KeyError, OSError) as error:
            result = {'content': [{'type': 'text', 'text': str(error)}], 'isError': True}
    else:
        return {'jsonrpc': '2.0', 'id': request['id'], 'error': {'code': -32601, 'message': 'Method not found'}}
    return {'jsonrpc': '2.0', 'id': request['id'], 'result': result}


def main() -> int:
    """Serve newline-delimited JSON-RPC messages on standard input/output."""
    for line in sys.stdin:
        try:
            reply = handle(json.loads(line))
            if reply is not None:
                print(json.dumps(reply, separators=(',', ':')), flush=True)
        except (ValueError, TypeError) as error:
            print(f'invalid request: {error}', file=sys.stderr)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
