# Hello World Reference Skill Implementation Plan

## 1. Plan objective

Implement the `hello-world` reference skill defined by `SPEC.md` as a sequence of small, verifiable tasks.

Each task SHALL:

- modify only the paths listed for that task;
- leave the repository in a coherent state;
- include its own verification command(s);
- be considered complete only when its completion condition is satisfied.

The plan assumes execution from the repository root.

## 2. Task 1 — Create repository skeleton

### Scope

Create the required directory structure and placeholder files without implementing runtime behavior.

### Paths

```text
SKILL.md
references/
scripts/
assets/
examples/
tests/
README.md
```

Create placeholders for:

```text
references/workflow.md
references/output-contract.md
references/contributor-profile.md
references/user-profile.md
scripts/render.py
scripts/validate.py
assets/welcome-template.md
examples/contributor.json
examples/user.json
examples/invalid.json
tests/test_render.py
tests/test_validate.py
```

### Verification

```console
python -c "from pathlib import Path; required=['SKILL.md','references/workflow.md','references/output-contract.md','references/contributor-profile.md','references/user-profile.md','scripts/render.py','scripts/validate.py','assets/welcome-template.md','examples/contributor.json','examples/user.json','examples/invalid.json','tests/test_render.py','tests/test_validate.py','README.md']; missing=[p for p in required if not Path(p).exists()]; assert not missing, missing"
```

### Completion condition

All required paths exist and no vendor-specific files or directories have been introduced.

## 3. Task 2 — Implement `SKILL.md`

### Scope

Implement the portable skill entry point and orchestration layer.

`SKILL.md` SHALL:

- contain only `name` and `description` in YAML frontmatter;
- define applicability and required logical input;
- route to `workflow.md` and `output-contract.md`;
- select exactly one audience profile;
- reference the asset and both scripts;
- require validation before success;
- avoid vendor-specific instructions or tool names.

### Paths

```text
SKILL.md
```

### Verification

```console
python -c "from pathlib import Path; s=Path('SKILL.md').read_text(encoding='utf-8'); assert s.startswith('---'); assert 'name:' in s and 'description:' in s; assert 'references/workflow.md' in s; assert 'references/output-contract.md' in s; assert 'references/contributor-profile.md' in s; assert 'references/user-profile.md' in s; assert 'assets/welcome-template.md' in s; assert 'scripts/render.py' in s; assert 'scripts/validate.py' in s"
```

### Completion condition

`SKILL.md` fully expresses the portable orchestration contract without duplicating detailed reference rules.

## 4. Task 3 — Implement reference resources

### Scope

Implement all Markdown reference resources.

Requirements SHALL remain shallow and directly reachable from `SKILL.md`.

### Paths

```text
references/workflow.md
references/output-contract.md
references/contributor-profile.md
references/user-profile.md
```

### Required outcomes

`workflow.md` SHALL define the detailed generation flow.

`output-contract.md` SHALL define:

- required output files;
- required Markdown structure;
- required `welcome.json` fields;
- `schema_version == 1`;
- validation invariants.

`contributor-profile.md` SHALL require:

- final section `First tiny change`;
- exactly one concrete starter task.

`user-profile.md` SHALL require:

- final section `Where to get help`;
- no required contribution instructions.

### Verification

```console
python -c "from pathlib import Path; c=Path('references/contributor-profile.md').read_text(encoding='utf-8'); u=Path('references/user-profile.md').read_text(encoding='utf-8'); o=Path('references/output-contract.md').read_text(encoding='utf-8'); assert 'First tiny change' in c; assert 'Where to get help' in u; assert 'schema_version' in o and 'generated_by' in o"
```

### Completion condition

Each reference file defines distinct, observable behavior and no reference depends on deeper reference chaining.

## 5. Task 4 — Implement the reusable asset

### Scope

Implement the stable Markdown template consumed by rendering.

