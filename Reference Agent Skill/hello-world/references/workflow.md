# Workflow

Generate a welcome pack from normalized project input.

1. Require `project`, `description`, and `audience`.
2. Accept only `contributor` or `user` for `audience`.
3. Preserve project and description text after trimming surrounding whitespace.
4. Load the shared Markdown template from `assets/welcome-template.md`.
5. Add the audience-specific final section defined by the selected profile.
6. Write exactly two artifacts: `WELCOME.md` and `welcome.json`.
7. Keep output deterministic: do not add timestamps, random values, environment-specific paths, or unordered data.
8. Validate the generated directory before reporting success.
