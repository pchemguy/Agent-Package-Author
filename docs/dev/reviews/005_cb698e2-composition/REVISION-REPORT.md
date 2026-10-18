# Composition revision evidence

## Campaign and result

- Campaign: `005_cb698e2-composition`; reviewed source baseline: `cb698e2c0d541a730a3070933778a66f6404a7fc`.
- Plan: [REVISION-PLAN.md](REVISION-PLAN.md); findings: R-001 and R-002 in [REVIEW-REPORT.md](REVIEW-REPORT.md).
- Working branch: `revision/005_cb698e2-composition`, created from `main` at the baseline above.
- Result: V-001 implemented and locally verified in the two runtime reference owners. The broader U-001–U-005 review remains pending, so this is a published action checkpoint, not campaign closure or a merge into `main`.

## V-001 changes and recheck

| Owner | Actual change | Finding |
| --- | --- | --- |
| [Skill design](../../../../agent-package-author/references/skill-design.md) | Explains coherent responsibility, substance appropriate to a reference's role, broad/shallow versus narrow/deep scope, clear use condition, combination of thin fragments, and splitting only a distinct substantial subworkflow with a caller-visible trigger. Preserves entry route, shared prerequisites and return/handoff. | R-001 |
| [Skill review](../../../../agent-package-author/references/skill-review.md) | Pairs completeness with both fragmentation and overloaded-module assessment; a proposed merge/split must preserve caller selection, prerequisites, qualifiers and return. Retains the no-length-quota distinction. | R-002 |

| Source contrast | Assessment from revised owners | Limit |
| --- | --- | --- |
| Short, complete policy/terminology guide with a clear shared or conditional use | Keep when its role is sufficiently developed; length alone does not require combining. | This is an analytic route, not an agent trial. |
| Generic fragment without independent use | Keep in the caller or neighboring owner; no new reference for a file-count or length target. | Actual content must be inspected in a real case. |
| Broad procedure with a distinct substantial recovery subworkflow | Split only if caller can select it before loading, and shared prerequisites and return survive. A cohesive procedure stays together regardless of length. | No numerical threshold or observed improvement is claimed. |
| Plugin with included skills and shared reference | Plugin review retains whole-package composition; skill review owns each included skill's reference assessment. No duplicate plugin-level policy is added. | Client handoff behavior is not tested. |

The entry's existing direct links to design and review remain the route for this criterion. `authoring-workflow.md` still invokes proportionate content review within permitted edits. `plugin-design.md` continues to govern when to split independent *skills*, which is a different boundary. No new Agent Skills format rule, validator error or SPEC requirement was introduced. The existing SPEC minimum-resource and conditional-routing contract is unchanged.

## Verification and limits

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`: 50 tests passed.
- `validate_skill.py agent-package-author` and `inspect_package.py agent-package-author`: zero errors and warnings; twelve references inventoried. Both plugin examples pass `validate_plugin.py`.
- A local Markdown link scan of current README/AGENTS, runtime Markdown, HANDOFF and active campaign records checked 119 targets with none missing; `git diff --check` passed. The scan excludes fenced illustrative code and closed campaign records.
- The source contrasts above assess the intended design/review decisions. Structural checks do not establish prose interpretation or client behavior; no independent agent routing trial was performed.

## Remaining campaign scope

R-001 and R-002 are revised and source-rechecked for V-001; their baseline observations remain in the review report. U-001–U-005 of the general composition review remain unassessed, and any future findings require their own decision. This checkpoint stops after V-001 publication. No closed campaign record is changed.

## V-002 — Presentation policy and example

- Accepted findings: R-008 and R-010 from the completed U-001–U-005 review. The governing SPEC §5 already requires APA to generate a presentation pair for each authored skill; no contract change was made.
- `references/openai-presentation.md` now selects the module for APA creation/substantive revision of a standalone or plugin child skill and for scoped assessment of existing presentation in review-only mode. It explicitly distinguishes APA's deliverable rule from the portable format and forbids generation/replacement during review-only work.
- `README.md` now distinguishes the intentionally sparse shipped example from an APA-authored plugin deliverable, for which each child retains the generated pair. The demonstration points users to a disposable copy if they want to avoid modifying the shipped example.
- Source recheck: a generic standalone request selects one pair; a two-child plugin selects two; scoped review assesses existing files without writes. Existing-file refusal and intentional `--force` remain in the module. No target-client rendering or independent invocation trial is claimed.
- Verification: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` passed (50 tests); `git diff --check` passed. Source trace covered generic standalone, two-child plugin, review-only, and existing-file replacement. These textual rechecks do not establish actual agent routing or client rendering.

## V-003 — Entry and authoring stage order

- Accepted findings: R-003 and R-004. `SKILL.md` now separates pre-write design/template decisions, post-content presentation and validation, and evidence-qualified reporting into short paragraphs. `references/authoring-workflow.md` keeps step 6 as one cohesive procedure with three ordered substeps: proportional content review, per-skill presentation, then structural and behavioral checks/repair.
- Source recheck: entry alone still shows collision checking before writes, conditional MCP template, relevant validator and behavioral evidence before the reporting stop. The workflow preserves unrelated files during revision, and the review-only route still excludes authoring and generation.
- Verification: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` passed (50 tests), `validate_skill.py agent-package-author` exited cleanly, and `git diff --check` passed. The stage trace is source-level, not a target-agent trial.

## V-004 — Conditional design exemplar

- Accepted finding: R-005. `references/hello-world-example.md` now has a compact illustrative acceptance scenario and a requirement-to-resource map covering shared contract, selected audience rules, consumed template, deterministic renderer and independent validator. It states when a simpler skill omits each resource and separates development evidence from installed resources.
- Source recheck: the module can explain its decisions with only its selected text and the entry route, without the hypothetical attachment or source-only README. Branch loading, common prerequisites and a failure case are explicit; no universal file scaffold or size threshold was added.
- Verification: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` passed (50 tests), `validate_skill.py agent-package-author` exited cleanly, and `git diff --check` passed. The exemplar remains an illustrative source case, not an observed generated package.

## V-005 — Evidence, MCP and README navigation

- Accepted findings: R-006, R-007 and R-009. `validation-policy.md` now separates review coverage/owner, findings and permitted effects, and trial setup without splitting the shared evidence module. `mcp-packaging.md` includes both justified MCP authoring and scoped assessment of an existing component, while stating review-only has no write effect. README promotes the complete twelve-reference map to a peer section and identifies its authoring and review routes.
- Source recheck: focused/comprehensive/trial scenarios each locate their rule; an existing mixed or MCP-only plugin review loads MCP guidance but a plugin creation without MCP does not. All twelve map rows remain direct owner links; heading order is authoring, review, map, boundaries.
- Verification: 50 tests passed under `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`. `validate_skill.py` and `inspect_package.py` on the creator passed with zero errors/warnings and twelve references; both shipped plugin examples passed `validate_plugin.py`. The active runtime/README/HANDOFF/campaign Markdown link scan found 123 local targets and none missing; `git diff --check` passed. This is structural/source evidence, not an MCP connection or client activation trial.
