# Development handoff

## Checkpoint

Campaign `012_0f43537-package-review` is open with a focused accepted revision to the skill-reference review criteria and placement of non-operative examples. Its [revision plan](reviews/012_0f43537-package-review/REVISION-PLAN.md) and [revision report](reviews/012_0f43537-package-review/REVISION-REPORT.md) record the actions and checks. Campaign 011 was closed on `main`; the governing contract remains [SPEC.md](SPEC.md), with context in [PLAN.md](PLAN.md).

## Scope and authority

- Workflow: focused review-criteria revision on the open package-review campaign branch.
- Decision sources: the user's 2026-11-05 campaign opening, per-reference workflow-component review requirement and follow-up placement rule.
- Completed effects: opening, initial plan, A-001 and A-002 published/read back; A-003 relocation and evidence recorded locally, pending publication.
- Current stop: publish/read back A-003, then A-004 coupled verification.

## Git and return

- Campaign: `012_0f43537-package-review`; directory `docs/dev/reviews/012_0f43537-package-review/`.
- Creation parent and return target: `main` at `0f435371eccf592a7d99af83a1c6f44bae14d1d2`.
- Working branch: `revision/012_0f43537-package-review`; branch-off commit is the same full baseline. Closed campaigns `001`–`011` remain frozen.
- Published opening tip: `4bdc4dfba6e6e96b4f5218a6ca42ca8c04b91e8d`.
- Published initial A-001/A-002 plan tip: `4ee9b0e0d9566fa6239263f6f2f9003fd9a55046`.
- Published A-001 action tip: `5190d83339db7957f9e91de138716562d4de8832`.
- Published A-002 verification tip: `3c5151437001c8dda644030b5db0f67505367894`.

## Next action

Publish/read back A-003's relocated source-only example and reconciled callers, then recheck under A-004. Leave the campaign open.
