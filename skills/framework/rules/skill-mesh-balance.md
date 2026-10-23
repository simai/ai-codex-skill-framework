# Skill Mesh Balance

`$framework` owns SIMAI Framework frontend-first contracts: core, loader,
utilities, components, smart-components, blocks, source refresh, recipe
scaffolds, working-set generation, validation surfaces, and SIMAI Framework implementation
patterns for Bitrix/Laravel alignment.

## Does Not Own

- Larena platform/package lifecycle owned by `$larena`.
- Bitrix/SF4/OrgPortal facts owned by their domain skills.
- General repository delivery owned by `$dev`.
- Documentation methodology/content owned by `$docs`.
- UX design decisions owned by `$ux`.
- SEO Contract decisions owned by `$marketing`.
- QA evidence owned by `$tester`.
- Runtime/deploy incidents owned by `$ops`.

## Companion Contracts

- Use `$larena` when SIMAI Framework work touches Larena packages, admin, installer/update,
  or registration flows.
- Use `$bitrix`, `$sf4`, or `$orgportal` when SIMAI Framework contracts must align with
  those platforms.
- Use `$ux` and `$marketing` as contract owners for interface and public/search
  surfaces.
- Use `$docs` for substantial documentation and `$tester` for validation
  evidence.
- For SF4 -> SIMAI Framework, Bitrix -> SIMAI Framework, Larena/SIMAI Framework, or other reference-adaptive work,
  `$framework` owns target frontend adaptation: loader/runtime, components,
  smart-components, blocks, layout contracts, utilities, recipes, and generated
  working-set artifacts. `$tester` owns invariant evidence and verdict; source
  platform skills own the reference behavior.

## Handoff

Return SIMAI Framework layers/surfaces touched, source/recipe/working-set paths, generated
artifacts, validation commands, compatibility constraints, blockers, and the
companion owner expected to review.

For reference-adaptive handoff, also return target behavior, allowed SIMAI Framework
adaptations, source/recipe mapping, already-working baseline, do-not-break list,
and regression checks after fix.
