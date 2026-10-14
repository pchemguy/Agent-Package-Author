# Independent verification: extension namespace validation

- Campaign: `003_328c7d4-extension-namespace-validation`
- Reviewed repository baseline: `328c7d4034ab4bd141d5b88ddabfc65ae924d76e` (`main`)
- Scope: `agent-package-author/scripts/validate_plugin.py`, its tests, and the Agent Plugins 1.0.0 extension rules. This is a separate review of the repository checkout, not the installed snapshot described in the [submitted issue](../ISSUE-REPORT.md).

## Method and source

I inspected the manifest check and top-level directory scan, then ran the repository CLI from the repository root against disposable plugin directories. The repository entry point is `agent-package-author/scripts/validate_plugin.py`; the submitted report's `scripts/validate_plugin.py` path assumes the delivered skill directory is the working directory. I checked the [published specification, §8](https://agent-plugins.org/specification#8-client-extensions) and the [published manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json) on 2026-10-14. The specification calls for reverse-domain namespace names, without a three-component minimum; the schema permits object-valued extension entries and supplies no minimum component count or `propertyNames` expression. Its three-component example is illustrative. This creator intentionally performs stricter authoring validation than a client loader; the schema alone is not a complete namespace grammar.

## Findings at baseline

| ID | Reproduction and result | Assessment |
| --- | --- | --- |
| N-01 | A minimal manifest with `"extensions":{"com.openai":{}}` exits `1` with `extensions: 'com.openai' must be a reverse-domain namespace with object value`. With `com.example.product`, it exits `0`. | Confirmed false rejection. `NAMESPACE` uses `{2,}` after the first label, requiring three labels. The value in the failing case is an object. |
| N-02 | A top-level `com.openai` symlink to an external directory exits `0`; the same symlink named `com.example.product` exits `1` with `extension-containment`. | Confirmed directory-scan gap. `child.name.count('.') >= 2` excludes valid two-label extension directories before their resolved path is checked. The scanner does not open or execute that target, but the result falsely certifies the package. |
| N-03 | `com..openai` with an object value exits `1`; `com.openai` with an array value exits `1`. | Existing negative behavior is present. Separate error messages for namespace and value would make the diagnosis precise. |

All cases used the same canonical `$schema`, valid plugin name, temporary root, and direct CLI. External symlink targets were created outside that root. No client runtime behavior was tested. The submitted report's SHA-256 identifies a different installed validator snapshot; this report's repository baseline is the Git commit above.

## Recommended disposition

Accept two or more nonempty reverse-domain labels in strict creator checks. Keep malformed labels and non-object values as errors with specific diagnostics. Apply the same predicate to manifest names and extension directory candidates, and check resolved containment of recognized two-label directories. Preserve handling of unrelated top-level folders rather than interpreting every dotted directory as an extension. Test both the valid and escaping two-label directory paths alongside existing three-label behavior. Document the creator's naming policy separately from the schema's type constraint.
