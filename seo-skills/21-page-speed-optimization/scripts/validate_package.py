from pathlib import Path
import sys
CAN=['manifest', 'performance-brief', 'source-register', 'test-environment', 'cwv-baseline', 'lab-baseline', 'ttfb-analysis', 'lcp-analysis', 'inp-analysis', 'cls-analysis', 'image-analysis', 'js-analysis', 'css-analysis', 'font-analysis', 'cache-analysis', 'third-party-analysis', 'bottleneck-register', 'priority-plan', 'backup-change-plan', 'optimization-actions', 'retest-results', 'before-after-report', 'cross-skill-handoffs', 'closeout'];REF=['boundaries-and-ownership.md', 'data-provenance.md', 'field-vs-lab.md', 'core-web-vitals.md', 'ttfb-diagnosis.md', 'lcp-diagnosis.md', 'inp-diagnosis.md', 'cls-diagnosis.md', 'image-optimization.md', 'javascript-optimization.md', 'css-optimization.md', 'font-optimization.md', 'cache-cdn.md', 'third-party-scripts.md', 'wordpress-performance.md', 'priority-model.md', 'backup-change-control.md', 'retest-comparability.md', 'functional-regression.md', 'canonical-outputs.md'];EX=['healthy-field-and-lab', 'high-lighthouse-poor-field', 'missing-field-data', 'lcp-image-bottleneck', 'ttfb-origin-bottleneck', 'inp-third-party-js', 'cls-image-dimensions', 'risky-js-delay', 'risky-plugin-change', 'no-backup-risky-change', 'mobile-vs-desktop-compare', 'lab-improved-field-pending', 'functionality-regressed', 'wordpress-cache-plan', 'image-optimization-plan', 'third-party-plan', 'retest-improved', 'retest-unchanged', 'reuse', 'verify']
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