---
name: 04-page-planning-ui
display_name: Page Planning & UI
description: Converts a confirmed page ownership contract into an evidence-aware Page Blueprint covering strategy, information architecture, sections, proof, CTA, visuals, UI, responsive behavior, and downstream handoff without directly building WordPress.
version: 1.0.0
---
# 1. Purpose
Turn Skill 25's confirmed page contract into an implementation-ready Page Blueprint. Preserve upstream ownership and define strategy, IA, sections, proof, CTA, imagery, UI, responsive behavior, components, gaps, and handoffs.

# 2. Trigger
Use after G25 when a new page, redesign, or structural refresh needs page planning. Use STANDARD for batch/site planning and DETAILED for production-ready pages.

# 3. Do Not Trigger
Do not use to decide keyword-to-URL ownership (25), write final product copy (05), write/refresh informational copy (06), generate images (17), or construct/publish WordPress (07).

# 4. Inputs
Required: page type, primary/planned URL, keyword ownership, search intent, page action, G25 status. Read approved truth from 01, buyer/business context from 02, keyword/SERP evidence from 03. Optional: brand guidelines, design system, screenshots, component inventory, public research.

Data methods: USER_DATA, API_DATA, PUBLIC_RESEARCH. Record provenance. Missing evidence stays UNKNOWN/NOT_PROVIDED; never convert it to 0.

# 5. Preconditions
G25 must be usable. If page ownership, URL, or page type is materially unresolved, BLOCK and return to 25. Do not silently repair upstream ownership.

# 6. Workflow
Validate G25/page contract → choose STANDARD or DETAILED → choose NEW_PAGE, REDESIGN, or STRUCTURAL_REFRESH → load Base Blueprint → adapt for intent → adapt for buyer/business context → adapt for evidence/proof → adapt for SERP/market evidence when available → adapt for UX/conversion → assign section states/order → define content/proof/CTA/image/UI/responsive/component requirements → record gaps/conflicts → run G04 → hand off.

Base Blueprints are adaptable starting points, not rigid templates. Order sections using Search Journey + Buyer Journey + Conversion Journey.

# 7. Tool Routing
Route by capability, not vendor:
- page_contract_read: structured project data or USER_DATA
- company_truth_read: Skill 01 outputs or approved USER_DATA
- business_context_read: Skill 02 outputs
- keyword_dataset_read: Skill 03 outputs
- serp_search: API_DATA, PUBLIC_RESEARCH, or USER_DATA
- website_research: PUBLIC_RESEARCH, API_DATA, or USER_DATA
- design_context_read: USER_DATA, API_DATA, or PUBLIC_RESEARCH
Unavailable optional capabilities create explicit gaps; they never authorize invented evidence.

# 8. Decision Rules
Section states: REQUIRED, RECOMMENDED, CONDITIONAL, OPTIONAL, EXCLUDED.
SERP prevalence is evidence, not a command. Add information-gain sections when they solve real buyer decisions.
Material claims require proof slots. Missing proof means request evidence, weaken/remove the unsupported claim, or record a gap.
UI specifications are platform-agnostic. Define enough layout/responsive detail that 07 can execute without redesigning.
Do not claim accessibility/WCAG compliance without implementation testing.

# 9. Quality Gates
G04 statuses: PASS, WARN, FAIL, BLOCK, REUSE.
PASS: blueprint is production-ready for appropriate downstream work.
WARN: safe work can continue with non-critical documented gaps.
FAIL: blueprint itself is materially defective or contradicts confirmed contract.
BLOCK: critical upstream dependency prevents reliable planning.
REUSE: an existing valid blueprint still satisfies the current contract.
Final copy and final images are not prerequisites for G04.

# 10. Outputs
Produce exactly these canonical artifacts:
manifest.yaml; page-contract.yaml; page-strategy.yaml; information-architecture.yaml; section-blueprint.yaml; content-requirements.yaml; proof-requirements.yaml; cta-plan.yaml; image-requirements.yaml; ui-spec.yaml; responsive-spec.yaml; component-plan.yaml; blueprint-gaps.yaml; closeout.yaml.

# 11. Handoff
05 receives commercial/product copy slots. 06 receives informational content slots. 17 receives image requirements. 07 receives DETAILED blueprint plus completed content/assets/metadata as available. Return ownership contradictions to 25 and unsupported company claims to 01.

# 12. Safety / Change Control
This skill is planning-only. Never publish/delete pages, execute redirects/noindex/removal, change live navigation/site configuration, purchase services, or silently alter page ownership. Never fabricate company facts, metrics, certifications, cases, customer results, or proof. Never embed secrets.
