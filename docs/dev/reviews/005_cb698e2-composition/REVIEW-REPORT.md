# Composition review report

## Campaign and assessment

- Campaign: `005_cb698e2-composition`; starting and reviewed source baseline: `cb698e2c0d541a730a3070933778a66f6404a7fc`.
- Working branch: `revision/005_cb698e2-composition`; assessment: U-000 / C-000 in [REVIEW-PLAN.md](REVIEW-PLAN.md).
- Reviewer and date: Codex, 2026-10-18. The user's four bullet notes supply the requested concept, not a published format rule or a source-file attachment.
- Scope: reference size/scope balance as expressed in [skill design](../../../../agent-package-author/references/skill-design.md), [plugin design](../../../../agent-package-author/references/plugin-design.md), [skill review](../../../../agent-package-author/references/skill-review.md) and [plugin review](../../../../agent-package-author/references/plugin-review.md). The [entry](../../../../agent-package-author/SKILL.md), [authoring workflow](../../../../agent-package-author/references/authoring-workflow.md) and [SPEC](../../SPEC.md) were inspected only for routing and contract context.
- Evidence: located source reading and conceptual contrast cases. No revised runtime, target-client trial, structural validator or full twelve-reference audit is claimed. State: focused assessment complete; general U-001–U-005 and any revision remain pending.

## Concept and current articulation

The proposed balance is **cohesive substance at a selectable boundary**. A broad, shallow guide can be complete for its purpose; a narrower procedure can be deep if it owns a distinct decision and execution path. Length itself neither requires splitting nor justifies retaining a weak module. Before splitting, identify the separate concern, enough substance to support its use, a condition visible to the caller before loading, and the prerequisites/handoff that will remain intact. Before retaining a tiny file, ask whether it has a meaningful independent use or belongs with its caller/neighbor. This concerns *references within a skill*; choosing independent *skills within a plugin* is a related but separate level.

| Owner and baseline location | Present guidance | Assessment against the requested balance |
| --- | --- | --- |
| `skill-design.md` lines 3–7 | Coherent capability; focused reusable knowledge in references; task-relevant loading; direct purpose/boundary/condition; smallest useful structure. | Strong entry and optional-resource foundation. It does not explicitly ask whether a proposed reference is a substantial independent unit, whether a thin fragment should be combined, or when an overloaded reference warrants a split. R-001. |
| `plugin-design.md` lines 3–7 | Split independently meaningful *skills*, keep related branches together, assign shared ownership and link sibling guidance. | Appropriate for plugin-level capability boundaries. It should not become a duplicate reference-splitting policy; child reference design is reached through skill design/review. No independent finding. |
| `skill-review.md` lines 9–17, 29–46, 50–53 | Coherent purpose, headings without fragmenting, length not a ceiling, independent use/loading conditions rather than length alone, sufficient result/return and caller checks. | Most of the principle is already present. It can diagnose both extremes indirectly but does not explicitly pair a thin/vague fragment with an overloaded module whose substantial subworkflow has its own loading trigger. R-002. |
| `plugin-review.md` lines 9–31, 61–63 | Distinct plugin capabilities, related branches together, shared owners, conditional loading, concision without a quota; delegates included skill review. | Preserves plugin-versus-reference levels. The skill review owner should supply the detailed reference balance; no second checklist needed here. No independent finding. |
| `SKILL.md` lines 10–27; `authoring-workflow.md` lines 3–9; `SPEC.md` lines 53, 73–75 | Direct entry routing, minimum justified files, proportionate skill content check, optional resources and individual reference conditions. | Routing and checking paths exist. A stronger design/review criterion could travel through these owners without a new module or validator. Whether to codify the concept as a normative APA authoring requirement in SPEC is a subsequent revision decision. |

## Coverage and findings index

| Unit / criterion | Outcome | Evidence and boundary | Finding IDs |
| --- | --- | --- | --- |
| U-000 / C-000, design | Partial articulation | `skill-design.md` lines 3–7 and adjacent authoring/SPEC context. | R-001 |
| U-000 / C-000, assessment | Mostly articulated, paired check implicit | `skill-review.md` lines 9–17 and 35–46; review procedure lines 50–53. | R-002 |
| U-000 / C-000, plugin level | Appropriate separation and delegation | `plugin-design.md` lines 3–7; `plugin-review.md` lines 9–31 and 61–63. | None |
| U-001–U-005 | Not assessed in this checkpoint | Remain in the plan; source-context reads above do not establish full-unit coverage. | Not allocated |

