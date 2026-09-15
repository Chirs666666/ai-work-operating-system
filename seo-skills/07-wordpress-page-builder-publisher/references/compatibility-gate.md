# Compatibility Gate

Evaluate the approved Blueprint/Page Build Contract against the Project WordPress Profile, Project Component Registry, Builder Capability Matrix, and required dependencies before any write.

Outcomes:
- `COMPATIBLE`: critical requirements can be implemented reliably.
- `PARTIAL`: only non-critical limitations remain; record warning and strengthen QA.
- `CUSTOM_COMPONENT_REQUIRED`: required component has no suitable implementation.
- `CONFLICT`: approved requirement conflicts with project capability/architecture; return to decision owner.
- `BLOCKED`: critical input, permission, dependency, or execution capability is unavailable.

Never silently substitute a different information architecture or builder to force `COMPATIBLE`.
