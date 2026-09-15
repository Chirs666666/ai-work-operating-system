from pathlib import Path
import sys
r=Path(sys.argv[1]); errors=[]
seo=['01-company-knowledge-base', '02-business-model-analysis', '03-product-keyword-research', '04-page-planning-ui', '05-product-copywriting', '06-content-writing-optimization', '07-wordpress-page-builder-publisher', '08-internal-linking-architecture', '09-seo-metadata', '10-commercial-page-optimization', '11-backlink-building', '12-technical-seo-audit-fix', '13-site-data-analysis', '15-existing-site-inventory', '16-calculator-tool-builder', '17-image-generation', '18-google-ads-operations', '19-indexing-specialist', '20-ranking-validation', '21-page-speed-optimization', '22-semrush-analysis', '23-old-article-optimization', '24-geo-optimization', '25-keyword-page-mapping']; wb=['WB01-site-architecture-builder', 'WB02-wordpress-foundation-setup', 'WB03-global-components-builder', 'WB04-website-page-assembly', 'WB05-tracking-search-setup', 'WB06-infrastructure-performance', 'WB07-pre-launch-qa', 'WB08-deployment-launch']
for f in ['README.md','AGENTS.md','VERSION','skill-inventory.yaml']:
    if not (r/f).exists(): errors.append('missing root:'+f)
for p in ['system/seo-workflow-system','system/website-build-layer']:
    if not (r/p/'SKILL.md').exists(): errors.append('missing system:'+p)
for n in seo:
    if not (r/'seo-skills'/n/'SKILL.md').exists(): errors.append('missing seo:'+n)
for n in wb:
    if not (r/'website-build-skills'/n/'SKILL.md').exists(): errors.append('missing wb:'+n)
if any(p.name.startswith('14-') for p in (r/'seo-skills').glob('*')): errors.append('standalone Skill 14 forbidden')
for f in ['AGENTS.md','README.md']:
    if not (r/'project-template'/f).exists(): errors.append('missing project template:'+f)
for f in ['github-setup.md','codex-installation.md','how-to-use.md','skill-routing-map.md','update-workflow.md']:
    if not (r/'docs'/f).exists(): errors.append('missing doc:'+f)
print('PACKAGE_ERRORS='+repr(errors)); raise SystemExit(1 if errors else 0)
