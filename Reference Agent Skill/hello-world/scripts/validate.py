#!/usr/bin/env python3
"""Validate Project Welcome Pack artifacts produced by the reference skill."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

EXPECTED_KEYS = {"schema_version", "project", "audience", "sections", "generated_by"}
SUPPORTED_AUDIENCES = {"contributor", "user"}
CONTRIBUTOR_SECTION = "First tiny change"
CONTRIBUTOR_TASK = "- Run the test suite and fix one failing or unclear test."
USER_SECTION = "Where to get help"
USER_TEXT = "Check the project documentation for usage help and support options."


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Validate a generated Project Welcome Pack.")
    parser.add_argument("output", type=Path, help="Directory containing WELCOME.md and welcome.json.")
    return parser.parse_args(argv)


def load_artifacts(output_dir: Path) -> tuple[str, dict[str, Any]]:
    """Read the required artifacts from *output_dir*."""
    markdown_path = output_dir / "WELCOME.md"
    manifest_path = output_dir / "welcome.json"
    try:
        markdown = markdown_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"WELCOME.md: cannot read artifact: {exc}") from exc
    try:
        raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"welcome.json: cannot read artifact: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"welcome.json: invalid JSON: {exc.msg}") from exc
    if not isinstance(raw, dict):
        raise ValueError("welcome.json: root value must be an object")
    return markdown, raw


def level_two_sections(markdown: str) -> list[str]:
    """Return level-two Markdown ATX headings in source order."""
    return [line[3:].strip() for line in markdown.splitlines() if line.startswith("## ")]


def section_body(markdown: str, section_name: str) -> str:
    """Return the trimmed body of one level-two section."""
    lines = markdown.splitlines()
    marker = f"## {section_name}"
    try:
        start = lines.index(marker) + 1
    except ValueError as exc:
        raise ValueError(f"WELCOME.md: missing required section {section_name!r}") from exc
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return "\n".join(lines[start:end]).strip()


def validate(markdown: str, manifest: dict[str, Any]) -> None:
    """Validate common and audience-specific artifact invariants."""
    keys = set(manifest)
    if keys != EXPECTED_KEYS:
        missing = sorted(EXPECTED_KEYS - keys)
        extra = sorted(keys - EXPECTED_KEYS)
        details = []
        if missing:
            details.append(f"missing keys: {', '.join(missing)}")
        if extra:
            details.append(f"unexpected keys: {', '.join(extra)}")
        raise ValueError(f"welcome.json: invalid fields ({'; '.join(details)})")

    if manifest["schema_version"] != 1:
        raise ValueError("welcome.json: schema_version must equal 1")
    if manifest["generated_by"] != "hello-world":
        raise ValueError("welcome.json: generated_by must equal 'hello-world'")

    project = manifest["project"]
    audience = manifest["audience"]
    sections = manifest["sections"]
    if not isinstance(project, str) or not project.strip():
        raise ValueError("welcome.json: project must be a non-empty string")
    if audience not in SUPPORTED_AUDIENCES:
        raise ValueError("welcome.json: audience must be 'contributor' or 'user'")
    if not isinstance(sections, list) or not all(isinstance(item, str) for item in sections):
        raise ValueError("welcome.json: sections must be an array of strings")

    first_line = markdown.splitlines()[0] if markdown.splitlines() else ""
    if first_line != f"# Hello, {project}!":
        raise ValueError("WELCOME.md: title does not match welcome.json project")

    actual_sections = level_two_sections(markdown)
    if actual_sections != sections:
        raise ValueError("WELCOME.md/welcome.json: section list or order does not match")
    if not actual_sections or actual_sections[0] != "What it does":
        raise ValueError("WELCOME.md: first level-two section must be 'What it does'")
    if not section_body(markdown, "What it does"):
        raise ValueError("WELCOME.md: 'What it does' section must not be empty")

    if audience == "contributor":
        if actual_sections[-1] != CONTRIBUTOR_SECTION:
            raise ValueError(f"WELCOME.md: final section must be {CONTRIBUTOR_SECTION!r}")
        if USER_SECTION in actual_sections:
            raise ValueError(f"WELCOME.md: contributor output must not contain {USER_SECTION!r}")
        if section_body(markdown, CONTRIBUTOR_SECTION) != CONTRIBUTOR_TASK:
            raise ValueError("WELCOME.md: 'First tiny change' must contain exactly the required single starter task")
    else:
        if actual_sections[-1] != USER_SECTION:
            raise ValueError(f"WELCOME.md: final section must be {USER_SECTION!r}")
        if CONTRIBUTOR_SECTION in actual_sections or CONTRIBUTOR_SECTION in markdown:
            raise ValueError("WELCOME.md: user output must not contain contributor instructions")
        if section_body(markdown, USER_SECTION) != USER_TEXT:
            raise ValueError("WELCOME.md: 'Where to get help' content does not match the user profile")


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(argv)
    try:
        markdown, manifest = load_artifacts(args.output)
        validate(markdown, manifest)
    except ValueError as exc:
        print(f"validate: ERROR: {exc}", file=sys.stderr)
        return 1

    print("validate: OK: WELCOME.md")
    print("validate: OK: welcome.json")
    print(f"validate: OK: audience={manifest['audience']}")
    print("validate: OK: required sections present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
