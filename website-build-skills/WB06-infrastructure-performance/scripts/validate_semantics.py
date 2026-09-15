from pathlib import Path
import yaml,sys
def L(d,n):return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]);e=[];c=L(d,"closeout.yaml");ready=c.get("infrastructure_ready")
env=L(d,"environment-register.yaml")
if ready and (env.get("environment")=="UNKNOWN" or not env.get("separation_verified")):e.append("ready infrastructure requires verified environment separation")
for h in L(d,"ssl-tls-register.yaml").get("hosts",[]):
 if h.get("state") in ("READY","VERIFIED") and (not h.get("https_enabled") or not h.get("certificate_valid") or not h.get("evidence")):e.append(f"{h.get('host')}: invalid evidence-backed TLS readiness")
pages=[x for x in L(d,"cache-layer-register.yaml").get("layers",[]) if x.get("active") and x.get("layer_type")=="PAGE"]
if len({x.get("owner") for x in pages})>1 and not any(x.get("status") in ("RESOLVED","ACCEPTED_RISK") for x in L(d,"cache-conflict-register.yaml").get("conflicts",[])):e.append("multiple active PAGE cache owners unresolved")
smtp=L(d,"smtp-register.yaml");sv=L(d,"smtp-verification.yaml")
if ready and smtp.get("required") and (smtp.get("state")!="VERIFIED" or sv.get("state")!="VERIFIED" or not sv.get("delivered") or not sv.get("delivery_evidence")):e.append("required SMTP lacks delivery verification")
bp=L(d,"backup-policy.yaml");bv=L(d,"backup-verification.yaml")
if ready and bp.get("required") and (not bv.get("last_backup_success") or not bv.get("backup_evidence") or not bv.get("restore_method_known")):e.append("backup/restore readiness incomplete")
pf=L(d,"performance-foundation.yaml")
if pf.get("measured_performance_claim"):e.append("WB06 cannot claim measured page performance/CWV verification")
if L(d,"secret-handling-check.yaml").get("embedded_secret_detected"):e.append("embedded secret detected")
aps={a.get("approval_id"):a for a in L(d,"approval-register.yaml").get("approvals",[])}
rb=L(d,"rollback-plan.yaml")
for x in L(d,"production-change-plan.yaml").get("changes",[]):
 if x.get("environment")=="PRODUCTION" and x.get("risk") in ("HIGH","CRITICAL"):
  if x.get("backup_required") and (not bv.get("last_backup_success") or not bv.get("backup_evidence")):e.append(f"{x.get('change_id')}: high-risk production change lacks backup")
  if x.get("rollback_required") and (not rb.get("ready") or not rb.get("method") or not rb.get("evidence")):e.append(f"{x.get('change_id')}: high-risk production change lacks rollback readiness")
 if x.get("environment")=="PRODUCTION" and x.get("status") in ("APPROVED","DONE"):
  a=aps.get(x.get("approval_id"))
  if not a or a.get("state")!="APPROVED" or not a.get("evidence_ref"):e.append(f"{x.get('change_id')}: production change lacks explicit approval evidence")
print("SEMANTIC_ERRORS="+repr(e));raise SystemExit(1 if e else 0)
