# Agent Skills format

Use the current [Agent Skills specification](https://agentskills.io/specification) as authority. An Agent Skill is a directory with `SKILL.md`, YAML frontmatter, and Markdown instructions. `name` (1–64 lowercase ASCII letters, numbers or hyphens; no leading/trailing or doubled hyphen) matches its parent directory. `description` (1–1024 characters) describes the action and when it activates.

The standard optional metadata are `license`, `compatibility` (at most 500 characters), and a string-to-string `metadata` mapping. `allowed-tools` is experimental and is not a portable default. The creator's default template uses only the required fields; include standard optional fields only when justified.

`scripts/`, `references/`, and `assets/` are optional. Link resources by relative paths from the skill root and ensure targets exist. Directly name conditional references in `SKILL.md` so they can be found without traversing chains. Ordinary script execution and tool availability depend on the host; state actual interpreter and dependencies. Do not embed host-specific installation locations in the package.
