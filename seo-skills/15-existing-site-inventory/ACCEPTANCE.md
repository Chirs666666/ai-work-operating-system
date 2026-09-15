# Acceptance Matrix

| # | Requirement | Evidence |
|---|---|---|
| 01 | Existing-site entry layer | SKILL |
| 02 | 7 modes | manifest schema |
| 03 | 21 canonical outputs | package validator |
| 04 | URL normalization without deletion | duplicate-variant |
| 05 | Ranking asset protection | ranking-protection |
| 06 | Backlink asset protection | backlink-protection |
| 07 | Missing metrics stay null | missing-data |
| 08 | Third-party data does not override first-party | provider-conflict |
| 09 | MERGE requires 25 | merge-candidate |
| 10 | REDIRECT requires 25 | redirect-candidate |
| 11 | NOINDEX approval + 12 validation | noindex-candidate |
| 12 | Ownership conflict handoff | ownership-conflict |
| 13 | Commercial page → 10 | commercial-handoff |
| 14 | Informational article → 06 | article-handoff |
| 15 | Technical issue → 12 | technical-handoff |
| 16 | High-impact actions never auto-execute | semantic validator |
| 17 | REUSE outcome supported | reuse |
| 18 | VERIFY mode supported | verify |
| 19 | No secrets | secret scan |
