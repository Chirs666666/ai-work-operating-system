from pathlib import Path
import sys,yaml
def load(p): return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]); e=[]
 for d in [p for p in root.iterdir() if p.is_dir()]:
  f={p.name:load(p) for p in d.glob("*.yaml")}
  perf=f.get("performance-baseline.yaml",{}).get("items",[])
  if d.name=="missing-data":
   for x in perf:
    for k in ("gsc_clicks","gsc_impressions","ga4_sessions","ga4_conversions","provider_estimated_traffic"):
     if x.get(k)==0: e.append(f"{d.name}: missing {k} fabricated as zero")
  preserve={x.get("url"):x for x in f.get("preservation-register.yaml",{}).get("items",[])}
  for x in f.get("action-classification.yaml",{}).get("items",[]):
   action=x.get("action"); url=x.get("url")
   if action in ("MERGE","REDIRECT","REASSIGN"):
    if x.get("ownership_validation_required") is not True:
     e.append(f"{d.name}: {action} must require ownership validation")
    hs=f.get("cross-skill-handoffs.yaml",{}).get("handoffs",[])
    if not any(h.get("target_skill")=="25-keyword-page-mapping" for h in hs):
     e.append(f"{d.name}: {action} must hand off to 25")
   if action in ("MERGE","REDIRECT","NOINDEX","REMOVE","REASSIGN"):
    if x.get("execution_allowed") is True:
     e.append(f"{d.name}: high-impact action cannot auto-execute")
    if x.get("approval_required") is not True:
     e.append(f"{d.name}: high-impact action requires approval")
   p=preserve.get(url)
   if p and p.get("preservation_risk") in ("CRITICAL","HIGH") and action in ("REMOVE","NOINDEX","REDIRECT","MERGE","REWRITE") and x.get("confidence") in ("LOW","UNKNOWN"):
    e.append(f"{d.name}: high preservation risk cannot take low-confidence destructive action")
  for x in f.get("backlink-asset-signals.yaml",{}).get("items",[]):
   if x.get("referring_domains") is None and x.get("backlinks") is None and x.get("authority_metric")==0:
    e.append(f"{d.name}: unknown backlink authority cannot become zero")
  for h in f.get("cross-skill-handoffs.yaml",{}).get("handoffs",[]):
   reason=(h.get("reason") or "").lower()
   if ("ownership" in reason or "competing url" in reason) and h.get("target_skill")!="25-keyword-page-mapping":
    e.append(f"{d.name}: ownership work must hand off to 25")
 print("EXAMPLE_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
