from pathlib import Path
import sys,json
try: import yaml
except ImportError: yaml=None
EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL=['manifest', 'inventory-scope', 'source-register', 'url-discovery', 'url-normalization', 'page-classification', 'indexability-inventory', 'performance-baseline', 'query-keyword-signals', 'backlink-asset-signals', 'content-state', 'technical-signals', 'asset-value', 'preservation-register', 'action-classification', 'priority-queue', 'ownership-conflicts', 'cross-skill-handoffs', 'change-control', 'inventory-summary', 'closeout']
REFS=['boundaries-and-ownership.md', 'data-provenance.md', 'url-discovery-and-normalization.md', 'page-classification.md', 'indexability-model.md', 'performance-baseline.md', 'query-keyword-signals.md', 'backlink-asset-value.md', 'content-state.md', 'technical-signals.md', 'asset-value-and-preservation.md', 'action-classification.md', 'priority-framework.md', 'tool-routing.md', 'canonical-outputs.md']
EXAMPLES=['high-value-asset', 'low-value-page', 'duplicate-variant', 'ranking-protection', 'backlink-protection', 'merge-candidate', 'redirect-candidate', 'noindex-candidate', 'ownership-conflict', 'commercial-handoff', 'article-handoff', 'technical-handoff', 'missing-data', 'provider-conflict', 'reuse', 'verify']
def main():
 r=Path(sys.argv[1]); e=[]
 for x in EXPECTED_ROOT:
  if not (r/x).exists(): e.append("missing:"+x)
 for x in REFS:
  if not (r/"references"/x).exists(): e.append("missing reference:"+x)
 if not (r/"schemas"/"common.schema.json").exists(): e.append("missing schema:common")
 for x in CANONICAL:
  if not (r/"schemas"/f"{x}.schema.json").exists(): e.append("missing schema:"+x)
  if not (r/"templates"/f"{x}.yaml").exists(): e.append("missing template:"+x)
 for x in EXAMPLES:
  if not (r/"examples"/x).is_dir(): e.append("missing example:"+x)
 print("VERIFICATION_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
