# Validation and reporting

Keep four forms of evidence distinct:

| Evidence | Supports | Does not establish |
| --- | --- | --- |
| Source content review | Located instruction, composition and handoff findings at stated depth | Actual execution or client selection. |
| Structural validator and inventory | Checked metadata, manifest, paths, containment and included components | Prose quality, runtime behavior or client rendering. |
| Representative workflow trial | Observed decisions, outputs, failures and recovery for the stated context | Coverage of all requested source content or all clients. |
| Target-client trial | Observed discovery, activation and effects in that client/version/context | Universal client compatibility. |

For comprehensive content review, inventory requested entries, references and supporting material relevant to their claims. Record assessed depth, exclusions and unassessed parts. A representative trial adds evidence but cannot replace requested content inspection. For focused review, inspect the selected content and necessary interfaces without silently expanding the request. Use [skill review](skill-review.md) for entry/reference criteria and [plugin review](plugin-review.md) for package composition. Report located findings with consequence, confidence, correction owner and objective recheck; preserve no-finding coverage, uncertainty, unrun checks and requested stopping point. Review-only findings do not authorize changes. If a consumer trial is run, record source/model, initial context, loaded instructions, actual actions/output and stop; do not feed the trial the expected review conclusion.

Run the matching offline structural validator and inventory command when the request calls for structural evidence; review names, boundaries, contained resource paths, referenced files, metadata, and case-specific outputs. Run representative positive and negative workflows and branch variants when a behavioral claim is needed. For generated artifacts that admit mechanical checks, prefer independent validation of their producer.

For a plugin with sibling links, validate the plugin root so child links are checked against the resolved package boundary. Existing sibling files produce at most a warning; missing files, absolute paths and resolved escapes are errors. The standalone skill CLI uses its own stricter skill-directory boundary. Review each named handoff separately in the target client; link validity alone does not show that the client activates the sibling workflow.

For OpenAI presentation, separately check the generated `agents/openai.yaml` values against the accepted skill context, `$name` in its default prompt, both local icon paths, and the parseable self-contained `assets/icon.svg`. Check every immediate-child skill independently in a plugin. Portable structural validation does not verify OpenAI display behavior.

The validators use strict creator rules: a package advertised as completely conforming cannot contain an invalid included component. Explain client failure boundaries separately: unknown manifest keys are reported and ignored by clients, invalid skills are skipped, and an invalid MCP server can be skipped while other components load.

Document the difference between verified structural properties, tested runtime behavior, and untested client-specific execution. A package inspector never runs code or makes a network request. Do not claim portability based only on file presence.
