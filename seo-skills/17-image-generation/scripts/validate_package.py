from pathlib import Path
import sys
EXPECTED_ROOT={"SKILL.md","README.md","VERSION","CHANGELOG.md","ACCEPTANCE.md","references","schemas","templates","examples","scripts"}
CANONICAL=['manifest', 'image-brief', 'source-register', 'truth-boundary', 'image-type', 'dimension-spec', 'prompt-contract', 'edit-contract', 'technical-fact-register', 'composition-spec', 'brand-style-spec', 'generation-record', 'edit-record', 'technical-accuracy-review', 'visual-quality-review', 'text-data-review', 'image-seo', 'accessibility-review', 'asset-export-spec', 'cross-skill-handoffs', 'change-control', 'verification-report', 'closeout']
REFS=['boundaries-and-ownership.md', 'data-provenance.md', 'image-requirement-method.md', 'image-type-classification.md', 'truth-and-evidence-boundary.md', 'prompt-contract.md', 'edit-contract.md', 'technical-diagram-policy.md', 'product-accuracy-policy.md', 'industrial-scene-policy.md', 'dimensions-and-cropping.md', 'brand-visual-consistency.md', 'text-and-data-in-images.md', 'image-seo.md', 'accessibility-alt-text.md', 'quality-assurance.md', 'wordpress-handoff.md', 'canonical-outputs.md']
EXAMPLES=['article-hero', 'standard-1280x720', 'banner-1900x550', 'product-edit', 'color-variation', 'background-replacement', 'enhancement', 'technical-diagram', 'conceptual-factory', 'process-visual', 'calculator-visual', 'missing-source', 'unsupported-dimensions', 'text-data-validation', 'seo-asset', 'reuse', 'verify']
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
 print("VERIFICATION_ERRORS="+repr(e)); return 1 if e else 0
if __name__=="__main__": raise SystemExit(main())
