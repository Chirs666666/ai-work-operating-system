from pathlib import Path
import sys
EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL=['manifest', 'calculator-brief', 'source-register', 'formula-evidence', 'formula-contract', 'variable-spec', 'unit-system', 'assumptions-boundaries', 'edge-case-register', 'test-vectors', 'test-results', 'calculation-engine-contract', 'error-handling-contract', 'frontend-contract', 'explanatory-content-contract', 'seo-page-requirements', 'security-safety-review', 'change-control', 'cross-skill-handoffs', 'implementation-handoff', 'verification-report', 'closeout']
REFS=['boundaries-and-ownership.md', 'data-provenance.md', 'calculator-opportunity.md', 'formula-evidence-policy.md', 'formula-contract.md', 'variable-and-unit-model.md', 'assumptions-and-boundaries.md', 'edge-case-design.md', 'test-strategy.md', 'calculation-engine.md', 'error-handling.md', 'frontend-contract.md', 'explanatory-content.md', 'seo-tool-page.md', 'change-control.md', 'canonical-outputs.md']
EXAMPLES=['bend-allowance', 'bend-radius', 'cnc-cycle-time', 'material-weight', 'unit-conversion', 'missing-evidence', 'conflicting-formula', 'failed-tests', 'invalid-geometry', 'unit-equivalence', 'formula-change', 'frontend-contract', 'commercial-handoff', 'informational-handoff', 'reuse', 'verify']
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
