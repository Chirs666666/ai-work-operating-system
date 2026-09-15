---
name: WB08-deployment-launch
display_name: WB08 Deployment & Launch
version: 1.0.0
description: Approval-controlled production deployment, rollback, smoke test and launch verification.
---

# 1. Purpose
Move a WB07-ready release into production safely and verify launch before indexing handoff.

# 2. Trigger
Use for FULL_SITE, INCREMENTAL, PAGE_ONLY, CONFIG_ONLY, DNS_CUTOVER, MIGRATION or HOTFIX production deployment.

# 3. Do Not Trigger
Do not infer launch approval, replace WB07 QA, claim indexing/ranking, or expand approved scope.

# 4. Inputs
WB07 launch gate, deployment scope/manifest, strategy, snapshot/rollback plan, production approval, execution and verification evidence.

# 5. Preconditions
WB07 must be ready. Production actions need explicit approval. High-risk changes need snapshot and rollback readiness.

# 6. Workflow
WB07 → SCOPE → MANIFEST → PRECHECK → SNAPSHOT → ROLLBACK → APPROVAL → DEPLOY → SMOKE → PRODUCTION VERIFY → LAUNCH VERIFIED → 19.

# 7. Tool Routing
Return QA defects to WB07/responsible skill; infrastructure faults to WB06; technical SEO to 12; tracking to WB05; indexing to 19; ranking to 20.

# 8. Decision Rules
DEPLOYED is not VERIFIED. Critical smoke failure blocks/rolls back. ROLLBACK_EXECUTED is not ROLLBACK_VERIFIED. Submission is not indexing.

# 9. Quality Gates
PASS, WARN, FAIL, BLOCK, WAITING_APPROVAL, ROLLBACK_REQUIRED.

# 10. Outputs
Deployment scope/manifest, approvals, snapshot/rollback, execution, smoke/production verification, incidents, launch gate and indexing handoff.

# 11. Handoff
Only LAUNCH_VERIFIED production context passes to Skill 19.

# 12. Safety / Change Control
Never execute or mark production deployment approved without explicit approval evidence tied to scope.
