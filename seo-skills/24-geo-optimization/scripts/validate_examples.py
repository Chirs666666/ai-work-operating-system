from pathlib import Path
import yaml,sys
def L(p):return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]);e=[]
 for d in [x for x in root.iterdir() if x.is_dir()]:
  f={p.name:L(p) for p in d.glob("*.yaml")}
  sd=f.get("structured-data-alignment.yaml",{})
  if sd.get("guarantees_ai_citation") is True:e.append(f"{d.name}: schema cannot guarantee AI citation")
  cr=f.get("citation-readiness.yaml",{})
  if cr.get("guarantees_ai_citation") is True:e.append(f"{d.name}: citation readiness cannot guarantee AI citation")
  av=f.get("ai-visibility-observations.yaml",{})
  obs=av.get("observations",[])
  if len(obs)==1 and av.get("success_claimed") is True:e.append(f"{d.name}: one AI observation cannot prove GEO success")
  if obs and all(x.get("status")=="NO_OBSERVATION" for x in obs) and av.get("seo_value_claimed_absent") is True:e.append(f"{d.name}: no AI mention cannot prove no SEO value")
  claims={x["claim_id"]:x for x in f.get("claim-register.yaml",{}).get("claims",[])}
  maps={x["claim_id"]:x for x in f.get("claim-evidence-map.yaml",{}).get("mappings",[])}
  close=f.get("closeout.yaml",{})
  for cid,c in claims.items():
   if c.get("material") and c.get("requires_evidence"):
    m=maps.get(cid)
    if (not m or m.get("support_status")=="UNSUPPORTED") and close.get("g24")=="PASS":
     e.append(f"{d.name}: unsupported material claim cannot PASS")
  vr=f.get("verification-plan.yaml",{})
  if d.name=="seo-preservation" and vr.get("seo_assets_preserved") is False:e.append(f"{d.name}: proven SEO assets must be preserved")
 print("EXAMPLE_ERRORS="+repr(e));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())