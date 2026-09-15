# Change Control
Risk classes: SAFE_READ_ONLY, SAFE_REVERSIBLE_FIX, LIVE_PAGE_TECHNICAL_CHANGE, SITEWIDE_CONFIGURATION_CHANGE, URL_OWNERSHIP_CHANGE, SERVER_OR_CDN_CHANGE.
SAFE_READ_ONLY needs no approval. SAFE_REVERSIBLE_FIX may run only within authorized scope. All other live/high-impact classes require WAITING_APPROVAL.
Examples requiring approval: redirects, canonicals, robots/noindex, sitemap generation, headers, bulk link changes, global CMS/SEO plugin settings, server/CDN rules.
