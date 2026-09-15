from pathlib import Path
import sys
CAN=['manifest', 'validation-brief', 'source-register', 'url-baseline', 'gsc-query-page', 'ranking-keywords', 'target-query-map', 'related-query-clusters', 'serp-validation', 'position-baseline', 'impression-trend', 'query-growth', 'keyword-growth', 'ranking-trend', 'intent-alignment', 'time-maturity', 'ranking-diagnosis', 'verdict', 'next-action', 'cross-skill-handoffs', 'verification-report', 'closeout'];REF=['boundaries-and-ownership.md', 'data-provenance.md', 'ranking-lifecycle.md', 'gsc-query-page.md', 'provider-semantics.md', 'target-query-matching.md', 'related-query-clustering.md', 'serp-validation.md', 'position-analysis.md', 'impression-trend.md', 'query-growth.md', 'keyword-growth.md', 'ranking-trend.md', 'intent-alignment.md', 'time-maturity.md', 'ranking-diagnosis.md', 'verdict-method.md', 'next-action-routing.md', 'comparison-windows.md', 'canonical-outputs.md'];EX=['healthy-target-growth', 'new-page-growing', 'new-page-one-impression', 'no-gsc-data', 'related-query-growth', 'unrelated-query-wrong-intent', 'target-not-detected', 'ranking-declining', 'noncomparable-window', 'semrush-vs-gsc', 'serp-intent-mismatch', 'stagnant-mature-page', 'index-health-unknown', 'content-handoff', 'commercial-handoff', 'ownership-handoff', 'monitor-action', 'reuse', 'verify']
def main():
 r=Path(sys.argv[1]);e=[]
 for x in ["SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md"]:
  if not (r/x).exists():e.append("missing:"+x)
 for x in REF:
  if not (r/"references"/x).exists():e.append("missing ref:"+x)
 if not (r/"schemas"/"common.schema.json").exists():e.append("missing common schema")
 for x in CAN:
  if not (r/"schemas"/f"{x}.schema.json").exists():e.append("missing schema:"+x)
  if not (r/"templates"/f"{x}.yaml").exists():e.append("missing template:"+x)
 for x in EX:
  if not (r/"examples"/x).is_dir():e.append("missing example:"+x)
 print("ERRORS="+repr(e));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())