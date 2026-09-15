# Update Policy

Modes:
- `CREATE`: establish a new truth base.
- `UPDATE`: ingest approved additions/changes.
- `VERIFY`: validate targeted claims.
- `REFRESH`: re-check stale/time-sensitive sources.
- `MERGE`: combine truth bases while preserving provenance/conflicts.
- `AUDIT`: inspect quality/readiness without broad mutation.

Use semantic versions for packaged skill releases; use project-specific `knowledge_version` for truth-base state. For knowledge changes record entity, field, prior value, new value, source, reason, date, and downstream review needs. Never erase historical provenance merely to make the current file look clean.
