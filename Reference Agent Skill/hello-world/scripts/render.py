#!/usr/bin/env python3
"""Render deterministic Project Welcome Pack artifacts for the reference skill."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SUPPORTED_AUDIENCES = {"contributor", "user"}
GENERATED_BY = "hello-world"
SCHEMA_VERSION = 1


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Render WELCOME.md and welcome.json from a project input JSON file."
    )
    parser.add_argument("--input", required=True, type=Path, help="Input JSON file.")
    parser.add_argument("--output", required=True, type=Path, help="Output directory.")
    return parser.parse_args(argv)


def load_input(path: Path) -> dict[str, str]:
    """Load and normalize the supported input fields from *path*."""
    try:
        raw: Any = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"cannot read input {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc.msg}") from exc

    if not isinstance(raw, dict):
        raise ValueError("input must be a JSON object")

    result: dict[str, str] = {}
    for field in ("project", "description", "audience"):
        value = raw.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"field {field!r} must be a non-empty string")
        result[field] = value.strip()

    if result["audience"] not in SUPPORTED_AUDIENCES:
        choices = ", ".join(sorted(SUPPORTED_AUDIENCES))
        raise ValueError(f"unsupported audience {result['audience']!r}; expected one of: {choices}")

    return result


def load_template() -> str:
    """Load the shared template relative to this script, independent of the CWD."""
    template_path = Path(__file__).resolve().parents[1] / "assets" / "welcome-template.md"
    try:
        return template_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"cannot read template {template_path}: {exc}") from exc


def audience_section(audience: str) -> tuple[str, str]:
    """Return the audience-specific section name and rendered Markdown."""
    if audience == "contributor":
        name = "First tiny change"
        body = "- Run the test suite and fix one failing or unclear test."
    elif audience == "user":
        name = "Where to get help"
        body = "Check the project documentation for usage help and support options."
    else:  # guarded by load_input; retained as a defensive invariant
        raise ValueError(f"unsupported audience {audience!r}")
    return name, f"## {name}\n\n{body}"


def render(data: dict[str, str], template: str) -> tuple[str, dict[str, object]]:
    """Render Markdown and manifest values from normalized input."""
    final_section_name, final_section = audience_section(data["audience"])
    markdown = template
    markdown = markdown.replace("{{ project }}", data["project"])
    markdown = markdown.replace("{{ description }}", data["description"])
    markdown = markdown.replace("{{ audience_section }}", final_section)
    markdown = markdown.rstrip() + "\n"

    manifest: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "project": data["project"],
        "audience": data["audience"],
        "sections": ["What it does", final_section_name],
        "generated_by": GENERATED_BY,
    }
    return markdown, manifest


def write_outputs(output_dir: Path, markdown: str, manifest: dict[str, object]) -> None:
    """Write deterministic output artifacts to *output_dir*."""
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "WELCOME.md").write_text(markdown, encoding="utf-8", newline="\n")
    manifest_text = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    (output_dir / "welcome.json").write_text(manifest_text, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)
    try:
        data = load_input(args.input)
        template = load_template()
        markdown, manifest = render(data, template)
        write_outputs(args.output, markdown, manifest)
    except (ValueError, OSError) as exc:
        print(f"render: ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"render: OK: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
