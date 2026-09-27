# Hello World Reference Skill

`hello-world` is a minimal-complete, vendor-neutral reference Agent Skill. It demonstrates discovery metadata, progressive disclosure, conditional reference loading, reusable assets, deterministic Python helpers, artifact generation, and independent validation through a small Project Welcome Pack workflow.

## Portable runtime

The runtime skill is intentionally limited to the common portable structure:

```text
SKILL.md
references/
scripts/
assets/
```

`SKILL.md` is the skill entry point and orchestration layer. `references/` contains task-specific Markdown rules, `scripts/` contains deterministic executable helpers, and `assets/` contains reusable static material.

The skill does not require vendor-specific metadata, proprietary tool names, host APIs, network access, or third-party Python packages.

## Repository support material

The repository also contains:

```text
examples/
tests/
SPEC.md
PLAN.md
README.md
```

These files support development, demonstration, and verification. They are not required by the portable runtime workflow.

## Input model

The renderer accepts a JSON object with three required non-empty string fields:

```json
{
  "project": "Example Calculator",
  "description": "A small Python CLI for evaluating arithmetic expressions.",
  "audience": "contributor"
}
```

`audience` must be either `contributor` or `user`.

## Output model

A successful run produces:

```text
out/
├── WELCOME.md
└── welcome.json
```

The contributor and user branches intentionally produce different final sections. The manifest records the audience and ordered Markdown section names.

## Example commands

Contributor branch:

```console
python scripts/render.py --input examples/contributor.json --output out/contributor
python scripts/validate.py out/contributor
```

User branch:

```console
python scripts/render.py --input examples/user.json --output out/user
python scripts/validate.py out/user
```

Invalid input:

```console
python scripts/render.py --input examples/invalid.json --output out/invalid
```

The invalid command returns a nonzero exit code with an actionable diagnostic.

## Progressive disclosure

The intended skill flow is:

```text
discovery metadata
    -> SKILL.md
        -> references/workflow.md
        -> references/output-contract.md
        -> exactly one audience profile
        -> assets/welcome-template.md
        -> scripts/render.py
        -> scripts/validate.py
```

The irrelevant audience profile is not required for a run. Resources remain shallow and are directly reachable from `SKILL.md`.

## Acceptance scenarios

The reference implementation demonstrates three canonical scenarios:

- contributor input produces `First tiny change` and passes validation;
- user input produces `Where to get help` and passes validation;
- invalid input or corrupted output returns nonzero and reports the violated rule.

Repeated rendering of the same normalized input is byte-for-byte deterministic.

## Tests

Run the dependency-free test suite with:

```console
python -m unittest discover -s tests -v
```

## Installation

Installation and discovery locations are host responsibilities. Copy or register the `hello-world` skill directory according to the target agent's supported skill-discovery mechanism.

The portable skill contract does not prescribe a Codex-, Gemini-, Claude-, or local-agent-specific installation path. A compatible host only needs to discover `SKILL.md`, make the bundled resources available, and permit ordinary Python script execution.
