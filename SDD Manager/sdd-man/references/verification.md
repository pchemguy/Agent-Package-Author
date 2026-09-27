# Verification Strategy and Routing

Use this reference to design project verification, maintain `docs/dev/verification-map.json`, select checks for changed components, classify failures, and define milestone, phase, and campaign evidence.

## Contents

- [Verification responsibilities](#verification-responsibilities)
- [Derive verification from contracts](#derive-verification-from-contracts)
- [Verification levels](#verification-levels)
- [Verification-map authority](#verification-map-authority)
- [Verification-map structure](#verification-map-structure)
- [Create or bootstrap the map](#create-or-bootstrap-the-map)
- [Maintain the map](#maintain-the-map)
- [Select affected checks](#select-affected-checks)
- [Validate the map](#validate-the-map)
- [Execute verification](#execute-verification)
- [Handle failures](#handle-failures)
- [Classify defect work](#classify-defect-work)
- [Template](#template)

## Verification responsibilities

Keep these responsibilities distinct:

| Source               | Canonical responsibility                                              |
| -------------------- | --------------------------------------------------------------------- |
| SPEC                 | Required behavior, invariants, boundaries, errors, and acceptance     |
| PLAN                 | Checks required by tasks, milestones, phases, and campaign completion |
| LAYOUT               | Physical ownership of source, tests, fixtures, and helpers            |
| Verification map     | Current component and path routing to reusable executable checks      |
| Test suite and tools | Executable verification truth                                         |
| Journal              | Exact checks and successful outcomes executed for a task              |

Do not treat a registry entry as proof that behavior is covered. Do not omit a PLAN- or instruction-required check because the registry lacks it.

## Derive verification from contracts

For every specified capability, derive checks from:

- normal successful behavior;
- public and internal invariants;
- error semantics;
- boundary and empty cases;
- lifecycle and cleanup behavior;
- ownership and resource rules;
- persistent and external format compatibility;
- component interactions;
- system acceptance conditions.

Place tests at the lowest level that can verify the contract reliably. Add broader tests only for behavior that crosses a boundary or cannot be proven at a lower level.

Avoid duplicating identical assertions at every level. Use higher levels to verify integration, not to restate every unit case.

## Verification levels

### Direct component verification

Run focused unit or component checks for every changed implementation component. Cover the changed behavior and relevant boundary cases.

### Dependent-component verification

Run checks for components that consume the changed contract. Determine dependents from the architectural dependency model, not only import statements.

### Integration verification

Run checks for workflows crossing affected component boundaries, public entry points, external formats, persistence, subprocesses, packaging, or installed behavior.

### Non-test checks

Include project-required:

- formatting checks;
- linting;
- static analysis;
- type checking;
- compilation;
- build validation;
- packaging validation;
- generated-file validation;
- docstring or documentation-comment lint;
- documentation builds, API extraction, doctests, compiled examples, and documentation-link checks;
- platform-specific checks.

### Boundary verification

At milestone, phase, and campaign completion, run the exit checks declared by PLAN even when their components were not changed by the final task.

## Verification-map authority

Use `docs/dev/verification-map.json` when source-to-check routing is sufficiently complex to justify persistent structured ownership.

It is especially useful when:

- source and test correspondence is non-obvious;
- several verification levels exist;
- integration targets cover multiple components;
- test selection is costly;
- repeated agents would rediscover the same commands;
- the project needs deterministic restart and status inspection.

For a small project with obvious source and test layout, PLAN and LAYOUT may be sufficient. Do not create a verification map solely to satisfy a generic shape.

When present, treat the map as the canonical current routing registry, not as architectural dependency ownership or future implementation intent.

## Verification-map structure

Use valid JSON with:

- `schema_version`;
- semantic component identifiers;
- current owned source paths;
- stable verification-target identifiers;
- normalized target definitions;
- command argument arrays.

Execute a target from the governed project root by default. A target may define a normalized repository-relative `cwd` for a monorepo or nested package and a mapping of non-secret deterministic environment overrides when the command requires them. Do not store credentials, inherited secret values, absolute machine-specific directories, or shell setup fragments.

Prefer:

```text
component
→ owned source paths
→ reusable verification targets
```

Do not normally map every function to individual test node IDs. Test case names, parameter IDs, and implementation functions are too volatile.

Use a case-level selector only when it is intentionally stable and materially useful, such as isolating an expensive acceptance scenario.

Define a target once even when several components reference it. Use `kind` values meaningful to the project, such as `unit`, `integration`, `acceptance`, `typecheck`, `build`, or `package`.

Store commands as arrays:

```json
["python", "-m", "pytest", "tests/test_component.py"]
```

Do not store shell pipelines, quoting-dependent command strings, environment secrets, or machine-specific absolute paths.

## Create or bootstrap the map

### Greenfield project

1. Let PLAN define future test intent.
2. Create the map when implemented components and test targets first exist.
3. Add a component only when its mapped paths exist in current project state.
4. Add reusable targets in the same task that creates their real tests or checks.
5. Keep planned future files out of the map.

### Existing project

1. Discover test configuration, test roots, and project commands.
2. Collect tests without execution when the runner supports it.
3. Inspect naming, imports, fixtures, markers, coverage configuration, and directory correspondence.
4. Propose component ownership from SPEC and LAYOUT.
5. Identify black-box, public-API, persistence, packaging, and cross-component tests that imports cannot reveal.
6. Validate every registered command or selector.
7. Escalate ambiguous ownership rather than encoding a guess.

Treat import and coverage analysis as evidence. Dynamic imports, dependency injection, subprocesses, fixtures, public interfaces, and external formats make import-only mapping incomplete.

## Maintain the map

Update the map in the same task when that task:

- creates or removes a component;
- creates or removes a test module;
- moves source or tests;
- changes physical test ownership;
- introduces or removes an integration boundary;
- adds or removes a stable project verification command;
- consolidates or splits components;
- changes a target selector.

Include the map in the task's declared transaction scope before modifying it.

Do not register speculative future paths. Do not leave renamed or deleted paths for historical reference.

After checkpoint normalization, remove targets used only by a rejected capability. Retain negative verification when it proves the accepted unsupported-behavior contract.

## Select affected checks

For a task, build the verification set in this order:

1. Map every changed production path to its owning component.
2. Add direct targets for each changed component.
3. Traverse the architectural dependency graph to identify affected dependents.
4. Add dependent-component targets.
5. Add integration targets crossing an affected boundary.
6. Add exact checks required by the active PLAN task.
7. Add checks required by applicable project instructions.
8. Add applicable documentation checks for substantively changed code or in-code documentation.
9. Add milestone, phase, or campaign checks when closing that boundary.
10. Add a broader regression check when risk or project policy requires it.
11. Deduplicate identical commands while preserving narrow-to-broad order.

If a changed path has no component mapping:

- determine whether it is documentation, configuration, generated output, test-only infrastructure, or an unmapped production path;
- add or correct mapping when required;
- do not silently treat it as requiring no tests.

If several components own the same path, require an explicit allowed-overlap rule or correct the ownership model.

## Validate the map

Check mechanically decidable properties:

- valid JSON;
- supported `schema_version`;
- unique component identifiers;
- unique target identifiers;
- repository-relative normalized paths;
- no prohibited or unresolved path traversal;
- nonempty path and target lists under the project's policy;
- every referenced target exists;
- every command is a nonempty array of nonempty strings;
- every optional `cwd` is a normalized repository-relative directory without traversal and exists in current state;
- every optional environment key and value is a nonempty string and contains no recorded secret;
- referenced current paths exist;
- renamed or deleted paths are absent;
- path ownership overlaps are explicitly allowed;
- no orphan target remains unless the project permits global targets.

When supported and safe, collect each registered test target without executing it. Require a nonempty collection for targets expected to select tests.

Do not make semantic sufficiency mechanically decidable when it is not. Review whether mapped tests actually correspond to the declared contracts.

## Execute verification

Before execution:

1. resolve commands, working directories, and permitted non-secret environment overrides from the map, PLAN, and project instructions;
2. record the intended verification in task preflight;
3. confirm required environments and dependencies are available;
4. identify expensive or destructive checks;
5. preserve exact argument arrays and execute without shell reinterpretation.

Execute from narrowest to broadest:

```text
direct
→ dependent
→ integration
→ lint/type/build/package
→ milestone or phase
→ campaign acceptance
```

Record exact executed commands and outcomes in the completion record. When the map is used, record its schema version and content hash or equivalent durable identity when practical.

Do not record success for a command that was skipped, unavailable, interrupted, or only partially executed.

## Handle failures

### Task-caused failure

Fix a failure inside the current transaction when it results from the task and the fix belongs to its declared behavior.

If another path must change, follow declared scope extension before modification. Repeat every affected check after the fix.

### Pre-existing or unrelated failure

Determine whether the failure existed before the task and whether it blocks required completion evidence.

- Do not absorb it silently into the task.
- Do not modify an unrelated path without authorization and preparation.
- Do not claim completion when a required check remains failing.
- Report or plan separate corrective work when it does not belong to the current task.

### Environment failure

Distinguish a project failure from an unavailable service, missing platform, absent tool, permission problem, or transient environment issue.

If a required check cannot run, the task is not complete. Follow controlled-stop or escalation rules; do not substitute a weaker check without authority.

### Prohibited repair

Never:

- delete a valid assertion to obtain green status;
- broaden accepted output without a contract decision;
- mark a test expected-to-fail instead of fixing required behavior;
- exclude an affected test from selection merely because it fails;
- change unrelated behavior to satisfy the current task.

## Classify defect work

Before fixing a reported bug, classify it:

| Classification                                | Required response                                      |
| --------------------------------------------- | ------------------------------------------------------ |
| Implementation violates adequate SPEC         | Correct implementation and tests within a bounded task |
| SPEC is missing or ambiguous                  | Return to document review before choosing behavior     |
| User wants different intended behavior        | Create a change or checkpoint-revision workflow        |
| Defect reveals architectural boundary failure | Return to exploration or architectural revision        |
| Failure is external or environmental          | Preserve project state and report the blocker          |

Do not label an intended-behavior change as a bug merely to bypass specification revision.

## Template

Use `../assets/templates/verification-map.json` as a valid minimal example. Replace its example components, paths, target identifiers, and commands with current project values. Preserve valid JSON throughout editing.
