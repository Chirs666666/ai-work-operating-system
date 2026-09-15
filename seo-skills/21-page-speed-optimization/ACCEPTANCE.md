# Acceptance Matrix

| Requirement | Evidence |
|---|---|
| Field and lab remain separate | high-lighthouse-poor-field |
| Missing field data remains null/UNKNOWN | missing-field-data |
| LCP image bottleneck | lcp-image-bottleneck |
| TTFB origin/cache diagnosis | ttfb-origin-bottleneck |
| INP third-party JS diagnosis | inp-third-party-js |
| CLS dimension diagnosis | cls-image-dimensions |
| Risky changes require backup + approval | risky-js-delay, risky-plugin-change |
| No-backup risky change blocks | no-backup-risky-change |
| Non-comparable tests cannot prove improvement | mobile-vs-desktop-compare |
| Lab improvement does not instantly prove field improvement | lab-improved-field-pending |
| Faster but broken functionality fails | functionality-regressed |
| WordPress/cache/image/third-party action planning | wordpress-cache-plan, image-optimization-plan, third-party-plan |
| Retest improved/unchanged | retest-improved, retest-unchanged |
| REUSE/VERIFY supported | reuse, verify |
