# Comprehensive review plan

## Campaign and scope

- Campaign: `007_bf115bc-comprehensive-review`.
- Starting baseline and exact source candidate: `bf115bce52adf2487462db33440ce7702120080a` on `main`. Record any later reviewed or tested commit separately.
- Creation parent and integration target: `main`; working branch: `revision/007_bf115bc-comprehensive-review`.
- Objective: assess the current Agent Package Author deliverable and its user/developer interfaces for correctness, completeness, usability, portability claims, and consistency with the project contract.
- Included: `agent-package-author/` entry, twelve references, scripts, assets and presentation; `README.md`, `AGENTS.md`, root policies, current `docs/dev/SPEC.md` and `PLAN.md`; maintained examples, tests, fixtures, package links and declared checks. Inspect repository and distribution boundaries where they affect delivery.
- Excluded: changes to the reviewed source, automatic repairs, installation or target-client behavior without an actual trial, and routine validation or editing of closed campaign records. Historical records may be consulted only for a specific provenance question.
- Evidence mode: source and consumer-path inspection, independent structural checks, local executable tests and representative workflow trials where feasible. Separate each evidence class and record unavailable external/client checks.
- Companion report: [REVIEW-REPORT.md](REVIEW-REPORT.md). State: U-001–U-006 assessed and consolidated; revision decisions remain pending.

## Review order and criteria

| Unit | Scope and dependencies | Criteria | Representative positive and negative scenarios / evidence |
| --- | --- | --- | --- |
| U-001 | Package inventory, current contract and published format baselines; establish exact tracked paths, links and dependencies before dependent assessments. | C-001: delivered and development material have clear boundaries; standards claims are correctly sourced and versioned; no required input depends on a former checkout or undeclared host path. | Inventory tracked files, symlinks, imports, paths, links and packaging; compare format assertions with primary specifications. Test valid sibling links versus missing targets and escapes. |
| U-002 | Creator entry and all twelve reference modules after U-001; follow standalone skill and plugin branches at the requested depth. | C-002: operation-first routing, reference loading and handoffs are actionable; each reference has a meaningful, cohesive boundary; content review and authoring stop at their proper effects. C-003: skill/plugin design and review cover actual package shapes and distinguish optional components. | Trace standalone create/revise, focused/comprehensive review, structural-only inspection, plugin without skills, bundled sibling handoff, MCP and presentation branches. Check positive and absent/ambiguous routes with located source evidence. |
| U-003 | Script implementation, validation policy and tests after U-001; inspect producers and validators independently. | C-004: diagnostics, containment, format checks and error handling match documented contracts; test assertions cover consequential success and failure paths without overclaiming behavior. | Run the declared suite and CLI checks; probe valid/invalid skill and plugin fixtures, path/symlink boundaries, unknown fields, MCP variants and presentation replacement/context errors. Record exact commands, exit states and limits. |
| U-004 | Shipped example packages, templates and realistic consumer paths after U-002/U-003. | C-005: examples are runnable and illustrate the advertised distinct workflows; templates are useful starting material and do not silently impose optional files or extensions. | Validate and exercise standalone, multi-skill and MCP examples where local facilities permit; inspect generated presentation in a temporary target; include an invalid or unsupported case. Do not equate local execution with client discovery. |
| U-005 | README, root agent entry/policies, current SPEC/PLAN and cross-surface integration after U-002–U-004. | C-006: the complete sample workflow, seed/reference/draft usage and each reference-module role match actual behavior; installation, evidence and portability limits are accurately described. C-007: current links, terminology and developer handoff are coherent. | Walk the README as a user from brainstorming to package review and verification; follow every reference-row invocation; check root policy paths and current Markdown links. Use observed results from preceding units to test claims. |
| U-006 | Consolidation after U-001–U-005. | C-008: coverage, findings, no-finding areas, priorities, dependencies and uncertainties are explicit; proposed rechecks are objective and bounded. | Reconcile all twelve references and other included paths against the inventory, trace findings to owners and acceptance criteria, and distinguish verified defects from recommendations and evidence gaps. |

## Evidence and persistence

Create `REVIEW-REPORT.md` when U-001 begins. For each unit, record the exact source state, locations, assessment depth, observed commands/results, no-finding coverage, unknowns and exclusions. Give each finding a stable `R-###` ID, type, priority, confidence, reader or runtime consequence, proposed owner, correction boundary and objective recheck. A planned check is not a passing check. Report material disagreements between the project contract and published standards without silently revising the contract.

After each unit, update and commit the report, then publish and read back that commit before beginning the next unit. Check the full diff for unintended changes to closed campaigns. The review report is the assessment checkpoint; any revision plan or source edit needs a subsequent accepted scope.

## Consolidation and stopping

Return the completed report and prioritized revision queue after U-006. Stop before source repair, project-document amendments or campaign integration unless the user authorizes those effects. The report records which scenarios ran and their limits; this plan alone is not evidence of execution.
