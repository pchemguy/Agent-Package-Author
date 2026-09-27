# Shared authoring workflow

1. Gather capability, audience, activation phrases, inputs, outputs, runtime and environment requirements, representative success and failure cases. Reuse supplied requirements.
2. Choose standalone skill or plugin. For a plugin, split only workflows with independently meaningful activation and outputs; decide whether MCP is genuinely needed.
3. Before writing into an existing target or installing anything, check proposed skill and plugin names against that destination's discovery scope. Treat a collision as a decision to rename, revise the identified owned package, or obtain an explicit overwrite instruction; never overwrite an unrelated item.
4. Classify proposed files according to `portability-policy.md`. Keep client extensions isolated and documented.
5. Establish an observable acceptance contract, design the minimum files, and, for substantial projects, write an explicit spec and ordered plan. An example skill is not a mandatory scaffold.
6. Implement, validate structure, run representative successful and failing workflows, inspect results, repair, and validate again. For revisions, preserve unrelated files.
7. Report output location, actual verification, runtime dependencies, portability limits and whether installation was separately performed.
