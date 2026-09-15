#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
EX=ROOT/'examples'
errors=[]

def err(x): errors.append(x)
try:
    import yaml
except Exception as e:
    print('FAIL\n- PyYAML required for example validation:',e); sys.exit(1)
try:
    import jsonschema
except Exception as e:
    print('FAIL\n- jsonschema required for example validation:',e); sys.exit(1)

required_dirs=['new-page-final','reuse-existing-link','ownership-conflict','missing-gsc-warning','orphan-sitemap-only','breadcrumb-underlinked','technical-404-handoff','live-replace-approval','stale-graph-refresh','verify-execution-mismatch']
for d in required_dirs:
    if not (EX/d).is_dir(): err(f'missing example dir: {d}')

for p in sorted(EX.glob('*/*.yaml')):
    sp=ROOT/'schemas'/f'{p.stem}.schema.json'
    if not sp.exists():
        err(f'no matching schema for {p.relative_to(ROOT)}'); continue
    try:
        data=yaml.safe_load(p.read_text(encoding='utf-8'))
        schema=json.loads(sp.read_text(encoding='utf-8'))
        jsonschema.validate(data,schema)
    except Exception as e: err(f'schema fail {p.relative_to(ROOT)}: {e}')

def load(d,n):
    p=EX/d/f'{n}.yaml'
    if not p.exists(): err(f'{d}: missing {n}.yaml'); return None
    return yaml.safe_load(p.read_text(encoding='utf-8'))

# new-page-final
D=load('new-page-final','link-decisions'); O=load('new-page-final','outgoing-link-plan'); I=load('new-page-final','incoming-link-opportunities'); A=load('new-page-final','anchor-placement-plan'); H=load('new-page-final','execution-handoff')
if D:
    highs=[x for x in D['decisions'] if x['priority']=='PRIORITY_HIGH']
    if not highs: err('new-page-final: needs PRIORITY_HIGH decision')
    for x in highs:
        if x['dimensions']['semantic_relevance']!='HIGH' or x['dimensions']['placement_quality']!='HIGH': err('new-page-final: high priority violates gating')
if O and not O['links']: err('new-page-final: outgoing must not be empty')
if I and not I['links']: err('new-page-final: incoming must not be empty')
if H and H['owner']!='07-wordpress-page-builder-publisher': err('new-page-final: wrong handoff owner')

# reuse
D=load('reuse-existing-link','link-decisions'); C=load('reuse-existing-link','closeout')
if D and not any(x['action']=='REUSE_EXISTING' for x in D['decisions']): err('reuse-existing-link: REUSE_EXISTING missing')
if C and C['g08_status']!='REUSE': err('reuse-existing-link: closeout must be REUSE')

# ownership
C=load('ownership-conflict','closeout'); X=load('ownership-conflict','ownership-conflicts')
if C and C['g08_status']!='BLOCK': err('ownership-conflict: must BLOCK')
if X and X['handoff_owner']!='25-keyword-page-mapping': err('ownership-conflict: must handoff 25')

# missing gsc
C=load('missing-gsc-warning','closeout'); U=load('missing-gsc-warning','site-url-inventory')
if C and C['g08_status']!='WARN': err('missing-gsc-warning: must WARN')
if U:
    for p in U['pages']:
        if p.get('traffic')==0: err('missing-gsc-warning: missing traffic must not be 0')

# orphan
R=load('orphan-sitemap-only','orphan-underlinked-report')
if R and not any(x['classification']=='ORPHAN_PAGE' and x.get('sitemap_present') is True and x.get('html_internal_entries')==0 for x in R['pages']): err('orphan-sitemap-only: incorrect orphan classification')
R=load('breadcrumb-underlinked','orphan-underlinked-report')
if R and any(x['classification']=='ORPHAN_PAGE' for x in R['pages']): err('breadcrumb-underlinked: breadcrumb page must not be orphan')

# 404 handoff
T=load('technical-404-handoff','technical-link-issues'); D=load('technical-404-handoff','link-decisions')
if T and T['handoff_owner']!='12-technical-seo-audit-fix': err('technical-404-handoff: wrong handoff owner')
if D and any(x['priority']!='REJECT' for x in D['decisions']): err('technical-404-handoff: 404 candidate must be REJECT')

# approval
CC=load('live-replace-approval','change-control'); C=load('live-replace-approval','closeout')
if CC:
    for x in CC['changes']:
        if x['change_class'] in ('REPLACE','REMOVE_RECOMMENDATION') and not x['approval_required']: err('live-replace-approval: high impact needs approval')
if C and C['g08_status']!='WAITING_APPROVAL': err('live-replace-approval: must WAITING_APPROVAL')

# stale graph
G=load('stale-graph-refresh','graph-freshness')
if G and G['state']=='STALE' and G['recommended_operation']=='REUSE': err('stale-graph-refresh: stale graph cannot blind REUSE')

# verify mismatch
C=load('verify-execution-mismatch','closeout')
if C and C.get('verification_result')!='MISMATCH': err('verify-execution-mismatch: must MISMATCH')

# universal high-priority gating, no zeros in inventory examples
for p in EX.glob('*/link-decisions.yaml'):
    data=yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    for x in data.get('decisions',[]):
        if x.get('priority')=='PRIORITY_HIGH':
            dims=x.get('dimensions',{})
            if dims.get('semantic_relevance')=='LOW' or dims.get('placement_quality')=='LOW': err(f'{p.parent.name}: invalid PRIORITY_HIGH gating')
for p in EX.glob('*/site-url-inventory.yaml'):
    data=yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    for x in data.get('pages',[]):
        if x.get('traffic')==0 and x.get('traffic_source') in (None,'MISSING','UNKNOWN'): err(f'{p.parent.name}: suspicious zero missing metric')

if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('PASS')
