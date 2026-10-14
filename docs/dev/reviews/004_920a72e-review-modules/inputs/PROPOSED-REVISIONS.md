# Proposed Agent Package Author revisions

## Objective and package status

Extend Agent Package Author with review modules for skills/references and plugin-level composition, routing, composite workflows and optional coordination. Its current skill-design and validation guidance already covers parts of this subject; integrate the proposed material with those owners instead of maintaining parallel instructions. Use existing APA format guidance for conformance; skill-review.md and plugin-review.md supply assessment criteria. The plugin module explains the custom-entry boundary where relevant without turning the skill module into a standard-format introduction.

This is a developing proposal package in SDD Manager campaign 060. It has not been integrated into Agent Package Author, installed or behaviorally accepted. The review modules, proposal and provenance remain in this campaign; the accepted SDD contract is maintained at docs/dev/PLUGIN-CONTRACT.md. APA transfer/integration remains unselected. This document records the proposed downstream scope; the receiving agent must establish its actual repository, instructions and authorized effects before execution.

## Package contents and reading order

| File | Role in the downstream revision |
| --- | --- |
| [skill-review.md](skill-review.md) | Shared criteria plus distinct entry/reference review sections, proposed for APA's references; read after this proposal |
| [plugin-review.md](plugin-review.md) | General plugin composition, PLUGIN.md rationale, shared-entry and coordinator review; second APA integration candidate |
| [PLUGIN-CONTRACT.md](../../PLUGIN-CONTRACT.md) | Independent SDD Manager contract integrating plugin-entry and coordinator responsibilities/cases; domain example, not APA policy |
| [PLUGIN-CONTRACT-DRAFT.md](PLUGIN-CONTRACT-DRAFT.md) | Relocated original plugin contract; provenance and abstraction source, not an integration candidate |
| [COORDINATOR-CONTRACT-DRAFT.md](COORDINATOR-CONTRACT-DRAFT.md) | Preserved mixed source used for the split; provenance and comparison, not the integration candidate |
| [REVISION-PLAN.md](REVISION-PLAN.md), [REVISION-REPORT.md](REVISION-REPORT.md) | Campaign authority, change/check evidence and current limitations |
| [REVIEW-REPORT.md](REVIEW-REPORT.md) | Earlier text findings and latest full-set review, with accepted revisions and source rechecks; behavioral trials remain unrun |

## Review activation policy

A **full or comprehensive review of a skill** should load and apply skill-review.md. A **full or comprehensive review of a plugin** should load and apply plugin-review.md, with skill-review.md covering included skills/references as required by that scope.

Ordinary or focused review requests should **not automatically trigger these review programs**. Preserve the narrower requested workflow and existing review guidance. An explicit request to use either proposed module can select it at a narrower scope; full/comprehensive activation does not authorize repairs or unrelated effects.

Make these distinctions explicit in APA’s entry routing and activation guidance. Apply the trigger to the reviewed skill/plugin, not to an unrelated project merely using a plugin. For comprehensive review, inventory the requested target and account for each item's reviewed depth and evidence, reason for exclusion or unassessed status. Representative cases do not replace content coverage; a focused check retains its narrower scope.

## Proposed integration

| APA owner | Proposed change |
| --- | --- |
| `references/skill-review.md` | Add the general skill/reference module, adapting only to established APA terminology, routing and packaging conventions |
| `references/plugin-review.md` | Add component composition, conditional shared-entry and coordinator review, text composition and evidence-before-selection checks, preserving independence from SDD policies |
| `SKILL.md` | Route full/comprehensive skill or plugin review to the appropriate module under Review activation policy, with clear conditional links; ordinary/focused reviews retain their narrower workflow; where APA supplies `references/*.md`, its entry routing must individually name/link every such file with scope/boundary and use conditions; preserve creation, revision, inspection and structural-validation paths |
| `references/skill-design.md` | Keep skill design principles under this owner; link the review procedure where useful and consolidate overlapping review detail |
| `references/plugin-design.md` | Keep plugin design guidance under this owner; route composition/coordinator review to plugin-review.md and consolidate overlapping assessment guidance |
| `references/validation-policy.md` | Distinguish structural conformance, content/ownership review and observed workflow behavior; route to the appropriate review module without duplicating its checklist |
| `references/authoring-workflow.md` | Include proportionate content review before reporting an accepted authoring/revision result; a focused review need not force complete reauthoring or every behavioral trial |
| Maintained README/development guidance | Explain the new review capability and actual checks where affected; preserve unrelated presentation and examples |

