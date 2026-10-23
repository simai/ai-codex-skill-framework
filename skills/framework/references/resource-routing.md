# Resource Routing

> Источник: repo://ai-skill-framework/skills/framework · Проверено: 2026-10-23 · Версия: снимок источников 2026-10-23 (ui 3d9bf903a590, ui-source aa81305b14f1)

Exhaustive map of SIMAI Framework references, knowledge packs and scripts. Load
narrowly: pick the entry for the current activity, not the whole list.
Activities live in [activity-registry.json](../activities/activity-registry.json);
specialist profiles live in `specialists/<id>/profile.md`.

## Specialists

| Id | Focus |
|---|---|
| `task-goal` | goal, `Done when`, scope control, remaining work |
| `source-sync` | source mirrors, inventory, upstream drift, source-backed truth |
| `routing-orchestrator` | scenarios, recipe routing, playbook routing, fixtures |
| `recipe-scaffold` | page recipes, generators, starter templates |
| `working-set` | bundle generation, section variants, upstream extraction |
| `tailwind-converter` | Tailwind CSS to SIMAI Framework conversion, mapping quality, unmapped token reports |
| `validation-qa` | validators, regression fixtures, strict local checks |
| `bitrix-integration` | Bitrix installable usage, local asset packaging, `sfPath`/`sfSmartPath` wiring, admin/public demo surfaces, storage-safe deployment |
| `docs-learning` | references, indexes, usage facts, narrow learning updates; writing method with `$docs` |
| `skill-maintainer` | coordinator architecture, metadata, folder structure |

## Scope, conventions, sources

- `references/frontend.md` first: scope, source map, global rules.
- `references/project-conventions.md`: team naming, layout, compatibility.
- `references/source-repositories.md`: model ui-source (editable) → ui (generated release),
  trust order, snapshot refresh.
- `references/framework-family.md`: ui-control hub and task cycle, component packages
  (SIMAI Pro `sf-table`/`sf-admin-menu` in `ui-pro`), products ui-admin, ui-chat,
  ui-mail, larena-ui, licences.
- `references/source-inventory.md`: shipped coverage and runnable examples.
- `scripts/sync_source_repos.py`: sync the ignored mirror in `source/simai/`;
  then `scripts/build_source_inventory.py` and `scripts/build_component_smart_catalog.py`.
- Topic truth in source mirrors:
  - `source/simai/ui-doc/content/ru` docs pages;
  - `source/simai/ui-play/examples` runnable examples;
  - `source/simai/ui/distr/component` shipped components;
  - `source/simai/ui/distr/smart` shipped Smart Components (`ui-smart` is archived);
  - `source/simai/ui/distr/utility` shipped utility groups;
  - `source/simai/ui-source/src/utility` utility source, rule and state semantics.
- Vendor data is the truth for strict class/state/smart validation:
  `references/vendor/source/catalog-lite.sf-only.json`,
  `references/vendor/source-repos.json`, `references/vendor/source-inventory.json`,
  `references/vendor/manifest/framework.conditions.json`,
  `references/vendor/manifest/framework.excluded-non-sf-classes.json`,
  `references/vendor/manifest/framework.smart.json`,
  `references/vendor/registries/smart-codes.json`,
  `references/vendor/manifest/framework.tokens.sf.json`.

## Routing

- Recurring UI tasks (forms, dropdowns, overlays, pagination, uploads):
  `references/pattern-playbooks.md`, `references/pattern-routing.md`,
  `scripts/recommend_ui_pattern.py "<task>"`.
- Whole feature screens (auth, catalog, checkout, profile, dashboard):
  `references/product-scenarios.md`, `scripts/recommend_product_scenario.py "<task>"`.
- One-shot task -> scenario -> recipe -> patterns: `references/routing-overview.md`,
  `scripts/recommend_framework_route.py "<task>"`.
- Activity, specialists, knowledge packs and gates: `references/activity-routing-overview.md`,
  `scripts/recommend_framework_activity.py "<task>"`.

## Execution and working sets

- `references/execution-workflow.md`: default order from intake to validation.
- `references/task-intake-template.md`: task boundaries and acceptance criteria.
- `references/task-preparation.md`, `scripts/prepare_framework_task.py "<task>" --scaffold-out /tmp/page.html`.
- `references/working-set-generation.md`, `scripts/generate_framework_working_set.py "<task>" --out-dir /tmp/framework-task`.
- `references/working-set-coverage.md`, `scripts/build_working_set_coverage.py`;
  extend coverage via `references/vendor/working-set.section-variants.json` and
  `references/vendor/working-set.legacy-class-map.json`.
