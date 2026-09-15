from pathlib import Path
import sys,json
try: import yaml
except ImportError: yaml=None
EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL=['manifest', 'analysis-brief', 'source-register', 'source-quality', 'period-definition', 'site-kpi-summary', 'search-performance', 'landing-page-performance', 'query-performance', 'query-page-matrix', 'conversion-engagement', 'keyword-visibility', 'competitor-visibility', 'backlink-trend-context', 'anomaly-register', 'diagnosis-register', 'opportunity-register', 'priority-action-plan', 'cross-skill-handoffs', 'monitoring-plan', 'closeout']
REFS=['boundaries-and-ownership.md', 'data-provenance.md', 'source-quality.md', 'period-comparison.md', 'gsc-analysis.md', 'ga4-analysis.md', 'semrush-ahrefs-analysis.md', 'query-page-analysis.md', 'diagnosis-and-causality.md', 'anomaly-detection.md', 'opportunity-framework.md', 'action-routing.md', 'monitoring-policy.md', 'tool-routing.md', 'canonical-outputs.md']
EXAMPLES=['gsc-growth', 'gsc-decline', 'ctr-anomaly', 'wrong-page-ranking', 'cannibalization-signal', 'ga4-conversion-decline', 'provider-conflict', 'missing-metrics', 'competitor-visibility', 'backlink-trend', 'tracking-break', 'quick-win', 'technical-handoff', 'content-handoff', 'commercial-page-handoff', 'monitor-reuse']
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
 for p in (r/"schemas").glob("*.json"):
  try: json.loads(p.read_text())
  except Exception as z: e.append(f"bad json:{p.name}:{z}")
 if yaml:
  for p in (r/"templates").glob("*.yaml"):
   try: yaml.safe_load(p.read_text())
   except Exception as z: e.append(f"bad yaml:{p.name}:{z}")
 print("VERIFICATION_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
