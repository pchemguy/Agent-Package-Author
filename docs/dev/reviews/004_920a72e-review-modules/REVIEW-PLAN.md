# Proposed review modules: critical assessment plan

- Campaign: `004_920a72e-review-modules`
- Starting baseline: `920a72ecbfe70cf5733cbf45da1fa0f995585824` (`main`)
- Working branch: `revision/004_920a72e-review-modules`
- Target: `main`, if a later revision is accepted and verified
- Current stopping boundary: publish the assessment and proposed decisions on this branch; no APA source integration or repair is selected yet.

## Intake

The three user-supplied files are preserved byte for byte under [inputs](inputs/), including their CRLF line endings. The scoped `.gitattributes` disables text conversion for these historical inputs. They are proposal material, not APA instructions or accepted requirements. The proposal came from SDD Manager campaign 060 and mentions additional contract, draft and review records that were not supplied. Its relative links back to that campaign are provenance links and are not APA-local dependencies.

## One integrated review unit

Assess the proposal and both modules together, comparing each proposed owner and trigger with the current APA entry, references, SPEC, README and validator/inspector boundaries. In order:

1. Check scope, evidence and format claims against the published Agent Skills and Agent Plugins 1.0.0 specifications; separate normative rules from APA authoring policy and optional client conventions.
2. Trace a focused assessment, comprehensive skill review, comprehensive plugin review, ordinary authoring/revision, plugin without skills, and an optional coordinator/`PLUGIN.md` path through the proposed instructions and current APA owners. Identify duplication, unavailable prerequisites and wrong effects at handoffs.
3. Review instruction structure and coverage in the two modules: entry versus reference responsibility, integrated plugin versus unrelated bundle, source evidence versus observed behavior, stopping boundaries, and practicality for simple packages.
4. Propose an integrated owner map and routing shape: what moves into each current APA owner, what remains in two review modules, what is consolidated or omitted, and how review-only and authorized authoring paths share assessment without changing their effects. Give a representative skill and plugin route from entry to output.
5. Record stable findings with locations, consequence, confidence, priority, proposed disposition and objective recheck. Preserve supported aspects and unresolved choices. Only source inspection and standards comparison are in scope for this assessment; behavioral trials and changed-package validation belong to any later accepted implementation.

The review report is the checkpoint for this unit. Commit and publish it before further repository work. The supplied files remain unchanged, and prior closed campaigns remain outside the diff.
