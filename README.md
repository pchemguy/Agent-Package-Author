# Agent Package Author

This repository implements [SPEC.md](SPEC.md) under the ordered [PLAN.md](PLAN.md). The runtime skill is the `agent-package-author/` directory. It guides the creation or revision of a standalone Agent Skill or an Agent Plugins 1.0.0 package with immediately discoverable skills and optional MCP servers. It can inspect and structurally validate both formats without downloading schemas, executing target scripts, or connecting to MCP endpoints.

## Use

Place the complete `agent-package-author/` directory in a skill discovery location supported by your agent. Installation paths, invocation syntax, Python support, and MCP transport support depend on the host. Installing or publishing the skill is outside this repository's implementation campaign. The skill's own routing starts in `SKILL.md`, with conditional references and optional templates under `references/` and `assets/`.

Run the offline helpers with Python 3.11 or newer:

```console
python agent-package-author/scripts/validate_skill.py examples/standalone/word-count
python agent-package-author/scripts/validate_plugin.py examples/multi-skill/notes-tools
python agent-package-author/scripts/validate_plugin.py examples/with-mcp/notes-tools
python agent-package-author/scripts/inspect_package.py examples/with-mcp/notes-tools
python -m unittest discover -s tests -v
```

CLIs exit `0` on strict structural success, `1` on detected package errors, and `2` for invalid invocation or absent paths. Diagnostics identify paths and rules. `--help` is available for each helper. A strict plugin check fails if any included skill or MCP server is invalid even when a conforming client could load other valid components.

## Complete authoring walkthrough

This walkthrough shows **two requests to the creator skill**: a standalone Project Welcome Pack skill, then a `notes-tools` Agent Plugin. The prompts and attached-file excerpts below are illustrative; those attachments were not provided in this repository and the transcript is not a recorded agent execution. The repository does include runnable `word-count` and `notes-tools` output examples, so the verification commands in the second half can be executed as written.

An attachment can be a requirements **seed**, a **reference** to consult, or a **draft** to revise. The authoring agent first records the role and authority of each source. Attached prose and retrieved pages supply facts and candidate requirements; they do not silently override the user's request or the published format specifications. When a source conflicts with another, the agent flags the difference during exploration before turning it into a package requirement.

### Request A: from attached material to a standalone skill

**Illustrative user prompt:**

