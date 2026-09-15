# Error Routing

| Problem | Owner / action |
|---|---|
| Missing or unsupported company/product claim evidence | return to 01/05 |
| Blueprint cannot be implemented safely | return to 04 |
| Informational-content strategy/copy decision missing | return to 06 |
| Internal-link strategy conflict | return to 08 |
| Required metadata decision missing | return to 09 |
| Required image asset unavailable | return to 17, or WARN/BLOCK based on criticality |
| Keyword/page ownership conflict | return to 25 |
| WordPress authentication/capability failure | `BLOCK` in 07 |
| Builder serialization/rendering failure | `FAIL` in 07; repair/retry if safe |
| High-impact action not approved | `WAITING_APPROVAL` |

A `BLOCK` stops dependent actions, not unrelated branches managed by the orchestrator.
