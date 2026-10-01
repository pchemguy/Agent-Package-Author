# Agent Package Author Specification

## 1. Purpose and identity

Implement `agent-package-author`, a portable Agent Skill that creates, revises, inspects, and validates (a) standalone Agent Skills and (b) Agent Plugins 1.0 packages containing Agent Skills and, when justified, MCP server configuration. These are two authoring modes within one skill. Inspection and validation serve both modes.

The skill's frontmatter `name` SHALL be `agent-package-author`, and its directory SHALL have the same name. Its description SHALL mention both standalone skills and Agent Plugins so either request can activate it. Before installing a generated package, the workflow SHALL check for a same-name package or skill in the target discovery scope and resolve collisions without overwriting an unrelated item. The name does not assert global uniqueness.

The creator SHALL produce the smallest package that satisfies the user's requested capabilities. The Hello World reference skill is a design exemplar for a deliberately broad feature demonstration; its file count and workflow SHALL NOT be imposed on other skills.

## 2. Standards, scope, and terminology

The creator SHALL target the published Agent Skills specification for skills and Agent Plugins **1.0.0** for plugin packages. Standards are authoritative over summaries, templates, and examples in this repository. A version change SHALL prompt an explicit review of the affected rules and validators; the creator SHALL NOT silently claim conformance to an unimplemented version.

In this document, **SHALL** is a creator requirement, **SHOULD** is a recommended default, and **MAY** denotes an option. A *portable package* uses standard Agent Skills or Agent Plugins components and ordinary documented runtime requirements. *Client extension* means behavior supported by a particular host outside the Agent Plugins v1 portable component model. *Development material* includes tests and examples that the delivered runtime does not require.

The creator SHALL distinguish package-format conformance from runtime availability: a structurally conforming skill or plugin is not proof that every client can run Python, load MCP, support a particular transport, or install the package from the same path. Installation instructions SHALL be separate from the generated package's portable layout.

## 3. Creator package layout

The creator itself SHALL be an Agent Skill. Its planned runtime layout is:

```text
agent-package-author/
├── SKILL.md
├── references/
│   ├── authoring-workflow.md
│   ├── skill-standard.md
│   ├── skill-design.md
│   ├── plugin-standard.md
│   ├── plugin-design.md
│   ├── mcp-packaging.md
│   ├── portability-policy.md
│   ├── validation-policy.md
│   └── hello-world-example.md
├── scripts/
│   ├── inspect_package.py
│   ├── validate_skill.py
│   └── validate_plugin.py
└── assets/
    ├── skill-entry-template.md
    ├── plugin-manifest-template.json
    └── mcp-template.json
```

`SKILL.md` SHALL contain only valid `name` and `description` frontmatter and concise routing, relative resource paths, creation steps, and completion conditions. Each reference SHALL be directly discoverable from it; reading a reference SHALL NOT be required to discover another reference. `references/` contains conditional authoring knowledge; `scripts/` contains deterministic offline helpers; `assets/` contains starting material for generated files. The Hello World example SHALL explain design choices without turning them into universal requirements. Development `SPEC.md`, `PLAN.md`, `README.md`, examples, and tests MAY accompany the source repository but SHALL NOT be necessary to execute the runtime skill.

## 4. Shared authoring workflow

For either mode, the creator SHALL:

1. Identify the requested capability, users, activation phrases, inputs, outputs, runtime constraints, and success and failure cases. Reuse supplied requirements rather than requesting them again.
2. Choose skill or plugin mode. For plugin mode, decide which capabilities merit independently discoverable skills and whether any requirement genuinely needs MCP.
3. Check proposed package and skill names against the intended destination; identify collisions before writing or installing.
4. Classify each proposed component as portable core, standard optional material, client extension, development material, or unsupported/nonportable behavior. Record the disposition of anything outside the core.
5. Define an observable acceptance model, then write the package and its justified resources. A large new project SHOULD have an explicit specification and ordered plan before implementation; a small self-contained skill need not reproduce the Hello World development documents.
6. Run structural checks, inspect cross-file references and capability boundaries, exercise realistic positive and negative scenarios, repair findings, and revalidate.
7. Report output paths, included capabilities, test evidence, required runtime facilities, client-dependent behavior, and any limitations. The workflow SHALL not claim a package is installed or universally supported merely because local validation passed.

The creator SHALL preserve unrelated files when revising an existing package and SHALL distinguish review findings from edits it actually made.

## 5. Standalone skill mode

The generated skill SHALL be a directory whose `SKILL.md` contains valid YAML frontmatter with a matching `name` and a nonempty `description` explaining function and activation. For the portable default, it SHALL use only `name` and `description`; optional standard fields MAY be used when justified and documented, while experimental or client-specific fields SHALL NOT be silently introduced. The skill SHALL satisfy the current Agent Skills name and description constraints.

The workflow SHALL put concise orchestration and conditional routing in `SKILL.md`; focused detail MAY reside in `references/`, executable repeatable operations in `scripts/`, and reusable input material in `assets/`. None of those optional directories SHALL be created just to match a template. Every linked resource SHALL exist and be reachable through a path relative to the skill root. References SHOULD be linked directly from `SKILL.md`, with task-specific loading where useful. Conditional branches SHALL have observable effects when they are part of the requested behavior.

Scripts SHALL state their runtime requirements, provide actionable errors and nonzero failure status, and be tested on their supported paths. Prefer deterministic and offline helpers when the task permits; external tools, network access, and dependencies are permitted only if genuinely required and declared. Where generated artifacts admit mechanical checks, validation SHOULD be independent of their producer. Acceptance SHALL cover representative success, branching when applicable, and meaningful failure behavior.