| Finding | Type | Priority | Status | Related finding |
| --- | --- | --- | --- | --- |
| R-001 | Authoring-guidance gap | Medium | Revised and source-rechecked in V-001 | R-002 |
| R-002 | Review-criterion clarity gap | Medium | Revised and source-rechecked in V-001 | R-001 |

## Finding records

### R-001 — Reference boundary decision is underspecified in design guidance

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `agent-package-author/references/skill-design.md` lines 3–7; high confidence from direct text and authoring workflow step 5. |
| Observation and reader consequence | “Focused reusable knowledge,” “task-relevant,” and “smallest structure” support the idea but do not state the two-sided decision. An author can meet direct routing requirements while creating a thin, vaguely scoped reference, or retain a broad procedure with a natural independently invoked subworkflow. This is a guidance gap, not proof that current APA modules are incorrectly split. |
| Proposed correction and meaning limit | Add a compact criterion in `skill-design.md`: keep the entry shallow; give a reference a coherent, sufficiently developed responsibility; combine a fragment without meaningful independent use; split only a distinct substantial concern with a caller-visible trigger, preserving prerequisites and return path. Broad/shallow guidance and narrow/deep procedure are both valid. Avoid a numeric threshold or a mandatory split. If the criterion is adopted as a project requirement, reconcile `docs/dev/SPEC.md` through its document owner. |
| Objective recheck | From design guidance alone, explain decisions for a complete short policy, a thin extra file, and a broad procedure containing an independently selected substantial subworkflow; resulting routes remain discoverable from `SKILL.md`. |
| Current disposition | Accepted 2026-10-18; V-001 revised and source-rechecked this owner. See [REVISION-REPORT.md](REVISION-REPORT.md). General campaign review remains pending. |

### R-002 — Review criteria do not explicitly test both failure modes together

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `agent-package-author/references/skill-review.md` lines 9–17, 35–46, 50–53; high confidence from direct text. |
| Observation and reader consequence | The checklist already rejects splitting on length alone and asks about independent use/loading, cohesion and sufficient result. It does not explicitly prompt the reviewer to catch both an underdeveloped fragment and an overloaded module with a naturally separable, substantial workflow. Reviewers can apply the existing questions correctly, but a lopsided assessment is easier. This is a clarification recommendation, not a missing formal standard rule. |
| Proposed correction and meaning limit | Pair the two alternatives in the local purpose/cohesion criterion: ask whether each reference has enough substance and a clear boundary for its trigger, and whether a current module buries a distinct substantial subworkflow that should load separately. Evaluate caller-visible selection, required context and handoff before suggesting a split/merge. Retain length as a measurement, not an acceptance target. `plugin-review.md` should continue delegating included skill references rather than duplicating this check. |
| Objective recheck | Source review of the same three contrasting cases yields a justified keep/combine/split decision with caller routing, preserved instructions and no numerical ceiling; a plugin case reaches the skill-review owner without a second competing policy. |
| Current disposition | Accepted 2026-10-18; V-001 revised and source-rechecked this owner. See [REVISION-REPORT.md](REVISION-REPORT.md). General campaign review remains pending. |

## Contrasts and evidence limits

| Illustrative case | What the present guidance supports | What the proposed paired criterion would expose |
| --- | --- | --- |
| Short, complete terminology/policy note with a distinct conditional use | Keep if sufficient for its role; do not split or merge due to length alone. | Its purpose, caller trigger and use boundary justify the file. |
| A few generic sentences moved into a new reference without a distinct trigger | Coherence and minimum-file advice may question it. | Combine with caller/neighbor unless a meaningful independent use can be shown. |
| Broad procedural reference containing a separately invoked, substantial recovery path | Independent use/loading condition can support a split. | Check that the recovery path has its own decision and substance and that its prerequisite/return route survives the move. |
| Plugin with two independently useful skills and a shared reference | Plugin design assesses skill split and ownership; skill review assesses actual reference. | Do not use a reference-file size decision as a surrogate for a plugin capability boundary. |

These cases are analytic contrasts, not constructed packages or observed agent executions. No token/cost improvement or numerical file-size claim is supported by this source review. Current reference lengths were not treated as a defect metric. The user notes originated outside this repository; no unseen SDD document is assumed to govern APA.

## Revision handoff and stop

The paired findings have a common policy shape and two current owners: design guidance and the skill-review checklist. The user accepted V-001 on 2026-10-18; [REVISION-PLAN.md](REVISION-PLAN.md) owns its scope and [REVISION-REPORT.md](REVISION-REPORT.md) records actual changes and checks. The baseline observations above remain unchanged. The broader composition review remains queued at U-001; no merge into `main` is selected while the wider campaign remains incomplete.
