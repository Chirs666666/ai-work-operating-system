---
name: business-model-analysis
display_name: 生意模式分析
description: Convert verified company/product truth and permitted commercial evidence into structured ICP, buyer, buying-journey, pain-value, competitor-positioning, and commercial-priority intelligence for downstream SEO and growth workflows.
version: 1.0.0
---

# 1. Purpose
Build an evidence-aware commercial model from Skill 01 truth plus permitted commercial research. Answer what is sold, to whom, why they buy, who participates, what triggers purchase, which alternatives are considered, what can be differentiated with evidence, and what deserves commercial priority.

# 2. Trigger
Use for CREATE, UPDATE, VERIFY, REFRESH, or AUDIT of business-model intelligence before keyword research, page planning, product copy, GEO, or Google Ads planning.

# 3. Do Not Trigger
Do not use for keyword volume, Keyword Gap, KD, ranking keywords, SERP SEO strength, DR/DA, backlink gap, SEO content gap, technical SEO, final keyword-to-page mapping, final copywriting, or ad launch/spend changes.

# 4. Inputs
Required: a usable `01-company-knowledge-base` truth base or equivalent verified company/product facts.
Optional: sales decks, CRM/ERP exports, quotations, inquiry records, customer interviews, cases, channel information, competitor lists, official competitor sources, industry sources, and structured API data.

Every important input should preserve provenance. Use `UNKNOWN` or `NOT_PROVIDED` when information is absent; never convert missing information to zero.

# 5. Preconditions
Check Skill 01 readiness for the current task. Skill 02 may read company/product truth but must not silently change it. A factual contradiction routes to Skill 01 VERIFY/UPDATE. Existing valid Skill 02 artifacts may return `REUSE`.

# 6. Workflow
1. Define task scope and mode.
2. Check/reuse Skill 01 truth.
3. Acquire required evidence using USER_DATA, API_DATA, and/or PUBLIC_RESEARCH.
4. Build the product/service portfolio.
5. Identify customer segments and ICP fit/disqualifiers.
6. Map buyer roles and buying committee.
7. Map triggers and buying journey.
8. Map pain → requirement → verified capability → buyer value.
9. Analyze commercial competitors and alternatives.
10. Identify evidence-backed differentiation and label inference/hypothesis.
11. Rate commercial priority with explainable dimensions; exclude search volume.
12. Record gaps/conflicts, run G02, and write canonical artifacts.

# 7. Tool Routing
Use three acquisition methods, independently or together:

- `USER_DATA`: user-supplied files, exports, Skill 01 artifacts, sales/CRM materials, cases, quotations, interviews, competitor lists.
- `API_DATA`: connected APIs, MCP tools, plugins, connectors, CRM/ERP or approved data services.
- `PUBLIC_RESEARCH`: public company/competitor websites, brochures, PDFs, associations, standards, technical documents, case studies, integrators/distributors, reputable industry sources.

Request capabilities rather than hard-code vendors. Examples: `document_read`, `website_research`, `business_data`, `crm_read`, `structured_compare`.

For company truth prefer Skill 01 and approved USER_DATA. For competitor facts prefer first-party/primary public sources. API unavailability does not block the Skill when another permitted method can satisfy the need. Never store API keys, passwords, OAuth tokens, or credentials in this package.

# 8. Decision Rules
Classify analytical statements as:
- `FACT`: established by approved truth/evidence.
- `EVIDENCE`: an observed source item supporting analysis.
- `INFERENCE`: reasoned interpretation supported by evidence.
- `HYPOTHESIS`: plausible but unverified; requires validation.
- `UNKNOWN`: not established.

Source methods are `USER_DATA`, `API_DATA`, `PUBLIC_RESEARCH`. When sources disagree, set `SOURCE_CONFLICT`, preserve both observations, explain any selected working value, and mark verification need. Never silently overwrite.

Commercial priority dimensions: Buyer Relevance, Purchase Intent/Buying Urgency, Business Value, Company Capability Fit, Differentiation Strength, Evidence Strength. Rate each `HIGH | MEDIUM | LOW | UNKNOWN`. Overall priority is `HIGH | MEDIUM | LOW | HOLD`, with rationale. Do not fabricate revenue, margin, ROI, market share, deal size, or numeric scoring.

# 9. Quality Gates
Run `G02 — BUSINESS MODEL GATE`.
- `PASS`: sufficient supported commercial context for the requested downstream task.
- `WARN`: usable model, but non-critical assumptions/gaps remain.
- `FAIL`: malformed/contradictory artifacts or provenance/rule violations.
- `BLOCK`: a critical downstream decision depends on missing truth, unresolved Skill 01 conflict, or high-impact unvalidated hypothesis.
- `REUSE`: existing valid artifacts satisfy the task.

# 10. Outputs
Write `business-model/` artifacts:
`manifest.yaml`, `business-model.yaml`, `product-portfolio.yaml`, `icp.yaml`, `buyer-personas.yaml`, `buying-journey.yaml`, `pain-value-map.yaml`, `commercial-priority.yaml`, `competitor-positioning.yaml`, `knowledge-gaps.yaml`, `closeout.yaml`.

# 11. Handoff
Skill 03 consumes commercial relevance/segments/priority and adds search-demand/SERP evidence. Skill 04 consumes journey/decision/proof needs. Skill 05 consumes pain/value/differentiation under Skill 01 claims rules. Skill 18 consumes segments/intent/value propositions but controls campaign/spend separately. Skill 24 consumes entity/value/evidence clarity. Factual contradictions return to Skill 01.

# 12. Safety / Change Control
Do not invent customer identities, revenue, margins, ROI, market share, buying behavior, competitor performance, or product advantages. Do not present inference/hypothesis as fact. Do not publish unverifiable superiority claims. Analysis and artifact creation may proceed automatically; publishing, paid actions, live-site changes, or other high-impact actions remain subject to orchestrator approval.
