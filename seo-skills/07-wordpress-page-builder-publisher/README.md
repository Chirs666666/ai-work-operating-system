# 07 WordPress Page Builder & Publisher

A controlled WordPress construction and verification skill for B2B SEO/content workflows.

## Architecture

`Approved artifacts → Project Environment → Page Build Contract → Component Matching → Builder Adapter → WordPress Write → Read-back → Three-Layer QA → G07 → Approval → Post-write verification`.

V1 supports `BLOCK_EDITOR` (Gutenberg / native blocks / Greenshift) and `ELEMENTOR` (Elementor / Elementor Pro when already available).

This package intentionally does not contain site credentials or a hardcoded WordPress client. Runtime integrations provide the execution capabilities.

## Install

Install the directory as a Codex/agent skill package according to your runtime's skill-loading mechanism. Keep runtime secrets outside the package.

## Validate

```bash
python scripts/validate_package.py
python scripts/validate_examples.py
```

Both commands should print `PASS`.
