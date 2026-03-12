#!/usr/bin/env python3
"""Render an authorization matrix from JSON or YAML rules."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from io import StringIO
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None


SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = SCRIPT_DIR.parent / "assets" / "templates" / "authorization-matrix.csv"
REQUIRED_FIELDS = ("subject", "resource", "action")
DEFAULT_FIELDS = (
    "effect",
    "ownership_scope",
    "tenant_scope",
    "conditions",
    "notes",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a CSV or markdown authorization matrix from JSON or YAML rules."
    )
    parser.add_argument(
        "input_path",
        help="Path to a JSON or YAML file. Use '-' to read from stdin.",
    )
    parser.add_argument(
        "--format",
        choices=["csv", "markdown"],
        default="csv",
        help="Output format. Defaults to csv.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write the rendered matrix. Defaults to stdout.",
    )
    return parser.parse_args()


def read_input(path_arg: str) -> tuple[str, str]:
    if path_arg == "-":
        return sys.stdin.read(), ""
    path = Path(path_arg)
    return path.read_text(encoding="utf-8"), path.suffix.lower()


def parse_rules(raw_text: str, suffix: str, header: list[str]) -> list[dict[str, str]]:
    data = None
    if suffix == ".json":
        data = json.loads(raw_text)
    elif suffix in {".yaml", ".yml"}:
        data = parse_yaml(raw_text)
    else:
        try:
            data = json.loads(raw_text)
        except json.JSONDecodeError:
            data = parse_yaml(raw_text)
    if isinstance(data, dict):
        rules = data.get("rules")
    else:
        rules = data
    if not isinstance(rules, list):
        raise ValueError("Input must be a list of rules or a mapping with a 'rules' list.")
    normalized: list[dict[str, str]] = []
    for index, rule in enumerate(rules, start=1):
        if not isinstance(rule, dict):
            raise ValueError(f"Rule {index} must be an object.")
        row = {field: "" for field in header}
        for field in REQUIRED_FIELDS:
            value = rule.get(field)
            if value in (None, ""):
                raise ValueError(f"Rule {index} is missing required field '{field}'.")
            row[field] = stringify(value)
        for field in DEFAULT_FIELDS:
            row[field] = stringify(rule.get(field, ""))
        normalized.append(row)
    return normalized


def parse_yaml(raw_text: str):
    if yaml is None:
        raise ValueError("YAML input requires PyYAML to be installed.")
    return yaml.safe_load(raw_text)


def stringify(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return str(value)


def load_header() -> list[str]:
    with TEMPLATE_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        header = next(reader)
    return header


def render_csv(rows: list[dict[str, str]], header: list[str]) -> str:
    buffer = StringIO()
    writer = csv.DictWriter(buffer, fieldnames=header, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def render_markdown(rows: list[dict[str, str]], header: list[str]) -> str:
    separator = "| " + " | ".join("---" for _ in header) + " |"
    lines = [
        "| " + " | ".join(header) + " |",
        separator,
    ]
    for row in rows:
        lines.append("| " + " | ".join(row[column] for column in header) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    raw_text, suffix = read_input(args.input_path)
    header = load_header()
    rows = parse_rules(raw_text, suffix, header)
    rendered = render_csv(rows, header) if args.format == "csv" else render_markdown(rows, header)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
