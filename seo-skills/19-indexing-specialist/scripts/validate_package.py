from pathlib import Path
import sys
CAN=['manifest', 'validation-brief', 'source-register', 'url-register', 'technical-access', 'indexability-check', 'sitemap-discovery', 'crawl-status', 'index-status', 'canonical-status', 'inspection-record', 'query-observations', 'target-query-map', 'ranking-observations', 'visibility-baseline', 'indexing-diagnosis', 'ranking-diagnosis', 'benchmark-status', 'action-plan', 'cross-skill-handoffs', 'change-control', 'verification-report', 'closeout'];REF=['boundaries-and-ownership.md', 'data-provenance.md', 'lifecycle-model.md', 'technical-access.md', 'indexability-method.md', 'sitemap-discovery.md', 'crawl-status.md', 'index-status.md', 'canonical-validation.md', 'url-inspection.md', 'site-query-limitations.md', 'query-validation.md', 'target-query-matching.md', 'ranking-validation.md', 'visibility-baseline.md', 'indexing-diagnosis.md', 'ranking-diagnosis.md', 'configurable-benchmarks.md', 'action-routing.md', 'canonical-outputs.md'];EX=['healthy-indexed-target-query', 'not-discovered', 'crawled-not-indexed', 'unexpected-noindex', 'robots-blocked', 'canonical-other', 'site-query-only', 'missing-gsc-data', 'unrelated-query', 'target-query-ranking', 'ranking-declining', 't7-benchmark', 't30-benchmark', 'technical-handoff', 'ownership-handoff', 'content-handoff', 'reuse', 'verify']
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