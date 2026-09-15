---
name: WB05-tracking-search-setup
display_name: WB05 Tracking & Search Setup
version: 1.0.0
description: Configure and verify analytics, conversions and search-platform connections without confusing installation with verification or submission with indexing.
---

# 1. Purpose
Prepare and verify measurement/search setup for pre-launch and launch handoffs.

# 2. Trigger
Use for GA4, GTM, event/conversion tracking, GSC, Bing Webmaster, IndexNow, tracking audits, refresh, VERIFY or REUSE.

# 3. Do Not Trigger
Do not use to decide technical indexability (12), actual indexing state (19), ranking performance (20), or to silently execute production changes.

# 4. Inputs
Site/environment, business conversions, existing tag/plugin inventory, GA4/GTM identifiers, GSC/Bing/IndexNow facts, sitemap reference, privacy requirements and approval evidence.

# 5. Preconditions
Facts not evidenced remain UNKNOWN. Never invent IDs, verification states, event receipt or search acceptance.

# 6. Workflow
ENVIRONMENT → REQUIREMENTS → OWNERSHIP → GA4 → GTM → EVENTS → CONVERSIONS → DETECTION → FIRING → DATA RECEIPT → GSC → SITEMAP → BING → INDEXNOW → SEARCH VERIFY → CONFLICT → PII → PRE-LAUNCH GATE → HANDOFF

# 7. Tool Routing
12 owns robots/canonical/technical sitemap correctness; 19 owns actual indexing; 20 owns ranking. WB07 consumes pre-launch verification. WB08 consumes launch-safe configuration.

# 8. Decision Rules
INSTALLED != VERIFIED. FIRING != RECEIVING_DATA. SUBMITTED != INDEXED. One primary owner per tracking capability. Raw PII is prohibited in analytics parameters.

# 9. Quality Gates
PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Canonical tracking/search registers, verification evidence, conflicts, privacy checks, approvals, handoffs and closeout.

# 11. Handoff
WB07 receives readiness; WB08 receives launch actions; 19 receives verified search-property/sitemap context; 20 later validates ranking.

# 12. Safety / Change Control
Production tracking/search configuration changes require explicit approval. Planning/configuration records never imply authorization.
