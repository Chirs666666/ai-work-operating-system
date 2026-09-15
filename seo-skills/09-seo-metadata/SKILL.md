---
name: 09-seo-metadata
display_name: SEO Metadata
description: Make evidence-backed SEO Title and Meta Description decisions, audit metadata quality and conflicts, diagnose performance opportunities, and produce controlled execution contracts for Skill 07.
version: 1.0.0
---
# 1. Purpose
Own SEO Title and Meta Description decisions. Prefer correct decisions and preservation over needless rewriting.

# 2. Trigger
Use for metadata generation, page audit, optimization, performance diagnosis, site metadata audit, or post-write verification.

# 3. Do Not Trigger
Do not use for keyword research (03), URL ownership (25), page/H1 content creation (04/05/06/10), WordPress writes (07), schema markup, or index/ranking lifecycle (19).

# 4. Inputs
Consume 25 ownership, current page content/H1, 01 truth, configured metadata, optional GSC performance, and tiered SERP evidence. Data may come from USER_DATA, API_DATA, or PUBLIC_RESEARCH. Missing data is UNKNOWN, never zero.

# 5. Preconditions
Confirm page identity and ownership. For claims, obtain sufficient evidence. For existing pages, read current metadata before recommending change.

# 6. Workflow
INPUT NORMALIZATION → OWNERSHIP + CONTENT CHECK → EXISTING METADATA DIAGNOSIS → SERP RESEARCH POLICY → PERFORMANCE DIAGNOSIS → CLAIM / EVIDENCE CHECK → CANDIDATE GENERATION → CANDIDATE EVALUATION → RECOMMENDED METADATA → H1 ALIGNMENT REVIEW → CHANGE CONTROL → G09 → 07 EXECUTION.
Modes: GENERATE, AUDIT_PAGE, OPTIMIZE, PERFORMANCE_DIAGNOSIS, SITE_AUDIT, VERIFY. REUSE may end work without regeneration.

# 7. Tool Routing
Route by capability, not vendor. Read `references/tool-routing.md`.

# 8. Decision Rules
Actions: KEEP, OPTIMIZE, REWRITE, TEST, REUSE, INSUFFICIENT_DATA, BLOCK_FOR_OWNERSHIP. Generate 2–3 Title+Meta pairs only when justified. Hard reject candidates failing search intent, URL ownership, or accuracy/evidence. Unsupported claims cannot be recommended. Length is a guardrail.

# 9. Quality Gates
G09: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL. PASS means the decision package is ready, not that WordPress changed.

# 10. Outputs
Use the 16 canonical outputs in `references/canonical-outputs.md`.

# 11. Handoff
07 executes plugin-agnostic metadata contracts. Ownership conflicts return to 25. H1 changes return to the relevant content owner. 19 handles post-publication index/ranking lifecycle.

# 12. Safety / Change Control
Never fabricate claims, stuff keywords, treat missing metrics as zero, guarantee Google display, or auto-rewrite stable high-value live metadata. High-impact live changes require approval.
