from pathlib import Path
import sys
CAN=['manifest', 'analysis-brief', 'source-register', 'semrush-snapshot', 'organic-keywords', 'position-changes', 'keyword-growth', 'keyword-loss', 'top-pages', 'page-opportunities', 'organic-competitors', 'competitor-gap', 'keyword-gap', 'backlink-overview', 'backlink-gap', 'traffic-trend', 'serp-feature-opportunities', 'intent-analysis', 'country-device-context', 'opportunity-register', 'risk-register', 'priority-plan', 'cross-skill-handoffs', 'closeout'];REF=['boundaries-and-ownership.md', 'data-provenance.md', 'semrush-metric-semantics.md', 'snapshot-context.md', 'organic-research.md', 'position-changes.md', 'keyword-growth-loss.md', 'top-pages.md', 'page-opportunities.md', 'organic-competitors.md', 'competitor-gap.md', 'keyword-gap.md', 'backlink-overview.md', 'backlink-gap.md', 'traffic-trend.md', 'serp-features.md', 'keyword-intent.md', 'priority-method.md', 'handoff-routing.md', 'canonical-outputs.md'];EX=['organic-opportunity', 'position-gain', 'position-loss', 'keyword-growth', 'keyword-loss', 'top-page-opportunity', 'competitor-gap', 'keyword-gap', 'backlink-gap', 'serp-feature-opportunity', 'intent-mismatch', 'semrush-traffic-not-ga4', 'semrush-position-not-gsc', 'missing-keyword-not-google-absence', 'cross-country-noncomparable', 'cross-device-noncomparable', 'kd-not-go-no-go', 'authority-score-not-link-quality', 'ranking-handoff', 'ownership-handoff', 'content-handoff', 'commercial-handoff', 'backlink-handoff', 'reuse', 'verify']
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