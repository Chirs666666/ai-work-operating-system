# Component Registry

V1 has two layers.

## Global Component Registry
Defines semantic component types independent of a site or builder. Each record declares purpose, required slots, optional slots, and layout constraints.

## Project Component Registry
Defines actual site implementations: project component ID, builder, engine, template/pattern/widget identity, dependencies, verification evidence, and state.

States:
- `VERIFIED`: validated on this project; highest-confidence auto-build path.
- `AVAILABLE`: exists but is not fully verified; use only with warning and stronger QA.
- `CUSTOM_REQUIRED`: no suitable implementation exists.
- `DEPRECATED`: do not select for new builds.

Project definitions may override/extend global definitions but may not silently change the approved semantic purpose.
