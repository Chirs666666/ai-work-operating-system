from pathlib import Path
import sys, yaml

HARD=["search_intent_alignment","url_ownership_alignment","accuracy_evidence"]

def load(p):
 return yaml.safe_load(p.read_text()) or {}

def main():
 root=Path(sys.argv[1]); errors=[]
 for d in [p for p in root.iterdir() if p.is_dir()]:
  files={p.name:load(p) for p in d.glob("*.yaml")}
  claims={c["claim_id"]:c for c in files.get("claim-register.yaml",{}).get("claims",[])}
  evals={e["candidate_id"]:e for e in files.get("candidate-evaluation.yaml",{}).get("evaluations",[])}
  cands=files.get("metadata-candidates.yaml",{}).get("candidates",[])
  ctx=files.get("metadata-candidates.yaml",{}).get("decision_context")
  if ctx in ("GENERATE","REWRITE") and not 2 <= len(cands) <= 3:
   errors.append(f"{d.name}: active generation requires 2-3 candidates")
  for c in cands:
   e=evals.get(c["candidate_id"],{})
   if e.get("outcome")=="RECOMMENDED":
    for h in HARD:
     if e.get(h)=="FAIL": errors.append(f"{d.name}:{c['candidate_id']}: recommended hard gate FAIL:{h}")
    for cid in c.get("claim_ids",[]):
     if claims.get(cid,{}).get("state") in ("UNSUPPORTED","CONFLICTING"):
      errors.append(f"{d.name}:{c['candidate_id']}: recommended invalid claim:{cid}")
  diag=files.get("metadata-diagnosis.yaml",{})
  if diag.get("state")=="OWNERSHIP_CONFLICT" and diag.get("action")!="BLOCK_FOR_OWNERSHIP":
   errors.append(f"{d.name}: ownership conflict must BLOCK_FOR_OWNERSHIP")
  perf=files.get("performance-diagnosis.yaml",{})
  if perf.get("availability")=="UNKNOWN":
   for k in ("impressions","clicks","ctr","average_position"):
    if perf.get(k)==0: errors.append(f"{d.name}: UNKNOWN performance fabricated zero:{k}")
  h1=files.get("h1-alignment-review.yaml",{})
  if h1.get("status")=="MISALIGNED" and h1.get("execution_allowed") is True:
   errors.append(f"{d.name}: H1 misalignment cannot be executable")
  cc=files.get("change-control.yaml",{})
  if cc.get("risk_class") in ("LIVE_PERFORMANCE_SENSITIVE","HIGH_RISK_REWRITE") and cc.get("approval_required") is not True:
   errors.append(f"{d.name}: live high-risk change requires approval")
  hand=files.get("execution-handoff.yaml",{})
  if hand and hand.get("owner")!="07-wordpress-page-builder-publisher":
   errors.append(f"{d.name}: execution owner must be 07")
  ver=files.get("verification.yaml",{})
  if ver and ver.get("recommended_title")!=ver.get("configured_title") and ver.get("overall")=="VERIFIED":
   errors.append(f"{d.name}: mismatch cannot be VERIFIED")
  obs=files.get("observation.yaml",{})
  if files.get("serp-research.yaml",{}).get("serp_rewrite_observed") and obs.get("configured_metadata_failure") is True:
   errors.append(f"{d.name}: SERP rewrite cannot automatically mean configured failure")
 print("EXAMPLE_ERRORS="+repr(errors))
 return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main())