The asset SHALL contain content structure/placeholders only and SHALL NOT duplicate procedural instructions from the references.

### Paths

```text
assets/welcome-template.md
```

### Verification

```console
python -c "from pathlib import Path; s=Path('assets/welcome-template.md').read_text(encoding='utf-8'); assert 'project' in s.lower(); assert 'description' in s.lower()"
```

### Completion condition

The template is reusable for both audience branches and contains no vendor-specific or execution instructions.

## 6. Task 5 — Implement `render.py`

### Scope

Implement the deterministic artifact generator using only the Python standard library.

The script SHALL:

- expose a documented CLI;
- read structured JSON input;
- validate required input fields;
- support only `contributor` and `user`;
- consume the shared asset;
- generate `WELCOME.md` and `welcome.json`;
- apply audience-specific output rules;
- write deterministic output;
- return `0` on success and nonzero on failure;
- emit concise diagnostics.

### Paths

```text
scripts/render.py
```

### Verification

```console
python scripts/render.py --help
python -m py_compile scripts/render.py
```

### Completion condition

The script is syntactically valid, exposes the required CLI, uses no third-party imports, and is ready for fixture-driven execution.

## 7. Task 6 — Implement fixtures

### Scope

Create two valid inputs and one invalid input.

### Paths

```text
examples/contributor.json
examples/user.json
examples/invalid.json
```

### Required outcomes

- `contributor.json` SHALL represent a valid contributor request.
- `user.json` SHALL represent a valid user request.
- `invalid.json` SHALL violate at least one required input rule.

### Verification

```console
python -c "import json; from pathlib import Path; [json.loads(Path(p).read_text(encoding='utf-8')) for p in ['examples/contributor.json','examples/user.json','examples/invalid.json']]"
```

### Completion condition

All fixtures are valid JSON and exercise both supported branches plus one input failure path.

## 8. Task 7 — Verify rendering behavior

### Scope

Exercise `render.py` against the valid and invalid fixtures before implementing the independent validator.

### Paths

No new paths required.

Generated verification artifacts MAY use temporary directories.

### Verification

```console
python scripts/render.py --input examples/contributor.json --output .tmp/contributor
python scripts/render.py --input examples/user.json --output .tmp/user
python scripts/render.py --input examples/invalid.json --output .tmp/invalid
```

The invalid command SHALL return nonzero.

Additional checks:

```console
python -c "import json; from pathlib import Path; c=Path('.tmp/contributor/WELCOME.md').read_text(encoding='utf-8'); u=Path('.tmp/user/WELCOME.md').read_text(encoding='utf-8'); cj=json.loads(Path('.tmp/contributor/welcome.json').read_text(encoding='utf-8')); uj=json.loads(Path('.tmp/user/welcome.json').read_text(encoding='utf-8')); assert 'First tiny change' in c; assert 'Where to get help' in u; assert cj['audience']=='contributor'; assert uj['audience']=='user'"
```

### Completion condition

Both valid branches generate distinct correct artifacts and invalid input is rejected.

## 9. Task 8 — Implement `validate.py`

### Scope

Implement the independent artifact validator using only the Python standard library.

The script SHALL:

- expose a documented CLI;
- inspect `WELCOME.md` and `welcome.json`;
- enforce the common output contract;
- enforce audience-specific requirements;
- detect missing or malformed artifacts;
- return `0` on success and nonzero on failure;
- produce actionable diagnostics.

The validator SHALL determine validity from generated artifacts and SHALL NOT depend on `render.py` internals.

### Paths

```text
scripts/validate.py
```

### Verification

```console
python scripts/validate.py --help
python -m py_compile scripts/validate.py
python scripts/validate.py .tmp/contributor
python scripts/validate.py .tmp/user
```

### Completion condition

Both valid generated outputs pass independent validation.

## 10. Task 9 — Verify negative validation

### Scope

Prove that validation detects deliberately corrupted output.

