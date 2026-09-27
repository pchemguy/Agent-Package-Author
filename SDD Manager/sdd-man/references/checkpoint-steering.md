# Checkpoint Steering and Normalization

Use this reference after a requested implementation range reaches a durable boundary or when the user asks to revise completed work before forward implementation continues.

## Contents

- [Checkpoint invariant](#checkpoint-invariant)
- [Establish a checkpoint](#establish-a-checkpoint)
- [Await explicit direction](#await-explicit-direction)
- [Classify steering](#classify-steering)
- [Inspect revision impact](#inspect-revision-impact)
- [Choose focused revision or redesign](#choose-focused-revision-or-redesign)
- [Execute a focused revision](#execute-a-focused-revision)
- [Remove a rejected capability](#remove-a-rejected-capability)
- [Normalize authoritative state](#normalize-authoritative-state)
- [Revise future work only](#revise-future-work-only)
- [Handle broader redesign](#handle-broader-redesign)
- [Respect released behavior](#respect-released-behavior)
- [Journal steering](#journal-steering)
- [Return to a paused checkpoint](#return-to-a-paused-checkpoint)

## Checkpoint invariant

A checkpoint is a clean human decision boundary, not permission to continue. While the project is `awaiting-steering`, do not select or start another PLAN task until the user explicitly authorizes a new bounded range.

Steering revises current intent through new recoverable work. Never reopen, rewrite, delete, or pretend earlier task transactions did not occur.

After accepted steering, make authoritative project state describe the direct final design rather than the historical route used to reach it. Preserve history only where history is authoritative: the append-only journal, Git history, released compatibility records, and explicitly historical documentation.

## Establish a checkpoint

After the user-requested implementation range:

1. Confirm every included task is durably complete.
2. Run required task and crossed milestone, phase, or campaign verification.
3. Confirm no active or unexplained recovery state remains.
4. Reconcile PLAN, ROADMAP, journal, filesystem, verification map, and Git evidence.
5. Produce the applicable reports through `reporting.md`.
6. Identify the exact next incomplete PLAN boundary without starting it.
7. Append a `checkpoint` event that records the completed boundary, progress coordinates, verification outcome, recovery cleanliness, and next boundary.
8. Make that record durable through the project journal convention. In a Git project, use a narrow metadata-only checkpoint commit when necessary; do not amend the completed task commit or include unrelated paths.
9. Enter `awaiting-steering`.

Do not establish a clean checkpoint when required verification is unavailable, a task is only prepared or completed-but-uncommitted, recovery data is unexplained, or progress evidence conflicts.

## Await explicit direction

At a checkpoint the user may:

- accept the completed range and stop;
- explicitly continue through a named or relative bounded range;
- request a focused revision of completed behavior;
- revise future tasks without changing completed implementation;
- reopen exploration, specification, planning, or architectural design;
- stop or abandon the campaign.

Acceptance alone does not imply continuation. Status questions, review comments, and approval of the report do not release the checkpoint unless they also authorize a specific next range.

For an explicit continuation request, append or update checkpoint release evidence according to the journal convention, resolve the new range through `roadmap.md`, run startup recovery, and return to normal implementation.

## Classify steering

Classify the requested change before mutation:

| Classification                  | Meaning                                                                                                               | Normal route                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Contract-neutral simplification | Internal capability or complexity is removed or changed without altering required observable behavior                 | Focused revision when impact remains bounded                                 |
| Contract revision               | Supported behavior, public interface, configuration, errors, dependency promise, or persistent representation changes | Change overlay or focused document-and-code revision                         |
| Architectural revision          | Component boundaries, dependency direction, major data flow, or system structure changes                              | Return to exploration/design before implementation                           |
| Defect correction               | Implementation violates an already adequate current SPEC                                                              | Focused corrective transaction; SPEC changes only if clarification is needed |

Do not call a revision contract-neutral merely because later PLAN phases can still compile. Consider all observable and maintained contracts.

When classification is ambiguous and the choice changes documents, compatibility, task scope, or verification, present the evidence and ask before mutation.

## Inspect revision impact

Inspect the complete affected surface before confirming that steering is focused:

| Surface                  | Questions                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------- |
| Public interfaces        | Are functions, commands, options, schemas, formats, or documented behaviors added, removed, or changed?  |
| Configuration            | Do defaults, flags, environment settings, feature gates, or validation rules change?                     |
| Errors                   | Do supported failures, exception types, messages, exit codes, or rejection timing change?                |
| Dependencies             | Can a capability-specific dependency, version constraint, adapter, or build step be removed?             |
| Persistent formats       | Is stored data, wire data, migration behavior, or backward readability affected?                         |
| Architecture             | Do component responsibilities, dependency direction, lifecycle, concurrency, or ownership change?        |
| Tests and fixtures       | Which positive, negative, dependent, integration, acceptance, and compatibility cases change?            |
| Documentation            | Which SPEC, PLAN, LAYOUT, user docs, examples, and operational instructions describe the old capability? |
| Verification routing     | Which verification-map components and targets become obsolete, change coverage, or gain rejection tests? |
| Completed dependents     | Does any already completed component rely on the behavior or interface being revised?                    |
| Future work              | Which unimplemented tasks, milestones, prerequisites, estimates, or acceptance checks assume it?         |
| Distribution and release | Has the behavior been packaged, published, deployed, persisted, or consumed externally?                  |

Use code and import analysis as evidence, not as the sole dependency model. Inspect declared contracts and runtime integration points as well.

## Choose focused revision or redesign

A revision may remain focused when:

- the final behavior is unambiguous;
- affected paths and documents can be bounded;
- completed dependents are absent or can be updated coherently within a small declared range;
- no unresolved architecture decision is required;
- the project can return to a verified clean checkpoint after one or a few task transactions.

Broaden the change or return to design when impact crosses unresolved public contracts, persistent compatibility, multiple architectural layers, released consumers, or substantial completed dependents.

Do not force a broad revision into one “cleanup” task. If the correct final design needs several dependency-ordered tasks, create a change plan and execute each as a separate recoverable transaction.

## Execute a focused revision

Suspend ordinary forward task selection during steering.

1. Record the user's steering intent and classification in `steering-started`.
2. Define the intended final supported and unsupported behavior.
3. Create a temporary change overlay when the revision needs multiple tasks or material contract definition; a small unambiguous defect correction may use the existing SPEC and a bounded corrective task.
4. Determine affected completed behavior, future work, documents, tests, and verification targets.
5. Define dependency-ordered revision tasks and their verification.
6. Execute each revision task through `implementation.md` as a new recoverable transaction with a new task identifier.
7. Normalize the authoritative document complex after the final design is verified.
8. Run every affected direct, dependent, integration, milestone, and phase check.
9. Append `steering-completed` with the final capability and removal summaries, verification, normalization results, and remaining boundaries.
10. Produce steering and affected-boundary reports through `reporting.md`.
11. Return to `awaiting-steering`.

Do not reuse an earlier task identifier, reopen a completed transaction, amend old commits, or rewrite old journal records.

## Remove a rejected capability

When the user rejects an implemented capability:

1. State the final supported behavior and the precise unsupported boundary.
2. Remove obsolete implementation branches, adapters, handlers, configuration, and public options.
3. Remove positive tests whose only purpose was to require the rejected behavior.
4. Retain or add negative tests when the final contract requires explicit rejection, a stable error, or safe refusal.
5. Remove obsolete capability-specific fixtures, examples, documentation, dependencies, build configuration, and packaging metadata.
6. Update affected callers and completed dependents only when the impact inspection shows they rely on the capability.
7. Remove obsolete verification-map records and add the current rejection or boundary targets.
8. Run affected verification and confirm unrelated supported behavior remains intact.

Leave interface-neutral later phases and tasks unchanged. For example, removing encrypted-archive support must not rewrite persistence work that depends only on the unchanged archive-stream interface; revise future work only where it actually assumes encryption support.

Do not retain dead feature switches, dormant dependencies, misleading examples, or success fixtures merely to show that the capability once existed.

## Normalize authoritative state

Normalize current-state artifacts so that, except for legitimate history, the result is substantively equivalent to a project in which the rejected design had never been intended:

- **SPEC:** describe only the final supported system, including explicit unsupported behavior when normatively useful;
- **PLAN:** describe how to construct the final system from scratch; remove add-then-remove tasks, abandoned branches, and retrospective explanation;
- **LAYOUT:** describe only current physical ownership and dependency constraints;
- **ROADMAP:** regenerate from the normalized PLAN, remove obsolete tasks, and preserve completion only where current evidence still satisfies revised completion conditions;
- **verification map:** contain only current component-to-check relationships and current boundary checks;
- **user and developer documentation:** describe the final behavior without historical detours unless compatibility or release history makes them relevant;
- **temporary change documents:** remove them after their accepted delta is integrated into the main documents.

Verify bidirectional PLAN–ROADMAP correspondence after normalization. Recalculate task, milestone, and phase totals; do not preserve historical denominators.

Do not erase journal or Git history. Those sources explain how the current state was reached without polluting the documents used to understand or rebuild it.

## Revise future work only

When steering changes only unimplemented work:

1. Confirm completed code and contracts remain valid.
2. Revise the affected SPEC, PLAN, and LAYOUT nodes as required.
3. Regenerate the affected ROADMAP hierarchy and verification routing.
4. Preserve completed checkmarks only where their revised completion conditions remain satisfied.
5. Record the steering decision and document-only transaction evidence.
6. Report that no runtime behavior changed.
7. Return to `awaiting-steering` without beginning the revised future task.

Even a document-only revision must be recoverable and verified when it mutates authoritative files.

## Handle broader redesign

When steering reveals an unresolved architectural or product decision:

1. Preserve the clean checkpoint.
2. Classify the project as under review rather than in forward implementation.
3. Return to exploration or document revision through `lifecycle.md`.
4. Resolve the intended contract and architecture.
5. Create or revise a change overlay and its bounded plan.
6. Require a new explicit implementation request after design approval.

Do not begin speculative refactoring while the design question is open.

## Respect released behavior

Determine whether the capability has been externally released, persisted, deployed, documented as supported, or consumed by another project.

If it has, do not normalize away obligations that users or stored data still depend on. Treat removal as a compatibility change and preserve required:

- migration and rollback behavior;
- deprecation or transition periods;
- versioning and release notes;
- persistent-format readers or converters;
- compatibility tests;
- consumer communication or operational steps.

The “as if never intended” normalization rule applies only to unreleased or unconsumed design history. It does not authorize breaking external contracts invisibly.

## Journal steering

Use append-only records containing at least:

- `checkpoint`: completed boundary, progress, verification, clean recovery state, next boundary, and `awaiting-steering` status;
- `steering-started`: user intent, impact classification, affected surfaces, governing change documents, and planned revision boundary;
- ordinary transaction events for every revision task;
- `steering-completed`: final supported and unsupported behavior, feature additions or removals, normalized documents, verification, progress, and paused status.

Journal records describe execution history. Do not copy historical narration into the normalized SPEC or PLAN.

Make terminal checkpoint and steering records durable. If they are appended after the final task commit in a Git project, use the project's narrow metadata-only journal commit convention rather than amending task history or leaving a supposedly clean checkpoint with an uncommitted tracked journal.

## Return to a paused checkpoint

After steering:

1. Confirm every revision task is durably complete.
2. Confirm authoritative documents and derived maps describe the final design.
3. Confirm all affected verification passed.
4. Confirm recovery state is clean.
5. Reconcile progress after any PLAN or ROADMAP changes.
6. Report the final resulting capability, removed behavior, compatibility boundaries, and next planned work.
7. Append the final checkpoint evidence when not already represented by `steering-completed`.
8. Remain `awaiting-steering`.

Never infer permission to continue from successful revision.
