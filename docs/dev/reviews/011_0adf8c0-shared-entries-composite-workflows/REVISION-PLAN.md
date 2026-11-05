# Shared entries and composite workflows revision intake

## Identity and authority

- Campaign: `011_0adf8c0-shared-entries-composite-workflows`.
- Starting baseline and branch-off commit: `0adf8c072260faf8045366984be791b156f46a2a`.
- Creation parent and return target: `main` at that baseline.
- Working branch: `revision/011_0adf8c0-shared-entries-composite-workflows`.
- User instructions: open a revision campaign for shared entries and composite workflows definition, then concisely define an optional `SKILL.md` section for composite workflows involving multiple references on 2026-11-05.
- State: A-001–A-006 are implemented, verified, published and read back. The user subsequently requested closure; the campaign is integrated into `main` by the two-parent closure commit. No preceding review finding is invented.

## Scope to resolve

The selected topic is how the creator defines and distinguishes an optional shared `PLUGIN.md` entry, a coordinator skill, shared guidance and a composite workflow; how an agent reaches their operational owners; and what remains usable when the optional shared entry is unavailable. Existing relevant owners include `agent-package-author/SKILL.md`, `references/plugin-design.md`, `references/plugin-review.md`, and their adjacent skill design/review, authoring, README and `docs/dev/SPEC.md` interfaces. Inventory these against actual package shapes and consumer paths before changing definitions. Keep published format requirements separate from APA's design/review advice; do not turn optional entries into portable discovery requirements.

The current [skill design](../../../../agent-package-author/references/skill-design.md) requires entry routing to every reference; [skill review](../../../../agent-package-author/references/skill-review.md) checks that inventory and entry-only selection. The new composite summary complements this existing routing rather than replacing it. Unlike an optional plugin-level `PLUGIN.md` file, this is an optional **section within the required skill entry**. A skill with several independent reference choices needs no composite section just because the file count exceeds one.

| Action | Owners and outcome | Recheck |
| --- | --- | --- |
| A-001 | Add a concise conditional composite-workflow pattern to `skill-design.md` and its corresponding optional content check to `skill-review.md`. State selection, principal reference owners, sequence/handoffs, output/stop, and avoidance of duplicate procedures; preserve the direct per-reference routing policy. | Trace a single-reference skill, independent multi-reference variants, and an actual composite path with and without a section. Confirm that a present section gives entry-level selection while linked references remain canonical; check the existing plugin-level analogy without conflating the two. |
| A-002 | Verify the coupled content and repository regression, record scope/evidence and prepare the later return boundary. | Skill self-validation, full test suite, active links and scoped diff, with untested agent behavior stated. |
| A-003 | Correct `plugin-design.md`'s reverse handoff into `plugin-review.md`: give authoring guidance for meaningful cross-skill composites, optional shared `PLUGIN.md` projection and coordinator ownership in the design owner itself. Remove the review-only no-skill instruction already owned by `plugin-review.md`. | Trace direct focused, composite-without-coordinator, optional shared-entry unavailable and coordinator direct-entry paths against the existing review criteria; ensure no portable discovery or mandatory coordinator claim. |
| A-004 | Recheck the coupled skill/plugin guidance and current campaign scope after A-003. | Self-validation, full suite, active links and diff against baseline; record limits and leave campaign open pending closure instruction. |
| A-005 | Put `## Shared plugin entries and coordination` in `plugin-design.md`. Define optional root `PLUGIN.md` and coordinator as APA design patterns, their supported loading/entry paths, canonical ownership and composite workflow placement. Explain these nonstandard concepts in README. Refine `plugin-review.md` to assess those decisions without supplying general introductions. Update entry routing if needed. | Trace direct focused skill, composite without coordinator, coordinator direct entry, optional shared entry present/unavailable, and both handoff sides. Confirm format claims against Agent Plugins 1.0.0 and avoid a second full procedure catalog. |
| A-006 | Recheck the coupled guidance and publish the action evidence. | Full suite, self-validator and inspector, Markdown links, scoped diff and campaign state; report unobserved client behavior. Keep campaign open. |

No governing SPEC/PLAN amendment is needed for this bounded authoring/review refinement; their existing entry, reference and plugin composition requirements remain compatible. No change to portable format rules or Python structural validation is authorized. Closed campaigns 001–010 remain unchanged.

The user's follow-up identified that `plugin-design.md` sends an author to the review checklist for detailed composition and coordinator criteria. That reverses design/review ownership. A-003 adds concise design decisions in the authoring owner while `plugin-review.md` retains its existing assessment questions; no duplicate checklist is needed.

The user's conditional factoring rule applies if both paths actually consume one checklist. The entry routes design before authoring and review during assessment; after A-003 the design owner states decisions without consuming the review checklist. Inspect this boundary before deciding whether a shared reference is warranted; do not create a trivial third file solely because both modules discuss the same concepts.

## Persistence and return

The A-001–A-006 checkpoints, including source and verification evidence, were published and read back before the explicit closure request. The closure merge retains the branch and this record as history.
