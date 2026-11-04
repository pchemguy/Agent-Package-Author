# Comprehensive review report

## Campaign and assessment

- Campaign: `007_bf115bc-comprehensive-review`; starting and reviewed source baseline: `bf115bce52adf2487462db33440ce7702120080a` on `main`.
- Reviewer/date: Codex, 2026-11-04. The campaign branch begins with the plan-only opening commit `fb5c7986dc694cb6e54fa96b34f1fd232c897394`; report commits do not change the pinned reviewed source.
- Scope and criteria: [REVIEW-PLAN.md](REVIEW-PLAN.md), U-001–U-006. Closed campaign records are excluded from current-source validity checks.
- Evidence boundary: source inventory and primary specification comparison in U-001; entry/reference content inspection in U-002; source inspection, 50 automated tests, CLI checks and disposable-package probes in U-003; shipped example and temporary presentation execution in U-004; documentation/link trace in U-005. No target-client activation or Windows CMD trial has been observed.
- State: U-001–U-005 assessed; U-006 pending. No revision is accepted or implemented.

## Coverage

| Unit / criterion | Outcome | Evidence and limit | Findings |
| --- | --- | --- | --- |
| U-001 / C-001 | Satisfied within inspected inventory and standards scope | The baseline has 80 tracked files and no tracked symlinks. The delivered skill contains `SKILL.md`, twelve references, four scripts, four assets and `agents/openai.yaml`; development records, examples and tests are outside that directory. Relative links in delivered/reference and example Markdown resolve within their inspected package roots except the intentionally broken `examples/standalone/sample.md` link used as negative sample data. Source searches found no former-checkout absolute dependency in the delivered skill, examples or tests. Compared format claims in `skill-standard.md`, `plugin-standard.md`, `SPEC.md` and templates with the published Agent Skills and Agent Plugins 1.0.0 specifications. This is source evidence, not an isolated-installation trial. | None |
| U-002 / C-002–C-003 | Satisfied in source inspection | Read the creator entry and all twelve references, comparing entry-only routing, scope, content boundary and consequential caller/owner handoffs. See the assessed-depth inventory below. No independent consumer-model routing trial was run. | None |
| U-003 / C-004 | Findings | Read all four Python helpers and seven test files; 50 tests passed. Creator self-validation/inventory and both shipped plugin validators passed; all four CLIs returned zero for `--help`. Disposable probes exposed false success for non-string YAML scalars and links inside references. | R-001, R-002 |
| U-004 / C-005 | Finding with positive coverage | All three package examples validated; standalone count and both note workflows produced documented outputs. MCP server answered initialize, tools/list, valid heading call and missing-file tool error. Temporary plugin generation produced distinct child presentation and refused replacement. A malformed tool argument produced no response; a non-object request crashed the server. | R-003 |
| U-005 / C-006–C-007 | Findings with positive coverage | Traced README's two illustrative authoring paths and review path against all twelve reference owners and U-003/U-004 outputs; read AGENTS, both root policies and current SPEC/PLAN. Active links resolve; two unresolved raw-regex hits are explicitly hypothetical links inside a fenced example. The network claim and test-command cleanliness need qualification. | R-004, R-005 |
| U-006 / C-008 | Pending | Consolidation follows the preceding units. | — |

## Findings index

| Finding | Type | Priority | Status | Related findings |
| --- | --- | --- | --- | --- |
| R-001 | Structural coverage defect | P2 | Open | R-002 (same validator owner) |
| R-002 | YAML type-validation defect | P1 | Open | R-001 (same validator owner) |
| R-003 | Example MCP runtime defect | P2 | Open | None |
| R-004 | Documentation precision | P3 | Open | None |
| R-005 | Reproducibility/housekeeping | P3 | Open | None |

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

### R-003 — Example MCP server drops malformed calls and can terminate

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `examples/with-mcp/notes-tools/bin/notes_server.py`, `handle()` and `main()`; high confidence from disposable subprocess probes. |
| Observation and consequence | `tools/call` with `arguments.path: 42` emitted a stderr diagnostic but no JSON-RPC response for its request ID, exiting 0. A non-object JSON request `[]` raised an uncaught `AttributeError`, exited 1 and prevented a following valid `tools/list` request from being served. A client can wait for an unanswered call or lose the local server. The bundled tests cover initialize/list but not these failures. |
| Owner and bounded correction | Example server and its runtime tests. Validate request and tool-argument shapes and return a correlated JSON-RPC error or `isError` tool result for recoverable failures; keep the process available for later valid requests. Avoid treating invalid user data as a silent notification. |
| Objective recheck and limit | Feed a malformed request or path type followed by a valid request; each request with an ID receives a response, the valid request still succeeds, and positive heading/missing-file calls remain intact. This is a local fixture behavior finding, not a target-client handshake conclusion. |

