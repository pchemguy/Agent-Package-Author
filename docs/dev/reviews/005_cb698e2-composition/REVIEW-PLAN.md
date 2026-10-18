# Composition review plan

## Campaign and scope

- Campaign: `005_cb698e2-composition`.
- Starting and reviewed baseline: `cb698e2c0d541a730a3070933778a66f6404a7fc` on `main`.
- Creation parent and integration target: `main`; working branch: `revision/005_cb698e2-composition`.
- Objective: assess the composition of Agent Package Author's current instructions and user documentation before deciding on bounded revisions.
- Included source: `agent-package-author/SKILL.md`, the twelve current `references/*.md`, `README.md`, `AGENTS.md`, and current `docs/dev/SPEC.md`/`PLAN.md` as governing context. Inspect scripts, examples, metadata or assets only where a textual claim or handoff depends on them.
- Exclusions: closed campaign records and historical proposal inputs; independent standards/fact checking; functional validator or packaging redesign; automatic prose or contract changes. The review can identify a substantive conflict but must not smooth it into a silent editorial repair.
- Evidence mode: source inspection and bounded local checks, with structural and observed behavior reported separately. No target-client consumer trial is presumed.
- Companion report: [REVIEW-REPORT.md](REVIEW-REPORT.md). U-000 is assessed; R-001 and R-002 are accepted for bounded V-001 in [REVISION-PLAN.md](REVISION-PLAN.md). U-001–U-005 remain pending.

## Review order and criteria

| Unit | Scope and dependency | Criteria | Representative source scenarios and checks |
| --- | --- | --- | --- |
| U-000 | User-selected focused balance review before the general units: `skill-design.md`, `plugin-design.md`, `skill-review.md`, `plugin-review.md`; inspect the entry, authoring workflow and current SPEC only for the associated route/contract. | C-000: reference modules are bounded by meaningful responsibility and loading trigger. Check both unnecessary fragmentation (thin/vague modules) and overloading (separable substantial subworkflows), keeping shallow entry routing and cohesive procedural depth. Size is evidence to interpret, never a numerical threshold. | Compare a short but complete purpose-specific module, a thin fragment without an independent decision, and a broad module with an independently invoked substantial subworkflow. Locate how both creation and content review would decide, without proposing splits merely to reduce length. |
| U-001 | Entry and activation: creator `SKILL.md`, description, direct reference map; begin from the entry alone. | C-001: purpose, operation, package scope and stop are available before loading detail. C-002: routing rows identify distinct owner, condition and boundary without forcing unrelated modules. | Focused entry question; comprehensive skill and plugin review; authorized authoring; structural-only inspection; no-skill plugin. Trace the next owner and permitted effect from entry text. |
| U-002 | Individual reference composition after U-001: each of twelve modules, assessed in its own role. | C-003: sentences and paragraphs carry one coherent concern, prerequisites precede dependent steps, headings describe contents, and examples support the point. C-004: each module is complete for its selected reading boundary without duplicating a full neighboring procedure. | Inspect procedure versus format guide versus example; selective MCP and OpenAI presentation branches; assess reference use without imposing a word quota or one universal template. |
| U-003 | Cross-module composition after U-001 and U-002: authoring, skill/plugin design and review, validation, standards and optional components. | C-005: canonical ownership, transitions, terminology and handoffs are consistent; necessary reminders remain, competing full procedures do not. C-006: qualifiers and evidence limits stay close to their claims. | Trace a creation-to-verification path, focused and comprehensive assessment paths, sibling handoff, optional coordinator/`PLUGIN.md`, and review-to-authorized-revision transition on both sides. |
| U-004 | User and developer documentation after U-003: README, AGENTS and applicable SPEC/PLAN context. | C-007: opening, hierarchy, examples, reference map and closure serve their intended reader; source and illustrative behavior are distinguished. C-008: current governing statements remain intelligible and consistent with the runtime entry without importing campaign history. | Follow standalone and plugin walkthroughs from seed/reference/draft material; compare the worked review example and all twelve reference rows to the actual entry. Check current local links and Markdown structure. |
| U-005 | Consolidation after all units. | C-009: located findings name reader consequence, confidence, proposed owner, meaning implications and objective recheck; no-finding coverage and unassessed items remain explicit. | Prioritize a bounded revision queue and assess whether a structural rearrangement requires a human substantive decision or governing-document amendment. |

## Evidence and persistence

Use a lightweight reverse outline at paragraph/section/document levels and inspect representative sentences where density or references impede use. A long module is not a defect by itself; a short module can still be incomplete. Distinguish composition symptoms from absent premises, disputed requirements, or format behavior. Report each finding at its current baseline location with stable `R-###` ID, reader impact, correction boundary and checkable recheck. Record what was read, which local commands ran, what was not assessed, and any no-finding coverage.

After each planned unit, update and commit `REVIEW-REPORT.md`; push that commit and verify remote containment before starting the next unit. The report checkpoint closes the assessment. Revision planning, source edits, integration and merge require a subsequent accepted scope; opening this campaign does not preaccept proposed fixes.

## Current stopping boundary

The U-000 report was published at `8d18fbb`. The user's later 2026-10-18 request accepts V-001; publish its plan and action checkpoints, then stop before U-001. The remaining units retain their planned dependency order.
