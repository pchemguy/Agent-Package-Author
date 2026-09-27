# Plugin design

Choose a plugin when packaging multiple independently useful skills or a skill with optional MCP configuration. Split skills where activation, workflow, resources, outputs or lifecycle are independently meaningful; keep branches of one capability in a single skill. Distinguish plugin identity from each skill name and avoid overlapping trigger descriptions.

Keep shared material under explicit ownership. A bundled skill must not assume a client discovers another skill's private references. If common data is needed, give each skill a self-contained copy or a documented contained path while preserving its standalone behavior.

Only `skills/*/SKILL.md` immediate children are portable skills. Do not imply that arbitrary `commands/`, hooks, custom agents, or rules are portable v1 components. Explicit client-specific behavior belongs under the client's verified reverse-domain `extensions` namespace and/or matching root directory; this is not portable core. Installation and presentation remain client concerns.
