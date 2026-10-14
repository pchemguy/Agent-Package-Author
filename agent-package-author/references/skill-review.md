# Skill entry and reference content review

Use this module for a full/comprehensive skill review, or for a selected entry or reference question in a focused review. During authorized creation or revision, apply only the relevant criteria as a content check before reporting a result. The creator's [entry](../SKILL.md) selects the operation and scope; [authoring workflow](authoring-workflow.md) owns writes. Review-only requests return findings and stop without package edits.

Review instruction quality in `SKILL.md` and `references/*.md`. Apply [skill format guidance](skill-standard.md) and [validation policy](validation-policy.md) for conformance checks and evidence levels. A content shortcoming is not automatically a format violation. In a plugin, coordinate package-level questions with [plugin review](plugin-review.md); the local entry/reference criteria still apply to each included skill at the requested depth.

## Shared criteria

- **Purpose and scope:** Does the artifact serve one coherent capability or local responsibility, with assumptions and exclusions that agree with it?
- **Document structure:** Does the sequence fit a procedure, explanation, contract or example? Do headings support navigation without fragmenting short material?
- **Paragraphs and steps:** Does each unit have one controlling concern? Are prerequisites and exceptions near the action they govern, without overload or topic drift?
- **Language and precision:** Are conditions, actors, terms, technical distinctions, uncertainty and outputs stated clearly? Does repetition have a reason?
- **Ownership and discovery:** Is shared guidance owned in one place? Can an agent find the needed module before acting without loading unrelated branches or traversing hidden chains?
- **Authority and continuity:** Do assessment and execution remain distinct? Can sufficient established context be reused and missing consequential decisions be handled without guessed permission?
- **Completion and evidence:** Does the selected path define its output and stop, distinguishing planned, performed, verified and externally observed states where applicable?

Length alone is not a defect or an acceptance ceiling. Judge the information needed by the intended models, including local or less capable ones. State byte/word counts as measurements; token, cost or behavior improvement claims need their own method and evidence. For repeated guidance, identify the canonical owner and the decision protected by each copy. Keep a short prerequisite or handoff reminder when the currently loaded instructions need it; consolidate a second full procedure.

## Skill entry

Assess the actual `SKILL.md` against its metadata, supported capability and neighboring entries. The information needed to select a module or respect an immediate constraint must be available before that selection or action.

- Do the description and body agree on purpose, activation, outputs and scope exclusions?
- Are inputs, initial state and a route for missing information clear?
- Can the agent choose the relevant variant and next module from the entry alone?
- Are allowed effects, applicable acceptance gates, required facilities and requested stopping points visible before dependent work?
- Does the entry avoid making essential instructions depend on an unavailable custom or plugin-level entry?

### Reference routing

When `references/*.md` exists, APA's **authoring policy** calls for an identified routing section in `SKILL.md`, preferably a compact table. It names and links every reference individually, states its purpose and scope boundary, and gives a request/state/variant condition for loading it; identify unconditional use explicitly. A grouped row may share a condition but must identify each file. This is a content-review criterion, not an Agent Skills format rule or a Python validator error. A skill with no references needs no such section.

Compare the actual reference inventory with the entry. Check both coverage and whether the entry supplies enough information to select each reference without opening it first. A bare filename list, vague topic labels or “inspect references to find out” instructions do not supply that decision. For a consumer routing trial, expose only `SKILL.md` and ordinary request facts before observing selection; do not leak the reviewer's expected answer or reference contents. Link validity, entry-only routing and successful execution are separate properties.

## Reference modules

Assess each selected reference according to its role. A procedural reference needs operational boundaries and a return path; a terminology guide needs clear definitions, and an example needs its illustrative status and intended use. Do not impose a procedure or skill-wide activation duties on every reference.

- **Local purpose and cohesion:** Does the module cover a coherent subject? Is a split justified by independent use/loading conditions rather than length alone?
- **Scope and ownership:** Does it agree with its caller and neighboring owners? Does a local clause improperly introduce a skill-wide obligation or duplicate a separate procedure?
- **Required context:** Can it be used with the stated prior instructions and inputs? Are consequential prerequisites available before use without requiring every module to be self-contained?
- **Loading and onward route:** Are dependencies and subsequent handoffs discoverable before dependent actions, without unrelated loading or deep chains?
- **Result and return:** For a procedure, are output, stop and next owner clear? For guidance/contract/example material, is it sufficient for its intended decision and distinguishable from operative instructions?
- **Shared content:** Does a reminder protect a boundary, or does it repeat material whose versions can diverge?

Inspect a caller and adjacent owner when a reference changes routing, shared state or handoff. That local interface check does not expand a focused review into an audit of every reference.

## Review procedure

1. Pin the request, source, selected artifact(s), required prior context, permitted effects and evidence limits. For a comprehensive review, inventory the entry, references and support material needed for their claims; record each item's assessed depth, exclusion or unassessed state. A focused review retains its narrower target.
2. Reverse-outline sections and significant paragraphs/steps. Evaluate structure and controlling concerns before local wording changes.
3. Trace entry-to-reference decisions, repeated clauses and consequential handoffs on both sides. If a shortening or move is proposed, verify the destination preserves conditions, qualifiers and reading context.
4. Select representative positive, variant, negative and recovery contrasts appropriate to the actual workflow. A case supplements content coverage; it does not replace inspection of the requested material.
5. Check metadata, direct links and package containment with the owning structural tooling; inspect supporting scripts/assets only when a claim depends on them. If a consumer trial is selected, record source/model, initial context, loaded instructions, actual decisions/actions/output and stop separately from source inspection.
6. Report located findings, consequence, confidence, bounded correction owner and objective recheck. Retain no-finding coverage, unknowns, unrun checks and the requested stop. An accepted repair follows the separate authorized authoring/revision path.

## Useful contrasts

| Contrast | Inspect or observe |
| --- | --- |
| Intended use versus nearby out-of-scope use | Capability boundary without invented output or dependency. |
| Different supported variants | Clear selection condition, relevant module and no unnecessary loading. |
| Reference selected versus nearby request outside its scope | Entry-only route before reference contents are exposed. |
| Required context supplied versus missing/stale | Reuse or scoped recovery without guessed decisions. |
| Assessment-only versus authorized changes | Correct effects, evidence and stop. |
| Successful path versus unavailable prerequisite or interrupted work | Specific blocker/recovery and preservation of valid work. |
| Partial result versus complete operation | Requested output and return boundary without unrequested continuation. |

For evidence and reporting, apply [validation policy](validation-policy.md): source review, structural checks and observed behavior support different claims. Do not report a client activation or behavioral result from links and prose alone.
