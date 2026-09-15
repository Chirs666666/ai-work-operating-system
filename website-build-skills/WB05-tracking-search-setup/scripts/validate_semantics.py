from pathlib import Path
import yaml,sys
def L(d,n):return yaml.safe_load((d/n).read_text()) or {}
d=Path(sys.argv[1]); e=[]; c=L(d,"closeout.yaml"); ready=c.get("ready_for_prelaunch")
ga=L(d,"ga4-property.yaml")
if ready and (not ga.get("measurement_id") or ga.get("state")!="VERIFIED" or not ga.get("evidence")): e.append("prelaunch-ready requires evidence-backed verified GA4 identity")
for x in L(d,"tracking-ownership.yaml").get("capabilities",[]):
 if len(x.get("active_paths",[]))>1 and not x.get("resolution"): e.append(f"{x.get('capability')}: duplicate active tracking paths unresolved")
 if x.get("conflict") and ready: e.append(f"{x.get('capability')}: tracking ownership conflict blocks readiness")
ev=L(d,"event-register.yaml").get("events",[])
if len([x.get("event_name") for x in ev])!=len(set(x.get("event_name") for x in ev)): e.append("duplicate event names")
cv=L(d,"conversion-register.yaml").get("conversions",[])
keys=[x.get("trigger_key") for x in cv]
if len(keys)!=len(set(keys)): e.append("duplicate conversion trigger")
receipts={x.get("event_name"):x for x in L(d,"data-receipt-verification.yaml").get("events",[])}
for x in ev:
 if x.get("state")=="VERIFIED":
  r=receipts.get(x.get("event_name"))
  if not r or not r.get("received") or not r.get("receipt_evidence") or r.get("state")!="VERIFIED": e.append(f"{x.get('event_name')}: VERIFIED without destination receipt evidence")
g=L(d,"gsc-property.yaml"); gv=L(d,"gsc-verification.yaml")
if ready and g.get("required") and (not gv.get("verified") or gv.get("state")!="VERIFIED" or not gv.get("evidence")): e.append("required GSC property not evidence-verified")
s=L(d,"sitemap-submission.yaml")
if s.get("indexed_claim"): e.append("sitemap submission/acceptance cannot claim indexing")
ix=L(d,"indexnow-setup.yaml")
if ix.get("indexed_claim"): e.append("IndexNow submission/receipt cannot claim indexing")
for x in L(d,"search-platform-register.yaml").get("platforms",[]):
 if x.get("indexed_claim") and x.get("submission_state") in ("SUBMITTED","RECEIVED"): e.append(f"{x.get('platform')}: submission state cannot prove indexing")
for x in L(d,"privacy-pii-check.yaml").get("parameters",[]):
 if x.get("classification")=="PII" and x.get("allowed"): e.append(f"{x.get('event_name')}.{x.get('parameter')}: raw PII cannot be allowed")
 if x.get("classification")=="UNKNOWN" and x.get("allowed"): e.append(f"{x.get('event_name')}.{x.get('parameter')}: unknown privacy classification cannot be allowed")
aps={a.get("approval_id"):a for a in L(d,"approval-register.yaml").get("approvals",[])}
for x in L(d,"tag-installation-register.yaml").get("tags",[]):
 if x.get("environment")=="PRODUCTION" and x.get("state")=="VERIFIED" and not x.get("evidence"): e.append(f"{x.get('tag_id')}: production verified state lacks evidence")
print("SEMANTIC_ERRORS="+repr(e)); raise SystemExit(1 if e else 0)
