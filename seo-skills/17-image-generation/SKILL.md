---
name: 17-image-generation
display_name: Image Generation
description: Plan, generate, edit, enhance, resize and validate evidence-safe B2B industrial visual assets, then package them for SEO/accessibility and WordPress handoff.
version: 1.0.0
---
# 1. Purpose
Convert page/content visual needs into controlled image-generation or editing contracts while preserving product truth, source provenance, technical accuracy and downstream SEO usability.

# 2. Trigger
Use for new image generation, image edits, clarity enhancement, resize/crop, background replacement, color variation, product/process visuals, technical diagrams, article heroes, banners, thumbnails, calculator visuals, image SEO packaging, verification or reuse.

# 3. Do Not Trigger
Do not use to invent technical data, certification marks, customers, factory evidence, product geometry or unsupported documentary claims. Do not treat a generated scene as proof of a real facility or customer application.

# 4. Inputs
Page/content context from 04/05/06/16; source images when editing; approved product/technical facts; brand rules; target dimensions/aspect ratio; asset role; generation/edit request; USER_DATA/API_DATA/PUBLIC_RESEARCH evidence where appropriate.

# 5. Preconditions
For EDIT/ENHANCE/CROP/BACKGROUND_REPLACE/COLOR_VARIATION, a usable source image must exist. Technical labels/numbers require evidence. Define intended size/role before production.

# 6. Workflow
PAGE / CONTENT NEED → IMAGE REQUIREMENT → IMAGE TYPE → SOURCE/TRUTH CHECK → GENERATE/EDIT/ENHANCE → TECHNICAL ACCURACY → BRAND/VISUAL CONSISTENCY → SEO ASSET PACKAGING → G17 → 07 HANDOFF.

Modes: GENERATE, EDIT, ENHANCE, RESIZE, CROP, BACKGROUND_REPLACE, COLOR_VARIATION, DIAGRAM, PROCESS_VISUAL, PRODUCT_VISUAL, ARTICLE_HERO, BANNER, THUMBNAIL, VERIFY, REUSE.

# 7. Tool Routing
Use an image-generation/editing capability for visual production. Use source files when edits depend on an existing image. Use deterministic scripts for metadata/schema validation, not for hallucinating image facts.

# 8. Decision Rules
Generated visuals retain provenance. Technical claims require evidence. Missing technical facts become UNKNOWN or are omitted. Conceptual factory/process scenes must not be represented as real documentary evidence. Existing subject identity should be preserved unless explicitly changed.

# 9. Quality Gates
G17: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.
BLOCK for missing edit source or unsupported factual technical content.
FAIL when output violates the image contract.
WARN for explicit acceptable conceptual limitations.
REUSE when an existing asset already satisfies the requirement.

# 10. Outputs
Use the 23 canonical outputs in `references/canonical-outputs.md`.

# 11. Handoff
04 visual requirements; 05 product context; 06 article context; 16 calculator context; 17 image production/QA; 07 WordPress asset upload/insertion/ALT; 09 page metadata remains separate.

# 12. Safety / Change Control
Do not fabricate product/factory/customer/certification/technical evidence. Factual edits that could change interpretation require review. 17 does not directly publish WordPress assets.
