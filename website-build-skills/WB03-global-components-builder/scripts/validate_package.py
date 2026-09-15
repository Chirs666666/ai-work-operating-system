from pathlib import Path
import sys
REQ={'root': ['SKILL.md', 'README.md', 'VERSION', 'CHANGELOG.md', 'ACCEPTANCE.md'], 'references': ['component-policy.md', 'architecture-alignment.md', 'design-token-alignment.md', 'header-policy.md', 'navigation-policy.md', 'mobile-navigation-policy.md', 'footer-policy.md', 'breadcrumb-policy.md', 'cta-policy.md', 'form-policy.md', 'reusable-pattern-policy.md', 'system-component-policy.md', 'responsive-policy.md', 'accessibility-policy.md', 'ownership-policy.md', 'wordpress-implementation-policy.md', 'approval-policy.md', 'handoff-policy.md', 'verification-policy.md'], 'schemas': ['manifest.schema.json', 'component-inventory.schema.json', 'component-ownership.schema.json', 'header-spec.schema.json', 'navigation-spec.schema.json', 'mobile-navigation-spec.schema.json', 'footer-spec.schema.json', 'breadcrumb-spec.schema.json', 'global-cta-register.schema.json', 'form-register.schema.json', 'reusable-pattern-register.schema.json', 'system-component-register.schema.json', 'responsive-rules.schema.json', 'accessibility-check.schema.json', 'design-token-alignment.schema.json', 'architecture-alignment.schema.json', 'wordpress-component-plan.schema.json', 'approval-register.schema.json', 'verification-plan.schema.json', 'cross-skill-handoffs.schema.json', 'closeout.schema.json'], 'templates': ['manifest.yaml', 'component-inventory.yaml', 'component-ownership.yaml', 'header-spec.yaml', 'navigation-spec.yaml', 'mobile-navigation-spec.yaml', 'footer-spec.yaml', 'breadcrumb-spec.yaml', 'global-cta-register.yaml', 'form-register.yaml', 'reusable-pattern-register.yaml', 'system-component-register.yaml', 'responsive-rules.yaml', 'accessibility-check.yaml', 'design-token-alignment.yaml', 'architecture-alignment.yaml', 'wordpress-component-plan.yaml', 'approval-register.yaml', 'verification-plan.yaml', 'cross-skill-handoffs.yaml', 'closeout.yaml'], 'examples': ['new-industrial-site', 'existing-site-refresh', 'blocked-component-plan']}
r=Path(sys.argv[1]); e=[]
for f in REQ['root']:
    if not (r/f).exists(): e.append('missing:'+f)
for sec in ['references','schemas','templates']:
    for f in REQ[sec]:
        if not (r/sec/f).exists(): e.append('missing '+sec+':'+f)
for d in REQ['examples']:
    if not (r/'examples'/d).is_dir(): e.append('missing example:'+d)
print('PACKAGE_ERRORS='+repr(e)); raise SystemExit(1 if e else 0)
