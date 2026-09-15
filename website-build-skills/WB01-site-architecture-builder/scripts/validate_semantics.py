from pathlib import Path
import sys,yaml

def load(p): return yaml.safe_load(Path(p).read_text()) or {}

def main(example):
    d=Path(example); errors=[]
    pages=load(d/"page-inventory.yaml").get("pages",[])
    fams={x["family_id"] for x in load(d/"page-family-register.yaml").get("families",[])}
    urls=[]
    intents={}
    for p in pages:
        if not p.get("family_id") or p.get("family_id") not in fams:
            errors.append(f"{p.get('page_id')}: invalid/missing family")
        u=p.get("proposed_url")
        if u in urls: errors.append(f"duplicate proposed URL: {u}")
        urls.append(u)
        key=(p.get("primary_intent"),p.get("ownership_key"))
        if key!=(None,None):
            if key in intents and not p.get("differentiation_rationale"):
                errors.append(f"{p.get('page_id')}: duplicate intent/ownership without rationale")
            intents[key]=p.get("page_id")
    kip=load(d/"keyword-page-input-check.yaml")
    conflicts=load(d/"architecture-conflict-register.yaml").get("conflicts",[])
    if kip.get("skill_25_available") and kip.get("alignment_status")=="CONFLICT":
        if not any(c.get("type")=="OWNERSHIP_OVERRIDE" and c.get("resolution_state") in ("RETURNED","RESOLVED","ACCEPTED_RISK") for c in conflicts):
            errors.append("Skill 25 ownership conflict not explicitly returned/resolved")
    nav=load(d/"navigation-map.yaml")
    if nav.get("sitemap_equals_primary_nav") is True:
        errors.append("primary navigation must not be forced equal to full sitemap")
    for u in load(d/"url-architecture.yaml").get("urls",[]):
        if u.get("change_type")=="PROPOSED_CHANGE" and u.get("live_change_approved") is True:
            errors.append(f"{u.get('page_id')}: WB01 cannot pre-approve live URL changes")
    for s in load(d/"source-register.yaml").get("sources",[]):
        if s.get("source_type")=="UNKNOWN" and s.get("status")=="VALID":
            errors.append(f"{s.get('source_id')}: unknown source cannot be VALID")
    print("SEMANTIC_ERRORS="+repr(errors))
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main(sys.argv[1]))
