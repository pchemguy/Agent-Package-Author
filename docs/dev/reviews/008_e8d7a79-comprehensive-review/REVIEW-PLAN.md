# Comprehensive review plan

## Campaign and boundary

- Campaign: `008_e8d7a79-comprehensive-review`.
- Starting baseline: `e8d7a7941cbd3f16a411928ad236253a7e0665ce` on `main`; pin the exact source candidate for each review unit if it changes.
- Creation parent and eventual return target: `main`; working branch: `revision/008_e8d7a79-comprehensive-review`.
- Objective: independently assess the current Agent Package Author deliverable, its executable helpers and examples, and its user and developer interfaces for correctness, completeness, coherent composition, and evidence-qualified claims.
- Included: the current `agent-package-author/` entry, references, scripts, templates and presentation; `README.md`, `AGENTS.md`, active root policies and `docs/dev/SPEC.md`/`PLAN.md`; maintained examples, tests, fixtures, package links and distribution boundaries. Review the interactions among these surfaces, not merely their individual presence.
- Excluded: edits to the reviewed source, automatic fixes, installation or client behavior without an actual trial, and routine reassessment or repair of closed campaign records. Consult selected historical evidence only for a concrete provenance question; record any new findings in this campaign.
- Evidence mode: source and consumer-path assessment, independent structural checks, executable positive and negative trials, and externally sourced format comparison when standards claims are assessed. Keep those evidence classes distinct and report unavailable host or client checks.
- Authorized opening output: this plan and the entry handoff. The review report begins with the first assessed unit. Opening the campaign does not authorize source repairs or completion integration.

## Units and criteria

| Unit | Scope and dependency | Assessment criterion | Representative evidence and scenarios |
| --- | --- | --- | --- |
| U-001 | Establish exact inventory, governing contract, current baseline and normative format sources. | C-001: distribution and development boundaries are explicit; format assertions match the published versions; no current deliverable depends on a former checkout or undeclared absolute path. | Enumerate tracked paths, links, symlinks, imports and runtime dependencies; check current standards claims against primary specifications. Exercise a contained resource and a missing or escaping target. |
| U-002 | Creator entry and every current reference after U-001. | C-002: operation routing and reference loading are actionable; boundaries are cohesive and substantial without trivial fragments or overloaded subworkflows; review-only and authoring effects stay separate. C-003: skill and plugin composition covers actual optional components and handoffs. | Trace standalone creation, draft revision, focused/comprehensive review, structural-only inspection, sibling handoff, no-skill plugin, optional MCP and presentation routes. Assess each reference's trigger, ownership and consumer consequence. |
| U-003 | Python helpers, templates, validation policy, tests and fixtures after U-001. | C-004: accepted and rejected inputs, diagnostics, containment, metadata types, referenced resource coverage, and CLI statuses match stated contracts; tests challenge consequential failure paths. | Run the suite and all helper CLIs; use disposable valid/invalid packages for YAML scalars, linked references, symlinks, plugin components, MCP transport variants and presentation replacement. Check script error recovery and output claims independently of test assertions. |
| U-004 | Shipped examples and generated-package consumer paths after U-002/U-003. | C-005: examples and templates demonstrate distinct runnable workflows, accurate output, meaningful failures and declared facilities without treating local execution as client discovery. | Exercise standalone and both plugin variants; send valid and malformed requests to the local MCP example, followed by a valid request; generate and inspect child presentation in a disposable package and view the SVG at small sizes. |
| U-005 | README, root policies, current development documents and cross-surface integration after U-002–U-004. | C-006: the complete attached-seed/reference/draft walkthrough and all reference-module roles align with actual behavior; installation and runtime statements reflect observed evidence. C-007: active links, terminology, commands and agent handoff are coherent. | Follow README prompts and commands as a reader; resolve current relative links, check documented test command cleanliness, compare root instructions and project contract with observed implementation. |
| U-006 | Consolidation after U-001–U-005. | C-008: coverage accounts for every included module and material interface; findings, no-finding areas, priorities, dependencies, uncertainty and bounded rechecks are explicit. | Reconcile inventory and unit evidence; distinguish confirmed defects, recommendations and untested behavior. Recheck coupled interfaces only where earlier units expose a concrete risk. |

## Report and persistence

Create `REVIEW-REPORT.md` when U-001 begins. For each unit record the reviewed source commit, inspected paths and depth, commands and observed results, positive and negative coverage, exclusions and uncertainty. Assign stable `R-###` finding IDs with located evidence, consequence, priority, confidence, proposed owner, bounded correction and objective recheck. An old deferred finding is a historical lead, not evidence of a current defect; verify any current observation independently against this baseline.

After each unit, update and commit the report; publish and read back that commit before starting the next unit. Inspect each owned diff for incidental edits to closed campaigns. A planned check is never described as a passing check.

After U-006, return the report and prioritized revision queue and stop. Any revision plan, source repair or campaign integration requires subsequent authorization. Report actual host/client limitations and do not infer installation, activation or compatibility from structural checks.
