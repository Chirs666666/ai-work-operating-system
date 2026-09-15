from pathlib import Path
import sys,json
try: import yaml
except ImportError: yaml=None
EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL=['manifest', 'campaign-brief', 'target-page-readiness', 'prospect-source-register', 'prospect-inventory', 'prospect-qualification', 'competitor-link-opportunities', 'link-opportunity-map', 'anchor-target-plan', 'contact-register', 'outreach-strategy', 'outreach-drafts', 'outreach-queue', 'paid-placement-review', 'risk-register', 'live-link-register', 'link-verification-report', 'campaign-performance', 'cross-skill-handoffs', 'change-control', 'closeout']
REFS=['boundaries-and-ownership.md', 'target-page-readiness.md', 'prospect-discovery.md', 'prospect-qualification.md', 'authority-metrics.md', 'opportunity-types.md', 'anchor-policy.md', 'contact-data.md', 'outreach-policy.md', 'paid-placement-and-risk.md', 'competitor-backlink-policy.md', 'link-verification.md', 'campaign-prioritization.md', 'tool-routing.md', 'canonical-outputs.md']
EXAMPLES=['target-ready', 'target-not-ready', 'qualified-high', 'qualified-medium', 'rejected-spam', 'missing-metrics', 'competitor-requalification', 'natural-anchor', 'paid-placement', 'high-risk-scheme', 'public-contact', 'outreach-queue', 'live-link', 'removed-link']
def main():
 r=Path(sys.argv[1]); e=[]
 for x in EXPECTED_ROOT:
  if not (r/x).exists(): e.append("missing:"+x)
 for x in REFS:
  if not (r/"references"/x).exists(): e.append("missing reference:"+x)
 if not (r/"schemas"/"common.schema.json").exists(): e.append("missing schema:common")
 for x in CANONICAL:
  if not (r/"schemas"/f"{x}.schema.json").exists(): e.append("missing schema:"+x)
  if not (r/"templates"/f"{x}.yaml").exists(): e.append("missing template:"+x)
 for x in EXAMPLES:
  if not (r/"examples"/x).is_dir(): e.append("missing example:"+x)
 for p in (r/"schemas").glob("*.json"):
  try: json.loads(p.read_text())
  except Exception as z: e.append(f"bad json:{p.name}:{z}")
 if yaml:
  for p in (r/"templates").glob("*.yaml"):
   try: yaml.safe_load(p.read_text())
   except Exception as z: e.append(f"bad yaml:{p.name}:{z}")
 print("VERIFICATION_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
