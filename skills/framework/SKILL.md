---
name: framework
description: "SIMAI Framework: core, loader, utilities, components, smart-components, blocks. Frontend-first разработка, архитектура, паттерны, code review, план миграции, поэтапный backend для Bitrix и Laravel."
metadata:
  display-name: "SIMAI Framework"
  short-description: "SIMAI Framework workflows, architecture, frontend and component work"
---

# SIMAI Framework

`framework` owns frontend-first SIMAI Framework architecture, loader, utilities, components,
smart-components, blocks, recipes, working sets and source-backed validation.

Before substantial work load the required kernel and rules:

- [kernel/framework-dna.md](./kernel/framework-dna.md);
- [kernel/scope-contract.md](./kernel/scope-contract.md);
- [kernel/output-contract.md](./kernel/output-contract.md);
- [rules/routing.md](./rules/routing.md);
- [rules/decision-policy.md](./rules/decision-policy.md);
- [rules/change-gates.md](./rules/change-gates.md);
- [rules/skill-mesh-balance.md](./rules/skill-mesh-balance.md);
- [rules/coordinator.md](./rules/coordinator.md).

## Семейство и источники (проверено 2026-10-23)

- Правка Framework — только в `simai/ui-source`; `simai/ui` — сгенерированный
  выпуск (`distr/`, включая `distr/smart`), собирается `ui-builder`, руками не
  правится; потребители закрепляют коммит выпуска, не `main`.
- `simai/ui-smart` архивирован; `ui-loader` теперь `ui-source`.
- Треды Framework живут в `simai/ui-control`: диспетчер раскладывает цель по
  репозиториям-владельцам и принимает доказательства.
- Компоненты продуктов — пакетами у владельца: `sf-table`, `sf-data-view`,
  `sf-property-view`, `sf-admin-menu` — SIMAI Pro в `simai/ui-pro` (пакет `larena`).
- Продукты на Framework: `ui-admin`, `ui-chat`, `ui-mail`, `larena-ui`.

Подробно: [source-repositories.md](./references/source-repositories.md) и
[framework-family.md](./references/framework-family.md).

## Mirai Graph Runtime Entry

Use current graph context for capability, route, gates and evidence. Raw SIMAI Framework
sources remain authoritative; platform playbooks do not move into the central
graph. Graph-only runtime is forbidden.

Load [references/resource-routing.md](./references/resource-routing.md) for the
specialist list, source inventory, recipe/scaffold tools, Tailwind conversion,
Bitrix integration or exhaustive reference routing.

## Core Workflow

For visual product delivery, follow
[Visual product platform mapping](./references/visual-product-platform-mapping.md):
inventory exact SIMAI Framework capabilities before implementation, record
`no_fit` before creating a token/primitive/component, and never replace a
Framework target with unrelated standalone HTML.

1. Define goal, `Done When` and affected SIMAI Framework layer.
2. Select an activity from `activities/activity-registry.json`; use
   `scripts/recommend_framework_activity.py` when unclear.
3. For a new or substantially changed Component/Smart Component, execute the
   technology `technologies/component-design-evolution.json` (pick its
   scenario) and load `references/component-design-evolution.md` before
   editing implementation.
4. For non-trivial work select specialists via `rules/routing.md` and assign roles
   via `rules/specialist-engagement-model.md`; load only the selected activity,
   specialist profiles and directly required references.
5. Separate source refresh, routing, recipes and working-set changes into
   explicit batches.
6. Implement the nearest reversible slice with stated assumptions.
7. Run the selected change gates and source/route/scaffold validation.
8. Run `scripts/run_local_checks.sh` before delivery for repository-wide SIMAI Framework
   changes.
9. Update source-backed inventories/references only when their inputs changed.
10. If a reusable lesson was learned, apply `rules/learning.md` and update the
    narrowest owner.

## Layer Boundaries

- Core: contracts and cross-cutting primitives, no feature UI.
- Loader: deterministic idempotent boot and explicit module order.
- Utilities: pure/framework-agnostic helpers without hidden side effects.
- Components: presentation and local interaction.
- Smart-components: state, data and explicit side effects.
- Blocks: composition with explicit input/output and extension contracts.

Preserve backward compatibility unless explicitly waived. `marketing`, `ux`, `docs`,
`tester`, `bitrix` and `larena` retain their owner decisions; SIMAI Framework implements
them through its own surfaces.

## Fast Reference Routing

- deterministic building-block selection:
  `references/framework-contract-registry.md`;
- general frontend: `references/frontend.md`;
- execution: `references/execution-workflow.md`;
- patterns/scenarios: `references/pattern-routing.md` and
  `references/product-scenarios.md`;
- recipes: `references/page-recipe-routing.md`;
- loader/components: `references/frontend-loader.md` and
  `references/frontend-components-smart.md`;
- component and Smart Component design/evolution:
  `references/component-design-evolution.md`;
- task/working set: `scripts/prepare_framework_task.py` and
  `scripts/generate_framework_working_set.py`;
- strict HTML/recipe validation: `scripts/validate_page_recipes.py` and
  `scripts/validate_framework_html_files.py`.

## Чем навык не занимается

- не владеет репозиториями: работу в `ui-source`, `ui-admin`, `ui-chat` и др.
  организует тред репозитория (`dev`, `teamlead`), навык даёт знание и проверки;
- сценарий и структура экрана — `ux`; макет, Figma, визуальный паритет и
  оформление презентаций — `designer`;
- приложение Larena и его пакеты — `larena`; Bitrix-модули — `bitrix`;
  сайт документации на Docara — `docara`; вердикт о выпуске — `tester`;
- выпуск, push, публикация и деплой — только по подтверждённой задаче
  владельца; имена, новые пакеты и репозитории решает человек;
- правила и маршрутизация Федерации — `federation`; упорядочивание данных — `mirai`.

## Output

Return selected activity/layers, assumptions, changed source-backed artifacts,
validation/gate evidence, compatibility impact, blockers and next action.
