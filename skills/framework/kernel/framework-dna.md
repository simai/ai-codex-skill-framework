# SIMAI Framework DNA

SIMAI Framework is a frontend-first implementation skill with source-backed validation and deterministic delivery.

Core invariants:

- Start from the narrowest useful SIMAI Framework layer: `core`, `loader`, `utilities`, `components`, `smart-components`, `blocks`.
- Treat raw HTML as render output, legacy input, or explicit exception only; SIMAI Framework source of truth should be structured content, page/section/block manifests, data bindings, design packs, smart contracts, and adapter render output.
- Keep `simai.storage`, settings, and `simai.property` in separate planes: storage owns content and site/page structure; settings own contextual characteristics and preferences; `simai.property` owns field rendering/editing and may render through SIMAI Framework smart/components.
- Model pages as ordered section calls, not copied section internals. Section definitions live in `/simai/section` and `/simai.data/section`; page calls reference `section`, `version`, `view`, and `params`.
- Model blocks as physical reusable units in `/simai/block` and `/simai.data/block`. A section definition composes blocks and maps section params to block params through bindings.
- Allow path-scoped `simai.data` overlays such as `/company/simai.data` for local section/block/design libraries. Resolve overlays from root to current route, keep deeper scopes higher priority, and include the overlay chain in compiled cache keys.
- Treat platform cache as a backend, not the SIMAI Framework cache contract. SIMAI Framework runtime should use compiled registry/page/section/block plans with explicit cache keys, tags, dependencies, invalidation, and warmup.
- For property templates or backend-generated controls, prefer this order: SIMAI Framework smart-component, SIMAI Framework component, SIMAI Framework utilities, custom layer only as an explicit framework gap.
- When SIMAI Framework output is adapted into Blade or similar PHP templates, keep templates presentation-only: markup plus ordinary output, includes, conditionals and loops. CSS/JS belongs in asset files connected through the owner asset pipeline, and data preparation, formatting, mapping, helper functions, service calls and other PHP computations belong in controllers, view models, presenters, components, services or runtime classes. Do not generate inline `<style>`, `<script>`, `@php`, raw PHP functions or calculation blocks in templates except as a documented legacy exception with owner, reason, cleanup trigger and evidence.
- Treat synced upstream `source/simai/*` repositories and vendor manifests as authoritative whenever current SIMAI Framework behavior matters.
- Keep recipes, playbooks, routing, working sets, and validation aligned with real shipped runtime and examples.
- Prefer small reversible updates to the skill over broad undocumented restructuring.
- Preserve backward compatibility in the skill unless the task explicitly allows a contract break.
- Do not bloat `SKILL.md`; move detail to the narrowest rule, specialist, activity, or reference file.
