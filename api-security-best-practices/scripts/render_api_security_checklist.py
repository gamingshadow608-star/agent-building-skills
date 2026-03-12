#!/usr/bin/env python3
"""Render a scoped API security checklist."""

from __future__ import annotations

import argparse
from pathlib import Path


REFERENCE_PATHS = {
    "triage": "references/api-surface-triage.md",
    "auth": "references/authentication-and-session-controls.md",
    "authz": "references/authorization-control-patterns.md",
    "validation": "references/validation-and-data-handling.md",
    "abuse": "references/abuse-and-resource-controls.md",
    "protocol": "references/protocol-hardening.md",
    "owasp": "references/owasp-api-top-10-control-map.md",
}

TEMPLATE_PATHS = {
    "profile": "assets/templates/endpoint-security-profile.md",
    "authz_matrix": "assets/templates/authorization-matrix.csv",
    "error_contract": "assets/templates/error-response-contract.json",
    "abuse_matrix": "assets/templates/abuse-controls-matrix.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a scoped API security checklist for one API surface."
    )
    parser.add_argument(
        "--surface",
        required=True,
        help="Surface classification such as public, partner, internal, or admin.",
    )
    parser.add_argument(
        "--protocol",
        required=True,
        choices=["rest", "graphql", "websocket", "webhook"],
        help="Protocol used by the surface.",
    )
    parser.add_argument(
        "--auth",
        required=True,
        choices=[
            "none",
            "session-cookies",
            "bearer-tokens",
            "oauth-oidc",
            "api-keys",
            "mtls",
            "mixed",
        ],
        help="Primary authentication pattern.",
    )
    parser.add_argument(
        "--multi-tenant",
        action="store_true",
        help="Set when the surface crosses tenant boundaries or requires tenant isolation.",
    )
    parser.add_argument(
        "--handles-sensitive-data",
        action="store_true",
        help="Set when requests or responses contain secrets, PII, financial, health, or regulated data.",
    )
    parser.add_argument(
        "--supports-upload",
        action="store_true",
        help="Set when the surface accepts file uploads or binary payloads.",
    )
    parser.add_argument(
        "--supports-webhooks",
        action="store_true",
        help="Set when the system also receives provider callbacks or webhook deliveries.",
    )
    parser.add_argument(
        "--output",
        help="Optional path to write the generated markdown. Defaults to stdout.",
    )
    return parser.parse_args()


def build_references(args: argparse.Namespace) -> list[str]:
    refs = [REFERENCE_PATHS["triage"], REFERENCE_PATHS["validation"], REFERENCE_PATHS["abuse"]]
    if args.auth != "none":
        refs.append(REFERENCE_PATHS["auth"])
        refs.append(REFERENCE_PATHS["authz"])
    if args.multi_tenant:
        refs.append(REFERENCE_PATHS["authz"])
    if args.protocol in {"rest", "graphql", "websocket", "webhook"} or args.supports_webhooks:
        refs.append(REFERENCE_PATHS["protocol"])
    refs.append(REFERENCE_PATHS["owasp"])
    return dedupe(refs)


