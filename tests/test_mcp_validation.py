"""Verify Agent Plugins MCP variant, version, and path contracts."""

import json
from pathlib import Path
import tempfile
import unittest

from test_plugin_validation import load


class McpValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'demo-plugin'
        self.root.mkdir()
        (self.root / 'plugin.json').write_text(json.dumps({'$schema':load().PLUGIN_SCHEMA,'name':'demo-plugin'}))

    def mcp(self, servers, schema=None):
        (self.root / 'mcp.json').write_text(json.dumps({'$schema':schema or load().MCP_SCHEMA,'mcpServers':servers}))

    def test_valid_empty_and_bare_stdio_server(self):
        self.mcp({})
        self.assertEqual(load().validate_plugin(self.root), [])
        self.mcp({'local':{'type':'stdio','command':'python','args':['--version'],'cwd':'${PLUGIN_DATA}/local'}})
        self.assertEqual(load().validate_plugin(self.root), [])

    def test_invalid_schema_variant_and_escape(self):
        self.mcp({}, schema='https://agent-plugins.org/schemas/2.0.0/mcp.schema.json')
        self.assertTrue(any(i.rule == 'mcp-schema' for i in load().validate_plugin(self.root)))
        self.mcp({'bad':{'type':'stdio','command':'./../outside','url':'https://example.com'}})
        rules = {i.rule for i in load().validate_plugin(self.root)}
        self.assertIn('mcp-server-fields', rules)
        self.assertIn('mcp-path', rules)

    def test_remote_url_and_case_insensitive_headers(self):
        self.mcp({'remote':{'type':'streamable-http','url':'http://example.com/mcp'}})
        self.assertTrue(any(i.rule == 'mcp-url' for i in load().validate_plugin(self.root)))
        self.mcp({'remote':{'type':'streamable-http','url':'https://example.com/mcp','headers':{'X-Test':'a','x-test':'b'}}})
        self.assertTrue(any(i.rule == 'mcp-headers' for i in load().validate_plugin(self.root)))

    def test_reserved_environment_and_malformed_root(self):
        self.mcp({'local':{'type':'stdio','command':'python','env':{'PLUGIN_ROOT':'bad'}}})
        self.assertTrue(any(i.rule == 'mcp-env' for i in load().validate_plugin(self.root)))
        (self.root / 'mcp.json').write_text('{')
        self.assertTrue(any(i.rule == 'mcp-json' for i in load().validate_plugin(self.root)))

    def test_nonstring_header_key_and_cwd_traversal_diagnosed(self):
        self.mcp({'remote': {'type': 'streamable-http', 'url': 'https://example.com/mcp', 'headers': {'X-Test': 'ok', 'bad': 3}}})
        self.assertTrue(any(i.rule == 'mcp-headers' for i in load().validate_plugin(self.root)))
        self.mcp({'local': {'type': 'stdio', 'command': 'python', 'cwd': '${PLUGIN_DATA}/../escape'}})
        self.assertTrue(any(i.rule == 'mcp-path' for i in load().validate_plugin(self.root)))

    def test_invalid_port_is_not_accepted_as_remote_url(self):
        self.mcp({'remote': {'type': 'streamable-http', 'url': 'https://example.com:bad/mcp'}})
        self.assertTrue(any(i.rule == 'mcp-url' for i in load().validate_plugin(self.root)))

    def test_bundled_command_must_resolve_to_file(self):
        self.mcp({'local': {'type': 'stdio', 'command': './bin/server'}})
        self.assertTrue(any(i.rule == 'mcp-path' for i in load().validate_plugin(self.root)))


if __name__ == '__main__':
    unittest.main()
