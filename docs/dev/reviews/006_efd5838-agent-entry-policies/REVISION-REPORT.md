# Agent entry policy revision evidence

## Campaign and result

- Campaign: `006_efd5838-agent-entry-policies`; starting baseline: `efd58388f93f879a452b4e94d1e4acc5abcc0941` on `main`.
- Plan: [REVISION-PLAN.md](REVISION-PLAN.md). Working branch: `revision/006_efd5838-agent-entry-policies`; return target: `main`.
- Decision source: the user's supplied files and exact AGENTS.md text. No separate review findings were asserted.
- State: V-001 changed and locally verified. The campaign remains open on its branch; this report does not claim a merge or a Windows-host execution trial.

## V-001 — Root agent entry policies

| Owner | Actual change | Check |
| --- | --- | --- |
| `SKILL_DISCOVERY_PROTOCOL.md` | Copied the supplied attachment to repository root without edits. | Byte comparison with the supplied file passed. |
| `WINDOWS_SHELL_POLICY.md` | Copied the supplied attachment to repository root without edits. | Byte comparison with the supplied file passed. |
| `AGENTS.md` | Inserted the requested Initialization and Windows shell sections immediately before `## Start here`; left the prior content in order. | Exact text, single occurrence, section order and both relative targets checked. |

The read-only repository discovery pass found no `.agents/skills/` or `.agents/plugins/` entries. This is a Linux execution host, so the Windows CMD probe/recovery instructions were not executed. The two root documents are project agent guidance, outside the delivered `agent-package-author/` directory.

Verification: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` passed 50 tests. File byte comparisons and exact insertion/link checks passed. The supplied files use CRLF; Git's whitespace check is run with `core.whitespace=cr-at-eol` so their unchanged carriage returns are recognized as line endings. These checks do not establish that a Windows shell tool uses CMD or that a future agent follows the discovery workflow.

The opening checkpoint was published through the connected GitHub account as `b280f44487bd493b8b71329cec1da4e720fa4313`; its tree matched the local opening commit and the checkout was synchronized to that remote tip. The V-001 action commit and remote publication follow this report's creation.

## Closure decision and finalization

The user's later 2026-11-04 “Close it” request selects campaign finalization and explicit integration into its recorded `main` parent. V-001 was published at `41931871dc3bdf1ce87d2c299efeb46a9c960cac` and read back at the exact branch ref; its tree matched the verified local action. No additional source change or separate comprehensive review was requested.

The complete branch difference from `main` at `efd58388f93f879a452b4e94d1e4acc5abcc0941` contains only the two supplied root policies, the specified AGENTS.md insertion, this campaign's plan/report, and HANDOFF. No prior closed campaign record or delivered `agent-package-author/` file changed. The attachments retain their supplied CRLF bytes. The finalization and merged-state checks will distinguish source/text verification from Windows-host behavior; no CMD shim or target-agent trial is claimed.

This record precedes the explicit merge and publication. Git history and remote readback will establish their eventual result.
