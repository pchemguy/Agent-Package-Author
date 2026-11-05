# Source cleanup revision plan

## Identity and authority

- Campaign: `013_5d0846b-cleanup`.
- Starting baseline and branch-off commit: `5d0846b592b516c7f3d79dd48a7e5ea8c544cc7a`.
- Creation parent and return target: `main` at that baseline.
- Working branch: `revision/013_5d0846b-cleanup`.
- User instructions: close campaign 012, open a cleanup campaign, then delete `examples/hello-world-design.md`, `examples/standalone/sample.md`, `SKILL_DISCOVERY_PROTOCOL.md`, `WINDOWS_SHELL_POLICY.md`, and the `## Initialization` and `## Windows shell` sections of root `AGENTS.md`.
- State: A-001–A-003 completed and verified; the campaign remains open on its branch.

## Work and checks

| Action | Files and outcome | Recheck |
| --- | --- | --- |
| A-001 | Delete the two requested example files. Remove references to the source-only design example from README and development documents. Keep the notes-tools smoke and negative cases reproducible using temporary input in tests and documented commands, without a tracked sample file. | Full suite; example script output; no active link to deleted files; README commands remain executable and expected output accurate. |
| A-002 | Delete the two root policy files and exactly the requested `AGENTS.md` sections. Preserve the remaining agent entry and update any active references to the deleted files. | No active links or remaining references to removed policies; remaining AGENTS links resolve; `git diff --check`. |
| A-003 | Verify the combined cleanup, record evidence and stop at the open campaign boundary. | Full suite, creator validator/inspector, example plugin validation, active links, scoped diff and file absence. No client behavior claim. |

Closed campaigns 001–012 remain historical and unchanged. The deletion request supersedes the earlier addition of the two policies and the source-only example. This cleanup does not amend portable format rules or the delivered skill's review criterion. A-001 and A-002 were published/read back before dependent work; publish/read back A-003's final evidence. Keep `main` at the baseline until an explicit closure request.
