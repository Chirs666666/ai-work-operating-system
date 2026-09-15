# Environment Discovery

Before the first build on a project, establish a Project WordPress Profile. Reuse it only while material dependencies remain valid.

## Discover
Record, when available: WordPress version, environment identity, theme/child theme, default builder, Gutenberg capability, Greenshift, Elementor/Pro, SEO plugin, fonts, colors, widths, spacing, radius conventions, breakpoints, reusable templates/components, and relevant dependencies.

## Reuse / refresh
- `CURRENT`: safe to reuse.
- `PROFILE_STALE`: theme, builder, plugin, global style, template, environment, or another material dependency changed; refresh before build.
- Unknown critical environment facts may block writes but should not be fabricated.

Do not expose licenses, tokens, passwords, or other secrets while detecting capability.
