---
name: 20-ranking-validation
display_name: Ranking Validation
description: Validate whether an indexed URL has begun earning relevant queries, impressions and rankings, distinguish target/related/wrong-intent visibility, and choose a maturity-aware next action.
version: 1.0.0
---
# 1. Purpose
Answer: has the URL started to rank, is it ranking for the right query space, is visibility growing, and should the team wait or intervene?

# 2. Trigger
Use after index validation for GSC Query×Page analysis, ranking-keyword review, target-query matching, related-query growth, SERP validation, trend diagnosis and next-action selection.

# 3. Do Not Trigger
Do not replace 19 index validation. Do not treat missing data as zero, one impression as established ranking, unrelated queries as target success, or third-party rank positions as GSC average position.

# 4. Inputs
Target URL, index evidence/date, target queries, GSC Query×Page, Semrush/Ahrefs/DataForSEO ranking data, SERP observations, comparable date windows, market/device context.

# 5. Preconditions
Index health must be established or route to 19. Preserve provider semantics and observation windows.

# 6. Workflow
TARGET URL → INDEX EVIDENCE → GSC QUERY×PAGE → RANKING KEYWORDS → TARGET MATCH → RELATED CLUSTERS → SERP INTENT → POSITION/IMPRESSION/QUERY TREND → MATURITY → DIAGNOSIS → VERDICT → NEXT ACTION.

# 7. Tool Routing
USER_DATA, API_DATA and PUBLIC_RESEARCH may be combined. Keep GSC, Semrush, Ahrefs, DataForSEO and live SERP observations separate unless a documented normalization is explicitly appropriate.

# 8. Decision Rules
Growing young pages may be monitored. Persistent wrong-intent/stagnant signals require diagnosis. Ranking decline requires comparable windows. No universal wait period or ranking guarantee.

# 9. Quality Gates
G20: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Use the 22 canonical outputs in references/canonical-outputs.md.

# 11. Handoff
19 for index uncertainty; 25 for ownership/intent; 06 for informational content; 10 for commercial pages; 08 for internal links; 11 for authority/backlinks; 13 for broader analytics.

# 12. Safety / Change Control
20 is diagnostic/read-mostly. It proposes changes; downstream skills own live modifications and their approval gates.
