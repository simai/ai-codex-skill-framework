# SIMAI Framework Pattern Playbooks

> Источник: github.com/simai/ui, github.com/simai/ui-play, github.com/simai/ui-doc · Проверено: 2026-10-23 · Версия: ui 3d9bf903a590, ui-play e062a00367aa, ui-doc ae2c38b8b1ab

Use this file as the entry point for recurring UI tasks that should map quickly to known SIMAI Framework markup and smart-component flows.

## When To Use

- The user wants a common UI pattern, not a full custom architecture pass.
- You need a fast answer to "static or smart?" for a typical SIMAI Framework feature.
- You want to start from real upstream examples instead of inventing markup.

## Playbooks

- `references/pattern-forms-inputs.md`
  - text inputs, textarea, mask, validation, disabled states
- `references/pattern-dropdown-selection.md`
  - select/tag dropdowns, list items, multiple selection, search/select flows
- `references/pattern-feedback-overlays.md`
  - modal, toast, tooltip, button-triggered feedback and overlays
- `references/pattern-pagination-filters.md`
  - page navigation, list paging, range filters, toggles, tag-based controls
- `references/pattern-upload-and-progress.md`
  - file upload, progress surfaces, range sliders, upload status blocks
- `references/pattern-routing.md`
  - quick routing rules and CLI helper for choosing the right playbook

## Fast Choice Rules

- Use static components when the task is mostly presentational and server-rendered markup is enough.
- Use smart-components when the feature needs instance API, dynamic insertion, event hooks, or a cleaner custom-element authoring model.
- Use utilities first for layout, spacing, typography, and responsive behavior around the component.

## Source Priority

1. `source/simai/ui-play/examples/components/*`
2. `source/simai/ui-play/examples/smart-components/*`
3. `source/simai/ui/distr/component/*`
4. `source/simai/ui/distr/smart/*`
5. `source/simai/ui-doc/content/ru` (loader and connection pages) for loader semantics

## Validation Rule

After adapting a pattern, validate the final snippet with:

```bash
python3 skills/framework/scripts/validate_framework_html_files.py --strict --catalog-strict /tmp/example.html
```
