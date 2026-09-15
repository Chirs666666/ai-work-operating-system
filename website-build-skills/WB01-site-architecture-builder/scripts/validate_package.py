from pathlib import Path
import sys
REQ={'root': ['SKILL.md', 'README.md', 'VERSION', 'CHANGELOG.md', 'ACCEPTANCE.md'], 'references': ['architecture-policy.md', 'page-family-policy.md', 'url-architecture-policy.md', 'navigation-policy.md', 'taxonomy-policy.md', 'ownership-policy.md', 'conflict-policy.md', 'migration-equity-policy.md', 'reuse-policy.md', 'change-control.md', 'handoff-policy.md', 'verification-policy.md'], 'schemas': ['manifest.schema.json', 'architecture-brief.schema.json', 'source-register.schema.json', 'site-scope.schema.json', 'page-family-register.schema.json', 'page-inventory.schema.json', 'hierarchy-map.schema.json', 'url-architecture.schema.json', 'navigation-map.schema.json', 'taxonomy-map.schema.json', 'entity-page-map.schema.json', 'keyword-page-input-check.schema.json', 'architecture-conflict-register.schema.json', 'missing-page-register.schema.json', 'build-priority.schema.json', 'cross-skill-handoffs.schema.json', 'verification-plan.schema.json', 'closeout.schema.json'], 'templates': ['manifest.yaml', 'architecture-brief.yaml', 'source-register.yaml', 'site-scope.yaml', 'page-family-register.yaml', 'page-inventory.yaml', 'hierarchy-map.yaml', 'url-architecture.yaml', 'navigation-map.yaml', 'taxonomy-map.yaml', 'entity-page-map.yaml', 'keyword-page-input-check.yaml', 'architecture-conflict-register.yaml', 'missing-page-register.yaml', 'build-priority.yaml', 'cross-skill-handoffs.yaml', 'verification-plan.yaml', 'closeout.yaml'], 'examples': ['new-industrial-site', 'existing-site-rebuild', 'ownership-conflict']}
def main(root):
    root=Path(root); errors=[]
    for f in REQ['root']:
        if not (root/f).exists(): errors.append('missing:'+f)
    for sec in ['references','schemas','templates']:
        for f in REQ[sec]:
            if not (root/sec/f).exists(): errors.append(f'missing {sec}:'+f)
    for d in REQ['examples']:
        if not (root/'examples'/d).is_dir(): errors.append('missing example:'+d)
    print('PACKAGE_ERRORS='+repr(errors))
    return 1 if errors else 0
if __name__=='__main__':
    raise SystemExit(main(sys.argv[1]))
