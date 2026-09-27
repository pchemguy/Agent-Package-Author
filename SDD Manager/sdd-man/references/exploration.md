# Exploration and Decision Formation

Use this reference while the user is defining a problem, desired outcomes, constraints, scope, or implementation direction. Exploration develops an accepted design state; it does not authorize authoritative document creation or project implementation.

## Contents

- [Objectives](#objectives)
- [Decision-state model](#decision-state-model)
- [Exploration workflow](#exploration-workflow)
- [Questions and initiative](#questions-and-initiative)
- [Alternatives and tradeoffs](#alternatives-and-tradeoffs)
- [Prototypes and experiments](#prototypes-and-experiments)
- [Readiness for specification](#readiness-for-specification)
- [Exploration output](#exploration-output)

## Objectives

Use exploration to:

- articulate the actual problem before formalizing a solution;
- establish shared vocabulary;
- identify required outcomes, constraints, non-goals, and acceptance concerns;
- expose architectural boundaries, contracts, data models, and external dependencies;
- compare plausible approaches using relevant tradeoffs;
- identify boundary cases, risks, assumptions, and unknowns;
- converge incrementally on decisions the user understands and accepts.

Do not force a complete design before enough information exists. Do not prolong exploration once remaining questions can be represented safely in the specification or delegated as implementation detail.

## Decision-state model

Keep these categories distinct:

| Category              | Meaning                                      | Treatment                                                                          |
| --------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------- |
| Fact                  | Evidence supplied or verified                | Preserve with source or context when material                                      |
| User decision         | Explicitly accepted direction                | Treat as governing until revised                                                   |
| Working assumption    | Temporary premise used to continue analysis  | Label and confirm when it affects design                                           |
| Open question         | Unresolved issue with potential consequences | Resolve or explicitly defer before affected authoring                              |
| Alternative           | Plausible option not selected                | Compare without treating it as a requirement                                       |
| Discarded alternative | Rejected option                              | Do not carry into normative documents unless its exclusion is itself a requirement |
| Delegated detail      | Choice safely left to implementation         | Record the boundary of discretion, not an invented solution                        |

Do not infer acceptance merely because the user did not object to an illustrative example.

When new information conflicts with an accepted decision:

1. identify the earlier decision;
2. explain the conflict and practical consequence;
3. determine whether the new statement revises the decision or is exploratory;
4. update the decision state only after the intent is clear.

## Exploration workflow

### 1. Frame the problem

Establish:

- who or what uses the system;
- the problem being solved;
- the observable outcome;
- the environment and operational constraints;
- what is explicitly outside scope.

Correct vague or overloaded vocabulary early. Reuse settled terms consistently.

### 2. Inspect available context

Use read-only inspection when an existing project, document, format, interface, or failure informs the design. Read only what is relevant to the current question.

Do not mutate the project during exploration. If inspection reveals active recovery state, report it; do not resolve it unless the user requests recovery or implementation.

### 3. Identify design surfaces

Explore only the surfaces material to the decision, such as:

- public behavior and error semantics;
- component responsibilities;
- interfaces and dependency direction;
- data representation and persistence;
- concurrency and lifecycle;
- portability and packaging;
- verification and acceptance;
- migration or compatibility constraints.

Avoid premature file-by-file design unless physical layout is itself the decision.

### 4. Develop plausible alternatives

For each serious alternative, state:

- the core approach;
- what it simplifies;
- what it complicates;
- relevant risks and dependencies;
- reversibility;
- effect on testing, recovery, or future evolution.

Prefer a small number of meaningful alternatives over exhaustive lists of superficial variants.

### 5. Challenge the design

Identify:

- contradictory requirements;
- cyclic or unclear dependencies;
- components with mixed responsibilities;
- undefined ownership;
- behavior lacking error or boundary semantics;
- assumptions that make recovery or testing impossible;
- features whose cost exceeds their demonstrated value.

Explain the consequence rather than merely labeling the design weak.

### 6. Converge incrementally

Resolve the decisions necessary for the next useful step. Preserve intentionally deferred matters as explicit open questions, constraints, non-goals, or delegated details.

Periodically summarize:

- accepted decisions;
- current assumptions;
- unresolved blockers;
- discarded alternatives that must not reappear;
- the next decision or proposed transition.

## Questions and initiative

Ask a focused question when its answer would materially change:

- architecture;
- public behavior;
- compatibility;
- scope;
- acceptance criteria;
- implementation order;
- the safety of a mutation.

Do not ask the user to decide routine implementation details already bounded by accepted contracts. Provide a reasoned recommendation when enough evidence exists.

Ask one or a small coherent set of questions at a time. Continue useful analysis around nonblocking unknowns instead of stopping unnecessarily.

## Alternatives and tradeoffs

Distinguish:

- established facts from inference;
- design preference from hard constraint;
- current cost from future optionality;
- implementation convenience from architectural soundness;
- reversible choices from commitments embedded in public contracts or persistent formats.

When recommending an option, identify why it best fits the accepted priorities. Do not present an arbitrary choice as inevitable.

When no option dominates, make the decision surface explicit and let the user choose.

## Prototypes and experiments

Before creating an exploratory prototype, classify it.

### Disposable experiment

Treat work as disposable only when it:

- lives outside the governed project or in an explicitly disposable location;
- is not imported, packaged, shipped, or relied upon by project code;
- is not represented as an implemented baseline;
- can be removed without affecting project state.

State what question the experiment answers and how results will be evaluated.

### Project change

Treat a prototype as project implementation when it:

- modifies governed project files;
- establishes a public or internal contract;
- becomes a dependency of project code or tests;
- changes authoritative documents;
- is intended to remain after exploration.

Require an explicit implementation request and follow the implementation and recovery workflow. Do not allow useful experimental code to become an undocumented baseline silently.

## Readiness for specification

Exploration is ready for authoritative document creation when:

- the problem and intended outcome are clear;
- scope and important non-goals are known;
- principal components or responsibility boundaries are sufficiently understood;
- public contracts and persistent representations are decided or explicitly deferred;
- material constraints and dependencies are identified;
- acceptance can be expressed objectively;
- no unresolved issue would force the specification to invent a material decision.

Readiness is a recommendation, not a mode transition. Wait for an explicit request to create or restructure authoritative documents.

If the user directly requests documents before every issue is resolved, distinguish:

- blockers that require clarification;
- intentional open decisions that may be represented explicitly;
- details safely delegated to later design or implementation.

## Exploration output

When useful, provide a compact decision-state summary:

```text
Problem:
Accepted decisions:
Constraints and non-goals:
Working assumptions:
Open questions:
Discarded alternatives:
Recommended next step:
```

Keep this summary conversational unless the user asks to save or formalize it. Do not create SPEC, PLAN, LAYOUT, ROADMAP, feature documents, journal records, or implementation files solely because exploration appears complete.
