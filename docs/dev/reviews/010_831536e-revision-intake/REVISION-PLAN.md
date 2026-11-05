# Revision campaign 010 plan

## Identity and authority

- Campaign: `010_831536e-revision-intake`.
- Starting baseline and branch-off commit: `831536ef6f0e93b733db6a686ffcf011bdef8577`.
- Creation parent and eventual return target: `main` at that baseline.
- Working branch: `revision/010_831536e-revision-intake`.
- User instructions: open a new revision campaign, then replace the `agent-package-author/SKILL.md` description with the exact supplied wording on 2026-11-05.
- State: active, with one directly accepted focused amendment. No prior review or finding is invented.

## Accepted action

| Action | Owner and effect | Recheck |
| --- | --- | --- |
| A-001 | Replace only the `description` frontmatter value in `agent-package-author/SKILL.md` with the user's exact text, removing `1.0` from that description. Leave format references and other package claims in their owning files. | Compare exact frontmatter text; validate the delivered skill; run the repository test suite and inspect the scoped diff. |

The supplied description is the authority for this change. Its reference to Agent Plugins packages is broad while this project's detailed format guidance remains version-specific. No governing SPEC/PLAN amendment or test fixture change is needed for a frontmatter wording update. Preserve campaigns 001–009 unchanged.

## Persistence and return

Retain the branch and this directory while the campaign is open. Commit and publish this accepted plan before A-001, then commit and publish the verified action with its revision report. This numbered request may be followed by further scope; do not close or merge the campaign merely because A-001 finishes. At a later explicit closure boundary, verify the complete campaign tip and explicitly integrate it into `main`.
