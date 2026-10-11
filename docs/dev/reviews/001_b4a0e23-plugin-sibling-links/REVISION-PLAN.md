# Revision plan: bundled skill references

## Campaign and decision

- Campaign: `001_b4a0e23-plugin-sibling-links`.
- Starting source: `b4a0e2328dbd736f5eb808059cc110e01ed63f76` on `main`.
- Working branch: `revision/001_b4a0e23-plugin-sibling-links`; intended integration target: `main`.
- State: **planned**. This opening records the accepted behavioral direction and does not claim that the validator has been changed.
- Input: the user's diagnostic and requested rule. No separate review was commissioned or performed. The reported count of 35 `resource-escape` findings belongs to that external diagnostic; this checkout does not contain the SDD Manager plugin used to produce it.

The creator currently calls `validate_skill(child)` from `validate_plugin.py`. `validate_skill` resolves Markdown links against the child skill directory and emits `ERROR resource-escape` whenever the result lies outside it. That rejects a sibling skill's `SKILL.md` or reference file even when the resolved file remains inside the plugin. The Agent Skills specification recommends relative file references from a skill root but does not define a cross-skill dependency or handoff protocol. Agent Plugins 1.0.0 requires package-supplied paths accessed by a client to resolve within the plugin root. See [Agent Skills](https://agentskills.io/specification) and [Agent Plugins](https://agent-plugins.org/specification), sections 4.1 and 7.1.

## Resulting contract

| Context and resolved target | Creator diagnostic |
| --- | --- |
| Standalone skill, target inside its skill directory | Valid, subject to existence and file checks. |
| Standalone skill, target outside its skill directory | Error under the creator's standalone validation policy. Do not call that policy a universal format prohibition. |
| Plugin child, target inside that child | Valid, subject to existence and file checks. |
| Plugin child, target outside that child but inside the resolved plugin root | Valid package path; at most a **warning** about the shared or sibling dependency and client-specific handoff behavior. Never `resource-escape` error solely for crossing the child boundary. |
| Plugin child, missing target or target resolving outside the plugin root | Error with a distinct actionable reason. Symlinks and traversal are checked after filesystem resolution. |
| Absolute path | Error; a package reference must be relative for this workflow. |

Named handoffs in skill prose may link to the destination `SKILL.md`. Direct links to a sibling's reference file load shared guidance; neither form guarantees that a client activates the sibling skill. This package should document that its sibling links assume the bundled skills are distributed together. The generator and inspector must use the same context-sensitive validation result as the plugin validator.

## Authoritative project updates

| Owner | Planned amendment | Before action |
| --- | --- | --- |
| `SPEC.md` and `PLAN.md` | State plugin-root containment and the warning/error distinction; retain standalone policy and the exact CLI/API contract. | Validator change. |
| `agent-package-author/references/skill-standard.md`, `plugin-standard.md`, `plugin-design.md`, `validation-policy.md`, and `SKILL.md` as needed | Explain ordinary relative links, their boundary and limitation, and distinguish a direct reference from a named handoff. | Authoring acceptance. |
| `README.md` | Show a bundled sibling entry link and a direct shared-reference link; describe the warning and limits without claiming automatic invocation. | Campaign closure. |

## Ordered actions

| Action | Intended change | Acceptance and regression checks |
| --- | --- | --- |
| V-001 | Add plugin fixtures for sibling `SKILL.md`, sibling reference, same-skill reference, missing sibling file, plugin-root escape, symlink escape, and standalone `../` behavior. Capture the failing baseline first. | Plugin-contained links produce no errors and optional warnings; missing/escaping links remain errors; direct standalone validation stays strict. |
| V-002 | Pass an explicit plugin-root context from `validate_plugin` into `validate_skill`; resolve all links on the filesystem before classifying them. Preserve standalone CLI defaults. Reconcile the presentation generator's validation call if a bundled child is generated separately. | `validate_plugin` and `inspect_package` return success for warning-only plugins; stable diagnostic order and actionable paths; failure status for any error. |
| V-003 | Align governing documents, focused authoring references, and README examples with the accepted boundary and host-dependent handoff. | No statement treats sibling-relative links as a standardized dependency mechanism, a guaranteed activation, or a path outside the plugin. |
| V-004 | Run focused and full tests, CLI checks on a representative plugin fixture, and link/diff checks. Review the full changed-path inventory before integration. | Expected warnings/errors and exit codes observed; unchanged examples validate; source and documents agree. |

Each executed action records actual changes and evidence in `REVISION-REPORT.md` when execution is requested. The campaign then uses one verified action checkpoint per commit, an explicit integration into `main`, and merged-state verification. The campaign opening is replayed from the earlier local plan commit `6339638`; record actual publication separately. Do not claim implementation or integration from this plan.

## Stopping point

This request opens and plans the revision. Implementation, verification of the revised behavior, and integration remain pending a separate execution instruction. The baseline check on the cloned source is `python -m unittest discover -s tests -q`: 35 tests passed; those tests do not yet cover sibling links.
