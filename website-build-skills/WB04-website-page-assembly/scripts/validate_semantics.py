from pathlib import Path
import yaml,sys
def L(d,n): return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]); e=[]
close=L(d,"closeout.yaml"); ready=close.get("ready_for_skill_07")
ident=L(d,"page-identity.yaml")
if ready and (not ident.get("resolved") or not ident.get("wb01_artifact") or not ident.get("url")): e.append("assembly-ready page identity must resolve to WB01")
ptype=L(d,"page-type.yaml").get("page_type")
arts=L(d,"upstream-artifact-register.yaml").get("artifacts",[])
owners={x.get("skill_owner") for x in arts if x.get("status") in ("AVAILABLE","REUSE")}
if ready and "04-page-planning-ui" not in owners: e.append("assembly-ready page requires Skill 04 page plan")
if ready and ptype=="PRODUCT_DETAIL" and "05-product-copywriting" not in owners: e.append("PRODUCT_DETAIL requires Skill 05 content")
if ready and ptype=="ARTICLE" and "06-content-writing-optimization" not in owners: e.append("ARTICLE requires Skill 06 content")
for x in L(d,"section-source-map.yaml").get("mappings",[]):
    if ready and (not x.get("source_owner") or not x.get("source_artifact") or x.get("provenance_status") in ("MISSING","UNKNOWN")):
        e.append(f"{x.get('section_id')}: section source/provenance missing")
for x in L(d,"global-component-binding.yaml").get("components",[]):
    if x.get("reference_mode")!="REFERENCE": e.append(f"{x.get('component_id')}: WB03 global component must be referenced, not copied")
for x in L(d,"media-binding.yaml").get("bindings",[]):
    if x.get("status")=="BOUND" and not x.get("artifact_ref"): e.append(f"{x.get('asset_id')}: bound media lacks artifact reference")
seo=L(d,"seo-binding.yaml")
if ready and seo.get("required_for_page") and (not seo.get("metadata_artifact_ref") or not seo.get("title_bound") or not seo.get("meta_description_bound")):
    e.append("required SEO metadata is incomplete")
for x in L(d,"conversion-binding.yaml").get("ctas",[]):
    if x.get("status")=="BOUND" and not x.get("destination"): e.append(f"{x.get('cta_id')}: CTA missing destination")
for x in L(d,"page-assembly-manifest.yaml").get("claims",[]):
    if x.get("support_status")=="UNSUPPORTED" and ready: e.append(f"{x.get('claim_id')}: unsupported claim blocks readiness")
plan=L(d,"draft-build-plan.yaml"); aps={a.get("approval_id"):a for a in L(d,"approval-register.yaml").get("approvals",[])}
if plan.get("target_environment")=="PRODUCTION" and plan.get("mode")=="PUBLISH" and plan.get("status") in ("APPROVED","DONE"):
    a=aps.get(plan.get("approval_id"))
    if not plan.get("requires_approval") or not a or a.get("state")!="APPROVED" or not a.get("evidence_ref"):
        e.append("production publish lacks explicit approval evidence")
print("SEMANTIC_ERRORS="+repr(e)); raise SystemExit(1 if e else 0)
