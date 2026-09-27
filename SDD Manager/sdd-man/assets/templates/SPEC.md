# Project Specification

<!-- Adapt headings to the project. Remove instructional comments from the completed document. -->

## 1. Purpose

Define the problem solved, intended outcome, and principal users or consumers.

## 2. Scope

### 2.1 Included

Define the complete intended system boundary.

### 2.2 Non-goals

Define intentionally unsupported behavior and adjacent concerns outside the project.

## 3. System context and use cases

Describe the operating environment, external actors or systems, and principal end-to-end uses.

## 4. Terminology and invariants

Define project-wide terms and guarantees used by multiple components.

## 5. Architecture

### 5.1 Component model

Describe top-level components, their responsibilities, and explicit boundaries.

### 5.2 Dependency direction

Use `A → B` to mean that B depends on A. Define allowed dependencies and prohibit cycles.

### 5.3 Cross-component contracts

Define only system-level contracts and relationships. Route component detail to the owning child specification.

## 6. Interfaces and data contracts

Define public interfaces, external protocols, persistent representations, and compatibility requirements at the appropriate level.

## 7. Required behavior

Describe system-level successful behavior, lifecycle, error semantics, and boundary cases.

## 8. Specification map

| Area     | Canonical specification | Responsibility                 |
| -------- | ----------------------- | ------------------------------ |
| `<area>` | `spec/<node>.md`        | `<owned behavior or contract>` |

<!-- Omit the table when the complete specification remains in this file. -->

## 9. Acceptance conditions

Define objective system-level outcomes, including important successful, boundary, and failure scenarios.

## 10. Explicitly unresolved decisions

List only intentionally deferred decisions that do not make the current specification internally contradictory. Omit this section when none remain.
