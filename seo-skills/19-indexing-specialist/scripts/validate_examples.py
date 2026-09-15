from pathlib import Path
import yaml,sys
def L(p):return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]);e=[]
 for d in [x for x in root.iterdir() if x.is_dir()]:
  f={p.name:L(p) for p in d.glob("*.yaml")}
  idx=f.get("index-status.yaml",{});co=f.get("closeout.yaml",{});can=f.get("canonical-status.yaml",{})
  if idx.get("status") in ("NOINDEX","BLOCKED_ROBOTS","INDEXED_CANONICAL_OTHER") and co.get("g19")=="PASS":
   e.append(f"{d.name}: unhealthy index state cannot PASS")
  if can.get("alignment")=="FAIL" and co.get("g19")=="PASS":e.append(f"{d.name}: canonical mismatch cannot PASS")
  ir=f.get("inspection-record.yaml",{})
  if ir.get("inspection_type")=="PUBLIC_SITE_QUERY" and ir.get("authoritative_for_index_status") is True:
   e.append(f"{d.name}: site query cannot be authoritative index proof")
  if ir.get("inspection_type")=="PUBLIC_SITE_QUERY" and idx.get("definitive") is True:
   e.append(f"{d.name}: site query cannot create definitive index state")
  vb=f.get("visibility-baseline.yaml",{})
  if vb.get("data_available") is False:
   for k in ("impressions","clicks","query_count","average_position"):
    if vb.get(k)==0:e.append(f"{d.name}: missing {k} cannot become zero")
  tq=f.get("target-query-map.yaml",{})
  for t in tq.get("targets",[]):
   if t.get("best_match_class") in ("UNRELATED_QUERY","BRAND_QUERY","RELATED_QUERY","UNKNOWN") and t.get("status")=="DETECTED":
    e.append(f"{d.name}: non-target match cannot satisfy target detection")
  bm=f.get("benchmark-status.yaml",{})
  if bm and (bm.get("benchmark_type")!="CONFIGURABLE_BENCHMARK" or bm.get("guarantee") is not False):
   e.append(f"{d.name}: benchmark must be configurable and non-guaranteed")
 print("EXAMPLE_ERRORS="+repr(e));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())