from pathlib import Path
import sys

try:
    import yaml
except Exception as exc:
    print(f"ERROR: PyYAML required: {exc}")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
errors = []


def load(rel):
    p = ROOT / rel
    if not p.exists():
        errors.append(f"missing:{rel}")
        return {}
    try:
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        errors.append(f"invalid-yaml:{rel}:{exc}")
        return {}


def validate_contract(rel, expected_builder):
    data = load(rel)
    page = data.get("page", {})
    if page.get("build_mode") != expected_builder:
        errors.append(f"builder:{rel}:{page.get('build_mode')}")
    if page.get("build_mode") not in {"BLOCK_EDITOR", "ELEMENTOR"}:
        errors.append(f"unsupported-builder:{rel}")
    sections = data.get("sections", [])
    ids = []
    for sec in sections:
        sid = sec.get("section_id")
        if not sid:
            errors.append(f"missing-section-id:{rel}")
        elif sid in ids:
            errors.append(f"duplicate-section-id:{rel}:{sid}")
        ids.append(sid)
        comp = sec.get("component", {})
        if not comp.get("component_id"):
            errors.append(f"missing-component-id:{rel}:{sid}")
        if comp.get("state") not in {"VERIFIED", "AVAILABLE", "CUSTOM_REQUIRED", "DEPRECATED"}:
            errors.append(f"bad-component-state:{rel}:{sid}")
        layout = sec.get("layout", {})
        for bp in ["desktop", "tablet", "mobile"]:
            if not layout.get(bp):
                errors.append(f"missing-layout:{rel}:{sid}:{bp}")
    if not data.get("provenance"):
        errors.append(f"missing-provenance:{rel}")
    return data


def validate_readback(rel, expected_builder):
    data = load(rel)
    for key in ["readback_id", "page_id", "status", "build_mode", "sections", "metadata", "links", "media", "read_at"]:
        if key not in data:
            errors.append(f"missing-readback-field:{rel}:{key}")
    if data.get("build_mode") != expected_builder:
        errors.append(f"readback-builder:{rel}:{data.get('build_mode')}")
    return data


def validate_closeout(rel):
    data = load(rel)
    g = data.get("g07")
    if g not in {"PASS", "WARN", "FAIL", "BLOCK", "WAITING_APPROVAL", "REUSE"}:
        errors.append(f"bad-g07:{rel}:{g}")
    goal = data.get("task_goal")
    approval = data.get("approval_status")
    done = bool(data.get("done"))
    post = bool(data.get("post_write_readback_complete"))
    if goal in {"PUBLISH", "LIVE_UPDATE", "DELETE", "BULK_CHANGE"}:
        if approval != "APPROVED" and g != "WAITING_APPROVAL" and not (goal in {"DELETE", "BULK_CHANGE"} and g == "BLOCK"):
            errors.append(f"high-impact-without-approval-gate:{rel}")
        if done and (approval != "APPROVED" or not post):
            errors.append(f"done-without-approved-post-readback:{rel}")
    return data

block_contract = validate_contract("examples/block-editor-product-page/page-build-contract.yaml", "BLOCK_EDITOR")
block_rb = validate_readback("examples/block-editor-product-page/readback.yaml", "BLOCK_EDITOR")
block_close = validate_closeout("examples/block-editor-product-page/closeout.yaml")

el_contract = validate_contract("examples/elementor-product-page/page-build-contract.yaml", "ELEMENTOR")
el_rb = validate_readback("examples/elementor-product-page/readback.yaml", "ELEMENTOR")
el_close = validate_closeout("examples/elementor-product-page/closeout.yaml")

# Content integrity proof for critical numeric example.
try:
    expected = block_contract["sections"][0]["content"]["repeatability"]["value"]
    actual = block_rb["sections"][0]["content"]["repeatability"]
    if expected != actual:
        errors.append(f"content-integrity:block-repeatability:{expected}!={actual}")
except Exception:
    errors.append("content-integrity:block-repeatability:missing")

try:
    expected = el_contract["sections"][0]["content"]["repeatability"]["value"]
    actual = el_rb["sections"][0]["content"]["repeatability"]
    if expected != actual:
        errors.append(f"content-integrity:elementor-repeatability:{expected}!={actual}")
except Exception:
    errors.append("content-integrity:elementor-repeatability:missing")

# Drift conflict must block.
drift = load("examples/drift-conflict/change-control.yaml")
drift_close = validate_closeout("examples/drift-conflict/closeout.yaml")
if drift.get("drift_state") != "CONFLICTING_DRIFT":
    errors.append("drift-example:not-conflicting")
if drift_close.get("g07") != "BLOCK":
    errors.append("drift-example:not-blocked")

# Publish approval pending example must wait.
pub = load("examples/publish-approval/change-control.yaml")
pub_close = validate_closeout("examples/publish-approval/closeout.yaml")
if pub.get("approval_status") != "PENDING":
    errors.append("publish-example:approval-not-pending")
if pub_close.get("g07") != "WAITING_APPROVAL":
    errors.append("publish-example:not-waiting")
if pub_close.get("done"):
    errors.append("publish-example:done-while-pending")


# Approved publish may complete only with post-publish read-back.
approved = load("examples/publish-approval/approved-change-control.yaml")
approved_close = validate_closeout("examples/publish-approval/approved-closeout.yaml")
if approved.get("approval_status") != "APPROVED":
    errors.append("approved-publish-example:not-approved")
if approved_close.get("task_goal") != "PUBLISH" or not approved_close.get("post_write_readback_complete") or not approved_close.get("done"):
    errors.append("approved-publish-example:completion-invalid")

# A transport success is not accepted as proof of G07 PASS: examples include persisted readback.
for name, rb, close in [("block", block_rb, block_close), ("elementor", el_rb, el_close)]:
    if close.get("g07") == "PASS" and not rb.get("readback_id"):
        errors.append(f"pass-without-readback:{name}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS")
