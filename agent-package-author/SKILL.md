---
name: agent-package-author
description: Design, create, revise, inspect, and validate standalone Agent Skills and Agent Plugins 1.0 packages. Use for portable skill authoring or multi-skill plugin packaging with optional MCP configuration.
---

# Agent Package Author

Determine whether the request targets a standalone skill or an Agent Plugin. For either mode, read `references/authoring-workflow.md`, `references/portability-policy.md`, and `references/validation-policy.md`.

- **Standalone skill:** Read `references/skill-standard.md` and `references/skill-design.md`. Read `references/hello-world-example.md` only if a deliberately full-featured reference example helps the design. Start with `assets/skill-entry-template.md` if useful; do not create optional directories without a reason. Check with `python scripts/validate_skill.py PATH`.
- **Plugin:** Read `references/plugin-standard.md`, `references/plugin-design.md`, `references/skill-standard.md`, and `references/skill-design.md`. Apply each skill's metadata and workflow rules. A documented relative link to a sibling file may stay within the plugin root and yield a warning; use a named handoff and link to the sibling `SKILL.md` when appropriate. Read `references/mcp-packaging.md` only if MCP is requested or genuinely needed; use `assets/plugin-manifest-template.json` and, only then, `assets/mcp-template.json` if useful. Run `python scripts/validate_plugin.py PATH` on the plugin root.

Before writing or installing, check names in the target discovery scope for collisions; preserve unrelated files. Define observable acceptance cases, create the smallest useful package, test its real workflow, and run `python scripts/inspect_package.py PATH`. Structural validation alone does not prove client runtime support. Report exact paths, checks run, required facilities, extensions, and limitations. Do not claim installation, publishing, or universal client support without separate evidence.

After the portable skill content is accepted, read `references/openai-presentation.md` to derive and generate its OpenAI presentation files. In plugin mode, apply it to each child skill. Review generated metadata and icon against the accepted context.
