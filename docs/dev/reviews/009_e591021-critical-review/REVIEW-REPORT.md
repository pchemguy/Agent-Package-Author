# Critical review report

## Baseline and evidence boundary

- Campaign: `009_e591021-critical-review`; [plan](REVIEW-PLAN.md). Pinned reviewed source: `e591021a4ca3ed4dc48b40fc984604bde3f7227d` on `main`. Review branch commits change only this report and active navigation, not the pinned source.
- Reviewer: Codex, 2026-11-05. This report records source inspection, structural checks and local execution separately. No target-client activation or Windows CMD execution is claimed.
- State: U-001–U-005 assessed and consolidated. Eight findings remain open for a separate revision decision; no source repair or integration was performed. A prior campaign's observations are not treated as evidence for this baseline.

## U-001 — Inventory and format baseline

- Source paths: the tracked baseline has 83 files and no tracked symlink. The delivered `agent-package-author/` contains 22 files: `SKILL.md`, twelve references, four Python helpers, four assets and `agents/openai.yaml`. Examples, tests and development records are outside the delivered directory. A source search over the delivered package, examples, tests and README found no hardcoded former workspace path, temporary path or `IMPLEMENTATION_LOG` dependency.
- Normative comparison: inspected current `references/skill-standard.md`, `plugin-standard.md`, `portability-policy.md` and `validation-policy.md` against the published [Agent Skills specification](https://agentskills.io/specification) and [Agent Plugins 1.0.0 specification](https://agent-plugins.org/specification) on 2026-11-05. Their sampled required metadata, optional skill resources, root manifest fields, fixed component discovery, missing-location treatment and plugin-root containment claims agree with the cited normative text. This is a source comparison, not a complete schema conformance proof.
- Resource check: a fenced-code-aware scan of the delivered Markdown found 33 operative local links; all targets exist and resolve inside `agent-package-author/`. `validate_skill.py agent-package-author` exited 0; `inspect_package.py agent-package-author` reported twelve references, four scripts, four assets, zero errors and zero warnings. A disposable skill with a contained linked reference exited 0; replacing its entry link with a missing target or a `../` escape exited 1 with `resource-missing` or `resource-escape`, respectively.
- Assessment: C-001 satisfied for the inspected baseline and cases. The current generator, nested resource links, plugin examples and actual client loading remain for later units. No finding in this unit.

## U-002 — Entry and reference composition

Read the creator `SKILL.md` and all twelve reference files in the pinned source. Assessed each at full-text source depth: `authoring-workflow` (intake and effects), `portability-policy` (classification), `validation-policy` (evidence), `skill-standard`/`skill-design`/`skill-review`/`hello-world-example` (skill format, capability boundaries, review and conditional exemplar), `plugin-standard`/`plugin-design`/`plugin-review` (plugin discovery, decomposition and optional coordinator), `mcp-packaging` (optional transport), and `openai-presentation` (per-skill presentation). This is instruction inspection, not an independent agent activation trial.

The entry directly names and links all twelve files and gives a load condition and boundary for each. Standalone creation, review-only, structural-only, a no-skill plugin, sibling handoff and optional MCP/presentation can be traced without assuming a plugin-wide `PLUGIN.md`. The detailed review modules are substantive; short format/classification modules serve shallow routing and owner summaries. No length-only split is warranted. The optional coordinator and `PLUGIN.md` criteria in `plugin-review` are conditional. The entry's review-only path explicitly stops without generation or writes.

### R-001 — Attachment authority is specified in the walkthrough but not the authoring procedure

- **Priority/type/confidence:** P2, instruction and cross-surface contract gap; medium-high source confidence, behavioral impact untested.
- **Located evidence:** `README.md` under “Complete authoring walkthrough” says an attachment can be a seed, reference or draft; the agent first records its role and authority and flags source conflicts during exploration. `references/authoring-workflow.md` steps 1–5 say to gather and reuse supplied requirements, then design/write, without classifying source roles, checking a draft against accepted requirements, or resolving conflicting sources. `references/openai-presentation.md` applies attachment role handling only to presentation context, after portable content exists. The entry does not route a general source-arbitration owner.
- **Consequence:** A normal authoring request with an older draft and newer brief can be executed by following the loaded procedure while silently treating both as requirements. The README's demonstrated exploration behavior is not guaranteed by the creator's operative instructions.
- **Bounded correction and recheck:** `authoring-workflow.md` should make source-role/authority and conflict resolution part of intake before accepting the package contract; link to a substantive owner only if that responsibility grows. Recheck with a conflicting seed, reference and draft, observing whether the agent identifies the difference before writing, while preserving a simple brief-only path.

Other U-002 routes were coherent on source inspection. Consumer selection of references, handoff activation, and whether a less capable model applies the distinctions remain untested.

## U-003 — Helpers, fixtures and failure behavior

Read all four Python helpers (609 lines), all seven test modules (620 lines), three templates and `tests/fixtures/format-cases.json`. The 50-test `unittest` suite passed; all four helpers' `--help` commands returned 0. Both shipped plugins passed `validate_plugin.py`, and the MCP plugin inspector reported two skills, one stdio server and zero structural errors. The creator self-check passed in U-001. These checks establish only the exercised paths.

Disposable skill probes showed: a valid linked reference passed; plain `description: 42` and an indented `metadata` value `version: 1.0` also passed; a reference containing a broken local link passed; and a fenced Markdown example containing `[missing](absent.md)` failed with `resource-missing`. The last three outcomes disagree with the helper's claimed string and operative-resource checks. All probes ran outside the repository and left no source changes. Source inspection confirms the corresponding `_scalar()` and entry-only regex logic. The test suite lacks these negative cases. Existing manifest/MCP tests do challenge type, namespace, transport, containment and partial component failure, but their pass does not cover every variant or client behavior.

### R-002 — Plain numeric YAML scalars receive false string validation

- **Priority/type/confidence:** P1, structural false success; high, from source and disposable CLI execution.
- **Located evidence:** `scripts/validate_skill.py` `_scalar()` returns a plain value as text after only a small reserved-word check (lines 28–50). A skill with `description: 42` exited 0; an indented `metadata` value `version: 1.0` also exited 0. YAML interprets these unquoted forms as numbers, whereas Agent Skills requires `description` and metadata values to be strings.
- **Consequence:** Invalid frontmatter can be certified by `validate_skill`, then by plugin validation/inspection using it. Quoted numeric strings should remain valid.
- **Bounded correction and recheck:** Frontmatter parser and tests should reject or explicitly mark implicitly typed YAML scalars unverified, including `name`, `description` and metadata. Test unquoted numeric, quoted numeric, and a valid ordinary skill; retain the documented bounded-parser behavior.

### R-003 — Links inside loaded references are not checked

- **Priority/type/confidence:** P2, resource-validation coverage; high, from source and disposable CLI execution.
- **Located evidence:** `scripts/validate_skill.py` extracts links and resource literals only from the `SKILL.md` `content` string (lines 133–151). A valid entry linking `references/guide.md` passed with exit 0 even when that reference linked nonexistent `absent.md`. The plugin validator and inspector call the same skill validator.
- **Consequence:** Strict success can hide an unavailable or escaping resource needed by a selected workflow. A manual inventory scan is not a replacement for the advertised helper result.
- **Bounded correction and recheck:** Traverse operative links in reachable local Markdown references with cycle handling and per-file resolution, while preserving the skill/plugin containment boundary and warning-only valid sibling links. A nested missing or escaping link must fail; a contained link and fenced illustrative text must pass.

### R-004 — Fenced example links are treated as operative resources

- **Priority/type/confidence:** P2, structural false failure; high, from source and disposable CLI execution.
- **Located evidence:** The same regex in `validate_skill.py` scans the whole entry without excluding fenced code. A skill whose body only showed a fenced `markdown` example containing `[missing](absent.md)` exited 1 with `resource-missing`, though the example does not instruct the agent to load that path.
- **Consequence:** A valid instructional skill can fail strict creator validation merely for teaching a negative path example. This also affects plugin child validation.
- **Bounded correction and recheck:** Parse operative links outside code spans/fences and distinguish actual resource literals from examples. Test fenced and inline-code examples against a real broken link in prose; keep the latter as an error.

The helper source read found no claim of executing included code during inspection, and the tested inspector remained read-only. Generated presentation and example MCP behavior are assessed in U-004. Target-native Windows and client execution remain untested.

## U-004 — Examples, presentation and reader path

Local execution of the shipped examples produced `3` for the standalone word count, `- First` for note outlining, and `missing: absent.md` for link checking. Both plugin variants passed strict structural validation in U-003. The MCP server returned a heading result and a correlated `isError` result for a missing note, but failed the malformed request sequence described below. A disposable plugin copy generated distinct YAML/SVG files for both children, with each `$name` prompt and parseable 128×128 SVG; a second run refused replacement and `--force` regenerated them. No presentation was written at plugin root. A 16-pixel raster render was attempted but the host's ImageMagick SVG delegate (`rsvg-convert`) was unavailable, so icon legibility is a geometry-based concern, not an observed visual pass or failure.

Read the README walkthrough and command/boundary sections, `AGENTS.md`, both root policies, current SPEC/PLAN and the shipped example entries against the assessed paths. The walkthrough clearly marks its attached seed/draft prompts as illustrative rather than executed; its per-reference map identifies all twelve modules. A fenced-code-aware scan of these active Markdown surfaces found 66 operative local links and no missing target. On this Linux host, the Windows CMD policy was inspected but not executed. The current development documents and delivered skill contain no dependency on a former checkout. The following concerns affect the user path.

### R-005 — Example MCP server drops malformed calls and can terminate

- **Priority/type/confidence:** P2, runtime recovery defect in a shipped example; high, observed in subprocess trials.
- **Located evidence:** `examples/with-mcp/notes-tools/bin/notes_server.py` `handle()` passes `arguments.path` to `Path` and catches `TypeError` only in `main()`. A `tools/call` with `path: 42` yielded no response for ID 7 and only stderr, while the following valid ID 8 succeeded. A separate sequence containing JSON `[]` raised an uncaught `AttributeError` at `request.get`, exited 1 and prevented the following valid request from being served. The tests cover initialize and tool listing but not these shapes.
- **Consequence:** A client can wait indefinitely for a call result or lose the server on malformed input, undermining the example's demonstration of an MCP tool boundary.
- **Bounded correction and recheck:** Validate request/params/argument shapes and return correlated JSON-RPC errors or tool `isError` responses for recoverable requests. Send each malformed input followed by a valid request; require an ID-correlated response and continued service while preserving the positive heading and missing-file behavior.

### R-006 — README's offline statement extends beyond the helpers

- **Priority/type/confidence:** P3, documentation precision; high from the wording and described workflow.
- **Located evidence:** `README.md` “Boundaries” says “The creator's runtime uses only Python's standard library and no network.” Its authoring walkthrough directs the agent to consult published external format specifications. The bundled Python helpers themselves are offline.
- **Consequence:** A reader may infer that the complete agent-led authoring workflow needs no network, which the walkthrough does not guarantee.
- **Bounded correction and recheck:** Scope the offline/standard-library promise to the bundled helpers, and state that external source consultation and generated package facilities depend on the task and host. Read both walkthrough branches against the revised statement.

### R-007 — The documented test command dirties a fresh checkout

- **Priority/type/confidence:** P3, developer reproducibility; high, from a disposable copy.
- **Located evidence:** `README.md` “Use” shows `python -m unittest discover -s tests -v`, while `AGENTS.md` uses `PYTHONDONTWRITEBYTECODE=1`. In a disposable copy, the README form passed but created `tests/__pycache__/` and `agent-package-author/scripts/__pycache__/`; root `.gitignore` does not exclude them.
- **Consequence:** A developer following the README gets untracked bytecode artifacts and an unexpectedly dirty checkout.
- **Bounded correction and recheck:** Align the README invocation with the clean developer command or ignore generated caches; rerun it in a fresh disposable copy and check for no untracked bytecode.

### R-008 — Generated icon text is too small for the stated small-size review

- **Priority/type/confidence:** P3, presentation legibility concern; medium, inferred from source geometry; visual rendering unverified on this host.
- **Located evidence:** `scripts/create_openai_presentation.py` lines 79–87 draws a 1–3-letter label at `font-size="15"` in a 128-unit viewBox. At 16×16 display, that is roughly 1.9 pixels of nominal font size. `references/openai-presentation.md` asks for recognizability at small sizes, and tests assert only label presence/XML validity. The creator's own `assets/icon.svg` uses a label-free package motif.
- **Consequence:** The text mark cannot function as a legible identifier at typical small-icon scale; it consumes visual space without reliable information. This is not a claim of observed client rendering.
- **Bounded correction and recheck:** Redesign the generated motif/mark for small displays and inspect actual 16/32-pixel renders, including 1- and 3-letter contexts. Keep XML and prompt/context tests, but do not treat them as a legibility test.

No source modification or target-client installation was performed. The examples' successful local scripts and structural validation do not prove their use by a particular agent or MCP client.

## U-005 — Consolidated coverage and disposition

| Surface / criterion | Assessment depth and result | Limits |
| --- | --- | --- |
| Delivered entry and twelve references / C-001–C-003 | Full-text source inspection, entry routing and adjacent ownership; R-001. The reference inventory is directly routed and the core format summaries match sampled normative rules. | No independent agent selection/authoring run; source wording cannot prove behavior. |
| Four helpers, templates, tests and fixture / C-004 | Full helper/test source inspection, 50 passing tests, CLI self/fixture checks and disposable counterexamples; R-002–R-004. Contextual presentation generated for both plugin skills with replacement refusal. | Bounded YAML parser was not compared against every valid YAML construct; Windows native paths and OpenAI client display not run. |
| Three shipped example package shapes / C-005 | Structural checks and standalone/skill script outputs passed; local MCP positive/error and malformed recovery probes; R-005. | No full target-client handshake or agent activation. |
| README, root policies, current SPEC/PLAN and active links / C-006–C-007 | Full reader-path inspection; 66 local links resolved; disposable documented test command; R-001, R-006–R-007. | Attached-file prompts are illustrative, not an executed authoring transcript. Windows policy inspected on Linux only. |
| Presentation / C-005–C-007 | Generated YAML/XML and source geometry examined; R-008. | Raster delegate unavailable, so visual legibility and client rendering remain unverified. |

**Finding index:** eight open findings: P1 `R-002`; P2 `R-001`, `R-003`, `R-004`, `R-005`; P3 `R-006`, `R-007`, `R-008`. `R-003` and `R-004` share the link-scanning owner and need one parser design with tests that avoids replacing a false success with a false failure. `R-002` shares the skill validator but is a separate metadata semantics issue. All findings describe the pinned source; none is accepted as an implementation task by this review request.

**Proposed revision order:** first correct `R-002` and its quoted/unquoted regression cases; then design and test operative link traversal for `R-003`/`R-004`; then fix MCP recovery `R-005` with malformed-then-valid sequences. Align authoring intake with the README's source authority claim (`R-001`), and address the scoped documentation/housekeeping concerns (`R-006`/`R-007`). For `R-008`, obtain actual small-size rendering before selecting a motif redesign. The order is a recommendation, not an accepted revision plan.

**No-finding areas and uncertainty:** current sampled published format claims, package inventory/containment, entry reference inventory, optional no-skill/plugin/MCP routing, template schemas in tests, normal CLI paths, example positive outputs and active local links gave no additional finding at the recorded depth. The absence of a finding does not certify untested variants, security, usability in a specific client or universal portability. No source changes, installations, releases or external client trials were made. The review stops at this published report pending a separate decision on revision and integration.
