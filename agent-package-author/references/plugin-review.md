# Plugin composition and coordination review

Use this module for a full/comprehensive plugin content review or a selected plugin-level question in a focused review. The creator's [entry](../SKILL.md) selects review-only or authorized authoring/revision before this module is loaded. Apply [plugin format guidance](plugin-standard.md), [plugin design](plugin-design.md) and [validation policy](validation-policy.md) for their respective owners; this module assesses how the package's advertised capabilities work together.

Inventory actual `plugin.json`, supported component paths, included skills and references, optional MCP configuration, extensions and any custom shared entry/coordinator that affects a claim. A plugin with no skills gets no invented skill-entry obligation. For included skills, use [skill review](skill-review.md) at the depth the requested scope requires. Structural conformance, content assessment and observed behavior remain distinct.

## Composition and ownership

- **Capability boundaries**
    - Do advertised skills and other components have distinct responsibilities, useful outputs and clear entry/use conditions?
    - Are overlaps resolved without making a user know internal component names?
- **Workflow decomposition**
    - Do composite paths connect focused capabilities through meaningful handoffs?
    - Are closely related branches retained together when another independent skill has no useful activation boundary?
- **Shared ownership**
    - Do common conventions, prerequisites and reporting rules have identifiable owners?
    - Are short summaries consistent with those owners rather than competing full procedures?
- **Coupling and loading**
    - Can a selected path use only relevant skills, references and other components?
    - Are dependencies explicit, available and bounded by the package/client interface?
- **Package and client boundary**
    - Are advertised capabilities supplied and referenced paths contained within the plugin root?
    - Are client extensions and unverified invocation behavior distinguished from portable skill/MCP structure?
- **Human and agent documentation**
    - Do user-facing examples explain supported behavior while agent instructions supply selection, authority and stops?
    - Are source-only development instructions kept out of runtime dependencies?
- **Instruction composition**
    - Do sections distinguish responsibility, shared gates, procedure and conditional routing?
    - Does each paragraph/step have one controlling concern, with conditions and exceptions near the action?

Concision is judged by sufficient explicit guidance for the intended models, not a word quota. For repeated guidance, identify the canonical owner and the decision a local summary protects. A shared entry or coordinator may make a consequential obligation visible before a handoff; a second complete procedure can drift.

## Optional shared `PLUGIN.md` entry

Apply this section **only when the package includes** a `PLUGIN.md` intended as shared workflow guidance. Agent Plugins 1.0.0 does not discover it as a portable component. Establish how the target agent would load it; do not infer automatic discovery or require one for every integrated plugin. See [plugin design](plugin-design.md) for when authoring such an optional entry is justified.

- Does it identify the capability system, relevant common prerequisites, optional coordinator and clear condition for loading the next owner?
- Can ordinary requests route to a supported capability without opening every skill or requiring the user to know internals?
- Do composite summaries state purpose, principal owners, outputs, consequential handoffs and stops without repeating every execution procedure?
- Are shared authority, acceptance, persistence or other domain obligations visible before governed actions, with detailed gates linked to their owners?
- Do summaries agree with the operational owners? Is **each substantial rule also defined in the canonical coordinator, skill or component owner**, and are those instructions sufficient when `PLUGIN.md` is unavailable?
- Can an established owner keep a contextual follow-up without reloading the optional shared entry? Does unclear context route to bounded recovery?

`PLUGIN.md` may project the coordinator's canonical orchestration guidance; it must not be its only source. Entry routing, context reuse and missing-context recovery answer different questions. A capability directory is not a replacement for a workflow summary, and neither should become a second procedure catalog.

## Optional coordinator

Apply this section when the plugin includes a coordinator capability. Inspect its relevant entry/modules and its actual handoffs; do not presume its name, branch model, backend or an approval sequence.

- **Selection and continuity:** Does it establish or reuse sufficient evidence before choosing a path and announcing a consequential change? Can it retain an applicable workflow without duplicate orientation?
- **Shared readiness:** Are prerequisites and human decisions established for the next owner, with authority, readiness and completed state distinguished?
- **Delegation:** Are focused owners, handoff inputs/effects/expected results clear without the coordinator reimplementing their procedures?
- **Handoff boundaries:** Do scope, unresolved acceptance and requested stops survive transitions and recovery? Can a child finish without automatically resuming an unfinished parent?
- **Results and blockers:** Does it collect actual evidence, reconcile failures and return at the correct boundary without claiming unavailable capabilities or unobserved effects?
- **Entry/module structure:** Are coordination decisions and consequential obligations visible in its own entry before dependent work, with conditional detail accessible from that entry? Does moving detail preserve pre-action guidance?

The coordinator may own canonical orchestration instructions. Do **not** impose the shared `PLUGIN.md` projection-only rule on that owner. Check both sides of a consequential handoff: who selects, establishes readiness, executes, verifies and returns control. Its ordinary context reuse and recovery must work without reloading `PLUGIN.md`.

## Review procedure

1. Pin the requested package, capabilities, source and permitted effects. For a comprehensive review, inventory the requested entries, skills/references and other advertised components; record assessed depth/evidence, exclusions and unassessed parts. A focused review retains its selected interfaces. Inspect supporting configuration/resources only where a capability claim needs them.
2. Map responsibilities across optional shared entry, coordinator, focused skills, shared guidance, MCP and extensions. Trace ordinary request routing and selected composites without inferring missing components from a favored template.
3. Reverse-outline consequential sections and assess composition, loading conditions, duplicated procedure and ownership against the criteria above. Keep necessary prominence while consolidating competing detail.
4. Trace prerequisites, retained context, authorization, human decisions, result evidence and stops on both sides of affected handoffs, including contextual follow-ups and recovery.
5. Check actual links, containment, package inclusion and source agreement with the owning tooling. Apply MCP/configuration and client-specific interfaces where relevant; report uninspected behavior. For a selected consumer trial, give ordinary initial task context rather than reviewer expectations and record observed routing separately.
6. Report located findings, consequence, confidence, bounded correction owners and objective rechecks. Preserve no-finding coverage, unresolved choices and unrun checks. Accepted revisions recheck affected entry/owner/projection under the project's actual persistence policy.

## Selected contrasts

| Contrast | Inspect or observe |
| --- | --- |
| Independent request versus composite request | Direct focused owner or justified coordination, without activating the entire plugin by default. |
| Shared `PLUGIN.md` available versus unavailable | Supported loading/fallback and sufficient operational owners. |
| Fresh entry versus established owner/context | Needed discovery versus reuse without repeated ceremony. |
| Recoverable context versus missing consequential decision | Evidence-based recovery or targeted clarification, not guessed authority. |
| Assessment request versus authorized changes | Correct effects and return boundary. |
| Prerequisite satisfied versus unresolved | Dependent work proceeds or stays blocked; handoff preserves the gate. |
| Child operation complete versus unfinished parent | Correct return and retained parent scope. |
| Coordinator direct entry versus shared entry | Canonical duties reachable without `PLUGIN.md`. |
| Valid delegation versus blocked delegation | Actual result/blocker and preserved scope, without claiming unperformed work. |

Use only contrasts applicable to the actual package. For a behavioral trial, [validation policy](validation-policy.md) separates source/model/context and observed output from reviewer expectation. Passing structural checks never establishes host discovery, cross-skill invocation or runtime compatibility.
