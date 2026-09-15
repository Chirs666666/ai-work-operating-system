from pathlib import Path
import sys,yaml
def load(p): return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]); e=[]
 for d in [p for p in root.iterdir() if p.is_dir()]:
  f={p.name:load(p) for p in d.glob("*.yaml")}
  kpi=f.get("site-kpi-summary.yaml",{})
  if kpi.get("change_class")=="INSUFFICIENT_DATA":
   for k in ("clicks","impressions","sessions","conversions"):
    if kpi.get(k)==0: e.append(f"{d.name}: missing {k} cannot be fabricated as zero")
  sq=f.get("source-quality.yaml",{}).get("items",[])
  if any(x.get("status")=="CONFLICTING" for x in sq):
   for x in f.get("diagnosis-register.yaml",{}).get("items",[]):
    if x.get("confidence")=="CONFIRMED" and not x.get("evidence"):
     e.append(f"{d.name}: conflicting sources cannot yield unsupported CONFIRMED diagnosis")
  for x in f.get("query-page-matrix.yaml",{}).get("items",[]):
   if x.get("relationship") in ("WRONG_PAGE_SIGNAL","CANNIBALIZATION_SIGNAL"):
    hs=f.get("cross-skill-handoffs.yaml",{}).get("handoffs",[])
    if not any(h.get("target_skill")=="25-keyword-page-mapping" for h in hs):
     e.append(f"{d.name}: ownership signal must hand off to 25")
  for x in f.get("diagnosis-register.yaml",{}).get("items",[]):
   if x.get("confidence")=="CONFIRMED" and not x.get("evidence"):
    e.append(f"{d.name}: CONFIRMED diagnosis requires evidence")
  kv=f.get("keyword-visibility.yaml",{})
  if kv and kv.get("provider") in ("Semrush","Ahrefs") and kv.get("provider_specific") is not True:
   e.append(f"{d.name}: third-party visibility must remain provider-specific")
  p=f.get("period-definition.yaml",{})
  if p and p.get("equivalent_periods") is False and not p.get("warnings"):
   e.append(f"{d.name}: non-equivalent periods require warnings")
  for h in f.get("cross-skill-handoffs.yaml",{}).get("handoffs",[]):
   r=(h.get("reason") or "").lower()
   if ("wrong-page" in r or "cannibal" in r or "ownership" in r) and h.get("target_skill")!="25-keyword-page-mapping":
    e.append(f"{d.name}: ownership work must hand off to 25")
 print("EXAMPLE_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
