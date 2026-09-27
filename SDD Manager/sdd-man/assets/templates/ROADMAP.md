# Project Roadmap

## Authority

This roadmap is a derived implementation-progress view.

- `PLAN.md` and its child plans define canonical phases, milestones, tasks, ordering, dependencies, and verification.
- This roadmap mirrors every current phase, milestone, and task exactly once.
- A checked item indicates durable completion under the project's implementation and recovery protocol.
- The implementation journal governs active, interrupted, blocked, and reverted task state.

## Progress

| Level      | Completed |     Total |
| ---------- | --------: | --------: |
| Phases     | `<count>` | `<count>` |
| Milestones | `<count>` | `<count>` |
| Tasks      | `<count>` | `<count>` |

- [ ] **[Phase: `<semantic phase name>`](notes/Spec-Driven%20Development/Skill/sdd-man/assets/templates/PLAN.md#phase-semantic-phase-name)**
    - [ ] **[Milestone: `<semantic milestone name>`](notes/Spec-Driven%20Development/Skill/sdd-man/assets/templates/PLAN.md#milestone-semantic-milestone-name)**
        - [ ] [Task: `<semantic task name>`](notes/Spec-Driven%20Development/Skill/sdd-man/assets/templates/PLAN.md#task-semantic-task-name)
        - [ ] [Task: `<semantic task name>`](notes/Spec-Driven%20Development/Skill/sdd-man/assets/templates/PLAN.md#task-semantic-task-name-1)

<!-- Repeat phases, milestones, and tasks in exact PLAN order. Replace links with canonical PLAN or child-plan anchors. -->

## Status semantics

- `[ ]` means not durably complete.
- `[x]` means durably complete.
- Active, prepared, blocked, partial, and reverted states belong to the implementation journal and recovery state, not alternate checkbox syntax.
- A checkmark written during transaction finalization is prospective until its completion record, required Git commit, and recovery cleanup are durable.

## Reconciliation

Before selecting new work, reconcile this roadmap with PLAN, the implementation journal, recovery data, and matching task commits when Git is available.
