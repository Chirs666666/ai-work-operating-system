from pathlib import Path
import sys
CAN=['manifest', 'geo-brief', 'source-register', 'entity-register', 'entity-relationship', 'topic-intent', 'answerability-audit', 'extractability-audit', 'claim-register', 'evidence-register', 'claim-evidence-map', 'attribution-audit', 'technical-fact-audit', 'content-structure-audit', 'citation-readiness', 'brand-topic-association', 'structured-data-alignment', 'ai-query-set', 'ai-visibility-observations', 'geo-gap-register', 'geo-priority-plan', 'cross-skill-handoffs', 'verification-plan', 'closeout'];REF=['boundaries-and-ownership.md', 'data-provenance.md', 'entity-clarity.md', 'entity-relationships.md', 'answerability.md', 'extractability.md', 'claim-taxonomy.md', 'evidence-taxonomy.md', 'claim-evidence-policy.md', 'attribution.md', 'technical-facts.md', 'citation-readiness.md', 'brand-topic-association.md', 'structured-data-alignment.md', 'ai-visibility-method.md', 'query-set-design.md', 'seo-preservation.md', 'priority-method.md', 'handoff-routing.md', 'canonical-outputs.md'];EX=['entity-clear', 'entity-relationship', 'answerable-page', 'extractable-page', 'supported-specification', 'unsupported-marketing-claim', 'unsupported-manufacturer-claim', 'evidence-proximity', 'citation-ready', 'structured-data-aligned', 'schema-not-guarantee', 'single-ai-mention', 'no-ai-mention-not-seo-failure', 'repeated-ai-observations', 'competitor-dominant', 'seo-preservation', 'invented-statistic-blocked', 'content-handoff', 'commercial-handoff', 'technical-handoff', 'internal-link-handoff', 'authority-handoff', 'ranking-handoff', 'ownership-handoff', 'reuse', 'verify']
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