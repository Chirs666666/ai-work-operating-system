from pathlib import Path
import sys, json
try:
 import yaml
except ImportError: yaml=None
EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL_OUTPUTS=["manifest","page-context","metadata-inventory","existing-metadata-audit","performance-diagnosis","serp-research","claim-register","metadata-diagnosis","metadata-candidates","candidate-evaluation","recommended-metadata","h1-alignment-review","site-metadata-audit","change-control","execution-handoff","closeout"]
REFERENCE_FILES=["boundaries-and-ownership.md","metadata-diagnosis.md","performance-diagnosis.md","serp-research-policy.md","metadata-generation.md","candidate-evaluation.md","evidence-gated-claims.md","title-meta-length.md","h1-alignment.md","site-metadata-audit.md","serp-rewrite-awareness.md","tool-routing.md","change-control.md","verification-and-reuse.md","canonical-outputs.md"]
REQUIRED_EXAMPLES=["new-product-page","reuse-healthy-page","conditional-claim","missing-gsc","low-position-low-ctr","performance-opportunity","h1-misaligned","truncation-risk","serp-title-rewrite","draft-page-handoff","site-audit","unsupported-claim","ownership-conflict","live-page-approval","verify-mismatch"]
def main():
 r=Path(sys.argv[1]); errors=[]
 for n in EXPECTED_ROOT:
  if not (r/n).exists(): errors.append("missing:"+n)
 for n in REFERENCE_FILES:
  if not (r/"references"/n).exists(): errors.append("missing reference:"+n)
 if not (r/"schemas"/"common.schema.json").exists(): errors.append("missing schema:common")
 for n in CANONICAL_OUTPUTS:
  for folder,suf in [("schemas",".schema.json"),("templates",".yaml")]:
   p=r/folder/(n+suf)
   if not p.exists(): errors.append("missing "+folder+":"+p.name)
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
if __name__=="__main__": raise SystemExit(main())
