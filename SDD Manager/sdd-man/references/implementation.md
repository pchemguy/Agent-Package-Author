# Transactional Implementation

Use this reference only after the user explicitly authorizes implementation, continuation, or resumption of a bounded task, milestone, phase, or campaign range.

## Contents

- [Operating invariant](#operating-invariant)
- [Campaigns and governing documents](#campaigns-and-governing-documents)
- [Implementation state](#implementation-state)
- [Startup gate](#startup-gate)
- [Select a bounded range](#select-a-bounded-range)
- [Prepare one task](#prepare-one-task)
- [Extend task scope](#extend-task-scope)
- [Implement within the transaction](#implement-within-the-transaction)
- [Verify the task](#verify-the-task)
- [Complete a task](#complete-a-task)
- [Durable Git completion](#durable-git-completion)
- [Durable non-Git completion](#durable-non-git-completion)
- [Close milestones, phases, and campaigns](#close-milestones-phases-and-campaigns)
- [Stop for human steering](#stop-for-human-steering)
- [Journal records](#journal-records)
- [Safety rules](#safety-rules)

## Operating invariant

Execute exactly one PLAN task transaction at a time. A task transaction is the smallest recoverable mutation unit and moves through:

```text
STARTED → PREPARED → COMPLETED → COMMITTED → CLEANED
                   ↘ REVERTED
```

`COMMITTED` applies only when Git-backed completion is required. In a non-Git project, successful verification followed by cleanup makes `COMPLETED` durable.

Do not begin a second task while the first task is nonterminal, while recovery data remains unexplained, or while the requested range is awaiting steering.

Use these default project-root locations unless project instructions define equivalents:

```text
IMPLEMENTATION_LOG.jsonl
.implementation-state/<task-id>/manifest.json
.implementation-state/<task-id>/backup/
```

Keep recovery state project-local. In a Git worktree, exclude `.implementation-state/` locally through `.git/info/exclude` when needed. Do not add a repository-wide ignore rule merely to support the agent protocol unless the user or project requires it.

## Campaigns and governing documents

Classify the implementation campaign before selecting work:

- `initial`: implement a main SPEC and PLAN in a greenfield or comprehensively planned project;
- `change`: implement an explicit `FEATURE-SPEC.md` and `FEATURE-PLAN.md` delta against the main baseline;
- `existing`: continue an already journaled campaign using its recorded document set.

For a change campaign, require both feature documents or neither. Read the main documents for the current system and the feature documents for the intended delta. If a feature document conflicts with the main baseline without explicitly revising it, stop.

When resuming, the latest valid campaign journal record identifies the governing document set. Confirm those documents still exist and have not changed incompatibly. Do not silently switch a campaign from the main PLAN to a feature PLAN or vice versa.

Before each task, discover all project instructions applicable to its declared paths, including nested instruction files. Re-run scoped instruction discovery when scope expands.

## Implementation state

Use journal events and recovery evidence to distinguish:

| State       | Minimum evidence                                            | Permitted next action                           |
| ----------- | ----------------------------------------------------------- | ----------------------------------------------- |
| `STARTED`   | valid `started` event                                       | finish preparation or recover                   |
| `PREPARED`  | valid manifest, verified backups, matching `prepared` event | mutate declared paths                           |
| `COMPLETED` | successful required checks and `completed` event            | create/verify task commit or close non-Git task |
| `COMMITTED` | exact matching task commit                                  | remove recovery data                            |
| `CLEANED`   | no active recovery directory                                | select next authorized task                     |
| `REVERTED`  | baseline restored and `reverted` event                      | restart with a new task identifier              |

The journal is append-only. Never edit an earlier valid record to make current state appear cleaner.

## Startup gate

Run this gate on every implementation invocation, including a request to “continue”:

1. Locate the governed project root and applicable instructions.
2. Detect Git or non-Git operation without changing repository state.
3. Inspect the journal, recovery directories, roadmap, filesystem, and relevant Git history.
4. Classify the latest campaign and task state.
5. If any task is nonterminal or recovery evidence is unexplained, read `recovery.md` and resolve it before task selection.
6. If evidence is ambiguous, stop and preserve it.
7. Only after the state is clean, select work from the governing PLAN and ROADMAP.

Do not interpret a clean Git status as proof that no interrupted non-Git-style preparation exists. Do not interpret an unchecked roadmap item as proof that no implementation exists.

## Select a bounded range

Translate the user's authorization into an exact stopping boundary:

- one named task;
- the next `N` tasks;
- one named or next milestone;
- one named or next phase;
- the remainder of the campaign.

Resolve “next” from the PLAN, confirmed by the ROADMAP, journal, recovery state, and Git when available. If those sources disagree materially, stop rather than choosing whichever source advances fastest.

Interpret “next milestone” or “next phase” as completing the currently incomplete boundary before advancing to a later one. Resolve “through” and “MVP” against explicit named PLAN and ROADMAP boundaries; ask when no unique boundary exists.

Record the requested boundary internally and enforce it after every task. A milestone or phase request authorizes its contained tasks, not later work.

## Prepare one task

### Preflight

Before writing the `started` record:

1. Identify the canonical PLAN task and its phase and milestone.
2. Read only the relevant SPEC, PLAN, LAYOUT, roadmap, verification-map, code, tests, and instructions.
3. Enumerate anticipated path operations as `create`, `modify`, `delete`, or `rename`.
4. For substantive code work, apply `in-code-documentation.md`: resolve the effective convention, inspect affected documentation, and include anticipated documentation paths and checks.
5. Identify focused, dependent, integration, quality, build, and boundary checks required for the task.
6. Generate a unique task identifier containing the PLAN task identity, a semantic slug, a UTC timestamp, and a collision-resistant suffix when needed.
7. In Git, record the branch, `HEAD`, staged state, unstaged state, untracked files, and relevant renames.
8. Refuse to claim or overwrite a dirty target path whose ownership is not established.
9. Preserve unrelated dirty paths and exclude them from backup, mutation, staging, restoration, and commits.

Do not use broad destructive commands, repository-wide cleanup, blanket staging, or unresolved globs to prepare a task.

### Start the transaction

Append a `started` JSON object before creating recovery data. Include at least:

```json
{
  "event": "started",
  "task_id": "3.1-20260920T120000Z-a1b2",
  "campaign_id": "initial-20260920",
  "plan_task": "3.1",
  "phase": "Phase 3",
  "milestone": "Transactional implementation",
  "requested_boundary": "Phase 3",
  "started_at": "2026-09-20T12:00:00Z",
  "git_head": "<hash-or-null>",
  "paths": [{"path": "src/example.py", "operation": "modify"}]
}
```

Use valid one-object-per-line JSON. Include schema or protocol version fields when the project defines them.

### Build the manifest and backups

Create a manifest that records the exact baseline for every declared path:

- normalized project-relative path;
- operation and, for renames, both source and destination;
- whether the path existed;
- path type: regular file, directory, symlink, or absent;
- byte-content hash for regular files;
- symlink target without following it;
- relevant file mode or permission metadata;
- backup location for every existing path requiring restoration;
- preparation timestamp and task identifier;
- Git baseline information when applicable.

Normalize manifest paths with `/` separators. Reject absolute paths, empty or `.` targets, `..` traversal, and path aliases or case collisions that the host filesystem cannot distinguish safely.

Before mutation, detect metadata the ordinary manifest cannot restore portably, including Windows junctions or other reparse points, ACLs, extended attributes, or symlinks that the current host cannot recreate. Use an explicit project-defined preservation mechanism or stop; do not promise exact restoration while silently dropping required metadata.

Back up existing content before mutation. Preserve the directory shape under the task recovery directory. Verify each backup against the recorded hash, symlink target, type, and mode.

For a `create`, record that the target was absent. For a `delete`, back up the target. For a `rename`, record and protect both endpoints, including whether the destination already existed.

Write the manifest atomically when practical. Compute its hash only after it is complete and its backups have been verified.

Append `prepared` with the manifest path and hash before the first project mutation. If preparation fails, do not modify project paths; recover or mark the task reverted after proving the baseline is intact.

## Extend task scope

Do not touch an undeclared path merely because implementation reveals it is convenient.

When a task legitimately requires additional paths:

1. Stop mutation before touching them.
2. Confirm the added work still belongs to the same PLAN task and user-authorized range.
3. Discover instructions and dirty state for the added paths.
4. Append `scope-extension-started` listing the proposed operations.
5. Back up and verify the added baselines.
6. Atomically update the manifest and append a matching prepared scope-extension record with the new manifest hash.
7. Resume only after the expanded transaction is recoverable.

If the added work is a distinct PLAN task, architectural decision, or scope expansion, stop and request direction instead.

If an undeclared path was already modified and its pre-task baseline cannot be proven, preserve all evidence and stop. Do not retroactively claim the current content as its baseline.

## Implement within the transaction

Modify only declared paths. Implement the complete current task contract, including the code, tests, documentation, and project metadata assigned to that task.

For substantive code changes, reconcile module/package documentation and affected symbol documentation through `in-code-documentation.md` after behavior stabilizes and before verification. Passing tests or absent project guidance does not waive this review.

Keep the governing artifacts aligned:

- update the verification map when a component-to-check relationship changes;
- update active change documents when implementation resolves an explicitly delegated detail;
- update the main documents only when the workflow authorizes normalization;
- update ROADMAP completion only during task closure;
- do not rewrite history in the journal.

Temporary build or test outputs are not automatically task paths. Keep disposable outputs out of commits and recovery ownership unless project rules make them authoritative artifacts.

If implementation uncovers a contradiction, missing public contract, or change outside delegated implementation detail, stop at the safest point and preserve the transaction for recovery or user review.

## Verify the task

Before declaring completion:

1. Compare actual touched paths with the current manifest.
2. Stop if any undeclared authoritative path changed.
3. Inspect the focused diff or non-Git equivalent for scope and correctness.
4. For substantive code changes, confirm affected in-code documentation was reconciled or record the concrete reason no change was required.
5. Run the narrowest direct checks first.
6. Run affected dependent checks identified through the verification map and code relationships.
7. Run required integration, documentation, lint, format, type, build, packaging, or boundary checks in the project-defined order.
8. Record each command, result, and relevant environment limitation.

Use `verification.md` to select and interpret checks. A required unavailable check is not a pass. A failing check must be classified as caused by the task, pre-existing, environment-blocked, or unclear, with evidence.

Fix task-caused failures inside the same transaction when the repair belongs to the declared behavior and path scope, then repeat affected checks. Use the scope-extension protocol when the repair needs another path. A pre-existing or unrelated failure that blocks required verification keeps the task incomplete until the blocker is resolved or the user authorizes a separate bounded correction.

Do not weaken assertions, remove meaningful coverage, or relabel a required check as optional merely to close the task.

## Complete a task

After all required task checks pass:

1. Update the matching ROADMAP task checkbox and any mechanically implied milestone or phase summaries.
2. Reconcile the verification map and governing documents affected by the task.
3. In a non-Git project, capture a durable final-state inventory for every declared path and rename endpoint: normalized path, existence, type, regular-file content hash or symlink target, and relevant restorable mode. Store this inventory, or sufficient canonical data to recompute and compare it, in the `completed` record rather than only in temporary recovery data.
4. Append a `completed` record.
5. Follow `reporting.md` for the durable capability summary, boundaries, verification evidence, roadmap coordinates, and human-facing task report.

## Durable Git completion

In a Git-backed project, durable task completion requires one exact task commit. If applicable project instructions prohibit commits, treat that as an authority conflict and stop before implementation rather than silently degrading to non-Git closure.

For Git completion:

1. Stage only the task's declared project paths, required ROADMAP or verification-map updates, and `IMPLEMENTATION_LOG.jsonl`.
2. Never stage `.implementation-state/`.
3. Never use blanket staging when unrelated paths exist.
4. Inspect the staged diff and confirm it contains exactly the completed task.
5. Commit with a clear task message and an exact `Task: <task-id>` trailer.
6. Verify that the commit exists at the expected `HEAD`, contains the exact staged paths, and carries the trailer.
7. Append a `committed` record if the journal protocol requires post-commit recording; when that record itself must be durable, use the project-defined follow-up mechanism without amending the task commit silently.
8. Remove the task recovery directory only after the durable commit is verified.
9. Confirm no declared task path remains modified or staged, no task-owned recovery data remains, and unrelated worktree state is unchanged.

Do not amend, rebase, squash, push, publish, or change branches unless the user explicitly authorizes that operation or governing project instructions unambiguously require it.

## Durable non-Git completion

For a non-Git project:

1. Reconfirm every declared output against the final-state inventory recorded by `completed`.
2. Confirm all required checks passed and the `completed` record is durable.
3. Confirm ROADMAP and verification-map changes are written.
4. Remove the task recovery directory.
5. Reinspect the journal and filesystem to confirm the task is terminal and clean.

The absence of a commit does not relax backup, verification, journal, or cleanup requirements.

## Close milestones, phases, and campaigns

At the end of a requested milestone or phase:

1. Confirm all constituent tasks are durably complete.
2. Run boundary-level verification defined by the PLAN and verification strategy.
3. Reconcile ROADMAP rollups with task evidence.
4. Prepare the applicable boundary summary for the completion and checkpoint journal records.
5. Produce the appropriate synthesized completion report through `reporting.md`.

At change-campaign completion, also run final affected-scope acceptance checks; integrate settled requirements into the main SPEC; express the final from-scratch construction in the main PLAN; update LAYOUT, ROADMAP, and the verification map; remove superseded baseline material; remove temporary feature documents; and record durable campaign completion. Preserve append-only journal and Git history even after the current-state documents are normalized.

## Stop for human steering

After the requested range is durably complete, establish the checkpoint through `checkpoint-steering.md` and report the boundary through `reporting.md`. Do not treat status, review, or acceptance alone as authorization to continue.

## Journal records

Use append-only JSONL. Every record should identify the protocol version, campaign, task when applicable, UTC timestamp, and event-specific evidence.

Support at least these events:

- `campaign`;
- `started`;
- `prepared`;
- `scope-extension-started`;
- `scope-extension-prepared`;
- `completed`;
- `committed` when used by the project protocol;
- `reverted`;
- `checkpoint`;
- `steering-started`;
- `steering-completed`.

Never append `completed` before verification passes. Never append `reverted` until baseline restoration is verified. Checkpoint and steering events do not replace the ordinary transaction events required for revision tasks.

## Safety rules

- Never operate on the filesystem root, home directory, workspace root, or unresolved broad path as a task target.
- Never overwrite a backup or manifest whose ownership is uncertain.
- Never follow symlinks while backing up or restoring unless the manifest explicitly requires the resolved target as a separate path.
- Never treat a junction, reparse point, ACL, extended attribute, or unsupported symlink as exactly recoverable without an explicit preservation mechanism.
- Never delete unknown recovery data.
- Never restore unrelated user changes.
- Never continue after missing backups, mismatched hashes, multiple active tasks, corrupt journal history, or uncertain ownership.
- Prefer stopping with complete evidence over guessing how to finish or undo a task.
