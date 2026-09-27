# `sdd-man` Implementation Plan

## 1. Objective

Implement the complete `sdd-man` skill specified by `sdd-man-SPEC.md` as a modular, progressively disclosed Specification-Driven Development system.

The completed skill shall:

- route exploration, inspection, document authoring, review, implementation, recovery, checkpoint steering, and progress reporting;
- enforce explicit authorization at mutation and continuation boundaries;
- define the authoritative SPEC, PLAN, LAYOUT, ROADMAP, verification-map, journal, and recovery-state relationships;
- support greenfield, feature, corrective, subtractive, and architectural work;
- support Git and non-Git projects;
- preserve deterministic recovery of interrupted task transactions;
- support bounded human-directed execution through tasks, milestones, and phases;
- require capability-oriented completion reporting;
- remain usable without bundled scripts.

This PLAN describes construction of the skill itself. It does not authorize implementation.

## 2. Governing specification

The canonical specification is:

```text
sdd-man-SPEC.md
```

Every task in this PLAN shall be checked against the relevant specification sections before implementation and again during task verification.

The implementation shall not silently resolve a conflict or omission by inventing behavior. A material specification issue discovered during implementation shall return to specification review before affected work proceeds.

## 3. Implementation strategy

### 3.1 Baseline delivery

The baseline skill will be implemented as a concise orchestration entry point plus focused workflow references and reusable project templates.

No bundled executable helper is planned for the baseline. The workflows can be performed using agent reasoning and ordinary host tools, while the specification explicitly makes scripts optional.

A helper may be proposed only if implementation or forward-testing demonstrates a repeated operation with:

- precise inputs and outputs;
- mechanically decidable preconditions;
- deterministic behavior;
- clear refusal semantics;
- a material safety, repeatability, or context-efficiency benefit.

Adding such a helper requires an explicit SPEC and PLAN revision before implementation. It shall not be added opportunistically inside another task.

### 3.2 Progressive-disclosure strategy

`SKILL.md` will contain only:

- discovery metadata;
- workflow classification;
- mutation and transition gates;
- reference-routing rules;
- compact universal safety rules;
- completion conditions.

Detailed procedures will live in directly referenced Markdown resources. No workflow reference will require another reference in order to discover a mandatory rule; `SKILL.md` will link every required reference directly.

### 3.3 Construction order

Implementation proceeds in this dependency order:

```text
package foundation
    ↓
lifecycle and discovery
    ↓
document system
    ↓
roadmap and verification routing
    ↓
transactional implementation and recovery
    ↓
checkpoint steering and reporting
    ↓
integrated validation and forward-testing
    ↓
final skill validation and installation
```

### 3.4 Verification model

Each task shall receive:

1. focused content review against its SPEC sections;
2. path and reference validation for its changed file;
3. relevant scenario inspection;
4. regression checks for previously completed routing and contracts.

Each milestone adds integrated verification. Each phase adds broader acceptance verification. Final completion requires the complete acceptance matrix.

## 4. Final package layout

The baseline implementation shall produce:

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
└── assets/
    └── templates/
        ├── SPEC.md
        ├── PLAN.md
        ├── layout.md
        ├── ROADMAP.md
        └── verification-map.json
