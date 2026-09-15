from pathlib import Path
import yaml,sys
def L(d,n): return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]); e=[]
if L(d,"architecture-alignment.yaml").get("alignment")=="CONFLICT" and L(d,"closeout.yaml").get("ready_for_assembly"):
    e.append("WB01 architecture conflict cannot be assembly-ready")
if L(d,"design-token-alignment.yaml").get("alignment")=="CONFLICT" and L(d,"closeout.yaml").get("ready_for_assembly"):
    e.append("WB02 design-token conflict cannot be assembly-ready")
for x in L(d,"component-ownership.yaml").get("ownership",[]):
    if x.get("duplicate_owners") and not x.get("resolution"): e.append(f"{x.get('component_id')}: duplicate ownership unresolved")
desk=set(L(d,"navigation-spec.yaml").get("destinations",[])); mob=set(L(d,"mobile-navigation-spec.yaml").get("destinations",[]))
if L(d,"mobile-navigation-spec.yaml").get("architecture_consistency")=="PASS" and desk!=mob: e.append("desktop/mobile navigation mismatch")
for x in L(d,"global-cta-register.yaml").get("ctas",[]):
    if not x.get("destination"): e.append(f"{x.get('cta_id')}: CTA missing destination")
for x in L(d,"form-register.yaml").get("forms",[]):
    if not x.get("success_state") or not x.get("error_state"): e.append(f"{x.get('form_id')}: form missing success/error state")
    if x.get("privacy_consent_decision")=="UNKNOWN": e.append(f"{x.get('form_id')}: privacy/consent decision unresolved")
for x in L(d,"reusable-pattern-register.yaml").get("patterns",[]):
    if x.get("hardcoded_page_specific_content"): e.append(f"{x.get('pattern_id')}: reusable pattern contains page-specific hardcoding")
aps={a.get("approval_id"):a for a in L(d,"approval-register.yaml").get("approvals",[])}
for x in L(d,"wordpress-component-plan.yaml").get("changes",[]):
    if x.get("environment")=="PRODUCTION" and x.get("requires_approval") and x.get("status") in ("APPROVED","DONE"):
        a=aps.get(x.get("approval_id"))
        if not a or a.get("state")!="APPROVED" or not a.get("evidence_ref"): e.append(f"{x.get('change_id')}: production change lacks approval evidence")
print("SEMANTIC_ERRORS="+repr(e)); raise SystemExit(1 if e else 0)
