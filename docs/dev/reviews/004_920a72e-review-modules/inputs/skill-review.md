# Review skill entries and references

## Scope and output

Review composition, organization, scope, ownership and instruction quality in `SKILL.md` and reference modules (`references/*.md`). Apply the criteria to the selected material and report actionable findings.

Establish the requested output and editing authority first. A review-only request produces findings and proposed revisions; it does not authorize repairs, installation or external operations. A focused review need not become a full-package audit.

Apply Shared review criteria to both artifact types, then the relevant Skill entry review or Reference module review section. The review procedure and evidence requirements are shared.

## Shared review criteria

- **Purpose and scope**
    - Does the artifact serve its stated capability or local responsibility?
    - Do contents, assumptions and boundaries agree with that purpose?
- **Document structure**
    - Do sections have clear purposes and a useful order?
    - Does the organization fit a procedure, explanation, contract or example?
    - Do headings improve navigation without fragmenting short material?
- **Paragraphs and steps**
    - Does each paragraph or step have one controlling concern?
    - Are prerequisites, explanations and exceptions grouped with the action they govern?
    - Are overload, topic drift or unexplained scope changes present?
- **Language and precision**
    - Are conditions, actors, pronouns and terms unambiguous?
    - Does redundant wording obscure the meaning?
    - Are identifiers, evidence, quantities, uncertainty and technical distinctions stated accurately?
- **Duplication and ownership**
    - Does repetition support lookup, sequence or a boundary, or reproduce another owner's procedure?
    - Are shared rules maintained consistently and needed details at a clear destination?
- **Progressive discovery**
    - Can the agent identify what to load next and why?
    - Are necessary modules directly discoverable, available within the applicable package and sufficient when loaded under their stated prerequisites?
- **Authority and continuity**
    - Are assessment and execution distinguished where relevant?
    - Can sufficient existing context be reused?
    - Are missing decisions, interrupted work and request changes handled without guessing authority?
- **Completion and evidence**
    - Do instructions define observable outputs and the requested stop?
    - Are planned, performed, verified, persisted and externally observed states distinguished where applicable?

Length is a diagnostic signal, not a defect or an acceptance ceiling. Assess information needed by the intended models, including less capable or local models. A shorter entry or reference can lose necessary context or decision guidance. Report byte/word measures as such; token, cost or behavioral improvement claims require an identified method and evidence.

For repeated guidance, identify the canonical owner and the reason for each copy. A short prerequisite or boundary is justified when needed by the instructions already loaded or when it prevents a consequential handoff error. Recommend consolidation where repetition adds no condition, decision or protection. Any proposed relocation must preserve meaning, qualifications and discoverability.

## Skill entry review

Check that information required to choose the next module or respect an immediate constraint is available before that choice or action. A correct instruction discovered only after its dependent action is insufficient. Do not require every reference to be loaded at startup or make essential instructions depend on an unavailable custom entry.

- **Purpose and activation:** Do metadata and entry agree on the supported capability, triggers, outputs and scope exclusions?
- **Inputs and starting state:** Are required inputs and readiness conditions clear, with a usable path for missing information?
- **Paths and variants:** Are selection conditions, principal paths and the next instructions clear?
- **Authority and completion:** Are permitted effects, applicable acceptance gates and the stopping point explicit?
- **Dependencies:** Are necessary facilities identified, with appropriate handling of an unavailable tool or owner?

### Reference routing coverage

When a skill includes `references/*.md` references, require a clearly identified routing section in `SKILL.md`, preferably a table. It must name and link every reference file and provide the following selection information for each:

| Routing element | Review requirement |
| --- | --- |
| Reference | Explicit filename/path and a usable relative link; grouped rows must still identify every file individually |
| Purpose, scope and boundary | What the reference covers and the distinction from adjacent references or another workflow |
| Trigger/use conditions | Which requests, states, variants or prerequisites require loading it; identify unconditional use explicitly when applicable |

An agent must be able to determine which references are relevant to a request from `SKILL.md` alone, before reading their contents. A filename list, vague topic labels or instructions to inspect references to discover their applicability do not satisfy this criterion.

Compare the `references/*.md` inventory with the routing section to detect omissions. In source review, identify the scope and conditions actually stated in the entry that justify selecting each reference; check their agreement with reference contents separately. If a consumer trial is selected, assess routing with only `SKILL.md` and ordinary request facts available before exposing reference contents. Do not use the reviewer’s target knowledge as evidence of entry-only consumer selection. Route completeness and selection clarity are separate from link validity and execution success.

## Reference module review

Review a reference’s local responsibility, required context and relationships with other modules. Apply scope, continuity, output and stopping criteria according to its role: an executable sub-workflow needs operational boundaries; a terminology guide needs consistent definitions and useful coverage. Do not impose an execution sequence on explanatory material.

- **Local purpose and cohesion**
    - Does the module cover a coherent procedure or subject?
    - Do sections develop that purpose rather than accumulate unrelated instructions?
    - Is a split justified by independent use or loading conditions, rather than length alone?
