---
name: 11-backlink-building
display_name: Backlink Building
description: Discover, qualify, prioritize, plan outreach for, and verify B2B backlink opportunities using evidence-backed relevance and risk controls.
version: 1.0.0
---
# 1. Purpose
Build relevant, credible backlink campaigns instead of maximizing raw link count.

# 2. Trigger
Use for campaign planning, competitor backlink opportunity research, prospect discovery/qualification, outreach queues, paid-placement review, or live-link verification.

# 3. Do Not Trigger
Do not use for internal links (08), URL ownership (25), content rewriting (06/10), metadata (09), technical SEO (12), or broad analytics (13).

# 4. Inputs
Use approved target URLs, 01/02/03/25 context, optional competitor backlink exports, public web research, API data, and user-provided prospect/contact data. Missing metrics are UNKNOWN/null, never zero.

# 5. Preconditions
Confirm target-page ownership and readiness before outreach. Confirm public/authorized source for contact data. Requalify competitor-link prospects.

# 6. Workflow
CAMPAIGN GOAL → TARGET READINESS → DISCOVERY → PROSPECT QUALIFICATION → OPPORTUNITY TYPE → ANCHOR/TARGET PLAN → CONTACT PATH → OUTREACH STRATEGY/DRAFT → RISK/PAID REVIEW → OUTREACH QUEUE → LIVE LINK VERIFY → CAMPAIGN LEARNING.
Modes: PLAN_CAMPAIGN, DISCOVER_PROSPECTS, QUALIFY_PROSPECTS, BUILD_OUTREACH_QUEUE, VERIFY_LINKS, AUDIT_CAMPAIGN.

# 7. Tool Routing
USER_DATA, API_DATA, PUBLIC_RESEARCH. Route by capability; never hard-code credentials.

# 8. Decision Rules
Prospect outcomes: QUALIFIED_HIGH, QUALIFIED_MEDIUM, QUALIFIED_LOW, HOLD, REJECT. Campaign priorities: PRIORITY_HIGH, PRIORITY_MEDIUM, PRIORITY_LOW, HOLD, REJECT. Paid placement requires approval. High-risk link schemes are rejected.

# 9. Quality Gates
G11: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Use the 21 canonical outputs in `references/canonical-outputs.md`.

# 11. Handoff
Page readiness problems return to 06/10/12/25 as appropriate. 13 analyzes broader performance. Outreach sending/submission requires an authorized execution channel and applicable approval.

# 12. Safety / Change Control
Never fabricate metrics, contact details, prices, relationships, or live-link status. Never automate spam, PBN/link-farm participation, mass profile blasts, or forced exact-match anchors. Paid backlinks require explicit approval.
