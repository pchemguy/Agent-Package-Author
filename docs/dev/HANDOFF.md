# Development handoff

## Checkpoint

Campaign `013_5d0846b-cleanup` is open from the published campaign 012 merge. Its [revision plan](reviews/013_5d0846b-cleanup/REVISION-PLAN.md) and [revision report](reviews/013_5d0846b-cleanup/REVISION-REPORT.md) record the requested deletions and checks. Campaign 012 is closed; the governing contract remains [SPEC.md](SPEC.md), with context in [PLAN.md](PLAN.md).

## Scope and authority

- Workflow: bounded source cleanup revision.
- Decision sources: the user's request to close campaign 012, open cleanup and delete four files and two root `AGENTS.md` sections.
- Completed effects: cleanup opening and A-001 published/read back; A-002 policy deletion and evidence recorded locally, pending publication.
- Current stop: publish/read back A-002, then A-003 combined verification.

## Git and return

- Campaign: `013_5d0846b-cleanup`; directory `docs/dev/reviews/013_5d0846b-cleanup/`.
- Creation parent and return target: `main` at `5d0846b592b516c7f3d79dd48a7e5ea8c544cc7a`.
- Working branch: `revision/013_5d0846b-cleanup`; branch-off commit is the same full baseline. Closed campaigns `001`–`012` remain frozen.
- Published opening tip: `60e9f10115f2c31dc82e7d01947c52fcc5c083a5`.
- Published A-001 source example deletion tip: `b44ee4848460b83cabbb0b996c0860e1409af487`.

## Next action

Publish/read back A-002's policy deletion and agent entry update, then verify the combined cleanup under A-003.