## 6. Agent Plugin mode

The generated plugin SHALL have root `plugin.json` with the canonical Agent Plugins 1.0.0 schema identifier and a valid `name`. The creator SHALL treat skills at `skills/<skill-name>/SKILL.md` and optional root `mcp.json` as the only v1 portable component locations. `plugin.json` SHALL NOT invent configurable component paths or inline MCP configuration. Every bundled skill SHALL independently satisfy section 5 and be an immediate child of `skills/`; nested skills SHALL NOT be represented as independently exposed. A plugin MAY contain only one kind of component under the standard, though the creator's multi-skill acceptance case SHALL include at least two distinct bundled skills.

The creator SHALL distinguish plugin identity from bundled skill identity, avoid duplicate/confusing activation descriptions, and use separate skills only for capabilities with meaningful independent triggers or workflows. Shared material SHALL have explicit ownership and usable paths; bundled skills SHALL not rely on accidental discovery of another skill's private resources. A consumer's visible presentation of plugin skills is client-defined, so the creator SHALL claim only that conforming clients discover immediate-child skills according to their supported component types.

`plugin.json` SHALL contain only standard top-level fields: `$schema`, `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, `extensions`. The creator SHALL validate their types and constraints against Agent Plugins 1.0.0. It SHALL distinguish strict authoring checks from client loading behavior: an unknown top-level manifest field is nonconforming but is reported and ignored by a conforming client, whereas other fatal manifest violations reject the plugin. Optional absent component locations SHALL not be treated as format errors. A deliverable advertised as fully conforming SHALL have no unknown fields or invalid included components.

## 7. MCP and client extensions

The creator SHALL add `mcp.json` only when MCP capability is requested or needed. It SHALL use the matching Agent Plugins 1.0.0 MCP schema identifier and only `$schema` and `mcpServers` at the root. It SHALL validate each configured server against its transport variant, version alignment, path containment, and placeholder rules. Bundled executables SHALL use package-relative `./` commands; package-relative paths SHALL remain inside the resolved plugin root. It SHALL not embed credentials in configuration. Client-managed authorization and transport support SHALL be described as such.

The creator SHALL isolate explicitly requested client-specific behavior in the relevant reverse-domain `extensions` object and/or corresponding top-level namespace directory, after verifying the target client's documentation and namespace ownership. Client extensions SHALL not be advertised as portable Agent Plugins v1 components. It SHALL not add hooks, commands, custom agents, rules, or host instruction files as implicit portable components. An unsupported requested feature SHALL be documented with a feasible client-specific route or a clear limitation.

## 8. Inspectors and validators

`inspect_package.py PATH` SHALL identify skill versus plugin and inventory the discovered portable components, optional resources, MCP configuration, and client extensions without running included code. It SHALL report uncertainty rather than pronounce behavioral portability from file presence alone.

`validate_skill.py PATH` SHALL check the structural Agent Skills rules, directory/name agreement, discovery metadata, and referenced relative resource existence/containment. It MAY warn on design or portability concerns; it SHALL not present subjective prose-quality judgments as formal standard violations.

`validate_plugin.py PATH` SHALL check the Agent Plugins 1.0.0 manifest, fixed discovery layout, every immediate-child skill using the skill validator, optional MCP configuration, schema alignment, namespace placement, and resolved path containment. It SHALL report errors with component paths and rules. A strict creator success status SHALL require all included advertised components to validate, even where a conforming client might skip one invalid skill or server and continue loading others.

All three helpers SHALL use the Python standard library, require no network or package installation, provide `--help`, return zero for success and nonzero for invalid input or package, and yield stable, actionable diagnostics. A local structural pass SHALL NOT be labeled proof of script execution, MCP connectivity, security, or behavior on every client. The implementation plan SHALL specify exact CLIs, shared validation logic, and tests.

## 9. Verification scenarios and completion

1. **Standalone skill:** Create a small coherent skill, validate it, invoke its representative workflow, and show that no unjustified files or host-specific requirements are present. If it has conditional references, demonstrate the relevant branch and exclusion of irrelevant material.
2. **Multi-skill plugin:** Create a plugin with at least two independently named and discoverable skills, validate the manifest and every skill, and inspect the inventory. The package SHALL remain valid without `mcp.json`.
3. **Plugin with MCP:** Add one justified server configuration; validate its transport-specific fields, schema version, safe paths, and absence of embedded secrets. Connection/handshake verification is a separate runtime test when an environment permits it.
4. **Negative cases:** Reject or precisely diagnose malformed skill metadata, a mismatched skill directory, invalid manifest fields/types, missing or malformed MCP configuration when present, an escaping package path, version mismatch, and an invalid immediate-child skill. Confirm that diagnostics distinguish strict creator failure from client partial-load behavior.
5. **Collision and extension cases:** Detect a same-name item in a target install scope before overwriting it; classify a client-specific request and keep its extension isolated from portable claims.

The implementation is complete when the creator's own skill validates, both authoring modes and inspection operate on the acceptance cases, its offline validators agree with the targeted normative rules, all automated tests and end-to-end scenarios pass, and the README explains installation as a host concern. No installation, publishing, or compatibility claim SHALL be inferred solely from authoring completion.

## 10. Normative source references

- Agent Skills format: https://agentskills.io/specification
- Agent Plugins 1.0.0: https://agent-plugins.org/specification

These links identify the external standards; this document adds requirements for the creator's authoring behavior and acceptance criteria.
