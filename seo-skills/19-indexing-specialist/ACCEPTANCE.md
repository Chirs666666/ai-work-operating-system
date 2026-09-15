# Acceptance Matrix

| Requirement | Evidence |
|---|---|
| Healthy indexed target query | healthy-indexed-target-query |
| Discovery/crawl/index states separate | not-discovered, crawled-not-indexed |
| NOINDEX/robots block cannot healthy PASS | unexpected-noindex, robots-blocked |
| Canonical-other diagnosed | canonical-other |
| `site:` is auxiliary only | site-query-only |
| Missing GSC data stays null/NO_DATA | missing-gsc-data |
| Unrelated query is not target detection | unrelated-query |
| Target ranking/trend supported | target-query-ranking, ranking-declining |
| T+ milestones are configurable, not guarantees | t7-benchmark, t30-benchmark |
| Technical/ownership/content handoffs | technical-handoff, ownership-handoff, content-handoff |
| REUSE/VERIFY | reuse, verify |
