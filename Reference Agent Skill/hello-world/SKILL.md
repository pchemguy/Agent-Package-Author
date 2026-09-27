---
name: hello-world
description: Generate and validate a small project welcome pack while demonstrating portable Agent Skills discovery, progressive disclosure, conditional references, assets, scripts, and validation.
---

# Hello World reference skill

Use this skill when the user asks to generate the reference Project Welcome Pack or when demonstrating a portable Agent Skills workflow.

## Input

Require these logical fields:

- project name;
- project description;
- audience: `contributor` or `user`.

If any required field is missing or the audience is unsupported, treat the request as invalid.

## Workflow

1. Read `references/workflow.md` for the detailed generation procedure.
2. Read `references/output-contract.md` for required artifacts and invariants.
3. Select exactly one audience profile:
    - for `contributor`, read `references/contributor-profile.md`;
    - for `user`, read `references/user-profile.md`.
4. Use `assets/welcome-template.md` as the reusable content template.
5. Prepare structured JSON input matching the requested project information.
6. Run `python scripts/render.py --input <input.json> --output <output-dir>`.
7. Run `python scripts/validate.py <output-dir>`.
8. If validation fails, repair the generated artifacts or input as appropriate and validate again.
9. Report success only after validation succeeds.

Do not read the irrelevant audience profile merely to complete the workflow. Do not replace the scripts with host-specific tools when ordinary Python execution is available.

## Completion

A successful run produces `WELCOME.md` and `welcome.json` in the requested output directory and passes `scripts/validate.py` with exit code `0`.
