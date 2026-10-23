# UI Doc Atlas Usage

> Источник: github.com/simai/ui-doc (content/ru) · Проверено: 2026-10-23 · Версия: ui-doc ae2c38b8b1ab

This file describes how to use the exhaustive docs atlas resources.

## Contents

- Atlas Files
- Build/Refresh Atlas
- Query Atlas
- Recommended Retrieval Flow

## Atlas Files

- `references/ui-doc-manifest.json`:
  full machine-readable metadata for all docs pages.
- `references/ui-doc-full-map.md`:
  full grouped list of all markdown pages.
- `references/ui-doc-utility-atlas.md`:
  utility-focused atlas with extracted class tokens and playground markers.
- `references/page-recipe-routing.md`:
  prompt routing to page recipe + required utility groups.

## Build/Refresh Atlas

Run when docs snapshot changes:

```bash
skills/framework/scripts/build_ui_doc_atlas.py \
  --docs-root 'repo://ai-skill-framework/source/simai/ui-doc/content/ru' \
  --skill-root repo://ai-skill-framework/skills/framework
```

## Query Atlas

Search relevant pages before implementation:

```bash
skills/framework/scripts/query_ui_doc_manifest.py \
  --manifest repo://ai-skill-framework/skills/framework/references/ui-doc-manifest.json \
  grid container --top utilities --limit 12
```

Common filters:

- `--top utilities|start|fundamentals|reference|...`
- `--utility-group layout|grid|typography|...`

Route prompt to page recipe:

```bash
skills/framework/scripts/recommend_page_recipe.py \
  --manifest repo://ai-skill-framework/skills/framework/references/ui-doc-manifest.json \
  'Сверстай checkout: форма клиента, доставка, оплата, summary, валидация'
```

Generate page scaffold from recipe:

```bash
skills/framework/scripts/generate_page_scaffold.py \
  --type landing --theme light --title "My Landing" --out /tmp/landing.html
```

Generate component/smart/block scaffold:

```bash
skills/framework/scripts/generate_component_scaffold.py --kind component --name productCard --title "Product card" --snippet-only
skills/framework/scripts/generate_component_scaffold.py --kind smart --name catalogCards --title "Catalog cards" --smart-code cards --snippet-only
skills/framework/scripts/generate_component_scaffold.py --kind block --name catalogSection --title "Catalog section" --snippet-only
```

Validate recipe classes against docs manifest:

```bash
skills/framework/scripts/validate_page_recipes.py --strict
```

Validate strict vendor compatibility:

```bash
skills/framework/scripts/validate_page_recipes.py --strict --catalog-strict
skills/framework/scripts/validate_page_recipes.py --strict --catalog-strict --recipes-glob skills/framework/references/component-template.md
skills/framework/scripts/validate_page_recipes.py --strict --catalog-strict --recipes-glob skills/framework/references/smart-component-template.md
skills/framework/scripts/validate_page_recipes.py --strict --catalog-strict --recipes-glob skills/framework/references/block-template.md
```

Validate real HTML/PHP templates and generated snippets:

```bash
skills/framework/scripts/validate_framework_html_files.py --strict --catalog-strict /tmp/landing.html
skills/framework/scripts/validate_framework_html_files.py --strict --catalog-strict \
  --glob "/path/to/templates/**/*.html" \
  --glob "/path/to/templates/**/*.php"
```

Run all local checks in one command:

```bash
skills/framework/scripts/run_local_checks.sh
```

Install pre-commit hook for automatic SIMAI Framework checks:

```bash
skills/framework/scripts/install_pre_commit_hook.sh
```

## Recommended Retrieval Flow

1. Query manifest by task keywords.
2. For page tasks, route prompt with `recommend_page_recipe.py`.
3. Open top result pages and validate against `project-conventions.md`.
4. Cross-check final class choices in `ui-doc-utility-atlas.md`.
5. Implement and verify with `page-layout-playbook.md`.