```

The final baseline shall not contain:

```text
scripts/
README.md
CHANGELOG.md
INSTALLATION_GUIDE.md
QUICK_REFERENCE.md
placeholder examples
unused schemas
temporary forward-test projects
generated caches
```

`agents/openai.yaml` is host presentation metadata. The runtime workflow shall remain independent of it.

## 5. Resource responsibility map

| Resource | Canonical responsibility |
|---|---|
| `SKILL.md` | Activation, workflow selection, authorization gates, routing, universal completion rules |
| `references/lifecycle.md` | Conversation modes, transitions, authority, continuity, and workflow composition |
| `references/exploration.md` | Problem exploration, decision discipline, prototypes, and readiness for specification |
| `references/project-discovery.md` | Root, instruction, document, Git, state, and project-capability discovery |
| `references/document-system.md` | SPEC/PLAN/LAYOUT generation, decomposition, ownership, review, and normalization |
| `references/roadmap.md` | PLAN-derived roadmap generation, status semantics, reconciliation, and bounded selection |
| `references/verification.md` | Test strategy, verification-map contract, impact selection, failure classification, and boundary checks |
| `references/implementation.md` | Campaign selection, task preflight, preparation, execution, completion, Git/non-Git closure |
| `references/recovery.md` | Startup recovery, state-specific restoration, evidence preservation, and escalation |
| `references/checkpoint-steering.md` | HIL checkpoints, impact classification, focused revision, normalization, and paused handoff |
| `references/reporting.md` | Task, milestone, phase, campaign, steering, and progress reporting contracts |
| `assets/templates/SPEC.md` | Reusable root SPEC structure |
| `assets/templates/PLAN.md` | Reusable root PLAN structure with phases, milestones, tasks, and verification |
| `assets/templates/layout.md` | Reusable root LAYOUT structure and physical-ownership routing |
| `assets/templates/ROADMAP.md` | Reusable PLAN-aligned progress checklist structure |
| `assets/templates/verification-map.json` | Minimal machine-readable component-to-verification structure |

No resource shall become a miscellaneous overflow file. If a responsibility does not fit this map during implementation, revise the architecture before placing it.

## 6. Specification coverage map

| SPEC area | Primary implementation resources |
|---|---|
| Purpose, principles, non-goals | `SKILL.md`, `lifecycle.md` |
| Compatibility and modularity | `SKILL.md`, package layout, final validation |
| Conversation lifecycle | `lifecycle.md`, `SKILL.md` |
| Authority and precedence | `lifecycle.md`, `project-discovery.md`, `document-system.md` |
| Startup discovery | `project-discovery.md`, `recovery.md` |
| Exploration | `exploration.md` |
| SPEC/PLAN/LAYOUT | `document-system.md`, three document templates |
| Dependencies and incremental revision | `document-system.md`, `implementation.md`, `checkpoint-steering.md` |
| ROADMAP | `roadmap.md`, `ROADMAP.md` template |
| Verification map and test selection | `verification.md`, `verification-map.json` template |
| Campaigns and bounded execution | `implementation.md`, `roadmap.md`, `lifecycle.md` |
| Task transaction | `implementation.md`, `recovery.md` |
| Recovery | `recovery.md`, `project-discovery.md` |
| Test failure handling | `verification.md`, `implementation.md` |
| HIL checkpoints | `checkpoint-steering.md`, `lifecycle.md`, `roadmap.md` |
| Completion reporting | `reporting.md`, `implementation.md`, `checkpoint-steering.md` |
| Journal contract | `implementation.md`, `recovery.md`, `reporting.md` |
| Acceptance and completion | all resources, final conformance phase |

## 7. Phase overview

| Order | Phase | Milestones | Tasks | Delivered capability |
|---:|---|---:|---:|---|
| 1 | Routable lifecycle core | 2 | 5 | Installable skill skeleton with safe mode selection, exploration, and project discovery |
| 2 | Authoritative document complex | 3 | 8 | SPEC/PLAN/LAYOUT authoring plus ROADMAP and verification-map workflows and templates |
| 3 | Transactional implementation and recovery | 2 | 3 | Campaign execution, recoverable task transactions, Git/non-Git closure, and deterministic resumption rules |
| 4 | Human steering and completion communication | 2 | 3 | Bounded HIL checkpoints, normalization, and capability-oriented reporting |
| 5 | Integrated conformance and release | 3 | 5 | Cross-resource consistency, representative forward-testing, final validation, and installed skill |
| **Total** |  | **12** | **24** | Complete `sdd-man` skill |

## 8. Phase 1 — Routable lifecycle core

### 8.1 Capability

Deliver an installable skill skeleton whose entry point can distinguish conversational workflows, enforce authorization gates, and route exploration and project inspection to focused references.

### 8.2 Dependencies

None beyond the governing specification and the installed skill-creation tooling.

### 8.3 Milestone: Package foundation

#### Task 1.1 — Initialize the skill package

**Objective**

Create the canonical personal-skill directory and only the resource directories required by the baseline design.

**SPEC coverage**

- §5 Compatibility contract
- §6 Skill package architecture
- §27 Completion criteria

**Paths**

```text
sdd-man/SKILL.md
sdd-man/agents/openai.yaml
sdd-man/references/
sdd-man/assets/
sdd-man/assets/templates/
```

**Implementation work**

1. Initialize `sdd-man` with the canonical skill initializer in the personal-skills checkout.
2. Request only `references` and `assets`; do not create `scripts`.
3. Provide initial UI metadata values suitable for later regeneration.
4. Remove every generated placeholder resource not used by the plan.
5. Confirm that no auxiliary README or installation guide was created.

**Verification**

- Confirm `SKILL.md` and `agents/openai.yaml` exist.
- Confirm `references/` and `assets/templates/` exist.
- Confirm `scripts/` is absent.
- Confirm no placeholder files remain.
- Run the structural skill validator; frontmatter may remain provisional but must parse.

**Completion condition**

The package exists at the required location with only the planned baseline topology.

#### Task 1.2 — Implement the lifecycle and authority reference

**Objective**

Define the universal conversation state machine, authorization boundaries, authority hierarchy, continuity rules, and workflow transitions.

**SPEC coverage**

- §2 Design principles
- §8 Conversation lifecycle
- §9 Authority and precedence model
- §16 Campaign model at routing level

**Path**

```text
sdd-man/references/lifecycle.md
```

**Implementation work**

1. Define all supported modes and entry conditions.
2. Define explicit mutation and continuation gates.
3. Define direct entry into later modes when adequate artifacts exist.
4. Define authority precedence and unresolved-conflict behavior.
5. Define conversation continuity and decision discipline.
6. Define the relationship between a completed requested range and `awaiting-steering`.
7. Include a compact table of which other reference applies to each mode without making those links the sole discovery path.

**Verification**

- Trace every lifecycle transition in SPEC §8 to an explicit rule.
- Confirm exploration does not authorize document creation.
- Confirm document creation does not authorize implementation.
- Confirm checkpoint completion does not authorize continuation.
- Confirm conflict handling stops rather than guesses.

**Completion condition**

All modes, transitions, and authority rules have one coherent canonical definition.

#### Task 1.3 — Implement the exploration reference

**Objective**

Define the exploratory conversation workflow and its boundary with specification and implementation.

**SPEC coverage**

- §8 Conversation lifecycle
- §11 Exploration workflow
- §26.1 Exploration without mutation

**Path**

```text
sdd-man/references/exploration.md
```

**Implementation work**

1. Define problem framing, vocabulary, constraints, non-goals, alternatives, and tradeoffs.
2. Require classification of facts, decisions, assumptions, open questions, and discarded alternatives.
3. Define contradiction and weak-boundary handling.
4. Define decision-state summaries and readiness assessment.
5. Define disposable experiment versus project-change classification.
6. Prohibit silent conversion of exploratory work into a project baseline.

**Verification**

- Review the reference against SPEC §11 line by line.
- Walk through an ambiguous project idea and confirm no file mutation is authorized.
- Walk through a requested prototype and confirm it is classified before mutation.

**Completion condition**

Exploration can converge on an accepted design without prematurely creating authoritative artifacts or implementation state.

### 8.4 Milestone: Discovery and entry-point routing

#### Task 1.4 — Implement the project-discovery reference

**Objective**

Define read-only discovery of project roots, authorities, documents, repository state, tools, and active SDD state.

**SPEC coverage**

- §9 Authority and precedence model
- §10 Project discovery and startup inspection
- §19 Recovery protocol at discovery level

**Path**

```text
sdd-man/references/project-discovery.md
```

**Implementation work**

1. Define project-root and Git-root discovery.
2. Define discovery of `AGENTS.md`, nested instruction scopes, `PROJECT.md`, and referenced guidance.
3. Define main and active-change document discovery.
4. Define journal, recovery, roadmap, and verification-map inspection.
5. Define Git worktree/index inspection without mutation.
6. Define project tool and verification-command discovery.
7. Define the complete state-classification set.
8. Separate status reporting from repair authorization.

**Verification**

- Check every discovery item in SPEC §10.
- Verify nested instruction scope is evaluated per anticipated target.
- Verify non-Git projects remain supported.
- Verify inconsistent state is classified rather than repaired automatically.

**Completion condition**

An agent can determine what governs the project and its current state before selecting or modifying work.

#### Task 1.5 — Implement the initial `SKILL.md` router

**Objective**

Create the compact skill entry point with final triggering metadata, workflow classification, universal gates, and direct reference routing.

**SPEC coverage**

- §5 Skill compatibility
- §6 Skill package architecture
- §7 `SKILL.md` orchestration contract
- §8 Conversation lifecycle

**Paths**

```text
sdd-man/SKILL.md
sdd-man/agents/openai.yaml
```

**Implementation work**

1. Write final `name` and comprehensive activation `description` frontmatter.
2. Keep frontmatter limited to `name` and `description`.
3. Add workflow classification and authorization rules.
4. Link `lifecycle.md`, `exploration.md`, and `project-discovery.md` directly.
5. Add reserved routing entries for later reference files without duplicating their future content.
6. State that scripts are optional and absent in the baseline.
7. Define universal stop/escalation and truthful-status rules.
8. Regenerate `agents/openai.yaml` from the current skill interface.

**Verification**

- Run structural skill validation.
- Confirm every current reference is directly linked.
- Confirm `SKILL.md` remains an orchestrator rather than a manual.
- Confirm all “when to use” trigger information is present in the description.
- Confirm UI metadata matches the skill's actual purpose.

**Completion condition**

The skill activates for intended SDD requests and safely routes lifecycle, exploration, and inspection workflows.

### 8.5 Phase verification

- Run structural validation of the package.
- Verify all links in `SKILL.md` resolve.
- Exercise three read-only scenarios: exploration, status inspection, and ambiguous mutation request.
- Confirm no scenario requires a missing future reference before the route explicitly reaches that workflow.
- Confirm the package contains no scripts or unused placeholders.

### 8.6 Phase completion condition

The skill is structurally valid and can safely classify and route early-lifecycle requests without authorizing unintended mutation.

## 9. Phase 2 — Authoritative document complex

### 9.1 Capability

Deliver the complete document-authoring, recursive decomposition, PLAN-aligned roadmap, and component-to-verification mapping system with reusable project templates.

### 9.2 Dependencies

- Phase 1 lifecycle and authority rules.
- Accepted `sdd-man` SPEC document model.

### 9.3 Milestone: SPEC, PLAN, and LAYOUT system

#### Task 2.1 — Implement the development-document reference

**Objective**

Define generation, recursive decomposition, ownership, review, revision, dependency modeling, and normalization for SPEC, PLAN, LAYOUT, and shared documents.

**SPEC coverage**

- §12 Development-document system
- §13 Dependency and revision model
- §16 Change-campaign integration at document level
- §21.5 Normalization

**Path**

```text
sdd-man/references/document-system.md
```

**Implementation work**

1. Define complete-current-state documentation.
2. Define root orientation requirements.
3. Define recursive parent and child responsibilities.
4. Define canonical ownership and anti-duplication rules.
5. Define SPEC responsibilities and decomposition boundaries.
6. Define PLAN phases, milestones, tasks, and verification responsibilities.
7. Define LAYOUT physical-ownership responsibilities and decomposition.
8. Define other shared-document admission criteria.
9. Define DAG notation, cycle handling, and expand–migrate–contract.
10. Define review, correction propagation, and obsolete-content removal.
11. Define integration and normalization of temporary change documents.

**Verification**

- Trace all requirements in SPEC §§12–13.
- Confirm SPEC, PLAN, and LAYOUT are aligned but not required to share identical trees.
- Confirm milestones are canonically owned by PLAN.
- Confirm temporary changes disappear from final current-state documents.
- Confirm roots remain useful orientation nodes rather than link-only indexes.

**Completion condition**

The skill has one coherent normative workflow for creating and evolving the complete development-document complex.

#### Task 2.2 — Create the root SPEC template

**Objective**

Provide a reusable, architecture-neutral starting structure for a project root specification.

**SPEC coverage**

- §12.2 Recursive decomposition
- §12.3 SPEC tree

**Path**

```text
sdd-man/assets/templates/SPEC.md
```

**Implementation work**

The template shall provide adaptable sections for:

- purpose and scope;
- non-goals;
- system context and use cases;
- terminology and invariants;
- architecture and component boundaries;
- contracts and dependency constraints;
- child-specification routing;
- system acceptance conditions.

Template instructions shall be concise and removable. The template shall not impose a particular technology or architecture.

**Verification**

- Instantiate the template conceptually for a single-component and a multi-component project.
- Confirm it remains useful with no child specifications.
- Confirm it can route to children without duplicating their details.

**Completion condition**

The template supports both compact and decomposed specifications while preserving root-level orientation.

#### Task 2.3 — Create the root PLAN template

**Objective**

Provide a reusable complete-project implementation-plan structure with phases, milestones, bounded tasks, traceability, and verification.

**SPEC coverage**

- §12.2 Recursive decomposition
- §12.4 PLAN tree
- §13 Dependency and revision model
- §17 Bounded implementation selection

**Path**

```text
sdd-man/assets/templates/PLAN.md
```

**Implementation work**

The template shall provide adaptable sections for:

- objective and governing specification;
- implementation strategy;
- dependency order;
- phase overview;
- milestone definitions;
- task objective, scope, paths, verification, and completion conditions;
- phase and campaign acceptance.

It shall use semantic phase and task names rather than opaque requirement identifiers.

**Verification**

- Confirm the template can express an MVP-first sequence.
- Confirm milestones are review and stopping boundaries.
- Confirm task verification distinguishes direct, dependent, integration, and boundary checks.
- Confirm the root can delegate detailed phases to child plans.

**Completion condition**

The template can describe construction of a complete project in bounded, dependency-ordered, independently verifiable increments.

#### Task 2.4 — Create the root LAYOUT template

**Objective**

Provide a reusable root physical-ownership document that can remain compact or route to recursively decomposed layout children.

**SPEC coverage**

- §12.2 Recursive decomposition
- §12.5 LAYOUT tree

**Path**

```text
sdd-man/assets/templates/layout.md
```

**Implementation work**

The template shall provide adaptable sections for:

- purpose and authority;
- concise repository tree;
- physical ownership domains;
- cross-tree routing;
- dependency and import boundaries;
- tests and fixtures;
- packaging, generated, installation, and runtime artifacts;
- layout evolution rules.

**Verification**

- Confirm docs, production source, and tests can be separate child domains.
- Confirm the template does not force LAYOUT to mirror SPEC or PLAN.
- Confirm common tasks can route through the root to one focused child.

**Completion condition**

The template provides a canonical, architecture-neutral physical project map.

### 9.4 Milestone: PLAN-aligned roadmap

#### Task 2.5 — Implement the roadmap reference

**Objective**

Define roadmap derivation, checklist semantics, startup reconciliation, bounded selection, and update ordering.

**SPEC coverage**

- §14 Roadmap contract
- §17 Bounded implementation selection
- §21 Human-in-the-loop checkpoints at progress level

**Path**

```text
sdd-man/references/roadmap.md
```

**Implementation work**

1. Establish PLAN as canonical owner and ROADMAP as derived projection.
2. Define exact one-to-one task correspondence and order preservation.
3. Define binary durable checklist semantics.
4. Define milestone and phase roll-up conditions.
5. Define summary counts and links to PLAN anchors.
6. Define startup reconciliation against journal and Git.
7. Define “next N tasks,” milestone, phase, named boundary, and MVP selection.
8. Define roadmap mutation inside the completing task transaction.
9. Define mismatch escalation and normalization after PLAN revision.

**Verification**

- Walk through a partially completed milestone.
- Walk through a completed but uncommitted task.
- Walk through a removed PLAN task after checkpoint steering.
- Confirm active and blocked states remain outside ROADMAP.

**Completion condition**

ROADMAP can serve as a reliable human control surface without becoming an independent plan or transaction ledger.

#### Task 2.6 — Create the ROADMAP template

**Objective**

Provide a compact reusable checklist that mirrors phases, milestones, and tasks and explains its authority.

**SPEC coverage**

- §14 Roadmap contract

**Path**

```text
sdd-man/assets/templates/ROADMAP.md
```

**Implementation work**

The template shall include:

- authority statement;
- progress summary table;
- nested phase, milestone, and task checklists;
- PLAN-link placeholders;
- binary status semantics;
- concise reconciliation note.

It shall not contain implementation instructions already owned by PLAN.

**Verification**

- Instantiate a model with two phases, three milestones, and several tasks.
- Confirm counts can be calculated directly.
- Confirm every checklist item can link to one PLAN anchor.
- Confirm no transient status vocabulary is required.

**Completion condition**

The template is compact, auditable, and incapable of silently adding plan scope.

### 9.5 Milestone: Verification routing

#### Task 2.7 — Implement the verification reference

**Objective**

Define test strategy, verification-map maintenance, impact-based check selection, failure classification, and boundary verification.

**SPEC coverage**

- §15 Verification-map contract
- §18.7 Verification and completion
- §20 Testing and failure handling

**Path**

```text
sdd-man/references/verification.md
```

**Implementation work**

1. Define tests derived from behavior, invariants, errors, and acceptance conditions.
2. Define component-level, dependent, integration, milestone, phase, and campaign verification.
3. Define verification-map authority and granularity.
4. Define reusable command-array targets.
5. Define current-state incremental maintenance.
6. Define impact-selection ordering and deduplication.
7. Define import analysis and test collection as evidence rather than proof.
8. Define task-caused, unrelated, and pre-existing failure handling.
9. Define defect classification and prohibited test weakening.

**Verification**

- Trace SPEC §§15 and 20 completely.
- Exercise a component with direct and shared integration tests.
- Exercise an unrelated failing test.
- Confirm PLAN-required checks cannot be omitted because the map lacks them.

**Completion condition**

The skill can identify an appropriate minimum verification set without mistaking a registry for coverage proof.

#### Task 2.8 — Create the verification-map template

**Objective**

Provide the minimal machine-readable structure for component ownership and reusable verification targets.

**SPEC coverage**

- §15 Verification-map contract

**Path**

```text
sdd-man/assets/templates/verification-map.json
```

**Implementation work**

1. Define `schema_version`.
2. Define semantic component identifiers and owned paths.
3. Define normalized verification targets.
4. Represent commands as argument arrays.
5. Demonstrate one target shared by multiple components without duplication.
6. Keep the file valid JSON without comments or placeholder syntax that prevents parsing.

**Verification**

- Parse with Python's standard `json` module.
- Verify all sample component target references resolve.
- Verify all commands are arrays of nonempty strings.
- Confirm the template does not enumerate volatile individual test node IDs.

**Completion condition**

The template is valid JSON and demonstrates the complete minimum registry contract without imposing a test framework.

### 9.6 Phase verification

- Confirm `document-system.md`, `roadmap.md`, and `verification.md` have distinct canonical responsibilities.
- Confirm all five templates are referenced from the applicable workflow reference and `SKILL.md` routing.
- Confirm PLAN owns milestones and ROADMAP merely mirrors them.
- Confirm the verification map describes implemented current paths while PLAN owns future test intent.
- Run JSON parsing on the verification-map template.
- Perform a document-generation walkthrough for both a compact and recursively decomposed project.
- Run structural skill validation after adding all resources.

### 9.7 Phase completion condition

The skill can generate, review, navigate, and keep aligned the complete authoritative document complex and its two derived operational views.

## 10. Phase 3 — Transactional implementation and recovery

### 10.1 Capability

Deliver safe initial and change campaigns, one-task-at-a-time recoverable execution, explicit Git/non-Git closure, and deterministic startup recovery rules.

### 10.2 Dependencies

- Phase 1 lifecycle and discovery.
- Phase 2 PLAN, ROADMAP, LAYOUT, and verification contracts.

### 10.3 Milestone: Recoverable task execution

#### Task 3.1 — Implement the implementation reference

**Objective**

Define campaign selection, bounded work selection, task preflight, state transitions, manifest preparation, scope extension, implementation, verification, and durable closure.

**SPEC coverage**

- §16 Campaign model
- §17 Bounded implementation selection
- §18 Task transaction protocol
- §20 Testing and failure handling
- §23 Journal contract except recovery-specific interpretation

**Path**

```text
sdd-man/references/implementation.md
```

**Implementation work**

1. Define initial, change, and existing-campaign selection.
2. Define baseline plus explicit-delta semantics.
3. Define bounded HIL range resolution.
4. Define one-task-at-a-time execution.
5. Define preflight, target-operation classification, and dirty-path handling.
6. Define `STARTED` and `PREPARED` ordering.
7. Define manifest fields, backup rules, hashing, metadata, symlink, create, delete, and rename behavior.
8. Define declared scope extension.
9. Define implementation constraints and documentation synchronization.
10. Define verification order and failure repair.
11. Define ROADMAP and verification-map update timing.
12. Define `COMPLETED`, capability summaries, Git closure, non-Git closure, and cleanup.
13. Define phase and campaign integration.
14. Define journal record requirements and prohibited operations.

**Verification**

- Trace SPEC §§16–18 and §23.
- Walk through modify, create, delete, and rename operations.
- Walk through scope extension before and after an accidental undeclared edit.
- Confirm unrelated dirty changes are preserved and never staged.
- Confirm no new task begins before durable completion and cleanup.
- Confirm Git publication or history rewriting requires separate authorization.

**Completion condition**

The implementation workflow describes every state transition and mutation boundary needed for a safely recoverable task.

### 10.4 Milestone: Recovery and evidence preservation

#### Task 3.2 — Implement the recovery reference

**Objective**

Define startup-first recovery, exact restoration, completed-task reconciliation, corruption handling, and escalation.

**SPEC coverage**

- §10 Project discovery and startup inspection
- §18 Task states
- §19 Recovery protocol
- §23 Journal contract
- §26.7–26.9 Recovery acceptance scenarios

**Path**

```text
sdd-man/references/recovery.md
```

**Implementation work**

1. Make recovery inspection precede task selection.
2. Define no-active-task and previously reverted behavior.
3. Define `STARTED` without `PREPARED` handling.
4. Define all-or-nothing restoration for `PREPARED` without `COMPLETED`.
5. Define `COMPLETED` reconciliation in Git.
6. Define `COMPLETED` reconciliation without Git.
7. Define committed-without-completion protocol violation handling.
8. Define truncated final journal record handling.
9. Define unexpected backup and multi-active-task escalation.
10. Define evidence preservation and prohibited destructive recovery.

**Verification**

- Build decision tables for every recognized state.
- Verify every branch ends in proceed, restart, restore, preserve-and-ask, or clean.
- Confirm no branch guesses ownership or baseline.
- Confirm completed committed work is never automatically reverted.
- Confirm non-Git recovery is fully specified.

**Completion condition**

Every expected interruption state has one deterministic safe response and every ambiguous state preserves evidence for user direction.

#### Task 3.3 — Integrate implementation and recovery routing

**Objective**

Connect implementation, recovery, roadmap, verification, and project discovery without duplicating their detailed rules.

**SPEC coverage**

- §7 `SKILL.md` orchestration
- §8 Conversation lifecycle
- §10 Startup inspection
- §18–§20 implementation, recovery, and testing

**Paths**

```text
sdd-man/SKILL.md
sdd-man/references/lifecycle.md
sdd-man/references/project-discovery.md
```

**Implementation work**

1. Finalize implementation and recovery routing in `SKILL.md`.
2. Require startup recovery before new task selection.
3. Route test-impact selection to `verification.md`.
4. Route bounded selection and progress updates to `roadmap.md`.
5. Ensure lifecycle rules distinguish implementation, recovery, and status inspection.
6. Remove any temporary duplication introduced before the dedicated references existed.

**Verification**

- Follow all links for “implement,” “resume,” “recover,” and “status.”
- Confirm an implementation request cannot bypass recovery.
- Confirm status inspection remains read-only.
- Confirm the universal entry point stays concise.

**Completion condition**

The complete transactional workflow is reachable from `SKILL.md` with no conflicting or duplicated state-machine definition.

### 10.5 Phase verification

Use disposable representative project states to walk through:

- clean initial Git campaign;
- clean non-Git campaign;
- unrelated dirty Git paths;
- `STARTED` without `PREPARED`;
- `PREPARED` with partial modifications;
- `COMPLETED` without commit;
- matching commit with leftover recovery directory;
- missing backup;
- conflicting journal and Git evidence;
- required test failure that cannot be executed.

For each case, verify the documented result is safe, unambiguous, and consistent across all references.

### 10.6 Phase completion condition

The skill can execute and recover bounded implementation tasks without relying on Git for baseline restoration and without risking unrelated project work.

## 11. Phase 4 — Human steering and completion communication

### 11.1 Capability

Deliver clean HIL stopping points, focused post-checkpoint revision, final-state normalization, and consistent task/milestone/phase/campaign reports.

### 11.2 Dependencies

- Complete lifecycle, document, roadmap, verification, implementation, and recovery workflows.

### 11.3 Milestone: Checkpoint steering and normalization

#### Task 4.1 — Implement the checkpoint-steering reference

**Objective**

Define checkpoint establishment, explicit continuation, steering classification, focused revision, broader redesign, normalization, and external-release limits.

**SPEC coverage**

- §17 Bounded implementation selection
- §21 Human-in-the-loop checkpoints
- §26.10 Checkpoint steering acceptance

**Path**

```text
sdd-man/references/checkpoint-steering.md
```

**Implementation work**

1. Define clean checkpoint prerequisites.
2. Define `awaiting-steering` and explicit release.
3. Define user choices at the checkpoint.
4. Define contract-neutral, contract, architectural, and defect classifications.
5. Define the complete impact-inspection surface.
6. Define focused revision as new recoverable work rather than reopening old records.
7. Define removal of positive tests and retention of required negative-contract tests.
8. Define SPEC/PLAN/LAYOUT/ROADMAP/verification-map normalization.
9. Define paused handoff after steering completion.
10. Define externally released behavior limitations.

**Verification**

- Walk through the encrypted-7z removal scenario.
- Confirm subsequent interface-neutral phases remain untouched.
- Confirm the final PLAN does not contain add-then-remove history.
- Confirm ROADMAP removes obsolete tasks and reconciles affected completion.
- Confirm journal and Git history remain append-only evidence.
- Confirm the workflow remains paused after revision.

**Completion condition**

A user can revise a completed range before further work, leaving authoritative project state equivalent to the direct final design.

### 11.4 Milestone: Capability-oriented reporting

#### Task 4.2 — Implement the reporting reference

**Objective**

Define feature-summary requirements and aggregation rules for every completion and status boundary.

**SPEC coverage**

- §22 Completion reporting contract
- §23 Journal summaries
- §26.12 Completion reporting acceptance

**Path**

```text
sdd-man/references/reporting.md
```

**Implementation work**

1. Define task report fields and incremental capability focus.
2. Define milestone synthesis without concatenation.
3. Define phase and campaign capability summaries.
4. Define enabling-infrastructure, test, documentation, defect, migration, removal, and hardening categories.
5. Define explicit “no runtime behavior changed” reporting.
6. Define concise journal summaries and optional structured feature lists.
7. Define multi-task progress messages and self-contained final responses.
8. Define blocked, reverted, partial, and unverified status language.

**Verification**

- Produce model reports for a runtime feature, test foundation, documentation-only task, removed capability, milestone, and phase.
- Confirm no report treats file changes or tests as the feature summary.
- Confirm higher-level reports synthesize rather than repeat lower-level text.
- Confirm the final multi-task report stands alone.

**Completion condition**

Every completion boundary can communicate what verified capability now exists and what remains next.

#### Task 4.3 — Integrate checkpoint and reporting routes

**Objective**

Complete orchestration across bounded implementation, checkpoint steering, status reporting, and explicit continuation.

**Paths**

```text
sdd-man/SKILL.md
sdd-man/references/lifecycle.md
sdd-man/references/roadmap.md
sdd-man/references/implementation.md
```

**SPEC coverage**

- §7 `SKILL.md` orchestration
- §8 Conversation lifecycle
- §17 Bounded implementation selection
- §21 Checkpoints
- §22 Reporting

**Implementation work**

1. Route completed ranges into checkpoint steering.
2. Require explicit continuation after ordinary and revised checkpoints.
3. Route all completion reports through `reporting.md`.
4. Ensure roadmap selection semantics agree with checkpoint boundaries.
5. Ensure journal checkpoint and steering events agree with implementation state.
6. Remove any duplicated detailed reporting or steering instructions from other references.

**Verification**

- Trace “implement next phase” from selection to paused phase report.
- Trace “remove encrypted support, then stop” through normalization and paused report.
- Trace “continue to next milestone” through explicit checkpoint release.
- Confirm no path silently advances beyond authorized scope.

**Completion condition**

The complete HIL loop is coherent from user-selected range through review, revision, reporting, and explicit continuation.

### 11.5 Phase verification

- Run the complete encrypted-archive steering scenario.
- Run an acceptance-without-revision checkpoint.
- Run a future-PLAN revision that changes no completed code.
- Run a steering request that reveals downstream contract impact and must broaden or return to design.
- Verify task, milestone, phase, campaign, and steering reports.
- Confirm all resulting states are reported truthfully.

### 11.6 Phase completion condition

The user can inspect and steer implementation at meaningful boundaries, and the skill reports each completed capability at the correct aggregation level.

## 12. Phase 5 — Integrated conformance and release

### 12.1 Capability

Prove that the complete skill is coherent, safe, progressively disclosed, and effective on representative projects, then finalize and install it.

### 12.2 Dependencies

All earlier phases.

### 12.3 Milestone: Static conformance

#### Task 5.1 — Perform the resource-topology and portability audit

**Objective**

Verify package structure, direct resource reachability, metadata, optional-resource discipline, and portability.

**Scope**

All skill files.

**Verification work**

1. Run structural skill validation.
2. Confirm `SKILL.md` frontmatter contains only `name` and `description`.
3. Confirm every runtime reference and asset is directly discoverable from `SKILL.md` or the reference that explicitly consumes the asset.
4. Confirm reference topology has no mandatory deep chains.
5. Confirm no unused file or placeholder remains.
6. Confirm no bundled script exists in the baseline.
7. Confirm no workflow assumes a particular application language, test runner, shell, or Git availability.
8. Confirm `agents/openai.yaml` is not a runtime dependency.

**Completion condition**

The package is structurally valid, minimal, and portable within the specified host assumptions.

#### Task 5.2 — Perform the full SPEC traceability audit

**Objective**

Demonstrate that every normative SPEC requirement has one implementation owner and no contradictory duplicate.

**Scope**

All skill files and the coverage map in this PLAN.

**Verification work**

1. Trace every SPEC section to one or more implemented resources.
2. Verify every acceptance scenario has an executable forward-test prompt or deterministic inspection method.
3. Identify normative duplication and retain one canonical definition.
4. Identify uncovered behavior and correct it through a bounded task if needed.
5. Recheck terminology across all resources.

**Completion condition**

Every specified capability is covered, terminology is consistent, and canonical ownership is unambiguous.

### 12.4 Milestone: Independent forward-testing

Forward-testing shall use fresh agents with minimal task-local context. Test agents shall receive the skill and realistic user requests, not expected answers or diagnoses. Temporary projects shall not leak between scenarios.

#### Task 5.3 — Forward-test exploration and document authoring

**Objective**

Validate non-mutating exploration, transition gating, document generation, recursive decomposition, ROADMAP derivation, and verification-map creation.

**Scenarios**

- underspecified greenfield request requiring exploration only;
- explicit SPEC/PLAN/LAYOUT generation after decisions are supplied;
- document review correction without implementation;
- compact project that should not be over-decomposed;
- larger project requiring focused child nodes.

**Verification**

- Inspect agent behavior and emitted artifacts.
- Confirm no unauthorized implementation occurred.
- Confirm roadmap and PLAN align exactly.
- Confirm verification-map entries represent implemented rather than speculative paths.

**Completion condition**

Independent agents can use the skill to produce coherent documents and respect lifecycle gates without hidden context.

#### Task 5.4 — Forward-test implementation, recovery, and steering

**Objective**

Validate transactional implementation decisions, recovery classification, bounded execution, verification selection, checkpoint pausing, and focused normalization.

**Scenarios**

- clean Git project implementing the next task;
- non-Git project implementing a bounded task;
- prepared interrupted task requiring restoration;
- completed uncommitted task requiring reconciliation;
- unrelated dirty target requiring escalation;
- next-milestone request stopping at its boundary;
- encrypted-capability removal at a completed phase checkpoint.

**Verification**

- Inspect state transitions, selected checks, roadmap updates, and reports.
- Confirm agents do not continue beyond requested ranges.
- Confirm evidence is preserved in ambiguous states.
- Confirm authoritative artifacts normalize after steering.

**Completion condition**

Independent agents consistently follow safety, recovery, HIL, and reporting contracts on realistic project states.

### 12.5 Milestone: Final refinement and installation

#### Task 5.5 — Apply validated refinements and finalize the skill

**Objective**

Correct substantiated issues from conformance and forward-testing, regenerate interface metadata, validate the final package, and save the completed skill.

**Paths**

Only skill files required by validated findings, plus:

```text
sdd-man/agents/openai.yaml
```

**Implementation work**

1. Classify each finding as skill defect, scenario ambiguity, or unsupported expectation.
2. Apply only substantiated corrections.
3. Repeat affected forward tests after material changes.
4. Regenerate `agents/openai.yaml` from final `SKILL.md`.
5. Run final structural validation.
6. Confirm final package contains only required runtime resources.
7. Stage and save only the `sdd-man` skill according to skill-creation requirements.
8. Verify the installed skill's final paths and availability.

**Verification**

- Structural validation passes.
- All affected scenarios pass after refinements.
- No stale placeholder or temporary test artifact remains.
- Final metadata matches the installed skill.
- Final skill presence is verified after installation.

**Completion condition**

The validated `sdd-man` skill is installed and available, with all acceptance evidence passing and no unresolved material finding.

### 12.6 Phase verification

- Complete structural and traceability audits.
- Complete all forward-test scenarios.
- Re-run tests affected by refinements.
- Verify final portable runtime contents.
- Verify final installation state.

### 12.7 Phase completion condition

The complete skill satisfies the governing SPEC, behaves correctly under independent use, and is installed without unused or unjustified resources.

## 13. Cross-phase verification requirements

After every task:

1. Review the changed resource against its SPEC coverage.
2. Verify referenced paths and anchors.
3. Check terminology against completed resources.
4. Confirm no canonical responsibility was duplicated.
5. Run structural validation when `SKILL.md`, metadata, or topology changed.
6. Re-run the smallest relevant scenario walkthrough.

After every milestone:

1. Execute the milestone's integrated scenarios.
2. Confirm all child task completion conditions.
3. Confirm the milestone delivers the stated coherent capability.
4. Produce a milestone report summarizing implemented capability.

After every phase:

1. Execute phase verification.
2. Re-run relevant earlier routing and safety checks.
3. Confirm no later phase is required to make the current phase internally coherent.
4. Produce a phase report summarizing delivered capability and next work.

## 14. Final acceptance matrix

| Acceptance area | Required evidence |
|---|---|
| Exploration | Independent scenario completes without unauthorized files or implementation |
| Lifecycle gates | Direct inspection and scenarios confirm every explicit transition |
| Project discovery | Git, non-Git, nested instructions, and inconsistent-state scenarios |
| Document system | Compact and decomposed SPEC/PLAN/LAYOUT outputs |
| ROADMAP | Exact PLAN correspondence, counts, checkmarks, and bounded selection |
| Verification map | Valid JSON, shared targets, changed-path selection walkthrough |
| Initial campaign | Bounded greenfield task scenario |
| Change campaign | Baseline-plus-delta and final integration scenario |
| Task transaction | All operation kinds and state transitions inspected |
| Recovery | STARTED, PREPARED, COMPLETED, committed, and corrupt-state scenarios |
| Git safety | Unrelated dirty changes remain untouched and unstaged |
| Non-Git safety | Exact backup-and-journal recovery path succeeds conceptually or in fixture |
| Test handling | Direct, dependent, integration, boundary, and unrelated-failure cases |
| HIL checkpoint | Requested range stops cleanly and awaits explicit direction |
| Focused steering | Rejected capability is normalized out of all current-state artifacts |
| Reporting | Task, milestone, phase, campaign, removal, and infrastructure summaries |
| Progressive disclosure | Each scenario loads only the necessary focused references |
| Package quality | Structural validator passes; no unused resources or scripts |

## 15. Final completion criteria

Implementation is complete when:

- all 24 tasks and 12 milestones are complete;
- all five phases meet their completion conditions;
- the final package matches the declared baseline layout;
- every SPEC section is implemented and traceable;
- every reference has one focused canonical responsibility;
- `SKILL.md` remains concise and routes every workflow directly;
- all templates are valid, usable, and referenced by a workflow;
- no script or other optional resource exists without an approved deterministic role;
- all static audits and independent forward-test scenarios pass;
- Git and non-Git behavior are both covered;
- recovery and ambiguity scenarios fail safely;
- HIL checkpoints always prevent unauthorized continuation;
- completion reports consistently summarize verified capability;
- the final skill passes structural validation and is installed successfully.

## 16. Current status

This PLAN is ready for review. Implementation has not begun.
