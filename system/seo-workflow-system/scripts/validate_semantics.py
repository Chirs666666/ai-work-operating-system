from pathlib import Path
import yaml,sys
def L(d,n):return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]);e=[]
routes=L(d,"routing-plan.yaml").get("tasks",[]);arts={a.get("artifact_id"):a for a in L(d,"artifact-registry.yaml").get("artifacts",[])};deps=L(d,"dependency-graph.yaml").get("dependencies",[])
owners={"page_planning":"04","page_assembly":"WB04","wordpress_execution":"07","technical_seo":"12","indexing":"19","ranking_validation":"20","prelaunch_qa":"WB07","production_deployment":"WB08"}
for t in routes:
 if t.get("node")=="14":e.append("Skill 14 is merged alias; resolve to 12")
 if t.get("capability") in owners and t.get("node")!=owners[t.get("capability")]:e.append(f"{t.get('task_id')}: ownership violation")
 if t.get("action")=="REUSE":
  a=arts.get(t.get("artifact_id"))
  if not a or a.get("producer")!=t.get("node") or not a.get("ref") or not a.get("fresh") or not a.get("provenance_valid") or not a.get("assumptions_compatible") or a.get("prior_gate") not in ("PASS","WARN","REUSE") or a.get("evidence_state")=="UNKNOWN":e.append(f"{t.get('task_id')}: invalid REUSE")
 if t.get("action")=="DRAFT_ONLY" and t.get("capability")=="production_deployment" and "publish" in t.get("rationale","").lower():e.append("DRAFT_ONLY cannot request production publish")
 if t.get("node")=="WB08" and t.get("action")=="RUN":
  d7=[x for x in deps if x.get("upstream")=="WB07" and x.get("downstream")=="WB08" and x.get("critical")]
  if not d7 or any(x.get("state") not in ("PASS","REUSE") for x in d7):e.append("WB08 requires WB07 ready dependency")
  aps=L(d,"approval-register.yaml").get("approvals",[])
  if not any(a.get("requested_by")=="WB08" and a.get("action")=="PRODUCTION_DEPLOYMENT" and a.get("scope")==t.get("scope") and a.get("environment")=="PRODUCTION" and a.get("state")=="APPROVED" and a.get("evidence_ref") and "WB08" in a.get("consumed_by",[]) for a in aps):e.append("WB08 requires scope-matched explicit production approval")
for x in deps:
 if x.get("critical") and x.get("state") in ("BLOCKED","FAILED","WAITING_DEPENDENCY"):
  if any(t.get("node")==x.get("downstream") and t.get("action")=="RUN" for t in routes):e.append(f"{x.get('dependency_id')}: critical dependency bypass")
fails=L(d,"failure-register.yaml").get("failures",[]);rec={x.get("failure_id"):x for x in L(d,"recovery-plan.yaml").get("items",[])}
for f in fails:
 if f.get("state") in ("OPEN","FIXING","RETEST"):
  r=rec.get(f.get("failure_id"))
  if not r or r.get("correction_node")!=f.get("responsible_node") or r.get("rerun_gate")!=f.get("failed_gate"):e.append(f"{f.get('failure_id')}: recovery routed to wrong owner/gate")
  elif r.get("restart_entire_project"):e.append(f"{f.get('failure_id')}: unnecessary full-project restart")
c=L(d,"closeout.yaml")
if c.get("indexing_claimed"):e.append("orchestrator cannot claim indexing")
if c.get("ranking_claimed"):e.append("orchestrator cannot claim ranking")
if not c.get("unknown_metrics_preserved"):e.append("UNKNOWN/null must not be converted to zero")
print("SEMANTIC_ERRORS="+repr(e));raise SystemExit(1 if e else 0)
