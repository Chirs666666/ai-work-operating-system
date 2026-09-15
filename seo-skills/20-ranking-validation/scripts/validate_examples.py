from pathlib import Path
import yaml,sys
def L(p):return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]);e=[]
 for d in [x for x in root.iterdir() if x.is_dir()]:
  f={p.name:L(p) for p in d.glob("*.yaml")}
  g=f.get("gsc-query-page.yaml",{})
  if g.get("data_available") is False:
   for q in g.get("queries",[]):
    if any(q.get(k)==0 for k in ("impressions","clicks","average_position")):e.append(f"{d.name}: missing GSC data cannot become zero metrics")
  v=f.get("verdict.yaml",{})
  if v.get("state")=="IMPRESSION_STARTED" and v.get("ranking_established") is True:e.append(f"{d.name}: impression-started cannot equal established ranking")
  tq=f.get("target-query-map.yaml",{})
  for t in tq.get("targets",[]):
   if t.get("best_match_class") in ("RELATED_QUERY","UNRELATED_QUERY","BRAND_QUERY","UNKNOWN") and t.get("status")=="DETECTED":
    e.append(f"{d.name}: non-target match cannot satisfy target detection")
  rt=f.get("ranking-trend.yaml",{})
  if rt.get("windows_comparable") is False and rt.get("trend")!="UNKNOWN":e.append(f"{d.name}: noncomparable windows cannot assert ranking trend")
  pb=f.get("position-baseline.yaml",{})
  for x in pb.get("observations",[]):
   if x.get("provider")=="SEMRUSH" and x.get("metric")=="AVERAGE_POSITION":e.append(f"{d.name}: Semrush rank cannot be relabeled GSC average position")
  tm=f.get("time-maturity.yaml",{})
  if tm.get("maturity")=="EARLY" and tm.get("signal_growth")=="GROWING" and tm.get("wait_recommendation")=="INTERVENE":
   e.append(f"{d.name}: early growing page should not force immediate intervention")
  ia=f.get("intent-alignment.yaml",{})
  na=f.get("next-action.yaml",{})
  if ia.get("alignment")=="FAIL" and na.get("action")=="MONITOR":e.append(f"{d.name}: known intent mismatch cannot be indefinite monitor")
 print("EXAMPLE_ERRORS="+repr(e));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())