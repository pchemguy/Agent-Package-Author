# Revision campaign 010 plan

## Identity and authority

- Campaign: `010_831536e-revision-intake`.
- Starting baseline and branch-off commit: `831536ef6f0e93b733db6a686ffcf011bdef8577`.
- Creation parent and eventual return target: `main` at that baseline.
- Working branch: `revision/010_831536e-revision-intake`.
- User instructions: open a new revision campaign, replace the `agent-package-author/SKILL.md` description, and add the supplied metadata on 2026-11-05.
- State: active, with two directly accepted focused amendments. No prior review or finding is invented.

## Accepted action

| Action | Owner and effect | Recheck |
| --- | --- | --- |
| A-001 | Replace only the `description` frontmatter value in `agent-package-author/SKILL.md` with the user's exact text, removing `1.0` from that description. Leave format references and other package claims in their owning files. | Compare exact frontmatter text; validate the delivered skill; run the repository test suite and inspect the scoped diff. |
| A-002 | Add `display-name`, `aliases`, `author`, and `repository` under the skill's frontmatter `metadata`. Represent `aliases` as a quoted JSON array string containing `APA` and `apa`, since portable Agent Skills metadata values are strings. Do not imply that clients use this custom key for invocation. | Parse the frontmatter and compare all four values; validate/inspect the delivered skill; run the repository test suite and inspect the scoped diff. |

The supplied description and metadata values are the authority for these changes. Its reference to Agent Plugins packages is broad while this project's detailed format guidance remains version-specific. The requested YAML sequence for aliases cannot appear as a portable metadata value; the quoted JSON string retains the ordered alias pair without changing the validator or claiming a standardized alias mechanism. No governing SPEC/PLAN amendment is needed for these frontmatter updates. Preserve campaigns 001–009 unchanged.

## Persistence and return

Retain the branch and this directory while the campaign is open. A-001 and its evidence are published; publish this plan extension before A-002, then commit and publish the verified action with its revision report. These numbered requests may be followed by further scope; do not close or merge the campaign merely because A-002 finishes. At a later explicit closure boundary, verify the complete campaign tip and explicitly integrate it into `main`.

## Reopened amendment — 2026-11-05

The user explicitly reopened this last closed campaign for two focused reference edits and authorized closure again. The qualifying latest first-parent merge on `main` is `f9af864bfc2287b0ed4624e584d5640d45a790e3`, with parents `831536ef6f0e93b733db6a686ffcf011bdef8577` and `df0cccefc3433599ce9a360d35e8b420baae0e2e`. The original opening commit is `809c7d43bc9bc7d8e89adb5874431964adf2d343`; the original baseline remains unchanged. The current reopening/source and return checkpoint is that `main` merge. The campaign branch incorporates it before further edits.

| Action | Owner and effect | Recheck |
| --- | --- | --- |
| A-003 | Remove the blank line between step 6's introductory sentence and its indented stage list in `references/authoring-workflow.md`; retain the blank line after the heading. | Inspect the exact diff and Markdown list structure; validate the delivered skill. |
| A-004 | Mark `userinfo` as an inline technical token in `references/mcp-packaging.md`. | Inspect the exact sentence and Markdown; validate the delivered skill. |

Each action updates the active revision report and is committed, published and read back before the next. Then run coupled regression checks, publish the amended campaign tip, explicitly merge it into the refreshed `main` return target, verify the merged state, publish/read back, and close again. Earlier actions and closure evidence remain historical, and other closed campaign records stay frozen.