### Paths

No source paths required.

Temporary verification copies MAY be created under `.tmp/`.

### Verification

Create a corrupted copy, for example by removing the required contributor section:

```console
python -c "from pathlib import Path; import shutil; src=Path('.tmp/contributor'); dst=Path('.tmp/corrupt'); shutil.rmtree(dst, ignore_errors=True); shutil.copytree(src,dst); p=dst/'WELCOME.md'; p.write_text(p.read_text(encoding='utf-8').replace('## First tiny change','## Removed section'), encoding='utf-8')"
python scripts/validate.py .tmp/corrupt
```

The final command SHALL return nonzero and identify the violated rule.

### Completion condition

At least one deliberate structural corruption is rejected with an actionable diagnostic.

## 11. Task 10 — Implement automated tests

### Scope

Implement repository-level tests for generation and validation behavior.

Tests SHALL cover at minimum:

- deterministic rendering;
- contributor-specific output;
- user-specific output;
- invalid input rejection;
- validation success for valid artifacts;
- validation failure for corrupted artifacts;
- script exit-code behavior.

Tests SHALL use only the Python standard library so the repository remains dependency-free.

### Paths

```text
tests/test_render.py
tests/test_validate.py
```

### Verification

```console
python -m unittest discover -s tests -v
```

### Completion condition

The complete automated test suite passes.

## 12. Task 11 — Implement README

### Scope

Document the reference skill for human readers.

`README.md` SHALL explain:

- purpose;
- portable runtime structure;
- distinction between runtime resources and repository support material;
- input and output model;
- example commands;
- acceptance scenarios;
- installation as a host responsibility;
- absence of vendor-specific runtime requirements.

It SHALL NOT prescribe a single vendor-specific installation path as part of the skill contract.

### Paths

```text
README.md
```

### Verification

```console
python -c "from pathlib import Path; s=Path('README.md').read_text(encoding='utf-8').lower(); assert 'portable' in s; assert 'skill.md' in s; assert 'installation' in s; assert 'vendor' in s"
```

### Completion condition

The README accurately describes the implemented portable skill without contradicting `SPEC.md`.

## 13. Task 12 — Final conformance and acceptance verification

### Scope

Run the complete verification suite and inspect the repository for portability violations.

### Paths

No implementation changes unless verification reveals a defect.

### Verification

Run automated tests:

```console
python -m unittest discover -s tests -v
```

Run contributor scenario:

```console
python scripts/render.py --input examples/contributor.json --output .tmp/final-contributor
python scripts/validate.py .tmp/final-contributor
```

Run user scenario:

```console
python scripts/render.py --input examples/user.json --output .tmp/final-user
python scripts/validate.py .tmp/final-user
```

Run invalid-input scenario:

```console
python scripts/render.py --input examples/invalid.json --output .tmp/final-invalid
```

The invalid-input command SHALL return nonzero.

Check deterministic output by rendering the same fixture twice and comparing bytes:

```console
python scripts/render.py --input examples/contributor.json --output .tmp/determinism-a
python scripts/render.py --input examples/contributor.json --output .tmp/determinism-b
python -c "from pathlib import Path; a=Path('.tmp/determinism-a'); b=Path('.tmp/determinism-b'); assert (a/'WELCOME.md').read_bytes()==(b/'WELCOME.md').read_bytes(); assert (a/'welcome.json').read_bytes()==(b/'welcome.json').read_bytes()"
```

Review source files for forbidden dependencies or host bindings.

### Completion condition

Implementation is complete only when:

- all tests pass;
- both valid acceptance scenarios pass validation;
- the invalid scenario fails as required;
- repeated rendering is byte-for-byte deterministic;
- the runtime skill requires only `SKILL.md`, `references/`, `scripts/`, and `assets/`;
- no vendor-specific metadata, proprietary APIs, host-specific installation paths, network dependencies, or third-party Python packages are required.