Inspect the current target sources before adopting these proposed integration points. They derive from the installed APA reference structure, not an independent review of its current repository. Do not treat the proposal as proof that those owners are defective or absent.

## Boundaries to preserve

- Keep both modules vendor-neutral. Skill review applies to simple and composite skills; plugin review accounts for advertised skill and non-skill components, distinguishes independent bundles from integrated workflows and reviews a coordinator only when present. Skill-entry criteria apply to skill workflows; packages without skills acquire no skill requirement.
- Optional references, scripts and assets remain optional; no fixed total section count, byte/token quota or new skill dependency is introduced. A dedicated routing section is required when `references/*.md` files are present.
- Keep SDD-specific document approvals, task/commit rules, Git pushes, hosted phase/milestone projection and campaign lifecycle out of general APA guidance. The combined SDD contract demonstrates how domain constraints specialize general criteria.
- Preserve APA's standalone-versus-bundled resource containment and structural validation rules. The review modules complement those checks; they do not redefine the Agent Skills/Plugins specifications or guarantee client invocation.
- Preserve explicit scope and editing authority. A review returns findings; accepted repairs follow the receiving workflow's actual authorization and persistence policy. Do not add approval gates or Git publication rules from the source example.
- Keep preserved drafts as comparison material. No need to ship the SDD contract, campaign records or this proposal with APA. Do not edit the installed cache as a substitute for durable target-repository integration.

## Downstream verification and acceptance

Verify conditional discovery of both review procedures, links/anchors and actual package contents with existing APA tooling. Check agreement with the design, validation and authoring owners.

For plugin review, assess skill-only, mixed and no-skill applicability against actual advertised components and their supported discovery paths and interfaces. Use owning configuration and runtime checks for non-skill components. Assess independent capability requests, integrated entry/fallback, optional coordination, contextual follow-ups and cross-skill handoffs where applicable. Do not make skills, a coordinator or PLUGIN.md mandatory for every plugin.

Check that comprehensive review accounts for the full requested target, including exclusions and unassessed material, while focused requests retain their narrower scope. Assess visible section responsibilities and paragraph and step cohesion without requiring fixed headings. Coordinator selection and its consequential announcement must follow sufficient reused/recovered evidence, with no duplicate orientation or routine restart.

For skill review, compare the supplied `references/*.md` inventory with entry routing; evaluate request-to-reference selection from SKILL.md before exposing reference contents. Treat complete routing as proposed authoring/review policy, not a new specification claim. Include simple entries, procedure/guidance/contract/example references, branched instructions, repeated gates, unavailable dependencies and assessment-only requests. Check that shortening or relocation preserves conditions, qualifiers and the documented reading context. References must not inherit skill-root activation, metadata or whole-workflow responsibilities by default.

Choose representative successful, negative, variant and recovery cases appropriate to the changed instructions. For behavioral assessment, record source/model/context, actual actions and output; do not give reviewer expectations to the consumer. Structural validation and source review must not be reported as behavioral acceptance. Do not add tests that merely assert prose wording.

Report implemented versus proposed scope, source/static checks versus observed behavior, unrun facilities and the exact publication/integration boundary. The current package's checks are recorded in the campaign report; no downstream APA verification is claimed here.
