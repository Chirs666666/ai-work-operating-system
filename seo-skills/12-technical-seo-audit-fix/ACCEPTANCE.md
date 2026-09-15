# Acceptance Matrix

| # | Requirement | Evidence |
|---|---|---|
| 01 | Broken-link + technical SEO merged | SKILL.md |
| 02 | Six modes | SKILL + manifest schema |
| 03 | 22 canonical outputs | package validator |
| 04 | 404 does not auto-redirect | broken-internal-link + semantic validator |
| 05 | Redirect chain/loop handling | redirect-chain / redirect-loop |
| 06 | Ownership-gated redirects/canonicals | canonical-conflict / ownership-block |
| 07 | Robots/noindex intent comparison | unexpected-noindex / robots-block |
| 08 | Sitemap validation | sitemap-errors |
| 09 | Orphan semantic handoff to 08 | orphan-handoff |
| 10 | Hreflang validation | hreflang-error |
| 11 | Existing structured-data technical errors | structured-data-error |
| 12 | Safe reversible fix scope | safe-fix |
| 13 | Live high-impact approval | live-approval |
| 14 | Write success != fix success | verify-failed |
| 15 | Verified fix requires evidence | verify-fixed + validator |
| 16 | 21 retains page-speed ownership | boundaries |
| 17 | 19 retains index/ranking lifecycle | boundaries |
| 18 | No secrets | secret scan |
