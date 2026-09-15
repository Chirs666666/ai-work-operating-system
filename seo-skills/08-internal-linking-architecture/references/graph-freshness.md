# Graph Freshness
States: `CURRENT`, `PARTIALLY_STALE`, `STALE`, `UNKNOWN`. Operations: `FULL_BUILD`, `FULL_REFRESH`, `INCREMENTAL_UPDATE`, `REUSE`. Decide freshness from sitemap/URL/content/redirect/ownership changes, collection time and current-task risk. Reuse forms include `GRAPH_REUSE`, `LINK_REUSE`, `PLAN_REUSE`. No universal day-based stale threshold.