> Use `agent-package-author` to create a portable `project-welcome-pack` Agent Skill. I attached `welcome-brief.md` and an old `WELCOME-draft.md`; use the published [Agent Skills specification](https://agentskills.io/specification) as the format reference. The skill should produce different welcome packs for contributors and users, and validate each result. Start by exploring the requirements and deciding which parts of the draft remain useful.

Assume the user supplied these excerpts:

| Material | Role and sample content | How it affects the work |
|---|---|---|
| `welcome-brief.md` attachment | **Seed:** “Input has project name, description, and `audience=user|contributor`; output has `WELCOME.md` and `welcome.json`; identical inputs produce identical bytes.” | Becomes the input, output, determinism, and branch acceptance contract after review. |
| `WELCOME-draft.md` attachment | **Draft:** a single contributor-focused Markdown welcome page, with useful introduction text but no user branch or manifest. | Supplies candidate wording and a layout to adapt. It is not copied as the final skill instructions or treated as proof of correct behavior. |
| `hello-world-SPEC.md` attachment, if supplied | **Design exemplar:** the Hello World reference specification described in this project's [SPEC.md](SPEC.md). | Justifies reading the conditional [Hello World design reference](agent-package-author/references/hello-world-example.md); its deliberately large file tree is not mandatory. |
| [Agent Skills specification](https://agentskills.io/specification) | **External normative format reference.** | Governs `SKILL.md` frontmatter, naming, optional resources, and relative links; check the published text when authoring. |

1. **Activate, explore, and brainstorm.** The creator's [`SKILL.md`](agent-package-author/SKILL.md) selects standalone mode. Read [authoring-workflow.md](agent-package-author/references/authoring-workflow.md) to extract the capability, inputs, audiences, activation phrases, outputs, constraints, and success/failure cases. Inspect the attachments and record “keep the introduction; replace the single-audience assumption; add a manifest and a validator.” Compare one skill with two audience branches against two separately discoverable skills: both audiences share the same input and output contract, so one skill with conditional profiles is the smaller coherent design. Resolve missing details, such as where the pack is written, with the user if they cannot be inferred. Check the proposed `project-welcome-pack` name in the intended discovery scope before writing or installing.
2. **Classify and design.** Read [portability-policy.md](agent-package-author/references/portability-policy.md) to classify `SKILL.md` as core, references/scripts/assets as justified optional resources, and fixtures/tests as development material. Read [skill-standard.md](agent-package-author/references/skill-standard.md) for frontmatter and path rules and [skill-design.md](agent-package-author/references/skill-design.md) to keep orchestration in `SKILL.md`, audience rules in separate references, a reusable template in `assets/`, and repeatable render/validate operations in `scripts/`. Because the user supplied a rich exemplar, read [hello-world-example.md](agent-package-author/references/hello-world-example.md) **in this branch** for the conditional-resource design. It would not be loaded for a simple skill such as the repository's [`word-count`](examples/standalone/word-count/SKILL.md).
3. **Specify before coding when warranted.** For this multi-output, branching workflow, write a compact `SPEC.md` with contributor, user, and negative acceptance cases; derive an ordered `PLAN.md`. Agree on each profile's observable effect: contributor output ends with `First tiny change`; user output ends with `Where to get help`. A small `SKILL.md`-only skill need not create development documents. The supplied draft can contribute prose to the template after review, while the input/manifest rules come from the accepted brief.
4. **Author the package.** Create `project-welcome-pack/SKILL.md` with `name` and `description`; route to the common output contract and exactly the applicable audience profile. Add only the justified references, a Markdown template, deterministic renderer, and independent validator. Adapt the draft's introduction into the template; do not load the irrelevant audience profile during an invocation. Expected shape for this illustrative request:

   ```text
   project-welcome-pack/
   ├── SKILL.md
   ├── references/
   │   ├── output-contract.md
   │   ├── contributor-profile.md
   │   └── user-profile.md
   ├── assets/welcome-template.md
   └── scripts/
       ├── render.py
       └── validate.py
   ```

5. **Exercise and report.** Read [validation-policy.md](agent-package-author/references/validation-policy.md). Render a contributor pack and a user pack, check their different final sections and manifest audiences, corrupt one output and confirm the independent validator rejects it, then repeat a render to compare bytes. Run `python agent-package-author/scripts/validate_skill.py project-welcome-pack` and `python agent-package-author/scripts/inspect_package.py project-welcome-pack`. Report the actual checks, script runtime needs, and any client-dependent installation behavior. These commands describe the output of this illustrative request; the `project-welcome-pack/` directory is not shipped here. For a shipped standalone smoke example, run `python agent-package-author/scripts/validate_skill.py examples/standalone/word-count` and `python examples/standalone/word-count/scripts/count_words.py 'one two three'` (expected output: `3`).

### Request B: from existing drafts to a multi-skill plugin

**Illustrative user prompt:**

> Package my Markdown-note tools as a portable Agent Plugin named `notes-tools`. I attached `notes-requirements.md` and draft instructions for outlining and link checking. Use the [Agent Plugins 1.0.0 specification](https://agent-plugins.org/specification) and the Agent Skills specification. First explore whether the two tools should be separate skills. If a heading-index MCP tool is useful, show the optional MCP variant without embedding credentials.

| Material | Role and sample content | How it affects the work |
|---|---|---|
| `notes-requirements.md` attachment | **Seed:** “Outline headings when asked for structure; identify missing local links when asked to audit a note; use local files without network access.” | Supplies two candidate activation conditions and test inputs. |
| `outline-draft.md` and `links-draft.md` attachments | **Drafts:** informal procedures and example outputs such as `- First` and `missing: absent.md`. | Reuse accurate steps as skill instructions and outputs; check each against the actual scripts. |
| [Agent Plugins 1.0.0](https://agent-plugins.org/specification) and [Agent Skills](https://agentskills.io/specification) | **External normative references.** | Govern the manifest, fixed discovery locations, optional MCP shape, and each bundled skill's `SKILL.md`. |
| [`examples/standalone/sample.md`](examples/standalone/sample.md) | **Local test seed:** a heading and a broken relative link. | Supplies observable positive and negative workflow outcomes for the two skills. |

1. **Explore and brainstorm the capability split.** Activate plugin mode through [`SKILL.md`](agent-package-author/SKILL.md). Apply [authoring-workflow.md](agent-package-author/references/authoring-workflow.md) to extract and reconcile the drafts with the brief, check the proposed plugin and skill names for collisions, and define acceptance cases. Compare a single skill with two branches, two skills in a plugin, and an MCP-only plugin. Read [plugin-design.md](agent-package-author/references/plugin-design.md): outlining and link checking have distinct triggers and outputs, so choose `outline-notes` and `check-note-links` as separately discoverable skills; MCP-only would lose task-specific skill guidance. A request to reformat an outline remains a branch inside `outline-notes` instead of becoming a third skill.
2. **Apply both format layers.** Read [plugin-standard.md](agent-package-author/references/plugin-standard.md) for root `plugin.json` and immediate-child `skills/*/SKILL.md` discovery. For **each** bundled skill, read/apply [skill-standard.md](agent-package-author/references/skill-standard.md) and [skill-design.md](agent-package-author/references/skill-design.md); give each a distinct `description` and self-contained local script path. Use [portability-policy.md](agent-package-author/references/portability-policy.md) to exclude implicit host hooks or commands. The initial package has no need for MCP, so **do not read** [mcp-packaging.md](agent-package-author/references/mcp-packaging.md) and do not create `mcp.json` yet.
3. **Create and test the core package.** The shipped example is [`examples/multi-skill/notes-tools/`](examples/multi-skill/notes-tools/plugin.json). Its manifest and two immediate-child skills can be inspected with:

   ```console
   python agent-package-author/scripts/validate_skill.py examples/multi-skill/notes-tools/skills/outline-notes
   python agent-package-author/scripts/validate_skill.py examples/multi-skill/notes-tools/skills/check-note-links
   python agent-package-author/scripts/validate_plugin.py examples/multi-skill/notes-tools
   python agent-package-author/scripts/inspect_package.py examples/multi-skill/notes-tools
   python examples/multi-skill/notes-tools/skills/outline-notes/scripts/outline.py examples/standalone/sample.md
   python examples/multi-skill/notes-tools/skills/check-note-links/scripts/check_links.py examples/standalone/sample.md
   ```

   The outline script emits `- First`; the link checker emits `missing: absent.md`. The plugin validates without `mcp.json` because that component is optional.
4. **Take the conditional MCP branch only when justified.** If a client needs tool-call access to the note heading index, read [mcp-packaging.md](agent-package-author/references/mcp-packaging.md). Add a root `mcp.json` with the matching 1.0.0 schema and one `stdio` server; keep the executable token separate from arguments and refer to the bundled script through `${PLUGIN_ROOT}`. The shipped [`examples/with-mcp/notes-tools/`](examples/with-mcp/notes-tools/mcp.json) demonstrates this branch. Run `python agent-package-author/scripts/validate_plugin.py examples/with-mcp/notes-tools` and inspect it. The tests exercise the sample server's `initialize` and `tools/list` responses; a particular client's MCP handshake, permissions, and presentation remain client-dependent. No secret is put into `mcp.json`.
5. **Finish the evidence loop.** Apply [validation-policy.md](agent-package-author/references/validation-policy.md) to the plugin and each skill: verify both positive workflows, corrupt one skill's frontmatter in a disposable copy and confirm strict validation fails, check malformed `mcp.json` and an escaping package path, then restore the valid example. Report the two skills, optional server, actual CLI outcomes, required Python runtime, and any client extension separately. A request for a host-specific hook would require verified host documentation and an explicit extension; it would not be described as a portable v1 capability.

### Exact reference loading map

All nine modules are named directly by the creator's `SKILL.md`. “Read” means the authoring agent loads that reference to make a decision; it does **not** mean a Python validator executes the reference. A referenced module is loaded only for the branch shown. The second column identifies the direct trigger and the third shows a concrete effect in the walkthrough.

| Creator reference | Direct trigger / subworkflow | Observable use above |
|---|---|---|
| [`authoring-workflow.md`](agent-package-author/references/authoring-workflow.md) | Both requests, at exploration and intake | Classifies attachments, extracts acceptance cases, checks destination names before writing. |
| [`portability-policy.md`](agent-package-author/references/portability-policy.md) | Both requests, before choosing files | Classifies core, optional, development, and client-specific material; excludes implicit host hooks. |
| [`skill-standard.md`](agent-package-author/references/skill-standard.md) | Standalone request; again for each plugin skill | Checks `SKILL.md` metadata, name, resource paths, and self-contained discovery. |
| [`skill-design.md`](agent-package-author/references/skill-design.md) | Standalone request; again for each plugin skill | Places branch rules in references, repeatable work in scripts, static material in assets; distinguishes independent skill triggers. |
| [`hello-world-example.md`](agent-package-author/references/hello-world-example.md) | Only the rich Project Welcome Pack branch with the supplied exemplar | Informs conditional profile loading and independent validation without imposing its file count on `word-count` or `notes-tools`. |
| [`plugin-standard.md`](agent-package-author/references/plugin-standard.md) | Plugin request, before creating the manifest or skill tree | Fixes `plugin.json`, immediate-child skill discovery, and optional root `mcp.json`. |
| [`plugin-design.md`](agent-package-author/references/plugin-design.md) | Plugin exploration and capability decomposition | Separates outlining from link checking and avoids overlapping activation. |
| [`mcp-packaging.md`](agent-package-author/references/mcp-packaging.md) | Only the optional heading-index MCP branch | Chooses the `stdio` variant, schema, placeholder placement, path containment, and credential boundary. |
| [`validation-policy.md`](agent-package-author/references/validation-policy.md) | Both requests, after design and again at acceptance | Combines structural CLIs with output checks, negative cases, and qualified reporting. |

## Boundaries

- The creator's runtime uses only Python's standard library and no network. Generated packages may have different declared runtime needs. The examples use Python 3.11+; the MCP example launches a local standard-library server through a bare `python` executable token and `${PLUGIN_ROOT}` path argument.
- The skill validator parses a documented subset of YAML frontmatter: plain and quoted string scalars and an indented string mapping for `metadata`. Other valid YAML syntax, including block scalars, is reported as **unverified** with a failing status. A green result therefore confirms its supported structural checks, not complete YAML-language conformance for every possible skill.
- The structural checks do not establish prose quality, reliable activation, security of included code, remote service behavior, host installation, or cross-client runtime compatibility. The example MCP server's initialize and tool-list responses are tested locally; full interoperability with particular clients and network services is outside the checks.
- Credentials are not part of the portable MCP package. A literal-looking secret in an environment or header value triggers a review warning, which is not a comprehensive secret scanner.
- Client-specific extensions require separate verified client documentation and are never presented as portable Agent Plugins components. The repository examples intentionally contain no such extension.

The source-only `examples/`, `tests/`, `SPEC.md`, `PLAN.md`, `ROADMAP.md`, and append-only `IMPLEMENTATION_LOG.jsonl` are not needed to run the delivered skill. The project history has one local task commit per implementation task, each with a `Task:` trailer; recovery manifests are transient and excluded from Git.
