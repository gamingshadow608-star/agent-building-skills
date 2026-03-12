# Authorization Control Patterns

When to read this: Read this when the API exposes protected resources, role-restricted actions, multi-tenant data, or field-level visibility rules.

## Evaluate Authorization At Three Levels

- Object level:
  - Can this subject access this specific record, document, account, or tenant object?
- Function level:
  - Can this subject invoke this operation, workflow step, export, or admin action?
- Property level:
  - Can this subject read or write this specific field, relation, or nested attribute?

## Policy Evaluation Order

Use a stable order so the implementation is reviewable:

1. Resolve the authenticated subject and tenant context.
2. Resolve the target resource and its ownership or tenancy.
3. Evaluate the requested action against role, scope, and workflow state.
4. Filter readable fields and writable fields separately.
5. Deny by default when any required fact is missing.

## Multi-Tenant And Ownership Rules

- Bind the tenant context from trusted server-side state, not from a client-supplied tenant ID alone.
- Check both tenant membership and resource ownership when both rules apply.
- Use explicit cross-tenant exceptions for support, admin, or automation roles.
- Treat search, export, and bulk-update endpoints as high-risk because one query can cross many records.

## Batch And Async Pitfalls

- Batch reads:
  - Authorize every returned object, not just the query entry point.
- Batch writes:
  - Authorize every target and define partial-failure behavior explicitly.
- Async jobs:
  - Persist the initiating subject and tenant context so later workers cannot drift into broader access.
- Derived fields and joins:
  - Re-check field visibility after joins, expansions, and nested loads.

## Permission Matrix Guidance

Use `assets/templates/authorization-matrix.csv` when:

- more than one role or subject class exists
- tenant and ownership rules differ by action
- admin or support break-glass paths exist
- field-level exceptions are easy to miss in prose

Recommended matrix columns:

- subject
- resource
- action
- effect
- ownership scope
- tenant scope
- conditions
- notes

## Authorization Review Prompts

- What server-side fact proves the tenant or owner relationship?
- What happens when the resource is missing, archived, locked, or in a restricted workflow state?
- Which fields must be hidden even when the object itself is readable?
- Which bulk or export paths bypass the same checks as single-object reads?

## Minimal Pseudocode Pattern

```text
subject = authenticate(request)
resource = load_target(request)
decision = policy(subject, resource, action)
if decision is deny:
  return forbidden
response = shape_response(resource, decision.visible_fields)
```

## Common Failure Modes

- Authorization is performed only in controllers, while background jobs or secondary fetches skip the same policy.
- Ownership is inferred from a client-sent identifier instead of the loaded resource.
- Read access is checked, but field filtering is forgotten for nested or related data.
- Admin or support overrides exist but are not logged, gated, or narrowly scoped.
