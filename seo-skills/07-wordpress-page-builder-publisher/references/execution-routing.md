# Execution Routing

07 requests capabilities rather than hardcoding a vendor:

`wordpress_environment_read`, `wordpress_content_read`, `wordpress_draft_create`, `wordpress_draft_update`, `wordpress_live_update`, `builder_capability_read`, `component_registry_read`, `media_upload`, `media_read`, `seo_field_write`, `internal_link_write`, `browser_render`, `responsive_render`, `visual_compare`, `structured_compare`.

Runtime execution classes may include WordPress API, MCP/plugin/connector, browser/computer use, and controlled scripts.

Choose the most reliable, verifiable, lowest-risk route for each operation. A successful HTTP status, connector action, browser click, or script exit code only proves transport/execution success; it does not prove page correctness.
