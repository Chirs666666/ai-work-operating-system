from pathlib import Path
import yaml,sys
def L(d,n):return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]);e=[]
wb=L(d,"wb07-readiness.yaml");scope=L(d,"deployment-scope.yaml");man=L(d,"deployment-manifest.yaml");pre=L(d,"pre-deployment-check.yaml");snap=L(d,"snapshot-register.yaml");rb=L(d,"rollback-plan.yaml");exe=L(d,"deployment-execution.yaml");sm=L(d,"smoke-test.yaml");pv=L(d,"production-verification.yaml");rv=L(d,"rollback-verification.yaml");gate=L(d,"launch-gate.yaml");idx=L(d,"indexing-handoff.yaml")
aps={a.get("approval_id"):a for a in L(d,"approval-register.yaml").get("approvals",[])}
active=exe.get("started") or exe.get("state") not in ("NOT_STARTED",)
if active and (not wb.get("ready") or wb.get("state")!="READY_FOR_LAUNCH_APPROVAL" or not wb.get("evidence")):e.append("production execution requires WB07 readiness evidence")
if active:
 a=aps.get(man.get("approval_id"))
 if not a or a.get("type")!="PRODUCTION_DEPLOYMENT" or a.get("state")!="APPROVED" or not a.get("evidence_ref"):e.append("production execution lacks explicit deployment approval evidence")
 elif a.get("scope_id")!=scope.get("scope_id") or man.get("scope_id")!=scope.get("scope_id"):e.append("deployment approval/scope mismatch")
 if exe.get("scope_id")!=scope.get("scope_id"):e.append("actual execution scope differs from approved scope")
if man.get("risk") in ("HIGH","CRITICAL") and active:
 if not snap.get("required") or not snap.get("created") or not snap.get("verified") or not snap.get("evidence"):e.append("high-risk deployment lacks verified snapshot")
 if not rb.get("required") or not rb.get("ready") or not rb.get("method") or not rb.get("evidence"):e.append("high-risk deployment lacks rollback readiness")
if active and not pre.get("ready"):e.append("deployment started before pre-deployment readiness")
critfail=any(x.get("critical") and x.get("result") in ("FAIL","BLOCK") for x in sm.get("checks",[]))
if gate.get("launch_verified"):
 if exe.get("state")!="DEPLOYED" or not exe.get("completed") or not exe.get("evidence"):e.append("launch verified without completed deployment evidence")
 if sm.get("overall") not in ("PASS","WARN") or critfail:e.append("launch verified despite critical smoke failure")
 if not pv.get("production_verified") or pv.get("overall") not in ("PASS","WARN") or not pv.get("checks"):e.append("launch verified without production verification")
 if not gate.get("handoff_to_19_ready"):e.append("verified launch missing indexing handoff readiness")
for x in pv.get("checks",[]):
 if x.get("critical") and x.get("result") in ("FAIL","BLOCK") and gate.get("launch_verified"):e.append(f"{x.get('check_id')}: critical production failure cannot be launch verified")
rex=L(d,"rollback-execution.yaml")
if rex.get("executed") and (not rv.get("required") or not rv.get("verified") or rv.get("state")!="VERIFIED" or not rv.get("evidence")):e.append("rollback executed but not verified")
if idx.get("indexing_state")!="NOT_CLAIMED":e.append("WB08 cannot claim indexing state")
if idx.get("ranking_state")!="NOT_CLAIMED":e.append("WB08 cannot claim ranking success")
if idx.get("submission_state") in ("SUBMITTED","RECEIVED") and idx.get("indexing_state")!="NOT_CLAIMED":e.append("submission/receipt cannot imply indexing")
print("SEMANTIC_ERRORS="+repr(e));raise SystemExit(1 if e else 0)
