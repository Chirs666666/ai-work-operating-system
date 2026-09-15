---
name: WB03-global-components-builder
display_name: WB03 Global Components Builder
version: 1.0.0
description: Define and validate reusable global website components before page assembly.
---

# 1. Purpose
Create reusable global component specifications for WB04.

# 2. Trigger
NEW_SITE, REBUILD, COMPONENT_AUDIT, COMPONENT_REFRESH, VERIFY, REUSE.

# 3. Do Not Trigger
Do not use for copywriting, page-specific architecture, full page assembly, publishing, or silent production changes.

# 4. Inputs
WB01 navigation/hierarchy/page inventory; WB02 theme/editor/design tokens/plugin constraints; CTA/form requirements; accessibility and responsive requirements.

# 5. Preconditions
WB01/WB02 artifacts should be available or their absence explicitly marked UNKNOWN/BLOCKED.

# 6. Workflow
INPUT CHECK → INVENTORY → HEADER → NAVIGATION → MOBILE NAVIGATION → FOOTER → BREADCRUMB → CTA → FORMS → PATTERNS → SYSTEM COMPONENTS → RESPONSIVE → ACCESSIBILITY → OWNERSHIP → WORDPRESS PLAN → VERIFY → HANDOFF

# 7. Tool Routing
WB01 owns architecture; WB02 owns foundation; 04 owns page planning; 07 may execute WordPress changes; 08 owns internal-link architecture; 12 owns technical SEO; WB04 assembles pages.

# 8. Decision Rules
Never silently redefine WB01 navigation or WB02 tokens. Reusable patterns must be parameterized. CTA requires action/destination. Forms require success/error behavior and privacy/consent decision. Duplicate component ownership is invalid unless explicitly resolved.

# 9. Quality Gates
PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.

# 10. Outputs
manifest, component inventory/ownership, header/navigation/mobile/footer/breadcrumb specs, CTA/forms/patterns/system components, responsive/accessibility/alignment artifacts, WordPress plan, approvals, verification, handoffs, closeout.

# 11. Handoff
WB04 consumes component specs; 07 consumes implementation plan; 08 consumes navigation/breadcrumb context; 12 consumes technical conflicts.

# 12. Safety / Change Control
Production global component changes require explicit approval. Planning is not approval.
