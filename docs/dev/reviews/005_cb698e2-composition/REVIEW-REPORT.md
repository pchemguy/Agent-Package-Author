# Composition review report

## Campaign and assessment

- Campaign: `005_cb698e2-composition`; starting and reviewed source baseline: `cb698e2c0d541a730a3070933778a66f6404a7fc`.
- Working branch: `revision/005_cb698e2-composition`; assessment: U-000 / C-000 in [REVIEW-PLAN.md](REVIEW-PLAN.md).
- Reviewer and date: Codex, 2026-10-18. The user's four bullet notes supply the requested concept, not a published format rule or a source-file attachment.
- Scope: reference size/scope balance as expressed in [skill design](../../../../agent-package-author/references/skill-design.md), [plugin design](../../../../agent-package-author/references/plugin-design.md), [skill review](../../../../agent-package-author/references/skill-review.md) and [plugin review](../../../../agent-package-author/references/plugin-review.md). The [entry](../../../../agent-package-author/SKILL.md), [authoring workflow](../../../../agent-package-author/references/authoring-workflow.md) and [SPEC](../../SPEC.md) were inspected only for routing and contract context.
- Evidence: located source reading and conceptual contrast cases. No revised runtime, target-client trial, structural validator or full twelve-reference audit is claimed. State: U-000–U-003 assessed; V-001 completed on the campaign branch. U-004–U-005 remain pending; new recommendations are not accepted repairs.

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

## U-001 — Entry and activation composition

- Exact assessed source: `agent-package-author/SKILL.md` at `527e77a754ed0dc53ffea99519e26ff490f533ef` (unchanged from the campaign baseline). Criteria C-001 and C-002; source inspection only.
- Reverse outline: frontmatter selects the capability; opening paragraph selects operation and effects; routing introduction/table identifies twelve owners, conditions and boundaries; next paragraph gives skill/plugin and optional-component qualifications; final paragraph summarizes authorized authoring, validation and reporting.
- Direct-link inventory check: twelve `references/*.md` links in the routing table match all twelve shipped references and resolve locally. This checks discoverability, not client selection.

| Scenario | Source route and stop | Assessment |
| --- | --- | --- |
| Focused entry/reference question | Select review-only, the relevant skill-review criterion and evidence owner; return scoped findings without authoring. | C-001/C-002 satisfied. |
| Comprehensive standalone skill | Inventory selected skill and references through skill review; format guidance only for a format claim. | C-001/C-002 satisfied. |
| Comprehensive mixed plugin | Plugin review plus skill review for actual children; MCP guidance when the package contains it. | C-001/C-002 satisfied. |
| Authorized authoring/revision | Authoring workflow and applicable package owners; collision check, content check, presentation, structural and behavioral verification. | Route present; final paragraph density noted in R-003. |
| Structural-only inspection | Matching CLI and validation evidence; skip the authoring workflow. | C-001/C-002 satisfied. |
| Existing no-skill plugin | Plugin owners and actual components; no invented child skill review or presentation. | C-001/C-002 satisfied. |

### R-003 — Final entry paragraph obscures authoring stages

| Field | Evidence |
| --- | --- |
| Baseline location and confidence | `agent-package-author/SKILL.md` line 31, a 112-word paragraph; high confidence in the text, medium confidence in reader impact without a consumer trial. |
| Observation and consequence | The paragraph moves from collision/authorization to package shape, generated presentation, templates, validation, runtime evidence and reporting. Each qualification is relevant to an authoring request, but their sequence is difficult to scan at the moment of selection, especially the distinction between checks and claims. This is an editorial recommendation, not a demonstrated missed action. |
| Bounded correction and meaning implication | Group the same actions into compact ordered stages or two to three purpose-specific paragraphs in the entry; retain pre-write collision checking, post-content presentation, optional MCP template, distinct structural/behavioral evidence and completion limits. Do not move necessary pre-action gates into a reference without an entry reminder or create a new module for these sentences. |
| Objective recheck | From entry alone, locate the pre-write gate, conditional generation, applicable validator, behavioral evidence and reporting stop in order; cross-check authoring workflow and no-review-only side effect. |
| Disposition | Open recommendation; no runtime edit authorized by this review. |

No finding was assigned to the twelve-row map merely for its length: each shipped module has a direct trigger, owner and boundary, and an entry-only task can select without opening all twelve. The other two long entry paragraphs group one controlling concern each (operation effects; package qualification). U-002–U-005 remain unassessed at this checkpoint.

## U-002 — Individual reference composition

- Exact runtime candidate: `527e77a754ed0dc53ffea99519e26ff490f533ef`; intervening commits changed only the campaign report. All twelve `references/*.md` were read at source level for C-003/C-004. Length measurements are orientation, not acceptance ceilings.

