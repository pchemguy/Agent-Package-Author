# Integrate content review into Agent Package Author

- Campaign: `004_920a72e-review-modules`
- Starting baseline: `920a72ecbfe70cf5733cbf45da1fa0f995585824`
- Campaign branch: `revision/004_920a72e-review-modules`
- Integration target: `main`
- Source: [critical review](REVIEW-REPORT.md) of the [supplied proposal](inputs/PROPOSED-REVISIONS.md), [skill module](inputs/skill-review.md) and [plugin module](inputs/plugin-review.md).

## Decisions and scope

Accept R-001, R-002, R-005 and R-006 as integration requirements. Accept R-003 with `PLUGIN.md` as an optional, explicitly loaded convention. Accept R-004 for reviewing existing no-skill plugins; APA's creation default remains skill-oriented, so this campaign does not promise MCP-only plugin authoring. R-007 remains an evidence gap: the absent SDD contract/drafts are not needed to adapt the supplied criteria on their own merits. Retain every finding ID in the review report.

The result shall support focused and comprehensive **content** reviews of standalone skills and plugins, alongside existing creation, revision, structural validation and inspection. A review-only request returns findings without edits. During authorized authoring or revision, a proportionate content check can feed permitted repairs. Comprehensive review accounts for its requested package inventory, including exclusions and unassessed parts; representative scenarios add evidence but do not replace content coverage. Structural checks retain their own scope; no prose-quality rule enters the Python validators.

## Ordered actions

| Action | Owner and intended result | Acceptance and evidence |
| --- | --- | --- |
| V-01 | Amend existing `docs/dev/SPEC.md` and relevant `docs/dev/PLAN.md` strategy/map through scoped `design-docs/004_920a72e-review-modules`. Capture review operation, 12 direct references, no-skill review boundary, evidence tiers and unchanged authoring default. Complete owner QC, push, explicitly merge/publish preparation into `main`, then incorporate that baseline into the campaign branch. | Governing docs agree with the accepted findings before runtime edits; no new document checkpoint is created. Record preparation parents and checks in the campaign report. |
| V-02 | Adapt supplied modules into `agent-package-author/references/skill-review.md` and `plugin-review.md`. Preserve actionable entry/reference and composition/coordinator criteria. Remove duplicated general process/format exposition owned elsewhere, qualify `PLUGIN.md`, and retain bounded/full review contrast and evidence rules. | Compare each proposed section with the retained owner, check source fidelity and direct applicability to simple, composite, mixed and no-skill packages. No SDD-specific contract enters the shipped skill. |
| V-03 | Refactor `SKILL.md` to select operation before package type and give a complete, concise, linked reference map. Align `skill-design.md`, `plugin-design.md`, `validation-policy.md` and `authoring-workflow.md`; update OpenAI presentation text only if it becomes stale. | Entry-only selection handles focused review, comprehensive review, authoring and structural inspection without wrong effects; every shipped reference is directly linked with condition and boundary. Existing portable format and cross-skill containment behavior remain intact. |
| V-04 | Update README capability/usage and a worked review example. Add meaningful integration checks for reference inventory/link resolution, creator validation and example behavior; use source-based scenario review for routing. | Do not assert behavioral acceptance from prose tests or structural checks. Run full suite, creator self-validator/inspector, both plugin examples, link checks and diff check. Record any unavailable independent consumer trial. |
| V-05 | Recheck findings and the full candidate diff, publish evidence in `REVISION-REPORT.md`, explicitly merge verified campaign into refreshed `main`, verify merged state and push/read back. | No previous closed campaign record changes, two-parent merge, verified remote target. |

## Boundaries

The imported files under `inputs/` remain historical proposal material. The delivered modules are adaptations, not verbatim copies. The review policy is APA authoring guidance, not a new Agent Skills or Agent Plugins format rule. A `PLUGIN.md` or coordinator is never mandatory. A no-skill package does not inherit skill-review requirements. Host discovery, client runtime invocation and independent consumer behavior need separate evidence and are not promised by local structural checks.
