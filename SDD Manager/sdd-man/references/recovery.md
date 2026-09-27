# Startup Recovery

Use this reference at the start of every implementation invocation and whenever a task may have been interrupted. Recovery precedes selection of new work.

## Contents

- [Recovery invariant](#recovery-invariant)
- [Inspect before acting](#inspect-before-acting)
- [Decision table](#decision-table)
- [No active task](#no-active-task)
- [Started without preparation](#started-without-preparation)
- [Prepared but incomplete](#prepared-but-incomplete)
- [Completed in a Git project](#completed-in-a-git-project)
- [Completed in a non-Git project](#completed-in-a-non-git-project)
- [Committed but not cleaned](#committed-but-not-cleaned)
- [Unexpected recovery data](#unexpected-recovery-data)
- [Journal damage](#journal-damage)
- [Escalation conditions](#escalation-conditions)
- [Recovery reporting](#recovery-reporting)
- [Safety rules](#safety-rules)

## Recovery invariant

Resolve the latest nonterminal transaction before selecting or starting another task. Prefer exact restoration to the verified prepared baseline when safe continuation cannot be proven.

Recovery must be all-or-nothing for the task-owned path set. Do not restore a convenient subset and then continue as though the original transaction remained valid.

Preserve evidence until the outcome is verified. A recovery directory is not disposable merely because its timestamp is old.

## Inspect before acting

Perform read-only inspection first:

1. Locate the governed project root, project instructions, journal, and recovery root.
2. Parse complete journal records in order.
3. Identify the latest campaign and every task without a proven terminal state.
4. Inventory recovery directories without deleting or rewriting them.
5. Read each candidate manifest and verify its task identifier and recorded hash against the journal.
6. Compare declared paths, backups, current filesystem state, ROADMAP state, verification-map state, and Git state when available.
7. Search Git history for the exact `Task: <task-id>` trailer when a completed task may have been committed.
8. Classify the state using the decision table.

Do not run mutating project tools, auto-formatters, dependency installers, cleanup commands, or tests that rewrite fixtures during initial inspection.

## Decision table

| Evidence                                                  | Classification              | Default action                                                                       |
| --------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------ |
| No nonterminal journal task; no unexplained recovery data | clean                       | Permit bounded task selection                                                        |
| `started`, no `prepared`, no project mutation             | started-not-prepared        | Remove incomplete recovery preparation, append `reverted`, restart with a new ID     |
| `prepared`, no `completed`                                | prepared-incomplete         | Restore the full declared baseline, verify, append `reverted`, restart with a new ID |
| `completed`, no matching Git commit                       | completed-uncommitted       | Validate scope and checks, then commit exactly that task or restore and restart      |
| `completed`, exact matching Git commit, recovery remains  | committed-not-cleaned       | Validate commit and remove matching recovery data                                    |
| `completed` in non-Git, recovery remains                  | completed-not-cleaned       | Reverify final state and remove recovery data                                        |
| Matching commit exists but journal lacks `completed`      | inconsistent                | Preserve evidence and ask; do not synthesize completion silently                     |
| Recovery directory without attributable journal state     | unknown ownership           | Preserve and escalate                                                                |
| Missing/corrupt manifest or required backup               | unrecoverable automatically | Preserve and escalate                                                                |
| More than one apparently active task                      | ambiguous                   | Preserve and escalate                                                                |

Roadmap state is corroborating evidence, not a substitute for the transaction record.

## No active task

When the latest task is terminal and no unexplained recovery data exists:

1. Confirm any required Git task commit exists.
2. Confirm task recovery directories are absent.
3. Confirm ROADMAP state agrees with durable task history.
4. Classify the project as `between-tasks`, `awaiting-steering`, `phase-complete`, or `campaign-complete` as supported.

Treat a valid `reverted` event as terminal only after its restoration evidence checks out and its recovery directory is absent. If the same PLAN task remains authorized, restart it with a new task identifier; never reopen the reverted transaction.

Do not start work during recovery itself. Return control to the implementation selection gate.

## Started without preparation

For `started` without a matching valid `prepared` event:

1. Confirm no declared project path was mutated after the recorded baseline point.
2. Confirm no other evidence indicates preparation completed but the journal append was interrupted.
3. Inspect any partial manifest or backup data without trusting it.
4. If project paths are unchanged, remove only the clearly task-owned incomplete recovery directory.
5. Append `reverted` with reason `preparation-incomplete-no-project-mutation` and the inspection evidence.
6. Restart the PLAN task with a new task identifier if it remains in the authorized range.

If any declared path changed or the timing cannot be established, do not treat the task as unprepared. Preserve the evidence and escalate.

## Prepared but incomplete

For a valid `prepared` event without `completed`:

### Validate recovery material

Before restoration:

1. Verify the manifest hash recorded by the journal.
2. Verify every backup's content hash, type, symlink target, and relevant mode.
3. Confirm every current task-owned path maps to one declared operation.
4. Confirm no unrelated path is included.
5. Confirm rename endpoints are both represented.
6. Confirm path normalization has no absolute path, traversal, host-equivalent alias, or case collision.
7. Confirm the host can restore every recorded path type and required metadata; otherwise preserve evidence and escalate.

If validation fails, stop. Do not perform a best-effort partial restore.

### Restore exact baseline

Restore according to the manifest:

- `modify`: replace current task-owned content with the verified backup;
- `create`: remove the created path only when the manifest proves it was absent and ownership is unambiguous;
- `delete`: recreate the original from the verified backup;
- `rename`: restore both source and destination to their recorded baseline states;
- symlink: restore the link itself, not the target;
- mode change: restore the recorded mode after content and type restoration.

Avoid overwriting newly introduced content unless the manifest and journal prove the active task owns it. If another actor may have modified a task path after interruption, escalate rather than erasing it.

### Verify restoration

After restoration:

1. Recompute hashes and compare all restored regular files with the manifest.
2. Verify absent paths, directory types, symlink targets, and modes.
3. In Git, compare relevant paths with the recorded task-start `HEAD` and preserved pre-existing dirty state.
4. Confirm unrelated dirty paths are unchanged.
5. Remove the recovery directory after restoration is verified.
6. Append `reverted` with reason `interrupted-before-completion` and the restoration evidence.

Restart with a new task identifier. Do not reuse the interrupted transaction identifier.

Do not continue partially implemented code in place unless the user explicitly authorizes an evidence-backed exceptional path after being told why normal restoration is impossible or undesirable.

## Completed in a Git project

For `completed` when Git-backed task commits are required:

### Matching task commit exists

Search for an exact `Task: <task-id>` trailer. If found:

1. Confirm the commit descends from the recorded task baseline as expected.
2. Confirm it contains only the task-owned paths and required journal/roadmap artifacts.
3. Confirm its content matches the completed state and its verification evidence is credible.
4. Preserve unrelated worktree changes.
5. Append or reconcile the `committed` evidence according to project protocol.
6. Remove only the matching recovery directory.
7. Classify the task as durable and clean.

A similar commit message without the exact trailer is not sufficient proof.

### No matching task commit

When no matching commit exists:

1. Validate the manifest and current task diff.
2. Confirm no undeclared path is needed and no unrelated change is staged.
3. Re-run required task verification when safe and available.
4. If final state and checks match the `completed` record, stage exactly the declared task paths plus required roadmap and journal artifacts.
5. Commit with the exact task trailer, verify the commit, and then clean recovery state.

If verification fails, scope is no longer exact, or current files cannot be attributed confidently, preserve evidence. Either restore the full prepared baseline and restart or ask the user which recovery path to take.

If a task commit exists but the journal has no valid `completed` event, stop. Do not append a fabricated completion record based only on Git history.

## Completed in a non-Git project

For a non-Git completed task with recovery data remaining:

1. Validate the manifest and completed journal record.
2. Recompute and compare every declared output with the completed record's durable final-state inventory.
3. Re-run required checks when safe and available.
4. Confirm ROADMAP and verification-map state agree.
5. Remove the matching recovery directory only after final state is verified.

If current state differs from the completion record, do not guess whether completion or later edits should win. Preserve evidence and ask, or restore the prepared baseline when ownership and user intent make that unambiguously correct.

## Committed but not cleaned

When a valid exact task commit exists and only recovery cleanup was interrupted:

1. Revalidate the commit trailer, parent relationship, path set, and expected content.
2. Confirm the recovery directory belongs only to that task.
3. Confirm no later active transaction references its backups.
4. Remove that recovery directory.
5. Reinspect the journal, Git state, and recovery root.

Do not rerun implementation or create a duplicate commit.

## Unexpected recovery data

For recovery directories not explained by valid journal events:

- inventory their manifests and backup paths read-only;
- compare identifiers and timestamps with journal and Git evidence;
- do not merge them into the latest transaction;
- do not delete them as stale;
- report the ownership uncertainty and request direction.

For a journal task whose recovery directory is missing, do not create replacement backups from current files and call them the baseline. Current files cannot prove their own prior state.

## Journal damage

Treat JSONL as append-only evidence.

A clearly truncated final line may be isolated when all preceding lines parse, the incomplete bytes are preserved, and journal plus recovery evidence establish one unambiguous state. Do not rewrite the file during read-only diagnosis.

Escalate when:

- corruption occurs before the final line;
- records are out of causal order;
- task identifiers collide;
- a manifest hash disagrees;
- an event contradicts filesystem or Git evidence;
- removing the final fragment would change ownership or completion conclusions.

Do not silently repair journal history. Any authorized repair should preserve the original bytes and record what was normalized.

## Escalation conditions

Stop automatic recovery when any of these hold:

- multiple tasks appear active;
- the active campaign or governing documents are unclear;
- a required backup or manifest is missing or corrupt;
- target ownership is uncertain;
- undeclared paths were modified;
- pre-existing dirty state cannot be reconstructed;
- a task path may contain later human changes;
- journal, ROADMAP, verification map, manifest, filesystem, and Git evidence conflict materially;
- a required verification command is unavailable and completion depends on it;
- a destructive action would rely on an unresolved variable, wildcard, symlink target, or broad directory.
- exact restoration requires unsupported junction, reparse-point, ACL, extended-attribute, symlink, or other host filesystem semantics.

Report the exact evidence, safe options, and smallest decision needed from the user.

## Recovery reporting

After successful recovery, report:

- the task and detected interruption state;
- whether the task was restored, durably completed, or merely cleaned;
- paths restored or finalized;
- verification performed;
- whether recovery state is now clean;
- whether the same PLAN task will restart with a new identifier;
- the current authorized stopping boundary.

When recovery completes a task, include the implemented feature summary required of all task completion reports. When it reverts a task, state that no implementation completion is being claimed.

## Safety rules

- Never delete a recovery directory before its evidence has been validated, restoration or completion has been verified, and its terminal outcome is unambiguous.
- Never use broad reset, clean, checkout, restore, or recursive deletion commands to recover a scoped task.
- Never overwrite unrelated changes or untracked files.
- Never manufacture a baseline from current content.
- Never mark a task complete merely because tests pass after an interruption.
- Never mark a task reverted until exact restoration is verified.
- Never proceed to new work while recovery remains ambiguous.
