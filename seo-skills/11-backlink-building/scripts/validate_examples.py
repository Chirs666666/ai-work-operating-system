from pathlib import Path
import sys,yaml
def load(p): return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]); e=[]
 for d in [p for p in root.iterdir() if p.is_dir()]:
  f={p.name:load(p) for p in d.glob("*.yaml")}
  for p in f.get("prospect-inventory.yaml",{}).get("prospects",[]):
   for k in ("dr","da","authority_score","organic_traffic"):
    if p.get(k)==0 and d.name=="missing-metrics": e.append(f"{d.name}: missing {k} fabricated as zero")
  for x in f.get("competitor-link-opportunities.yaml",{}).get("items",[]):
   if x.get("status")=="QUALIFIED" and x.get("requalified") is not True:
    e.append(f"{d.name}: competitor link qualified without requalification")
  for x in f.get("contact-register.yaml",{}).get("contacts",[]):
   if x.get("value") and x.get("public_or_authorized") is not True:
    e.append(f"{d.name}: contact value lacks public/authorized basis")
  for x in f.get("paid-placement-review.yaml",{}).get("items",[]):
   if x.get("paid") and x.get("approval_required") is not True:
    e.append(f"{d.name}: paid placement must require approval")
   if x.get("paid") and x.get("approved") is False:
    cc=f.get("change-control.yaml",{})
    if cc.get("execution_allowed") is True: e.append(f"{d.name}: unapproved paid placement executable")
  for x in f.get("risk-register.yaml",{}).get("items",[]):
   if x.get("risk_class")=="HIGH_RISK_LINK_SCHEME" and x.get("decision")!="REJECT":
    e.append(f"{d.name}: high-risk link scheme must REJECT")
  for x in f.get("live-link-register.yaml",{}).get("links",[]):
   if x.get("status")=="LIVE_VERIFIED":
    vr=f.get("link-verification-report.yaml",{}).get("items",[])
    match=[v for v in vr if v.get("prospect_id")==x.get("prospect_id") and v.get("status")=="LIVE_VERIFIED" and v.get("evidence")]
    if not match: e.append(f"{d.name}: LIVE_VERIFIED lacks verification evidence")
  for x in f.get("target-page-readiness.yaml",{}).get("items",[]):
   if x.get("ownership")=="CONFLICTING" and x.get("readiness")=="READY":
    e.append(f"{d.name}: conflicting ownership cannot be READY")
  cc=f.get("change-control.yaml",{})
  if cc.get("risk_class")=="HIGH_RISK_LINK_SCHEME" and cc.get("execution_allowed") is True:
   e.append(f"{d.name}: high-risk scheme cannot execute")
 print("EXAMPLE_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
