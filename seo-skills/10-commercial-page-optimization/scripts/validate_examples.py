from pathlib import Path
import sys, yaml

def load(path):
    return yaml.safe_load(path.read_text()) or {}

def main():
    root = Path(sys.argv[1])
    errors = []
    for d in [p for p in root.iterdir() if p.is_dir()]:
        files = {p.name: load(p) for p in d.glob("*.yaml")}

        perf = files.get("performance-baseline.yaml", {})
        if perf.get("availability") == "UNKNOWN":
            for key in ("impressions","clicks","ctr","average_position","conversions"):
                if perf.get(key) == 0:
                    errors.append(f"{d.name}: UNKNOWN performance cannot use fabricated zero for {key}")

        diagnosis = files.get("page-diagnosis.yaml", {})
        if diagnosis.get("overall") == "OWNERSHIP_CONFLICT":
            if diagnosis.get("recommended_action") != "BLOCK_FOR_OWNERSHIP":
                errors.append(f"{d.name}: ownership conflict must BLOCK_FOR_OWNERSHIP")

        evidence = files.get("evidence-register.yaml", {})
        claim_states = {x.get("claim_id"): x.get("state") for x in evidence.get("claims", [])}
        revised = files.get("revised-page-copy.yaml", {})
        for section in revised.get("sections", []):
            for cid in section.get("claim_ids", []):
                if claim_states.get(cid) in ("UNSUPPORTED","CONFLICTING"):
                    errors.append(f"{d.name}: revised copy uses invalid claim {cid}")

        cc = files.get("change-control.yaml", {})
        if cc.get("risk_class") == "HIGH_IMPACT_LIVE_REWRITE" and cc.get("approval_required") is not True:
            errors.append(f"{d.name}: high-impact live rewrite requires approval")

        handoff = files.get("execution-handoff.yaml", {})
        if handoff and handoff.get("owner") != "07-wordpress-page-builder-publisher":
            errors.append(f"{d.name}: execution owner must be 07")
        if handoff and handoff.get("approval_required") is False:
            # This skill is for existing commercial pages; live writes stay approval controlled.
            ctx = files.get("page-context.yaml", {})
            if ctx.get("live_state") == "LIVE":
                errors.append(f"{d.name}: live execution cannot bypass approval")

        closeout = files.get("closeout.yaml", {})
        if closeout.get("g10") == "WAITING_APPROVAL" and closeout.get("approval_pending") is not True:
            errors.append(f"{d.name}: WAITING_APPROVAL requires approval_pending true")
        if closeout.get("final_action") == "BLOCK_FOR_OWNERSHIP":
            if "25-keyword-page-mapping" not in closeout.get("downstream_handoffs", []):
                errors.append(f"{d.name}: ownership block must hand off to 25")

        issues = files.get("issue-register.yaml", {}).get("issues", [])
        expected = {
            "METADATA":"09-seo-metadata",
            "INTERNAL_LINK":"08-internal-linking-architecture",
            "TECHNICAL_SEO":"12-technical-seo-audit-fix",
            "PAGE_SPEED":"21-page-speed-optimization",
            "OWNERSHIP":"25-keyword-page-mapping",
        }
        for issue in issues:
            cat = issue.get("category")
            if cat in expected and issue.get("owner_skill") != expected[cat]:
                errors.append(f"{d.name}: {cat} must be owned by {expected[cat]}")

        ver = files.get("verification-report.yaml", {})
        if ver.get("overall") == "VERIFIED" and ver.get("mismatches"):
            errors.append(f"{d.name}: VERIFIED cannot contain mismatches")

    print("EXAMPLE_ERRORS="+repr(errors))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
