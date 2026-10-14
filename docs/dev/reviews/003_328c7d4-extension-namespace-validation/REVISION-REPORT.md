# Revision report: extension namespace validation

- Campaign: `003_328c7d4-extension-namespace-validation`
- Baseline: `328c7d4034ab4bd141d5b88ddabfc65ae924d76e`
- Branch: `revision/003_328c7d4-extension-namespace-validation`
- Target: `main`

## Intake and result

The [submitted issue](ISSUE-REPORT.md) is preserved as received, including its installed-snapshot hash and reproduction working-directory assumption. The [independent verification](independent/REVIEW-REPORT.md) reproduced N-01 and N-02 directly against the repository baseline. Both findings are resolved in implementation commit `ee58dd2`.

| Plan item | Evidence | Result |
| --- | --- | --- |
| V-01 | Focused pre-fix suite: 14 tests, four failures across the two-label manifest, two-label symlink, and combined message expectations. The other two-label subcase also failed. | Regression failures demonstrated before the implementation. |
| V-02 | Namespace pattern now accepts two or more well-formed labels. Invalid name and non-object value have distinct diagnostics. The directory scan includes valid two-label names and checks resolved containment. | Direct CLI: `com.openai` and `com.example.product` object-valued manifests exit `0`; `com..openai` and an array value exit `1` with their specific messages; external two- and three-label symlinks each exit `1` with `extension-containment`. |
| V-03 | Updated `agent-package-author/references/plugin-standard.md` and `docs/dev/SPEC.md` with the creator's strict naming policy and the schema's narrower type constraint. | Checked against the published Agent Plugins 1.0.0 specification and manifest schema on 2026-10-14. |
| V-04 | `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`: **49 tests, OK**. `validate_skill.py agent-package-author`, `validate_plugin.py` on both plugin examples, and `inspect_package.py` on the MCP example exited `0`; inspector reported zero errors and warnings. `git diff --check` passed before implementation commit. | Repository structural checks pass. Client extension payload behavior and host runtime loading were not tested. |

The branch records both reports, plan, source repair, tests, and this result. Integration and remote publication require observing the merge and push; this report records only the verified branch state.
