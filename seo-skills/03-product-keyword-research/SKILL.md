---
name: product-keyword-research
display_name: 产品关键词研究
description: Discover, validate, classify, cluster and prioritize product-related search terms using company truth, commercial context and sourced search evidence without deciding final page ownership.
version: 1.0.0
---
# 1. Purpose
Turn Skill 01 truth and Skill 02 commercial intelligence into a sourced keyword opportunity set for downstream page mapping.

# 2. Trigger
Use for CREATE, UPDATE, VERIFY, REFRESH or AUDIT of product/application keyword research.

# 3. Do Not Trigger
Do not use to make final Page Type, target URL, new/update/merge, redirect or cannibalization decisions; those belong to Skill 25. Do not use as a backlink, technical SEO or publishing workflow.

# 4. Inputs
Required: relevant Skill 01 product/capability truth and Skill 02 commercial context. Optional: Semrush/Ahrefs/Keyword Planner/GSC exports, spreadsheets, APIs/connectors, SERP research, trends, competitor terminology and prior keyword datasets. Missing metrics remain null/UNKNOWN, never zero.

# 5. Preconditions
Confirm upstream truth is usable for the requested scope. Existing valid research may return REUSE. Factual company conflicts return upstream rather than being repaired here.

# 6. Workflow
1. Define market, language, scope and mode.
2. Load/reuse 01 and 02 context.
3. Acquire evidence via USER_DATA, API_DATA and/or PUBLIC_RESEARCH.
4. Generate seed and candidate keywords with provenance.
5. Collect available metrics and preserve provider context.
6. Classify search intent and buyer/search stage.
7. Evaluate product, capability, ICP and commercial fit.
8. Assign demand validation state.
9. Cluster by semantics, intent, SERP overlap and buyer/product relationship where evidence permits.
10. Prioritize with explainable categorical reasoning.
11. Record conflicts/gaps.
12. Run G03 and hand research to Skill 25.

# 7. Tool Routing
Supported acquisition methods:
- USER_DATA: user files/exports, GSC exports, keyword tools, spreadsheets, sales/search-term lists.
- API_DATA: connected APIs/MCP/plugins/connectors such as keyword, SERP, trend or search-console providers.
- PUBLIC_RESEARCH: public SERPs, autocomplete/PAA/related concepts where accessible, public trends, competitor/product pages and industry terminology.

Request capabilities such as keyword_discovery, keyword_metrics, serp_search, trend_data, search_console, website_research, spreadsheet_read and structured_compare. Never store credentials in the Skill. Provider unavailability should fall back to another permitted method when appropriate.

# 8. Decision Rules
Intent: INFORMATIONAL, COMMERCIAL, TRANSACTIONAL, NAVIGATIONAL, MIXED, UNKNOWN.
Demand: VERIFIED, OBSERVED, UNVERIFIED, CONFLICTING, UNKNOWN.
Qualitative fit: HIGH, MEDIUM, LOW, UNKNOWN.
Priority: HIGH, MEDIUM, LOW, HOLD, VALIDATE.

AI/competitor discovery does not prove demand. CPC does not prove purchase intent. KD may be stored but cannot be the sole difficulty or priority decision. Conflicting provider metrics must remain separately sourced or use an explicitly selected project dataset with rationale. Clusters are research objects, not final URLs.

# 9. Quality Gates
G03 — KEYWORD RESEARCH READINESS GATE:
PASS = sufficient sourced discovery, intent, commercial fit and validation for downstream mapping.
WARN = useful research with non-critical missing metrics/validation.
FAIL = fabricated/invalid metrics, provenance failure or contradictory malformed outputs.
BLOCK = critical upstream context/evidence is missing.
REUSE = existing valid research satisfies the task.

# 10. Outputs
Write keyword-research/manifest.yaml, seed-keywords.yaml, keyword-master.yaml, keyword-metrics.yaml, search-intent.yaml, keyword-clusters.yaml, commercial-fit.yaml, keyword-priority.yaml, source-conflicts.yaml, research-gaps.yaml and closeout.yaml.

# 11. Handoff
Skill 25 consumes keywords/clusters and decides Page Type, target URL, action and cannibalization. Skills 04/05/06 should consume research after ownership is resolved when page-specific execution is required.

# 12. Safety / Change Control
Never fabricate Search Volume, CPC, KD, trend, ranking, traffic or SERP observations. Preserve provider/market/language/date context when known. Missing values are null/UNKNOWN, not zero. Do not claim demand merely because AI generated a term or a competitor used it. Do not create final page ownership decisions here.
