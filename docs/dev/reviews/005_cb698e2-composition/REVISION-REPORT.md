# Reference boundary revision evidence

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
