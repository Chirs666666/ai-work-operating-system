---
name: 22-semrush-analysis
display_name: Semrush Analysis
description: Analyze Semrush domain, URL, keyword, competitor and backlink evidence and convert it into prioritized SEO opportunities, risks and downstream actions without confusing modeled Semrush metrics with first-party metrics.
version: 1.0.0
---
# 1. Purpose
Convert Semrush observations into actionable SEO diagnosis rather than merely reporting dashboard numbers.

# 2. Trigger
Use for Organic Research, Position Changes, Top Pages, Keyword Gap, Organic Competitors, Backlink Overview/Gap, traffic trends, SERP features and keyword intent from Semrush.

# 3. Do Not Trigger
Do not equate Semrush traffic with GA4 traffic or Semrush position with GSC Average Position. Do not infer Google absence from a missing Semrush keyword. Do not make keyword decisions from KD alone or backlink-quality decisions from Authority Score alone.

# 4. Inputs
Domain/URL/competitors, Semrush database/country, device, date/snapshot, report/export/API evidence and business target.

# 5. Preconditions
Preserve provider/report/database/device/date context. Mark missing metrics UNKNOWN/null rather than zero.

# 6. Workflow
SCOPE → SNAPSHOT → KEYWORDS → POSITION CHANGES → PAGES → COMPETITORS/GAPS → BACKLINK SIGNALS → TRENDS → OPPORTUNITIES/RISKS → PRIORITY → HANDOFF.

# 7. Tool Routing
Semrush is the primary evidence provider. 13-site-data-analysis is used when first-party or multi-provider confirmation is needed.

# 8. Decision Rules
Comparable trend claims require compatible market/database/device/scope. Estimated traffic is modeled. KD and Authority Score are contextual signals, not standalone decisions.

# 9. Quality Gates
G22: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Use the 24 canonical outputs in references/canonical-outputs.md.

# 11. Handoff
03 keyword research; 06 informational content; 10 commercial pages; 11 backlinks; 13 multi-source analytics; 20 ranking validation; 25 ownership/cannibalization.

# 12. Safety / Change Control
22 is diagnostic/read-mostly. Live content, link, publishing or paid actions are owned by downstream skills and their approval gates.
