---
name: company-knowledge-base
display_name: 公司知识库搭建
description: >
  Build, update, verify, refresh, merge, or audit the company and product
  truth base used by downstream B2B website, SEO, content, GEO, advertising,
  and publishing workflows. Never invent missing company or product facts.
version: 1.0.0
---

# 1. Purpose
Create and maintain the single source of truth for one company. Convert fragmented approved materials into structured, evidence-aware company and product knowledge that downstream skills can safely reuse. This skill establishes facts, provenance, terminology, claims restrictions, conflicts, and knowledge gaps; it does not perform market or SEO strategy.

# 2. Trigger
Use this skill to onboard a company, build or update its truth base, ingest new catalogs/spec sheets/certificates/cases, verify a disputed claim, refresh stale knowledge, merge knowledge sets, or audit knowledge quality. If a valid truth base already contains everything required for the current task, return `REUSE` rather than rebuilding it.

Modes: `CREATE | UPDATE | VERIFY | REFRESH | MERGE | AUDIT`.
- `CREATE`: no usable truth base exists.
- `UPDATE`: approved new material changes or adds facts.
- `VERIFY`: validate one or more claims without broad rebuilding.
- `REFRESH`: re-check time-sensitive or stale facts/sources.
- `MERGE`: combine two or more truth bases while preserving provenance and conflicts.
- `AUDIT`: inspect artifact quality, provenance, consistency, and downstream readiness without changing verified truth unless explicitly authorized.

# 3. Do Not Trigger
Do not use this skill as the primary workflow for keyword research, search intent, SERP/competitor SEO research, business strategy, page-type selection, product copy, blog writing, analytics, technical SEO, backlink research, or page publishing. Route those tasks to their specialist skills after this truth layer is ready.

# 4. Inputs
At least one approved company-information source is required for `CREATE`. Typical sources include company profiles, product catalogs, specification sheets, engineering documents, certificates, cases, official websites, customer-provided facts, spreadsheets, PDFs, images, videos, quotations, sales decks, and prior truth artifacts.

For every source record: `source_id`, category, name, owner/publisher when known, date/version when known, location, trust/provenance notes, and publication permission when relevant. Missing values stay `UNKNOWN` or `NOT_PROVIDED`; never convert absence into numeric zero.

# 5. Preconditions
Identify the company/project scope and, when known, target language. Separate customer-provided material from company-official and external sources before extraction. Treat website text as evidence of what the website states, not automatic proof of truth. Do not silently replace customer facts with external information. Do not infer unreadable or missing technical values.

Load only the references needed for the current decision:
- `references/knowledge-methodology.md` for the end-to-end extraction method.
- `references/source-classification.md` for provenance categories.
- `references/evidence-levels.md` for E1–E5.
- `references/claims-policy.md` for GREEN/YELLOW/RED publication rules.
- `references/terminology-rules.md` for normalized terms.
- `references/conflict-resolution.md` when sources disagree.
- `references/update-policy.md` for modes, versions, and change handling.

# 6. Workflow
1. Inventory sources and classify provenance.
2. Extract entities without merging merely similar entities.
3. Extract company facts: identity, scope, locations, capabilities, industries, certifications, services, approved commercial facts.
4. Extract product truth per product/model: names, family, applications, processes, materials, specifications, options, boundaries, evidence, unknown fields.
5. Separate claimed capability from specification proof, case evidence, and external reporting.
6. Map high-value publishable claims to evidence records.
7. Detect conflicts; preserve competing values and provenance rather than silently selecting a winner.
8. Normalize terminology without turning terminology work into keyword research.
9. Classify claims GREEN/YELLOW/RED.
10. Record knowledge gaps and downstream impact.
11. Run current-task sufficiency: determine what can proceed and what is blocked.
12. Write the canonical artifact package and closeout result.

# 7. Tool Routing
Choose tools by capability, not vendor lock-in.

| Capability | Primary | Fallback | Rule |
|---|---|---|---|
| Conversation/library documents | Connected file reader | Local deterministic parser | Never reconstruct unreadable values |
| PDF/Word/Excel extraction | Parsed document/file tools | Local parser | Preserve source location when possible |
| Company website extraction | Structured crawler | Browser/web fetch | Website statement is not automatic verification |
| Public fact verification | Primary/official web sources | Reliable secondary sources | External evidence must not silently overwrite customer facts |
| Structured comparison | Deterministic comparison + model review | Human review | Critical disagreement becomes CONFLICT |
| Artifact writing | Project/repository files | Working-directory artifacts | Preserve version and provenance |

Prefer evidence sources in this order when applicable: approved primary company/engineering records; authoritative certification/standards records; technical primary sources; reliable third-party sources; secondary reporting. Tool failure must produce `UNKNOWN`, `WARN`, or `BLOCK` as appropriate—not invented data.

# 8. Decision Rules
- Keep `USER_PROVIDED`, `COMPANY_OFFICIAL`, `EXTERNAL_PRIMARY`, `EXTERNAL_SECONDARY`, `INFERRED`, and `UNKNOWN` distinguishable.
- `E5` cannot support a publishable factual claim.
- AI inference is never evidence.
- Never infer a specification from a similar product/model.
- A capability statement is not a performance guarantee.
- Critical conflicts retain all candidate values and require confirmation.
- Downstream readiness is task-specific: a missing detailed spec can block a specification page while not blocking a general educational article.
- Existing verified artifacts are reused unless scope, staleness, conflicts, or new approved evidence require another mode.

# 9. Quality Gates
Use `G01 — COMPANY TRUTH GATE`.
- `PASS`: required identity/product facts for the current task are supported and no critical unresolved conflict blocks use.
- `WARN`: non-critical information/evidence is incomplete, but the current task can proceed safely.
- `FAIL`: artifacts are malformed, inconsistent, broken, or violate the required structure/policies.
- `BLOCK`: the current task requires missing critical facts, unresolved critical conflicts, or unsupported claims that cannot safely be used.
- `REUSE`: an existing valid truth base already satisfies the current task.

# 10. Outputs
Canonical package: `manifest.yaml`, `company.yaml`, `products.yaml`, `evidence-register.yaml`, `knowledge-gaps.yaml`, `claims-policy.yaml`, and `closeout.yaml`. Use the matching files in `templates/` and validate structures against `schemas/` when deterministic validation is available. Maintain a change log in project/repository history for updates.

# 11. Handoff
Downstream consumers include business-model analysis, keyword research, page planning/UI, product copy, article writing, image generation, Google Ads, and GEO. Consumers may read verified truth and report gaps/conflicts, but must not silently modify verified facts. New evidence or contradictions route back to this skill using `UPDATE` or `VERIFY`.

# 12. Safety / Change Control
Never invent company, product, certification, customer, performance, ROI, or technical facts. Never silently resolve a critical conflict. Never publish RED claims without the evidence/approval required by policy. Never mutate verified truth from a downstream skill. Preserve provenance and prior values when updating. Actions that publish externally, delete source artifacts, overwrite authoritative records, or make irreversible changes require the orchestrator's approval policy; this skill's normal output is knowledge artifacts, not external publication.
