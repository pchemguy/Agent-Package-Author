---
name: agent-package-author
description: Design, create, revise, review, inspect, and validate standalone Agent Skills and Agent Plugins 1.0 packages. Use for portable skill authoring, content assessment, or multi-skill plugin packaging with optional MCP configuration.
---

# Agent Package Author

Select the **operation** first: create/revise, focused content review, comprehensive content review, or structural inspect/validate. Then identify standalone skill or plugin scope. A review-only request examines the requested material and returns findings, coverage, uncertainty, and a stopping boundary; it does not edit, install, or generate files. A focused review stays with the selected content and consequential interfaces. A comprehensive review inventories the requested package and accounts for assessed, excluded, and unassessed material. Structural inspection uses the matching CLI and reports only what it checks. During authorized creation or revision, apply proportionate content review and repair within the user's scope.

## Reference routing

Open only the references selected by the operation, package contents, and request. Each link below is a direct entry to its owner; the scope column names what it contributes and excludes.

| Reference | Load when | Purpose and boundary |
| --- | --- | --- |
| [Authoring workflow](references/authoring-workflow.md) | Creating or revising | Intake through authorized writes, repair and reporting; skip for review-only and structural-only work. |
| [Portability policy](references/portability-policy.md) | Classifying proposed files or portability claims | Portable core versus client extensions and development files; not a format validator. |
| [Validation policy](references/validation-policy.md) | Assessing evidence, running checks, or reporting | Structural, source and observed-behavior evidence; detailed content criteria live in review modules. |
| [Skill standard](references/skill-standard.md) | Authoring, reviewing format, or validating a skill | Published skill format and resource rules; not a prose-quality checklist. |
| [Skill design](references/skill-design.md) | Designing/revising a skill or assessing its design | Capability and resource boundaries; detailed entry/reference review is separate. |
| [Skill review](references/skill-review.md) | Comprehensive skill content review, or a relevant focused question; proportionately during authorized work | Entry and reference composition, routing and content coverage; no format-error classification or automatic edits. |
| [Hello World example](references/hello-world-example.md) | A deliberately broad exemplar would inform design | Optional example, never a required scaffold. |
| [Plugin standard](references/plugin-standard.md) | Authoring, reviewing format, or validating a plugin | Manifest and fixed discovery locations; not content quality. |
| [Plugin design](references/plugin-design.md) | Designing/revising a plugin or assessing composition | Capability split and ownership; detailed package review is separate. |
| [Plugin review](references/plugin-review.md) | Comprehensive plugin content review, or a relevant focused question; proportionately during authorized work | Composition and optional coordination; include skill review only for actual bundled skills. |
| [MCP packaging](references/mcp-packaging.md) | MCP is requested or exists in the package | MCP config and transport guidance; irrelevant for a skill-only package. |
| [OpenAI presentation](references/openai-presentation.md) | Generating/revising OpenAI presentation after skill content is accepted, or assessing existing presentation | Derive `agents/openai.yaml` and `assets/icon.svg`; client presentation is distinct from portable skill format. |

For a standalone skill, use skill-specific owners. For a plugin, use plugin owners and the skill owners for each included skill; an existing plugin with no skills gets no invented skill requirements. A custom `PLUGIN.md` or coordinator is assessed only when present; `PLUGIN.md` needs an explicit loading path and is not a portable plugin entry. A documented relative link to a sibling file may stay within the plugin root and yield a warning; name the sibling skill and link its `SKILL.md` for a workflow handoff. A sibling reference link loads shared guidance without selecting its skill.

For authorized creation/revision, check names in the target discovery scope before writing or installing; preserve unrelated files. Use the smallest useful package and observable acceptance cases. After portable skill content is accepted, derive and review distinct OpenAI presentation for each created skill. Use `assets/skill-entry-template.md` or `assets/plugin-manifest-template.json` only as useful starting material; use `assets/mcp-template.json` only for an MCP path. Validate with `python scripts/validate_skill.py PATH` or `python scripts/validate_plugin.py PATH`, then `python scripts/inspect_package.py PATH` when inventory helps. Run real workflow cases for behavioral claims. Structural success does not establish client loading, execution, or portability across every host. Report paths, actual checks, required facilities, extensions, and unrun behavior; do not claim installation or publishing without evidence.
