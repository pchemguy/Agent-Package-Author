# Comprehensive project review plan

Campaign: `002_283617b-comprehensive-review`

Starting baseline: `283617b53fe51f32284ba54df1a6a901e678aa3e` (`main`)

Target: `main`

## Scope

Review the current Agent Package Author source, documentation, examples, and tests against the project contract. Give particular attention to dependencies on the former checkout and to paths affected by the move into `docs/dev/` and removal of `IMPLEMENTATION_LOG.jsonl`. Do not revise closed campaign records or treat their historical links as current instructions.

## Review procedure

1. Inventory tracked files, symlinks, Git remotes, script imports, external-file reads, and local Markdown links. Compare the former checkout only to establish whether the current checkout still needs anything from it.
2. Review the authoring entry point and each reference against `docs/dev/SPEC.md`, README claims, examples, and portability boundaries. Inspect validator and presentation-helper behavior and tests for meaningful gaps and failure paths.
3. Run the declared test suite, self-validation, example validation and inspection, CLI smoke checks, and package-isolation checks. Record observed outcomes, limitations, and findings with stable IDs in `REVIEW-REPORT.md`.
4. Repair confirmed defects within the requested scope, recheck the affected behavior, and record final disposition. Keep broader design choices as explicit follow-up findings rather than silently expanding the contract.

## Exit

The report identifies reviewed baseline and candidate commits, checks and observed results, each finding's evidence and disposition, remaining limitations, and whether the delivered package can operate without the former checkout. Publish the verified campaign branch and integrate it into `main` when its accepted scope is complete.
