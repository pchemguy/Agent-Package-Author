# Output contract

## Required files

The output directory must contain:

- `WELCOME.md`;
- `welcome.json`.

## `WELCOME.md`

The document must:

- start with `# Hello, <project>!`;
- contain a `## What it does` section;
- reproduce the normalized project description in that section;
- end with the audience-specific required section.

## `welcome.json`

The JSON document must be an object containing exactly these required fields:

- `schema_version`;
- `project`;
- `audience`;
- `sections`;
- `generated_by`.

Requirements:

- `schema_version` must equal integer `1`;
- `project` must be the normalized project name;
- `audience` must be `contributor` or `user`;
- `sections` must be an ordered JSON array of the level-two Markdown section names present in `WELCOME.md`;
- `generated_by` must equal `hello-world`.

The final item in `sections` must be the final level-two section in `WELCOME.md`.
