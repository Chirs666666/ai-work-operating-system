---
name: 08-internal-linking-architecture
display_name: 08 Internal Linking Architecture & Optimization
description: Build or reuse an evidence-backed internal-link graph, decide incoming/outgoing links, anchors and placements, and hand approved decisions to WordPress execution without directly modifying WordPress.
version: 1.0.0
---

# 1. Purpose
08 is the **Internal Link Decision Owner**. It determines which pages should link, why, with what anchor and placement, using URL ownership, page relationships, commercial priority, current internal-link structure and user journey. It does not directly modify WordPress.

# 2. Trigger
Use for `NEW_PAGE_LINKING`, `EXISTING_SITE_OPTIMIZATION`, `VERIFY`, `REFRESH_GRAPH`, or `REUSE` when planning, auditing, validating, refreshing or reusing internal-link decisions.

# 3. Do Not Trigger
Do not use 08 to research keywords (03), assign URL ownership (25), write articles (06), rewrite commercial pages (10), build/publish WordPress pages (07), fix broken-link technical faults (12), create metadata (09), build backlinks (11), or validate indexing/rankings (19).

# 4. Inputs
Typical inputs include 25 URL ownership, 02 commercial priority, 04/05/06/10 content artifacts, 15 site inventory, current sitemap/crawl/WordPress state, GSC/GA4 and optional SEO-provider exports. Accept `USER_DATA`, `API_DATA`, and `PUBLIC_RESEARCH`. Missing signals remain `UNKNOWN`, never numeric zero.

# 5. Preconditions
Resolve source/target identity, current page content, URL ownership where relevant, and an inventory/graph sufficient for the requested scope. Missing optional performance data degrades to `WARN`; missing critical ownership/inventory/content needed for a reliable decision yields `BLOCK`.

# 6. Workflow
```text
INPUT
↓
Load / Build / Refresh Internal Link Graph
↓
Merge 25 URL Ownership
↓
Page Relationship Model
↓
Candidate Generation
↓
Existing Link Awareness
↓
7-Dimension Evaluation
↓
Priority + Anchor + Placement
↓
Incoming + Outgoing Plan
↓
Change Control
↓
G08
↓
07 Execution Handoff
```
For new pages, plans may be `PRELIMINARY` until final copy exists, then `FINAL`.

# 7. Tool Routing
Route by capability, not vendor: `website_crawl`, `sitemap_read`, `wordpress_read`, `search_console`, `web_analytics`, `backlink_data`, `keyword_metrics`, `public_page_research`. Public research may establish page content/link structure but must not invent private performance metrics.

# 8. Decision Rules
Balance Crawl/Discovery, Topic/Semantic Relationship, Authority Flow, and User Journey/Conversion. Never recommend a link solely to pass authority. 25 remains URL ownership authority. Reuse good existing links. Do not impose fixed link density, fixed exact-match anchor ratios, or fabricated 0–100 scores.

# 9. Quality Gates
G08 values: `PASS`, `WARN`, `FAIL`, `BLOCK`, `REUSE`, `WAITING_APPROVAL`.
`PASS` means the decision package is ready, not that WordPress has been modified. `WAITING_APPROVAL` applies to high-impact recommendations such as live `REPLACE`, `REMOVE_RECOMMENDATION`, `BULK`, or `SITEWIDE` changes.

# 10. Outputs
Canonical outputs: `manifest.yaml`, `site-url-inventory.yaml`, `internal-link-graph.yaml`, `graph-freshness.yaml`, `page-relationship-map.yaml`, `existing-link-audit.yaml`, `link-candidates.yaml`, `link-decisions.yaml`, `outgoing-link-plan.yaml`, `incoming-link-opportunities.yaml`, `anchor-placement-plan.yaml`, `topic-cluster-health.yaml`, `orphan-underlinked-report.yaml`, `ownership-conflicts.yaml`, `technical-link-issues.yaml`, `change-control.yaml`, `execution-handoff.yaml`, `closeout.yaml`.

# 11. Handoff
Ownership ambiguity → 25. Technical broken/redirect/crawl repair → 12. Approved link execution → 07. Post-publication index/ranking validation → 19. VERIFY may compare 08 plan with 07 read-back and current crawl state.

# 12. Safety / Change Control
08 must not directly modify WordPress. Preserve existing valuable links unless evidence supports change. `REPLACE`, `REMOVE_RECOMMENDATION`, live bulk/sitewide changes, and global navigation/footer changes require approval. Never fabricate GSC/GA4/traffic/ranking/backlink data; never interpret missing data as zero; never force exact-match anchors; never override 25 URL ownership; never use 404/410 or inappropriate noindex/redirect URLs as normal new SEO targets.
