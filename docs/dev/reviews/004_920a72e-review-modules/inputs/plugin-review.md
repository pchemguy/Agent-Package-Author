# Review plugin composition and coordination

## Shared plugin entries and coordination

Skills and plugins support modular organization of agent capabilities. Within a skill, complex functionality can be divided into capability modules in `references/*.md`. `SKILL.md` orients the agent and provides enough routing information to select the relevant modules without loading every reference.

Plugins group skills into a further level of composition. This modular architecture serves two purposes:

- **Development:** clear responsibilities, maintainable units and limited coupling.
- **Context management:** progressive loading that avoids unnecessary instructions and context pollution.

The [Agent Plugins specification v1.0.0](https://agent-plugins.org/specification) does not define `PLUGIN.md`, a plugin entry analogous to `SKILL.md`. Such an entry may be unnecessary when a plugin merely bundles unrelated skills for distribution, each used through its own entry. An integrated plugin composes relatively independent capabilities as skills and keeps closely related sub-workflows within their references, with shared capabilities reused across workflows. In that case, a shared `PLUGIN.md` entry is desirable: it orients the agent across the system and routes workflows involving several skills, much as `SKILL.md` orients the agent within a skill and routes it to reference modules.

A complex plugin may also define a coordinator skill to manage composite workflows. The loading path becomes `PLUGIN.md` → coordinator `SKILL.md` → selected skill entries and references. Other skills can depend primarily on the coordinator and a small set of shared capabilities, reducing connections between individual skills.

Because `PLUGIN.md` is non-standard, automatic loading cannot be assumed; agents may need explicit instructions to read it. The plugin's skill workflows should remain fully functional through their skill entries when `PLUGIN.md` is not loaded. When a coordinator is present, `PLUGIN.md` should serve as a convenience front for its `SKILL.md`, summarizing capabilities, routing and essential obligations already defined by the coordinator and focused skills.

## Scope and output

Review plugin-level capability boundaries, shared entry guidance, composite workflows, coordination and ownership. Assess the current supported package and report actionable findings. Inspect individual skills and references where a plugin claim or handoff depends on them; keep the review bounded by the requested scope.

Assess the accepted plugin design and its actual responsibilities using the distinction above. A review does not introduce new components or authorize additional effects by implication.

Apply skill-entry criteria to skill workflows. Apply shared-entry and coordinator criteria only when those components are present. Assess other advertised components, such as MCP servers, through their supported discovery paths, interfaces, dependencies and owners. A package without skills does not acquire a skill-entry requirement.

Format conformance, content review and observed behavior provide different evidence. Use the owning format/structural tooling for metadata and package validity; this procedure assesses how capabilities form a usable system. Source review does not establish installation, host discovery or runtime invocation.

## Plugin composition and ownership

- **Capability boundaries**
    - Do advertised skills and other components have distinct responsibilities, useful outputs and clear entry and use conditions?
    - Are overlaps resolved without requiring the user to know internal names?
- **Workflow decomposition**
    - Do composite paths connect focused capabilities through meaningful handoffs?
    - Are closely related internal branches kept together where independent capability boundaries add no value?
- **Shared ownership**
    - Do common conventions, prerequisites and reporting rules have identifiable owners?
    - Are summaries consistent with them, with justified short reminders rather than competing procedure copies?
- **Coupling and loading**
    - Can the selected path use only the relevant skills/modules and other components?
    - Are dependencies explicit and available, without requiring the entire plugin context for every request?
- **Package and client boundary**
    - Are advertised capabilities actually supplied and referenced files within the applicable package boundary?
    - Are client extensions and unverified invocation behavior distinguished from portable structure?
- **Human and agent documentation**
    - Do user-facing examples explain supported behavior while agent guidance supplies selection and execution boundaries?
    - Are source-only development instructions kept out of runtime dependencies?
- **Instruction composition**
    - Do sections visibly distinguish responsibilities, shared gates, the principal procedure and conditional routing where applicable?
    - Does each paragraph or step have one controlling concern, with prerequisites and exceptions grouped with their action?

For repeated guidance, identify its canonical owner and the decision protected by each summary. A shared entry or coordinator can highlight a consequential rule at a handoff; a full second procedure increases maintenance risk. Judge concision by sufficient explicit guidance for the intended models, not a byte/word quota or speculative token savings.

## Integrated plugin entry review

Apply this section when the plugin uses `PLUGIN.md` as its shared workflow entry. Assess its stated purpose, loading path and fallback. Essential operations must remain reachable through their supported entries or interfaces and operational owners when `PLUGIN.md` is unavailable.

- **Orientation and coordinator pointer**
    - Does the entry identify the plugin's capability system, relevant common prerequisites and any coordinator, with a clear condition for loading it?
    - Is `PLUGIN.md`'s loading path explicit, without assuming automatic discovery of this non-standard entry?
- **Request-to-capability routing**
    - Can an agent resolve ordinary requests to a supported owner or path from entry guidance, without opening all skill procedures or asking the user to name internals?
- **Composite summaries**
    - Are purpose/trigger, principal owners, outputs, consequential handoffs and stops clear, without repeating every execution procedure?
- **Prominent obligations**
    - Are shared authority, acceptance, persistence or other domain constraints visible before the actions they govern?
    - Are detailed gates linked to their owners?
- **Projection and source fidelity**
    - Do summaries agree with operational owners?
    - Is each substantial operational rule defined in its canonical coordinator, skill or component owner?
    - Are those operational instructions sufficient for supported workflows when `PLUGIN.md` is unavailable?
- **Established context**
    - Can follow-ups remain with an already active owner?
    - Does unclear interpretation route to appropriate recovery rather than restart discovery or guess missing decisions?

Keep workflow entry, established-context use and missing-context recovery distinct. A plugin entry can establish the owner needed for subsequent requests without interpreting every later task itself. A capability directory and a workflow summary serve different selection questions; neither should silently become a second full procedure catalog.

## Coordinator review

Apply this section when the plugin includes coordination. Assess the coordinator as part of the plugin's architecture and inspect its relevant entry/modules; do not presume a particular name, branch model, backend or mandatory approval sequence.

- **Selection and continuity**
    - Does it establish or reuse sufficient evidence before selecting a path and communicating the decision and its basis at consequential boundaries?
    - Can it reuse an applicable workflow or recognize a material change without duplicate orientation or routine restart?
- **Shared readiness**
    - Does it establish the prerequisites and human decisions needed by the next owner, keeping authority, readiness and performed state distinct?
- **Delegation**
    - Are responsible skills and handoff inputs/effects/expected results clear?
    - Does the coordinator preserve focused ownership instead of reimplementing each skill?
- **Boundaries across handoffs**
    - Do scope, unresolved acceptance, requested stops and actual authorization survive transitions and recovery?
    - Can a child operation finish without automatically resuming its parent?
- **Results and blockers**
    - Does it collect actual evidence, reconcile blockers and return the correct completion boundary?
    - Are unavailable capabilities and uncertain external effects reported rather than assumed complete?
- **Entry/module structure**
    - Are coordination decisions and consequential obligations visible in the coordinator entry before dependent work, with conditional detail under accessible owners?
    - Does moving procedure out of the entry preserve required pre-action guidance?

The shared plugin entry may project coordinator behavior; the coordinator may own canonical orchestration instructions. Do not impose the projection-only rule on that canonical owner. Inspect both sides of a consequential handoff and identify which layer selects, establishes readiness, executes, verifies and returns control. Ordinary context reuse and recovery must not depend on `PLUGIN.md` being loaded again.

## Review procedure

For a full/comprehensive plugin review, inventory the requested package's entries, included skills, their references and other advertised components. Record each item's review depth and evidence, reason for exclusion or unassessed status. Inspect supporting configuration and resources when a capability claim depends on them. Representative workflows supplement content coverage; focused reviews retain their selected scope and interfaces.

1. **Establish scope and source.** Pin the inspected package, intended capability model, requested outputs/effects and evidence limits. Identify actual installed/package contents and development exclusions where relevant.
2. **Map responsibilities.** Identify entry, coordinator, focused skills, shared guidance and optional tools/extensions. Trace ordinary request routing and selected composites; do not infer missing components from a preferred template.
3. **Assess composition and duplication.** Inspect visible section responsibilities, paragraph/step cohesion, information order, loading conditions, repeated procedures and ownership against the criteria above. Distinguish necessary prominence from repeated detail.
4. **Trace affected transitions.** Check prerequisites, carried context, authority, human decisions, result evidence and stop on both sides. Include contextual follow-ups and recovery, not only fresh entry.
5. **Verify claims and cases.** Check actual links, containment, package inclusion and source agreement. Use owning configuration and runtime guidance for non-skill components; report uninspected or unavailable behavior. If a behavioral trial is selected, supply only the intended initial context before observing discovery or routing; assess target agreement separately.
6. **Report and hand off.** Give located findings, consequences, confidence, bounded correction owners and objective rechecks. Preserve the coverage record, no-finding results and unresolved choices. Accepted revisions require affected entry/owner/projection rechecks under the project's actual persistence policy.

## Assessment contrasts and evidence

Use contrasts appropriate to the accepted design; do not make every trial compulsory. Keep domain-specific sample prompts and expected behavior in the plugin's own review material rather than importing its policies here.

### Shared contrasts

| Contrast | Inspect or observe |
| --- | --- |
| Independent capability request versus composite workflow request | Direct owner use or appropriate coordination, without unnecessary full-system activation |
| `PLUGIN.md` available versus unavailable | Supported loading/fallback; no claim of automatic host discovery or dependence on an unavailable custom entry |
| Ordinary request versus request outside advertised scope | Clear owner/path or bounded clarification; no invented capability |
| Fresh workflow entry versus established owner/context | Needed discovery versus context reuse; no repeated selection ceremony |
| Recoverable context versus a consequential missing decision | Evidence-based recovery or targeted clarification; no guessed authority, acceptance or range |
| Assessment request versus authorized changes | Correct effects and return boundary |
| Shared prerequisite satisfied versus unresolved | Dependent work proceeds or remains blocked; delegation does not erase the gate |
| Child operation complete versus unfinished parent scope | Correct return and retained parent context; no implicit continuation |
| Narrow preparation result versus external publication | Requested outputs and permitted effects remain distinct |

### Coordinator contrasts

Apply these when a coordinator is present, alongside the relevant shared contrasts.

| Contrast | Inspect or observe |
| --- | --- |
| Entry through `PLUGIN.md` versus direct coordinator entry | Canonical coordination duties remain reachable from the coordinator; loading the plugin front is optional |
| Current workflow still applicable versus request requiring a stage or path switch | Sufficient evidence precedes reuse or switching and its consequential announcement; scope, accepted inputs and requested stops survive |
| Successful delegation versus blocked or failed delegation | Actual result/evidence or a concrete blocker; retained parent scope and correct return/stop, with no claim of unperformed work |
| Coordination module relevant versus unrelated to the selected path | Entry guidance identifies the required module and use conditions before its dependent action; unrelated modules need not be loaded |

### Evidence

For source review, record the actual instruction evidence and coverage. For a selected consumer trial, record source/model, initial context/request, loaded instructions, visible decisions, actual actions/output and reached boundary. Do not supply expected owners or reviewer answers to the consumer. A correct route does not prove downstream behavior, and structural validation does not prove universal client support. Report unrun or unavailable checks explicitly.
