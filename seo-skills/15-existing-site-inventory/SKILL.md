---
name: 15-existing-site-inventory
display_name: Existing Site Inventory
description: Inventory an existing website, normalize URLs, enrich them with search/analytics/link/content/technical signals, classify asset value and preservation risk, and route optimization actions without executing destructive changes.
version: 1.0.0
---
# 1. Purpose
Create a reliable baseline of what an existing site has, how those assets perform, which URLs must be protected, and what should happen next.

# 2. Trigger
Use for an existing-site SEO baseline, migration/cleanup prep, URL inventory, asset protection, optimization prioritization, or inventory refresh/verification.

# 3. Do Not Trigger
Do not use to execute page rewrites, redirects, noindex, deletion, metadata changes, internal-link placement, or technical fixes.

# 4. Inputs
USER_DATA, API_DATA, PUBLIC_RESEARCH from sitemap, WordPress, crawler, GSC, GA4, Semrush, Ahrefs, DataForSEO, Bing Webmaster Tools, or user exports. Missing values remain UNKNOWN/null.

# 5. Preconditions
Define site scope, environment, canonical host preference if known, data periods, and available source provenance.

# 6. Workflow
DISCOVER → URL NORMALIZE → DATA ENRICHMENT → PAGE CLASSIFICATION → PERFORMANCE BASELINE → ASSET VALUE → ISSUE SIGNALS → ACTION CLASSIFICATION → PRIORITY → HANDOFF.
Modes: FULL_INVENTORY, URL_INVENTORY, PERFORMANCE_ENRICHMENT, ASSET_CLASSIFICATION, ACTION_CLASSIFICATION, REFRESH, VERIFY.

# 7. Tool Routing
Use provider-agnostic routing. First-party and provider-estimated metrics remain distinct.

# 8. Decision Rules
Protect existing ranking/traffic/conversion/backlink value. MERGE/REDIRECT/REASSIGN require 25 ownership validation. REMOVE/NOINDEX are approval-gated. Use HOLD when evidence is weak.

# 9. Quality Gates
G15: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Use the 21 canonical outputs in `references/canonical-outputs.md`.

# 11. Handoff
25 ownership; 10 commercial pages; 06 informational content; 09 metadata; 08 internal linking; 11 backlinks; 12 technical SEO; 13 deeper analytics; 19 index/ranking; 21 speed; 24 GEO; 07 later approved WordPress execution.

# 12. Safety / Change Control
Never fabricate metrics, convert missing data to zero, infer ownership, auto-redirect 404s, or enable destructive/high-impact execution without approval.
