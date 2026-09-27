# `sdd-man` Specification

## 1. Purpose

Implement `sdd-man`, a modular Specification-Driven Development skill that governs a software project from exploratory design through authoritative documentation, bounded implementation, verification, recovery, human steering, and final reconciliation.

The skill SHALL support:

- greenfield projects;
- existing codebases;
- additive features;
- subtractive and corrective revisions;
- architectural changes;
- Git and non-Git projects;
- interrupted implementation runs;
- human-in-the-loop checkpoints and bounded implementation requests;
- recursively decomposed SPEC, PLAN, and LAYOUT document trees;
- a PLAN-aligned human-readable roadmap;
- component-to-verification routing;
- durable, recoverable task transactions;
- task, milestone, phase, and campaign completion reports.

The skill SHALL preserve a strict separation between:

1. the intended current system;
2. the from-scratch construction plan;
3. summarized implementation progress;
4. active execution and recovery state; and
5. historical execution evidence.

The skill SHALL never treat its mere activation as authorization to create documents, modify project files, commit changes, or continue implementation. The user's current request governs the active workflow and permitted mutations.

## 2. Design principles

### 2.1 Complete-current-state documentation

The authoritative development documents SHALL describe the complete intended current project as though it were being constructed from scratch.

They SHALL NOT become chronological collections of feature additions, reversals, migrations, or implementation history. Historical execution evidence belongs in the journal and, when available, Git history.

### 2.2 Explicit authority

Every persistent artifact SHALL have one defined responsibility. A normative fact SHALL have one canonical owner and SHALL be referenced rather than normatively duplicated elsewhere.

### 2.3 Progressive disclosure

`SKILL.md` SHALL route to focused workflow references. It SHALL NOT reproduce the complete SDD manual.

An ordinary invocation SHOULD require `SKILL.md` plus only the references needed for the active workflow. All reference resources SHALL be directly reachable from `SKILL.md`; the skill SHALL NOT depend on deep reference chains.

### 2.4 Recoverable implementation

Every implementation task SHALL execute as one recoverable transaction. A task SHALL preserve the exact baseline of every declared target before modifying it and SHALL leave a durable completion record before recovery data is removed.

### 2.5 Human control of transitions

Exploration, document authoring, review, implementation, and continuation are distinct authorization states. The skill SHALL require an explicit user request before crossing a boundary that creates authoritative documents or modifies the project.

### 2.6 Bounded context and work

Document and workflow decomposition SHALL follow meaningful responsibility, contract, physical-ownership, or implementation boundaries. The skill SHALL avoid both monolithic context loading and arbitrary fragmentation.

### 2.7 Verified capability reporting

Completion SHALL be reported in terms of verified capability delivered. File lists, commits, and passing checks are evidence; they are not substitutes for an implemented-feature summary.

## 3. Non-goals

The skill SHALL NOT:

- impose one application architecture, programming language, test framework, or build system;
- infer authorization to implement from discussion or document creation;
- replace project-specific instructions with generic conventions;
- use the journal as an architectural specification or narrative diary;
- use the roadmap as an independent implementation plan;
- use the verification map as proof of behavioral coverage;
- require Git in order to provide interruption recovery;
- rewrite or delete historical journal records;
- silently absorb unrelated user or agent changes;
- preserve rejected capabilities in authoritative documents merely because they existed temporarily;
- continue beyond a user-selected task, milestone, or phase boundary without authorization;
- claim completion when required verification is failing or unexecuted.

## 4. Terminology

| Term | Meaning |
|---|---|
| **authoritative documents** | The main SPEC, PLAN, LAYOUT, and other explicitly designated current-state documents |
| **SPEC tree** | `SPEC.md` and recursively decomposed specification nodes defining the required system |
| **PLAN tree** | `PLAN.md` and recursively decomposed plan nodes defining from-scratch implementation order |
| **LAYOUT tree** | `layout.md` and optional children defining physical project ownership |
| **roadmap** | A PLAN-derived checklist of phases, milestones, tasks, and durable completion status |
| **verification map** | A machine-readable mapping from implemented components and paths to stable verification targets |
| **phase** | A major independently meaningful project capability |
| **milestone** | A coherent review, handoff, or stopping boundary within a phase |
| **task** | The smallest recoverable, independently verifiable implementation transaction |
| **campaign** | A sequence of implementation tasks pursuing an initial project or a defined change |
| **checkpoint** | A clean durable boundary at which forward implementation pauses for human review or steering |
| **change overlay** | Temporary specification and plan material defining an intended delta from the main baseline |
| **normalization** | Rewriting authoritative state to describe only the settled resulting project, without chronological residue |
| **direct verification** | Checks owned by the changed component |
| **dependent verification** | Checks for components depending on changed behavior |
| **boundary verification** | Milestone-, phase-, or campaign-level checks |
| **durable completion** | Verified completion recorded in the journal and committed when Git is available |
| **recovery state** | Temporary manifests and backups required to restore an interrupted task |

## 5. Compatibility contract

### 5.1 Skill package

