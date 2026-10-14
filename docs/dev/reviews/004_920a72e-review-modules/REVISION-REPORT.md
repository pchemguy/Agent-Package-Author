# Revision evidence: integrated content review

- Campaign: `004_920a72e-review-modules`
- Baseline: `920a72ecbfe70cf5733cbf45da1fa0f995585824`
- Target: `main`

## Preparation and V-01

The accepted contract amendment was prepared on `design-docs/004_920a72e-review-modules` (`94d47c7`, `1690a83`), merged into `main` at `bc0386948264d9f3bb607a307bd8ec11e0b6f28e`, then incorporated into the campaign at `d812c63e4e759b955ef51a775d6b854d04d203a9`. Both branches were pushed and remote readback matched. `docs/dev/SPEC.md` and `PLAN.md` own the accepted capability and gates.

## V-02: source preservation and review criteria

The three supplied documents under `inputs/` are historical evidence, stored with original bytes and CRLF endings. The scoped `.gitattributes` prevents Git text conversion. Their SHA-256 digests are:

| Input | SHA-256 |
| --- | --- |
| `PROPOSED-REVISIONS.md` | `fac9566e42824e9ceec3b81b2a593759631bbaa01db3dcd39b3ee96184b9ab93` |
| `skill-review.md` | `7acf7900a5c86cda0272fa4e4896329d00faa4c869eb82f6dfe5a6e19fe5b520` |
| `plugin-review.md` | `ee767a246925ccf3877cfbf68621a47d4f9a63d371a4f73419bcccb45d35174c` |

The runtime `skill-review.md` retains entry and reference routing, local composition, bounded/full coverage and meaningful contrasts. The runtime `plugin-review.md` retains composition, optional shared entry/coordinator and cross-component handoff criteria. Shared evidence belongs to `validation-policy.md`; format rules and design remain with their existing owners. The runtime modules do not treat `PLUGIN.md`, coordinators, or skills in an existing no-skill plugin as mandatory. No unseen SDD contract is treated as authority.

## V-03: operation routing and owner integration

`17f436d15bf810d256511f78607ca84cb93c6731` refactors the entry to select operation before package type and directly links all twelve references with purpose, boundary and loading condition. `skill-design.md` owns APA's direct reference routing policy, `plugin-design.md` owns optional shared-entry design, `authoring-workflow.md` owns permitted changes, and `validation-policy.md` owns source/structure/workflow/client evidence. `agents/openai.yaml` now advertises review. README and AGENTS orientation follow those owners. The runtime modules remain adapted criteria rather than new format rules or validators.

## V-04: source and structural checks

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q`: 50 tests passed. The reference-inventory test compares actual `references/*.md` against all direct Markdown links in the entry and confirms each target exists.
- `validate_skill.py agent-package-author` and `inspect_package.py agent-package-author`: zero errors/warnings; 12 references, four scripts, four assets. The inspector explicitly says runtime is unverified.
- `validate_skill.py examples/standalone/word-count`, `validate_plugin.py examples/multi-skill/notes-tools`, and `validate_plugin.py examples/with-mcp/notes-tools`: all exit zero. Plugin inspector on both examples: two skills each, optional MCP only in the latter, zero errors/warnings, runtime unverified.
- A disposable plugin with only a valid manifest passes both plugin validator and inspector (zero errors/warnings, no invented skills). This establishes structural acceptance, not an MCP-only authoring promise.
- A local Markdown link scan over README, AGENTS and runtime Markdown, excluding fenced illustrative code, checked 92 links with zero missing targets. `git diff --check main...HEAD` passed. All three committed input blobs have SHA-256 digests identical to the table above.

Source scenario trace (entry and linked owner text, not a consumer trial):

| Request | Route and effect | Evidence limit |
| --- | --- | --- |
| Focused skill-entry routing review | Entry selects review then skill, loads the relevant `skill-review.md` criteria; no authoring workflow or writes. | Source route, not observed client selection. |
| Comprehensive mixed plugin review | Entry selects plugin review, inventories package, applies `plugin-review.md` and `skill-review.md` to actual children; optional MCP owner only for present config. | Source and structural inventory; not full client execution. |
| Existing no-skill plugin composition review | Plugin criteria and actual components only; no child entry/presentation obligations. | Disposable validator/inspector pass does not prove prose review quality. |
| Create/revise from supplied drafts | Authoring workflow retains collision/authority checks, proportionate content review, permitted repair, OpenAI presentation and verification. | README is illustrative; no independent consumer trial. |
| Existing optional `PLUGIN.md` or coordinator | Relevant conditional criteria apply only when present, with explicit loading/fallback; absent artifacts impose no requirement. | No host loading claim. |

## Findings disposition

| Finding | Integrated owner and resolution |
| --- | --- |
| R-001 | Operation-first `SKILL.md`, review-only stopping boundary; authoring workflow loaded only for writes. |
| R-002 | Published SPEC/PLAN preparation and README/entry alignment. |
| R-003 | `plugin-design.md` and `plugin-review.md` constrain `PLUGIN.md` to an explicit loader and optional role. |
| R-004 | Entry and plugin review cover existing no-skill packages without creating an MCP-only authoring promise. |
| R-005 | `skill-design.md` and `skill-review.md` make direct routing a content policy; no Python format error. |
| R-006 | Shared evidence and effects have single validation/authoring owners; review modules retain detailed criteria. |
| R-007 | The three exact supplied inputs are preserved; unseen SDD records provide no authority. |

## V-05: merge and remote verification

The published campaign tip `25136f9be611f129681eddf9158ddd88cdd54b7c` was integrated into refreshed `main` (`bc0386948264d9f3bb607a307bd8ec11e0b6f28e`) with `--no-ff --no-commit`, after remote `main` was fetched and confirmed equal to local. The staged merge passed the complete 50-test suite, creator self-validator/inspector, standalone example, both plugin example validators and MCP plugin inspector, and `git diff --cached --check`. The resulting merge commit has these two parents; remote push/readback is checked after commit. No independent target-client consumer trial was performed; structural checks and source routing do not establish activation or runtime behavior on a host.
