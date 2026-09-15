# Update Workflow
1. Change the canonical skill source in GitHub.
2. Run that skill's validators and regression tests.
3. Bump the skill version and update changelog.
4. Update any affected orchestrator registry/capability/ownership references.
5. Validate the complete distribution inventory and aliases.
6. Publish/tag the GitHub release.
7. Replace/update only the affected Codex runtime skill(s), not every project.
8. Existing project artifacts remain project-scoped; re-VERIFY them only when changed assumptions/version boundaries require it.
