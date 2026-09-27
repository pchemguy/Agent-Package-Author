# Authoritative Development Documents

Use this reference to create, restructure, review, or normalize SPEC, PLAN, LAYOUT, and genuinely shared development documents. Apply it only after the user explicitly authorizes document work.

## Contents

- [Governing model](#governing-model)
- [Before authoring](#before-authoring)
- [Recursive document architecture](#recursive-document-architecture)
- [SPEC tree](#spec-tree)
- [PLAN tree](#plan-tree)
- [LAYOUT tree](#layout-tree)
- [Other shared documents](#other-shared-documents)
- [Cross-tree alignment](#cross-tree-alignment)
- [Dependencies and contract revision](#dependencies-and-contract-revision)
- [Review and correction](#review-and-correction)
- [Change overlays](#change-overlays)
- [Normalization](#normalization)
- [Templates](#templates)
- [Completion checks](#completion-checks)

## Governing model

Maintain the development documents as authoritative, recursively decomposable descriptions of the complete intended current project.

Use these distinct responsibilities:

```text
SPEC      What components, behavior, and contracts constitute the final system?
PLAN      In what testable capability slices and dependency order is it built?
LAYOUT    Where do implementation, tests, documentation, and artifacts physically live?
ROADMAP   Which PLAN boundaries are durably complete?
```

Do not force the four views into identical trees. Align them through explicit routing and shared terminology.

Treat docstrings, API documentation comments, and source-adjacent explanatory comments as implementation-owned in-code documentation governed by `in-code-documentation.md`, not as additional SPEC or PLAN nodes. Authoritative development documents define intended contracts; in-code documentation presents the implemented current contract beside its code. Reconcile both when a change affects their shared subject without duplicating full requirements into source comments.

Do not write a chronological account of feature additions, reversals, or migrations into the main documents. A reader must be able to reconstruct the current project without conversation history, old proposals, temporary change files, the implementation journal, or Git history.

## Before authoring

1. Read `lifecycle.md` and confirm document work is authorized.
2. Consolidate accepted exploration decisions.
3. Separate accepted requirements from assumptions, open questions, and discarded alternatives.
4. Identify unresolved issues that materially affect scope, architecture, public contracts, persistent formats, acceptance, or implementation order.
5. Resolve blockers with the user or represent intentionally deferred matters explicitly.
6. For an existing project, read `project-discovery.md` and inspect relevant documents, code, tests, and project instructions.
7. Determine whether the request creates main documents, revises them, or creates a temporary change overlay.

Do not invent decisions to make documents appear complete.

## Recursive document architecture

Treat every document as a node in a hierarchy. A parent node must define:

- its scope and abstraction level;
- its children and their precise responsibilities;
- boundaries between children;
- contracts, dependencies, and shared invariants connecting them;
- where each normative subject is canonically defined.

A child must add detail within its assigned scope. It must not silently broaden responsibility or repeat requirements owned elsewhere.

Keep a node as one file while it remains focused, navigable, and economical to load. Split it when distinct responsibilities have substantial independent detail or routine work repeatedly requires unrelated context.

When splitting a node:

1. inventory all normative content;
2. assign every item one canonical destination;
3. turn the original file into an orienting parent;
4. define each child's scope and relationships;
5. update incoming and outgoing references;
6. remove normative duplication;
7. verify ordinary work requires the root plus only a small focused subset.

Use stable semantic names such as `rules-engine.md`, `archive-streams.md`, or `frontends/cli.md`. Avoid ordinal or opaque names such as `spec-3.md`, `phase-2.md`, or arbitrary requirement-code files.

## SPEC tree

### Responsibility

Define the system that shall exist:

- purpose, complete scope, and non-goals;
- system context and principal use cases;
- terminology and system-wide invariants;
- architectural decomposition;
- component responsibilities and boundaries;
- public and internal contracts;
- interfaces and external protocols;
- data and persistent formats;
- dependency constraints;
- required behavior and error semantics;
- boundary cases;
- objective acceptance conditions.

### Root requirements

Keep `docs/dev/SPEC.md` compact but substantive. It must orient a human or agent without requiring an initial traversal of every child.

Include at the appropriate level:

- project purpose and scope;
- principal architecture;
- top-level contracts and invariants;
- dependency direction;
- a scope map of child specifications;
- system-level acceptance.

### Decomposition boundaries

Normally split by cohesive:

- component;
- public interface;
- external protocol;
- persistent representation;
- independently understandable behavioral contract.

Place detailed behavior in the lowest appropriate child. Keep broad guarantees and inter-component relationships in parents.

Do not duplicate a child's detailed requirements in its parent. Link to the canonical child and state only the broader guarantee needed at the parent's level.

### Acceptance

Write acceptance conditions as observable outcomes. Cover successful behavior, important boundaries, failure semantics, and cross-component guarantees. Do not substitute implementation tasks for behavioral acceptance.

## PLAN tree

### Responsibility

Define how to construct the complete specified system from scratch in bounded, dependency-ordered, testable increments.

The PLAN is an executable blueprint, not a progress diary. Preserve tasks necessary to construct the current system; remove abandoned approaches and obsolete migration history.

### Root requirements

Keep `docs/dev/PLAN.md` as a substantive implementation map containing:

- governing specification;
- implementation strategy;
- named top-level phases and order;
- milestone boundaries;
- inter-phase and component dependencies;
- SPEC-to-PLAN routing;
- project-wide verification and completion conditions.

### Hierarchy

Use:

```text
PLAN
└── phases
    └── milestones
        └── task transactions
```

- A **phase** delivers a major independently meaningful project capability.
- A **milestone** provides a coherent review, handoff, or stopping boundary within a phase.
- A **task** is the smallest recoverable independently verifiable implementation transaction.

Use semantic names. Declare order in the parent so phases and milestones can be inserted or reordered without renaming files.

### MVP rule

Make the first phase the smallest useful testable MVP or prototype with as little code as reasonably possible. Make later phases the smallest meaningful independently verifiable increments.

### Task contract

Each task must state:

- objective and delivered increment;
- SPEC nodes and contracts implemented;
- prerequisites;
- anticipated paths or affected components when knowable;
- ordered implementation work;
- direct unit verification;
- dependent-component verification;
- integration verification;
- boundary verification when completing a milestone or phase;
- objective completion conditions.

An ordinary task should modify one production file plus associated tests and directly affected documentation. Do not force a one-file boundary when an atomic contract change spans inseparable artifacts.

### Milestone and phase verification

Define explicit exit checks for every milestone and phase. A milestone is more than a task grouping: it must deliver a reviewable integrated capability. A phase must deliver its named major capability without relying on later phases to become internally coherent.

## LAYOUT tree

### Responsibility

Define final physical ownership:

- repository-root files and major directories;
- responsibility of important locations;
- implementation, test, documentation, fixture, and asset ownership;
- import and dependency constraints enforced by placement;
- generated, build, installation, and runtime artifacts;
- packaging and installed behavior;
- cross-tree routing;
- layout evolution rules.

### Root requirements

Keep `docs/dev/layout.md` as a compact physical architecture entry point. Include:

1. purpose and authority;
2. concise repository overview;
3. child layout nodes and exact scopes;
4. cross-tree relationships;
5. global physical invariants;
6. change and refactoring rules.

### Decomposition

Split by physical ownership domain, not PLAN phase and not mechanically by SPEC component. Common domains may include:

```text
layout/
├── repository.md
├── docs.md
├── src.md
├── tests.md
└── packaging-runtime.md
```

Adapt names to the actual project. Keep documentation, production source, and tests separate when each has substantial independent structure. Do not turn `repository.md` into a catch-all.

Group cohesive source-to-build-to-runtime concerns until they become broad enough for recursive decomposition.

## Other shared documents

Create a shared document beside SPEC, PLAN, and LAYOUT only when it has a clear canonical responsibility not naturally owned by those trees.

Examples may include:

- `PROJECT.md` for project-wide operating constraints;
- a shared glossary when terminology is too substantial for the SPEC root;
- a focused conventions document used across architecture and planning.

Do not create miscellaneous overflow documents merely to reduce another file's size.

Apply the same rules to every shared document:

- define authority and scope;
- keep each normative fact in one place;
- route rather than duplicate;
- decompose by coherent responsibility;
- retain a useful root.

## Cross-tree alignment

Maintain alignment without duplication:

| Question | Canonical owner |
|---|---|
| Required behavior and contracts | SPEC |
| Construction order and task verification | PLAN |
| Physical location and ownership | LAYOUT |
| Durable progress | ROADMAP |
| Current component-to-check routing | Verification map |

Provide concise routing where useful:

| Architectural area | SPEC owner | Physical owner | Test owner | Principal PLAN phase |
|---|---|---|---|---|
| `<area>` | `spec/<node>.md` | source package | test location | `plan/<phase>.md` |

Keep this navigational. Do not restate detailed contracts or task procedures in the routing table.

When one tree changes, update only affected information in the others:

- a behavioral change normally updates a focused SPEC leaf and affected PLAN tasks;
- a physical move normally updates LAYOUT and PLAN paths, not behavioral requirements;
- a phase reorder normally updates PLAN and ROADMAP, not component contracts;
- a changed test owner updates LAYOUT and the verification map.

## Dependencies and contract revision

Model component dependencies as a directed acyclic graph. Use `A → B` to mean B depends on A.

- Begin maximal paths at dependency-free components.
- End them at components with no dependents.
- Permit reconvergent and diamond structures.
- Prohibit direct and transitive cycles.
- When components require mutual dependency, combine them or extract a lower-level contract both can depend on.

Implement and revise in dependency order from unaffected dependencies toward dependents.

For an established breaking contract, use expand–migrate–contract when necessary:

1. expand by adding the new contract while temporarily preserving compatibility;
2. migrate dependents through bounded tasks in dependency order;
3. contract by removing the obsolete contract after no dependent uses it.

Require every intermediate task to leave the project internally consistent and testable.

## Review and correction

After producing documents, remain in review and revision mode until implementation is explicitly requested.

For every accepted correction:

1. identify the canonical owner;
2. update affected leaf detail;
3. update parent scope, contract, invariant, or navigation only when necessary;
4. update affected PLAN tasks and verification;
5. update LAYOUT when physical ownership changes;
6. update ROADMAP structure when PLAN structure changes;
7. update the verification map only for implemented current paths;
8. remove superseded statements;
9. recheck dependencies and acceptance.

Changes should normally become smaller toward roots. Do not append a contradictory “revision” section beneath obsolete text.

## Change overlays

Use temporary change documents for a substantial additive, subtractive, corrective, or architectural delta when they improve review and bounded execution.

Under the current convention, use:

```text
docs/dev/FEATURE-SPEC.md
docs/dev/FEATURE-PLAN.md
```

Treat their role as a generic change overlay even when the change is not an additive feature.

The change specification must state:

- change kind and objective;
- affected baseline contracts;
- final intended behavior;
- explicit non-goals;
- compatibility or migration consequences;
- acceptance conditions.

The change plan must state:

- affected main nodes;
- dependency order;
- bounded implementation tasks;
- intermediate compatibility requirements;
- integration and normalization task;
- affected-scope verification.

If exactly one change document exists, stop and ask. If an overlay conflicts with the main baseline without explicitly defining the revision, stop and resolve the ambiguity.

## Normalization

At change completion:

1. integrate settled final behavior into canonical SPEC nodes;
2. integrate direct from-scratch construction into PLAN nodes;
3. update LAYOUT, ROADMAP, and verification routing;
4. remove superseded baseline content;
5. remove add-then-remove or migration-only history from the main PLAN;
6. delete temporary change documents;
7. verify that the project is comprehensible without the overlay or journal.

Preserve historical evidence only in the append-only journal and Git history when available. Retain migration or compatibility history in current documents only when released consumers still require it.

## Templates

Use these assets as starting structures, then adapt them to the actual project:

- `../assets/templates/SPEC.md`
- `../assets/templates/PLAN.md`
- `../assets/templates/layout.md`

Do not copy headings mechanically when a section is irrelevant. Do not omit a required responsibility merely because the template expresses it differently from the project.

## Completion checks

Before reporting document work complete, confirm:

- every accepted requirement has one canonical owner;
- unresolved material decisions are explicit;
- roots provide orientation and routing;
- children stay within assigned scope;
- SPEC describes the complete intended system;
- PLAN builds that system directly from scratch;
- PLAN includes phases, milestones, bounded tasks, and verification;
- LAYOUT describes final physical ownership;
- dependency direction is acyclic;
- ROADMAP can be derived exactly from PLAN;
- current progress remains in ROADMAP, journal, recovery, and Git evidence rather than a PLAN status section;
- verification intent is sufficient to build the current verification map as implementation proceeds;
- superseded and chronological residue is removed;
- no implementation has begun without separate authorization.
