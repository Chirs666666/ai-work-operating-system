---
name: WB01-site-architecture-builder
display_name: WB01 Site Architecture Builder
description: Plan and validate website information architecture, page families, hierarchy, URLs, navigation, taxonomy, and build priority for a new site, rebuild, expansion, or migration plan.
version: 1.0.0
---

# 1. Purpose
Create the site-level structure required before page design and WordPress assembly.

# 2. Trigger
Use for NEW_SITE, REBUILD, EXPANSION, MIGRATION_PLANNING, ARCHITECTURE_AUDIT, REFRESH, VERIFY, or REUSE work.

# 3. Do Not Trigger
Do not use WB01 to research keywords, write copy, build WordPress pages, deploy redirects, change canonical/noindex, or publish navigation changes.

# 4. Inputs
Business/company evidence, site goal, product/service/application/resource entities, target markets, existing URL inventory if any, keyword research, Skill 25 keyword/page ownership outputs, user constraints, and desired build scope.

# 5. Preconditions
- Site/business scope is known enough to distinguish page families.
- If keyword research or ownership evidence exists, preserve its provenance.
- For rebuild/migration planning, load the current live URL inventory before proposing destructive URL changes.

# 6. Workflow
PROJECT CONTEXT → BUSINESS/SITE SCOPE → INPUT ARTIFACT CHECK → PAGE FAMILIES → PAGE INVENTORY → HIERARCHY → URL DESIGN → NAVIGATION → TAXONOMY → OWNERSHIP CHECK → ARCHITECTURE RISKS → BUILD PRIORITY → DOWNSTREAM HANDOFF → VERIFY

# 7. Tool Routing
Use 01 for company facts, 02 for buyer/business logic, 03 for keyword research, 25 for keyword/page ownership, 15 for existing site inventory when rebuilding, 12 for technical migration implications, and downstream WB02–WB04 for implementation.

# 8. Decision Rules
- Keyword ownership from Skill 25 is authoritative input unless a conflict is explicitly raised and returned for resolution.
- A proposed URL is not a live URL change authorization.
- Every planned page requires a page family/type and hierarchy status.
- Primary navigation is a curated user-navigation layer, not a copy of the entire sitemap.
- Duplicate intent pages require explicit differentiation rationale.
- Existing live URL equity must be preserved during rebuild/migration planning.
- Missing evidence remains UNKNOWN/null, never invented.

# 9. Quality Gates
PASS: architecture internally consistent and build-ready.
WARN: architecture usable with documented risks/UNKNOWN items.
FAIL: invalid/contradictory structure requiring correction.
BLOCK: missing upstream ownership/evidence or unresolved live-equity conflict prevents safe architecture.
REUSE: prior architecture matches scope/freshness/provenance and passes validation.
WAITING_APPROVAL: only when a downstream live-change decision is intentionally surfaced.

# 10. Outputs
manifest.yaml; architecture-brief.yaml; source-register.yaml; site-scope.yaml; page-family-register.yaml; page-inventory.yaml; hierarchy-map.yaml; url-architecture.yaml; navigation-map.yaml; taxonomy-map.yaml; entity-page-map.yaml; keyword-page-input-check.yaml; architecture-conflict-register.yaml; missing-page-register.yaml; build-priority.yaml; cross-skill-handoffs.yaml; verification-plan.yaml; closeout.yaml.

# 11. Handoff
04 consumes page-level planning requirements. 08 consumes hierarchy/navigation context. 09 consumes page inventory and proposed URL conventions. WB02 consumes foundation requirements. WB03 consumes global navigation/component requirements. WB04 consumes page inventory/build priority. 12 handles technical migration implications.

# 12. Safety / Change Control
WB01 is planning-only. Never execute or assume approval for live slug/URL changes, redirects, canonical/noindex changes, production navigation edits, deletions, or publishing.
