from pathlib import Path
import yaml,sys
def L(p):return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]);e=[]
 for d in [x for x in root.iterdir() if x.is_dir()]:
  f={p.name:L(p) for p in d.glob("*.yaml")}
  tr=f.get("traffic-trend.yaml",{})
  if tr and tr.get("metric")!="SEMRUSH_ESTIMATED_TRAFFIC":e.append(f"{d.name}: Semrush traffic must not be relabeled GA4 traffic")
  if tr.get("comparable") is False and tr.get("trend")!="UNKNOWN":e.append(f"{d.name}: noncomparable context cannot assert traffic trend")
  ctx=f.get("country-device-context.yaml",{})
  if ctx:
   incompatible=(ctx.get("comparison_database") and ctx.get("comparison_database")!=ctx.get("database")) or (ctx.get("comparison_device") and ctx.get("comparison_device")!=ctx.get("device"))
   if incompatible and ctx.get("comparable") is True:e.append(f"{d.name}: incompatible database/device cannot be directly comparable")
  kg=f.get("keyword-gap.yaml",{})
  for k in kg.get("keywords",[]):
   if k.get("decision") in ("CREATE","OPTIMIZE") and k.get("decision_basis")==[f"KD={k.get('kd')}"]:
    e.append(f"{d.name}: KD alone cannot decide keyword action")
  bg=f.get("backlink-gap.yaml",{})
  for p in bg.get("prospects",[]):
   if p.get("quality_decision")=="QUALIFY" and p.get("decision_basis")==[f"Authority Score={p.get('authority_score')}"]:
    e.append(f"{d.name}: Authority Score alone cannot qualify backlink")
  ok=f.get("organic-keywords.yaml",{})
  co=f.get("closeout.yaml",{})
  if ok=={"keywords":[]} and co.get("g22")=="PASS" and "absence" in " ".join(co.get("warnings",[])).lower():
    e.append(f"{d.name}: missing Semrush keyword cannot prove Google absence")
 print("EXAMPLE_ERRORS="+repr(e));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())