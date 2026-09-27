# In-Code Documentation Governance

Use this reference for every authorized implementation task that substantively creates or modifies code, and whenever the user requests a focused or project-wide review of docstrings, documentation comments, or other source-adjacent explanatory comments.

## Contents

- [Operating invariant](#operating-invariant)
- [Resolve authority and style](#resolve-authority-and-style)
- [Classify documentation impact](#classify-documentation-impact)
- [Apply the incremental workflow](#apply-the-incremental-workflow)
- [Write contract-focused documentation](#write-contract-focused-documentation)
- [Use language-specific defaults](#use-language-specific-defaults)
- [Verify documentation](#verify-documentation)
- [Run a project-wide review](#run-a-project-wide-review)
- [Report and record outcomes](#report-and-record-outcomes)
- [Common mistakes](#common-mistakes)

## Operating invariant

Every substantively modified production module must receive a documentation-impact review before task verification. Review does not mean adding a docstring to every symbol. It means proving that source-adjacent documentation remains accurate, sufficient, idiomatic, and proportionate to the final contract.

Perform this review after implementation behavior stabilizes and before verification. Anticipate its paths and checks during task preparation so documentation changes remain inside the recoverable transaction.

Treat documentation as part of the implemented interface when it describes public use, errors, ownership, lifecycle, state, concurrency, persistence, security, or other observable guarantees. Do not close a task while such documentation is stale merely because runtime tests pass.

## Resolve authority and style

Use this precedence:

1. Explicit path-scoped project instructions and referenced policies.
2. Enforced project configuration or documentation tooling.
3. A clearly coherent convention already used in the affected project area.
4. A recognized Google style for the language when applicable.
5. The official or predominant language and ecosystem convention.
6. Concise idiomatic documentation comments when no stable formal convention exists.

Treat a coherent existing style as an implicit project convention. Preserve it within bounded work instead of converting unaffected documentation. If styles conflict without a dominant local convention, apply the default only to new or substantively revised documentation and report the inconsistency; a project-wide normalization requires separate authorization.

For a new or inconsistent Python project without governing guidance, use professional Google-style docstrings consistent with PEP 257 fundamentals. Do not transpose Python headings into languages whose native documentation systems use different structures.

Do not invent a new dependency, linter, generator, or repository policy merely to enforce this fallback. Propose tooling separately unless its introduction is already authorized by the PLAN task.

## Classify documentation impact

Treat a code change as substantively documentation-bearing when it creates, removes, renames, or changes any of these:

- a public or exported module, package, type, function, method, field, constant, option, command, or endpoint;
- a non-public symbol with a non-obvious contract, invariant, algorithm, or failure mode;
- parameters, returns, yields, errors, side effects, mutation, state, or lifecycle behavior;
- resource ownership, cleanup, concurrency, thread-safety, asynchronous behavior, or cancellation;
- schemas, serialization, persistence, protocols, configuration, or command-line behavior;
- security-sensitive assumptions or performance constraints that affect correct use;
- behavior that makes an existing module, package, type, or callable description false or materially incomplete.

Inspect but normally do not add documentation for:

- a trivial private helper whose name and signature express its complete contract;
- self-explanatory accessors or passive data holders;
- routine tests and fixtures unless unusual setup, execution, or intent needs explanation;
- formatting-only or comment-only changes with no affected contract;
- generated or vendored code.

For generated code, identify the owning generator or template. Change generated output directly only when project rules designate it as authoritative.

## Apply the incremental workflow

### Prepare

Before the task transaction starts:

1. Discover applicable instructions, local conventions, documentation tooling, generated paths, and public API boundaries.
2. Inspect the existing module/package documentation and documentation on symbols expected to change.
3. Record the expected documentation impact in the PLAN task or task preflight.
4. Include anticipated source, stub, template, example, or API-documentation paths in transaction scope.
5. Include configured documentation checks in planned verification.

### Reconcile

After code behavior stabilizes and before verification:

1. Inspect every created or modified production module.
2. Inspect its module or package documentation and every created, removed, renamed, or behaviorally affected public symbol.
3. Inspect affected non-public symbols with non-obvious contracts or invariants.
4. Compare documentation with the final signature, implementation, tests, SPEC, and public behavior.
5. Add, update, remove, or retain documentation deliberately.
6. Remove claims, examples, parameters, exceptions, and sections belonging only to rejected or deleted behavior.
7. Search for directly affected in-code references to renamed or changed symbols.
8. Use the implementation scope-extension protocol before touching an undeclared authoritative path.

### Gate completion

A substantive code task may complete only when one of these outcomes is established:

- affected in-code documentation was reconciled with final behavior; or
- inspection established that no change was required, with a concrete reason.

Acceptable no-change reasons include an unchanged documented contract, an idiomatically undocumented trivial private detail, or an excluded generated/vendor path. Lack of time, lack of a written project policy, passing runtime tests, or absence of a docstring linter are not sufficient reasons.

## Write contract-focused documentation

Make documentation comprehensive relative to the contract, not maximally long. Include when relevant:

- purpose, audience, and intended use;
- meaningful parameter constraints, units, defaults, and relationships;
- returned or yielded values and important empty or sentinel cases;
- public errors, panics, or rejection behavior;
- side effects, mutation, state transitions, and idempotency;
- ownership, cleanup, context management, and resource lifetime;
- concurrency, thread-safety, async, cancellation, and reentrancy guarantees;
- security-sensitive assumptions;
- performance or memory characteristics that constrain correct use;
- examples for non-obvious usage or interaction.

Describe the interface and rationale a caller or maintainer needs. Keep implementation mechanics in nearby comments only when they explain a non-obvious invariant, algorithmic choice, workaround, or hazard.

Do not repeat the symbol name, signature, obvious types, or control flow. Do not document behavior that is merely hoped for. Keep terminology aligned with the SPEC and related public surfaces.

## Use language-specific defaults

Use this table only after the authority hierarchy has not selected another convention:

| Language or ecosystem | Default documentation form                                                                                                                      |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Python                | Google-style docstrings with PEP 257 fundamentals; use `Args`, `Returns` or `Yields`, `Raises`, `Attributes`, and examples only when applicable |
| TypeScript            | TSDoc for public API; use established JSDoc when the project or toolchain owns that convention                                                  |
| Java                  | Javadoc                                                                                                                                         |
| Kotlin                | KDoc                                                                                                                                            |
| C#                    | XML documentation comments                                                                                                                      |
| Rust                  | rustdoc with contract-driven `# Errors`, `# Panics`, `# Safety`, and examples where applicable                                                  |
| Go                    | Go doc comments for packages and exported declarations, following identifier-opening conventions                                                |
| Ruby                  | YARD where ecosystem tooling or local practice supports it                                                                                      |
| Swift                 | Swift Markdown documentation comments                                                                                                           |
| C or C++              | Project/tooling convention such as Doxygen when established; otherwise concise idiomatic API comments                                           |
| Shell                 | Concise file and function comments; do not invent a docstring grammar                                                                           |

Avoid duplicating types already expressed clearly by signatures unless the selected documentation tool requires them. Prefer official language documentation behavior over superficially similar cross-language formatting.

## Verify documentation

Run project-configured checks that apply to the touched documentation surface, including:

- docstring or documentation-comment lint;
- documentation generation or API extraction;
- doctests and compiled examples;
- broken intra-doc reference or link checks;
- compiler, type-checker, or linter documentation warnings;
- format checks that normalize documentation syntax.

Do not install or configure a new tool during an ordinary task unless authorized. When no dedicated tooling exists, perform a semantic comparison against final code and tests, then use ordinary parse, import, compile, type, and test checks as structural evidence.

A successful documentation build proves syntactic integration, not semantic truth. Inspect contract accuracy manually.

Record unavailable required checks as blockers. Do not describe an unexecuted documentation check as passed.

## Run a project-wide review

Treat an explicit project-wide review as its own bounded workflow. Read-only review does not authorize correction.

### Establish the review

1. Discover the project root, languages, instructions, tooling, public surfaces, generated ownership, and vendored exclusions.
2. Resolve the convention independently for each language or coherently distinct project area.
3. Define coverage. By default inspect every in-scope production module while prioritizing public/exported and contract-sensitive symbols.
4. State whether tests, examples, scripts, private helpers, generated templates, and deprecated code are included.

### Inventory findings

Classify findings as:

- missing contract documentation;
- stale or false documentation;
- incomplete parameters, results, errors, side effects, lifecycle, ownership, or concurrency semantics;
- malformed or unverifiable documentation;
- inconsistent terminology or style;
- redundant or implementation-narrating documentation;
- generated-code ownership problem;
- unresolved project-policy decision.

Distinguish contract-dangerous and public API findings from maintenance and style findings. Record positive local patterns that can serve as remediation models.

### Review or remediate

For review-only authorization, report findings without editing files, configuring tools, or creating authoritative policies.

For remediation, create or revise a PLAN before broad mutation. Divide large work by stable package or component boundaries. Make each task independently recoverable and verifiable; do not turn a repository-wide rewrite into one transaction. Preserve accurate unaffected documentation and avoid style-only churn outside each task.

Finish with affected documentation builds, lint, doctests, examples, API checks, and ordinary project regression checks. Report inspected coverage and explicit exclusions; do not equate raw docstring coverage with documentation quality.

## Report and record outcomes

For an ordinary implementation task, summarize material documentation reconciliation as supporting evidence after the implemented capability. State a no-change outcome only when useful to demonstrate that the completion gate was performed.

For dedicated documentation work, lead with the documentation capability or contract correction and state `Runtime behavior did not change.`

For a project-wide review, report:

- languages, components, and production modules inspected;
- conventions applied and confidence in inferred local conventions;
- exclusions and generated-code ownership;
- prioritized findings or documentation added, updated, and removed;
- exact checks and unavailable evidence;
- remaining gaps or policy decisions.

A `completed` journal event may include a compact `documentation` object or equivalent with the selected convention, reviewed scope, changed paths, checks, and relevant no-change reason. Do not require a schema change merely to record a trivial inspection; keep the durable capability summary primary.

## Common mistakes

| Mistake                                                        | Required correction                                                                       |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Treating no written policy as no documentation obligation      | Apply the fallback authority and style hierarchy                                          |
| Adding a docstring to every touched symbol                     | Document public and non-obvious contracts; inspect trivial symbols without forced prose   |
| Converting an established local style during a feature task    | Preserve the coherent local convention; normalize only with separate authorization        |
| Updating code first and forgetting stale docs after tests pass | Reconcile documentation before verification and completion                                |
| Editing generated output                                       | Change its authoritative generator or template when appropriate                           |
| Running a linter and assuming documentation is correct         | Review semantic agreement with final behavior                                             |
| Hiding removed capability history in current docstrings        | Describe only the accepted current contract; preserve history in journal and Git evidence |
