from pathlib import Path
import sys,yaml
def load(p): return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]); e=[]
 for d in [p for p in root.iterdir() if p.is_dir()]:
  f={p.name:load(p) for p in d.glob("*.yaml")}
  for x in f.get("broken-link-report.yaml",{}).get("links",[]):
   if x.get("status")==404 and x.get("recommended_action")=="REDIRECT_TARGET" and not x.get("replacement_url"):
    e.append(f"{d.name}: 404 cannot auto-redirect without replacement URL")
  for x in f.get("redirect-audit.yaml",{}).get("redirects",[]):
   if x.get("ownership_status") in ("UNKNOWN","CONFLICTING") and x.get("recommended_action") in ("CREATE_301","CREATE_302","UPDATE_EXISTING"):
    e.append(f"{d.name}: unresolved ownership cannot execute redirect decision")
  for x in f.get("canonical-audit.yaml",{}).get("items",[]):
   if x.get("ownership_status") in ("UNKNOWN","CONFLICTING") and x.get("recommended_action")=="CHANGE_TARGET":
    e.append(f"{d.name}: unresolved ownership cannot change canonical target")
  for x in f.get("remediation-plan.yaml",{}).get("items",[]):
   if x.get("risk_class") in ("LIVE_PAGE_TECHNICAL_CHANGE","SITEWIDE_CONFIGURATION_CHANGE","URL_OWNERSHIP_CHANGE","SERVER_OR_CDN_CHANGE") and x.get("approval_required") is not True:
    e.append(f"{d.name}: high-impact live technical change requires approval")
   if x.get("confidence")=="LOW" and x.get("risk_class") not in ("SAFE_READ_ONLY","SAFE_REVERSIBLE_FIX") and x.get("approval_required") is False:
    e.append(f"{d.name}: low-confidence high-impact fix cannot bypass approval")
  for x in f.get("safe-fix-queue.yaml",{}).get("items",[]):
   if x.get("environment")=="PRODUCTION" and x.get("execution_allowed") is True:
    e.append(f"{d.name}: production change cannot be treated as safe auto-execution")
   if x.get("execution_allowed") is True and x.get("authorized") is not True:
    e.append(f"{d.name}: executable safe fix must be authorized")
  for x in f.get("verification-report.yaml",{}).get("items",[]):
   if x.get("state")=="VERIFIED_FIXED" and not x.get("evidence"):
    e.append(f"{d.name}: VERIFIED_FIXED requires evidence")
  execs={x.get("issue_id"):x for x in f.get("execution-log.yaml",{}).get("items",[])}
  for x in f.get("verification-report.yaml",{}).get("items",[]):
   if x.get("state")=="VERIFIED_FIXED" and x.get("issue_id") in execs and execs[x.get("issue_id")].get("success_response") is not True:
    e.append(f"{d.name}: verified fix conflicts with failed execution response")
  for x in f.get("cross-skill-handoffs.yaml",{}).get("handoffs",[]):
   reason=(x.get("reason") or "").lower()
   if "semantic" in reason and x.get("target_skill")!="08-internal-linking-architecture":
    e.append(f"{d.name}: semantic internal-link work must hand off to 08")
   if "speed" in reason and x.get("target_skill")!="21-page-speed-optimization":
    e.append(f"{d.name}: speed work must hand off to 21")
  c=f.get("closeout.yaml",{})
  if c.get("g12")=="WAITING_APPROVAL" and c.get("final_status")!="WAITING_APPROVAL":
    e.append(f"{d.name}: G12 WAITING_APPROVAL requires matching final_status")
 print("EXAMPLE_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
