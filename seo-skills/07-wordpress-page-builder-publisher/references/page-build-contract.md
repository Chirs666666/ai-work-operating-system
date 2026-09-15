# Page Build Contract

The Page Build Contract is the builder-agnostic execution interface between approved upstream decisions and 07.

It must preserve:
- page identity/type/status/build mode;
- stable semantic `section_id` values;
- semantic component type plus selected project `component_id`;
- approved content values and provenance;
- asset/link bindings and provenance;
- required/optional slot expectations;
- desktop/tablet/mobile layout intent;
- upstream artifact references;
- existing builder identity for existing pages.

Builder-specific block markup, Elementor JSON, REST payloads, credentials, or browser selectors do not belong in this contract.
