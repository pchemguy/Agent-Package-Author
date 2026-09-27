# Lifecycle and Authority

Use this reference to select the active SDD mode, enforce authorization boundaries, resolve governing sources, and preserve continuity across turns.

## Contents

- [Operating rule](#operating-rule)
- [Modes](#modes)
- [Transition gates](#transition-gates)
- [Authority and precedence](#authority-and-precedence)
- [Continuity](#continuity)
- [Checkpoint behavior](#checkpoint-behavior)
- [Truthful status](#truthful-status)
- [Workflow routing](#workflow-routing)

## Operating rule

Treat the user's current request as the authorization boundary. Skill activation supplies procedure, not permission to mutate files, create authoritative documents, commit changes, or continue beyond requested work.

Before acting:

1. Classify the requested mode.
2. Determine whether the requested action is read-only or mutating.
3. Load only the references required for that mode.
4. Resolve applicable project authorities before mutation.
5. Ask for clarification when ambiguity would change authoritative documents or project files.

## Modes

### Exploration

Use exploration while defining the problem, outcomes, constraints, scope, terminology, or possible design.

Allow discussion, read-only inspection, pseudocode, and small illustrative snippets. Do not create authoritative project documents or modify the project unless the user explicitly requests that transition.

Read `exploration.md`.

### Document authoring

Use document authoring when the user explicitly asks to create or materially restructure SPEC, PLAN, LAYOUT, ROADMAP, a verification map, or a temporary change definition.

Consolidate accepted decisions, expose material unresolved issues, inspect existing project state when available, and create complete-current-state documents. Do not begin implementation.

Read `document-system.md`; also read `roadmap.md` or `verification.md` when producing those artifacts.

### Review and revision

Use review and revision after authoring or when the user asks to assess or correct development documents.

Treat corrections as changes to intended design. Propagate them through affected document nodes, remove superseded content, and recheck architecture, dependencies, testability, and task order. Do not treat document sufficiency as implementation authorization.

Read `document-system.md`.

### Status inspection

Use status inspection when the user asks what exists, what is complete, what is active, what is next, or whether project artifacts agree.

Inspect read-only. Reconcile evidence conceptually, report inconsistencies, and do not repair or resume unless requested.

Read `project-discovery.md`; when present, also read `roadmap.md`, `recovery.md`, and `reporting.md` as required by the evidence being inspected.

### Implementation

Use implementation only when the user explicitly asks to implement, continue, resume, or complete a defined range.

Inspect startup and recovery state before choosing work. Resolve the requested task, milestone, or phase boundary. Execute one recoverable task transaction at a time. Stop after the requested range.

Read `project-discovery.md`, `implementation.md`, `recovery.md`, `verification.md`, `roadmap.md`, and `reporting.md`.

### Recovery

Use recovery when an implementation run may have been interrupted or when journal, recovery, filesystem, roadmap, or Git evidence indicates a nonterminal task.

Resolve recovery before new implementation. Preserve evidence and escalate ambiguous state.

Read `project-discovery.md`, `recovery.md`, and the applicable parts of `implementation.md`.

Recovery is a startup gate, not merely an error handler. Run it before selecting new work on every implementation invocation.

### Checkpoint steering

Use checkpoint steering after a requested implementation range reaches a clean durable boundary or when the user asks to revise work before proceeding.

Pause forward implementation. Accept, revise, redesign, or stop according to the user's instruction. Normalize accepted revisions into current-state artifacts and return to a paused checkpoint.

Read `checkpoint-steering.md`, plus the document, implementation, verification, roadmap, and reporting references required by the revision.

### Reporting

Use reporting for completion, checkpoint, steering, recovery, blocked-work, and read-only status communication.

Lead with verified capability and use evidence-supported state language. Read `reporting.md`; also read `roadmap.md` for progress counts and `project-discovery.md` when sources must be reconciled.

## Transition gates

Apply these normal transitions:

```text
exploration
    ↓ explicit request to create authoritative documents
document authoring
    ↓ documents produced
review and revision
    ↓ explicit request to implement
implementation
    ↓ requested range completed
checkpoint steering
    ↓ explicit acceptance or next bounded request
implementation
```

Allow a direct entry into a later mode when the user supplies adequate governing artifacts. Do not replay exploration or document generation solely because they normally occur earlier.

Return from implementation to exploration or review when implementation reveals:

- a material architectural contradiction;
- a missing public contract;
- a scope change beyond delegated implementation detail;
- an unresolved authority conflict;
- a change that would make authoritative documents false.

Stop at a safe task boundary when possible. Do not silently diverge from governing documents.

### Mutation gates

- Do not treat analysis as authorization to create files.
- Do not treat document creation as authorization to change code.
- Do not treat successful verification as authorization to commit unless the active workflow requires a task commit.
- Do not treat one completed range as authorization to start the next range.
- Do not publish, push, release, or otherwise affect external systems without explicit authority.
- Ask before acting when the transition remains ambiguous and mutation would occur.

## Authority and precedence

Determine applicable authority for the current scope. Use this responsibility model:

| Source                            | Responsibility                                                       |
| --------------------------------- | -------------------------------------------------------------------- |
| Current explicit user instruction | Authorization and accepted steering                                  |
| Project instruction files         | Local operating constraints, tools, conventions, and required checks |
| Main SPEC                         | Complete required current system                                     |
| Active change specification       | Explicit intended delta from the main SPEC                           |
| Main PLAN                         | Complete from-scratch implementation blueprint                       |
| Active change plan                | Ordered tasks for the active delta                                   |
| LAYOUT                            | Physical location and ownership                                      |
| ROADMAP                           | PLAN-derived durable progress view                                   |
| Verification map                  | Current component-to-check routing                                   |
| Journal and recovery state        | Transaction state and recovery evidence                              |
| Git history                       | Durable task commits and historical evidence when Git exists         |

Treat an active change document as overriding the main baseline only where it explicitly defines a revision.

Apply more deeply scoped project instructions to paths within their scope. Follow referenced instruction files far enough to obtain every applicable rule.

When sources conflict:

1. Apply an explicit precedence rule supplied by a governing source.
2. Otherwise stop before mutation.
3. Identify the exact conflict and affected action.
4. Preserve filesystem, journal, recovery, and Git evidence.
5. Ask the user which requirement governs.

Do not choose the most convenient instruction or silently ignore a conflict.

## Continuity

Across turns:

- build on accepted decisions;
- preserve exact terminology and contract boundaries;
- distinguish facts, accepted decisions, working assumptions, open questions, and discarded alternatives;
- surface earlier decisions when new information conflicts with them;
- avoid reopening settled decisions without a concrete reason;
- summarize accumulated decisions before authoring authoritative documents when conversation state is dispersed;
- ensure project artifacts remain comprehensible without conversation history.

Do not promote a brainstormed alternative, illustrative example, or tentative preference into a requirement without acceptance.

## Checkpoint behavior

After completing the user-requested range, establish the clean boundary through `checkpoint-steering.md` and report it through `reporting.md`.

While awaiting steering, do not start the next task. Accept only an explicit instruction to continue, revise, redesign, inspect, or stop.

After a focused steering revision, return to `awaiting-steering`; do not infer continuation from completion of the revision.

## Truthful status

Use the status that evidence supports:

```text
explored
specified
planned
under review
ready to implement
started
prepared
partially implemented
blocked
reverted
verified but not durably completed
completed
awaiting steering
campaign complete
```

Never report:

- a proposal as implemented;
- an unverified change as complete;
- a prepared task as complete;
- a completed but required-uncommitted Git task as durably complete;
- a roadmap checkbox as proof when journal or Git evidence disagrees.

## Workflow routing

Load the minimum applicable set:

| Intent                                 | Required references                                                                                         |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Explore or clarify                     | `exploration.md`                                                                                            |
| Inspect status or authorities          | `project-discovery.md`                                                                                      |
| Create or revise development documents | `document-system.md`                                                                                        |
| Generate or reconcile roadmap          | `roadmap.md`                                                                                                |
| Design or select verification          | `verification.md`                                                                                           |
| Implement or continue                  | `project-discovery.md`, `implementation.md`, `recovery.md`, `verification.md`, `roadmap.md`, `reporting.md` |
| Recover interrupted work               | `project-discovery.md`, `recovery.md`, `implementation.md`                                                  |
| Review or revise at checkpoint         | `checkpoint-steering.md` plus affected workflow references                                                  |
| Report completion or progress          | `reporting.md`, with `roadmap.md` for structured progress                                                   |

If a referenced later-phase file is not yet present during skill development, report that the corresponding workflow is not implemented rather than improvising an incomplete substitute.
