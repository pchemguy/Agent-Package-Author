# Reference boundary revision plan

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
