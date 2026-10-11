# Validation and reporting

Validate the format, then test actual behavior. Run the matching offline structural validator and inventory command; review names, boundaries, contained resource paths, referenced files, metadata, and case-specific outputs. Run representative positive and negative workflows and branch variants when present. For generated artifacts that admit mechanical checks, prefer independent validation of their producer.

For a plugin with sibling links, validate the plugin root so child links are checked against the resolved package boundary. Existing sibling files produce at most a warning; missing files, absolute paths and resolved escapes are errors. The standalone skill CLI uses its own stricter skill-directory boundary. Review each named handoff separately in the target client; link validity alone does not show that the client activates the sibling workflow.

For OpenAI presentation, separately check the generated `agents/openai.yaml` values against the accepted skill context, `$name` in its default prompt, both local icon paths, and the parseable self-contained `assets/icon.svg`. Check every immediate-child skill independently in a plugin. Portable structural validation does not verify OpenAI display behavior.

The validators use strict creator rules: a package advertised as completely conforming cannot contain an invalid included component. Explain client failure boundaries separately: unknown manifest keys are reported and ignored by clients, invalid skills are skipped, and an invalid MCP server can be skipped while other components load.

Document the difference between verified structural properties, tested runtime behavior, and untested client-specific execution. A package inspector never runs code or makes a network request. Do not claim portability based only on file presence.
