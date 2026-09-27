# Project Implementation Plan

<!-- Adapt headings to the project. Remove instructional comments from the completed document. -->

## 1. Objective

State the complete specified system this plan constructs.

## 2. Governing specification

Identify the root SPEC and relevant child specifications.

## 3. Implementation strategy

Describe the principal construction approach, MVP boundary, dependency order, and project-wide verification strategy.

## 4. Dependency model

Use `A → B` to mean that B depends on A. Identify prerequisites, parallelizable branches, and any expand–migrate–contract sequence.

## 5. Phase overview

| Order | Phase                   | Milestones |     Tasks | Delivered capability      |
| ----: | ----------------------- | ---------: | --------: | ------------------------- |
|     1 | `<semantic phase name>` |  `<count>` | `<count>` | `<reviewable capability>` |

## 6. Phase: `<semantic phase name>`

### 6.1 Capability

State the major independently meaningful capability delivered by this phase.

### 6.2 Specification coverage

Identify the SPEC nodes and contracts implemented by the phase.

### 6.3 Dependencies

Identify prerequisite phases, components, contracts, or tooling.

### 6.4 Milestone: `<semantic milestone name>`

State the coherent review, handoff, or stopping capability delivered by the milestone.

#### Task: `<semantic task name>`

**Objective**

State the smallest complete implementation increment.

**Specification coverage**

Identify exact governing SPEC sections.

**Prerequisites**

Identify prerequisite tasks, contracts, tools, or environment assumptions. State `None` when the task has no prerequisite.

**Affected paths or components**

```text
<production path>
<test path>
<development-document path>
```

**Implementation work**

1. Define the ordered work.
2. Keep the task atomic and recoverable.
3. Update implementation, tests, and affected development documents together.

**In-code documentation impact**

Identify affected module, package, type, and callable documentation. State the expected convention and documentation checks, or explain why the task is not expected to require in-code documentation changes.

**Verification**

- Run direct unit tests.
- Run affected dependent-component tests.
- Run relevant integration checks.
- Reconcile affected in-code documentation and run applicable documentation checks.
- Run required lint, type, build, formatting, or packaging checks.

**Completion condition**

State the objective condition proving the task is complete.

### 6.5 Milestone verification

Define the integrated checks and reviewable capability required to close this milestone.

### 6.6 Phase verification

Define phase-level integration and acceptance checks.

### 6.7 Phase completion condition

State the complete capability and evidence required to close the phase.

<!-- Repeat the phase structure using semantic names. Split broad phases into plan children when necessary. -->

## 7. Cross-phase verification

Define regression, compatibility, packaging, installation, performance, or platform checks that apply across phases.

## 8. Final acceptance

Map system-level SPEC acceptance conditions to final verification evidence.

## 9. Completion criteria

Define project-wide documentary, implementation, test, recovery-state, and distribution conditions.
