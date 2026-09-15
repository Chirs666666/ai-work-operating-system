---
name: WB07-pre-launch-qa
display_name: WB07 Pre-Launch QA
version: 1.0.0
description: Evidence-driven pre-launch QA and launch-readiness gate.
---

# 1. Purpose
Determine whether a built site is ready to request launch approval.

# 2. Trigger
Use after build/tracking/infrastructure/technical/performance artifacts exist, for pre-launch QA, re-test, VERIFY or REUSE.

# 3. Do Not Trigger
Do not replace specialist diagnosis, approve launch on the user's behalf, or deploy production.

# 4. Inputs
WB01-WB06 outputs, Skill 07 build result, Skill 12 technical SEO result, Skill 21 performance result, critical URLs/template families, requirements and risk approvals.

# 5. Preconditions
Unknown evidence stays UNKNOWN. Critical/system pages require full coverage. Specialist blocking states must be resolved or explicitly handled.

# 6. Workflow
CONTEXT → UPSTREAM → SAMPLING → PAGE → RESPONSIVE → NAVIGATION → FORMS → EMAIL → CONVERSION → TECH SEO → TRACKING/SEARCH → INFRASTRUCTURE → PERFORMANCE → ACCESSIBILITY → BROWSER → DEFECTS → RETEST → RISK → LAUNCH GATE → WB08

# 7. Tool Routing
Consume 12/21/WB05/WB06 verification. Return defects to responsible skills. Handoff only launch-ready evidence to WB08.

# 8. Decision Rules
BLOCK always blocks. FAIL blocks unless explicitly accepted risk. ACCEPTED_RISK is not PASS. A fixed defect needs retest evidence before PASS. Template-sample failure expands scope.

# 9. Quality Gates
INFO, WARN, FAIL, BLOCK plus PASS and ACCEPTED_RISK result states.

# 10. Outputs
Canonical QA checks, defect/retest/risk registers, launch gate, approvals, verification and handoffs.

# 11. Handoff
WB08 receives READY_FOR_LAUNCH_APPROVAL, never implied user approval.

# 12. Safety / Change Control
QA_PASSED != USER_APPROVED_LAUNCH != DEPLOYED != PRODUCTION_VERIFIED.
