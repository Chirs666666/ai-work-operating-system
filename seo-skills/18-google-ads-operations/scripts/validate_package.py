from pathlib import Path
import sys
CAN=['manifest', 'ads-brief', 'source-register', 'account-readiness', 'conversion-map', 'tracking-readiness', 'market-targeting', 'keyword-plan', 'negative-keyword-plan', 'landing-page-map', 'campaign-architecture', 'ad-group-plan', 'bidding-strategy', 'budget-plan', 'ad-copy', 'ad-assets', 'prelaunch-qa', 'search-term-review', 'performance-review', 'optimization-plan', 'experiment-plan', 'change-control', 'cross-skill-handoffs', 'closeout'];REF=['boundaries-and-ownership.md', 'data-provenance.md', 'b2b-search-ads-strategy.md', 'conversion-definition.md', 'tracking-readiness.md', 'keyword-intent.md', 'match-types.md', 'negative-keywords.md', 'landing-page-gate.md', 'campaign-architecture.md', 'ad-copy-evidence.md', 'targeting.md', 'bidding-strategy.md', 'budget-planning.md', 'prelaunch-qa.md', 'search-term-review.md', 'optimization-method.md', 'experiments.md', 'change-control.md', 'canonical-outputs.md'];EX=['verified-search-campaign', 'broken-tracking', 'unverified-tracking-zero-conversions', 'landing-page-mismatch', 'unsupported-ad-claim', 'budget-increase', 'campaign-enable', 'bulk-negative-change', 'missing-cpc', 'search-term-review', 'negative-keyword-review', 'bidding-insufficient-data', 'conversion-map', 'market-targeting', 'experiment', 'reuse', 'verify']
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