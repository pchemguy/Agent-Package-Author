# Critical review report

## Baseline and evidence boundary

- Campaign: `009_e591021-critical-review`; [plan](REVIEW-PLAN.md). Pinned reviewed source: `e591021a4ca3ed4dc48b40fc984604bde3f7227d` on `main`. Review branch commits change only this report and active navigation, not the pinned source.
- Reviewer: Codex, 2026-11-05. This report records source inspection, structural checks and local execution separately. No target-client activation or Windows CMD execution is claimed.
- State: U-001–U-002 assessed; U-003–U-005 pending. One finding allocated. A prior campaign's observations are not treated as evidence for this baseline.

## U-001 — Inventory and format baseline

- Source paths: the tracked baseline has 83 files and no tracked symlink. The delivered `agent-package-author/` contains 22 files: `SKILL.md`, twelve references, four Python helpers, four assets and `agents/openai.yaml`. Examples, tests and development records are outside the delivered directory. A source search over the delivered package, examples, tests and README found no hardcoded former workspace path, temporary path or `IMPLEMENTATION_LOG` dependency.
- Normative comparison: inspected current `references/skill-standard.md`, `plugin-standard.md`, `portability-policy.md` and `validation-policy.md` against the published [Agent Skills specification](https://agentskills.io/specification) and [Agent Plugins 1.0.0 specification](https://agent-plugins.org/specification) on 2026-11-05. Their sampled required metadata, optional skill resources, root manifest fields, fixed component discovery, missing-location treatment and plugin-root containment claims agree with the cited normative text. This is a source comparison, not a complete schema conformance proof.
- Resource check: a fenced-code-aware scan of the delivered Markdown found 33 operative local links; all targets exist and resolve inside `agent-package-author/`. `validate_skill.py agent-package-author` exited 0; `inspect_package.py agent-package-author` reported twelve references, four scripts, four assets, zero errors and zero warnings. A disposable skill with a contained linked reference exited 0; replacing its entry link with a missing target or a `../` escape exited 1 with `resource-missing` or `resource-escape`, respectively.
- Assessment: C-001 satisfied for the inspected baseline and cases. The current generator, nested resource links, plugin examples and actual client loading remain for later units. No finding in this unit.

## U-002 — Entry and reference composition

Read the creator `SKILL.md` and all twelve reference files in the pinned source. Assessed each at full-text source depth: `authoring-workflow` (intake and effects), `portability-policy` (classification), `validation-policy` (evidence), `skill-standard`/`skill-design`/`skill-review`/`hello-world-example` (skill format, capability boundaries, review and conditional exemplar), `plugin-standard`/`plugin-design`/`plugin-review` (plugin discovery, decomposition and optional coordinator), `mcp-packaging` (optional transport), and `openai-presentation` (per-skill presentation). This is instruction inspection, not an independent agent activation trial.

The entry directly names and links all twelve files and gives a load condition and boundary for each. Standalone creation, review-only, structural-only, a no-skill plugin, sibling handoff and optional MCP/presentation can be traced without assuming a plugin-wide `PLUGIN.md`. The detailed review modules are substantive; short format/classification modules serve shallow routing and owner summaries. No length-only split is warranted. The optional coordinator and `PLUGIN.md` criteria in `plugin-review` are conditional. The entry's review-only path explicitly stops without generation or writes.

### R-001 — Attachment authority is specified in the walkthrough but not the authoring procedure

- **Priority/type/confidence:** P2, instruction and cross-surface contract gap; medium-high source confidence, behavioral impact untested.
- **Located evidence:** `README.md` under “Complete authoring walkthrough” says an attachment can be a seed, reference or draft; the agent first records its role and authority and flags source conflicts during exploration. `references/authoring-workflow.md` steps 1–5 say to gather and reuse supplied requirements, then design/write, without classifying source roles, checking a draft against accepted requirements, or resolving conflicting sources. `references/openai-presentation.md` applies attachment role handling only to presentation context, after portable content exists. The entry does not route a general source-arbitration owner.
- **Consequence:** A normal authoring request with an older draft and newer brief can be executed by following the loaded procedure while silently treating both as requirements. The README's demonstrated exploration behavior is not guaranteed by the creator's operative instructions.
- **Bounded correction and recheck:** `authoring-workflow.md` should make source-role/authority and conflict resolution part of intake before accepting the package contract; link to a substantive owner only if that responsibility grows. Recheck with a conflicting seed, reference and draft, observing whether the agent identifies the difference before writing, while preserving a simple brief-only path.

Other U-002 routes were coherent on source inspection. Consumer selection of references, handoff activation, and whether a less capable model applies the distinctions remain untested.
