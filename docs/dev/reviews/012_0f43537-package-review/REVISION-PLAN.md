# Package review revision intake

## Identity and authority

- Campaign: `012_0f43537-package-review`.
- Starting baseline and branch-off commit: `0f435371eccf592a7d99af83a1c6f44bae14d1d2`.
- Creation parent and return target: `main` at that baseline.
- Working branch: `revision/012_0f43537-package-review`.
- User instruction: “Open package review revision campaign” on 2026-11-05.
- State: active with a focused accepted revision to skill-reference review criteria. No comprehensive package review or prior finding is invented.

## Scope and next boundary

Reserve this campaign for package review and any subsequent accepted revisions. At the review stage, pin the package and requested depth, inventory actual entries and components, and distinguish content findings from format checks and observed behavior. The APA review owners are [skill review](../../../../agent-package-author/references/skill-review.md), [plugin review](../../../../agent-package-author/references/plugin-review.md), and [validation policy](../../../../agent-package-author/references/validation-policy.md). Inspect only the applicable owners when the review scope is established; a focused question does not imply a comprehensive audit.

The user now requires each reference in a skill review to be evaluated for whether it defines a particular component of that skill's workflow. This is a content judgment, not a format check or a file-count rule. Do not use the user's named negative example as an illustration when defining the criterion. A comprehensive skill review applies it to every included reference; a focused review applies it to the selected references and reports the rest as unassessed. The user's follow-up directs standalone examples and background to the repository README or root `examples/`; skill-local `examples/` requires a strong runtime justification and explicit loading path. Keep the review-only stopping boundary and avoid an unrelated package audit. Closed campaigns 001–011 remain historical and unchanged.

| Action | Owners and outcome | Recheck |
| --- | --- | --- |
| A-001 | Add an explicit per-reference workflow-component assessment in `skill-review.md`: identify the reference's distinct operational role, entry trigger, contribution to a decision/action/result, and whether it merits a separate reference. Align design, portability and governing review guidance; route standalone examples/background outside the skill by default and require a justified runtime use for skill-local `examples/`. | Trace a cohesive procedure, shared operational guidance, and non-operative background material. Confirm the check is per file, produces a located content finding when the role is absent, and does not become a structural validator error. |
| A-002 | Verify the coupled guidance and record scoped evidence and limits. | Full repository tests, creator self-validation, active links, diff scope and no claim of full package review or client behavior. |
| A-003 | Relocate the bundled non-operative design exemplar to root `examples/` as source-only material. Remove its delivered-skill route and reconcile README, governing layout, implementation map and existing tests while retaining the illustrative source content where useful. | The delivered skill validates and has no link or runtime dependency on the root exemplar; README links resolve; the review criterion does not cite this file as its illustrative case; existing examples and tests still work. |
| A-004 | Recheck the coupled A-001/A-003 result and record the return boundary. | Full suite, validator/inspector, source links and scoped diff; leave campaign open. |

## Persistence and return

The opening checkpoint is published/read back at `4bdc4dfba6e6e96b4f5218a6ca42ca8c04b91e8d`, and the initial A-001/A-002 plan at `4ee9b0e0d9566fa6239263f6f2f9003fd9a55046`. The user's placement instruction arrived during A-001. Commit and publish the refined A-001 with its evidence and this amended plan, then perform A-002. Publish/read back that checkpoint before A-003 relocation. Verify A-004 after relocation. Keep `main` at the starting baseline and leave the campaign open for later scope or explicit closure.
