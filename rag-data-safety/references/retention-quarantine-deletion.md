# Retention, Quarantine, And Deletion

Use this file when defining lifecycle rules for RAG stores, retrieval caches, or memory.

## Quarantine

- Quarantine every new memory write before reuse.
- Review quarantined entries for provenance, scope, relevance, safety, and retention fit before promotion.
- Do not promote entries that lack provenance or that contain unsafe or irrelevant instructions.

## Retention

- Define a retention window for each store, cache, and memory surface.
- State why the retention window is necessary for that scope.
- Treat missing retention policy as an unresolved safety gap.

## Forget Paths And Deletion

- Define an explicit delete or forget path for every primary store.
- Remove stale, poisoned, unsafe, or incorrectly scoped data from derived or cached surfaces as well as primary storage.
- Record how deletions affect vector indexes, retrieval caches, exports, or any other derived artifacts.
- If no delete path exists, record the gap and stop short of treating the store as safely governed.
