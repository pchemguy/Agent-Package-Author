# Capability-Oriented Reporting

Use this reference for project status and every task, milestone, phase, campaign, checkpoint, steering, recovery, or blocked-work report.

## Contents

- [Reporting invariant](#reporting-invariant)
- [Evidence and truthful language](#evidence-and-truthful-language)
- [Outcome categories](#outcome-categories)
- [Task completion reports](#task-completion-reports)
- [Milestone completion reports](#milestone-completion-reports)
- [Phase completion reports](#phase-completion-reports)
- [Campaign completion reports](#campaign-completion-reports)
- [Checkpoint and steering reports](#checkpoint-and-steering-reports)
- [Status and non-completion reports](#status-and-non-completion-reports)
- [Journal summaries](#journal-summaries)
- [Multi-task runs](#multi-task-runs)
- [Report quality checks](#report-quality-checks)

## Reporting invariant

Lead with what verified capability now exists, changed, or was removed. File lists, commit identifiers, test counts, and implementation mechanics are evidence; they are not the capability summary.

Every completed task, milestone, phase, and campaign report must summarize implemented features or enabling capabilities at that boundary's natural level.

Keep reports self-contained. A user should not need earlier progress messages to understand what completed, what was verified, the current durable state, and what may happen next.

## Evidence and truthful language

Base claims on reconciled SPEC, PLAN, ROADMAP, journal, recovery, filesystem, verification, and Git evidence as applicable.

Use precise states:

| Evidence                                             | Report language                                           |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Required implementation and verification are durable | completed                                                 |
| Checks passed but a required Git commit is absent    | verified but not durably completed                        |
| Transaction is prepared or partially changed         | prepared or partially implemented                         |
| Exact baseline was restored                          | reverted; no implementation completion claimed            |
| A required check failed or is unavailable            | blocked or incomplete                                     |
| Evidence conflicts                                   | status uncertain; preserve evidence and identify conflict |
| Requested range completed and clean                  | awaiting steering                                         |

Do not say “complete,” “implemented,” “fixed,” or “supported” when required verification is missing. Distinguish observed evidence from inference.

## Outcome categories

Describe the actual outcome category when “feature” would be misleading:

- user-visible runtime feature;
- enabling infrastructure;
- test or verification capability;
- documentation or contract clarification;
- defect correction;
- migration or compatibility step;
- removal of obsolete or rejected behavior;
- operational hardening;
- architectural preparation with no exposed behavior yet.

For documentation-only, test-only, planning-only, or infrastructure-only work, explicitly state: `Runtime behavior did not change.` Add the capability that did change, such as stronger validation, clearer contract ownership, or future implementation readiness.

## Task completion reports

Report one task as:

1. **Task:** canonical task identity and semantic name.
2. **Implemented capability:** the incremental behavior or enabling outcome delivered by this task.
3. **Boundaries:** important unsupported behavior, deliberate exclusions, or unchanged contracts.
4. **Documentation:** material in-code documentation reconciled with the delivered contract, or a useful no-change conclusion.
5. **Verification:** required direct and affected checks, summarized by outcome; identify any justified omissions.
6. **Durability:** journal/commit/cleanup state as applicable.
7. **Progress:** completed and total tasks plus containing milestone and phase when trustworthy.
8. **Next boundary:** next canonical task or the reached HIL stopping boundary.

Keep documentation subordinate to the capability summary for ordinary implementation work. For a dedicated in-code documentation review or remediation, use `in-code-documentation.md` for the review coverage and finding fields.

Example for a runtime feature:

```text
Task “ZIP stream backend” completed. The package can now expose the single text member
of a ZIP archive as the common sequential byte stream, including ownership-safe close
and public error translation. Encrypted ZIP input remains unsupported. Focused backend,
registry, and stream-lifecycle checks passed. Progress: 8/25 tasks; ZIP support milestone
complete. The project is awaiting steering before TAR work.
```

Example for enabling infrastructure:

```text
Task “archive fixture foundation” completed. Tests can now generate valid and malformed
archives through one shared fixture interface, enabling consistent backend conformance
checks. Runtime package behavior did not change. Fixture validation and existing tests
passed. Progress: 2/25 tasks; next task is the ZIP backend.
```

Example for documentation-only work:

```text
Task “public error contract” completed. The SPEC now defines which archive failures map
to each public exception and gives implementation and test tasks one canonical contract.
Runtime behavior did not change. Cross-document links and PLAN acceptance coverage were
verified. Progress: 4/25 tasks; next task is public error translation.
```

Do not turn a task report into a raw changed-file inventory.

## Milestone completion reports

Synthesize the integrated capability delivered by all milestone tasks. Do not concatenate task summaries.

Include:

- milestone name;
- integrated supported behavior or enabling capability;
- important guarantees and exclusions;
- milestone-level verification;
- completed/total milestone and task progress;
- next milestone or checkpoint state.

Example:

```text
Milestone “ZIP support” completed. ZIP archives now use the same public stream and line
index interfaces as plain input, with single-member validation, cleanup guarantees, and
consistent public errors. Encrypted and multi-file archives remain unsupported. Backend,
registry, index, and lifecycle verification passed. Progress: 3/12 milestones and 8/25
tasks. The project is awaiting steering before TAR support.
```

## Phase completion reports

Summarize the phase's major project capability rather than its internal task sequence.

Include:

- phase name and major capability now available;
- public workflows and cross-component guarantees delivered;
- important scope boundaries;
- phase acceptance results;
- cumulative phase, milestone, and task progress;
- remaining phases or campaign status;
- `awaiting-steering` when the requested phase was the stopping boundary.

Example:

```text
Phase “Archive streams” completed. Applications can consume plain, ZIP, TAR-family, and
7z single-file sources through one sequential stream contract, with bounded buffering,
consistent ownership, cleanup, integrity, and public failure semantics. Password-protected
archives remain unsupported. Cross-format lifecycle and indexing acceptance passed.
Progress: 2/4 phases, 5/12 milestones, 13/25 tasks. The project is awaiting steering.
```

## Campaign completion reports

Report the final usable system or accepted change, not merely that all tasks were checked.

Include:

- complete delivered user and developer capabilities;
- important final non-goals and compatibility boundaries;
- architecture or operational guarantees material to use;
- final acceptance, packaging, installation, migration, or release evidence;
- authoritative-document normalization status;
- final progress totals;
- release or handoff status.

For a change campaign, state how the final delta was integrated into the main current-state documents and whether temporary change documents were retired.

## Checkpoint and steering reports

At an ordinary checkpoint, report:

- the completed requested range and synthesized capability;
- verification and durable-clean state;
- current progress;
- exact next planned boundary;
- that no further work will begin without explicit direction.

After focused steering, report the resulting final state rather than narrating every removal step:

- final supported capability;
- behavior explicitly removed or now rejected;
- whether public contracts or compatibility changed;
- normalized SPEC/PLAN/LAYOUT/ROADMAP/verification-map state;
- affected verification;
- revised progress totals;
- paused checkpoint status.

Example for capability removal:

```text
Checkpoint revision completed. 7z support now accepts only unencrypted archives and
rejects encrypted input through the documented unsupported-input error. Encryption code,
success fixtures, options, dependency paths, and examples were removed; the negative
contract test remains. Current-state documents and the roadmap now describe the reduced
design directly, while journal and Git history remain intact. Affected 7z and archive-phase
checks passed. The project remains awaiting steering; the next planned phase is persistence.
```

## Status and non-completion reports

Do not use completion-report structure for work that did not complete.

### Blocked

State:

- the exact task and current transaction state;
- what required evidence or check failed or is unavailable;
- whether project paths were modified;
- whether recovery data is intact;
- the smallest decision or resource needed to proceed.

### Reverted

State:

- which task was interrupted;
- that its entire declared baseline was restored and verified;
- that no feature completion is claimed;
- whether the task may restart with a new identifier.

### Partial or prepared

State what has been prepared or changed without describing it as an available capability. Identify the safe recovery or continuation route.

### Unverified

Describe implementation as present but unverified. Name the missing evidence and do not check ROADMAP completion.

### Status inspection

For read-only status, report reconciled progress, current phase/milestone/task, transaction state, next canonical boundary, and any evidence disagreement. Use `roadmap.md` for counts and `project-discovery.md` for source reconciliation.

## Journal summaries

Every `completed` record must contain a concise `summary`. It may also contain structured `features`, `boundaries`, and `verification` fields.

Write summaries as durable reconstruction material:

- identify the delivered capability, not merely actions performed;
- distinguish runtime behavior from enabling work;
- state meaningful exclusions;
- include concise milestone or phase synthesis when the task closes that boundary;
- keep detailed manifests, file hashes, and large output outside the summary.

Steering records should contain concise added, changed, and removed capability lists sufficient to reconstruct later checkpoint reports.

## Multi-task runs

For a request spanning several tasks:

1. Provide concise task-boundary progress after each durable task.
2. Add synthesized milestone reports whenever a milestone closes.
3. Add a synthesized phase report whenever a phase closes.
4. Do not repeat identical verification details at every aggregation level.
5. End with one self-contained report for the full requested range.
6. State that the project is awaiting steering and identify the next boundary.

Intermediate updates may be compact, but the final report must stand alone if earlier updates are collapsed.

## Report quality checks

Before sending a report, confirm:

- the opening sentence states the outcome;
- every capability claim is supported by completed verification;
- the aggregation level matches the boundary;
- higher-level reports synthesize rather than concatenate;
- file lists, test counts, and commit IDs are supporting evidence only;
- runtime-neutral work is labeled explicitly;
- exclusions and unsupported behavior are not hidden;
- progress numbers come from reconciled current PLAN and ROADMAP structure;
- the next boundary and authorization state are explicit;
- blocked, partial, reverted, and unverified work is not described as complete.
