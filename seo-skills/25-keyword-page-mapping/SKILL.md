---
name: keyword-page-mapping
display_name: 关键词页面类型与归属决策
description: Map validated keyword/topic clusters to page types, primary URLs and safe page actions for new, existing and hybrid sites while controlling cannibalization and destructive changes.
version: 1.0.0
---
# 1. Purpose
Convert Skill 03 keyword clusters into an evidence-backed page ownership contract for NEW_SITE, EXISTING_SITE and HYBRID projects.

# 2. Trigger
Use after keyword research when deciding Page Type, target/planned URL, keyword ownership, existing-page action, split/consolidation or cannibalization risk.

# 3. Do Not Trigger
Do not use for raw keyword discovery, page UI design, copywriting, publishing, redirect execution, deletion or live noindex changes.

# 4. Inputs
Consume Skill 03 clusters, intent, demand and commercial fit. For existing sites, additionally use URL inventory, crawl/sitemap, GSC Query × Page, ranking/performance, backlink/authority and architecture evidence when available. Skill 01/02/15 context may be reused.

# 5. Preconditions
G03 must be usable for the requested scope. Missing evidence remains UNKNOWN/NOT_PROVIDED. Existing valid mapping may return REUSE.

# 6. Workflow
1. Set NEW_SITE, EXISTING_SITE or HYBRID mode.
2. Load clusters and upstream business context.
3. Acquire site/search evidence through USER_DATA, API_DATA and/or PUBLIC_RESEARCH.
4. Confirm dominant cluster intent.
5. Select standard or project-defined Page Type.
6. For existing sites, evaluate candidate URLs and protect established relevant URLs by default.
7. Select one proposed primary URL or planned URL per intent/topic cluster.
8. Assign PRIMARY, SECONDARY and SUPPORTING keyword roles.
9. Evaluate competing URLs and cannibalization using multiple signals.
10. Decide KEEP, UPDATE, REWRITE, CREATE, MERGE, REDIRECT, NOINDEX, REMOVE, REASSIGN or HOLD.
11. Record confidence, conflicts, gaps and change-control state.
12. Run G25 and hand the ownership contract downstream.

# 7. Tool Routing
Use capability routing: keyword_dataset_read, search_console, website_crawl, sitemap_read, serp_search, web_analytics, backlink_data, website_research, structured_compare. Sources may be USER_DATA, API_DATA or PUBLIC_RESEARCH. Never store credentials in this Skill.

# 8. Decision Rules
Default: one Search Intent / Topic Cluster → one Primary URL unless SERP, buyer intent or business evidence supports a split. Standard Page Types: HOME, CATEGORY, PRODUCT, APPLICATION, INDUSTRY, SERVICE, CAPABILITY, BLOG, GUIDE, COMPARISON, FAQ, SUPPORT, CASE_STUDY, CALCULATOR_TOOL, LANDING_PAGE, OTHER; project extensions are allowed.

Protect relevant existing URLs with meaningful rankings, clicks, qualified traffic, backlinks or stable relevance. Do not move them merely for prettier architecture. Cannibalization risk is HIGH, MEDIUM, LOW or UNKNOWN and cannot be inferred from keyword overlap alone. Decision confidence is HIGH, MEDIUM, LOW or UNKNOWN.

# 9. Quality Gates
G25 statuses: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.
PASS = mapping is sufficiently supported for safe downstream work.
WARN = usable with non-critical uncertainty.
FAIL = contradictory ownership, invalid provenance, malformed logic or unsupported destructive decisions.
BLOCK = critical evidence/dependency is missing.
REUSE = existing valid mapping remains applicable.
WAITING_APPROVAL = high-impact recommendation is ready but execution is forbidden pending approval.

# 10. Outputs
Write keyword-page-mapping/manifest.yaml, page-type-registry.yaml, cluster-page-map.yaml, keyword-ownership.yaml, existing-url-candidates.yaml, page-actions.yaml, cannibalization-report.yaml, split-merge-decisions.yaml, change-control.yaml, mapping-conflicts.yaml, mapping-gaps.yaml and closeout.yaml.

# 11. Handoff
CREATE → 04 then relevant content Skill. UPDATE/REWRITE → 10 for commercial pages or 06 for informational content where appropriate. MERGE/REDIRECT/NOINDEX/REMOVE remain WAITING_APPROVAL before any live execution. Downstream Skills inherit approved ownership and must not silently retarget the same cluster.

# 12. Safety / Change Control
Never fabricate rankings, clicks, traffic, backlinks or SERP evidence. Missing performance does not prove no value. Never create one page per keyword mechanically. Never declare cannibalization from lexical overlap alone. MERGE, REDIRECT, NOINDEX, REMOVE and destructive/material live ownership changes are recommendation-only: execution_allowed=false and status=WAITING_APPROVAL until explicit approval.
