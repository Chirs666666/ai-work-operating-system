---
name: wordpress-page-builder-publisher
display_name: 07 WordPress Page Builder & Publisher
description: Build, read back, verify, and approval-control WordPress pages from approved upstream artifacts using Block Editor or Elementor adapters.
version: 1.0.0
---

# 1. Purpose

`07 WordPress Page Builder & Publisher` is the WordPress execution layer. It turns approved upstream design, copy, SEO, image, and internal-link decisions into a verifiable WordPress Draft, then controls high-impact actions through explicit approval.

Core principle: **Upstream Skills are Decision Owners. 07 is the WordPress Execution Owner.**

# 2. Trigger

Use this skill when the task is to create, update, rebuild, verify, or publish a WordPress page/post from approved artifacts, including:
- create a new WordPress Draft;
- update or rebuild an unpublished Draft;
- apply approved SEO metadata, internal links, and image assets;
- validate a page against an approved Blueprint or Page Build Contract;
- prepare an approved page for publication;
- perform an explicitly approved live-page mutation with recovery and post-write verification.

Supported work modes: `CREATE_DRAFT`, `UPDATE_DRAFT`, `REBUILD_DRAFT`, `VERIFY`, `REUSE`.

Supported build modes: `BLOCK_EDITOR`, `ELEMENTOR`.

# 3. Do Not Trigger

Do not use 07 as the decision owner for:
- page strategy or UI architecture (04);
- product positioning or product-page copy strategy (05);
- informational article strategy/writing (06);
- internal-link strategy (08);
- SEO title/meta decisions (09);
- image generation or visual concept creation (17);
- indexing/ranking strategy (19);
- keyword-to-page ownership (25).

Do not silently migrate an existing page between builders, install/activate plugins, change themes/global styles, publish, delete, bulk-change, or mutate a live page without explicit approval.

# 4. Inputs

Primary inputs:
- 04 Blueprint / page architecture when the page requires designed structure;
- approved 05 or 06 copy;
- 08 internal-link decisions when available;
- 09 metadata decisions when available;
- 17 image assets/metadata recommendations when available;
- 25 page ownership/target URL decisions where relevant;
- WordPress project environment and current persisted page state;
- Project Component Registry and Builder Capability Matrix.

Every material input should retain provenance. Missing values use explicit states such as `UNKNOWN`, `NOT_PROVIDED`, or `UNAVAILABLE`.

# 5. Preconditions

Before any page write:
1. resolve or refresh the Project WordPress Profile;
2. resolve build mode and preserve the existing builder for existing pages;
3. load Global + Project Component Registry;
4. normalize approved inputs into a Page Build Contract;
5. run the Compatibility Gate;
6. produce a Build Plan;
7. verify that the requested operation is inside the current approval boundary.

A missing critical input, dependency, permission, or execution capability yields `BLOCK`.

# 6. Workflow

```text
INPUT
↓
Environment Discovery / REUSE
↓
Normalize Upstream Artifacts
↓
Page Build Contract
↓
Compatibility Gate
↓
Component Matching
↓
Build Plan
↓
Builder Adapter
↓
Execution Channel
↓
WordPress Draft / Approved Live Mutation
↓
Mandatory Read-back
↓
L1 Structure QA
↓
L2 Visual + Responsive QA
↓
L3 Content Integrity QA
↓
Safe Auto Repair if allowed
↓
Re-validate
↓
G07
↓
Approval gate for high-impact action
↓
Post-write / Post-publish Read-back
```

07 is a **Blueprint Executor**, not a second UI Designer. No valid component match means `CUSTOM_COMPONENT_REQUIRED`, `CONFLICT`, or `BLOCK`, not silent redesign.

# 7. Tool Routing

Express requirements as capabilities, not vendor-hardcoded dependencies:
- `wordpress_environment_read`
- `wordpress_content_read`
- `wordpress_draft_create`
- `wordpress_draft_update`
- `wordpress_live_update`
- `builder_capability_read`
- `component_registry_read`
- `media_upload`
- `media_read`
- `seo_field_write`
- `internal_link_write`
- `browser_render`
- `responsive_render`
- `visual_compare`
- `structured_compare`

Runtime routes may include WordPress API, MCP/plugin/connector, browser/computer use, or controlled scripts. Choose the most reliable, verifiable, lowest-risk route for the specific operation. Transport success never equals page-quality success.

# 8. Decision Rules

- Preserve upstream decisions; mechanical formatting repairs may not change meaning.
- Preserve existing builder by default.
- Prefer `VERIFIED` project components. `AVAILABLE` requires stronger QA. Missing critical components do not get improvised replacements.
- Repeated execution must be idempotent: no duplicate sections, images, internal links, metadata, or components.
- Detect drift before modifying an existing Draft/live page.
- Preserve unrelated manual edits when reliably separable; overlapping/conflicting drift yields `BLOCK` or `WARN` with diff.
- Every write requires read-back and comparison against approved sources.
- Low-risk Draft repair is allowed only for implementation defects, never strategy changes.

# 9. Quality Gates

`G07` values are exactly:
- `PASS` — Draft construction and required QA completed successfully.
- `WARN` — non-critical issues/uncertainties remain and are recorded.
- `FAIL` — build/integrity defect must be repaired.
- `BLOCK` — critical input/capability/permission/environment/component is missing.
- `WAITING_APPROVAL` — high-impact action is ready but not authorized.
- `REUSE` — current profile/component/Draft/build already satisfies the requirement.

Three QA layers are mandatory where applicable:
1. Structure QA;
2. Visual + Responsive QA;
3. Content Integrity QA.

# 10. Outputs

Canonical outputs:
- `manifest.yaml`
- `project-wordpress-profile.yaml`
- `builder-capability-matrix.yaml`
- `component-registry.yaml`
- `component-match.yaml`
- `page-build-contract.yaml`
- `build-plan.yaml`
- `execution-log.yaml`
- `readback.yaml`
- `structure-qa.yaml`
- `visual-qa.yaml`
- `responsive-qa.yaml`
- `content-integrity-qa.yaml`
- `metadata-write-report.yaml`
- `internal-link-write-report.yaml`
- `asset-write-report.yaml`
- `change-control.yaml`
- `build-gaps.yaml`
- `closeout.yaml`

# 11. Handoff

Typical handoffs:
- blueprint cannot be implemented safely → 04;
- unsupported/missing product claim → 01/05 as appropriate;
- informational content decision gap → 06;
- internal-link conflict → 08;
- metadata decision gap → 09;
- image asset gap → 17;
- index/ranking verification after publication → 19;
- keyword/page ownership conflict → 25.

If the task goal is Draft, `PASS` may complete 07. If the task goal includes publishing or another live mutation, use `WAITING_APPROVAL` until explicit approval, then require post-action read-back before completion.

# 12. Safety / Change Control

Auto-allowed: create/update unpublished Draft, read, read-back verification, structure/visual/responsive/content-integrity QA, and low-risk Draft repair.

Explicit approval required: publish, update live page, delete page, bulk page changes, plugin install/activation/deactivation, theme/global design/global template/sitewide settings changes, builder migration, and similarly high-impact mutations.

Never store credentials, API keys, WordPress Application Passwords, tokens, connector auth data, or MCP secrets in the package, examples, logs, or repository.
