# Project Discovery and State Inspection

Use this reference before document work on an existing project, before implementation or recovery, and whenever the user asks for project status. Discovery is read-only unless the user separately authorizes repair or implementation.

## Contents

- [Discovery outcomes](#discovery-outcomes)
- [Locate the project](#locate-the-project)
- [Discover governing instructions](#discover-governing-instructions)
- [Discover development documents](#discover-development-documents)
- [Discover repository state](#discover-repository-state)
- [Discover project tooling](#discover-project-tooling)
- [Inspect SDD execution state](#inspect-sdd-execution-state)
- [Classify project status](#classify-project-status)
- [Build the authority map](#build-the-authority-map)
- [Report without mutating](#report-without-mutating)

## Discovery outcomes

Establish enough evidence to answer:

- What directory is the governed project root?
- Which instructions apply to the contemplated paths?
- Which documents define intended behavior, implementation order, and physical ownership?
- Is an initial or change campaign active?
- Is the project Git-backed?
- Are target paths clean, dirty, staged, untracked, or owned by active recovery state?
- What task, milestone, phase, or checkpoint is current?
- Which commands and policies govern verification?
- Is it safe to select new work?

Do not infer safety from the apparent plausibility of existing files.

## Locate the project

Start from the user-provided path or current working directory.

Identify candidate roots using evidence such as:

- an explicit user path;
- a repository root;
- `docs/dev/` and authoritative document roots;
- project configuration and package metadata;
- root instruction files;
- source and test roots.

Distinguish the governed project root from a containing workspace or monorepo root. A project may be a nested subproject inside a larger Git repository.

Use the narrowest root that owns the project's authoritative documents and implementation while still allowing applicable parent-scoped instructions to be discovered.

When several candidates remain materially plausible, present them and ask rather than choosing silently.

## Discover governing instructions

Locate and read:

- repository-root `AGENTS.md` when present;
- every more deeply scoped `AGENTS.md` whose directory contains an anticipated target;
- `docs/dev/PROJECT.md` when present;
- files explicitly referenced by those instructions;
- equivalent project-defined instruction sources.

Resolve relative references from the referring document's directory unless it defines another rule.

Extract applicable requirements including:

- supported language and dependency versions;
- formatting, naming, and documentation conventions;
- architecture and import restrictions;
- permitted and prohibited tools;
- generated-file policies;
- required build, test, lint, type-check, package, or release commands;
- completion and commit requirements.

For work that may create or modify code, also determine whether documentation conventions are explicit, tool-enforced, coherently implicit in nearby source, inconsistent, or absent. Identify public API boundaries, generated or vendored paths, and the authoritative generator or template for generated documentation.

Instruction scope is path-sensitive. Determine applicable instructions for every anticipated target. If later work expands into another directory, repeat discovery for the added scope before preparation or mutation.

If an applicable source is missing, unreadable, contradictory, or conflicts with another authority without a precedence rule, classify the state as blocked and request direction.

## Discover development documents

Inspect the expected root and project-defined equivalents for:

```text
docs/dev/SPEC.md
docs/dev/spec/
docs/dev/PLAN.md
docs/dev/plan/
docs/dev/layout.md
docs/dev/layout/
docs/dev/ROADMAP.md
docs/dev/verification-map.json
docs/dev/PROJECT.md
docs/dev/FEATURE-SPEC.md
docs/dev/FEATURE-PLAN.md
```

Do not assume absence is an error for a small or pre-SDD project. Record what exists and what role it appears to serve.

For the main document set, determine:

- whether root documents exist and are readable;
- whether child nodes referenced by roots exist;
- whether roots provide orientation or are link-only;
- whether SPEC, PLAN, LAYOUT, and ROADMAP appear mutually aligned;
- whether the verification map describes current implemented paths.

For temporary change documents:

- if neither exists, no file-based change overlay is active;
- if both exist, read the main baseline plus the explicit delta;
- if exactly one exists, classify the state as inconsistent and ask;
- if they conflict with the main baseline without explicitly defining a revision, stop before implementation.

When a journal campaign record exists, its declared document set governs resumption after confirming that the files agree with it.

## Discover repository state

Determine whether the project root is inside a Git worktree. If it is:

1. identify the Git root;
2. record the current branch and `HEAD` without changing either;
3. inspect staged, unstaged, untracked, deleted, and renamed paths;
4. distinguish project paths from unrelated monorepo paths;
5. inspect recent task commits only when needed for recovery or status;
6. never assume a clean working tree from an empty diff of one path class.

Classify existing changes by relationship to the contemplated scope:

| Change                                            | Treatment                                                   |
| ------------------------------------------------- | ----------------------------------------------------------- |
| Target path changed by an active valid task       | Resolve through recovery                                    |
| Target path changed with no established ownership | Stop and ask before mutation                                |
| Unrelated dirty path                              | Preserve; do not modify, stage, restore, or commit          |
| Disposable ignored tool output                    | Exclude from source and clean only when authorized and safe |
| Unexpected generated or backup-like file          | Investigate; do not delete automatically                    |

If Git is absent, do not downgrade recovery or verification. Use filesystem, journal, manifest, and backup evidence.

## Discover project tooling

Inspect project configuration and instructions for the actual commands used to:

- run focused unit tests;
- collect tests without executing them when supported;
- run dependent and integration tests;
- lint and format;
- type-check;
- build;
- package;
- validate generated artifacts;
- lint docstrings or documentation comments;
- build or extract API documentation;
- run doctests, compiled examples, or documentation-link checks;
- execute full acceptance checks.

Prefer project-declared commands over familiar generic alternatives. Do not install or change tooling during read-only discovery.

Identify:

- test roots and naming conventions;
- source-to-test layout conventions;
- documentation syntax and style used in representative production modules;
- documentation generators, linters, API extractors, doctest systems, and example runners;
- markers, suites, or test categories;
- supported runtime versions;
- platform-specific commands;
- expensive or environment-dependent checks;
- commands unavailable in the current environment.

Record unavailable required checks as prospective blockers rather than silently substituting weaker checks.

## Inspect SDD execution state

Look for project-defined equivalents of:

```text
IMPLEMENTATION_LOG.jsonl
.implementation-state/
```

When they exist:

1. parse complete journal lines in order;
2. identify the latest campaign;
3. identify the latest task and its durable events;
4. locate matching recovery directories and manifests;
5. compare manifest versions and hashes recorded by the journal;
6. compare declared task paths with filesystem and Git state;
7. locate matching `Task: <task-id>` commits when Git is available;
8. identify checkpoint and steering state.

After classification, route every nonterminal task and every unexplained recovery directory through `recovery.md` before selecting new work. Status inspection itself remains read-only; only an explicitly authorized implementation or recovery workflow may restore, complete, or clean a transaction.

Treat a clearly truncated final JSONL append as potentially recoverable only when preceding records and recovery data make state unambiguous. Corruption before the final record is an escalation condition.

Do not delete stale-looking recovery data during inspection. First establish whether it belongs to an active, completed, or unknown task.

## Classify project status

Use the narrowest accurate classification.

### Design and documentation states

- `exploration-only`: no authoritative document set is established.
- `specified-not-planned`: a usable SPEC exists without a complete PLAN.
- `planned-not-ready`: PLAN exists but required supporting state is incomplete or inconsistent.
- `ready-to-implement`: authoritative documents are sufficient and no active transaction blocks work.
- `under-review`: document correction is active and implementation is not authorized.

### Campaign and task states

- `campaign-not-started`: governing documents exist but no campaign record exists.
- `started-not-prepared`: latest task has `started` without matching `prepared`.
- `prepared-incomplete`: latest task is prepared without completion.
- `completed-uncommitted`: completion exists but required Git commit does not.
- `committed-not-cleaned`: matching commit exists but recovery data remains.
- `between-tasks`: previous task is durable and clean; next task may be selected when authorized.
- `awaiting-steering`: requested range completed and continuation awaits user direction.
- `phase-complete`: phase boundary verification passed and state is clean.
- `campaign-complete`: campaign acceptance passed and change integration is complete.
- `reverted`: latest task scope was restored and may be restarted with a new identifier.

### Failure state

- `inconsistent-or-ambiguous`: evidence conflicts, required data is corrupt or missing, ownership is uncertain, or more than one task appears active.

Do not collapse `completed-uncommitted`, `committed-not-cleaned`, or `awaiting-steering` into `between-tasks`.

## Build the authority map

For the contemplated action, record or internally establish:

```text
project root:
Git root and HEAD, if any:
applicable project instructions:
main SPEC and relevant children:
active change specification, if any:
main PLAN and relevant children:
active change plan, if any:
LAYOUT owner for target paths:
ROADMAP location and status:
verification-map location and status:
journal campaign and task state:
required verification commands:
blocking conflicts or unknowns:
```

Keep the map scoped to the requested work. Do not load the entire document tree when roots and focused children are sufficient.

## Report without mutating

A status response should state:

- the classified project state;
- the current campaign, phase, milestone, and task when established;
- durable completion counts when ROADMAP is trustworthy;
- active recovery or inconsistency concerns;
- the next canonical task or decision;
- what authorization is required to proceed.

Distinguish evidence from inference. If ROADMAP, journal, filesystem, or Git disagree, report the disagreement instead of selecting the most favorable source.

Do not, during read-only status inspection:

- edit documents;
- check roadmap items;
- append journal records;
- restore backups;
- stage or commit files;
- clean generated or recovery data;
- begin the next task.