def build_checklist(args: argparse.Namespace) -> list[str]:
    items = [
        f"Capture the surface in `{TEMPLATE_PATHS['profile']}`.",
        "Record exposure, caller type, protocol, operation shape, and sensitive-data assumptions.",
        f"Read `{REFERENCE_PATHS['validation']}` and reject unknown, oversized, or malformed input early.",
        f"Read `{REFERENCE_PATHS['abuse']}` and set rate, size, pagination, concurrency, and timeout bounds.",
        f"Read `{REFERENCE_PATHS['protocol']}` and apply the {args.protocol} section.",
        f"Use `{TEMPLATE_PATHS['error_contract']}` for the public error envelope.",
    ]
    if args.auth != "none":
        items.extend(
            [
                f"Read `{REFERENCE_PATHS['auth']}` and bind subject, audience, scope, expiry, rotation, and revocation.",
                f"Read `{REFERENCE_PATHS['authz']}` and enforce object, function, and property-level authorization.",
            ]
        )
    if args.multi_tenant:
        items.extend(
            [
                "Bind tenant context from trusted server-side state.",
                f"Generate or fill `{TEMPLATE_PATHS['authz_matrix']}` for tenant and ownership rules.",
            ]
        )
    if args.handles_sensitive_data:
        items.extend(
            [
                "Minimize response fields and keep internal identifiers or backend details out of error bodies.",
                "Review logging and audit requirements with `$observability-and-audit` before shipping the change.",
            ]
        )
    if args.supports_upload:
        items.extend(
            [
                "Validate file type, detected content, size, filename handling, and storage location separately.",
                "Quarantine or scan uploads before later processing if the system consumes them asynchronously.",
            ]
        )
    if args.supports_webhooks or args.protocol == "webhook":
        items.extend(
            [
                "Verify webhook signatures over the raw request body before parsing business fields.",
                "Enforce timestamp tolerance and store replay identifiers for the full replay window.",
            ]
        )
    if args.protocol == "graphql":
        items.extend(
            [
                "Set field-level authorization and enforce depth or complexity controls.",
                "Decide whether persisted queries or operation allowlists are required for public access.",
            ]
        )
    if args.protocol == "websocket":
        items.extend(
            [
                "Authenticate at connect time and authorize channel joins and sensitive message types.",
                "Rate-limit messages per connection and subject, then define disconnect behavior on abuse.",
            ]
        )
    if args.protocol == "rest":
        items.extend(
            [
                "Align methods, idempotency expectations, CORS, and cache behavior with actual side effects.",
                "Apply the same authorization and response shaping rules to list, export, and nested-resource routes.",
            ]
        )
    items.extend(
        [
            f"Use `{TEMPLATE_PATHS['abuse_matrix']}` when limits differ by endpoint class.",
            f"Cross-check coverage with `{REFERENCE_PATHS['owasp']}`.",
            "Invoke `$tool-design` if the API contract itself is new or changing.",
            "Invoke `$security-threat-model` for threat modeling or security-only review.",
            "Invoke `$testing-and-evals` after implementation to verify auth, validation, replay, and abuse controls.",
        ]
    )
    return dedupe(items)


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def render_markdown(args: argparse.Namespace) -> str:
    references = build_references(args)
    checklist = build_checklist(args)
    flags = {
        "multi_tenant": "yes" if args.multi_tenant else "no",
        "handles_sensitive_data": "yes" if args.handles_sensitive_data else "no",
        "supports_upload": "yes" if args.supports_upload else "no",
        "supports_webhooks": "yes" if args.supports_webhooks else "no",
    }
    lines = [
        "# API Security Checklist",
        "",
        "## Context",
        "",
        f"- surface: `{args.surface}`",
        f"- protocol: `{args.protocol}`",
        f"- auth: `{args.auth}`",
    ]
    lines.extend(f"- {name}: `{value}`" for name, value in flags.items())
    lines.extend(
        [
            "",
            "## Load These References",
            "",
        ]
    )
    lines.extend(f"- `{reference}`" for reference in references)
    lines.extend(
        [
            "",
            "## Implementation Checklist",
            "",
        ]
    )
    lines.extend(f"- [ ] {item}" for item in checklist)
    lines.extend(
        [
            "",
            "## Artifact Targets",
            "",
            f"- `{TEMPLATE_PATHS['profile']}`",
            f"- `{TEMPLATE_PATHS['error_contract']}`",
            f"- `{TEMPLATE_PATHS['abuse_matrix']}`",
        ]
    )
    if args.auth != "none" or args.multi_tenant:
        lines.append(f"- `{TEMPLATE_PATHS['authz_matrix']}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    output = render_markdown(args)
    if args.output:
        path = Path(args.output)
        path.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
