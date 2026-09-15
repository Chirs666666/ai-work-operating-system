# Read-back and QA

Every write is followed by persisted-state read-back.

## L1 Structure QA
Compare the Page Build Contract to persisted structure: required sections/order, heading hierarchy, component IDs, content slots, CTA/image/table/FAQ presence, mandatory links, template/builder, duplicate/missing components.

## L2 Visual + Responsive QA
Validate desktop, tablet, and mobile when rendering capability is available: layout, spacing, typography, alignment, overflow, image ratio/crop, button behavior, tables, stacking, breakpoints, broken components.

If required visual rendering capability is unavailable, record an explicit capability gap; do not silently omit QA.

## L3 Content Integrity QA
Compare persisted content with approved 05/06/08/09/17 artifacts: text meaning, numeric values/units, headings, CTA text/destination, image assignment/alt, internal-link anchors/URLs, SEO metadata, duplication, dropped content.