The runtime skill SHALL use ordinary Agent Skills conventions. Only `SKILL.md` is structurally mandatory; resource directories SHALL be included only when they have an actual role:

```text
sdd-man/
├── SKILL.md
├── references/
├── scripts/       # optional deterministic helpers
└── assets/        # optional reusable templates or schemas
```

`SKILL.md` frontmatter SHALL contain only the portable required fields:

```yaml
---
name: sdd-man
description: <activation description covering exploration, specification, planning, implementation, recovery, verification, and steering>
---
```

Host-specific presentation metadata MAY exist outside the portable core, for example `agents/openai.yaml`, but the runtime workflows SHALL NOT depend on it.

### 5.2 Execution environment

Bundled executable helpers, when present, SHALL:

- use Python and the standard library only unless the final skill specification is explicitly revised;
- support Python 3.11 or later;
- avoid network access;
- accept explicit project-root arguments;
- avoid dependence on the caller's current working directory;
- use argument arrays rather than shell-specific command strings where commands are stored;
- operate on Windows, Linux, and macOS to the extent permitted by filesystem semantics;
- return zero on success and nonzero on failure;
- emit concise actionable diagnostics;
- avoid destructive repository-wide operations.

### 5.3 Project independence

The skill SHALL discover and honor the target project's own:

- language and dependency versions;
- test runners;
- build and packaging tools;
- formatting, linting, and type-checking commands;
- generated-file policies;
- repository layout;
- instruction hierarchy;
- supported platforms.

## 6. Skill package architecture

The implemented skill MAY use the following modular structure where each listed resource has a demonstrated purpose:

```text
sdd-man/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── lifecycle.md
│   ├── exploration.md
│   ├── project-discovery.md
│   ├── document-system.md
│   ├── roadmap.md
│   ├── verification.md
│   ├── implementation.md
│   ├── recovery.md
│   ├── checkpoint-steering.md
│   └── reporting.md
├── scripts/
│   ├── sdd_status.py
│   ├── sdd_roadmap.py
│   ├── sdd_verification.py
│   ├── sdd_transaction.py
│   └── sdd_validate.py
└── assets/
    ├── templates/
    │   ├── SPEC.md
    │   ├── PLAN.md
    │   ├── layout.md
    │   ├── ROADMAP.md
    │   └── verification-map.json
    └── schemas/
        ├── implementation-log.schema.json
        ├── transaction-manifest.schema.json
        └── verification-map.schema.json
```

Exact helper boundaries MAY be refined during implementation, but responsibilities SHALL remain nonredundant:

- references define judgment-intensive workflows and policies;
- scripts MAY implement deterministic state inspection, validation, selection, journaling, backup, or restoration mechanics when the operation is clear and well-defined;
- assets provide reusable project artifact templates and schemas.

The presence of a possible helper in this specification SHALL NOT require that helper to be implemented. A script SHALL be included only when:

- its inputs, outputs, preconditions, and failure behavior can be defined precisely;
- deterministic execution materially improves safety, repeatability, or context efficiency;
- the same operation would otherwise be reimplemented repeatedly;
- the helper can refuse ambiguous state rather than embedding architectural judgment;
- its maintenance cost is justified by actual workflow use.

Exploration, architectural decomposition, specification authorship, plan design, impact classification, and other judgment-heavy work SHALL remain agent-guided. The skill SHALL NOT create scripts merely to make the package appear comprehensive.

The skill package SHALL NOT include auxiliary documentation that is unnecessary to runtime operation or verification.

## 7. `SKILL.md` orchestration contract

`SKILL.md` SHALL:

1. determine the user's requested workflow;
2. enforce mutation and transition authorization;
3. identify the minimum required references;
4. invoke an available deterministic helper only when its defined operation matches the current need;
5. route contradictions and ambiguous state to escalation;
6. require verification before completion;
7. require capability-oriented completion reporting.

It SHALL contain a compact routing table covering at least:

| User intent | Required workflow references |
|---|---|
| Explore or clarify a project | `lifecycle.md`, `exploration.md` |
| Inspect project status | `lifecycle.md`, `project-discovery.md`, and recovery guidance when execution state exists |
| Create or revise SPEC/PLAN/LAYOUT | `document-system.md`, plus `roadmap.md` and `verification.md` where applicable |
| Review documents | `document-system.md` |
| Implement or resume | `project-discovery.md`, `implementation.md`, `recovery.md`, `verification.md`, `roadmap.md`, `reporting.md` |
| Recover interrupted work | `project-discovery.md`, `recovery.md`, `implementation.md` |
| Review a checkpoint or steer | `checkpoint-steering.md`, `document-system.md`, `implementation.md`, `verification.md`, `reporting.md` |
| Report progress | `project-discovery.md`, `roadmap.md`, `reporting.md` |

## 8. Conversation lifecycle

### 8.1 Modes

The skill SHALL support these modes:

```text
exploration
document authoring
review and revision
implementation
checkpoint steering
status inspection
recovery
```

### 8.2 Transition gates

The normal lifecycle is:

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
    ↓ explicit acceptance or new bounded request
