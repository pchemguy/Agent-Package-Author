# Agent entry policy revision plan

## Campaign and decision

- Campaign: `006_efd5838-agent-entry-policies`.
- Starting baseline and branch-off commit: `efd58388f93f879a452b4e94d1e4acc5abcc0941` on `main`.
- Working branch: `revision/006_efd5838-agent-entry-policies`; return target: `main`.
- Decision source: the user's request to open a new campaign, followed by the two attached Markdown files and exact AGENTS.md insertion.
- Scope: add the supplied `SKILL_DISCOVERY_PROTOCOL.md` and `WINDOWS_SHELL_POLICY.md` at repository root and insert the specified sections before `## Start here` in root `AGENTS.md`. Preserve the attachments' bytes and unrelated content.
- State: V-001 locally executed and checked; [REVISION-REPORT.md](REVISION-REPORT.md) records observed evidence. This directly accepted focused revision has no separate review finding or review report.

## Action and checks

| Action | Intended result | Verification |
| --- | --- | --- |
| V-001 | Copy both supplied policy files without edits; insert the exact Initialization and Windows shell sections at the requested AGENTS.md location. | Compare copied files byte-for-byte with supplied attachments; inspect section order and exact requested text; verify relative links; run Git's whitespace check with `core.whitespace=cr-at-eol` to preserve supplied CRLF bytes, and the repository test suite required by AGENTS.md. |

The new discovery instructions are read-only during their discovery phase. The repository currently has no `.agents/skills/` or `.agents/plugins/` entries. The Windows policy applies only to Windows execution hosts; this Linux checkout does not use its CMD rules. Neither root policy is a bundled runtime component of `agent-package-author/`.

## Persistence and stop

Commit and publish this opening plan and handoff before V-001. Commit the two root files, AGENTS.md insertion, and observed revision evidence together; push and read back that action commit. Keep the campaign branch open for any further user-directed revision; do not merge into `main` merely from this opening request. No validator behavior, format contract, or client runtime change is planned.

## Later closure authorization

The user's subsequent 2026-11-04 request to close the campaign supersedes the opening stop. After final checks and branch evidence publication, explicitly merge the complete verified campaign into the recorded `main` parent, verify the merged state, publish/read back `main`, and stop. Preserve the original action scope and closed earlier records.
