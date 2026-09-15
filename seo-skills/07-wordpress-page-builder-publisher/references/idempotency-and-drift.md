# Idempotency and Drift

Repeated execution must not duplicate sections, components, images, internal links, or metadata.

Stable identities:
- WordPress page/post ID = page identity;
- `section_id` = semantic section identity;
- project `component_id` = implementation identity.

Before updating an existing Draft/live page, compare the current persisted state with the prior verified read-back.

Drift states:
- `NO_MATERIAL_DRIFT`: apply intended update.
- `SAFE_MANUAL_DRIFT`: preserve unrelated manual edits and update only reliably scoped targets.
- `CONFLICTING_DRIFT`: overlapping/manual changes create overwrite risk; produce diff and `BLOCK` or `WARN` according to criticality.

Do not mutate live content merely to plant hidden tracking markers.
