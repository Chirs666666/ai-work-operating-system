from pathlib import Path
import yaml,sys
def L(p):return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]);e=[]
 for d in [x for x in root.iterdir() if x.is_dir()]:
  f={p.name:L(p) for p in d.glob("*.yaml")};dec=f.get("optimization-decision.yaml",{});act=dec.get("action")
  hist=f.get("historical-performance.yaml",{})
  if act=="REWRITE" and hist and hist.get("clicks_trend")=="DOWN" and hist.get("position_trend") in ("STABLE","UNKNOWN") and hist.get("demand_or_seasonality") in ("UNKNOWN","SEASONAL"):
   e.append(f"{d.name}: traffic decline alone cannot force rewrite")
  base=f.get("article-baseline.yaml",{})
  if act in ("REFRESH","REWRITE") and base.get("published_at") and not any(k in f for k in ("freshness-audit.yaml","content-gap.yaml","article-diagnosis.yaml","historical-performance.yaml")):
   e.append(f"{d.name}: age alone cannot force update")
  can=f.get("cannibalization-check.yaml",{})
  if act=="MERGE" and not (can.get("status")=="CONFIRMED" and can.get("ownership_confirmed") is True):
   e.append(f"{d.name}: merge requires confirmed cannibalization/ownership evidence")
  pr=f.get("preservation-register.yaml",{})
  for x in pr.get("items",[]):
   if x.get("proven_equity") is True and x.get("decision")=="REMOVE":e.append(f"{d.name}: proven equity cannot be removed without contrary evidence")
  be=f.get("backlink-equity.yaml",{})
  cr=f.get("change-register.yaml",{})
  if be.get("protected_url") is True:
   for x in cr.get("changes",[]):
    if x.get("target")=="URL" and x.get("change")!="Keep current URL" and not x.get("approval_required"):
     e.append(f"{d.name}: protected URL change requires approval")
  diag=f.get("article-diagnosis.yaml",{})
  if hist.get("demand_or_seasonality")=="SEASONAL" and hist.get("position_trend")=="STABLE" and diag.get("primary_cause")=="CONTENT":
   e.append(f"{d.name}: seasonal decline with stable rank cannot be labeled content failure without more evidence")
  if diag.get("state")=="CTR_WEAK" and act=="REWRITE":e.append(f"{d.name}: CTR weakness alone should not force full rewrite")
 print("EXAMPLE_ERRORS="+repr(e));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())