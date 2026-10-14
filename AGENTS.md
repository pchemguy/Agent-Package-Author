# Agent development entry point

This repository develops `agent-package-author`, a portable skill for authoring and reviewing standalone Agent Skills and Agent Plugins 1.0 packages. Work from the repository root. Use [README.md](README.md) for the user-facing workflow and runnable examples.

## Start here

1. Inspect Git status and the requested scope before editing. Preserve unrelated changes.
2. Read [docs/dev/SPEC.md](docs/dev/SPEC.md) for requirements, [docs/dev/PLAN.md](docs/dev/PLAN.md) for implementation decisions and checks, and [docs/dev/ROADMAP.md](docs/dev/ROADMAP.md) for the completed original task sequence. These documents describe this project; a generated package can have its own development documents.
3. Read [agent-package-author/SKILL.md](agent-package-author/SKILL.md) for operation-first routing. Load only the relevant files under `agent-package-author/references/` for the part of the workflow you are changing. [Skill review](agent-package-author/references/skill-review.md) owns entry/reference content criteria; [plugin review](agent-package-author/references/plugin-review.md) owns package composition. [Validation policy](agent-package-author/references/validation-policy.md) owns evidence boundaries.

## Repository map

| Path | Purpose |
| --- | --- |
| `agent-package-author/` | Delivered skill: entry point, authoring references, templates, presentation assets, and offline Python helpers. |
| `examples/` | Standalone skill, multi-skill plugin, and plugin with MCP acceptance packages. |
| `tests/` | Standard-library `unittest` coverage and format fixtures. |
| `docs/dev/` | Project requirements, plan, roadmap, and closed review records. |

Keep development files outside the delivered `agent-package-author/` directory. Do not treat the example packages or the creator's own OpenAI presentation files as mandatory portable package components.

## Changes and verification

- Follow the published Agent Skills and Agent Plugins 1.0 specifications for package-format claims. Keep standalone skill checks distinct from plugin-root checks: an existing sibling-relative link inside a plugin may warn, while missing targets and plugin-root escapes fail.
- Update affected requirements, references, examples, tests, and README instructions when behavior changes. Keep links relative to their containing Markdown file.
- Run `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` for repository changes. For package behavior, also run the relevant helpers from the repository root:

  ```console
  python agent-package-author/scripts/validate_skill.py PATH
  python agent-package-author/scripts/validate_plugin.py PATH
  python agent-package-author/scripts/inspect_package.py PATH
  ```

Report what changed and which checks actually ran. Do not claim client installation or runtime compatibility from structural validation alone.
