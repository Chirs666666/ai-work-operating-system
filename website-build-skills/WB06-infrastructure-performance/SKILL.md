---
name: WB06-infrastructure-performance
display_name: WB06 Infrastructure & Performance
version: 1.0.0
description: Plan and verify DNS, TLS, CDN, cache, SMTP, backup, security and performance foundations before launch.
---

# 1. Purpose
Establish an evidence-backed runtime infrastructure baseline for WB07/WB08 and Skill 21.

# 2. Trigger
Use for new-site infrastructure, existing-site audit, rebuild, infrastructure refresh, VERIFY or REUSE.

# 3. Do Not Trigger
Do not replace WB02 WordPress foundation, Skill 12 technical SEO, Skill 21 page-speed diagnosis, or WB08 production deployment.

# 4. Inputs
Environment/hosting facts, DNS, TLS, CDN, cache layers, SMTP, backup/restore, security baseline, runtime/performance configuration, planned production changes and approvals.

# 5. Preconditions
Unknown facts remain UNKNOWN. Never invent DNS, certificate, delivery, backup, restore or performance evidence.

# 6. Workflow
ENVIRONMENT → HOSTING → DNS → TLS → CDN → CACHE → SMTP → BACKUP → SECURITY → PERFORMANCE FOUNDATION → CONFLICTS → CHANGE PLAN → BACKUP/ROLLBACK → APPROVAL → VERIFY → HANDOFF

# 7. Tool Routing
WB02 owns WordPress foundation; 12 owns technical SEO correctness; 21 owns measured performance diagnosis; WB07 consumes readiness; WB08 owns launch/deployment.

# 8. Decision Rules
Configured is not verified. Duplicate page-cache owners require resolution. SMTP delivery requires evidence. Backup readiness includes recovery/restore method. High-risk production changes require backup and rollback readiness.

# 9. Quality Gates
PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Canonical infrastructure registers, change plans, conflicts, approvals, verification and handoffs.

# 11. Handoff
Skill 21 receives performance foundation; WB07 receives infrastructure readiness; WB08 receives approved production change plan.

# 12. Safety / Change Control
Production infrastructure mutations require explicit approval. Secrets are references only and must never be stored in artifacts.
