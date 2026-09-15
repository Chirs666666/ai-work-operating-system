from pathlib import Path
import sys,json
try: import yaml
except ImportError: yaml=None
EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL=['manifest', 'audit-scope', 'source-register', 'url-inventory', 'crawl-summary', 'issue-register', 'broken-link-report', 'redirect-audit', 'canonical-audit', 'robots-indexability-audit', 'sitemap-audit', 'crawlability-audit', 'hreflang-audit', 'structured-data-audit', 'root-cause-analysis', 'remediation-plan', 'safe-fix-queue', 'approval-queue', 'cross-skill-handoffs', 'execution-log', 'verification-report', 'closeout']
REFS=['boundaries-and-ownership.md', 'issue-taxonomy.md', 'broken-link-policy.md', 'redirect-policy.md', 'canonical-policy.md', 'robots-indexability.md', 'sitemap-policy.md', 'crawlability-and-orphans.md', 'hreflang-policy.md', 'structured-data-policy.md', 'root-cause-and-remediation.md', 'change-control.md', 'verification-policy.md', 'tool-routing.md', 'canonical-outputs.md']
EXAMPLES=['broken-internal-link', 'broken-external-link', 'redirect-chain', 'redirect-loop', 'canonical-conflict', 'unexpected-noindex', 'robots-block', 'sitemap-errors', 'ownership-block', 'orphan-handoff', 'hreflang-error', 'structured-data-error', 'safe-fix', 'live-approval', 'verify-fixed', 'verify-failed']
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
