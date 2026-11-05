# Critical review report

## Baseline and evidence boundary

- Campaign: `009_e591021-critical-review`; [plan](REVIEW-PLAN.md). Pinned reviewed source: `e591021a4ca3ed4dc48b40fc984604bde3f7227d` on `main`. Review branch commits change only this report and active navigation, not the pinned source.
- Reviewer: Codex, 2026-11-05. This report records source inspection, structural checks and local execution separately. No target-client activation or Windows CMD execution is claimed.
- State: U-001–U-003 assessed; U-004–U-005 pending. Four findings allocated. A prior campaign's observations are not treated as evidence for this baseline.

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
