# Development handoff

## Checkpoint

Campaign `006_efd5838-agent-entry-policies` is open on `revision/006_efd5838-agent-entry-policies` for the requested root agent-entry policies. Its [revision plan](reviews/006_efd5838-agent-entry-policies/REVISION-PLAN.md) and [revision report](reviews/006_efd5838-agent-entry-policies/REVISION-REPORT.md) record the accepted action and checks. Campaign `005_cb698e2-composition` was merged and published on `main` at `efd58388f93f879a452b4e94d1e4acc5abcc0941`; its [revision report](reviews/005_cb698e2-composition/REVISION-REPORT.md) retains the earlier outcome. The project contract is [SPEC.md](SPEC.md) with delivery context in [PLAN.md](PLAN.md).

## Scope and authority

- Workflow: directly accepted focused revision at finalization and integration handoff.
- Decision sources: the user's 2026-11-04 requests to open a new campaign, add two attached root policies with an exact AGENTS.md insertion, and later close the campaign.
- Accepted effects: copy the supplied files at root and insert the requested sections before `## Start here`. Preserve unrelated content and the delivered skill. No broader review or repair is authorized.
- Current stop: publish the finalization evidence, explicitly merge into `main`, verify and publish the target, then stop. No Windows-host trial is selected.

## Git and return

- Campaign: `006_efd5838-agent-entry-policies`.
- Creation parent and eventual return target: `main` at `efd58388f93f879a452b4e94d1e4acc5abcc0941`.
- Working branch: `revision/006_efd5838-agent-entry-policies`; published opening checkpoint `b280f44487bd493b8b71329cec1da4e720fa4313` and action tip `41931871dc3bdf1ce87d2c299efeb46a9c960cac`. The finalization commit and merge require remote readback.
- No active parent campaign is suspended; earlier closed campaign records remain frozen.

## Next action

On continuation, publish the finalization commit, refresh `main` against origin, inspect and verify the prospective merge, reconcile this handoff to the completed parent context, and publish/read back the two-parent merge. No further source revision is implied.
