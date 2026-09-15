from pathlib import Path
import sys
CAN=['manifest', 'optimization-brief', 'source-register', 'article-baseline', 'historical-performance', 'query-performance', 'keyword-ownership', 'serp-intent', 'freshness-audit', 'content-gap', 'technical-depth', 'trust-evidence', 'internal-link-audit', 'backlink-equity', 'conversion-audit', 'cannibalization-check', 'preservation-register', 'change-register', 'article-diagnosis', 'priority-score', 'optimization-decision', 'cross-skill-handoffs', 'verification-plan', 'closeout'];REF=['boundaries-and-ownership.md', 'data-provenance.md', 'decline-diagnosis.md', 'historical-equity.md', 'query-performance.md', 'serp-intent.md', 'freshness-method.md', 'content-gap.md', 'technical-depth.md', 'trust-evidence.md', 'internal-links.md', 'backlink-equity.md', 'conversion-audit.md', 'cannibalization.md', 'preservation-policy.md', 'change-policy.md', 'priority-method.md', 'decision-method.md', 'handoff-routing.md', 'canonical-outputs.md'];EX=['healthy-keep', 'growing-monitor', 'ranking-drop-recovery', 'traffic-drop-not-rewrite', 'old-not-auto-update', 'seasonal-decline', 'ctr-weak-metadata', 'intent-shift', 'content-gap-expand', 'outdated-refresh', 'thin-rewrite', 'similar-keyword-no-merge', 'confirmed-merge-candidate', 'semrush-missing-not-no-ranking', 'preserve-ranking-section', 'preserve-backlinked-url', 'internal-link-handoff', 'metadata-handoff', 'content-handoff', 'ownership-handoff', 'ranking-handoff', 'authority-handoff', 'technical-block', 'reuse', 'verify']
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