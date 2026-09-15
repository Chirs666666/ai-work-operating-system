# Builder Adapters

Both adapters consume the same Page Build Contract and return the same normalized persisted-state/read-back semantics.

## Block Editor Adapter
Owns valid WordPress block grammar, core block mapping, optional Greenshift mapping, nested-block integrity, reusable patterns/components, responsive implementation, serialization, and stable read-back mapping.

## Elementor Adapter
Owns container hierarchy, widget mapping, project global-style use, responsive controls, template/component reuse, safe Elementor data handling, and stable read-back mapping.

## Builder preservation
Existing pages remain on their current builder. Conversion between Elementor and Block Editor requires explicit approval and is outside ordinary Draft repair.
