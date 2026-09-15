---
name: 16-calculator-tool-builder
display_name: Calculator Tool Builder
description: Design and validate evidence-backed industrial calculators, including formula contracts, variables, units, assumptions, edge cases, deterministic tests, calculation-engine behavior, frontend behavior, supporting content and implementation handoff.
version: 1.0.0
---
# 1. Purpose
Turn a validated calculator/tool opportunity into a reproducible engineering calculation specification that can be safely implemented and verified.

# 2. Trigger
Use for industrial calculators, engineering formula tools, conversion tools, cycle-time calculators, geometry calculators, cost/weight estimators, or when an existing calculator formula/logic must be reviewed or refreshed.

# 3. Do Not Trigger
Do not use this skill to invent unsupported formulas, perform final keyword ownership decisions, design an entire page unrelated to the calculator, publish WordPress content, or claim rankings/indexing.

# 4. Inputs
USER_DATA, API_DATA, PUBLIC_RESEARCH. Typical inputs include approved company formulas, standards, engineering references, technical manuals, existing calculators, keyword demand, target URL/page contract, UI constraints, and user examples.

# 5. Preconditions
Define calculator purpose, user decision supported, required outputs, formula evidence status, variable meanings, unit expectations, and any known engineering boundaries. Production implementation is blocked when authoritative formula evidence is absent.

# 6. Workflow
SEARCH / BUYER NEED → CALCULATOR OPPORTUNITY → FORMULA SOURCE & EVIDENCE → FORMULA CONTRACT → VARIABLES & UNITS → ASSUMPTIONS / BOUNDARIES → EDGE CASES → TEST VECTORS → CALCULATION ENGINE CONTRACT → FRONTEND CONTRACT → EXPLANATORY CONTENT CONTRACT → QA / G16 → IMPLEMENTATION HANDOFF.

Modes: OPPORTUNITY_ASSESSMENT, FORMULA_DESIGN, BUILD_SPEC, VALIDATE, REFRESH, VERIFY, REUSE.

# 7. Tool Routing
Use provider-agnostic research and implementation. Formula evidence may come from user documents, APIs/connectors or public authoritative sources. Runtime code/framework choice is downstream unless the project already constrains it.

# 8. Decision Rules
Only VERIFIED or explicitly CONDITIONALLY_VERIFIED formulas may proceed toward production. Missing limits remain UNKNOWN/null. Unit conversion must be explicit and tested. Any formula or conversion-constant change requires revalidation. Do not use silent assumptions or arbitrary engineering defaults.

# 9. Quality Gates
G16: PASS, WARN, FAIL, BLOCK, REUSE, WAITING_APPROVAL.
FAIL: deterministic tests fail or implementation contradicts the formula contract.
BLOCK: formula evidence is UNKNOWN/UNSUPPORTED/CONFLICTING for production, or required evidence is missing.
WARN: explicit acceptable limitations remain.
REUSE: existing validated calculator contract remains fit for purpose.

# 10. Outputs
Use the 22 canonical outputs in `references/canonical-outputs.md`.

# 11. Handoff
03 demand/keywords; 25 final Keyword→CALCULATOR_TOOL URL; 04 broader page/UI blueprint; 06 supporting informational writing; 09 metadata; 17 images; 07 WordPress implementation; 19 index/ranking lifecycle; 13 post-launch analysis.

# 12. Safety / Change Control
Never fabricate formulas, constants, machine/material limits, correction factors, precision claims or passing tests. Formula logic, conversion constants and result interpretation are high-impact changes and require revalidation before production release.
