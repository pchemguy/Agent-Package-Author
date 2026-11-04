# Comprehensive review report

## Campaign and assessment

- Campaign: `007_bf115bc-comprehensive-review`; starting and reviewed source baseline: `bf115bce52adf2487462db33440ce7702120080a` on `main`.
- Reviewer/date: Codex, 2026-11-04. The campaign branch begins with the plan-only opening commit `fb5c7986dc694cb6e54fa96b34f1fd232c897394`; report commits do not change the pinned reviewed source.
- Scope and criteria: [REVIEW-PLAN.md](REVIEW-PLAN.md), U-001–U-006. Closed campaign records are excluded from current-source validity checks.
- Evidence boundary: source inventory and primary specification comparison in U-001; entry/reference content inspection in U-002; source inspection, 50 automated tests, CLI checks and disposable-package probes in U-003. No target-client activation or Windows CMD trial has been observed.
- State: U-001–U-003 assessed; U-004–U-006 pending. No revision is accepted or implemented.

## Coverage

| Unit / criterion | Outcome | Evidence and limit | Findings |
| --- | --- | --- | --- |
| U-001 / C-001 | Satisfied within inspected inventory and standards scope | The baseline has 80 tracked files and no tracked symlinks. The delivered skill contains `SKILL.md`, twelve references, four scripts, four assets and `agents/openai.yaml`; development records, examples and tests are outside that directory. Relative links in delivered/reference and example Markdown resolve within their inspected package roots except the intentionally broken `examples/standalone/sample.md` link used as negative sample data. Source searches found no former-checkout absolute dependency in the delivered skill, examples or tests. Compared format claims in `skill-standard.md`, `plugin-standard.md`, `SPEC.md` and templates with the published Agent Skills and Agent Plugins 1.0.0 specifications. This is source evidence, not an isolated-installation trial. | None |
| U-002 / C-002–C-003 | Satisfied in source inspection | Read the creator entry and all twelve references, comparing entry-only routing, scope, content boundary and consequential caller/owner handoffs. See the assessed-depth inventory below. No independent consumer-model routing trial was run. | None |
| U-003 / C-004 | Findings | Read all four Python helpers and seven test files; 50 tests passed. Creator self-validation/inventory and both shipped plugin validators passed; all four CLIs returned zero for `--help`. Disposable probes exposed false success for non-string YAML scalars and links inside references. | R-001, R-002 |
| U-004 / C-005 | Pending | Examples and producer outputs not yet exercised. | — |
| U-005 / C-006–C-007 | Pending | User/developer documentation not yet assessed. | — |
| U-006 / C-008 | Pending | Consolidation follows the preceding units. | — |

## Findings index

| Finding | Type | Priority | Status | Related findings |
| --- | --- | --- | --- | --- |
| R-001 | Structural coverage defect | P2 | Open | R-002 (same validator owner) |
| R-002 | YAML type-validation defect | P1 | Open | R-001 (same validator owner) |

### R-001 — Referenced Markdown links can escape validation coverage

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `agent-package-author/scripts/validate_skill.py`, `validate_skill()` extracts links/literals only from the `SKILL.md` `content` string (around lines 135–150); high confidence from source and disposable-package execution. |
| Observation and consequence | A valid entry links `references/guide.md`, whose body links missing `absent.md` and an outside path. `validate_skill.py`, `validate_plugin.py` and `inspect_package.py` all exited 0; the inspector printed `errors: 0, warnings: 0`. A generated package can therefore report strict structural success while a required loaded reference cannot resolve safely. This is a creator link-coverage problem, not a claim that all Markdown prose is a standard format field. |
| Owner and bounded correction | Skill resource validation plus plugin-root integration and tests. Define which referenced local Markdown files are traversed, resolve each link from its containing file, retain standalone/plugin boundaries and cycle handling, and distinguish code/example text from operative links. Preserve warning-only existing sibling references. |
| Objective recheck and limit | A disposable skill/plugin with a linked reference whose operative link is missing or escapes must fail; a contained sibling reference must remain warning-only and valid fixtures must pass. The present manual U-001 inventory scan does not substitute for the CLI's advertised result. |

### R-002 — Plain numeric YAML metadata is accepted as a string

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `agent-package-author/scripts/validate_skill.py`, `_scalar()` (around lines 28–50) returns every supported plain scalar as text; high confidence from source and disposable-package execution. |
| Observation and consequence | A directory `123` with `name: 123` and `description: 42` passed with exit 0; `description: 42` also passed in an ordinary named skill. YAML interprets these unquoted scalars as numbers, while Agent Skills requires string `name` and `description`. The parser rejects lowercase `true` but misses numeric and other implicitly typed plain forms, so strict success can misclassify invalid metadata. |
| Owner and bounded correction | Frontmatter subset parser and tests. Recognize implicit non-string scalar forms under the selected YAML semantics or return `frontmatter-unverified` rather than coercing them to text; keep quoted numeric strings valid. Include the optional `metadata` string mapping in the same check. |
| Objective recheck and limit | Numeric `name`, `description`, and metadata values fail or are explicitly unverified; quoted string equivalents pass, and existing valid examples remain green. A full YAML parser is not required by the current bounded-parser contract. |

## U-001 evidence and limits

