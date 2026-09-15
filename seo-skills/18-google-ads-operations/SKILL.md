---
name: 18-google-ads-operations
display_name: Google Ads Operations
description: Plan, audit, build, validate and optimize industrial B2B Google Search Ads while gating live spend, delivery, targeting and conversion changes behind explicit approval.
version: 1.0.0
---
# 1. Purpose
Operate the Google Search Ads lifecycle from readiness through optimization without silently changing real spend or live campaign state.

# 2. Trigger
Use for account/tracking audits, campaign planning/build drafts, paid-search keyword work, negatives, ad copy/assets, landing-page review, targeting, bidding/budget plans, prelaunch QA, search terms, pacing, performance reviews, optimization and experiments.

# 3. Do Not Trigger
Do not use for SEO keyword ownership, generic page publishing, unsupported advertising claims, or autonomous live-spend changes.

# 4. Inputs
01 company truth; 02 business/conversion context; 03 keyword universe; 25 page ownership; 04 landing-page structure; Google Ads/GA4 exports or API data; public research; approved budgets/markets.

# 5. Preconditions
Define business goal, conversion actions, market, product/service, data provenance, tracking status and landing-page target. Unknown metrics remain null/UNKNOWN.

# 6. Workflow
BUSINESS GOAL → CONVERSIONS → TRACKING → MARKET → INTENT/KEYWORDS → LANDING PAGE → CAMPAIGN/AD GROUPS → MATCH/NEGATIVES → ADS/ASSETS → TARGETING → BID/BUDGET → QA → WAITING_APPROVAL → LAUNCH → SEARCH TERMS/CONVERSIONS → OPTIMIZE.

Modes: ACCOUNT_AUDIT, TRACKING_READINESS, CAMPAIGN_PLANNING, SEARCH_CAMPAIGN_BUILD, KEYWORD_EXPANSION, NEGATIVE_KEYWORD_REVIEW, AD_COPY_BUILD, LANDING_PAGE_REVIEW, PRE_LAUNCH_QA, SEARCH_TERM_REVIEW, BUDGET_PACING, PERFORMANCE_REVIEW, OPTIMIZATION, EXPERIMENT, REFRESH, VERIFY, REUSE.

# 7. Tool Routing
USER_DATA, API_DATA, PUBLIC_RESEARCH may be combined. Provider-specific account mutations happen only through an authorized runtime connector/API and only after required approval.

# 8. Decision Rules
Tracking broken/unverified prevents confident conversion conclusions. Keyword/ad/landing-page mismatch blocks launch. Ad claims require evidence. Missing CPC/CVR/CPA is UNKNOWN, not zero. Negative keywords require intent review.

# 9. Quality Gates
G18: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.
Live launch or material live change enters WAITING_APPROVAL after QA.

# 10. Outputs
Use the 24 canonical outputs in references/canonical-outputs.md.

# 11. Handoff
01/02/03/25/04 feed 18. 13 consumes post-launch performance. Landing-page changes return to 04/05/06/07 as appropriate.

# 12. Safety / Change Control
Explicit approval is required before enabling/pausing campaigns, publishing ads, changing budgets/bids/targeting/conversions, bulk negatives, Auto-Apply or deletion. Drafts and recommendations may auto-continue.
