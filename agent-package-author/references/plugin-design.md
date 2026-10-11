# Plugin design

Choose a plugin when packaging multiple independently useful skills or a skill with optional MCP configuration. Split skills where activation, workflow, resources, outputs or lifecycle are independently meaningful; keep branches of one capability in a single skill. Distinguish plugin identity from each skill name and avoid overlapping trigger descriptions.

Keep shared material under explicit ownership. When skills are distributed together, use ordinary relative Markdown links for intentional sibling references. Link to `../other-skill/SKILL.md` and name **other-skill** in prose when requesting a workflow handoff. Link directly to `../other-skill/references/topic.md` when loading shared guidance without selecting the sibling workflow. Check that each resolved file stays within the plugin root. A skill intended to work in isolation needs its own copy of required guidance; a sibling link makes it dependent on the bundle.

Only `skills/*/SKILL.md` immediate children are portable skills. A named handoff and link identify another capability; they do not guarantee that a client activates it. Do not imply that arbitrary `commands/`, hooks, custom agents, or rules are portable v1 components. Explicit client-specific behavior belongs under the client's verified reverse-domain `extensions` namespace and/or matching root directory; this is not portable core. Installation and presentation remain client concerns.

Read `openai-presentation.md` to generate distinct OpenAI presentation in each immediate-child skill after the portable plugin is designed. Do not put a skill's OpenAI metadata at plugin root or in `plugin.json`.
