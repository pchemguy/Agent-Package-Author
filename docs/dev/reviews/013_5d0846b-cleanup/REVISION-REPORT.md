# Source cleanup revision report

## A-001 — Remove source examples

Deleted `examples/hello-world-design.md` and `examples/standalone/sample.md`. README no longer links the former and describes its supplied design exemplar as input material. The notes-tools walkthrough creates and removes a disposable note for its script smoke commands; the existing authoring test uses a temporary directory for the same positive and broken-link cases. `docs/dev/PLAN.md` no longer lists the deleted design example. No delivered skill file was changed.

The README commands produced `- First` and `missing: absent.md`, then removed the temporary note. `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` passed 55 tests. The creator and both plugin examples passed their validators. Active README, package, SPEC, PLAN and tests have no reference to the two deleted paths; staged/unstaged whitespace checks passed. This is a source and local execution check, not client behavior evidence.

## A-002 — Remove root policies and entry sections

Deleted `SKILL_DISCOVERY_PROTOCOL.md` and `WINDOWS_SHELL_POLICY.md`. Removed precisely `## Initialization` and `## Windows shell` and their contents from root `AGENTS.md`; the development entry beginning with `## Start here` remains. Active README, AGENTS, package, SPEC, PLAN, tests and examples have no references to the deleted policies. Closed campaign records retain their historical mentions.

`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` passed 55 tests. The requested paths and headings are absent, the remaining agent entry is intact, and staged/unstaged whitespace checks passed. The removed policies are no longer active repository instructions.
