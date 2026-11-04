# Development handoff

## Checkpoint

Campaign `007_bf115bc-comprehensive-review` is open at its review-plan checkpoint. Its [review plan](reviews/007_bf115bc-comprehensive-review/REVIEW-PLAN.md) defines U-001–U-006 and the report checkpoints. The current project contract is [SPEC.md](SPEC.md), with implementation context in [PLAN.md](PLAN.md). The preceding campaign is integrated into `main`; its closed records are not current review inputs.

## Scope and authority

- Workflow: comprehensive review, currently at opening/plan stage; the review report has not yet been created.
- Decision source: the user's 2026-11-04 request to open a comprehensive review campaign.
- Authorized work: create and publish this campaign branch, plan and checkpoint; assess the current source and record findings in the active review report. Do not repair source or amend governing documents from review findings alone.
- Current stop: this opening checkpoint. A subsequent review execution follows U-001–U-006, committing, publishing and reading back each unit before the next. Consolidation returns the report and proposed revisions for a separate decision.

## Git and return

- Campaign: `007_bf115bc-comprehensive-review`.
- Creation parent and return/integration target: `main` at `bf115bce52adf2487462db33440ce7702120080a`.
- Working branch: `revision/007_bf115bc-comprehensive-review`; branch-off commit: `bf115bce52adf2487462db33440ce7702120080a`.
- No parent campaign is suspended. Prior closed campaign records remain frozen.

## Next action

Confirm the opening commit and remote branch publication. When review execution is requested, start U-001 at the pinned source, create `REVIEW-REPORT.md`, and preserve unit-by-unit evidence and publication gates. Reconcile any changed `main` baseline explicitly before expanding the review candidate.