### R-004 — README overstates the no-network boundary

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `README.md`, “Boundaries” first bullet (around line 143); high confidence from its wording and the authoring walkthrough. |
| Observation and consequence | “The creator's runtime uses only Python's standard library and no network” can describe the entire agent workflow. Earlier README steps require checking published external specifications, while `agent-package-author/SKILL.md` and references discuss target-client documentation. The actual offline promise applies to bundled Python helpers, not every authoring request. A reader may plan an offline authoring run on a premise the package does not guarantee. |
| Owner and bounded correction | README wording, aligned with validation policy and script docstrings. State that bundled helpers are standard-library/offline; external source consultation and generated-package facilities depend on the task and host. |
| Objective recheck and limit | Follow both README requests and confirm each external consultation is consistent with the narrowed boundary. No network use was observed from the Python helpers. |

### R-005 — Documented test command creates untracked caches

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `README.md`, “Use” commands (around line 19), and root `.gitignore`; high confidence from a disposable checkout copy. |
| Observation and consequence | `python -m unittest discover -s tests -q` passed in a temporary copy but created `tests/__pycache__/` and `agent-package-author/scripts/__pycache__/`; the documented `-v` variant has the same import behavior. `.gitignore` does not exclude them. A developer following README's command gets an untracked checkout; the repository's AGENTS.md instead uses `PYTHONDONTWRITEBYTECODE=1`. |
| Owner and bounded correction | README command or source `.gitignore`, consistent with the developer entry. Prefer one documented practice for a clean checkout without changing the test semantics. |
| Objective recheck and limit | Run the documented command in a fresh disposable copy, verify all tests pass and no untracked bytecode artifacts appear. This is a source-development convenience issue, not a delivered skill format defect. |

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
- Positive checks do not establish target-client routing, arbitrary YAML support, MCP connectivity or safety of included scripts. U-004 records the separate shipped-example and temporary presentation trials.

## U-004 example and presentation evidence

- Read the skill entries across all three example packages, their scripts, the plugin manifests/MCP configuration, the local MCP server and package templates. All three validator CLIs returned 0; `inspect_package.py examples/with-mcp/notes-tools` listed two skills and `note-heading-index (stdio)` with zero errors/warnings and `RUNTIME: not verified by inventory`.
- `count_words.py 'one two three'` printed `3`; `outline.py examples/standalone/sample.md` printed `- First`; `check_links.py` on that sample printed `missing: absent.md`. These are CLI outputs, not client selection trials. The intentionally missing sample link is expected negative data.
- The MCP fixture returned responses for `initialize`, `tools/list`, a heading call producing `First` and `Second`, and a missing-path call with `isError: true`. The invalid-path and non-object probes in R-003 exposed distinct unhandled cases. The official MCP SDK guidance treats invalid tool arguments as a response carrying `isError`, reinforcing the local response/recovery expectation; this review did not run an SDK-backed client.
- Copied the multi-skill example to a temporary directory and ran `create_openai_presentation.py` with default context. It returned 0 and wrote exactly two pairs of child files; both YAML prompts contained their respective `$skill-name`, and both icons parsed as 128×128 SVG. A second run without `--force` returned 1 with `already exists`. No plugin-root presentation or tracked output was changed. Distinct visual legibility and OpenAI client rendering were not tested.
- The minimal manifest and MCP templates use matching 1.0.0 schema identifiers and do not force optional components. The examples intentionally omit generated presentation, while the authoring workflow calls for it in delivered authored skills; U-005 records the documentation of that distinction.

## U-005 documentation and integration evidence

- `README.md` distinguishes the illustrative attachment excerpts and unshipped Project Welcome Pack from runnable `word-count` and `notes-tools` examples. It shows brainstorming, seed/reference/draft roles, package choice, conditional MCP and OpenAI presentation, positive/negative checks, focused/comprehensive review, and explicit review-to-authorized-revision handoff. Its reference loading map names every one of the twelve actual modules with a trigger and use; no module is missing from the map.
- The standalone example's conditional profiles and generated outputs are illustrative, not a recorded consumer trial or shipped runnable package. The shipped examples demonstrate script and validator behavior but do not independently prove agent selection from attachments. README explicitly discloses this distinction, so no behavioral result is inferred from the prose.
- Checked current links in README, AGENTS, root policies, SPEC/PLAN/HANDOFF and delivered Markdown: 101 raw relative matches; two apparent missing targets are `../check-note-links/...` links in a fenced, explicitly illustrative snippet whose required file is said to be hypothetical. Other active targets exist. This path check does not verify anchors or Markdown rendering; reviewed the two exceptions in context rather than labeling them broken active links.
- AGENTS.md orders repository discovery, current handoff and project contract; the attached root policies remain separate from plugin/runtime instructions. `SKILL_DISCOVERY_PROTOCOL.md` is read-only/chat-only and `.agents/` currently has no entries. `WINDOWS_SHELL_POLICY.md` explicitly applies only to Windows execution hosts; its CMD adapter was source-inspected, not executed here. `ROADMAP.md` marks the original tasks complete while `PLAN.md` retains their planning checkboxes; AGENTS distinguishes their purposes.
- R-004 and R-005 are documentation/development findings. No unshipped attachment, client invocation or Windows behavior was represented as observed.

## Next checkpoint

Publish and read back this U-005 report commit before U-006. Then consolidate findings, priorities, dependencies, assessed coverage and unrun client checks; stop before revision.
