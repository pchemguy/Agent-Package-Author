# Package review revision report

## A-001 — Per-reference workflow-component assessment

Added a per-file content verdict to `skill-review.md`: for each reference in a comprehensive skill review, or each selected reference in a focused review, trace its entry condition and distinct contribution to a decision, action, constraint, check or handoff. Record a located finding if the file has no such workflow component. The criterion permits shared guidance that governs an identifiable step without demanding a standalone procedure, and it remains separate from format validation. The review procedure now records the verdict for each assessed file and identifies unassessed references in a focused review.

Aligned `skill-design.md`, `portability-policy.md`, `docs/dev/SPEC.md`, the creator entry and README. Standalone examples/background belong in the source repository README or root `examples/`. A skill-local `examples/` needs a concrete runtime use, explicit loading route and strong inclusion rationale; it has no special discovery status. Brief explanation inside an operational reference can still clarify its rule. The user-supplied negative example is not used as an illustration in the new review aspect.

Source-level contrasts: a selected procedure has its own action/result; cross-cutting guidance can govern a concrete decision; material with only topical or illustrative value receives an absent-component finding and a placement recommendation. `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` passed 55 tests. The creator validator exited 0; inspector reported twelve references, four scripts, four assets, zero errors and zero warnings. `git diff --check` passed. These checks do not constitute a complete content review or target-agent trial.

## A-002 — Coupled criterion check

The published/read-back A-001 tip is `5190d83339db7957f9e91de138716562d4de8832`. A fresh full suite passed 55 tests; self-validation exited 0; the inspector reported twelve references, four scripts, four assets and zero errors/warnings. Active campaign links resolve and `git diff --check main...HEAD` passed. The diff touches only the creator's relevant review/design/classification guidance, entry, README, governing SPEC and active campaign/HANDOFF records. The new criterion makes a per-file source judgment; the Python validator remains structural. No complete review of all twelve existing references, target-client trial or package relocation is claimed by this checkpoint. A-003 addresses the identified bundled exemplar separately.

## A-003 — Source-only design example placement

Moved the non-operative design exemplar from the delivered skill's `references/` to root `examples/hello-world-design.md`, marked it as source-only and removed its runtime entry route. README now presents it as repository material rather than an installed-skill module; the reference loading map names eleven runtime modules. Reconciled `docs/dev/SPEC.md`, `PLAN.md` and the existing authoring test. No source-only file is required by the installed creator to work from a user's brief or attachment.

The full suite passed 55 tests; `validate_skill.py agent-package-author` exited 0; `inspect_package.py` reported eleven references, four scripts, four assets, zero errors and zero warnings. The README's moved-file links resolve, the delivered entry has no source-only link, and staged/unstaged whitespace checks passed. These checks show packaging and source consistency, not host routing behavior. Historical closed-campaign records retain their original references as history; the new review criterion itself does not use this file as an illustrative case.
