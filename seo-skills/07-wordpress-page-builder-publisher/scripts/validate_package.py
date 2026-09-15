from pathlib import Path
import json
import re
import sys

try:
    import yaml
except Exception as exc:
    print(f"ERROR: PyYAML required: {exc}")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
errors = []

required_files = [
    "SKILL.md", "README.md", "VERSION", "CHANGELOG.md",
    "references/boundaries-and-ownership.md",
    "references/environment-discovery.md",
    "references/component-registry.md",
    "references/compatibility-gate.md",
    "references/page-build-contract.md",
    "references/builder-adapters.md",
    "references/execution-routing.md",
    "references/readback-and-qa.md",
    "references/idempotency-and-drift.md",
    "references/permission-and-change-control.md",
    "references/error-routing.md",
    "references/canonical-outputs.md",
    "schemas/common.schema.json",
    "schemas/manifest.schema.json",
    "schemas/project-wordpress-profile.schema.json",
    "schemas/builder-capability-matrix.schema.json",
    "schemas/component-registry.schema.json",
    "schemas/component-match.schema.json",
    "schemas/page-build-contract.schema.json",
    "schemas/build-plan.schema.json",
    "schemas/execution-log.schema.json",
    "schemas/readback.schema.json",
    "schemas/qa-report.schema.json",
    "schemas/write-report.schema.json",
    "schemas/change-control.schema.json",
    "schemas/build-gaps.schema.json",
    "schemas/closeout.schema.json",
    "scripts/validate_package.py",
    "scripts/validate_examples.py",
]

canonical_templates = [
    "manifest.yaml", "project-wordpress-profile.yaml", "builder-capability-matrix.yaml",
    "component-registry.yaml", "component-match.yaml", "page-build-contract.yaml",
    "build-plan.yaml", "execution-log.yaml", "readback.yaml", "structure-qa.yaml",
    "visual-qa.yaml", "responsive-qa.yaml", "content-integrity-qa.yaml",
    "metadata-write-report.yaml", "internal-link-write-report.yaml", "asset-write-report.yaml",
    "change-control.yaml", "build-gaps.yaml", "closeout.yaml",
]
required_files.extend(f"templates/{x}" for x in canonical_templates)

example_required = [
    "examples/block-editor-product-page/page-build-contract.yaml",
    "examples/block-editor-product-page/project-wordpress-profile.yaml",
    "examples/block-editor-product-page/component-registry.yaml",
    "examples/block-editor-product-page/readback.yaml",
    "examples/block-editor-product-page/closeout.yaml",
    "examples/elementor-product-page/page-build-contract.yaml",
    "examples/elementor-product-page/project-wordpress-profile.yaml",
    "examples/elementor-product-page/component-registry.yaml",
    "examples/elementor-product-page/readback.yaml",
    "examples/elementor-product-page/closeout.yaml",
    "examples/drift-conflict/change-control.yaml",
    "examples/drift-conflict/closeout.yaml",
    "examples/publish-approval/change-control.yaml",
    "examples/publish-approval/closeout.yaml",
]
required_files.extend(example_required)

for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"missing:{rel}")

skill_path = ROOT / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""
for heading in [
    "# 1. Purpose", "# 2. Trigger", "# 3. Do Not Trigger", "# 4. Inputs",
    "# 5. Preconditions", "# 6. Workflow", "# 7. Tool Routing",
    "# 8. Decision Rules", "# 9. Quality Gates", "# 10. Outputs",
    "# 11. Handoff", "# 12. Safety / Change Control",
]:
    if heading not in skill:
        errors.append(f"missing-heading:{heading}")

# Parse schemas.
for path in sorted((ROOT / "schemas").glob("*.json")):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid-json:{path.relative_to(ROOT)}:{exc}")

# Parse YAML templates/examples.
for base in [ROOT / "templates", ROOT / "examples"]:
    if base.exists():
        for path in sorted(base.rglob("*.yaml")):
            try:
                yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"invalid-yaml:{path.relative_to(ROOT)}:{exc}")

# No placeholder terms in deliverable content except validators themselves.
placeholder_re = re.compile(r"\b(TBD|TODO|implement later)\b", re.I)
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".json"}:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    if placeholder_re.search(text):
        errors.append(f"placeholder:{path.relative_to(ROOT)}")

# Secrets: reject obvious non-null assignments in YAML/Markdown examples.
secret_patterns = [
    re.compile(r"(?im)^\s*(api_key|password|application_password|token|secret)\s*:\s*(?!null\s*$|UNKNOWN\s*$|NOT_PROVIDED\s*$|UNAVAILABLE\s*$)(\S.+)$"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._-]{12,}"),
]
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or path.name in {"validate_package.py", "validate_examples.py"}:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    for pat in secret_patterns:
        if pat.search(text):
            errors.append(f"possible-secret:{path.relative_to(ROOT)}")
            break

# Contract enum checks across YAML data.
allowed_build = {"BLOCK_EDITOR", "ELEMENTOR"}
allowed_g07 = {"PASS", "WARN", "FAIL", "BLOCK", "WAITING_APPROVAL", "REUSE"}
for path in sorted((ROOT / "templates").glob("*.yaml")) + sorted((ROOT / "examples").rglob("*.yaml")):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        continue
    if isinstance(data, dict):
        bm = data.get("build_mode")
        if bm and bm not in allowed_build:
            errors.append(f"bad-build-mode:{path.relative_to(ROOT)}:{bm}")
        page = data.get("page")
        if isinstance(page, dict) and page.get("build_mode") and page["build_mode"] not in allowed_build:
            errors.append(f"bad-build-mode:{path.relative_to(ROOT)}:{page['build_mode']}")
        g = data.get("g07")
        if g and g not in allowed_g07:
            errors.append(f"bad-g07:{path.relative_to(ROOT)}:{g}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS")
