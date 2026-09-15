from pathlib import Path
import yaml,sys
def load(p):return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]);e=[]
 for d in [x for x in root.iterdir() if x.is_dir()]:
  f={p.name:load(p) for p in d.glob("*.yaml")}
  tr=f.get("tracking-readiness.yaml",{})
  qa=f.get("prelaunch-qa.yaml",{})
  if tr.get("status") in ("TRACKING_BROKEN","TRACKING_UNVERIFIED") and qa.get("launch_ready") is True:
   e.append(f"{d.name}: broken/unverified tracking cannot be launch-ready")
  lp=f.get("landing-page-map.yaml",{})
  if any(x.get("alignment")=="FAIL" for x in lp.get("mappings",[])) and qa.get("launch_ready") is True:
   e.append(f"{d.name}: landing-page mismatch cannot launch")
  ac=f.get("ad-copy.yaml",{})
  if any(x.get("unsupported_claims") for x in ac.get("ads",[])):
   if qa.get("claims") not in ("FAIL","BLOCK") or qa.get("launch_ready") is True:
    e.append(f"{d.name}: unsupported claims must fail/block launch")
  cc=f.get("change-control.yaml",{})
  if cc.get("live_change") is True:
   if cc.get("approval_required") is not True:e.append(f"{d.name}: live change requires approval")
   if cc.get("approval_status")!="APPROVED" and cc.get("execute_allowed") is True:e.append(f"{d.name}: live change cannot execute without approval")
  bp=f.get("budget-plan.yaml",{})
  if bp.get("metric_status")=="UNKNOWN":
   for k in ("cpc","cvr","cpa"):
    if bp.get(k)==0:e.append(f"{d.name}: unknown {k} cannot be converted to 0")
  pr=f.get("performance-review.yaml",{})
  if pr.get("tracking_status") in ("TRACKING_BROKEN","TRACKING_UNVERIFIED"):
   if pr.get("confidence")!="INSUFFICIENT":e.append(f"{d.name}: unverified tracking requires insufficient confidence")
   text=pr.get("interpretation","").lower()
   if "campaign failed" in text or "ads failed" in text:e.append(f"{d.name}: cannot diagnose failure from unverified tracking")
 print("EXAMPLE_ERRORS="+repr(e));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())