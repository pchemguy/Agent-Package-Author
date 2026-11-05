# Critical review revision plan

## Decision and boundary

The user's 2026-11-05 instruction accepts correction of all eight findings in [REVIEW-REPORT.md](REVIEW-REPORT.md), execution, verification and campaign closure. The original review observations remain pinned to `e591021a4ca3ed4dc48b40fc984604bde3f7227d`; rechecks assess the revised source. This plan owns campaign actions, while current [SPEC.md](../../SPEC.md) and [PLAN.md](../../PLAN.md) retain the project contract. No new product requirement or main design document is needed for these bounded corrections.

- Branch: `revision/009_e591021-critical-review`; creation parent and return target: `main` at the pinned baseline.
- Effects: edit only the applicable creator references/scripts, README, example MCP server, tests and this active campaign's records/HANDOFF. Preserve closed campaigns and unrelated files.
- After each action, commit source and observed evidence together, publish/read back before beginning another action. End with coupled regression and explicit verified two-parent integration into `main`.

## Actions and checks

| Action | Findings | Owner and intended result | Objective recheck |
| --- | --- | --- | --- |
| A-001 | R-002 | Skill frontmatter parser and tests: distinguish unquoted YAML numbers and other implicit non-string forms from quoted strings within the documented bounded subset. | Numeric `name`, `description`, metadata fail/unverified; quoted equivalents and examples pass. |
| A-002 | R-003, R-004 | Skill resource scanner and tests: traverse reachable Markdown references from the entry, resolve relative to each containing file, skip fenced/inline examples, retain cycle and plugin-root handling. | Nested missing/escaping links fail; real contained and sibling links pass (sibling warns); illustrative code does not fail. |
| A-003 | R-005 | Example MCP server and its tests: validate JSON-RPC request/params/tool arguments and answer malformed requests with IDs without terminating the stream. | Malformed then valid sequences yield correlated errors and later valid result; positive and missing-file calls pass. |
| A-004 | R-001, R-006, R-007 | Authoring intake and README: classify seed/reference/draft authority and resolve conflicts before acceptance; qualify the offline helper promise and keep test command clean. | Trace conflicting and brief-only inputs through instructions; documented command leaves a disposable copy clean. |
| A-005 | R-008 | Presentation generator, reference and tests: use an icon motif that remains meaningful at small size without a tiny text mark. | Inspect actual 16/32-pixel render if facility available, XML and generated contexts; document any unavailable visual verification. |
| A-006 | All | Final composition and regression verification, report dispositions, handoff and integration. | Full suite, self/example CLIs, targeted negative probes, active links, owned diff and merged-state checks pass; limits stated. |

## Evidence and closure

Record each action's changed paths, actual commands, findings disposition and remaining limits in [REVISION-REPORT.md](REVISION-REPORT.md). A-001–A-005 commits close only their respective bounded action; A-006 records final rechecks. Do not erase review observations. Publish and read back the complete campaign tip before merging. Reconcile HANDOFF on `main`, verify the prospective merge and publish/read back the two-parent merge. No client installation or Windows-native behavior is inferred from local checks.
