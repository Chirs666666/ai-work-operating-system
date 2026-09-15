#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
errors=[]

def err(msg): errors.append(msg)

required_root={'SKILL.md','README.md','VERSION','CHANGELOG.md','references','schemas','templates','examples','scripts'}
for name in required_root:
    if not (ROOT/name).exists(): err(f'missing root item: {name}')

if (ROOT/'VERSION').exists() and (ROOT/'VERSION').read_text(encoding='utf-8').strip()!='1.0.0': err('VERSION must be 1.0.0')
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8') if (ROOT/'SKILL.md').exists() else ''
for h in ['Purpose','Trigger','Do Not Trigger','Inputs','Preconditions','Workflow','Tool Routing','Decision Rules','Quality Gates','Outputs','Handoff','Safety / Change Control']:
    if h not in skill: err(f'SKILL missing section: {h}')
for token in ['NEW_PAGE_LINKING','EXISTING_SITE_OPTIMIZATION','VERIFY','REFRESH_GRAPH','REUSE']:
    if token not in skill: err(f'SKILL missing mode: {token}')

refs=['boundaries-and-ownership.md','internal-link-graph.md','page-relationship-model.md','candidate-generation.md','link-decision-engine.md','anchor-strategy.md','placement-rules.md','orphan-underlinked-rules.md','topic-cluster-health.md','graph-freshness.md','tool-routing.md','change-control.md','verification-and-reuse.md','canonical-outputs.md']
for f in refs:
    if not (ROOT/'references'/f).exists(): err(f'missing reference: {f}')
reftext='\n'.join((ROOT/'references'/f).read_text(encoding='utf-8') for f in refs if (ROOT/'references'/f).exists())
for token in ['PARENT_CHILD','TOPIC_SUPPORT','COMMERCIAL_SUPPORT','APPLICATION_RELATION','PROOF_SUPPORT','DEEPER_LEARNING','CONVERSION_PATH','RELATED_CONTENT','SIBLING_COMPARISON','OWNERSHIP_CONFLICT']:
    if token not in reftext: err(f'missing relationship/ownership token: {token}')
for token in ['Semantic Relevance','Page Relationship','User Journey Value','Target Page Priority','Link Gap','Source Page Value','Placement Quality']:
    if token not in reftext: err(f'missing decision dimension: {token}')
for token in ['PRIORITY_HIGH','PRIORITY_MEDIUM','PRIORITY_LOW','REJECT','REUSE_EXISTING','IMPROVE_EXISTING','ADD_NEW','NO_ACTION']:
    if token not in reftext: err(f'missing decision token: {token}')
for token in ['EXACT_DESCRIPTIVE','PARTIAL_DESCRIPTIVE','ENTITY_PRODUCT','CONTEXTUAL','ACTION']:
    if token not in reftext: err(f'missing anchor type: {token}')
for token in ['BODY_CONTEXTUAL','NAVIGATION','BREADCRUMB','RELATED_CONTENT','CTA','TABLE','FAQ','CARD','FOOTER']:
    if token not in reftext: err(f'missing placement type: {token}')
for token in ['STRONG','ADEQUATE','WEAK','FRAGMENTED','UNKNOWN','USER_DATA','API_DATA','PUBLIC_RESEARCH','VERIFIED','OBSERVED','INFERRED','CONFLICTING','CURRENT','PARTIALLY_STALE','STALE','FULL_BUILD','FULL_REFRESH','INCREMENTAL_UPDATE','GRAPH_REUSE','LINK_REUSE','PLAN_REUSE','SINGLE_PAGE','SMALL_BATCH','BULK','SITEWIDE','WAITING_APPROVAL']:
    if token not in reftext+skill: err(f'missing required vocabulary: {token}')

schema_names=['common','manifest','site-url-inventory','internal-link-graph','graph-freshness','page-relationship-map','existing-link-audit','link-candidates','link-decisions','outgoing-link-plan','incoming-link-opportunities','anchor-placement-plan','topic-cluster-health','orphan-underlinked-report','ownership-conflicts','technical-link-issues','change-control','execution-handoff','closeout']
for n in schema_names:
    if not (ROOT/'schemas'/f'{n}.schema.json').exists(): err(f'missing schema: {n}.schema.json')
for p in sorted((ROOT/'schemas').glob('*.json')):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: err(f'invalid json {p.name}: {e}')

canonical=['manifest','site-url-inventory','internal-link-graph','graph-freshness','page-relationship-map','existing-link-audit','link-candidates','link-decisions','outgoing-link-plan','incoming-link-opportunities','anchor-placement-plan','topic-cluster-health','orphan-underlinked-report','ownership-conflicts','technical-link-issues','change-control','execution-handoff','closeout']
actual={p.stem for p in (ROOT/'templates').glob('*.yaml')}
if actual and actual != set(canonical): err(f'template set mismatch: {sorted(actual ^ set(canonical))}')
for n in canonical:
    if not (ROOT/'templates'/f'{n}.yaml').exists(): err(f'missing template: {n}.yaml')

try:
    import yaml
except Exception:
    yaml=None
try:
    import jsonschema
except Exception:
    jsonschema=None

if yaml and jsonschema:
    from jsonschema import Draft202012Validator
    for p in sorted((ROOT/'schemas').glob('*.schema.json')):
        try: Draft202012Validator.check_schema(json.loads(p.read_text(encoding='utf-8')))
        except Exception as e: err(f'invalid schema {p.name}: {e}')
    for n in canonical:
        tp=ROOT/'templates'/f'{n}.yaml'; sp=ROOT/'schemas'/f'{n}.schema.json'
        if tp.exists() and sp.exists():
            try:
                data=yaml.safe_load(tp.read_text(encoding='utf-8'))
                schema=json.loads(sp.read_text(encoding='utf-8'))
                jsonschema.validate(data,schema)
            except Exception as e: err(f'template schema mismatch {n}: {e}')
else:
    print('NOTE: PyYAML/jsonschema unavailable; deep YAML/schema validation skipped')

# safety/documentation invariants
alltext=skill+'\n'+reftext
if re.search(r'\b(?:per|每)\s*1000\s*(?:words|字).*\b\d+\s*[-–]\s*\d+', alltext, re.I): err('fixed internal-link density rule detected')
if re.search(r'exact\s*match\s*\d+\s*%', alltext, re.I): err('fixed exact-match anchor ratio detected')
if 'must not directly modify WordPress' not in alltext and 'does not directly modify WordPress' not in alltext: err('direct WordPress mutation prohibition missing')

if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('PASS')
