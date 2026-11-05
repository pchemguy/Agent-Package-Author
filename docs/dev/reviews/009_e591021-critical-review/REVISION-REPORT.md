# Critical review revision report

The original [review](REVIEW-REPORT.md) remains the record of findings at `e591021a4ca3ed4dc48b40fc984604bde3f7227d`. This report tracks corrections against the [revision plan](REVISION-PLAN.md). Final disposition and integration evidence appear after the bounded actions.

## A-001 — YAML scalar types (R-002)

Changed `agent-package-author/scripts/validate_skill.py` and `tests/test_skill_validation.py`. The bounded frontmatter parser now rejects YAML core null, boolean, integer and float plain scalars as unsupported when a string is required, including case variants and numeric prefixes. Quoted equivalents continue to be strings. `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_skill_validation -q`: 8 tests passed, including the targeted matrix over name, description and metadata. This is a bounded parser, not a complete YAML implementation; unsupported forms are reported as unverified.

## A-002 — Reachable resources and examples (R-003, R-004)

Changed `validate_skill.py`, `tests/test_skill_validation.py` and `tests/test_plugin_validation.py`. The scanner follows reachable Markdown links relative to each containing file, visits cycles once, enforces the skill or plugin boundary on each target, and reports the containing path. Fenced and inline-code Markdown examples are excluded; explicit resource-path literals in the entry remain checked. Nested references may use inline paths as examples of generated output, so only linked paths in nested files are dependencies. `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_skill_validation tests.test_plugin_validation -q`: 25 tests passed. The creator's own `validate_skill.py agent-package-author` succeeds with no findings. This is a bounded Markdown link scanner, not a full CommonMark parser.

## A-003 — MCP request recovery (R-005)

Changed `examples/with-mcp/notes-tools/bin/notes_server.py` and `tests/test_authoring.py`. The line server now answers non-object and unparsable requests with JSON-RPC errors, validates identified calls and tool arguments, and continues serving after malformed input. For a valid path, the tool still returns headings; a missing file remains a tool-level error. `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_authoring -q` passes, including a five-request malformed/valid sequence with correlated IDs.

## A-004 — Intake authority and documentation (R-001, R-006, R-007)

Changed `agent-package-author/references/authoring-workflow.md`, `README.md` and `.gitignore`. The operative intake now records seed, reference and draft roles, provenance, conflicts, authority and observable acceptance decisions, including the brief-only path. The README's offline statement is scoped to bundled Python helpers, while authoring can consult external references. Python bytecode caches are ignored so the documented cross-platform test command leaves a fresh Git checkout clean. Rechecked the instruction paths and disposable test run in the final regression section.

## A-005 — Small-size icon (R-008)

Changed `create_openai_presentation.py`, `openai-presentation.md` and presentation tests. Generated SVGs enlarge the chosen motif and omit the tiny pill and visible text. The accepted `icon_label` remains useful as an accessible abbreviation in the SVG's `aria-label`; it is not a visual mark. `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_openai_presentation -q`: 7 tests passed, including XML and context checks. Inkscape rendered all four motifs at 16 pixels and the default package motif at 32 pixels; visual inspection found recognizable silhouettes without lettering. This checks local rendering, not client display.
