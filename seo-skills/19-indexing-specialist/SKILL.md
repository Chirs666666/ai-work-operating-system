---
name: 19-indexing-specialist
display_name: Indexing Specialist
description: Validate post-publish discovery, crawl, index/canonical status, query appearance, target-query match and ranking signals without confusing missing data with zero or auxiliary SERP checks with authoritative inspection.
version: 1.0.0
---
# 1. Purpose
Determine where a published URL actually sits in the search lifecycle and route the correct indexing, technical, ownership or content response.

# 2. Trigger
Use for indexing checks, indexability, sitemap/discovery, URL inspection, query/keyword validation, ranking checks, post-publish verification, indexing/ranking diagnosis, refresh, verify or reuse.

# 3. Do Not Trigger
Do not use `site:` alone as definitive index proof. Do not invent impressions/rankings. Do not treat publication, indexing, ranking, impressions and clicks as equivalent states.

# 4. Inputs
URL/page inventory; publication date; target query/page ownership; GSC/URL Inspection/provider exports or APIs; sitemap/robots/canonical/HTTP evidence; market/device/date-range context; configurable project benchmarks.

# 5. Preconditions
Record source/provenance and observation window. Missing GSC/provider data remains UNKNOWN/NO_DATA, not zero.

# 6. Workflow
PUBLISHED → ACCESS → INDEXABILITY → DISCOVERY → CRAWL → INDEX/CANONICAL → IMPRESSIONS → QUERIES → TARGET MATCH → RANKING → CLICKS → DIAGNOSIS → HANDOFF → RECHECK.

Modes: INDEX_CHECK, INDEXABILITY_AUDIT, SITEMAP_CHECK, DISCOVERY_CHECK, URL_INSPECTION, QUERY_VALIDATION, KEYWORD_VALIDATION, RANKING_CHECK, POST_PUBLISH_VERIFY, INDEXING_DIAGNOSIS, RANKING_DIAGNOSIS, REFRESH, VERIFY, REUSE.

# 7. Tool Routing
Combine USER_DATA, API_DATA and PUBLIC_RESEARCH as appropriate. Prefer authoritative first-party inspection/performance data for definitive status. Public `site:` checks are auxiliary only.

# 8. Decision Rules
Unexpected NOINDEX/robots block/canonical-to-other cannot be healthy PASS. Query appearance does not equal target-query ranking. Unrelated queries do not satisfy target-query validation. Benchmarks are configurable signals, not guarantees.

# 9. Quality Gates
G19: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Use the 23 canonical outputs in references/canonical-outputs.md.

# 11. Handoff
07 publish; 08 discovery/internal links; 12 technical fixes; 13 site analytics; 25 ownership; 06/10 content/commercial optimization.

# 12. Safety / Change Control
19 is diagnostic/read-mostly. High-impact live fixes such as noindex/canonical/redirect changes are routed to responsible skills and existing approval controls.
