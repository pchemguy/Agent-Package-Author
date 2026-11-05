# Development handoff

## Checkpoint

Campaign `013_5d0846b-cleanup` is open from the published campaign 012 merge. Its [revision plan](reviews/013_5d0846b-cleanup/REVISION-PLAN.md) records the requested deletions and coupled checks. Campaign 012 is closed; the governing contract remains [SPEC.md](SPEC.md), with context in [PLAN.md](PLAN.md).

## Scope and authority

- Workflow: bounded source cleanup revision.
- Decision sources: the user's request to close campaign 012, open cleanup and delete four files and two root `AGENTS.md` sections.
- Completed effects: campaign 012 merged/published/read back; cleanup branch and plan created locally, pending publication.
- Current stop: publish/read back the opening plan, then execute A-001–A-003 on this branch.

## Git and return

- Campaign: `013_5d0846b-cleanup`; directory `docs/dev/reviews/013_5d0846b-cleanup/`.
- Creation parent and return target: `main` at `5d0846b592b516c7f3d79dd48a7e5ea8c544cc7a`.
- Working branch: `revision/013_5d0846b-cleanup`; branch-off commit is the same full baseline. Closed campaigns `001`–`012` remain frozen.

## Next action

Publish/read back this opening checkpoint, then execute the requested cleanup actions with their dependent references and tests.
