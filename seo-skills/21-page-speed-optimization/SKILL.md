---
name: 21-page-speed-optimization
display_name: Page Speed Optimization
description: Diagnose Core Web Vitals and page performance, identify root causes, prioritize safe fixes, gate risky live changes, and verify comparable before/after results.
version: 1.0.0
---
# 1. Purpose
Determine why a page is slow, which bottlenecks matter, what should be fixed first, and whether the page actually improved after changes.

# 2. Trigger
Use for performance audits, CWV baselines, LCP/INP/CLS/TTFB diagnosis, image/JS/CSS/font/cache/third-party audits, optimization plans, pre-change checks, retests and before/after comparisons.

# 3. Do Not Trigger
Do not infer field CWV from Lighthouse score alone. Do not compare unlike test environments. Do not treat missing metrics as zero. Do not execute risky live changes without backup/change plan and approval.

# 4. Inputs
Target URL, field data where available, lab runs, server/network observations, WordPress/theme/plugin context, current cache/CDN setup, test environment, business-critical functionality.

# 5. Preconditions
Establish a baseline and evidence source. If no baseline exists, BLOCK before claiming improvement. Preserve test environment metadata.

# 6. Workflow
BASELINE → FIELD/LAB → CWV → ROOT CAUSE → PRIORITY → BACKUP/CHANGE PLAN → OPTIMIZE → RETEST → BEFORE/AFTER → VERDICT.

Modes: PERFORMANCE_AUDIT, CWV_BASELINE, LCP_DIAGNOSIS, INP_DIAGNOSIS, CLS_DIAGNOSIS, TTFB_DIAGNOSIS, IMAGE_AUDIT, JS_AUDIT, CSS_AUDIT, FONT_AUDIT, CACHE_AUDIT, THIRD_PARTY_AUDIT, OPTIMIZATION_PLAN, PRE_CHANGE_CHECK, POST_CHANGE_RETEST, BEFORE_AFTER_COMPARE, REFRESH, VERIFY, REUSE.

# 7. Tool Routing
USER_DATA, API_DATA and PUBLIC_RESEARCH may be combined. Treat PSI/CrUX field data, Lighthouse/PSI lab data, GTmetrix/WebPageTest and browser/server diagnostics as provider-specific observations.

# 8. Decision Rules
CWV = LCP/INP/CLS. TTFB/FCP/TBT/Speed Index are supporting diagnostics. Root-cause recommendations should connect metric → element/resource → cause → expected effect → risk → priority. Field-data improvement cannot be claimed immediately from lab retest alone.

# 9. Quality Gates
G21: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Use the 24 canonical outputs in references/canonical-outputs.md.

# 11. Handoff
12 handles broader technical SEO issues; 17 may produce optimized replacement images; 07 may implement WordPress page changes; hosting/CDN/plugin changes may require the relevant runtime/operator.

# 12. Safety / Change Control
Potentially breaking changes such as plugin removal, cache-rule changes, JS delay/defer, CSS removal, font changes, CDN rules, DB cleanup, theme/code edits and image replacement require a backup/change plan and explicit approval before live execution.
