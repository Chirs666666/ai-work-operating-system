---
name: 05-product-copywriting
display_name: Product Copywriting
description: Fills a confirmed PRODUCT page blueprint with evidence-aware B2B English copy using claim/evidence controls, buyer-value reasoning, keyword QA, and G05 readiness.
version: 1.0.0
---
# 1. Purpose
Fill confirmed Skill 04 PRODUCT-page content slots with accurate, buyer-oriented, evidence-traceable B2B English copy.

# 2. Trigger
Use only for a confirmed PRODUCT page. Supported modes: DRAFT and PRODUCTION.

# 3. Do Not Trigger
Do not use for CATEGORY, APPLICATION, INDUSTRY, SERVICE, CAPABILITY, LANDING_PAGE, BLOG, GUIDE, or other page types. Do not research page ownership, redesign structure, create metadata/images, or build WordPress.

# 4. Inputs
Read approved product truth/evidence from 01, buyer context from 02, keyword/search language from 03, ownership from 25, and page-contract/section-blueprint/content-requirements/proof-requirements/cta-plan from 04. Data methods: USER_DATA, API_DATA, PUBLIC_RESEARCH. Preserve provenance and conflicts.

# 5. Preconditions
Page type must be PRODUCT and G25/G04 must be usable. Missing critical ownership or Blueprint information returns BLOCK. New facts that conflict with 01 are preserved and routed for verification, not silently substituted.

# 6. Workflow
Validate PRODUCT contract → select DRAFT/PRODUCTION → load 04 slots → gather approved truth/buyer/search context → build feature-value reasoning → draft slot copy → register claims/evidence → keyword/CTA/repetition/style QA → resolve gaps → render YAML + Markdown → run G05.

# 7. Tool Routing
Route by capability: company_truth_read, business_context_read, keyword_dataset_read, page_ownership_read, page_blueprint_read, document_read, website_research, structured_compare, language_quality_check. Providers are replaceable. Missing optional capabilities create explicit gaps.

# 8. Decision Rules
Use FACT → FEATURE → FUNCTION → BUYER REQUIREMENT → BUYER VALUE → CLAIM → EVIDENCE → FINAL COPY.
Claim strengths: C1 VERIFIED_FACT; C2 SUPPORTED_INTERPRETATION; C3 CONDITIONAL_BENEFIT; C4 UNSUPPORTED_MARKETING_CLAIM. C4 is prohibited from publishable PRODUCTION copy. Missing values remain UNKNOWN/NOT_PROVIDED, never zero. Do not optimize to fixed keyword density. 04 owns structure; 05 fills slots only.

# 9. Quality Gates
G05: PASS, WARN, FAIL, BLOCK, REUSE. PASS means PRODUCTION copy is supported and downstream-ready. WARN permits safe continuation with non-critical documented gaps. FAIL means the copy itself is materially defective. BLOCK means critical truth/ownership/Blueprint/evidence prevents safe writing. REUSE means existing copy still satisfies the current Blueprint and evidence state.

# 10. Outputs
manifest.yaml; product-copy.yaml; section-copy.yaml; copy-slots.yaml; claim-register.yaml; feature-value-map.yaml; keyword-usage.yaml; cta-copy.yaml; copy-gaps.yaml; qa-report.yaml; closeout.yaml; product-copy.md.

# 11. Handoff
09 receives confirmed copy/keyword context; 17 receives visual context where needed; 07 receives structured and human-readable PRODUCT copy. Route truth conflicts to 01, business-context problems to 02, search-language problems to 03, ownership problems to 25, structural slot problems to 04.

# 12. Safety / Change Control
Never fabricate specifications, certifications, cases, customer results, ROI, deployment times, defect rates, or proof. Never publish/edit live WordPress, change URL ownership, execute redirects/noindex/removal, modify site configuration, or store secrets.
