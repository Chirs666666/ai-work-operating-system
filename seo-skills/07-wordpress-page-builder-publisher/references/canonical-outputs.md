# Canonical Outputs

Canonical filenames:

`manifest.yaml`, `project-wordpress-profile.yaml`, `builder-capability-matrix.yaml`, `component-registry.yaml`, `component-match.yaml`, `page-build-contract.yaml`, `build-plan.yaml`, `execution-log.yaml`, `readback.yaml`, `structure-qa.yaml`, `visual-qa.yaml`, `responsive-qa.yaml`, `content-integrity-qa.yaml`, `metadata-write-report.yaml`, `internal-link-write-report.yaml`, `asset-write-report.yaml`, `change-control.yaml`, `build-gaps.yaml`, `closeout.yaml`.

Normally required: manifest, profile or profile-reuse result, capability matrix, component match, build contract, build plan, execution log, read-back, applicable QA reports, change control, build gaps, and closeout.

Metadata/internal-link/asset write reports are conditional on those operations being part of the requested build. Visual/responsive reports must exist when those checks are required; unavailable rendering capability is represented as an explicit blocked/gap state, not omission.
