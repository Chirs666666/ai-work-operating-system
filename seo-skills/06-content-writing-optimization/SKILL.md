---
name: 06-content-writing-optimization
display_name: Content Writing & Optimization
description: Research-first informational content lifecycle for CREATE, UPDATE, REFRESH, and REWRITE.
version: 1.0.0
---

# 1. Purpose
Create and improve informational B2B content through evidence-aware research, strategy, writing, and QA. Scope: BLOG, GUIDE, HOW_TO, TECHNICAL_ARTICLE, COMPARISON_ARTICLE, INFORMATIONAL_FAQ_CONTENT.

# 2. Trigger
Use for new informational articles and for diagnosis-led updates, refreshes, or rewrites of existing informational content.

# 3. Do Not Trigger
Do not use for PRODUCT copy (05), commercial-page optimization (10), metadata (09), technical SEO (12), page speed (21), URL ownership/cannibalization decisions (25), internal-link execution (08), or GEO validation (24).

# 4. Inputs
Target topic/keywords, market/language, 03 keyword research and 25 ownership when available, 01 company truth for company claims, 02 buyer context, and the current article for existing-content modes. GSC/analytics/ranking evidence is preferred for existing content when available.

# 5. Preconditions
Confirm informational scope and mode. Preserve provenance using USER_DATA, API_DATA, or PUBLIC_RESEARCH. Missing data stays UNKNOWN/NOT_PROVIDED. Never treat unavailable metrics as zero.

# 6. Workflow
Shared Content Core:
Search Intent → SERP Baseline → User Questions → Content Gap → Evidence → Information Gain → Buyer Decision Value → Content Strategy → Outline → Article → QA → G06.

CREATE enters the shared core after topic/ownership validation.
UPDATE/REFRESH/REWRITE first run Existing Article + Performance → Content Diagnosis → Preserve What Works → Determine Change Depth, then enter the shared core.

UPDATE = localized changes. REFRESH = systematic improvement while intent remains valid. REWRITE = major body restructuring for confirmed intent. REWRITE never authorizes URL ownership changes.

# 7. Tool Routing
Route by capability, not vendor: keyword_dataset_read, serp_search, website_research, source_read, search_console, web_analytics, backlink_data, trend_data, company_truth_read, business_context_read, page_ownership_read, existing_content_read, structured_compare, language_quality_check.
Providers may include uploaded data, public research, GSC, GA4, DataForSEO, Semrush, Ahrefs, Firecrawl, APIs, MCP, plugins, or equivalent sources.

# 8. Decision Rules
Keep Company Claims and Topic Knowledge in separate evidence channels. Track material claims, not every sentence. Competitor content informs SERP coverage but is never company proof or a copying template. Information Gain is required where applicable and is not article length. No fixed word count or keyword-density target. Existing-content work must diagnose first and Preserve What Works. REUSE is valid when no justified content change exists.

# 9. Quality Gates
G06 states: PASS, WARN, FAIL, BLOCK, REUSE.
PASS = content-ready for downstream work.
WARN = non-critical documented gaps.
FAIL = content defect requiring revision.
BLOCK = critical evidence/input/ownership decision missing.
REUSE = existing content remains adequate; no justified edit.
G06 never means indexed, ranking, traffic-producing, or GEO-visible.

# 10. Outputs
manifest.yaml, search-intent.yaml, serp-research.yaml, source-register.yaml, claim-register.yaml, content-diagnosis.yaml, content-gap.yaml, information-gain.yaml, content-strategy.yaml, outline.yaml, article.yaml, article.md, keyword-usage.yaml, internal-link-opportunities.yaml, qa-report.yaml, change-log.yaml, closeout.yaml.

# 11. Handoff
08 internal-link execution; 09 metadata; 07 WordPress construction/upload; 24 GEO audit; 19 index/ranking validation; 13 performance analysis. Return company evidence issues to 01, keyword issues to 03, ownership/cannibalization to 25, commercial pages to 10, technical SEO to 12, performance/CWV to 21.

# 12. Safety / Change Control
Never fabricate metrics, standards, formulas, technical facts, company capabilities, certifications, customers, or outcomes. Never copy competitor text or silently resolve evidence conflicts. Do not change URL ownership, execute redirects/noindex/URL removal, modify live WordPress, publish without downstream approval, buy links, launch paid campaigns, or store secrets.
