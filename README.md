# Agent Package Author

This repository implements [SPEC.md](SPEC.md) under the ordered [PLAN.md](PLAN.md). The runtime skill is the `agent-package-author/` directory. It guides the creation or revision of a standalone Agent Skill or an Agent Plugins 1.0.0 package with immediately discoverable skills and optional MCP servers. It can inspect and structurally validate both formats without downloading schemas, executing target scripts, or connecting to MCP endpoints.

## Use

Place the complete `agent-package-author/` directory in a skill discovery location supported by your agent. Installation paths, invocation syntax, Python support, and MCP transport support depend on the host. Installing or publishing the skill is outside this repository's implementation campaign. The skill's own routing starts in `SKILL.md`, with conditional references and optional templates under `references/` and `assets/`.

Run the offline helpers with Python 3.11 or newer:

```console
python agent-package-author/scripts/validate_skill.py examples/standalone/word-count
python agent-package-author/scripts/validate_plugin.py examples/multi-skill/notes-tools
python agent-package-author/scripts/validate_plugin.py examples/with-mcp/notes-tools
python agent-package-author/scripts/inspect_package.py examples/with-mcp/notes-tools
python -m unittest discover -s tests -v
```

CLIs exit `0` on strict structural success, `1` on detected package errors, and `2` for invalid invocation or absent paths. Diagnostics identify paths and rules. `--help` is available for each helper. A strict plugin check fails if any included skill or MCP server is invalid even when a conforming client could load other valid components.

## Boundaries

- The creator's runtime uses only Python's standard library and no network. Generated packages may have different declared runtime needs. The examples use Python 3.11+; the MCP example launches a local standard-library server through a bare `python` executable token and `${PLUGIN_ROOT}` path argument.
- The skill validator parses a documented subset of YAML frontmatter: plain and quoted string scalars and an indented string mapping for `metadata`. Other valid YAML syntax, including block scalars, is reported as **unverified** with a failing status. A green result therefore confirms its supported structural checks, not complete YAML-language conformance for every possible skill.
- The structural checks do not establish prose quality, reliable activation, security of included code, remote service behavior, host installation, or cross-client runtime compatibility. The example MCP server's initialize and tool-list responses are tested locally; full interoperability with particular clients and network services is outside the checks.
- Credentials are not part of the portable MCP package. A literal-looking secret in an environment or header value triggers a review warning, which is not a comprehensive secret scanner.
- Client-specific extensions require separate verified client documentation and are never presented as portable Agent Plugins components. The repository examples intentionally contain no such extension.

The source-only `examples/`, `tests/`, `SPEC.md`, `PLAN.md`, `ROADMAP.md`, and append-only `IMPLEMENTATION_LOG.jsonl` are not needed to run the delivered skill. The project history has one local task commit per implementation task, each with a `Task:` trailer; recovery manifests are transient and excluded from Git.
