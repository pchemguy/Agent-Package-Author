# Development handoff

## Checkpoint

Campaign `006_efd5838-agent-entry-policies` is open on `revision/006_efd5838-agent-entry-policies` for the requested root agent-entry policies. Its [revision plan](reviews/006_efd5838-agent-entry-policies/REVISION-PLAN.md) records the accepted action. Campaign `005_cb698e2-composition` was merged and published on `main` at `efd58388f93f879a452b4e94d1e4acc5abcc0941`; its [revision report](reviews/005_cb698e2-composition/REVISION-REPORT.md) retains the earlier outcome. The project contract is [SPEC.md](SPEC.md) with delivery context in [PLAN.md](PLAN.md).

## Scope and authority

- Workflow: directly accepted focused revision; opening and V-001 execution on the campaign branch.
- Decision sources: the user's 2026-11-04 requests to open a new campaign and add two attached root policies with an exact AGENTS.md insertion.
- Accepted effects: copy the supplied files at root and insert the requested sections before `## Start here`. Preserve unrelated content and the delivered skill. No broader review or repair is authorized.
- Current stop: publish the opening checkpoint, execute and publish V-001, then leave the campaign branch open. No merge or client trial is selected.

## Git and return

- Campaign: `006_efd5838-agent-entry-policies`.
- Creation parent and eventual return target: `main` at `efd58388f93f879a452b4e94d1e4acc5abcc0941`.
- Working branch: `revision/006_efd5838-agent-entry-policies` at the opening checkpoint; remote publication must be verified before V-001.
- No active parent campaign is suspended; earlier closed campaign records remain frozen.

## Next action

On continuation, verify the opening branch publication and worktree state, then execute V-001 from its plan. Publish and read back the action commit before any other campaign work. Do not infer campaign closure or integration from the completed action.
