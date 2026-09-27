---
name: sdd-man
description: Guide specification-driven software development from problem exploration through authoritative SPEC, PLAN, LAYOUT, and ROADMAP design, bounded implementation, verification, interruption recovery, and human steering. Use for greenfield or existing projects when defining architecture, creating or reviewing development documents, governing in-code documentation, inspecting project status, planning or implementing task ranges, recovering interrupted work, reconciling tests, or revising completed features at checkpoints.
---

# SDD Manager

## Operating rule

Treat activation as procedural context, not permission to mutate. Classify the user's request, load only the references needed for that workflow, and respect every explicit transition gate.

Read [lifecycle.md](references/lifecycle.md) for every invocation that may change mode, create authoritative artifacts, inspect execution state, or modify a project.

## Classify the request

Choose one primary mode:

| Request                                                              | Mode                         | Required reference                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clarify a problem, compare approaches, or develop decisions          | Exploration                  | [lifecycle.md](references/lifecycle.md), [exploration.md](references/exploration.md)                                                                                                                                                                                                                                                                                               |
| Inspect an existing project, authorities, Git state, or SDD status   | Status inspection            | [lifecycle.md](references/lifecycle.md), [project-discovery.md](references/project-discovery.md), plus [recovery.md](references/recovery.md) and [reporting.md](references/reporting.md) when execution state exists                                                                                                                                                               |
| Create or materially revise authoritative development documents      | Document authoring or review | [lifecycle.md](references/lifecycle.md), [document-system.md](references/document-system.md), plus [roadmap.md](references/roadmap.md) and [verification.md](references/verification.md) where applicable                                                                                                                                                                          |
| Generate, validate, or interpret project progress                    | Roadmap                      | [lifecycle.md](references/lifecycle.md), [roadmap.md](references/roadmap.md)                                                                                                                                                                                                                                                                                                       |
| Design testing or resolve checks affected by a change                | Verification                 | [lifecycle.md](references/lifecycle.md), [verification.md](references/verification.md)                                                                                                                                                                                                                                                                                             |
| Review or govern docstrings and other in-code documentation          | In-code documentation        | [lifecycle.md](references/lifecycle.md), [project-discovery.md](references/project-discovery.md), [in-code-documentation.md](references/in-code-documentation.md), [verification.md](references/verification.md), and [reporting.md](references/reporting.md)                                                                                                                        |
| Implement, continue, or resume a bounded range                       | Implementation or recovery   | [lifecycle.md](references/lifecycle.md), [project-discovery.md](references/project-discovery.md), [implementation.md](references/implementation.md), [in-code-documentation.md](references/in-code-documentation.md), [recovery.md](references/recovery.md), [verification.md](references/verification.md), [roadmap.md](references/roadmap.md), and [reporting.md](references/reporting.md)                                |
| Review or revise work at a completed boundary                        | Checkpoint steering          | [lifecycle.md](references/lifecycle.md), [checkpoint-steering.md](references/checkpoint-steering.md), [document-system.md](references/document-system.md), [implementation.md](references/implementation.md), [in-code-documentation.md](references/in-code-documentation.md), [verification.md](references/verification.md), and [reporting.md](references/reporting.md), plus [roadmap.md](references/roadmap.md) when progress structure changes |
| Report task, milestone, phase, campaign, steering, or blocked status | Reporting                    | [lifecycle.md](references/lifecycle.md), [reporting.md](references/reporting.md), plus [project-discovery.md](references/project-discovery.md) and [roadmap.md](references/roadmap.md) when evidence must be reconciled                                                                                                                                                            |

Answer narrow questions within the current mode. Do not force a lifecycle transition merely because a later workflow could eventually be useful.

## Enforce transition gates

- Do not create authoritative documents during exploration without an explicit request.
- Do not begin implementation because documents were created, reviewed, or appear sufficient.
- Do not modify project state during a status inspection.
- Do not continue beyond the user-requested task, milestone, or phase range.
- Do not resolve an interrupted task by starting new work.
- Ask before mutation when the requested transition is ambiguous.

Allow direct entry into a later mode when the user supplies adequate governing artifacts and explicitly requests that mode. Do not replay earlier stages unnecessarily.

## Preserve authority and evidence

Before any project mutation:

1. Locate the governed project root.
2. Discover applicable project instructions and referenced requirements.
3. Identify the main and active-change document sets.
4. Determine Git or non-Git operation.
5. Inspect journal and recovery state.
6. Resolve contradictions or stop and ask.

Never silently absorb unrelated changes, guess file ownership, weaken verification, or select whichever conflicting source is most convenient.

## Keep state truthful

Distinguish proposed, specified, planned, started, prepared, partially implemented, blocked, reverted, verified, durably completed, and awaiting-steering states.

Do not present:

- tentative exploration as an accepted requirement;
- a document as implemented behavior;
- a prepared task as complete;
- an unverified implementation as successful;
- a roadmap checkbox as conclusive when execution evidence disagrees.

## Use resources progressively

Load only the active workflow references. Do not preload every resource.

Available workflow resources:

- [lifecycle.md](references/lifecycle.md): modes, transitions, authority, continuity, checkpoints, and truthful status.
- [exploration.md](references/exploration.md): decisions, alternatives, questions, prototypes, and specification readiness.
- [project-discovery.md](references/project-discovery.md): project roots, instructions, documents, Git, tools, journal state, and status classification.
- [document-system.md](references/document-system.md): SPEC, PLAN, LAYOUT, recursive ownership, dependencies, change overlays, review, and normalization.
- [roadmap.md](references/roadmap.md): PLAN-derived progress, bounded work selection, durable checklist semantics, and reconciliation.
- [verification.md](references/verification.md): verification strategy, component-to-check routing, affected-check selection, and failure handling.
- [implementation.md](references/implementation.md): campaigns, bounded ranges, one-task transactions, preparation, verification, durable completion, and HIL stopping boundaries.
- [in-code-documentation.md](references/in-code-documentation.md): docstring and documentation-comment defaults, incremental reconciliation, language conventions, verification, and project-wide review.
- [recovery.md](references/recovery.md): mandatory startup recovery, exact restoration, interrupted completion, cleanup, and evidence-preserving escalation.
- [checkpoint-steering.md](references/checkpoint-steering.md): clean HIL boundaries, revision classification, impact analysis, focused revision, normalization, and released-behavior limits.
- [reporting.md](references/reporting.md): capability summaries, aggregation, truthful non-completion language, journal summaries, and self-contained progress reports.

## Universal stop conditions

Stop and preserve evidence when:

- applicable instructions conflict;
- target ownership is uncertain;
- journal, recovery, filesystem, roadmap, or Git evidence disagrees materially;
- a required baseline cannot be established;
- the requested action exceeds the authorized mode or range;
- continuing would make authoritative documents and project state knowingly inconsistent.

Explain the exact blocker and the smallest user decision needed to proceed.
