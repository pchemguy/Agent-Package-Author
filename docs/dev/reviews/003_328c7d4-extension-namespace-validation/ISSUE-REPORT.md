# Validator incorrectly rejects the two-component extension namespace `com.openai`

## Summary

Agent Package Author rejects an otherwise valid plugin manifest containing `extensions.com.openai`, even when its value is an object. This is a validator false positive caused by a minimum-component error in its namespace regex, not a manifest conformance failure.

## Cause

In `scripts/validate_plugin.py`, line 17:

```python
NAMESPACE = re.compile(r'[a-z0-9]+(?:\.[a-z0-9-]+){2,}\Z')
```

The first component is matched before the repeated group. `{2,}` therefore requires at least two additional components: three in total. `com.openai` has two components and fails; `com.example.product` has three and passes.

The manifest check at lines 70–72 uses this regex and emits a combined namespace/value error, although the reproduction uses a valid object value. The pinned Agent Plugins 1.0.0 schema permits object-valued extension entries and specifies no three-component minimum.

Schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json

## Reproduction

Prerequisite: Python 3 and an Agent Package Author checkout containing `scripts/validate_plugin.py` and its sibling imports. Run from that checkout:

```bash
PYTHONDONTWRITEBYTECODE=1 python - <<'PYTHON'
import json
from pathlib import Path
import subprocess
import sys
import tempfile

validator = Path("scripts/validate_plugin.py").resolve()
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    for namespace in ("com.openai", "com.example.product"):
        manifest = {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "name": "namespace-repro",
            "extensions": {namespace: {}},
        }
        (root / "plugin.json").write_text(json.dumps(manifest), encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(validator), str(root)],
            capture_output=True, text=True,
        )
        print(f"{namespace}: exit {result.returncode}")
        print(result.stdout + result.stderr, end="")
PYTHON
```

Observed result (temporary path varies):

```text
com.openai: exit 1
ERROR: /tmp/.../plugin.json: extensions: 'com.openai' must be a reverse-domain namespace with object value
com.example.product: exit 0
```

Expected: both manifests pass namespace validation and exit with code 0.

## Impact and requested correction

Valid plugins using `extensions.com.openai` are reported as invalid. The error can prompt unnecessary manifest changes and misleading compatibility warnings.

Correct the minimum-component check to accept two-component reverse-domain namespaces. Changing `{2,}` to `{1,}` addresses this specific false positive; retain validation of object values and malformed namespaces. Add regression tests for two- and three-component namespaces, malformed names, and non-object extension values.

Also review extension-directory handling: it shares `NAMESPACE`, but its discovery condition currently checks `child.name.count('.') >= 2`, so two-component directory names bypass that check. This is a related code-path concern, not a demonstrated directory rejection.

## Verification evidence

Reproduced on Python 3.12.14 using the installed validator snapshot. The minimal `com.openai` manifest also passed validation against SDD Manager's pinned Agent Plugins 1.0.0 schema using `jsonschema`.

Validator file SHA-256:
`bb0170ba1c405186d7baae5380ed448d0799c5c1e19ffd14512c396685c8f6c2`

This report records the defect; no validator or plugin manifest was changed.
