"""Small standard-library MCP server for heading lookup in local notes.

This fixture demonstrates why the plugin adds MCP: a client can request a
heading index through a tool in addition to discovering the two skills.
The client supplies the note path; this script is not run by validators.
"""

import json
from pathlib import Path
import sys


def _error(identifier: object, code: int, message: str) -> dict:
    return {'jsonrpc': '2.0', 'id': identifier, 'error': {'code': code, 'message': message}}


def handle(request: object) -> dict | None:
    """Answer initialize and heading-index tool requests over JSON-RPC."""
    if not isinstance(request, dict):
        return _error(None, -32600, 'Invalid Request')
    if 'id' not in request:
        return None
    identifier = request['id']
    if request.get('jsonrpc') != '2.0' or not isinstance(request.get('method'), str):
        return _error(identifier, -32600, 'Invalid Request')
    method = request['method']
    params = request.get('params', {})
    if not isinstance(params, dict):
        return _error(identifier, -32602, 'Invalid params')
    if method == 'initialize':
        result = {'protocolVersion': '2025-06-18', 'capabilities': {'tools': {}}, 'serverInfo': {'name': 'note-heading-index', 'version': '0.1.0'}}
    elif method == 'tools/list':
        result = {'tools': [{'name': 'headings', 'description': 'List Markdown headings in a local note', 'inputSchema': {'type': 'object', 'properties': {'path': {'type': 'string'}}, 'required': ['path']}}]}
    elif method == 'tools/call' and params.get('name') == 'headings':
        try:
            arguments = params.get('arguments')
            if not isinstance(arguments, dict) or not isinstance(arguments.get('path'), str):
                return _error(identifier, -32602, 'path must be a string')
            path = Path(arguments['path'])
            headings = [line.lstrip('#').strip() for line in path.read_text(encoding='utf-8').splitlines() if line.startswith('#') and line.lstrip('#').startswith(' ')]
            result = {'content': [{'type': 'text', 'text': '\n'.join(headings)}]}
        except OSError as error:
            result = {'content': [{'type': 'text', 'text': str(error)}], 'isError': True}
    else:
        return _error(identifier, -32601, 'Method not found')
    return {'jsonrpc': '2.0', 'id': identifier, 'result': result}


def main() -> int:
    """Serve newline-delimited JSON-RPC messages on standard input/output."""
    for line in sys.stdin:
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            reply = _error(None, -32700, 'Parse error')
        else:
            reply = handle(request)
        if reply is not None:
            print(json.dumps(reply, separators=(',', ':')), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