| Reference | Role and internal trajectory | Assessment |
| --- | --- | --- |
| `authoring-workflow.md` | Seven-step intake, selection, collision, classification, acceptance, creation/verification, result procedure. | Complete overall; step 6 combines multiple distinct stages in one list item (R-004). |
| `portability-policy.md` | Component classification table, host limit, OpenAI presentation exception. | Coherent broad/shallow policy; short exception is sufficient and linked to its owner. |
| `validation-policy.md` | Evidence taxonomy, review coverage, structural/tool checks, plugin links, presentation, client failure boundaries, report. | One shared evidence owner is justified; paragraph 12 overloads review scope, output, effects and trial setup (R-006). |
| `skill-standard.md` | Normative metadata, optional fields, resource/path boundary. | Compact format guide with source and policy distinctions; no split indicated. |
| `skill-design.md` | Capability, conditional routing, reference boundary, acceptance cases. | V-001 clarifies the local design decision; cohesive and appropriately developed. |
| `skill-review.md` | Shared criteria, entry, reference routing/content, review procedure and contrasts. | Long but cohesive review procedure; V-001's paired reference criterion sits in the correct section. |
| `hello-world-example.md` | Two paragraphs name a rich Project Welcome Pack and warn against copying its file count. | Useful caution, but sparse as an independently loaded design exemplar (R-005). |
| `plugin-standard.md` | Manifest and discovery, containment, failure boundaries, extensions. | Dense format summary but conceptually grouped; no natural independent subworkflow identified. |
| `plugin-design.md` | Capability split, shared links, optional coordination, component/extension/presentation limits. | Coherent plugin-level guidance; reference-level split remains with skill design. |
| `plugin-review.md` | Composition, conditional shared entry, conditional coordinator, procedure and contrasts. | Optional sections have selection conditions inside the file. A split might save loading in a focused request, but source inspection alone does not show a better boundary once added routing and shared handoffs are counted; no split recommendation. |
| `mcp-packaging.md` | Optional trigger/schema, local transport, remote transport/security and evidence limit. | Compact conditional guide with a clear role; no material composition finding. |
| `openai-presentation.md` | Context derivation, output contract, generator commands/example, verification. | Procedural module with appropriate example and client limit; no material composition finding. |

### R-004 — Authoring step 6 contains several operational stages

| Field | Evidence |
| --- | --- |
| Location and confidence | `agent-package-author/references/authoring-workflow.md` line 8 at `527e77a`; high confidence in structure, medium in impact. |
| Observation and consequence | One numbered step covers implementation, two content reviews, presentation generation, structural and workflow verification, repair, and revision preservation. Its roughly 100 words force the reader to retain a sequence of different gates under one label; a hurried author may lose the distinction between accepted portable content and later OpenAI presentation. |
| Correction and meaning | Separate the stage into compact substeps or a short nested sequence in the same workflow. Preserve the existing order, authority, optionality and evidence ownership; do not split into a tiny new reference. |
| Objective recheck and status | Trace accepted content → presentation → checks/repair from the loaded authoring workflow and verify no new effect for review-only requests. Open editorial recommendation. |

### R-005 — Conditional exemplar has too little design reasoning for its role

| Field | Evidence |
| --- | --- |
| Location and confidence | `agent-package-author/references/hello-world-example.md` lines 3–5, compared with entry row and `docs/dev/SPEC.md` §3; high confidence in the textual gap, medium in user impact. |
| Observation and consequence | The module names components and cautions against a mandatory tree, but gives only a brief reason for profile selection and no concrete mapping from requirement to reference/script/asset/validator. If the source attachment is absent or unavailable after loading, the agent cannot use this file alone to reason through the claimed rich design exemplar. This is insufficiency for its advertised role, not a criticism based on 112 words. |
| Correction and meaning | Add a compact decision/example mapping with a conditional profile, common contract, renderer and independent validator, plus why each belongs at that boundary. Make the illustrative status and nonmandatory scope explicit. Do not turn the exemplar into a required scaffold or silently rely on README/source-only files at runtime. |
| Objective recheck and status | With only the entry and this selected module, justify each illustrative file type and identify when a simpler skill omits it. Open content/composition recommendation. |

### R-006 — Validation review paragraph combines multiple decisions