- **Scope and ownership**
    - Are the module's decisions, effects or subject boundaries clear?
    - Does it overlap or conflict with neighboring owners, or introduce a skill-wide rule without an appropriate entry/owner route?
- **Required context**
    - Can it be understood with its required prior instructions and inputs?
    - Are consequential assumptions or prerequisites available before use? Identify missing context without requiring every module to be independently self-contained.
- **Loading and onward routing**
    - Does the module agree with its caller’s stated purpose and use conditions?
    - Are its onward dependencies discoverable before use, without unnecessary chains or unrelated loading?
- **Result and return**
    - For a procedure, are its result, stop and return/next owner clear?
    - For guidance, contracts or examples, is the information sufficient for its intended decision or use, with illustrative content distinguished from operative instructions?
- **Shared content**
    - Is reused guidance maintained by a clear owner?
    - Does a local reminder protect a prerequisite or boundary, or copy a substantial procedure whose versions can diverge?

Inspect the relevant caller and neighboring modules when a local change affects loading, shared state, scope or a handoff. Keep the review bounded: tracing that interface does not require auditing every reference or restarting the whole skill.

### Reference assessment contrasts

| Contrast | Inspect or observe |
| --- | --- |
| Required prior instructions and inputs supplied versus missing | The reference supports its stated use, or identifies the missing prerequisite; no reliance on an unseen authoring conversation |
| Clear local scope versus overlap with an adjacent module | Responsibilities and shared ownership remain distinct, including after splitting, merging or relocation |
| Explanatory material organized for its intended use versus forced into an execution sequence | Guidance, contracts and examples remain useful without invented procedural steps, activation or completion duties |

## Review procedure

For a full/comprehensive skill review, inventory `SKILL.md`, its `references/*.md` modules and supporting files needed to assess their instruction claims. Record each item's review depth and evidence, reason for exclusion or unassessed status. A review confined to an entry or reference records that narrower target. Representative cases supplement content coverage; they do not replace it.

1. **Pin the brief and source.** Record the capability, selected files, required prior context, review scope, actual source and permitted effects. Identify applicable instructions, source owners and evidence limits. Respect project rules for retained history and protected material.
2. **Reverse-outline the text.** Identify the job of each section, paragraph and major step. Check the overall trajectory and selected dimensions above before proposing local edits.
3. **Trace consequential instructions.** Apply Reference routing coverage when reviewing an entry with references. Inspect relevant routes and handoffs on both sides; compare repeated or relocated clauses with their owners, use conditions and required prior instructions. Verify destinations preserve removed qualifiers before shortening either the entry or a reference.
4. **Assess representative contrasts.** Select cases that exercise the reviewed entry or module's important branches, boundaries and intended use. Reuse established cases when suitable; avoid tests that merely search for the revised wording.
5. **Verify supported properties.** Check required metadata, resource paths, links/anchors and the containment rules for the standalone or bundled package with the owning structural tooling. Inspect scripts, assets or external dependencies when an instruction claim depends on them; identify uninspected behavior. Observe actual output or execution only when selected and authorized. Link validity does not establish client invocation or runtime support.
6. **Return actionable findings.** Give location/source, observation, consequence, confidence, priority, correction destination and objective recheck. Distinguish defects, recommendations and evidence gaps. Retain the coverage record, no-finding results, unresolved choices and unrun checks; do not present proposals as implemented repairs.

For an accepted revision, preserve technical meaning and scope, recheck affected owners/routes and review the resulting composition. Update affected navigation or projections without automatically enlarging every entry. Use the project's actual persistence and integration policy; this procedure introduces no Git, hosting or approval requirement of its own.

## Assessment contrasts and evidence

Adapt cases to the skill and selected artifact role; omit inapplicable ones with a reason. Use ordinary starting facts and paraphrased requests rather than fixed invocation syntax.

| Contrast | Inspect or observe |
| --- | --- |
| Intended use versus nearby out-of-scope use | Capability or local-purpose boundary; no invented output or dependency |
| Different supported variants | Explicit selection condition and relevant module, without loading unrelated branches |
| Request selecting a reference versus a nearby request outside its scope, with references unopened | Entry routing identifies the relevant file and boundary; no reference inspection needed to discover applicability |
| Sufficient context versus missing/stale input | Reuse or scoped recovery; unresolved consequential decisions remain unresolved |
| Assessment-only versus authorized changes | Appropriate effects and completion boundary |
| Successful path versus unavailable prerequisite or interrupted work | Concrete blocker/recovery and preservation of valid work |
| Requested partial result versus complete operation | Correct output, evidence and stop without unrequested continuation |

Source review establishes instruction coverage and consistency. A selected behavioral trial separately records the actual source/model, initial context, request, loaded instructions, observed actions, output and stop. Give a consumer only its ordinary task inputs and permitted instructions, not reviewer expectations. Correct routing is distinct from successful execution; structural checks are distinct from live acceptance. Qualify unavailable facilities and client-dependent behavior rather than claim universal support.
