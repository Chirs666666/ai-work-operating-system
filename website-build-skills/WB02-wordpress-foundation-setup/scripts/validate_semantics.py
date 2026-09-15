from pathlib import Path
import sys,yaml
def load(p): return yaml.safe_load(Path(p).read_text()) or {}
def main(example):
    d=Path(example); errors=[]
    per=load(d/"permalink-baseline.yaml")
    if per.get("wb01_alignment")=="CONFLICT":
        errors.append("permalink baseline conflicts with WB01")
    env=load(d/"wordpress-environment.yaml")
    if env.get("evidence_status")=="VERIFIED":
        core=[env.get("wordpress_version"),env.get("environment"),env.get("site_url")]
        if any(v in (None,"UNKNOWN","") for v in core):
            errors.append("UNKNOWN environment evidence cannot be VERIFIED")
    plugins=load(d/"plugin-register.yaml").get("plugins",[])
    active=[p for p in plugins if p.get("status") in ("ACTIVE","PLANNED") and p.get("capability_owner")]
    owners={}
    for p in active:
        for c in p.get("capabilities",[]):
            owners.setdefault(c,[]).append(p.get("plugin_id"))
    for c,ids in owners.items():
        if c in {"seo_metadata","canonical","sitemap","schema","robots"} and len(ids)>1:
            errors.append(f"duplicate SEO capability owner: {c}")
        if c in {"page_cache","security_firewall"} and len(ids)>1:
            audit=load(d/"plugin-conflict-audit.yaml")
            compat=[x for x in audit.get("conflicts",[]) if x.get("capability")==c and x.get("compatibility")=="COMPATIBLE"]
            if not compat:
                errors.append(f"duplicate {c} ownership without compatibility evidence")
    staging=load(d/"staging-baseline.yaml")
    changes=load(d/"foundation-change-plan.yaml").get("changes",[])
    approvals={a.get("approval_id"):a for a in load(d/"approval-register.yaml").get("approvals",[])}
    backup=load(d/"backup-baseline.yaml")
    for ch in changes:
        if ch.get("environment")=="PRODUCTION":
            if ch.get("requires_approval") and ch.get("status") in ("APPROVED","DONE"):
                a=approvals.get(ch.get("approval_id"))
                if not a or a.get("state")!="APPROVED" or not a.get("evidence_ref"):
                    errors.append(f"{ch.get('change_id')}: production change treated as approved without approval evidence")
            if ch.get("requires_backup") and ch.get("status") not in ("BLOCKED","SKIPPED"):
                if backup.get("backup_available")!="YES" or not backup.get("rollback_ready") or not ch.get("rollback_plan"):
                    errors.append(f"{ch.get('change_id')}: risky production change lacks backup/rollback readiness")
    close=load(d/"closeout.yaml")
    if close.get("ready_for_components") and staging.get("staging_required_for_current_plan") and staging.get("staging_available")!="YES":
        errors.append("foundation cannot be ready when required staging is unavailable")
    print("SEMANTIC_ERRORS="+repr(errors))
    return 1 if errors else 0
if __name__=="__main__": raise SystemExit(main(sys.argv[1]))
