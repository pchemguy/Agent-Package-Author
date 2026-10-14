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

## V-03 through V-05

Pending implementation and final merged-state verification.
