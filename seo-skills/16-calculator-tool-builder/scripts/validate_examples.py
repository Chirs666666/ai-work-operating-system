from pathlib import Path
import sys,yaml
def load(p): return yaml.safe_load(p.read_text()) or {}
def main():
 root=Path(sys.argv[1]); e=[]
 for d in [p for p in root.iterdir() if p.is_dir()]:
  f={p.name:load(p) for p in d.glob("*.yaml")}
  evid={x.get("formula_id"):x for x in f.get("formula-evidence.yaml",{}).get("formulas",[])}
  for x in evid.values():
   state=x.get("formula_state")
   if state in ("UNKNOWN","UNSUPPORTED","CONFLICTING") and x.get("production_allowed") is True:
    e.append(f"{d.name}: {state} formula cannot be production_allowed")
   if state in ("VERIFIED","CONDITIONALLY_VERIFIED") and not x.get("evidence_refs"):
    e.append(f"{d.name}: verified formula needs evidence_refs")
  tests=f.get("test-results.yaml",{})
  overall=tests.get("overall_status")
  handoff=f.get("implementation-handoff.yaml",{})
  if overall in ("FAIL","BLOCKED","UNKNOWN") and handoff:
   if handoff.get("release_state")=="READY_FOR_IMPLEMENTATION" or handoff.get("tests_passed") is True:
    e.append(f"{d.name}: failed/unknown tests cannot be implementation-ready")
  if handoff:
   if handoff.get("release_state")=="READY_FOR_IMPLEMENTATION":
    if not handoff.get("formula_contract_complete"): e.append(f"{d.name}: ready handoff missing formula contract")
    if not handoff.get("tests_passed"): e.append(f"{d.name}: ready handoff tests not passed")
    if not handoff.get("frontend_contract_complete"): e.append(f"{d.name}: ready handoff frontend incomplete")
    if not handoff.get("production_formula_allowed"): e.append(f"{d.name}: ready handoff formula not production allowed")
  cc=f.get("change-control.yaml",{})
  if cc and any(cc.get(k) for k in ("formula_changed","constants_changed","units_changed","assumptions_changed","result_interpretation_changed")):
   if cc.get("revalidation_required") is not True:
    e.append(f"{d.name}: material calculation change requires revalidation")
   if cc.get("production_release_allowed") is True:
    e.append(f"{d.name}: changed formula cannot be released before revalidation")
  for v in f.get("variable-spec.yaml",{}).get("variables",[]):
   if v.get("default_value") is not None and not v.get("default_justification"):
    e.append(f"{d.name}: default value requires justification for {v.get('variable_id')}")
  us=f.get("unit-system.yaml",{})
  for c in us.get("conversions",[]):
   if c.get("tested") is not True:
    e.append(f"{d.name}: conversion {c.get('conversion_id')} must be tested")
  sec=f.get("security-safety-review.yaml",{})
  if sec and (sec.get("unsafe_eval_used") or sec.get("untrusted_formula_execution")):
    e.append(f"{d.name}: unsafe formula execution is not permitted")
 print("EXAMPLE_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
