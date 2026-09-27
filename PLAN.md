# Agent Package Author Implementation Plan

> **For implementation:** Execute tasks in order and mark each checkbox when its verification passes. Keep `SPEC.md` beside this plan; both govern the work.

**Goal:** Deliver `agent-package-author`, a portable skill that authors, inspects, and validates standalone Agent Skills and Agent Plugins 1.0.0 packages.

**Architecture:** `SKILL.md` routes between skill and plugin authoring. Focused references explain standards and design decisions; templates are optional starting material. Three offline Python CLIs share validation functions, with `validate_plugin.py` importing skill checks and `inspect_package.py` importing both validators without executing inspected code.

**Technology:** Markdown, JSON, Python standard library, `unittest` for development tests. Python 3.11 or newer for the creator's helpers; generated packages declare their own actual runtime requirements.

**Specification:** [SPEC.md](SPEC.md). Normative formats: [Agent Skills](https://agentskills.io/specification) and [Agent Plugins 1.0.0](https://agent-plugins.org/specification). At implementation start, compare rules with these published texts and record any material drift before changing validators.

## Global constraints and interfaces

- Creator directory and frontmatter name: `agent-package-author`. Its own frontmatter contains only `name` and `description`.
- Plugin schema identifiers are exactly `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` and `https://agent-plugins.org/schemas/1.0.0/mcp.schema.json`. Do not silently accept another version.
- Runtime helpers are offline and standard-library-only; no target package code is executed by inspection or structural validation.
- A validator's exit `0` means strict creator validation passed; exit `1` means package errors; exit `2` means invalid invocation or unreadable input. Warnings do not fail. Diagnostics use `ERROR|WARN: path: rule: explanation` and are stably ordered.
- Public CLIs: `python agent-package-author/scripts/validate_skill.py PATH`, `validate_plugin.py PATH`, `inspect_package.py PATH`, each with `--help`. `inspect_package.py` exits `1` on invalid recognized packages and `2` on unknown/unreadable paths; it still inventories valid components of a partially invalid package.
- Shared Python interfaces in `scripts/validate_skill.py`: `Issue(severity: str, path: str, rule: str, message: str)`, `validate_skill(path: Path) -> list[Issue]`, `print_issues(issues: list[Issue]) -> None`. `validate_plugin.py` exports `validate_plugin(path: Path) -> list[Issue]` and imports `Issue` and `validate_skill`. `inspect_package.py` imports both validation functions. No separate runtime package or third-party parser.
- The skill validator checks the portable default and documented optional standard metadata. Because Python's standard library has no general YAML parser, its frontmatter reader SHALL support the documented scalar and mapping subset used in the examples and templates, and report unsupported YAML syntax as **unverified** with exit `1`, never as a claim of full YAML conformance. Include a follow-up note in the README about this deliberate coverage limit. If full YAML syntax is required to meet the SPEC's validator scope, revise this design before implementation rather than silently rejecting otherwise valid skills.
- Keep tests, examples, `README.md`, `SPEC.md`, and `PLAN.md` at repository root, outside the delivered `agent-package-author/` runtime directory. Do not install or publish the creator as part of this plan.

## File map

| Path | Responsibility |
|---|---|
| `agent-package-author/SKILL.md` | Activation, mode routing, exact resource paths, workflow gates, completion reporting |
| `references/authoring-workflow.md`, `portability-policy.md`, `validation-policy.md` | Shared process, component classification, evidence and limits |
| `references/skill-standard.md`, `skill-design.md`, `hello-world-example.md` | Skill format, design choices, bounded exemplar |
| `references/plugin-standard.md`, `plugin-design.md`, `mcp-packaging.md` | Plugin format, capability split, optional MCP details |
| `assets/skill-entry-template.md`, `plugin-manifest-template.json`, `mcp-template.json` | Minimal, editable starting material |
| `scripts/validate_skill.py` | Frontmatter, naming, relative resource and containment checks; shared issues and CLI output |
| `scripts/validate_plugin.py` | Manifest, discovery, bundled skills, MCP, extensions, path checks |
| `scripts/inspect_package.py` | Read-only inventory and bounded validation summary |
| `tests/test_skill_validation.py`, `test_plugin_validation.py`, `test_mcp_validation.py`, `test_inspection.py`, `test_authoring.py` | Structural, negative, CLI, and end-to-end behavior |
| `examples/standalone/`, `examples/multi-skill/`, `examples/with-mcp/` | Realistic acceptance packages; only `with-mcp` contains `mcp.json` |
| `README.md` | Source usage, format scope, independent installation, verification instructions |

## Review focus

1. Quoted or multiline YAML descriptions: parse supported forms correctly or report syntax as unverified without falsely declaring a valid skill conforming.
2. Symlink or `..` escape in a referenced resource, bundled skill, or MCP path: reject the resolved escape and identify the component.
3. Absent `skills/` or `mcp.json`: accept the absence; an invalid *present* component fails strict creator validation.
4. Unknown manifest field versus fatal field/type violation: both fail strict authoring checks, but diagnostics explain that client loading treats an unknown field differently.
5. Empty `mcpServers`, invalid one-server variant, or mismatched schema: reflect format rules and explain client partial loading while failing strict creator validation.

## Task 01: Pin rules and establish a test harness

**Files:** `tests/fixtures/format-cases.json`, `tests/test_standards_baseline.py`, `README.md` (brief development command section).

- [ ] Extract the exact version identifiers, name patterns, allowed manifest keys, optional standard skill frontmatter fields, MCP variants, and failure boundaries from the published standards into `format-cases.json`; include source URLs and the reviewed date. Keep this fixture declarative rather than duplicating the specification in prose.
- [ ] Add `test_standards_baseline.py` asserting the fixture contains the exact `1.0.0` identifiers, the different skill/plugin naming alphabets, and immediate-child discovery examples; the test must fail if the fixture is absent or incomplete.
- [ ] Run `python -m unittest discover -s tests -v` (initially only the baseline test). **Complete when:** the pinned fixture and its test pass and any mismatch with `SPEC.md` is recorded for resolution.

## Task 02: Shared authoring contract and mode routing

**Files:** `agent-package-author/SKILL.md`, `references/authoring-workflow.md`, `portability-policy.md`, `validation-policy.md`, `tests/test_authoring.py`.

- [ ] Write a failing test that checks the creator's exact frontmatter fields, both mode keywords in `description`, directly named references, and explicit conditional routing for MCP and the Hello World exemplar.
- [ ] Author the entry point and shared references: requirements intake, collision check before any install/write, classification of every proposed component, observable acceptance model, revision without overwriting unrelated files, verification evidence, and qualified completion claims.
- [ ] Run `python -m unittest discover -s tests -p 'test_authoring.py' -v`. **Complete when:** skill and plugin requests route to the intended references and the creator itself has no host instruction files.

## Task 03: Standalone skill authoring resources

**Files:** `references/skill-standard.md`, `skill-design.md`, `hello-world-example.md`, `assets/skill-entry-template.md`, `tests/test_authoring.py`.

- [ ] Add assertions that the skill references distinguish mandatory `SKILL.md` from optional resources, describe activation and relative paths, treat the exemplar as nonmandatory, and reject template-driven file proliferation.
- [ ] Write the three references and a minimal `name`/`description` frontmatter template. Describe when to add scripts, assets, independent output validation, and positive/branch/negative cases; distinguish format rules from authoring advice.
- [ ] Run `python -m unittest discover -s tests -p 'test_authoring.py' -v`. **Complete when:** an implementer can design a `SKILL.md`-only skill or a more complex one without copying the Hello World tree.

## Task 04: Plugin and MCP authoring resources

**Files:** `references/plugin-standard.md`, `plugin-design.md`, `mcp-packaging.md`, `assets/plugin-manifest-template.json`, `mcp-template.json`, `tests/test_authoring.py`.

- [ ] Add tests checking canonical schema identifiers in templates, no inline MCP/component paths in `plugin.json`, no mandatory `mcp.json`, immediate-child skill discovery, and explicit extension isolation.
- [ ] Document plugin-versus-skill identity, when capabilities warrant distinct skills, component ownership, strict creator checks versus client partial loading, transport variants, safe paths, placeholders, credential handling, and runtime limits. Provide minimal valid JSON templates without secrets.
- [ ] Run `python -m unittest discover -s tests -p 'test_authoring.py' -v` and `python -m json.tool agent-package-author/assets/plugin-manifest-template.json` and the equivalent `mcp-template.json`. **Complete when:** both templates parse and the references make the optional MCP branch and client extensions unambiguous.

## Task 05: Skill validator, metadata and naming

**Files:** `scripts/validate_skill.py`, `tests/test_skill_validation.py`.

- [ ] Write failing cases for missing `SKILL.md`, absent/duplicate/invalid required metadata, invalid name, name/directory mismatch, valid description of 1–1024 characters, optional `compatibility` length, supported optional `metadata` mapping, and unsupported YAML constructs reported as unverified. Test a quoted description containing a colon.
- [ ] Implement `Issue`, frontmatter reading, `validate_skill(Path)`, stable `print_issues`, and the CLI/`--help` with the global exit rules. Validate standard optional fields without treating standard optional fields as vendor violations; warn or report unverified syntax precisely.
- [ ] Run `python -m unittest discover -s tests -p 'test_skill_validation.py' -v` and `python agent-package-author/scripts/validate_skill.py --help`. **Complete when:** valid minimal and documented optional examples pass, bad metadata fails, and an unsupported YAML form cannot receive a false clean pass.

## Task 06: Skill resource and path validation

**Files:** `scripts/validate_skill.py`, `tests/test_skill_validation.py`.

- [ ] Add tests for a valid directly linked reference, missing link, absolute path, `../` escape, symlink escape, optional directories absent, and a link into another bundled skill's private directory. Scope checks to explicit local resource links/paths; do not guess arbitrary prose is a file path.
- [ ] Resolve resource targets against the skill root; reject missing or escaped explicit resources and retain stable path-specific diagnostics. Apply plugin-root containment additionally when Task 08 validates bundled skills.
- [ ] Run `python -m unittest discover -s tests -p 'test_skill_validation.py' -v`. **Complete when:** all stated resource cases are handled without executing a script or opening unrelated files.

## Task 07: Plugin manifest validator

**Files:** `scripts/validate_plugin.py`, `tests/test_plugin_validation.py`.

- [ ] Test the minimal valid manifest, each required field, name punctuation and bounds, each optional field's type, closed `author`, unknown root key, malformed JSON, schema mismatch, root `plugin.json` escape, and non-object `extensions`.
- [ ] Implement `validate_plugin(Path) -> list[Issue]`, strict root manifest checks, canonical schema and name constraints, and the CLI/`--help`. The unknown-key and non-object-extensions diagnostics must state their distinct nonfatal client behavior even though the strict creator run fails.
- [ ] Run `python -m unittest discover -s tests -p 'test_plugin_validation.py' -v` and `python agent-package-author/scripts/validate_plugin.py --help`. **Complete when:** manifest validation agrees with the pinned v1 rules and clearly labels client failure boundaries.

## Task 08: Skill discovery and extensions inside plugins

**Files:** `scripts/validate_plugin.py`, `tests/test_plugin_validation.py`.

- [ ] Test two valid immediate-child skills; a nested `SKILL.md` not separately discovered; missing component locations; present wrong-kind `skills`; one invalid child; symlinks that escape plugin root; manifest and/or top-level extension namespace with valid and invalid forms.
- [ ] Enumerate only immediate skill child directories with regular `SKILL.md`, call `validate_skill` on each, and enforce both its skill-root and the plugin-root containment. Validate extension namespace placement and object values without pretending to validate client-owned extension semantics.
- [ ] Run `python -m unittest discover -s tests -p 'test_plugin_validation.py' -v`. **Complete when:** a plugin lacking MCP passes, each discovered child has an independent result, and strict failure of one component does not prevent reporting the others.

## Task 09: MCP configuration validator

**Files:** `scripts/validate_plugin.py`, `tests/test_mcp_validation.py`.

- [ ] Add transport-table tests: `stdio` bare versus `./` command, token separation, `args`/`env` types, reserved env keys, `cwd` forms and containment, `streamable-http`/`sse` URL restrictions, header validity/case duplication, unknown/cross-variant keys, empty `mcpServers`, malformed root, and schema mismatch. Include symlink and traversal escapes. Test detectable literal credentials in `env`/`headers` as warnings requiring review, not a promise to find every secret.
- [ ] Implement local JSON and transport checks without fetching schemas, starting subprocesses, expanding placeholders in disallowed fields, or making network calls. Apply per-server diagnostics while preserving manifest/skill findings.
- [ ] Run `python -m unittest discover -s tests -p 'test_mcp_validation.py' -v`. **Complete when:** valid stdio and remote examples pass, every invalid server yields a named diagnostic, and a bad `mcp.json` fails strict creator validation without suppressing skill findings.

## Task 10: Read-only package inspector

**Files:** `scripts/inspect_package.py`, `tests/test_inspection.py`.

- [ ] Test standalone skill, plugin with two skills/no MCP, plugin with MCP, invalid but readable plugin, unknown directory, and executable files with side effects that must remain untouched.
- [ ] Implement type detection from root `plugin.json` or `SKILL.md`, deterministic inventory of immediate skills, optional resources, MCP server names/transports, extension namespaces, and warning/error totals. Import validation functions for bounded summaries; never label inventory alone as proof of runtime portability.
- [ ] Run `python -m unittest discover -s tests -p 'test_inspection.py' -v` and `python agent-package-author/scripts/inspect_package.py --help`. **Complete when:** output and exit codes match the global CLI contract and target code is never run.

## Task 11: Realistic authoring acceptance packages

**Files:** `examples/standalone/**`, `examples/multi-skill/**`, `examples/with-mcp/**`, `tests/test_authoring.py`.

- [ ] Create one small coherent standalone skill with an exercisable no-network workflow; create a plugin with two independent triggers/outputs and no MCP; derive a third example by adding one justified valid MCP entry without credentials. Keep example names distinct from `agent-package-author`.
- [ ] Add end-to-end tests that invoke representative standalone and bundled skill workflows, call all applicable validators and inspector, assert the no-MCP plugin passes, and assert no unexplained files or host-specific runtime requirements were introduced. Cover a client-extension request through a classified example/test without asserting its behavior is portable.
- [ ] Run `python -m unittest discover -s tests -v`. **Complete when:** three positive scenarios pass and report the actual runtime needs of each example.

## Task 12: Negative authoring and collision scenarios

**Files:** `tests/test_authoring.py`, `tests/test_skill_validation.py`, `tests/test_plugin_validation.py`, `tests/test_mcp_validation.py`; revise runtime files only if a case fails.

- [ ] Exercise invalid metadata, manifest/type/unknown fields, invalid child, `mcp.json` mismatch, path escape, malformed configuration, and wrong or duplicate install-scope names. Model collision checking as a mandatory SKILL.md workflow gate and test that the authoring instructions require it before install/overwrite; do not add an installer CLI without a separate requirement.
- [ ] Verify actionable CLI stderr/stdout, exit `1` versus `2`, stable diagnostic order, and wording that separates strict creator rejection from client partial loading. Repair discovered gaps.
- [ ] Run `python -m unittest discover -s tests -v`. **Complete when:** every negative case fails for its intended reason, and a collision is surfaced before any test fixture's unrelated package is modified.

## Task 13: Source documentation and full conformance review

**Files:** `README.md`; revise `agent-package-author/**`, `examples/**`, `tests/**`, and this plan only to correct identified gaps.

- [ ] Explain the two modes, runtime versus development material, exact CLI commands, Python requirement, YAML subset limitation, host-controlled installation, no publishing in this plan, and the distinction between structural and runtime verification.
- [ ] Run `python -m unittest discover -s tests -v`; run all three CLIs on the relevant examples; run `python -m compileall -q agent-package-author/scripts`; check relative links, unexpected files, and version strings with `rg -n '1\.0\.0|SKILL\.md|mcp\.json|\.codex-plugin|\.claude-plugin' agent-package-author README.md`.
- [ ] Walk sections 1–10 of `SPEC.md` against test names and observed output; record any known limitations without claiming universal client compatibility. **Complete when:** tests and acceptance runs pass, the creator validates itself, and documentation accurately states what was and was not verified.

## Execution and review gates

After each task, record changed paths and its command output; if using Git, commit the verified increment before the next task. Revisit the published standards at the start of implementation and before final conformance claims. A change of normative version or a material contradiction with `SPEC.md` requires a documented spec/plan revision before validator behavior changes. Installation, publishing, and host-specific extensions are separately scoped actions.
