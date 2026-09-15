from pathlib import Path
import sys
REQ={'root': ['SKILL.md', 'README.md', 'VERSION', 'CHANGELOG.md', 'ACCEPTANCE.md'], 'registry': ['system-registry.yaml', 'specialist-registry.yaml', 'subsystem-registry.yaml', 'capability-registry.yaml', 'ownership-registry.yaml', 'workflow-registry.yaml'], 'workflows': ['full-new-site.yaml', 'existing-site-rebuild.yaml', 'new-product-page-build.yaml', 'new-seo-article-publish.yaml', 'site-migration.yaml', 'post-launch-growth.yaml'], 'orchestration': ['master-router.yaml', 'dependency-policy.yaml', 'workstream-policy.yaml', 'artifact-discovery-policy.yaml', 'failure-recovery-policy.yaml', 'approval-policy.yaml', 'gate-policy.yaml', 'ownership-policy.yaml'], 'schemas': ['manifest.schema.json', 'project-state.schema.json', 'workstream-state.schema.json', 'artifact-registry.schema.json', 'routing-plan.schema.json', 'dependency-graph.schema.json', 'approval-register.schema.json', 'gate-register.schema.json', 'failure-register.schema.json', 'recovery-plan.schema.json', 'cross-layer-handoffs.schema.json', 'closeout.schema.json'], 'templates': ['manifest.yaml', 'project-state.yaml', 'workstream-state.yaml', 'artifact-registry.yaml', 'routing-plan.yaml', 'dependency-graph.yaml', 'approval-register.yaml', 'gate-register.yaml', 'failure-register.yaml', 'recovery-plan.yaml', 'cross-layer-handoffs.yaml', 'closeout.yaml'], 'examples': ['full-new-site-project', 'existing-product-page-project', 'cross-layer-recovery']};r=Path(sys.argv[1]);e=[]
for f in REQ['root']:
 if not (r/f).exists():e.append('missing:'+f)
for sec in ['registry','workflows','orchestration','schemas','templates']:
 for f in REQ[sec]:
  if not (r/sec/f).exists():e.append('missing '+sec+':'+f)
for d in REQ['examples']:
 if not (r/'examples'/d).is_dir():e.append('missing example:'+d)
print('PACKAGE_ERRORS='+repr(e));raise SystemExit(1 if e else 0)
