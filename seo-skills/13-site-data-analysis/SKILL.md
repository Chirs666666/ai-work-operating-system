---
name: 13-site-data-analysis
display_name: Site Data Analysis
description: Analyze SEO and website performance using GSC, GA4, Semrush, Ahrefs, user data, and API data while preserving source provenance, avoiding false causality, and routing actions to the correct downstream skill.
version: 1.0.0
---
# 1. Purpose
Analyze site/search/landing-page/query/conversion/visibility/backlink data and convert evidence into prioritized actions.

# 2. Trigger
Use for site overview, search performance, landing-page analysis, query-page analysis, period comparison, competitor visibility, campaign review, or anomaly diagnosis.

# 3. Do Not Trigger
Do not use to execute page edits, metadata changes, redirects, publishing, backlink purchases, or tracking configuration changes.

# 4. Inputs
USER_DATA, API_DATA, PUBLIC_RESEARCH from GSC, GA4, Semrush, Ahrefs, DataForSEO, Bing Webmaster Tools, CRM, WordPress analytics, or crawler exports. Missing values remain UNKNOWN/null.

# 5. Preconditions
Record source, date range, timezone, market, device/filter/search type where relevant. Flag stale/conflicting/incompatible data.

# 6. Workflow
DATA QUALITY → NORMALIZE → COMPARE → SEGMENT → DIAGNOSE → VALIDATE → PRIORITIZE → HANDOFF.
Modes: SITE_OVERVIEW, SEARCH_PERFORMANCE, PAGE_PERFORMANCE, QUERY_PAGE_ANALYSIS, PERIOD_COMPARISON, COMPETITOR_VISIBILITY, CAMPAIGN_REVIEW, ANOMALY_DIAGNOSIS.

# 7. Tool Routing
Use provider-agnostic capability routing. Semrush is a provider, not the workflow.

# 8. Decision Rules
Do not silently average conflicting sources or equate third-party traffic estimates with first-party analytics. Label causal confidence. Route wrong-page/cannibalization to 25.

# 9. Quality Gates
G13: PASS, WARN, FAIL, BLOCK, REUSE.

# 10. Outputs
Use the 21 canonical outputs in `references/canonical-outputs.md`.

# 11. Handoff
03 keywords; 06 informational content; 08 internal links; 09 metadata; 10 commercial pages; 11 backlinks; 12 technical SEO; 19 indexing/ranking validation; 21 speed; 24 GEO; 25 ownership/cannibalization.

# 12. Safety / Change Control
Never fabricate metrics, turn missing data into zero, infer causality without evidence, or silently alter tracking/configuration.
