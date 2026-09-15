# Acceptance Matrix

| # | Requirement | Evidence |
|---|---|---|
| 01 | Formula evidence gate | missing-evidence / conflicting-formula |
| 02 | Verified formula contract | bend-allowance |
| 03 | Variable/unit contract | bend-allowance |
| 04 | Known-answer testing | bend-allowance / bend-radius |
| 05 | Unit conversion testing | unit-conversion |
| 06 | Cross-unit equivalence | unit-equivalence |
| 07 | Failed tests block release | failed-tests |
| 08 | Invalid geometry handled | invalid-geometry |
| 09 | Assumptions and boundaries explicit | cnc-cycle-time |
| 10 | Density/material assumption explicit | material-weight |
| 11 | Formula change requires revalidation | formula-change |
| 12 | Frontend behavior contract | frontend-contract |
| 13 | 25 owns URL mapping | commercial-handoff |
| 14 | 06 supporting-content handoff | informational-handoff |
| 15 | REUSE supported | reuse |
| 16 | VERIFY supported | verify |
| 17 | Unsafe defaults rejected | semantic validator |
| 18 | Untested conversions rejected | semantic validator |
| 19 | Unsafe formula execution rejected | semantic validator |
| 20 | No secrets in package | secret scan |
