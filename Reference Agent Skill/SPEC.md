# Hello World Reference Skill Specification

## 1. Purpose

Implement `hello-world`, a minimal-complete, vendor-neutral reference Agent Skill.

The skill demonstrates, through a small Project Welcome Pack workflow:

- skill discovery and activation;
- progressive disclosure from `SKILL.md` to task-specific resources;
- conditional reference loading;
- Markdown reference resources;
- static assets;
- deterministic Python script execution;
- artifact generation;
- independent validation;
- positive, branch, and negative test scenarios.

The skill is intended as a compact template for Codex/ChatGPT Work, Gemini, local agents, and other systems compatible with the common Agent Skills model.

## 2. Compatibility contract

The skill SHALL use only portable Agent Skills conventions and ordinary filesystem/process semantics.

The skill SHALL NOT require:

- vendor-specific metadata or instruction files;
- proprietary tool names or host APIs;
- experimental or implementation-specific frontmatter fields;
- host-specific installation paths;
- network access;
- third-party Python packages.

`SKILL.md` SHALL use only the portable required discovery metadata:

```yaml
---
name: hello-world
description: <concise activation description>
---
```

The portable runtime skill consists of:

```text
SKILL.md
references/
scripts/
assets/
```

Repository support material such as `examples/`, `tests/`, and `README.md` MAY be present but SHALL NOT be required by the runtime workflow.

## 3. Repository layout

```text
hello-world/
├── SKILL.md
├── references/
│   ├── workflow.md
│   ├── output-contract.md
│   ├── contributor-profile.md
│   └── user-profile.md
├── scripts/
│   ├── render.py
│   └── validate.py
├── assets/
│   └── welcome-template.md
├── examples/
│   ├── contributor.json
│   ├── user.json
│   └── invalid.json
├── tests/
│   ├── test_render.py
│   └── test_validate.py
└── README.md
```

Resources SHALL remain directly reachable from `SKILL.md`. The skill SHALL NOT depend on deep reference chains.

## 4. Skill behavior

The skill generates a Project Welcome Pack from structured project information.

Minimum logical input:

- project name;
- project description;
- audience: `contributor` or `user`.

The workflow SHALL:

1. normalize and validate the requested input;
2. read `references/workflow.md`;
3. read `references/output-contract.md`;
4. read exactly the audience-specific profile required by the request:
   - `references/contributor-profile.md`, or
   - `references/user-profile.md`;
5. use `assets/welcome-template.md`;
6. invoke `scripts/render.py`;
7. invoke `scripts/validate.py`;
8. report success only after validation succeeds.

The workflow SHALL NOT require the irrelevant audience profile.

This branching behavior is the primary demonstration of task-specific progressive disclosure.

## 5. Generated artifacts

A successful run SHALL create:

```text
out/
├── WELCOME.md
└── welcome.json
```

`WELCOME.md` is the human-readable welcome document.

`welcome.json` is the machine-readable manifest for the generated pack.

Identical normalized input SHALL produce deterministic output.

## 6. Reference resources

### 6.1 `workflow.md`

Defines detailed transformation and generation rules that are intentionally omitted from `SKILL.md`.

Its requirements SHALL have observable effects on generated artifacts.

### 6.2 `output-contract.md`

Defines the normative structure and invariants of `WELCOME.md` and `welcome.json`.

At minimum, `welcome.json` SHALL contain:

- `schema_version`;
- `project`;
- `audience`;
- `sections`;
- `generated_by`.

`schema_version` SHALL equal `1`.

### 6.3 Audience profiles

`contributor-profile.md` and `user-profile.md` SHALL define meaningfully different output requirements.

The contributor profile SHALL require a final section named `First tiny change` containing exactly one concrete starter task.

The user profile SHALL require a final section named `Where to get help` and SHALL NOT require contribution instructions.

The differences SHALL be mechanically or structurally observable in generated output.

## 7. Asset

`assets/welcome-template.md` SHALL be a genuine reusable content template, not an instruction document disguised as an asset.

It SHALL provide the stable structure consumed by the rendering workflow while leaving profile-dependent content to the selected reference rules.

## 8. Executable helpers

Both scripts SHALL:

- run with Python using only the standard library;
- be deterministic;
- require no network access;
- expose a documented CLI;
- return exit code `0` on success and nonzero on failure;
- emit concise actionable diagnostics.

### 8.1 `render.py`

`render.py` SHALL transform validated input plus the applicable template/profile rules into `WELCOME.md` and `welcome.json`.

It SHALL reject malformed or unsupported input.

### 8.2 `validate.py`

`validate.py` SHALL independently validate generated artifacts against the output contract and applicable audience requirements.

It SHALL detect structural or semantic violations and identify the failing artifact or rule.

The runtime pattern demonstrated by the skill is:

```text
generate -> validate -> repair if required -> validate again
```

## 9. Fixtures and tests

`examples/` and `tests/` are repository verification material and are not part of the portable runtime contract.

The fixtures SHALL include:

- a valid contributor input;
- a valid user input;
- an invalid input.

Automated tests SHALL verify at minimum:

- deterministic rendering;
- contributor-specific output;
- user-specific output;
- rejection of invalid input;
- successful validation of valid artifacts;
- failed validation of deliberately corrupted artifacts;
- conventional script exit codes.

## 10. Acceptance scenarios

### 10.1 Contributor scenario

Given the contributor fixture:

- the contributor profile SHALL apply;
- the user profile SHALL not be required;
- `WELCOME.md` SHALL contain `First tiny change`;
- `welcome.json` SHALL identify `audience` as `contributor`;
- validation SHALL succeed.

### 10.2 User scenario

Given the user fixture:

- the user profile SHALL apply;
- the contributor profile SHALL not be required;
- `WELCOME.md` SHALL contain `Where to get help`;
- contributor-specific instructions SHALL not be required;
- `welcome.json` SHALL identify `audience` as `user`;
- validation SHALL succeed.

### 10.3 Negative scenario

Given invalid input or deliberately corrupted generated output:

- the relevant script SHALL return nonzero;
- validation SHALL fail;
- the diagnostic SHALL identify the violated rule sufficiently for correction.

## 11. Completion criteria

The implementation is complete when:

- the repository layout conforms to this specification;
- the runtime skill contains no required vendor-specific behavior;
- all portable resources are reachable directly from `SKILL.md`;
- both audience branches produce distinct valid artifacts;
- the negative scenario fails as specified;
- all automated tests pass;
- the README explains installation as a host concern and does not bind the skill package to a particular agent platform.