- Inspected `git ls-tree -r` at the full baseline and `git ls-files -s` for symlinks; searched the current package, examples, tests, README and developer entry for checkout-specific paths, removed log names and external references.
- Resolved 34 ordinary relative Markdown links in `agent-package-author/` and `examples/` by path. The sole missing target, `examples/standalone/sample.md` → `absent.md`, is explicitly labeled broken in the sample; it is not a delivered skill dependency. No inspected link resolved outside its selected root. This scan does not parse Markdown code fences, anchors or client loading semantics.
- Checked the published [Agent Skills specification](https://agentskills.io/specification) for entry/frontmatter and optional resources and [Agent Plugins 1.0.0](https://agent-plugins.org/specification) for root containment, fixed component locations and manifest/MCP boundaries. The project uses the 1.0.0 identifiers and treats OpenAI presentation separately. No apparent baseline contradiction was found in these selected assertions; U-002–U-004 will test their implementation and content in depth.
- No source file was changed or executable validation run in this unit. A negative search is limited to tracked and inspected source text; runtime inputs, external clients and untracked files were not evaluated.

## U-002 entry and reference assessment

The 35-line `agent-package-author/SKILL.md` exposes operation and package choice before its twelve-row reference map. Each row supplies a selection condition and a distinct owner/boundary. Review-only routing avoids the authoring workflow and its write/collision steps. The entry's sibling handoff clause distinguishes a named skill entry from shared reference guidance. This is instruction-source evidence, not observed model selection.

| Reference | Assessed content and interface | Result |
| --- | --- | --- |
| `authoring-workflow.md` | Intake, classification, collision, acceptance, content review, presentation and validation order; route from entry. | Cohesive creation procedure; review-only skip remains explicit. |
| `portability-policy.md` | Component classes, client presentation exception, host support caveat; authoring and reporting callers. | Clear classification owner without claiming client behavior. |
| `validation-policy.md` | Four evidence levels, plugin containment and generated-presentation checks; entry and review callers. | Distinguishes source, structural, workflow and target-client evidence. |
| `skill-standard.md` | Skill frontmatter, optional material and standalone versus bundled links; entry/validator interface. | Format guidance remains separate from content-review criteria. |
| `skill-design.md` | Capability, resources and substantive reference boundaries; authoring caller and review handoff. | Shallow design owner with a meaningful distinct decision, not a size-driven fragment. |
| `skill-review.md` | Entry-only routing, reference composition, scope and source/consumer distinction. | Complete detailed skill content assessment procedure. |
| `hello-world-example.md` | Illustrative resource decisions, conditional profiles and independent validator; optional entry route. | Example status and non-template boundary explicit. |
| `plugin-standard.md` | Manifest, components, failure boundaries, extensions and sibling links. | Format owner distinct from composition review. |
| `plugin-design.md` | Split/ownership, sibling link versus handoff, optional shared entry/coordinator. | Cohesive design decision owner; named handoff does not promise activation. |
| `plugin-review.md` | Actual-component inventory, composition, optional `PLUGIN.md`/coordinator, review contrasts. | Detailed package assessment without imposing absent components. |
| `mcp-packaging.md` | Conditional transport/configuration rules and runtime limits. | Short but complete selective MCP guidance, with normative detail routed to the specification. |
| `openai-presentation.md` | Context derivation, helper invocation, replacement policy and validation; authoring caller. | Distinct, substantial client-presentation subworkflow after portable content. |

The two review modules and validation policy share short handoff reminders but do not duplicate their full procedures. Small format/design references have an identifiable independent loading condition. No split, merge or substantive conflict is justified solely by their line counts. The source was read at the baseline; no package code was executed in this unit. Remaining uncertainty: an unprimed target consumer might route differently, so client activation is not inferred.

## U-003 implementation and check evidence

- Inspected `validate_skill.py`, `validate_plugin.py`, `inspect_package.py`, `create_openai_presentation.py`, all seven `tests/*.py` files and `tests/fixtures/format-cases.json`. The tests cover manifest and MCP variants, sibling warning/missing/escape cases in entries, presentation context/replacement preflight, self-validation, three examples and a small MCP JSON-RPC fixture. Assertions of word presence in `test_authoring.py` supply only source-presence evidence, not model routing behavior.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`: 50 tests, OK. `validate_skill.py agent-package-author` returned 0; `inspect_package.py agent-package-author` returned 0 with twelve references, four scripts, four assets, zero errors/warnings and explicit runtime-unverified label. Both shipped `validate_plugin.py` examples returned 0. All four helpers returned 0 with usage on `--help`.
- Disposable plugin with `SKILL.md` → `references/guide.md` → missing and escaping links: both validators and inspector returned 0, as R-001 records. Disposable numeric frontmatter: `name: 123` plus `description: 42`, and ordinary-name `description: 42`, returned 0; `description: true` was reported unverified. No repository source was edited by these probes.
- Positive checks do not establish target-client routing, arbitrary YAML support, MCP connectivity or safety of included scripts. U-004 will exercise the shipped examples and a temporary presentation output independently.

## Next checkpoint

Publish and read back this U-003 report commit before U-004. Next exercise the three shipped examples, optional MCP fixture and presentation generation in a disposable copy.
