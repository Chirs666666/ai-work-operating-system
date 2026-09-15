# 08 Internal Linking Architecture & Optimization

Decision-layer skill for planning and validating internal links across new pages and existing sites.

It builds or reuses an internal-link graph, evaluates incoming/outgoing opportunities, selects natural anchors and placements, protects URL ownership from skill 25, and hands executable changes to skill 07. It does not directly modify WordPress.

## Modes
`NEW_PAGE_LINKING`, `EXISTING_SITE_OPTIMIZATION`, `VERIFY`, `REFRESH_GRAPH`, `REUSE`.

## Runtime data
Use any suitable combination of `USER_DATA`, `API_DATA`, and `PUBLIC_RESEARCH`. Provider credentials and secrets belong in runtime secret/connector configuration, never in this package.

## Validate
```bash
python scripts/validate_package.py
python scripts/validate_examples.py
```
