# Critical review plan

## Scope and boundary

- Campaign: `009_e591021-critical-review`; branch `revision/009_e591021-critical-review`; creation parent and eventual return target `main`.
- Starting and pinned reviewed source: `e591021a4ca3ed4dc48b40fc984604bde3f7227d`. Review commits may change this campaign's records but not the source under assessment.
- Objective: challenge Agent Package Author's format claims, resource safety, failure behavior, content routing, and user-facing evidence with adversarial and realistic cases. Give defects priority over stylistic suggestions; preserve no-finding coverage.
- Included: current `agent-package-author/` entry, all twelve references, scripts, templates and OpenAI presentation; maintained examples/tests/fixtures, README, root agent policies, current SPEC/PLAN and their consequential handoffs. Check the delivered package for dependencies on former checkouts and undeclared facilities.
- Excluded: repairs, generated output inside the repository, installation/activation claims without a target-client trial, and routine validation or edits of closed campaign packages. Historical findings may suggest probes but are not evidence; independently reproduce each current observation.
- Stop: publish the completed review report and return findings plus a revision queue. Do not plan fixes, change reviewed source or integrate into `main` without a later decision.

## Ordered units

| Unit | Critical question and dependency | Positive and negative evidence |
| --- | --- | --- |
| U-001 | Is the pinned package inventory and normative format contract sound? Establish source/format baseline before other units. | Enumerate current files, dependencies and links; compare current skill/plugin rules to primary specifications; probe valid contained and invalid escaping/missing paths. |
| U-002 | Does the entry and each reference lead to the promised authoring/review behavior with cohesive boundaries? After U-001. | Trace standalone/plugin, no-skill plugin, sibling handoff, optional MCP/presentation, and focused versus comprehensive review. Read all twelve modules; test ambiguous, missing and conflicting input branches against actual instructions. |
| U-003 | Do validators and generation scripts reject malformed input safely and report honest evidence? After U-001. | Inspect all helper and test paths; run suite and CLIs; use disposable adversarial fixtures for YAML types, nested links, symlinks, manifests, MCP variants, presentation context and replacement. Verify diagnostics, status and lack of unintended writes. |
| U-004 | Do examples and documentation survive a consumer walk-through? After U-002/U-003. | Run shipped standalone and plugin workflows, malformed then valid MCP requests, presentation output and small-size icon rendering; follow README attachments/commands, root policies and active links. Separate local execution from client behavior. |
| U-005 | Are findings, coverage and priorities defensible? After U-001–U-004. | Reconcile each included surface, concrete rechecks and no-finding areas; classify confirmed defect, design concern and untested behavior; check coupled interfaces for regressions. |

## Evidence and persistence

Create `REVIEW-REPORT.md` with U-001. For every unit record exact source, assessed paths/depth, commands and outputs, positive and negative cases, exclusions and unknowns. Each finding needs a stable `R-###`, located evidence, reader/runtime consequence, priority, confidence, bounded owner/correction and objective recheck. A planned probe is not a result. Commit each assessed unit's report and publish/read back before the next unit. Keep this campaign's records on its branch, inspect every diff for unrelated or closed-record changes, and refresh HANDOFF at final review checkpoint. The eventual integration decision is separate.
