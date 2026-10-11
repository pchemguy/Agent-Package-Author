# Revision report: bundled skill references

## Campaign and state

- Campaign: `001_b4a0e23-plugin-sibling-links`; baseline `b4a0e2328dbd736f5eb808059cc110e01ed63f76`.
- Plan: [REVISION-PLAN.md](REVISION-PLAN.md).
- Working branch: `revision/001_b4a0e23-plugin-sibling-links`; target: `main`.
- State: branch implementation verified; integration pending. The final merge commit and target publication record the integration result.

## Revision evidence

| Action | Actual change and check | Status |
| --- | --- | --- |
| V-001 | Added plugin tests for sibling entry/reference links, local links, missing siblings, traversal and symlink escape, CLI/inspector warning-only exit, and contextual presentation generation. The first focused run had two expected failures: sibling links were `resource-escape`, and missing siblings did not report `resource-missing`. | Red baseline observed; tests pass with V-002 in published `228db78`. |
| V-002 | The skill validator accepts an optional resolved plugin boundary; plugin validation passes it to every child. Existing files outside a child but inside the plugin produce `WARN resource-cross-skill`; absent files and package escapes remain errors. The OpenAI presentation generator uses the same boundary for bundled children. | Implemented and verified in published `228db78`. |
| V-003 | Amended `SPEC.md`, `PLAN.md`, creator routing and the focused skill/plugin/validation references. README illustrates a named sibling handoff and a direct reference link, explicitly distinguished from the shipped example and client activation. Repaired four README links to non-shipped presentation files. Checked local links in README, creator entry and this report: no missing targets. | Implemented and verified in published `4c68da2`. |
| V-004 | `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` returned **39 tests, OK**. Creator's standalone validator and both shipped plugin variants exited `0`. A temporary two-skill plugin with entry and reference sibling links yielded two `WARN resource-cross-skill` findings, `validate_plugin.py` exit `0`, and inspector `errors: 0, warnings: 2` with exit `0`. `git diff --check main...HEAD` passed and the branch diff contains the planned files. | Branch verified for integration. No client handoff runtime was exercised. |

V-001 and V-002 form one green source checkpoint because the new tests intentionally fail against the old boundary and establish the production change's acceptance. No client runtime handoff has been tested; a warning only confirms local plugin-root containment.

## Integration boundary

The verified branch is ready for an explicit merge into `main`. The merge commit will record its source tip, final merged-state checks and publication. This report does not claim those operations occurred before they are observed.
