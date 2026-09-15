from pathlib import Path
import yaml, sys

def load(p):
    return yaml.safe_load(p.read_text()) or {}

def main():
    root=Path(sys.argv[1]); errors=[]
    for d in [x for x in root.iterdir() if x.is_dir()]:
        f={p.name:load(p) for p in d.glob("*.yaml")}
        cwv=f.get("cwv-baseline.yaml",{})
        lab=f.get("lab-baseline.yaml",{})
        close=f.get("closeout.yaml",{})
        if cwv.get("field_data_available") is False:
            for m in ("lcp","inp","cls"):
                if cwv.get(m,{}).get("value")==0:
                    errors.append(f"{d.name}: missing field {m} cannot become zero")
        if cwv.get("field_cwv_status")=="POOR" and lab.get("performance_score") is not None and lab.get("performance_score")>=90:
            if close.get("g21")=="PASS":
                errors.append(f"{d.name}: high lab score cannot override poor field CWV")
        bp=f.get("backup-change-plan.yaml",{})
        if bp.get("risky_change") is True and bp.get("live_change_requested") is True:
            if not (bp.get("backup_ready") and bp.get("rollback_ready")) and close.get("g21")!="BLOCK":
                errors.append(f"{d.name}: risky live change without backup/rollback must BLOCK")
            if bp.get("approval_required") is not True:
                errors.append(f"{d.name}: risky live change requires approval")
        rep=f.get("before-after-report.yaml",{})
        if rep:
            required = rep.get("baseline_available") and rep.get("same_url") and rep.get("same_test_type") and rep.get("same_device_profile") and rep.get("comparable_location_network")
            if not required and rep.get("comparable") is True:
                errors.append(f"{d.name}: incompatible test environments cannot be comparable")
            if rep.get("comparable") is False and rep.get("overall_verdict")=="IMPROVED":
                errors.append(f"{d.name}: non-comparable tests cannot claim improvement")
            if rep.get("functionality_status")=="FAIL" and rep.get("overall_verdict")!="FAIL":
                errors.append(f"{d.name}: faster but broken functionality must FAIL")
            if rep.get("field_result")=="IMPROVED":
                rr=f.get("retest-results.yaml",{})
                if rr and rr.get("field_retest_status")=="NOT_AVAILABLE_YET":
                    errors.append(f"{d.name}: cannot claim field improvement before field evidence exists")
        rr=f.get("retest-results.yaml",{})
        if rr.get("lab_retest_status")=="IMPROVED" and rr.get("field_retest_status")=="NOT_AVAILABLE_YET":
            # allowed only if report keeps field pending, never field improved
            if rep.get("field_result")=="IMPROVED":
                errors.append(f"{d.name}: lab retest cannot immediately prove field improvement")
    print("EXAMPLE_ERRORS="+repr(errors))
    return 1 if errors else 0

if __name__=="__main__":
    raise SystemExit(main())
