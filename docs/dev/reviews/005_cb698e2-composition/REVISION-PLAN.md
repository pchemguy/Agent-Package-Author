# Composition revision plan

## Campaign and decisions

- Campaign: `005_cb698e2-composition`; starting baseline: `cb698e2c0d541a730a3070933778a66f6404a7fc`.
- Current revision source: `8d18fbbc35e72303719179367438aef0e6fa7d27` on `revision/005_cb698e2-composition`; return target: `main`.
- Review basis: [REVIEW-REPORT.md](REVIEW-REPORT.md), U-000 / C-000; revision report: `REVISION-REPORT.md` is planned.
- User decision: 2026-10-18 request to plan and execute the two recommended changes. R-001 and R-002 are accepted as paired guidance improvements. U-001–U-005 remain pending review and are not implicitly accepted revisions.
- Scope: edit the current skill design and skill review references, record checks and dispositions, commit and push the action. Do not edit plugin design/review, validators, examples, closed campaign records or the format specifications. Do not merge or close the wider campaign while planned review units remain incomplete.

## Authoritative project contract

The existing [SPEC.md](../../SPEC.md) §§4–5 already calls for minimum justified resources, conditional loading, direct routing and content review. These two recommendations operationalize that contract without creating a new `SHALL` or formal format condition. If later review identifies an actual contract gap, the document owner can amend SPEC through a separate accepted preparation step. `docs/dev/PLAN.md` needs no action for this bounded textual clarification.

## Ordered revision

| Action | Findings | Owners and intended outcome | Dependencies and recheck |
| --- | --- | --- | --- |
| V-001 | R-001, R-002 | In `skill-design.md`, articulate the two-sided reference boundary decision: broad/shallow guide or narrow/deep procedure, sufficient coherent substance, meaningful independent loading trigger, combine thin fragments, split a distinct substantial subworkflow, preserve caller route and prerequisites. In `skill-review.md`, use the same decision as a paired assessment without imposing a length threshold. | Review report and accepted scope. Source-trace a complete short guide, a thin vague fragment, and a broad procedure with a separately selected substantial path. Check plugin delegation and entry routing remain intact. Run creator structural validation, full test suite, current Markdown link and whitespace checks; record source-only versus observed behavior separately. |

## Persistence and stop

Keep both owner edits and V-001 evidence in one action commit, then push and verify remote containment before any further campaign unit. Mark baseline observations unchanged and append current dispositions in the active report. The next campaign unit is U-001; source changes from V-001 are inputs to it, not proof its general review is complete. This request executes only V-001 and stops on the published campaign branch. A later completed campaign boundary governs integration into `main`.

## V-002–V-005: accepted wider review revisions (2026-10-18)

The later request to prepare and execute a revision plan accepts R-003–R-010 from the completed U-001–U-005 review. The current starting tip is `542ad51cc716a2a48a97ff76f38adf4a76cd283b` on the same revision branch; [REVIEW-REPORT.md](REVIEW-REPORT.md) retains the original source observations. R-001/R-002 remain completed V-001, not work to repeat. No finding is rejected or deferred.

**Governing decision:** SPEC §5 requires an OpenAI presentation pair after APA authors each skill. These files are client-specific and do not change the portable format requirements. Clarify the selected module and README under that rule; no SPEC/PLAN, validator, manifest, or example package behavior change is needed. This is a source-guidance revision, not an external standard or client trial.

| Action | Findings | Files and intended outcome | Recheck and completion boundary |
| --- | --- | --- | --- |
| V-002 | R-008, R-010 | `references/openai-presentation.md`, `README.md`: align creation/revision and review-only triggers with APA's per-skill deliverable; distinguish shipped examples from generated deliverables. | Generic standalone and two-child plugin trace to presentation pairs; existing-file replacement remains deliberate; review-only writes none. Commit source and evidence, push/read back. |
| V-003 | R-003, R-004 | `SKILL.md`, `references/authoring-workflow.md`: group authoring stages in entry and subdivide workflow step 6 within its present module. | Locate collision gate, portable content review, per-skill presentation, structural/behavioral verification and report in sequence; no new review-only effects or tiny reference. Commit source and evidence, push/read back. |
| V-004 | R-005 | `references/hello-world-example.md`: add a compact illustrative requirement-to-resource decision map for common contract, conditional audience references, template, renderer and independent validator. | Selected reference is useful without README or missing attachments; simpler skills can omit every unjustified component. Commit source and evidence, push/read back. |
| V-005 | R-006, R-007, R-009 | `references/validation-policy.md`, `references/mcp-packaging.md`, `README.md`: organize review scope/evidence/trial rules, align existing-MCP assessment trigger, and promote the shared map to a peer README section. | Focused/comprehensive/trial rules remain distinct; existing MCP review does not authorize writes; twelve map rows still match entry. Run repository suite, structural checks and local-link/whitespace review. Commit source and evidence, push/read back. |

Each action updates [REVISION-REPORT.md](REVISION-REPORT.md) with actual files, source rechecks, checks and limits in the same commit. Do not rewrite U-001–U-005 baseline observations; append disposition evidence in the revision report. Preserve the original V-001 section above as its historical plan. After the coupled edits, inspect the complete branch delta against `main`, verify no closed campaign records changed, refresh HANDOFF at campaign finalization, and explicitly merge the complete verified branch into its recorded parent `main` with a campaign integration summary. Verify merged state, push/read back `main`, and stop. If an acceptance check or publication fails, preserve the actual branch state and report the blocker instead of marking completion.
