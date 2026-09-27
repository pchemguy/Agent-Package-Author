# Portability classification

Classify each component before creation:

| Class | Meaning | Examples |
|---|---|---|
| Portable core | Required standard structure | `SKILL.md`, root `plugin.json` |
| Standard optional | Supported only when useful | `references/`, `scripts/`, `assets/`, root `mcp.json` |
| Client extension | Explicitly requested host behavior | `extensions` namespace or matching top-level directory |
| Development material | Source-only tests and examples | `tests/`, `examples/`, repository README |
| Unsupported/nonportable | No standard representation | Implicit hooks, commands, custom agents, undeclared host API |

Portable format does not guarantee the client supports the component, interpreter, transport, or installation location. Verify host-specific requirements from the target client's own documentation. Do not silently insert vendor metadata or describe a client extension as portable behavior.

The creator intentionally adds `agents/openai.yaml` and `assets/icon.svg` inside each generated skill for OpenAI client presentation. Read `openai-presentation.md` for derivation and generation. Classify the metadata as client-specific presentation, not an Agent Plugins v1 component or a required Agent Skills field; the SVG is a local asset. Keep portable `SKILL.md` metadata unchanged.