implementation
```

Implementation MAY return to exploration or review when it reveals a material architectural error or missing decision.

An explicit request MAY enter a later mode directly when adequate authoritative documents already exist. The skill SHALL NOT replay earlier modes unnecessarily.

### 8.3 Authorization rules

- Discussion, analysis, read-only inspection, pseudocode, and illustrative snippets SHALL NOT authorize project mutation.
- Creating or revising documents SHALL NOT authorize implementation.
- Completing one requested task range SHALL NOT authorize the next range.
- A narrow technical question SHALL NOT change the active mode.
- When ambiguity would cause authoritative documents or project files to be changed, the skill SHALL request clarification.

### 8.4 Continuity

Across turns, the skill SHALL:

- preserve accepted terminology and decisions;
- distinguish accepted requirements from tentative ideas;
- surface conflicts with earlier decisions;
- avoid reopening settled questions without new evidence;
- summarize complex decision state before authoring authoritative documents;
- ensure final project artifacts remain understandable without conversation history.

## 9. Authority and precedence model

The skill SHALL distinguish these authorities:

| Artifact or source | Canonical responsibility |
|---|---|
| User's current explicit instruction | Current authorization and accepted steering |
| Applicable project instructions | Local operating constraints, tools, conventions, and required checks |
| Main SPEC | Required complete current system |
| Active change specification | Explicit intended delta from the main SPEC |
| Main PLAN | From-scratch implementation blueprint for the complete current system |
| Active change plan | Ordered tasks for the current delta |
| LAYOUT | Physical location and ownership |
| ROADMAP | Derived structure and durable progress view |
| Verification map | Current component-to-check routing |
| Journal and recovery state | Active and historical transaction evidence |
| Git history | Durable task commits and historical evidence when Git exists |

An active change document SHALL override the main baseline only where it explicitly defines a revision.

When authorities conflict and no explicit precedence rule resolves the conflict, the skill SHALL stop, preserve evidence, and request user direction.

## 10. Project discovery and startup inspection

Before mutation, the skill SHALL discover:

- the project root;
- whether the project is inside a Git repository;
- the authoritative development-document roots;
- applicable root and directory-scoped instruction files such as `AGENTS.md`;
- referenced project guidance such as `docs/dev/PROJECT.md`;
- main and active-change document sets;
- ROADMAP and verification-map presence;
- implementation journal and recovery directories;
- Git working-tree and index state when applicable;
- build, test, lint, type-check, formatting, and packaging commands;
- generated-file and ignored-file policies.

The skill SHALL produce or internally establish a project authority map and classify current state as one of at least:

- exploration only;
- specified but not planned;
- planned but not started;
- campaign ready;
- active task started but not prepared;
- active task prepared and incomplete;
- completed but not committed;
- committed but not cleaned;
- between tasks;
- awaiting checkpoint steering;
- phase complete;
- campaign complete;
- inconsistent or ambiguous.

Status inspection SHALL be usable without authorizing repair or implementation.

## 11. Exploration workflow

Exploration SHALL:

- clarify goals, outcomes, constraints, scope, and non-goals;
- normalize vocabulary;
- examine plausible architectures, contracts, data models, algorithms, tools, and established patterns;
- explain unfamiliar techniques sufficiently for informed decisions;
- identify assumptions, tradeoffs, boundary cases, risks, dependencies, and unknowns;
- distinguish facts, user decisions, working assumptions, unresolved questions, and discarded alternatives;
- challenge contradictions and weak boundaries directly;
- converge incrementally rather than forcing premature completeness;
- provide compact decision-state summaries when useful;
- assess readiness for authoritative document creation.

Exploratory prototypes that modify files SHALL be classified as either disposable work outside the project or actual project changes. Actual project changes SHALL follow the implementation protocol.

## 12. Development-document system

### 12.1 Root structure

The normal development-document structure is:

```text
docs/dev/
├── SPEC.md
├── spec/
├── PLAN.md
├── plan/
├── ROADMAP.md
├── layout.md
├── layout/
└── verification-map.json
```

Only required directories and files SHALL be created. Small projects MAY retain focused single-file SPEC, PLAN, or LAYOUT documents.

### 12.2 Recursive decomposition

Every decomposed document node SHALL define:

- its scope and abstraction level;
- its children and their responsibilities;
- explicit child boundaries;
- connecting contracts, dependencies, and shared invariants;
- canonical ownership of normative subjects.

A child SHALL add detail only within the responsibility assigned by its parent.

Documents SHALL be split by meaningful responsibility or contract boundaries, not by byte count alone, ordinal numbering, or arbitrary topic buckets.

### 12.3 SPEC tree

The SPEC tree SHALL define:

- purpose, scope, and non-goals;
- system context and use cases;
- terminology and invariants;
- architectural decomposition;
- component responsibilities;
- interfaces, data formats, persistent formats, and external protocols;
- dependency constraints;
- required behavior and boundary cases;
- error behavior;
- acceptance conditions;
- scope routing to child specifications.

Detailed behavior SHALL live in the lowest appropriate canonical node.

### 12.4 PLAN tree

The PLAN tree SHALL define:

- the complete from-scratch implementation strategy;
- named phases and their order;
- named milestones within phases;
- bounded tasks within milestones;
- dependencies and prerequisites;
- SPEC coverage;
- affected components and files where known;
- direct, dependent, integration, and boundary verification;
- objective completion conditions.

The first phase SHALL deliver the smallest useful testable MVP. Later phases SHALL provide the smallest meaningful independently verifiable increments.

An ordinary task SHOULD modify one production file plus associated tests and directly affected documents, but atomic contract changes MAY span inseparable artifacts.

### 12.5 LAYOUT tree

The LAYOUT tree SHALL define:

- repository-root files and major directories;
- physical ownership boundaries;
- implementation, test, documentation, packaging, generated, and runtime locations;
- import and dependency constraints enforced through layout;
- correspondence among SPEC areas, implementation locations, test owners, and PLAN phases;
- artifact and installed-behavior policies;
- layout evolution rules.

LAYOUT SHALL decompose by physical ownership domain. It SHALL NOT mechanically mirror SPEC or PLAN.

### 12.6 Review and revision

Document review SHALL:

- treat user corrections as intended-design changes;
- propagate accepted changes through affected nodes;
- remove superseded content;
- recheck architecture, dependencies, testability, task order, and document boundaries;
- preserve one canonical owner per normative fact;
- remain separate from implementation authorization.

## 13. Dependency and revision model

Inter-component dependencies SHALL form a directed acyclic graph using `A → B` to mean that B depends on A.

- Direct and transitive cycles are prohibited.
- Reconvergent and diamond dependencies are permitted.
- Proposed mutually dependent components SHALL be combined or refactored around a lower-level shared contract.
- Implementation and revision SHALL proceed from unaffected dependencies toward dependents.

Breaking contract changes SHALL use expand–migrate–contract when needed:

1. add the new contract while retaining temporary compatibility;
2. migrate dependents in dependency order;
3. remove the obsolete contract after no dependent uses it.

Every intermediate task SHALL leave the project internally consistent and testable.

## 14. Roadmap contract

### 14.1 Responsibility

`docs/dev/ROADMAP.md` SHALL be a human-readable projection of PLAN structure and durable progress.

PLAN owns phase, milestone, task, ordering, dependency, and verification definitions. ROADMAP SHALL NOT invent or alter them.

### 14.2 Structure

ROADMAP SHALL:

- contain every current PLAN phase, milestone, and task exactly once;
- preserve PLAN order;
- link each checklist entry to its canonical PLAN node;
- provide phase, milestone, and task counts;
- provide durable completion counts;
- remain compact enough for rapid human inspection.

### 14.3 Status semantics

Persisted checklist state SHALL be binary:

- `[ ]`: not durably complete;
- `[x]`: durably complete.

The roadmap SHALL NOT encode active, prepared, blocked, partially implemented, or reverted task states. Those belong to the journal and recovery state.

A milestone SHALL be checked only after all child tasks and milestone verification pass. A phase SHALL be checked only after all milestones and phase verification pass.

### 14.4 Generation and maintenance

After PLAN generation or material restructuring, the skill SHALL:

1. derive ROADMAP from PLAN;
2. confirm exact one-to-one task correspondence;
3. confirm identical ordering;
4. initialize or reconcile state from durable evidence;
5. validate counts and parent-child checkmarks.

ROADMAP SHALL be included in an implementation task's declared scope whenever completion state changes.

### 14.5 Startup use

ROADMAP MAY be read first for orientation, but new work SHALL NOT be selected until journal, recovery state, Git durability when applicable, ROADMAP, and PLAN have been reconciled.

## 15. Verification-map contract

### 15.1 Responsibility

`docs/dev/verification-map.json` SHALL map implemented components and physical source areas to stable executable verification targets.

It SHALL support unit tests, dependent-component tests, integration tests, and other component-specific checks. PLAN remains authoritative for checks required by a particular task, milestone, phase, or campaign.

### 15.2 Granularity

The map SHOULD identify:

```text
component
→ owned source paths
→ reusable verification targets
```

It SHOULD map test modules, suites, markers, or commands rather than individual test cases. Individual selectors MAY be used when intentionally stable and useful.

### 15.3 Command representation

Commands SHALL be stored as argument arrays rather than shell command strings.

Verification targets SHALL be normalized so that a target used by several components is defined once and referenced by stable semantic name.

### 15.4 Current-state rule

The verification map SHALL describe implemented current project paths. Future test intent belongs in PLAN until corresponding files exist.

Whenever a task creates, moves, deletes, or changes ownership of source or tests, it SHALL update the verification map in the same transaction when the map is present and applicable.

### 15.5 Selection algorithm

For changed paths, the skill SHALL:

1. resolve owning components;
2. select direct verification targets;
3. determine affected dependents;
4. select dependent and integration targets;
5. add PLAN-required checks;
6. add project-instruction checks;
7. add milestone, phase, or campaign checks when applicable;
8. deduplicate commands;
9. execute checks from narrowest to broadest.

The map defines a minimum candidate set. It SHALL NOT justify omitting other relevant verification.

### 15.6 Validation

Validation SHALL detect at least:

- invalid JSON or schema versions;
- duplicate identifiers;
- missing referenced targets;
- invalid or missing paths;
- empty commands;
- commands that collect no tests where collection is supported;
- stale renamed or deleted tests;
- disallowed ambiguous path ownership;
- orphan targets under the project's declared policy.

Import analysis, test collection, markers, fixtures, naming conventions, and coverage data MAY aid map construction and validation but SHALL NOT be treated as conclusive proof of behavioral coverage.

## 16. Campaign model

### 16.1 Initial campaign

An initial campaign implements the main SPEC and PLAN for a project whose active change overlay is absent.

### 16.2 Change campaign

A change campaign applies a defined delta to an existing authoritative baseline. Change kinds SHALL include at least:

- additive feature;
- checkpoint revision;
- defect correction;
- architectural revision.

The current protocol MAY use `docs/dev/FEATURE-SPEC.md` and `docs/dev/FEATURE-PLAN.md` as temporary change documents. Their role is a change overlay even when the change is subtractive. The final skill MAY adopt generalized filenames only if compatibility and migration behavior are explicitly specified.

The change specification SHALL define the intended delta. The change plan SHALL define bounded tasks needed to reach it.

### 16.3 Existing campaign

When the journal declares an existing campaign, that record SHALL govern resumption. The skill SHALL confirm its mode and document paths against the project and SHALL NOT silently replace it with a new campaign.

### 16.4 Campaign integration

At change-campaign completion, the skill SHALL:

1. integrate settled requirements into the main SPEC tree;
2. integrate final from-scratch construction into the main PLAN tree;
3. update LAYOUT, ROADMAP, and verification map;
4. remove superseded baseline material;
5. remove temporary change documents;
6. execute complete affected-scope verification;
7. record durable campaign completion.

## 17. Bounded implementation selection

The skill SHALL support requests to:

- implement the next task;
- implement the next `N` tasks;
- complete the current milestone;
- implement the next milestone;
- complete the current phase;
- implement the next phase;
- implement through a named milestone or phase;
- stop after the MVP;
- resume an existing campaign.

Each task SHALL remain an independent transaction even when several tasks are requested together.

“Next milestone” or “next phase” SHALL complete the currently incomplete boundary before advancing to a later boundary. Named boundaries SHALL be resolved unambiguously against PLAN and ROADMAP.

After the requested range is completed, the skill SHALL stop at a clean checkpoint and await further direction.

## 18. Task transaction protocol

### 18.1 Operational paths

Unless the project defines compatible equivalents, use:

```text
IMPLEMENTATION_LOG.jsonl
.implementation-state/
└── <task-id>/
    ├── manifest.json
    └── backup/
        └── <project-relative paths>
