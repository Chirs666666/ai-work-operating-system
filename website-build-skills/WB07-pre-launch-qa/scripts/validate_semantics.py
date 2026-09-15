from pathlib import Path
import yaml,sys
def L(d,n):return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]);e=[]; gate=L(d,"launch-gate.yaml"); ready=gate.get("ready_for_launch_approval")
sp=L(d,"page-sample-plan.yaml")
if ready and (not sp.get("critical_coverage_complete") or not sp.get("system_coverage_complete")):e.append("launch-ready requires complete critical/system coverage")
for p in sp.get("pages",[]):
 if ready and p.get("required") and p.get("class") in ("CRITICAL","SYSTEM") and not p.get("tested"):e.append(f"{p.get('page_id')}: required page not tested")
for u in L(d,"upstream-readiness.yaml").get("sources",[]):
 if ready and u.get("required") and u.get("state") in ("FAIL","BLOCK","UNKNOWN"):e.append(f"{u.get('source_skill')}: blocking/unready upstream state")
defs=L(d,"defect-register.yaml").get("defects",[]); ret={r.get("defect_id"):r for r in L(d,"retest-register.yaml").get("retests",[])}
risks={r.get("defect_id"):r for r in L(d,"risk-acceptance-register.yaml").get("risks",[])}
aps={a.get("approval_id"):a for a in L(d,"approval-register.yaml").get("approvals",[])}
for x in defs:
 if ready and x.get("severity")=="BLOCK" and x.get("state")!="RESOLVED":e.append(f"{x.get('defect_id')}: unresolved BLOCK")
 if ready and x.get("severity")=="FAIL" and x.get("state") not in ("RESOLVED","ACCEPTED_RISK"):e.append(f"{x.get('defect_id')}: unresolved FAIL")
 if x.get("state")=="RESOLVED":
  r=ret.get(x.get("defect_id"))
  if not r or not r.get("performed") or r.get("result")!="PASS" or not r.get("evidence"):e.append(f"{x.get('defect_id')}: resolved without PASS retest evidence")
 if x.get("state")=="ACCEPTED_RISK":
  r=risks.get(x.get("defect_id")); a=aps.get(r.get("approval_id")) if r else None
  if not r or r.get("state")!="ACCEPTED" or not r.get("evidence_ref") or not a or a.get("type")!="RISK_ACCEPTANCE" or a.get("state")!="APPROVED" or not a.get("evidence_ref"):e.append(f"{x.get('defect_id')}: accepted risk lacks approval evidence")
# check-level PASS tied to a defect requires retest if defect exists
for fn in ["page-completeness-check.yaml","responsive-check.yaml","navigation-check.yaml","form-check.yaml","email-delivery-check.yaml","conversion-path-check.yaml","technical-seo-check.yaml","tracking-check.yaml","search-readiness-check.yaml","infrastructure-check.yaml","performance-check.yaml","accessibility-check.yaml","browser-check.yaml"]:
 for x in L(d,fn).get("checks",[]):
  if x.get("result")=="PASS" and x.get("defect_id"):
   r=ret.get(x.get("defect_id"))
   if not r or r.get("result")!="PASS" or not r.get("evidence"):e.append(f"{x.get('check_id')}: defect changed to PASS without retest")
# template failure must be represented as template-level defect
template_fails=[]
for fn in ["page-completeness-check.yaml","responsive-check.yaml","navigation-check.yaml","form-check.yaml"]:
 for x in L(d,fn).get("checks",[]):
  if x.get("result") in ("FAIL","BLOCK") and any(p.get("class")=="TEMPLATE_SAMPLE" and p.get("page_id")==x.get("target") for p in sp.get("pages",[])):template_fails.append(x)
for x in template_fails:
 if not any(z.get("defect_id")==x.get("defect_id") and z.get("template_level") for z in defs):e.append(f"{x.get('check_id')}: template sample failure not escalated")
accepted=sum(1 for x in defs if x.get("state")=="ACCEPTED_RISK")
if gate.get("accepted_risk_count")!=accepted:e.append("accepted-risk count mismatch; accepted risk must remain visible")
if ready and gate.get("block_count")!=0:e.append("launch-ready cannot have BLOCK count")
if ready and gate.get("fail_count")!=0:e.append("launch-ready cannot have unresolved FAIL count")
if gate.get("user_launch_approved"):e.append("WB07 cannot claim user launch approval")
if gate.get("deployed"):e.append("WB07 cannot claim deployment")
print("SEMANTIC_ERRORS="+repr(e));raise SystemExit(1 if e else 0)
