---
name: WB02-wordpress-foundation-setup
display_name: WB02 WordPress Foundation Setup
description: Plan and validate a safe WordPress foundation before global components and page assembly.
version: 1.0.0
---

# 1. Purpose
Establish a verified WordPress foundation contract for WB03/WB04 without conflating planning with live production changes.

# 2. Trigger
Use for NEW_SITE, EXISTING_SITE, REBUILD, STAGING_SETUP, FOUNDATION_AUDIT, REFRESH, VERIFY, or REUSE.

# 3. Do Not Trigger
Do not use WB02 for page copywriting, detailed page-section design, Header/Footer assembly, full page assembly, DNS cutover, production deployment, or live URL migration.

# 4. Inputs
WB01 site scope and URL architecture, current WordPress/hosting facts, admin/access facts, theme/editor constraints, plugin inventory, staging status, backup state, security/performance requirements, SEO plugin strategy, and user change-control constraints.

# 5. Preconditions
- WB01 architecture should be available for new/rebuild work.
- Existing sites should provide current WordPress/plugin/theme state when possible.
- Risky production changes require explicit approval and an acceptable backup/rollback path.

# 6. Workflow
ENVIRONMENT → ACCESS/RISK → WB01 ALIGNMENT → THEME → EDITOR → DESIGN TOKENS → PERMALINK → PLUGINS → MEDIA → ROLES → STAGING → SECURITY → BACKUP → PERFORMANCE → SEO COMPATIBILITY → CHANGE PLAN → APPROVAL → VERIFY → HANDOFF

# 7. Tool Routing
WB01 owns architecture. 07 may execute WordPress page-building actions. 12 handles technical SEO. 21 handles performance optimization. WB05 owns tracking/search setup. WB06 owns broader infrastructure/performance operations. WB03/WB04 consume the verified foundation.

# 8. Decision Rules
- WB01 URL architecture is the baseline for permalink planning.
- Proposed permalink changes are not authorization to modify live URLs.
- One capability owner should exist for SEO metadata/schema/sitemap control unless coexistence is explicitly supported.
- Duplicate active cache/security layers require compatibility evidence or a conflict.
- Missing environment/access/configuration evidence remains UNKNOWN/null.
- Staging is required for high-risk foundation changes unless an explicit exception is approved.
- Risky production changes require backup/rollback readiness before execution.
- Analysis, recommendation, draft configuration and approval are separate states.

# 9. Quality Gates
PASS: foundation validated and safe for downstream component/page work.
WARN: usable with non-blocking risks documented.
FAIL: invalid or conflicting foundation requires correction.
BLOCK: missing evidence, ownership conflict, unsafe change, or no rollback path prevents safe progression.
REUSE: prior foundation artifacts match scope/freshness/provenance and pass verification.
WAITING_APPROVAL: a live/risky action is ready but requires explicit user approval.

# 10. Outputs
manifest.yaml; wordpress-environment.yaml; access-risk.yaml; theme-strategy.yaml; editor-strategy.yaml; global-design-tokens.yaml; permalink-baseline.yaml; plugin-register.yaml; plugin-conflict-audit.yaml; media-policy.yaml; role-policy.yaml; staging-baseline.yaml; security-baseline.yaml; backup-baseline.yaml; performance-foundation.yaml; seo-compatibility.yaml; foundation-change-plan.yaml; approval-register.yaml; verification-plan.yaml; cross-skill-handoffs.yaml; closeout.yaml.

# 11. Handoff
WB03 consumes editor/theme/design-token/global-component constraints. WB04 consumes page-build constraints. 07 receives implementation actions. 12 receives technical SEO conflicts. 21 receives performance actions. WB05/WB06 receive tracking/infrastructure dependencies.

# 12. Safety / Change Control
Never treat planning as approval. Production plugin/theme/permalink/site-setting/cache/security/role changes require explicit approval. Do not perform risky changes without a backup and rollback plan.
