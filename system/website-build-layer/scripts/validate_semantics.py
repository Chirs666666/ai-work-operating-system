from pathlib import Path
import yaml,sys
def L(d,n):return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]);e=[]
arts={a.get("artifact_id"):a for a in L(d,"artifact-registry.yaml").get("artifacts",[])}
routes=L(d,"routing-plan.yaml").get("tasks",[]); deps=L(d,"dependency-graph.yaml").get("dependencies",[])
for t in routes:
 if t.get("action")=="REUSE":
  a=arts.get(t.get("artifact_id"))
  if not a or a.get("producer")!=t.get("skill") or not a.get("ref") or not a.get("fresh") or not a.get("provenance_valid") or not a.get("assumptions_compatible") or a.get("prior_gate") not in ("PASS","WARN","REUSE"):e.append(f"{t.get('task_id')}: invalid REUSE evidence")
 if t.get("skill")=="WB08" and t.get("action")=="RUN":
  d7=[x for x in deps if x.get("upstream")=="WB07" and x.get("downstream")=="WB08" and x.get("critical")]
  if not d7 or any(x.get("state") not in ("PASS","REUSE") for x in d7):e.append("WB08 RUN requires ready WB07 dependency")
  aps=L(d,"approval-register.yaml").get("approvals",[])
  if not any(a.get("requested_by_skill")=="WB08" and a.get("action")=="PRODUCTION_DEPLOYMENT" and a.get("state")=="APPROVED" and a.get("evidence_ref") for a in aps):e.append("WB08 RUN requires explicit production approval")
for x in deps:
 if x.get("critical") and x.get("state") in ("BLOCKED","FAILED","WAITING_DEPENDENCY"):
  down=[t for t in routes if t.get("skill")==x.get("downstream")]
  if any(t.get("action")=="RUN" for t in down):e.append(f"{x.get('dependency_id')}: blocked critical dependency ignored")
# ownership
owners={"technical_seo":"12","indexing":"19","ranking_validation":"20"}
for t in routes:
 if t.get("capability") in owners and t.get("skill")!=owners[t.get("capability")]:e.append(f"{t.get('task_id')}: specialist ownership violation")
# failures require coherent recovery
fails=L(d,"failure-register.yaml").get("failures",[]); rec={x.get("failure_id"):x for x in L(d,"recovery-plan.yaml").get("items",[])}
for f in fails:
 if f.get("state") in ("OPEN","FIXING","RETEST"):
  r=rec.get(f.get("failure_id"))
  if not r or r.get("correction_skill")!=f.get("responsible_skill") or r.get("rerun_gate")!=f.get("failed_gate"):e.append(f"{f.get('failure_id')}: invalid recovery routing")
close=L(d,"closeout.yaml")
if close.get("indexing_claimed"):e.append("Website Build Layer cannot claim indexing")
if close.get("ranking_claimed"):e.append("Website Build Layer cannot claim ranking")
print("SEMANTIC_ERRORS="+repr(e));raise SystemExit(1 if e else 0)
