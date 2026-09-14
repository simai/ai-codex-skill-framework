---
name: framework
description: Build, refactor, and maintain SIMAI Framework projects with frontend-first workflows for core, loader, utilities, components, smart-components, and blocks. Use when tasks involve SIMAI Framework architecture decisions, implementation patterns, code reviews, migration planning, or staged backend planning for Bitrix and Laravel.
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
- [rules/skill-mesh-balance.md](./rules/skill-mesh-balance.md).

## Mirai Graph Runtime Entry

Use current graph context for capability, route, gates and evidence. Raw SIMAI Framework
sources remain authoritative; platform playbooks do not move into the central
graph. Graph-only runtime is forbidden.

Load [FULL_RUNTIME_PLAYBOOK.md](./FULL_RUNTIME_PLAYBOOK.md) for the complete
activity/specialist registry, source inventory, recipe/scaffold tools,
Tailwind conversion, Bitrix integration or exhaustive reference routing.

## Core Workflow

1. Define goal, `Done When` and affected SIMAI Framework layer.
2. Select an activity from `activities/activity-registry.json`; use
   `scripts/recommend_framework_activity.py` when unclear.
3. For a new or substantially changed Component/Smart Component, execute
   `component-design-evolution` and load
   `references/component-design-evolution.md` before editing implementation.
4. Load only the selected activity, specialist and directly required reference.
5. Separate source refresh, routing, recipes and working-set changes into
   explicit batches.
6. Implement the nearest reversible slice with stated assumptions.
7. Run the selected change gates and source/route/scaffold validation.
8. Run `scripts/run_local_checks.sh` before delivery for repository-wide SIMAI Framework
   changes.
9. Update source-backed inventories/references only when their inputs changed.

## Layer Boundaries

- Core: contracts and cross-cutting primitives, no feature UI.
- Loader: deterministic idempotent boot and explicit module order.
- Utilities: pure/framework-agnostic helpers without hidden side effects.
- Components: presentation and local interaction.
- Smart-components: state, data and explicit side effects.
- Blocks: composition with explicit input/output and extension contracts.

Preserve backward compatibility unless explicitly waived. `seo`, `ux`, `docs`,
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

## Output

Return selected activity/layers, assumptions, changed source-backed artifacts,
validation/gate evidence, compatibility impact, blockers and next action.
