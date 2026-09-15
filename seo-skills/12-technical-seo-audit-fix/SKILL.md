---
name: 12-technical-seo-audit-fix
display_name: Technical SEO Audit & Fix
description: Audit, diagnose, prioritize, remediate, and verify technical SEO issues including broken links, redirects, canonicals, robots/indexability, sitemaps, crawlability, hreflang, and structured-data implementation errors.
version: 1.0.0
---
# 1. Purpose
Own technical SEO diagnosis and remediation decisions for crawlability, indexability controls, URL behavior, broken links, canonicalization, redirects, sitemaps, hreflang, and related technical signals.

# 2. Trigger
Use for full technical audits, targeted issue diagnosis, broken-link audits, remediation planning, authorized safe fixes, and post-fix verification.

# 3. Do Not Trigger
Do not use for page speed/CWV optimization (21), keyword-to-URL ownership decisions (25), semantic internal-link architecture (08), metadata decisions (09), content optimization (06/10), or post-fix ranking/index lifecycle analysis (19).

# 4. Inputs
Use USER_DATA, API_DATA, and PUBLIC_RESEARCH from crawler exports, GSC, sitemap/robots/header reads, CMS/SEO plugin read-back, server/CDN rules when authorized, and public URL fetches. Missing values are UNKNOWN/null, never zero.

# 5. Preconditions
Identify target scope, intended indexability, URL ownership where relevant, current technical state, and available execution permissions before remediation.

# 6. Workflow
DISCOVER → CLASSIFY → ROOT CAUSE → PRIORITIZE → REMEDIATION PLAN → CHANGE CONTROL → SAFE FIX / APPROVAL QUEUE → EXECUTION → READ-BACK / RECRAWL → VERIFY.
Modes: FULL_AUDIT, TARGETED_AUDIT, BROKEN_LINK_AUDIT, REMEDIATION_PLAN, EXECUTE_SAFE_FIXES, VERIFY_FIXES.

# 7. Tool Routing
Route by capability and authorization. Read `references/tool-routing.md`.

# 8. Decision Rules
Do not redirect every 404. Do not change canonical/redirect/noindex when URL ownership is unresolved. High-impact live fixes require approval. Semantic internal-link opportunities go to 08; speed/CWV goes to 21.

# 9. Quality Gates
G12: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Use the 22 canonical outputs in `references/canonical-outputs.md`.

# 11. Handoff
Ownership conflicts → 25. Internal-link architecture → 08. Page speed → 21. WordPress page-body execution → 07 when appropriate. Post-fix index/ranking lifecycle → 19.

# 12. Safety / Change Control
Never fabricate crawl/status/header/index data, auto-change sitewide robots/noindex/sitemap settings, delete URLs, alter live redirect/server rules without approval, or claim a fix before re-verification.
