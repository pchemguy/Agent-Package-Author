# Optional MCP packaging

Load this reference only when the user needs MCP. `mcp.json` is optional and contains exactly `$schema` and `mcpServers`; its schema version must match `plugin.json`. Each server uses one closed variant: `stdio`, `streamable-http`, or legacy `sse`. Read the normative Agent Plugins transport rules before building a server entry.

For `stdio`, `command` is a bare executable token or contained package-relative `./` path; a bundled executable needs the latter. Keep `args` separate, and use allowed `cwd` forms (`./`, `${PLUGIN_ROOT}`, `${PLUGIN_DATA}` with optional children). Only `args`, `env` values and `cwd` expand the two placeholders. Never set reserved `PLUGIN_ROOT` or `PLUGIN_DATA` in `env`.

Remote URLs are absolute HTTP(S), without userinfo or fragment; non-loopback requires HTTPS. Header names are case-insensitively unique. Do not embed credentials in headers or `env`; client-managed authorization is separate. All resolved package paths remain within the plugin root; data paths remain within client-managed plugin data. Offline structural validation does not test transport availability, server startup, authorization, handshake, or trustworthiness.
