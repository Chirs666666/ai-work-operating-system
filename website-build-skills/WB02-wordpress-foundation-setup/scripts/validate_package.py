from pathlib import Path
import sys
REQ={'root': ['SKILL.md', 'README.md', 'VERSION', 'CHANGELOG.md', 'ACCEPTANCE.md'], 'references': ['environment-policy.md', 'access-risk-policy.md', 'theme-policy.md', 'editor-policy.md', 'design-token-policy.md', 'permalink-policy.md', 'plugin-policy.md', 'media-policy.md', 'role-policy.md', 'staging-policy.md', 'security-policy.md', 'backup-policy.md', 'performance-policy.md', 'seo-compatibility-policy.md', 'approval-policy.md', 'handoff-policy.md', 'verification-policy.md'], 'schemas': ['manifest.schema.json', 'wordpress-environment.schema.json', 'access-risk.schema.json', 'theme-strategy.schema.json', 'editor-strategy.schema.json', 'global-design-tokens.schema.json', 'permalink-baseline.schema.json', 'plugin-register.schema.json', 'plugin-conflict-audit.schema.json', 'media-policy.schema.json', 'role-policy.schema.json', 'staging-baseline.schema.json', 'security-baseline.schema.json', 'backup-baseline.schema.json', 'performance-foundation.schema.json', 'seo-compatibility.schema.json', 'foundation-change-plan.schema.json', 'approval-register.schema.json', 'verification-plan.schema.json', 'cross-skill-handoffs.schema.json', 'closeout.schema.json'], 'templates': ['manifest.yaml', 'wordpress-environment.yaml', 'access-risk.yaml', 'theme-strategy.yaml', 'editor-strategy.yaml', 'global-design-tokens.yaml', 'permalink-baseline.yaml', 'plugin-register.yaml', 'plugin-conflict-audit.yaml', 'media-policy.yaml', 'role-policy.yaml', 'staging-baseline.yaml', 'security-baseline.yaml', 'backup-baseline.yaml', 'performance-foundation.yaml', 'seo-compatibility.yaml', 'foundation-change-plan.yaml', 'approval-register.yaml', 'verification-plan.yaml', 'cross-skill-handoffs.yaml', 'closeout.yaml'], 'examples': ['new-site-staging', 'existing-site-audit', 'blocked-production-change']}
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
