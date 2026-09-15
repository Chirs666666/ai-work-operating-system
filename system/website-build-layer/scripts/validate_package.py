from pathlib import Path
import sys
REQ={'root': ['SKILL.md', 'README.md', 'VERSION', 'CHANGELOG.md', 'ACCEPTANCE.md'], 'references': ['routing-policy.md', 'reuse-policy.md', 'dependency-policy.md', 'artifact-policy.md', 'approval-policy.md', 'gate-policy.md', 'failure-recovery-policy.md', 'ownership-policy.md', 'state-policy.md', 'workflow-policy.md', 'change-control-policy.md', 'seo-system-handoff-policy.md', 'verification-policy.md'], 'registry': ['build-skill-registry.yaml', 'capability-registry.yaml', 'workflow-registry.yaml'], 'workflows': ['new-site-build.yaml', 'existing-site-rebuild.yaml', 'new-page-build.yaml', 'site-expansion.yaml', 'migration-launch.yaml', 'build-fix-relaunch.yaml'], 'schemas': ['manifest.schema.json', 'project-build-state.schema.json', 'artifact-registry.schema.json', 'dependency-graph.schema.json', 'routing-plan.schema.json', 'approval-register.schema.json', 'gate-register.schema.json', 'failure-register.schema.json', 'recovery-plan.schema.json', 'workflow-run.schema.json', 'cross-system-handoffs.schema.json', 'closeout.schema.json'], 'templates': ['manifest.yaml', 'project-build-state.yaml', 'artifact-registry.yaml', 'dependency-graph.yaml', 'routing-plan.yaml', 'approval-register.yaml', 'gate-register.yaml', 'failure-register.yaml', 'recovery-plan.yaml', 'workflow-run.yaml', 'cross-system-handoffs.yaml', 'closeout.yaml'], 'examples': ['new-site-project', 'existing-site-new-page', 'blocked-recovery']};r=Path(sys.argv[1]);e=[]
for f in REQ['root']:
 if not (r/f).exists():e.append('missing:'+f)
for sec in ['references','registry','workflows','schemas','templates']:
 for f in REQ[sec]:
  if not (r/sec/f).exists():e.append('missing '+sec+':'+f)
for d in REQ['examples']:
 if not (r/'examples'/d).is_dir():e.append('missing example:'+d)
print('PACKAGE_ERRORS='+repr(e));raise SystemExit(1 if e else 0)
