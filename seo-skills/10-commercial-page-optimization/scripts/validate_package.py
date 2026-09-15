from pathlib import Path
import sys, json
try:
 import yaml
except ImportError:
 yaml=None

EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL_OUTPUTS=['manifest', 'page-context', 'current-page-snapshot', 'performance-baseline', 'page-diagnosis', 'preserve-register', 'issue-register', 'optimization-strategy', 'section-change-plan', 'revised-page-copy', 'evidence-register', 'conversion-review', 'cross-skill-handoffs', 'batch-priority-queue', 'change-control', 'execution-handoff', 'verification-report', 'closeout']
REFERENCE_FILES=['boundaries-and-ownership.md', 'diagnosis-framework.md', 'performance-preservation.md', 'change-depth-model.md', 'commercial-page-optimization.md', 'evidence-and-claims.md', 'conversion-optimization.md', 'page-type-guidance.md', 'batch-audit.md', 'cross-skill-handoffs.md', 'change-control.md', 'verification-and-reuse.md', 'tool-routing.md', 'canonical-outputs.md']
REQUIRED_EXAMPLES=['reuse-healthy-page', 'minor-optimize', 'section-optimize', 'structural-refresh', 'rewrite-page', 'ownership-conflict', 'missing-performance', 'unsupported-claim', 'cross-skill-handoff', 'batch-audit', 'live-rewrite-approval', 'verify-mismatch']

def main():
 r=Path(sys.argv[1]); errors=[]
 for n in EXPECTED_ROOT:
  if not (r/n).exists(): errors.append("missing:"+n)
 for n in REFERENCE_FILES:
  if not (r/"references"/n).exists(): errors.append("missing reference:"+n)
 if not (r/"schemas"/"common.schema.json").exists(): errors.append("missing schema:common")
 for n in CANONICAL_OUTPUTS:
  if not (r/"schemas"/f"{n}.schema.json").exists(): errors.append("missing schema:"+n)
  if not (r/"templates"/f"{n}.yaml").exists(): errors.append("missing template:"+n)
 for n in REQUIRED_EXAMPLES:
  if not (r/"examples"/n).is_dir(): errors.append("missing example:"+n)
 for p in (r/"schemas").glob("*.json"):
  try: json.loads(p.read_text())
  except Exception as e: errors.append(f"bad json:{p.name}:{e}")
 if yaml:
  for p in (r/"templates").glob("*.yaml"):
   try: yaml.safe_load(p.read_text())
   except Exception as e: errors.append(f"bad yaml:{p.name}:{e}")
 print("VERIFICATION_ERRORS="+repr(errors))
 return 1 if errors else 0

if __name__=="__main__":
 raise SystemExit(main())
