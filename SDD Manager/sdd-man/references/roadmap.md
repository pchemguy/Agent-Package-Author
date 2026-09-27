# PLAN-Aligned Roadmap

Use this reference to derive, validate, reconcile, or interpret `docs/dev/ROADMAP.md`, and to resolve human-selected task, milestone, or phase boundaries.

## Contents

- [Authority](#authority)
- [Roadmap structure](#roadmap-structure)
- [Derivation](#derivation)
- [Checklist semantics](#checklist-semantics)
- [Progress reconciliation](#progress-reconciliation)
- [Bounded work selection](#bounded-work-selection)
- [Completion updates](#completion-updates)
- [PLAN revision and normalization](#plan-revision-and-normalization)
- [Status reporting](#status-reporting)
- [Template](#template)

## Authority

Treat PLAN as the canonical owner of:

- phases;
- milestones;
- tasks;
- ordering;
- dependencies;
- task and boundary verification;
- completion conditions.

Treat ROADMAP as a derived human-readable projection of PLAN structure and durable completion status.

Do not let ROADMAP:

- introduce a task absent from PLAN;
- change task order;
- define a dependency;
- replace task instructions;
- redefine verification;
- become the execution journal.

Use execution evidence to determine status and PLAN to determine structure.

## Roadmap structure

Keep ROADMAP compact enough to inspect in one pass. Include:

1. an authority statement;
2. a progress summary table with completed and total phase, milestone, and task counts;
3. phase checkboxes in PLAN order;
4. milestone checkboxes nested within each phase;
5. task checkboxes nested within each milestone;
6. links from every item to its canonical PLAN heading;
7. binary durable checkboxes.

Represent the hierarchy as:

```text
phase
└── milestone
    └── task
```

Use PLAN's semantic names. Do not replace them with ordinal-only labels or journal transaction identifiers.

## Derivation

After PLAN creation or material restructuring:

1. Read the complete PLAN tree necessary to enumerate its hierarchy.
2. Identify every current phase, milestone, and task.
3. Preserve the canonical relative order.
4. Create one roadmap item for every PLAN item.
5. Link each item to its canonical PLAN file and heading.
6. Count tasks within milestones and milestones within phases.
7. Initialize durable status from verified evidence.
8. Validate exact bidirectional correspondence.

Require these invariants:

- every PLAN task appears exactly once in ROADMAP;
- every ROADMAP task resolves to exactly one PLAN task;
- phase, milestone, and task order is identical;
- parent counts equal their actual children;
- no roadmap prose adds normative implementation scope.

For a new greenfield plan with no implementation evidence, initialize every item unchecked.

For an existing project, do not infer checkmarks from apparently implemented code alone. Require durable task evidence or an explicit project-baselining decision.

## Checklist semantics

Use only:

```text
[ ] not durably complete
[x] durably complete
```

Do not persist alternate checkbox states for:

- active;
- started;
- prepared;
- partially implemented;
- blocked;
- verified but uncommitted;
- reverted.

Those states belong to journal, recovery, and Git evidence.

### Task checkmark

Write a task's prospective `[x]` transition only during finalization, after:

- its complete planned scope is implemented;
- required documents and verification routing are aligned;
- required verification passes.

The checkmark becomes durable only when a matching `completed` record exists, the exact task commit exists in Git projects, and recovery cleanup succeeds. Until then, journal and recovery state override the working ROADMAP; do not report the prospective checkmark as completion.

### Milestone checkmark

Write a milestone's prospective `[x]` transition only when:

- every current child task is being closed durably in the same finalization or is already durable;
- milestone verification passes;

It becomes durable only when the closing completion record identifies the milestone boundary and every child task is durably complete.

### Phase checkmark

Write a phase's prospective `[x]` transition only when:

- every current child milestone is being closed durably in the same finalization or is already durable;
- phase verification and acceptance pass;

It becomes durable only when the closing completion record identifies the phase boundary and every child milestone is durably complete.

### Campaign completion

Treat the roadmap as fully complete only after campaign integration, final acceptance, and recovery cleanup succeed.

## Progress reconciliation

ROADMAP may be read first for rapid orientation, but do not select or begin work until it is reconciled with execution evidence.

When the latest durable state is `awaiting-steering`, reconciliation may identify the next boundary but must not select it for execution until an explicit continuation request releases the checkpoint.

Use this order:

1. Inspect the journal and recovery directories.
2. Inspect matching Git task commits when Git is required.
3. Resolve active or incomplete transaction state.
4. Read ROADMAP completion state.
5. Compare checkmarks with durable evidence.
6. Compare ROADMAP structure and order with PLAN.
7. Identify the next permitted incomplete item.

Validate:

- a checked task has a durable completion record;
- a checked Git-backed task has its matching commit;
- an unchecked task is not treated as complete merely because code resembles the requirement;
- a checked milestone has no unchecked child task;
- a checked phase has no unchecked child milestone;
- progress counts equal current checkbox state;
- the next incomplete item agrees with PLAN order;
- no active task is hidden by a later checked item.

When evidence disagrees, do not toggle checkmarks speculatively. Classify the mismatch:

- completed task awaiting required commit;
- committed task awaiting cleanup;
- stale roadmap after durable completion;
- roadmap checked without durable evidence;
- PLAN changed without roadmap regeneration;
- corrupt or ambiguous history.

Use recovery rules for transaction mismatches. Use document normalization for PLAN structural changes. Preserve evidence and ask when ownership or baseline remains uncertain.

## Bounded work selection

Resolve human requests against the next incomplete PLAN item after reconciliation.

### Next task

Select the first incomplete task whose declared prerequisites are complete.

### Next N tasks

Select the next `N` incomplete tasks in canonical PLAN order. Execute each as a separate recoverable transaction. Stop after the Nth task reaches durable clean completion.

### Current or next milestone

If the current milestone is partially complete, complete its remaining tasks and boundary verification. Otherwise select the next incomplete milestone.

Do not interpret “next milestone” as skipping an incomplete current milestone.

### Current or next phase

If the current phase is partially complete, complete its remaining milestones and phase verification. Otherwise select the next incomplete phase.

### Next N milestones or phases

Count incomplete boundaries from current durable progress, not historical completed boundaries. Execute through the requested count, preserving independent task transactions.

### Named boundary

Resolve “through `<name>`” to one unambiguous task, milestone, or phase. Include every incomplete prerequisite through that boundary. Ask when names are duplicated or scope is ambiguous.

### MVP boundary

Resolve the MVP from PLAN's explicit first useful testable boundary. Do not invent a smaller or larger MVP from roadmap convenience.

## Completion updates

Include ROADMAP in a task's declared transaction scope whenever task or parent status changes.

After implementation and verification:

1. confirm the changed scope belongs to the task;
2. run task and applicable boundary verification;
3. write the task's prospective checkmark as part of the transaction being finalized;
4. write its milestone's prospective checkmark when all children and milestone checks pass;
5. write its phase's prospective checkmark when all milestones and phase checks pass;
6. recalculate progress counts;
7. prepare the capability summary;
8. append the `completed` journal record;
9. create the required task commit when Git is available;
10. clean recovery state.

If interrupted before the completion record, normal recovery must restore the prior roadmap state with the rest of the task baseline.

If interrupted after completion but before commit, completed-task reconciliation must verify and commit the roadmap transition with the task.

At startup or status inspection, never count a prospective checkmark from a nonterminal transaction as durable progress.

## PLAN revision and normalization

When PLAN structure changes:

1. regenerate affected ROADMAP structure from the revised PLAN;
2. remove tasks absent from the current PLAN;
3. add new tasks unchecked unless durable evidence establishes completion;
4. preserve checkmarks only when the current implementation satisfies the revised task's completion conditions;
5. recompute parent checkmarks and counts;
6. verify links and relative order.

Do not preserve a roadmap item such as “remove rejected capability” after checkpoint normalization when the final PLAN directly describes the reduced system. The journal and Git history preserve that execution history.

For a multi-task steering revision, use the active change plan and journal to represent temporary work. Normalize the main ROADMAP only when the settled final PLAN is integrated.

After normalization, recalculate totals from the current PLAN-derived hierarchy. Historical tasks removed from the final PLAN remain in journal and Git history but do not remain as ROADMAP items or inflate current denominators.

## Status reporting

Calculate reported progress from reconciled evidence:

```text
PLAN structure
+ ROADMAP durable status
+ journal and recovery state
+ Git durability when applicable
= current project status
```

Report:

- completed and total phases, milestones, and tasks;
- current phase and milestone;
- active or blocked transaction state;
- next canonical task;
- next useful HIL stopping point;
- any disagreement preventing trustworthy counts.

Use `reporting.md` to express those counts and states at the appropriate task, milestone, phase, campaign, checkpoint, or blocked-work level.

Do not report a percentage when the denominator is unknown or PLAN and ROADMAP are inconsistent.

## Template

Use `../assets/templates/ROADMAP.md` as a starting structure. Replace its example items with the exact PLAN hierarchy and preserve its authority statement.