| Field | Evidence |
| --- | --- |
| Location and confidence | `agent-package-author/references/validation-policy.md` line 12 at `527e77a`; high confidence in the controlling-concern shift, medium in impact. |
| Observation and consequence | One paragraph moves from comprehensive inventory to focused scope, owner selection, finding content, review-only authority, then consumer-trial setup. The module itself has an appropriate shared evidence boundary, but readers cannot readily locate the scope decision versus output and trial conditions. |
| Correction and meaning | Reorganize this paragraph into short purpose-specific units or labeled subparts inside the same module, keeping evidence taxonomy and reporting rules adjacent to their uses. Do not create separate files just because the paragraph is long. |
| Objective recheck and status | A focused review, comprehensive review and selected consumer trial can each locate its scope/evidence/report rule without reading a competing procedure. Open editorial recommendation. |

The eight other modules have no material local composition finding at this depth. This unit did not independently verify normative format rules or run client workflows. Cross-owner agreement and README claims remain for U-003/U-004; these local outcomes do not preaccept revisions.

## U-003 — Cross-module ownership and handoffs

- Exact runtime candidate: `527e77a754ed0dc53ffea99519e26ff490f533ef`; C-005/C-006 source trace across the entry, authoring workflow, design/standards/review modules, portability, validation, MCP and OpenAI presentation. This is not a client activation trial.

| Path / paired owners | Source result |
| --- | --- |
| Authorized creation → content review → validation | Entry selects authoring first; `authoring-workflow.md` permits proportionate repairs and calls the relevant review criteria; `validation-policy.md` owns evidence. Effects and stop agree. |
| Focused/content-only review → findings | Entry excludes authoring workflow and writes; skill/plugin review modules return findings; validation policy distinguishes source inspection from structure and behavior. No conflicting repair instruction found. |
| Bundled sibling handoff | Entry, `plugin-design.md`, `plugin-standard.md` and validation policy agree on named `SKILL.md` handoff versus direct shared reference, plugin-root containment and non-guaranteed client activation. |
| Optional `PLUGIN.md` / coordinator | Plugin design and plugin review treat each as conditional and keep canonical behavior in the actual skill/coordinator owner. No inferred portable discovery. |
| Existing no-skill plugin | Entry and plugin review skip child criteria; plugin standard permits component variants. Creation default remains skill-oriented. |
| Existing MCP assessment | Entry selects MCP guidance when MCP exists; the module's first sentence can instead be read as only authoring a needed MCP component (R-007). |
| Presentation for an authored skill | Entry, authoring workflow, portability policy, plugin design and SPEC require the APA-generated OpenAI presentation after portable content; the presentation module's opening narrows its use to an OpenAI-client request (R-008). |

### R-007 — MCP module's opening narrows the entry route

| Field | Evidence |
| --- | --- |
| Location and confidence | `agent-package-author/SKILL.md` row for MCP (line 26) versus `references/mcp-packaging.md` line 3 at `527e77a`; high source confidence. |
| Observation and consequence | The entry loads MCP packaging when MCP is requested **or exists** in a package under review. “Only when the user needs MCP” in the selected module can be interpreted as requiring a request to add MCP, excluding a review of an existing MCP configuration. Its subsequent rules are relevant to that review. |
| Bounded correction and meaning | Qualify the module opening to include authoring requested/justified MCP and reviewing present MCP, with no implication that a review-only request writes configuration. Keep the rest of the transport contract and evidence limits. |
| Objective recheck and status | From entry plus module, trace both an existing mixed/MCP-only plugin review and a creation request without MCP; load only the former's actual component path. Open route/wording recommendation. |

### R-008 — Presentation module's trigger conflicts with APA's generated-output contract

| Field | Evidence |
| --- | --- |
| Location and confidence | `agent-package-author/SKILL.md` line 31, `references/authoring-workflow.md` step 6, `references/portability-policy.md` line 15, `references/openai-presentation.md` line 3, and `docs/dev/SPEC.md` §5; high source confidence. |
| Observation and consequence | APA's accepted workflow creates OpenAI metadata and SVG for each authored skill after portable content. The presentation module says to use it when creating/revising a skill “for an OpenAI client,” which implies it can be skipped for an otherwise portable skill even though the other owners require generation. The same paragraph correctly says the files are optional *portable-standard* metadata, but that distinction does not resolve APA's own deliverable rule. |
| Bounded correction and meaning | Align the module's activation with APA creation/revision of each skill and the entry's assessment of existing presentation. State separately that these outputs are OpenAI client presentation and not portable format requirements; preserve deliberate replacement/verification gates. A change to APA's mandatory generation policy would instead require an explicit governing decision, not a prose-only fix. |
| Objective recheck and status | From a generic portable standalone request and a plugin with two children, the entry and selected module agree when/how many presentations are generated; a review-only request assesses existing presentation without generating. Open high-priority route consistency finding. |

No separate finding is assigned to plugin-wide composition, sibling links or review-only effects at the inspected source level. U-004 will assess whether README/examples repeat or obscure these interface conditions. The present checks do not establish host loading, transport connectivity or OpenAI rendering.
