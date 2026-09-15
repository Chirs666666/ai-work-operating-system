---
name: WB04-website-page-assembly
display_name: WB04 Website Page Assembly
version: 1.0.0
description: Assemble validated SEO/content/media/global-component artifacts into a WordPress-ready page specification.
---

# 1. Purpose
Turn upstream artifacts into a deterministic page assembly contract without silently writing missing specialist content or publishing.

# 2. Trigger
Use for HOME, ABOUT, PRODUCT_CATEGORY, PRODUCT_DETAIL, SERVICE, APPLICATION, INDUSTRY, RESOURCE_HUB, ARTICLE, CONTACT, CUSTOM assembly; VERIFY and REUSE are also supported.

# 3. Do Not Trigger
Do not use to replace copywriting, keyword ownership, metadata creation, image generation, global component definition, WordPress execution, or production publishing.

# 4. Inputs
WB01 page identity/URL/hierarchy; WB02 editor/foundation; WB03 global components; 04 page plan; 05/06 content; 09 metadata; 17 media; 24 GEO; CTA/conversion requirements.

# 5. Preconditions
Page identity must resolve to WB01 for assembly-ready work. Required upstream artifacts must exist or be explicitly blocked/unknown.

# 6. Workflow
PAGE REQUEST → IDENTITY → ARTIFACT DISCOVERY → REUSE → PAGE TYPE → SECTIONS → SOURCE MAP → GLOBAL COMPONENTS → CONTENT → MEDIA → SEO → CONVERSION → GEO → RESPONSIVE → ACCESSIBILITY → WORDPRESS MAP → VALIDATE → DRAFT BUILD PLAN → 07 HANDOFF

# 7. Tool Routing
WB01 owns page identity/URL; 04 owns section planning; 05 owns product/commercial copy; 06 owns article/informational copy; 09 owns metadata; 17 owns generated images; 24 owns GEO; WB03 owns global components; 07 executes WordPress changes.

# 8. Decision Rules
Every section needs source owner/provenance. Product detail requires Skill 05 content; article requires Skill 06 content. Global components are referenced, never silently copied. Media bindings require artifact references. Unsupported claims block readiness. CTA requires a destination.

# 9. Quality Gates
PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
Canonical YAML artifacts covering identity, upstream artifacts, page type, sections/source map, content/media/SEO/conversion/GEO/global components, responsive/accessibility, WordPress blocks, assembly manifest/conflicts, draft build plan, approvals, verification, handoffs and closeout.

# 11. Handoff
Primary execution handoff is to 07 in DRAFT_ONLY unless the user separately approves publication. 08/12/WB07 may consume validated assembly artifacts.

# 12. Safety / Change Control
Assembly is not publication. Production publishing requires explicit approval evidence. Never invent missing claims, copy, media or SEO data.
