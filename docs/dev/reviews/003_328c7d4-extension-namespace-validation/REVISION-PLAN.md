# Revision plan: extension namespace validation

- Campaign: `003_328c7d4-extension-namespace-validation`
- Baseline: `328c7d4034ab4bd141d5b88ddabfc65ae924d76e` (`main`)
- Branch: `revision/003_328c7d4-extension-namespace-validation`
- Target: `main`

## Intake and decision

Preserve the [submitted issue](ISSUE-REPORT.md) unchanged. Use the [independent repository verification](independent/REVIEW-REPORT.md) to establish the current checkout's results and distinguish its Git baseline from the installed snapshot. Both N-01 and N-02 are accepted for repair. The creator uses a conservative lowercase ASCII, dot-separated reverse-domain policy for extension names; Agent Plugins 1.0.0 has no normative minimum of three labels. Client extension payload semantics remain client-owned.

## Execution

| ID | Work | Acceptance evidence |
| --- | --- | --- |
| V-01 | Add manifest tests for valid two- and three-label namespaces, malformed names and non-object values. Add directory tests for ordinary two-label roots and both two- and three-label symlink escapes. | Focused tests expose the two baseline failures before implementation. |
| V-02 | Update the shared namespace predicate to permit two or more well-formed labels. Diagnose invalid namespace and invalid object value separately. Scan valid two-label extension directory names as well as legacy multi-dot candidates, checking containment. | Both confirmed failures repaired; unrelated dotted folders are not misclassified as extension roots. |
| V-03 | Clarify the authoring policy and check compatibility of examples and project documentation. | Text does not imply a three-label minimum or claim that schema validates namespace syntax. |
| V-04 | Run focused and full unit suites, creator self-validation, plugin examples and inspector, CLI regression reproduction, diff checks. Publish branch checkpoints, record verified results in `REVISION-REPORT.md`, and merge the branch into `main` after review. | Evidence identifies exact commands, outcomes, remaining scope limits, and integrated commit. |

This campaign changes the offline creator validator and guidance. It does not establish runtime behavior of any host client or validate the contents of client-owned extensions.