```

The journal SHALL be append-only for the active campaign. Recovery data SHALL remain uncommitted.

### 18.2 State machine

```text
STARTED → PREPARED → COMPLETED → COMMITTED → CLEANED
                  ↘ REVERTED
```

- `STARTED`: task and intended operations declared; no target modified.
- `PREPARED`: every target baseline captured and verified; mutation permitted.
- `COMPLETED`: implementation and required verification succeeded.
- `COMMITTED`: a matching task commit contains the completed change when Git is available.
- `CLEANED`: recovery data removed and no task residue remains.
- `REVERTED`: the complete declared scope restored to its prepared baseline.

### 18.3 Preflight

Before starting a task, the skill SHALL:

- resolve any previous active transaction;
- identify the next permitted PLAN or change-PLAN task;
- read governing SPEC, PLAN, LAYOUT, roadmap, verification, and instruction nodes;
- inspect relevant code and tests read-only;
- define one bounded scope;
- enumerate anticipated paths;
- classify each operation as `create`, `modify`, `delete`, or `rename`;
- identify direct, dependent, integration, and boundary verification;
- inspect the Git worktree and index when applicable;
- refuse to absorb pre-existing changes in target paths without explicit authorization;
- generate a unique UTC timestamp plus semantic slug task identifier.

### 18.4 Preparation

The skill SHALL:

1. append a `started` record;
2. create a manifest recording every operation and baseline;
3. back up every existing target while preserving exact bytes and relevant metadata;
4. record absence for create targets;
5. preserve both endpoints for renames;
6. verify backup hashes;
7. hash and version the manifest;
8. append `prepared`;
9. modify no target before preparation is complete.

### 18.5 Scope extension

When an undeclared path must change, the skill SHALL stop before modifying it, discover newly applicable instructions, journal the extension, capture and verify its baseline, version the manifest, append a new `prepared` record, and only then continue.

If the path was already modified before declaration and its baseline cannot be proven, the skill SHALL stop and request direction.

### 18.6 Implementation

The task SHALL:

- modify only paths in the latest prepared manifest;
- implement the smallest complete planned change;
- update code, tests, and development documents together;
- update ROADMAP and verification map when applicable;
- preserve unrelated changes;
- avoid beginning a second PLAN task to make the current one pass.

Material architectural contradictions or scope expansions beyond the bounded task SHALL trigger a controlled stop or return to design.

### 18.7 Verification and completion

Before appending `completed`, the skill SHALL:

1. compare changed paths with the manifest;
2. inspect the complete diff;
3. verify document, code, test, roadmap, and verification-map consistency;
4. run direct tests;
5. run dependent tests;
6. run relevant integration checks;
7. run required lint, type, format, build, and packaging checks;
8. run boundary verification when completing a milestone, phase, or campaign;
9. fix task-caused failures and repeat affected checks;
10. update ROADMAP checkmarks and counts;
11. prepare the capability summary;
12. append `completed` with exact verification evidence.

### 18.8 Git completion

In a Git repository, the skill SHALL:

- stage only declared task paths and the journal;
- include declared deletions and renames explicitly;
- never stage recovery data;
- inspect the staged diff;
- create one task commit with an exact `Task: <task-id>` trailer;
- confirm the commit contains the complete task and no unrelated changes;
- remove recovery data only after commit verification;
- confirm no declared path remains modified or staged.

The skill SHALL NOT amend, squash, rebase, push, or otherwise rewrite or publish project commits without explicit user authorization.

### 18.9 Non-Git completion

Without Git, the skill SHALL treat the journal completion record as durable terminal evidence, reconfirm verification, remove recovery data, and confirm no backup artifacts remain.

## 19. Recovery protocol

Every implementation or continuation run SHALL inspect recovery state before selecting new work.

### 19.1 `STARTED` without `PREPARED`

Confirm no target changed, remove incomplete preparation, append `reverted`, and restart with a new task identifier. Escalate if baseline integrity is uncertain.

### 19.2 `PREPARED` without `COMPLETED`

Validate the manifest and backups, restore the entire latest prepared scope, verify baseline hashes, remove the recovery directory, append `reverted` with reason `interrupted-before-completion`, and restart with a new identifier.

Restoration SHALL be all-or-nothing unless the user explicitly overrides the rule.

### 19.3 `COMPLETED` in Git

Search history for the exact task trailer.

- If the matching commit exists and is correct, clean leftover recovery state.
- If no matching commit exists, inspect the diff, rerun verification, and commit the exact completed task if valid.
- If re-verification fails or state is inconsistent, preserve evidence and restore or escalate.
- If a matching commit exists without a completion record, stop and ask rather than reverting committed work.

### 19.4 `COMPLETED` without Git

Reconfirm recorded verification before removing recovery data. Preserve backups and escalate or restore when evidence conflicts.

### 19.5 Escalation conditions

The skill SHALL preserve evidence and ask the user when:

- multiple tasks appear active;
- a manifest or backup is absent or corrupt;
- an undeclared path changed;
- target changes may belong to another actor;
- journal, filesystem, roadmap, verification map, or Git disagree materially;
- restoration could overwrite work of uncertain origin;
- instruction authorities conflict;
- the journal is corrupt beyond a clearly truncated final append.

## 20. Testing and failure handling

### 20.1 Test strategy

PLAN SHALL derive tests from specified behavior, invariants, error cases, and acceptance conditions. It SHALL identify:

- component unit tests;
- dependent-component tests;
- integration tests;
- milestone verification;
- phase verification;
- campaign acceptance;
- non-test checks required by the project.

### 20.2 Task-caused failures

Failures caused by the active task SHALL be fixed within the same transaction when they belong to the declared behavior. Required scope extension SHALL follow the scope-extension protocol.

Tests SHALL NOT be weakened, valid assertions removed, or unrelated behavior altered merely to obtain a passing run.

### 20.3 Pre-existing or unrelated failures

The skill SHALL classify rather than silently absorb failures unrelated to the task. If they block required verification, the task SHALL remain incomplete until the user resolves the blocker or authorizes a bounded corrective change.

### 20.4 Defect classification

A defect request SHALL be classified as:

- implementation nonconformance with an adequate SPEC;
- missing or ambiguous specification;
- intended behavior change requiring a change overlay;
- architectural defect requiring redesign.

## 21. Human-in-the-loop checkpoints

### 21.1 Establishment

After completing the user-requested range, the skill SHALL:

- confirm all included tasks are durably completed;
- run requested boundary verification;
- confirm recovery state is clean;
- update ROADMAP;
- report implemented features;
- identify the exact next planned work;
- enter `awaiting-steering` state.

The skill SHALL NOT begin the next task without explicit authorization.

### 21.2 Steering choices

At a checkpoint, the user MAY:

- accept and continue;
- request a focused revision;
- revise future tasks;
- reopen exploration or architectural design;
- stop the campaign.

### 21.3 Steering impact classification

The skill SHALL classify requested steering as:

- contract-neutral simplification;
- contract revision;
- architectural revision;
- defect correction.

It SHALL inspect public interfaces, configuration, errors, dependencies, persistent formats, documentation, tests, fixtures, examples, verification routing, completed dependents, and future tasks before confirming that a revision is focused.

### 21.4 Focused revision

A focused revision SHALL execute as one or more recoverable transactions. It SHALL suspend normal forward task selection and SHALL NOT reopen or rewrite earlier task records.

For a rejected capability, the revision SHALL:

- define the final supported and unsupported behavior;
- remove obsolete implementation paths;
- remove success tests for rejected behavior;
- retain or add negative tests when the unsupported contract requires them;
- remove capability-specific dependencies, options, examples, and documentation;
- update SPEC, PLAN, LAYOUT, ROADMAP, and verification map;
- run all affected verification;
- return to `awaiting-steering` after completion.

### 21.5 Normalization

After steering, the authoritative state SHALL be equivalent to the state that would have existed had the rejected capability never been part of the intended project, except for append-only journal and Git history.

PLAN SHALL NOT retain add-then-remove tasks. ROADMAP SHALL NOT retain removed PLAN tasks. Historical explanations SHALL NOT remain in current-state documents unless externally released compatibility obligations make them normatively relevant.

### 21.6 Released behavior limitation

If the rejected capability was externally released or consumed, the skill SHALL treat removal as a compatibility change and preserve required migration, deprecation, versioning, or release-history obligations.

## 22. Completion reporting contract

### 22.1 General requirement

Every task, milestone, phase, and campaign completion report SHALL summarize verified implemented features or enabling capabilities.

It SHALL NOT substitute file lists, test counts, or commit identifiers for a capability summary.

### 22.2 Task report

A task report SHALL include:

- task name;
- incremental implemented features or enabling capabilities;
- verification result;
- roadmap progress;
- next task or reached stopping boundary.

### 22.3 Milestone report

A milestone report SHALL synthesize:

- the integrated capability delivered by its tasks;
- supported behavior and important guarantees;
- milestone verification;
- roadmap position;
- next milestone or stopping boundary.

It SHALL NOT merely concatenate task reports.

### 22.4 Phase report

A phase report SHALL synthesize:

- the major project capability now available;
- supported public workflows;
- cross-component guarantees;
- phase acceptance results;
- cumulative progress;
- remaining phases or campaign status.

### 22.5 Non-feature tasks

Reports SHALL describe the actual category of outcome, including when applicable:

- enabling infrastructure;
- test capability;
- documentation or contract clarification;
- defect correction;
- migration step;
- removal of obsolete behavior;
- operational hardening.

They SHALL explicitly state when runtime behavior did not change.

### 22.6 Journal summaries

Each `completed` record SHALL contain a concise summary and MAY contain a structured `features` list. When the task closes a milestone or phase, it SHOULD contain concise boundary summaries sufficient for later report reconstruction.

### 22.7 Multi-task runs

For a multi-task request, the skill SHALL provide concise task-boundary reports, aggregate milestone and phase reports when crossed, and a final self-contained summary of the entire requested run.

## 23. Journal contract

`IMPLEMENTATION_LOG.jsonl` SHALL contain one valid JSON object per physical line.

- Records SHALL be appended, not edited or reordered within an active campaign.
- Paths SHALL be project-relative with consistent separators.
- Timestamps SHALL be UTC.
- Task identifiers SHALL be stable and unique.
- Secrets, credentials, and large file contents SHALL NOT be recorded.
- Detailed backup metadata SHALL remain in the manifest.
- The journal SHALL record execution state, not architectural requirements.

Required event kinds SHALL include at least:

```text
campaign
started
prepared
scope-extension-started
completed
reverted
checkpoint
steering-started
steering-completed
```

The exact schema SHALL support:

- campaign identity and document set;
- task scope and intended operations;
- baseline and manifest hashes;
- exact verification commands and outcomes;
- capability summaries;
- phase and campaign completion flags;
- checkpoint boundaries;
- steering intent and completion.

## 24. Optional deterministic helpers

Scripts are optional. The skill SHALL remain operational through agent reasoning and available host tools when no bundled helper is justified or present. This section defines conditional contracts for helpers that MAY be included; it does not require their implementation.

A helper SHALL automate only a clear deterministic operation. It SHALL NOT decide architecture, invent document decomposition, determine product requirements, resolve ambiguous ownership, or replace required human judgment.

### 24.1 Optional `sdd_status.py`

If included, it SHALL inspect project roots, document presence, Git state, journal state, recovery directories, ROADMAP, and verification map. It SHALL produce a machine-readable status plus concise diagnostics without mutating the project.

### 24.2 Optional `sdd_roadmap.py`

If included, it SHALL support only well-defined operations such as structural validation, progress calculation, next-boundary resolution, or deterministic checkbox updates. It MAY render a roadmap from an already resolved structured plan representation, but it SHALL never infer or invent phases, milestones, tasks, or architectural groupings.

### 24.3 Optional `sdd_verification.py`

If included, it SHALL validate the verification map, resolve explicitly mapped components from paths, select registered verification targets, and optionally validate test collection through explicit project commands. It SHALL NOT infer that selected checks are sufficient when project judgment identifies additional affected behavior.

### 24.4 Optional `sdd_transaction.py`

If included, it SHALL support precisely specified operations such as manifest creation, baseline hashing, backup verification, journal append validation, declared scope extension, restoration, or cleanup checks. Destructive actions SHALL be limited to validated manifest paths.

### 24.5 Optional `sdd_validate.py`

If included, it SHALL validate mechanically decidable aspects of the SDD artifact complex, including document presence, explicit roadmap-to-PLAN correspondence, verification-map structure, journal schema, and recovery-state consistency. It SHALL report rather than attempt to resolve semantic or authority conflicts requiring judgment.

### 24.6 Safety

Any included helper SHALL refuse unsafe or ambiguous operations. Helpers SHALL NOT use repository-wide reset, checkout, clean, recursive deletion of unresolved paths, or broad Git staging.

## 25. Skill verification materials

Development fixtures and tests for `sdd-man` SHOULD include representative projects for:

- a small greenfield non-Git project;
- a greenfield Git project;
- a brownfield project with unrelated dirty paths;
- recursively decomposed SPEC, PLAN, and LAYOUT trees;
- a generated ROADMAP with phases, milestones, and tasks;
- a verification map with shared integration targets;
- `STARTED` without `PREPARED`;
- `PREPARED` without `COMPLETED`;
- `COMPLETED` without a Git commit;
- a committed task with leftover recovery state;
- roadmap/journal disagreement;
- corrupt or missing recovery data;
- a checkpoint steering revision that removes a capability;
- a non-Git completion and recovery path.

Automated tests SHALL cover every included helper's deterministic behavior, schema validation, path safety, refusal conditions, and other declared contracts. Workflows without helpers SHALL be tested through representative skill acceptance scenarios rather than artificial automation.

## 26. Acceptance scenarios

### 26.1 Exploration without mutation

Given an underspecified project idea, the skill SHALL explore alternatives, distinguish decisions from assumptions, and refrain from creating files or beginning implementation.

### 26.2 Document generation

Given an accepted greenfield design, the skill SHALL produce coherent SPEC, PLAN, LAYOUT, ROADMAP, and applicable verification-map foundations. PLAN and ROADMAP SHALL align exactly, and document roots SHALL remain useful orientation nodes.

### 26.3 Review correction

Given a user correction after document generation, the skill SHALL propagate it through affected nodes, remove superseded statements, revalidate dependencies and task order, and refrain from implementation.

### 26.4 Greenfield bounded implementation

Given “implement through the MVP milestone,” the skill SHALL execute each included task as a separate transaction, update progress, stop after milestone verification, summarize delivered capability, and await further direction.

### 26.5 Existing-code feature campaign

Given main documents plus a valid change overlay, the skill SHALL treat the main documents as baseline and the overlay as explicit delta, implement in bounded order, and normalize the completed change into the main trees.

### 26.6 Verification selection

Given a changed component path, the skill SHALL select its direct tests, affected dependent tests, relevant integration targets, PLAN-required checks, and boundary checks without relying only on import analysis.

### 26.7 Interrupted prepared task

Given a valid `PREPARED` task without `COMPLETED`, the skill SHALL restore the entire declared baseline, verify restoration, journal `reverted`, and restart with a new identifier before new implementation.

### 26.8 Completed uncommitted task

Given `COMPLETED` in Git without a matching commit, the skill SHALL inspect the exact diff, rerun recorded verification, commit the valid completed task, and clean recovery state. It SHALL preserve evidence and escalate if state is inconsistent.

### 26.9 Non-Git recovery

Given a non-Git project, the skill SHALL use journal, manifest, hashes, and backups for deterministic recovery and SHALL treat a verified completion record as the durable terminal boundary.

### 26.10 Human checkpoint steering

Given a completed archive phase that supports encrypted 7z archives and a user request to remove that support, the skill SHALL suspend forward work, classify impact, remove success behavior and obsolete artifacts, preserve or add the appropriate rejection test, normalize all authoritative documents and derived maps, rerun affected phase verification, report the final reduced capability, and remain paused.

### 26.11 Inconsistent evidence

Given disagreement among journal, recovery state, ROADMAP, verification map, filesystem, or Git such that ownership or baseline cannot be proven, the skill SHALL preserve evidence and request user direction rather than guessing or performing destructive repair.

### 26.12 Completion reporting

At every completed task, milestone, phase, and campaign boundary, the skill SHALL describe the verified capability delivered at that boundary and distinguish user-visible behavior from enabling infrastructure.

## 27. Completion criteria

The `sdd-man` skill is complete when:

- `SKILL.md` routes every specified workflow and enforces transition authorization;
- all required references are focused, directly reachable, and nonduplicative;
- every included deterministic helper implements its declared responsibilities safely, and no helper exists without a justified deterministic role;
- every included template or schema has a demonstrated workflow or helper consumer, and no unused resource is retained;
- project artifact authority and precedence are unambiguous;
- document generation, review, roadmap, verification mapping, implementation, recovery, steering, and reporting workflows conform to this specification;
- Git and non-Git paths are both verified;
- all acceptance scenarios pass;
- negative and corrupted-state scenarios fail safely with actionable diagnostics;
- every included helper produces deterministic output for identical input and project state;
- no workflow depends on network access or undeclared third-party Python packages;
- the skill never proceeds across an authorization or HIL checkpoint without an explicit user request;
- the final skill package passes structural validation and forward-testing on representative projects.
