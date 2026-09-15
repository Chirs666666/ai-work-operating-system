from pathlib import Path
import sys,yaml
EDIT_MODES={"EDIT","ENHANCE","CROP","BACKGROUND_REPLACE","COLOR_VARIATION"}
def load(p): return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]); e=[]
 for d in [p for p in root.iterdir() if p.is_dir()]:
  f={p.name:load(p) for p in d.glob("*.yaml")}
  mode=f.get("manifest.yaml",{}).get("mode")
  sources=f.get("source-register.yaml",{}).get("sources",[])
  ec=f.get("edit-contract.yaml",{})
  if mode in EDIT_MODES:
   sid=ec.get("source_asset_id")
   has_source=bool(sid and any(s.get("source_id")==sid for s in sources))
   if not has_source:
    co=f.get("closeout.yaml",{})
    properly_blocked=(co.get("g17")=="BLOCK" and co.get("final_status")=="BLOCKED")
    if not properly_blocked:
     e.append(f"{d.name}: edit mode requires matching source asset or BLOCK closeout")
  tb=f.get("truth-boundary.yaml",{})
  if tb.get("truth_class")=="CONCEPTUAL" and tb.get("documentary_evidence_claimed") is True:
    e.append(f"{d.name}: conceptual visual cannot claim documentary evidence")
  gr=f.get("generation-record.yaml",{})
  if gr.get("generated") is True and gr.get("truth_class")=="UNKNOWN":
    e.append(f"{d.name}: generated visual needs explicit truth class")
  facts=f.get("technical-fact-register.yaml",{}).get("facts",[])
  tdr=f.get("text-data-review.yaml",{})
  if tdr.get("technical_data_present") is True:
   approved=[x for x in facts if x.get("approved_for_image") is True and x.get("evidence_ref")]
   if not approved or tdr.get("all_factual_text_evidence_backed") is not True:
    e.append(f"{d.name}: technical image data requires approved evidence")
  for fact in facts:
   if fact.get("approved_for_image") is True and not fact.get("evidence_ref"):
    e.append(f"{d.name}: approved technical fact needs evidence")
  cc=f.get("change-control.yaml",{})
  if cc and any(cc.get(k) for k in ("factual_subject_changed","technical_data_changed","documentary_interpretation_changed")):
   if cc.get("review_required") is not True:
    e.append(f"{d.name}: factual image change requires review")
   if cc.get("publish_allowed") is True:
    e.append(f"{d.name}: factual change cannot auto-publish before review")
 print("EXAMPLE_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
