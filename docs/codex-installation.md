# Codex Installation / Runtime Layout
Use the skill directories in this repository as Codex-readable skill sources. The exact product UI/installation mechanism can evolve, so do not hard-code account-specific UI paths here.

Runtime set:
- `system/seo-workflow-system` — default top-level entry.
- `system/website-build-layer` — build subsystem.
- every directory under `seo-skills/`.
- every directory under `website-build-skills/`.

Do not install a standalone Skill 14; it is an alias to Skill 12.

Keep project repositories lightweight. A project should reference the orchestrator through its concise `AGENTS.md`; it should not copy this whole library into every project.