- `references/framework-fast-start.md`: connect SIMAI Framework quickly and start layout.

## Pages, components, layout

- `references/frontend-playbook.md`: deterministic implementation and review steps.
- `references/page-layout-playbook.md`: full page layouts.
- `references/page-recipes-index.md`, `references/page-recipe-routing.md`,
  `scripts/recommend_page_recipe.py`.
- `scripts/generate_page_scaffold.py --type <auth|landing|catalog|dashboard|article|checkout|profile>`.
- `references/frontend-loader.md`: SFLoader architecture, cache model, API, debug.
- `references/frontend-modifiers.md`: utility syntax, breakpoints, color roles, RTL-safe styling.
- `references/spacing-radius-pairs.md`: padding, gap, margin and radius for cards,
  panels, nested surfaces, code blocks, chips, compact controls.
- `references/frontend-components-smart.md`: components vs smart-components vs blocks.
- `references/component-smart-catalog.md`: existing shipped components and smart-components.
- Starter templates: `references/component-template.md`,
  `references/smart-component-template.md`, `references/block-template.md`;
  `scripts/generate_component_scaffold.py` for `component|smart|block`.
- `references/ux-implementation-contract.md`: when a `$ux` screen spec or UX handoff exists.

## Smart runtime and Bitrix

- `references/bitrix-ui-smart-integration.md`: SIMAI Framework UI assets in Bitrix
  modules, `sfPath`/`sfSmartPath`, Bitrix-native demo pages.
- `knowledge-packs/backend-first-smart-runtime.md`: `Smart::render()`,
  `Smart::tree()`, smart manifests/templates, composite runtime, runtime proofs.
- `knowledge-packs/smart-component-implementation.md`: backend/frontend smart
  components, especially `drawer`, `modal`, `sidebar`, `side-menu`, `top-menu`,
  `navigation-shell`.
- `knowledge-packs/demo-path-overlay-playground.md`: `/demo/framework/` or another
  demo path as a path-scoped `simai.data` overlay with composite smart artifacts.
- `references/backend-bitrix.md` and `references/backend-laravel.md`: backend planning only.

## Tailwind conversion

- `knowledge-packs/tailwind-to-framework-conversion.md` before Tailwind CSS,
  Tailwind UI or Tailwind Plus conversion.
- `scripts/run_tailwind_conversion_lab.py`: ignored `output/tailwind-to-framework-lab/` QA harness.
- `scripts/run_tailadmin_page_examples.py`: ignored
  `output/tailwind-to-framework-tailadmin-pages/` TailAdmin examples with
  source/Framework panes, conversion reports, screenshots and visual scores.
- `scripts/capture_html_screenshot.py <html> --output <png>`: Chrome/Chromium
  fallback when browser screenshot capture times out.
- `scripts/score_lab_visual.py <png>`: lightweight source/Framework similarity score.

## Documentation lookup

- `references/ui-doc-atlas-usage.md` before large lookups.
- `scripts/query_ui_doc_manifest.py` with `references/ui-doc-manifest.json` for exact pages.
- `references/ui-doc-full-map.md`, `references/ui-doc-utility-atlas.md` for exhaustive coverage;
  `references/ui-doc-curated-map.md` for original doc pages by topic.

## Validation

- `scripts/run_local_checks.sh`: full local suite, CI parity, before delivery.
- `scripts/install_pre_commit_hook.sh`: enforce local checks on commits touching `skills/framework`.
- `scripts/migrate_recipe_classes_to_vendor.py --write` normalizes legacy recipe
  classes; `--strict` detects legacy aliases in CI.
- `scripts/validate_page_recipes.py --strict` (vendor + docs manifest);
  add `--catalog-strict` for vendor-only class whitelist.
- `scripts/validate_framework_html_files.py --strict --catalog-strict <path...>` for real HTML/PHP templates.
- Templates: `scripts/validate_page_recipes.py --strict --catalog-strict --recipes-glob references/<component|smart-component|block>-template.md`.
- Standalone HTML checks: adapt `references/vendor/tools/validate-framework-html.js`
  and `references/vendor/tools/framework-lint.php`.
