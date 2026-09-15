# Acceptance Matrix

| Requirement | Evidence |
|---|---|
| New page has incoming + outgoing planning | `examples/new-page-final/` |
| Existing good link is reused | `examples/reuse-existing-link/` |
| URL ownership conflict returns to 25 | `examples/ownership-conflict/` |
| Missing GSC degrades to WARN, not BLOCK | `examples/missing-gsc-warning/` |
| Missing performance data is UNKNOWN, not zero | `examples/missing-gsc-warning/site-url-inventory.yaml` + validator |
| Sitemap-only page is orphan | `examples/orphan-sitemap-only/` |
| Breadcrumb-only page is not orphan | `examples/breadcrumb-underlinked/` |
| 404 target is rejected and handed to 12 | `examples/technical-404-handoff/` |
| Live REPLACE requires approval | `examples/live-replace-approval/` + regression test |
| Stale graph cannot blind REUSE | `examples/stale-graph-refresh/` |
| VERIFY mismatch is explicit | `examples/verify-execution-mismatch/` |
| High priority cannot override LOW semantic relevance/placement | `scripts/validate_examples.py` universal invariant |
| No fixed internal-link density | `references/orphan-underlinked-rules.md`, `SKILL.md`, package validator |
| No fixed exact/partial anchor ratio | `references/anchor-strategy.md`, `SKILL.md`, package validator |
| 08 does not directly mutate WordPress | `SKILL.md`, `references/boundaries-and-ownership.md`, package validator |
| 07 is execution owner | `schemas/execution-handoff.schema.json` + examples |
| 12 is technical repair owner | `schemas/technical-link-issues.schema.json` + examples |
| 25 is URL ownership authority | `schemas/ownership-conflicts.schema.json` + examples |
| 18 canonical outputs are defined and template/schema paired | `references/canonical-outputs.md`, `templates/`, `schemas/`, package validator |
